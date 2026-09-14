> **NIEM preset — bug verification.** Before starting the base stage, read the installed `.specify/presets/niem/templates/niem-guidance.md`, respecting the base path-safety rules. If it is unavailable, unreadable, or unsafe to read, report that and stop. The stage-specific NIEM guidance below applies **WITHIN the existing stage**, not as an extra phase or after completion. Retain all base prerequisites, permissions, paths, output contracts, hooks, and human approvals. Apply NIEM guidance only to relevant, in-scope information exchanges; do not broaden scope or force NIEM on unrelated work.

---

{CORE_TEMPLATE}

---

## NIEM guidance within bug verification

- Require and read both `assessment.md` and `fix.md`. Validate the recorded fix without modifying source code, schemas, model files, or fixtures; write only the base verification report. Do not repair failures or generate new implementations during this stage.
- Re-run the actual reproduction or its automated equivalent, the added/updated tests, and relevant regression checks. For affected NIEM exchange behavior, include checks of business semantics, compatibility, and the applicable model/message constraints that the assessment and fix require. Do not force unrelated NIEM checks or expand the patch's scope.
- Validate against the actual pinned model source, rule revision, and declared target, honoring explicit legacy versions rather than substituting the preset's 6.0 baseline. Record model/rule provenance and validator/tool versions with the relevant checks so results are reproducible. Unsupported component matches remain **unverified mapping candidates** and residual risks, never invented official components/namespaces or proof that local extensions are official Core/domains.
- Separate XSD/CMF model-level checks from XML/JSON message-format/instance checks and application/semantic regression tests. An XSD or JSON Schema pass demonstrates only what that check covers; it does not establish complete NIEM Model/NDR conformance, correct reuse, or business meaning. Do not claim unexecuted machine checks passed based on documentation review.
- In the existing **Checks Performed** and **Output Excerpts**, capture actual command/action, exit status, and concise evidence. Use `pass | fail | skipped | not-run` as applicable; missing tooling is `not-run`, and destructive, network-dependent, or expensive checks remain `skipped` without explicit consent. Document uncovered constraints and environments in **Residual Risks**.
- Retain exactly `verified | partial | failed`: `verified` requires all critical checks to pass and the original symptom no longer to reproduce; missing reproduction or inconclusive critical coverage is `partial`, not success. A reproduced symptom or regression caused by the fix is `failed`. A bug may be verified within its stated scope without certifying all NIEM conformance; state that boundary. Preserve report sections, overwrite approval, slug reporting, and the base recommendation to reassess a failed fix.
