# NIEM Preset

Adds NIEM exchange guidance to Spec Kit's core, assess, and bugfix processes:
verified component reuse, explicit versions, traceable mappings, and honest
conformance evidence. Experimental; not an official NIEMOpen product.

## Install

In an initialized **Spec Kit >= 1.0.4** project with an established constitution:

```bash
specify extension add assess
specify extension add bug
specify preset add --from https://github.com/mnriem/spec-kit-presets/releases/download/niem-v1.0.1/niem.zip
```

Skip `extension add` for extensions already installed; enable them if disabled.
Reload your agent's skills after installation. Missing extensions are not
installed automatically.

## Try the Resource-Request Example

Copy these prompts into Copilot skills mode **one at a time**.
Other integrations may use dotted names, such as `/speckit.specify`.

`specify` takes a feature description and creates `spec.md`. This example uses
the pinned [NIEM 6.0 PS02 Core model](https://raw.githubusercontent.com/NIEMOpen/niem-model/d6e74ac2edf30f5096973c25dbf3c13555466582/xsd/niem-core.xsd);
use your approved baseline for a real exchange.

```text
/speckit-specify Build an offline supply-request exchange between a city emergency office and a warehouse. Requests contain an ID, item name, and whole-number quantity from 1 to 10000. Preserve values in both directions, reject invalid requests clearly, and include regression tests. No server, UI, or database.
/speckit-plan Use Python 3.11+ standard library and JSON/XML. Use the linked NIEM 6.0 PS02 Core source to verify ItemName and ItemQuantity mappings. Use a clearly local request envelope. Record formal conformance checks as not run unless actually executed.
/speckit-tasks
/speckit-implement
/speckit-converge
```

**Expect:** `spec.md`, `plan.md`, `research.md`, `data-model.md`, `contracts/`,
`quickstart.md`, and `tasks.md` in the feature directory, followed by the converter
and regression tests. Mappings identify source components, namespace URIs,
constraints, and local extensions. Missing required evidence blocks dependent work.
If converge adds remaining tasks, repeat implement and converge.

## Assess an Idea First

Optional when you have not decided whether NIEM fits:

```text
/speckit-assess-intake Evaluate NIEM for supply requests exchanged between a city emergency office and a warehouse. slug=resource-request
/speckit-assess-research slug=resource-request
/speckit-assess-define slug=resource-request
/speckit-assess-shape slug=resource-request
/speckit-assess-decide slug=resource-request
```

**Expect:** artifacts under `.specify/assessments/resource-request/`, ending in
`decision.md` with `go`, `needs-clarification`, or `kill`. For `go`, use its handoff
summary as your `specify` input. NIEM adoption is not a predetermined outcome.

## Fix an Existing Exchange

Replace this example report with a defect you have actually reproduced:

```text
/speckit-bug-assess The exchange rejects quantity 10000 although the limit is inclusive; the maximum-quantity test reproduces it. Preserve the current NIEM version. slug=quantity-upper-bound
/speckit-bug-fix slug=quantity-upper-bound
/speckit-bug-test slug=quantity-upper-bound
```

**Expect:** `assessment.md`, `fix.md`, and `test.md` under
`.specify/bugs/quantity-upper-bound/`. Assessment leaves source unchanged; fix is
surgical; verification reruns the reproduction. No automatic NIEM migration.

## Important

The preset wraps 18 commands and provides 7 templates. It does not install
validators, certify output, or rewrite existing artifacts on installation.
Passing round-trip tests is not NIEM conformance. See [shared guidance and
sources](templates/niem-guidance.md) and the [mapping template](templates/niem-mapping-template.md).

Higher-priority replacements can hide its guidance. Inspect with
`specify preset resolve speckit.plan`.

## Development

From an initialized consumer project, install local edits with
`specify preset add --dev /path/to/spec-kit-presets/niem`.
Remove and reinstall after editing; `--dev` copies files.

From this repository's root, using a Python environment with supported
`specify-cli` installed and `zip` available:

```bash
python -m unittest discover -s niem/tests -p 'test_niem_preset.py'
```

Tests are excluded from release ZIPs. License: [MIT](LICENSE); referenced NIEM resources
retain their own licenses.
