> **NIEM preset — shape.** Before starting the base stage, read the installed `.specify/presets/niem/templates/niem-guidance.md`, respecting the base path-safety rules. If it is unavailable, unreadable, or unsafe to read, report that and stop. The stage-specific NIEM guidance below applies **WITHIN the existing stage**, not as an extra phase or after completion. Retain all base prerequisites, permissions, paths, output contracts, hooks, and human approvals. Apply NIEM guidance only to relevant, in-scope information exchanges; do not broaden scope or force NIEM on unrelated work.

---

{CORE_TEMPLATE}

---

## NIEM guidance within shape

- Keep the required `problem.md` gate and shape only the defined problem. In `concept.md`, retain 2–3 distinct concept-level options, including the smallest thing that could work and, where relevant, do nothing/buy. NIEM reuse, a non-NIEM approach, and recommending `none` are legitimate outcomes where the actual constraints permit; this preset is not evidence for selecting NIEM.
- Compare options on demonstrated semantic reuse potential, partner interoperability, compatibility burden, governance/ownership, validation effort, and adoption cost. Fit these into the existing **Sketch**, **Appetite**, **Trade-offs**, and **Rabbit holes** fields. Keep appetite `small | medium | large` a budget rather than an invented estimate.
- For a NIEM option, preserve the explicit existing legacy target; use 6.0 only as the baseline when none is specified. Describe exchange boundaries and reuse/extension trade-offs at concept level. Keep XSD/CMF model representations distinct from XML/JSON message formats without designing either; do not produce implementation schemas, architecture, field mappings, APIs, or tasks.
- Base any named reuse capability on authoritative pinned model-source evidence already gathered. Keep unsupported matches **unverified mapping candidates** and material gaps in **Assumptions to Validate**. Do not invent components or namespace URIs. A possible locally governed extension is not an official NIEM domain or addition to Core, and missing evidence does not justify duplicating known reusable semantics.
- Tie the recommendation to the problem's goals and metrics, retain explicit **Out of Scope** boundaries, and acknowledge uncertainty rather than claiming NIEM conformance or a passed machine check. A recommendation is not the `decide` verdict; preserve the base artifact structure and handoff to that stage without starting specification.
