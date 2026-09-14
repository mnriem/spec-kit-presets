> **NIEM preset — bug fix.** Before starting the base stage, read the installed `.specify/presets/niem/templates/niem-guidance.md`, respecting the base path-safety rules. If it is unavailable, unreadable, or unsafe to read, report that and stop. The stage-specific NIEM guidance below applies **WITHIN the existing stage**, not as an extra phase or after completion. Retain all base prerequisites, permissions, paths, output contracts, hooks, and human approvals. Apply NIEM guidance only to relevant, in-scope information exchanges; do not broaden scope or force NIEM on unrelated work.

---

{CORE_TEMPLATE}

---

## NIEM guidance within bug fix

- Treat `assessment.md` as the unchanged contract: preserve its preferred remediation, listed files, tests, and risks. Retain the 3–6 bullet plan confirmation, stop for `invalid`, and preserve the interactive approval/automated stop for `likely valid, needs reproduction` with unresolved clarification items.
- Apply a surgical compatibility patch, not opportunistic NIEM adoption, model redesign, namespace renaming, dependency changes, or migration. Honor the existing pinned NIEM/legacy target and partner contracts; the 6.0 baseline for unspecified targets is not permission to upgrade. If missing target/source evidence blocks a safe patch, record the blocker rather than guess.
- For affected mappings, use authoritative pinned model-source evidence to verify namespace URI/local name, business meaning, and relevant structural constraints. Preserve existing supported semantics and reuse. Never invent official components or namespace URIs, change official model semantics to fit local data, or ship an **unverified mapping candidate** as an established mapping. Any assessment-authorized local extension remains explicitly local, not official NIEM Core or a domain.
- Keep XSD/CMF model representations distinct from XML/JSON message formats. Update only the assessment-authorized artifacts needed for the defect and compatibility behavior; do not generate extra formats or rewrite unaffected exchange content. Add the specified regression coverage for the original symptom and relevant semantic/format behavior.
- If evidence requires a scope expansion, log it explicitly; if the root cause or assessment proves wrong, stop modifying code and use **Deviations from Assessment** to recommend reassessment. Do not edit `assessment.md`, delete unapproved files, or silently weaken validation to make tests pass.
- In `fix.md`, retain `applied | partial | not-applied`, the existing sections, actual local commands/results, deviations, and follow-ups. Separate implemented changes from unrun checks; prose review or a schema pass is not complete NIEM conformance. Preserve consent for destructive/network-dependent checks and the base handoff to bug testing.
