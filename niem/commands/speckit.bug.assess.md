> **NIEM preset — bug assessment.** Before starting the base stage, read the installed `.specify/presets/niem/templates/niem-guidance.md`, respecting the base path-safety rules. If it is unavailable, unreadable, or unsafe to read, report that and stop. The stage-specific NIEM guidance below applies **WITHIN the existing stage**, not as an extra phase or after completion. Retain all base prerequisites, permissions, paths, output contracts, hooks, and human approvals. Apply NIEM guidance only to relevant, in-scope information exchanges; do not broaden scope or force NIEM on unrelated work.

---

{CORE_TEMPLATE}

---

## NIEM guidance within bug assessment

- Remain read-only with respect to source code, schemas, model files, and fixtures: inspect the report and codebase, then write only the base assessment report. Do not apply fixes, migrate versions, generate replacement schemas, or alter mappings during triage.
- In the existing **Symptom**, **Reproduction**, and **Suspected Code Paths** sections, distinguish exchange semantics/model defects from serialization, validation, and application behavior. Record expected versus observed behavior, actual supporting evidence, and whether reproduction was performed; unknown steps remain `[NEEDS CLARIFICATION: …]`.
- Identify the project's actual NIEM version and pinned model source, affected namespace URI/local name, relevant definitions/constraints, and partner compatibility obligations where evidenced. Honor an explicit legacy target; NIEM 6.0 is only the default baseline when unspecified, not a reason to classify legacy behavior as a bug. Separate XSD/CMF model representations from XML/JSON message formats.
- Ground NIEM-specific root-cause claims in authoritative pinned model-source evidence and the applicable rules. The [official Model 6.0](https://docs.oasis-open.org/niemopen/niem-model/v6.0/os/niem-model-v6.0-os.html) and [NDR 6.0](https://docs.oasis-open.org/niemopen/ndr/v6.0/ndr-v6.0.html) ground 6.0 principles, not legacy behavior or component existence by themselves. Their presence here grants no extra fetch permission: retain the base URL trust/consent rules and record inaccessible evidence as a gap. Label unsupported matches **unverified mapping candidates**; do not invent components, namespaces, or conformance results.
- Propose the smallest evidence-supported remediation and regression checks in **Proposed Remediation**, with compatibility/data-loss risks in **Risks & Considerations**. Reuse the correct established semantics before proposing a justified local extension; such an extension is not official NIEM Core or a domain. Keep unneeded NIEM adoption and migrations out of scope.
- Retain `valid | likely valid, needs reproduction | invalid`, severity `critical | high | medium | low`, root-cause confidence, all assessment sections, and the base slug/next-step report. A schema-only validation pass cannot establish complete NIEM conformance or invalidate an evidenced semantic defect.
