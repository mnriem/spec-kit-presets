"""NIEM preset contract checks using a supported Spec Kit installation."""

import importlib.metadata
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import warnings
import zipfile
from pathlib import Path

import yaml
from packaging.specifiers import SpecifierSet

from specify_cli import _locate_core_pack, _repo_root
from specify_cli.extensions import ExtensionManifest
from specify_cli.presets import PresetManager, PresetManifest, PresetResolver


PRESET = Path(__file__).resolve().parents[1]
ROOT = PRESET.parent
SHARED_GUIDANCE = ".specify/presets/niem/templates/niem-guidance.md"
CORE_TEMPLATES = {
    "spec-template",
    "plan-template",
    "tasks-template",
    "checklist-template",
    "constitution-template",
}


def split_frontmatter(text):
    if not text.startswith("---\n"):
        return {}, text
    header, separator, body = text[4:].partition("\n---\n")
    if not separator:
        raise ValueError("Unclosed command frontmatter")
    return yaml.safe_load(header), body


class NiemPresetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = PresetManifest(PRESET / "preset.yml")
        cls.entries = cls.manifest.templates
        cls.commands = [entry for entry in cls.entries if entry["type"] == "command"]
        core_pack = _locate_core_pack()
        assets = core_pack if core_pack is not None else _repo_root()
        cls.templates = assets / "templates"
        cls.core_commands = assets / "commands" if core_pack else cls.templates / "commands"
        cls.extensions = assets / "extensions"
        cls.scripts = assets / "scripts"
        cls.extension_ids = [entry["id"] for entry in cls.manifest.requires_extensions]

    def make_project(self, skills=False, extensions=True):
        temporary = tempfile.TemporaryDirectory(prefix="niem-preset-test-")
        self.addCleanup(temporary.cleanup)
        project = Path(temporary.name)
        specify = project / ".specify"
        shutil.copytree(self.templates, specify / "templates")
        shutil.copytree(
            self.core_commands, specify / "templates" / "commands", dirs_exist_ok=True
        )
        if extensions:
            for extension_id in self.extension_ids:
                shutil.copytree(
                    self.extensions / extension_id,
                    specify / "extensions" / extension_id,
                )
        (specify / "init-options.json").write_text(
            json.dumps({"ai": "copilot", "ai_skills": skills, "script": "py"}),
            encoding="utf-8",
        )
        target = project / ".github" / ("skills" if skills else "agents")
        target.mkdir(parents=True)
        inactive = project / ".claude" / "commands"
        inactive.mkdir(parents=True)
        (inactive / "sentinel.md").write_text("Leave inactive integration alone.\n")
        memory = specify / "memory"
        memory.mkdir()
        (memory / "constitution.md").write_text("# Authored project constitution\n")
        return project

    def install(self, project, source=PRESET):
        manager = PresetManager(project)
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            manager.install_from_directory(source, "1.0.4")
        self.assertEqual([], [str(warning.message) for warning in caught])
        return manager

    def test_manifest_catalog_and_files_agree(self):
        catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
        entry = catalog["presets"]["niem"]
        self.assertEqual("niem", self.manifest.id)
        for field in ("id", "name", "version", "description", "author", "license"):
            self.assertEqual(self.manifest.data["preset"][field], entry[field])
        self.assertEqual(self.manifest.data["requires"], entry["requires"])
        self.assertEqual(self.manifest.tags, entry["tags"])
        for kind, count in (("template", 7), ("command", 18)):
            self.assertEqual(count, sum(item["type"] == kind for item in self.entries))
            self.assertEqual(count, entry["provides"][f"{kind}s"])
        declared = {entry["file"] for entry in self.entries}
        actual = {
            str(path.relative_to(PRESET))
            for folder in ("commands", "templates")
            for path in (PRESET / folder).glob("*.md")
        }
        self.assertEqual(declared, actual)
        for relative in declared:
            with self.subTest(file=relative):
                self.assertTrue((PRESET / relative).read_text(encoding="utf-8").strip())
        self.assertIn(
            f"/niem-v{self.manifest.version}/niem.zip", entry["download_url"]
        )

    def test_all_core_and_extension_commands_are_wrapped(self):
        expected = {
            f"speckit.{path.stem}" for path in self.core_commands.glob("*.md")
        }
        for extension_id in self.extension_ids:
            manifest = ExtensionManifest(
                self.extensions / extension_id / "extension.yml"
            )
            expected.update(command["name"] for command in manifest.commands)
        self.assertEqual(expected, {entry["name"] for entry in self.commands})
        for entry in self.commands:
            with self.subTest(command=entry["name"]):
                text = (PRESET / entry["file"]).read_text(encoding="utf-8")
                self.assertEqual("wrap", entry["strategy"])
                self.assertEqual(1, text.count("{CORE_TEMPLATE}"))
                self.assertIn(SHARED_GUIDANCE, text.partition("{CORE_TEMPLATE}")[0])
                self.assertFalse(text.startswith("---\n"))

    def test_readme_invocations_are_declared(self):
        readme = (PRESET / "README.md").read_text(encoding="utf-8")
        documented = set(re.findall(r"/(speckit-[a-z-]+)", readme))
        declared = {entry["name"].replace(".", "-") for entry in self.commands}
        self.assertTrue(documented)
        self.assertLessEqual(documented, declared)

    def test_every_layer_composes_without_losing_base_contract(self):
        project = self.make_project()
        resolver = PresetResolver(project)
        bases = {
            (entry["name"], entry["type"]): resolver.resolve_content(
                entry["name"], entry["type"]
            )
            for entry in self.entries
        }
        manager = self.install(project)
        self.assertEqual([], manager.find_unmet_extension_dependencies(self.manifest))
        resolver = PresetResolver(project)
        for entry in self.entries:
            with self.subTest(name=entry["name"]):
                raw = (PRESET / entry["file"]).read_text(encoding="utf-8")
                resolved = resolver.resolve_content(entry["name"], entry["type"])
                self.assertIsNotNone(resolved)
                self.assertNotIn("{CORE_TEMPLATE}", resolved)
                base = bases[(entry["name"], entry["type"])]
                if entry["type"] == "command":
                    self.assertIsNotNone(base)
                    base_metadata, base_body = split_frontmatter(base)
                    metadata, body = split_frontmatter(resolved)
                    self.assertEqual(base_metadata, metadata)
                    self.assertIn(base_body.strip(), body)
                elif entry["name"] in CORE_TEMPLATES:
                    self.assertEqual("append", entry["strategy"])
                    self.assertEqual(base + "\n\n" + raw, resolved)
                else:
                    self.assertEqual(raw, resolved)
        self.assertTrue((project / SHARED_GUIDANCE).is_file())

    def test_install_and_remove_in_command_and_skills_modes(self):
        for skills in (False, True):
            with self.subTest(skills=skills):
                project = self.make_project(skills=skills)
                manager = self.install(project)
                rendered = []
                for entry in self.commands:
                    name = entry["name"]
                    if skills:
                        path = (
                            project / ".github" / "skills"
                            / name.replace(".", "-") / "SKILL.md"
                        )
                    else:
                        path = project / ".github" / "agents" / f"{name}.agent.md"
                    self.assertTrue(path.is_file(), str(path))
                    rendered.append(path)
                    text = path.read_text(encoding="utf-8")
                    self.assertIn(SHARED_GUIDANCE, text)
                    self.assertNotIn("{CORE_TEMPLATE}", text)
                    self.assertNotIn("{SCRIPT}", text)
                    for reference in re.findall(
                        r"\.specify/presets/niem/templates/[a-z-]+\.md", text
                    ):
                        self.assertTrue((project / reference).is_file(), reference)
                inactive = project / ".claude" / "commands"
                self.assertEqual(["sentinel.md"], sorted(p.name for p in inactive.iterdir()))
                other_mode = project / ".github" / ("agents" if skills else "skills")
                self.assertFalse(other_mode.exists())
                self.assertTrue(manager.remove("niem"))
                self.assertFalse((project / ".specify" / "presets" / "niem").exists())
                for path in rendered:
                    if path.exists():
                        self.assertNotIn(SHARED_GUIDANCE, path.read_text(encoding="utf-8"))
                self.assertEqual(
                    "# Authored project constitution\n",
                    (project / ".specify" / "memory" / "constitution.md").read_text(),
                )

    def test_missing_extension_bases_warn_without_fake_commands(self):
        project = self.make_project(extensions=False)
        manager = PresetManager(project)
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            manager.install_from_directory(PRESET, "1.0.4")
        self.assertTrue(any("no base" in str(w.message).lower() for w in caught))
        self.assertEqual(
            {"assess", "bug"},
            {entry["id"] for entry in manager.find_unmet_extension_dependencies(self.manifest)},
        )
        resolver = PresetResolver(project)
        for entry in self.commands:
            if entry["name"].count(".") > 1:
                self.assertIsNone(resolver.resolve_content(entry["name"], "command"))
                self.assertFalse(
                    (project / ".github" / "agents" / f"{entry['name']}.agent.md").exists()
                )
        self.assertIn(
            SHARED_GUIDANCE, resolver.resolve_content("speckit.specify", "command")
        )

    def test_template_helper_returns_full_spec_content(self):
        project = self.make_project()
        self.install(project)
        scripts = project / ".specify" / "scripts" / "python"
        shutil.copytree(self.scripts / "python", scripts)
        result = subprocess.run(
            [sys.executable, str(scripts / "resolve_template.py"), "spec-template", "--json"],
            cwd=project,
            capture_output=True,
            text=True,
            check=True,
        )
        payload = json.loads(result.stdout)
        self.assertIn("# Feature Specification:", payload["TEMPLATE_CONTENT"])
        self.assertIn("## NIEM Exchange Requirements", payload["TEMPLATE_CONTENT"])
        self.assertEqual(
            PresetResolver(project).resolve_content("spec-template"),
            payload["TEMPLATE_CONTENT"],
        )

    def test_stacking_preserves_both_assess_wrappers(self):
        for niem_priority, questions_priority in ((5, 10), (10, 5)):
            with self.subTest(niem_priority=niem_priority):
                project = self.make_project()
                manager = PresetManager(project)
                manager.install_from_directory(
                    ROOT / "assess-ask-questions", "1.0.4", priority=questions_priority
                )
                manager.install_from_directory(
                    PRESET, "1.0.4", priority=niem_priority
                )
                resolver = PresetResolver(project)
                for entry in self.commands:
                    if entry["name"].startswith("speckit.assess."):
                        text = resolver.resolve_content(entry["name"], "command")
                        self.assertIn(SHARED_GUIDANCE, text)
                        self.assertIn("Clarifying Questions Protocol", text)
                        self.assertNotIn("{CORE_TEMPLATE}", text)

    def test_release_archive_installs(self):
        project = self.make_project()
        archive = project / "niem.zip"
        subprocess.run(
            ["zip", "-qr", str(archive), ".", "-x", ".*", "__pycache__/*", "tests/*"],
            cwd=PRESET,
            capture_output=True,
            text=True,
            check=True,
        )
        with zipfile.ZipFile(archive) as package:
            self.assertIn("preset.yml", package.namelist())
            self.assertFalse(any(name.startswith("tests/") for name in package.namelist()))
            self.assertNotIn("DEMO.md", package.namelist())
        manager = PresetManager(project)
        installed = manager.install_from_zip(archive, "1.0.4")
        self.assertEqual("niem", installed.id)
        self.assertTrue((project / SHARED_GUIDANCE).is_file())
        self.assertIn(
            SHARED_GUIDANCE,
            PresetResolver(project).resolve_content("speckit.bug.fix", "command"),
        )


class NiemCliSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        manifest = PresetManifest(PRESET / "preset.yml")
        try:
            installed = importlib.metadata.version("specify-cli")
        except importlib.metadata.PackageNotFoundError:
            raise unittest.SkipTest("CLI smoke test requires installed specify-cli metadata")
        if installed not in SpecifierSet(manifest.requires_speckit_version):
            raise unittest.SkipTest(
                f"CLI smoke test needs specify-cli {manifest.requires_speckit_version}; "
                f"this interpreter's installed distribution is {installed}"
            )

    def test_real_cli_initialization_and_template_resolution(self):
        script_types = ["py"]
        if shutil.which("bash"):
            script_types.append("sh")
        for script_type in script_types:
            with self.subTest(script_type=script_type):
                with tempfile.TemporaryDirectory(prefix="niem-cli-demo-") as directory:
                    parent = Path(directory)
                    project = parent / "exchange-demo"
                    env = {
                        **os.environ,
                        "PATH": str(Path(sys.executable).parent) + os.pathsep
                        + os.environ.get("PATH", ""),
                        "PYTHONDONTWRITEBYTECODE": "1",
                    }
                    cli = [sys.executable, "-c", "from specify_cli import main; main()"]

                    def run(arguments, cwd=project):
                        result = subprocess.run(
                            arguments, cwd=cwd, env=env, capture_output=True, text=True,
                            input="", timeout=120,
                        )
                        self.assertEqual(
                            0, result.returncode, result.stdout + result.stderr
                        )
                        return result.stdout

                    run(
                        cli + [
                            "init", "exchange-demo", "--integration", "copilot",
                            "--integration-options=--skills", "--script", script_type,
                            "--ignore-agent-tools",
                        ],
                        cwd=parent,
                    )
                    constitution = project / ".specify" / "memory" / "constitution.md"
                    original_constitution = constitution.read_bytes()
                    for extension_id in ("assess", "bug"):
                        run(cli + ["extension", "add", extension_id])
                    run(cli + ["preset", "add", "--dev", str(PRESET)])
                    self.assertEqual(original_constitution, constitution.read_bytes())
                    for name in (
                        "speckit-specify", "speckit-assess-research", "speckit-bug-fix"
                    ):
                        text = (
                            project / ".github" / "skills" / name / "SKILL.md"
                        ).read_text(encoding="utf-8")
                        self.assertIn(SHARED_GUIDANCE, text)
                        self.assertNotIn("{CORE_TEMPLATE}", text)
                    if script_type == "sh":
                        resolver = [
                            "bash", ".specify/scripts/bash/resolve-template.sh",
                            "spec-template", "--json",
                        ]
                    else:
                        resolver = [
                            sys.executable, ".specify/scripts/python/resolve_template.py",
                            "spec-template", "--json",
                        ]
                    payload = json.loads(run(resolver))
                    self.assertIn("# Feature Specification:", payload["TEMPLATE_CONTENT"])
                    self.assertIn(
                        "## NIEM Exchange Requirements", payload["TEMPLATE_CONTENT"]
                    )
                    run(cli + ["preset", "remove", "niem"])
                    text = (
                        project / ".github" / "skills" / "speckit-specify" / "SKILL.md"
                    ).read_text(encoding="utf-8")
                    self.assertNotIn(SHARED_GUIDANCE, text)


if __name__ == "__main__":
    unittest.main()
