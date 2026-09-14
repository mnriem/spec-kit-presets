> **NIEM preset — intake.** Before starting the base stage, read the installed `.specify/presets/niem/templates/niem-guidance.md`, respecting the base path-safety rules. If it is unavailable, unreadable, or unsafe to read, report that and stop. The stage-specific NIEM guidance below applies **WITHIN the existing stage**, not as an extra phase or after completion. Retain all base prerequisites, permissions, paths, output contracts, hooks, and human approvals. Apply NIEM guidance only to relevant, in-scope information exchanges; do not broaden scope or force NIEM on unrelated work.

---

{CORE_TEMPLATE}

---

## NIEM guidance within intake

- Capture, do not evaluate: in the existing `intake.md` sections, faithfully record the proposed exchange, its origin, affected producers/consumers if supplied, and the stated interoperability need. Keep proposals to adopt NIEM distinct from existing requirements. Do not decide whether NIEM is suitable, research mappings, recommend an approach, or generate schemas.
- Record any explicitly supplied NIEM version, model source, namespace, exchange constraints, or legacy compatibility requirement as supplied context, not independently verified fact. NIEM 6.0 is the preset baseline for later consideration when no target is specified; an explicit existing legacy target is honored, not silently upgraded.
- Put missing exchange context, target-version evidence, and claims of required NIEM adoption in **First-Glance Unknowns** using `[NEEDS CLARIFICATION: …]`. Preserve the distinction between model representations (XSD/CMF) and message formats (XML/JSON) when those are mentioned; do not choose either here.
- A supplied component mapping without authoritative pinned model-source evidence remains an **unverified mapping candidate**. Do not invent components or namespace URIs, label local extension proposals as official NIEM Core/domains, or treat a stakeholder's conformance claim as a passed machine check.
- Leave adoption open: the captured idea may later support NIEM, a non-NIEM approach, or doing nothing. Preserve the base idea-type vocabulary, intake artifact structure, slug reporting, overwrite approvals, and suggested next stage.
