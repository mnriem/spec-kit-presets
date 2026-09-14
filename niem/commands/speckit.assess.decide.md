> **NIEM preset — decide.** Before starting the base stage, read the installed `.specify/presets/niem/templates/niem-guidance.md`, respecting the base path-safety rules. If it is unavailable, unreadable, or unsafe to read, report that and stop. The stage-specific NIEM guidance below applies **WITHIN the existing stage**, not as an extra phase or after completion. Retain all base prerequisites, permissions, paths, output contracts, hooks, and human approvals. Apply NIEM guidance only to relevant, in-scope information exchanges; do not broaden scope or force NIEM on unrelated work.

---

{CORE_TEMPLATE}

---

## NIEM guidance within decide

- Judge the idea and its recommended concept, not compliance with a preset preference. NIEM adoption is neither an automatic `go` nor a prerequisite for one; a justified non-NIEM approach or closing the idea may be appropriate. Respect established partner obligations and the defined scope rather than imposing NIEM on unrelated work.
- Use the existing six-criterion scorecard and `strong | adequate | weak | unknown` ratings. Weigh NIEM reuse evidence, partner readiness, version compatibility, governance, and unresolved mapping risks within the relevant criteria; do not add an independent adoption/conformance gate or invent evidence.
- Preserve exactly `go | needs-clarification | kill`. A `go` still requires problem validity and evidence strength at least `adequate`, plus a recommended shaped concept. Missing `problem.md` stops the stage; missing `concept.md` prevents `go`. When material NIEM unknowns block the decision, identify the specific question and `intake | research | define | shape` stage to revisit rather than preemptively approving adoption.
- Distinguish authoritative pinned model-source evidence from **unverified mapping candidates** in the rationale. Do not infer component existence, namespace ownership, or conformance from names or prose. Local extension proposals remain locally governed, not official NIEM Core/domains; no assessment verdict certifies machine conformance.
- For `go` only, carry the chosen approach, bounded exchange scope, evidence references, compatibility constraints, and remaining questions into the existing handoff fields of `decision.md`. Preserve any explicit legacy target; 6.0 is only the baseline for otherwise unspecified NIEM work. Keep model representation (XSD/CMF) distinct from message format (XML/JSON) if relevant. Do not design schemas, start implementation, or execute the downstream specification stage here. Retain the base report and verdict-specific next step.
