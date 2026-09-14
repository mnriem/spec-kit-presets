> **NIEM preset — research.** Before starting the base stage, read the installed `.specify/presets/niem/templates/niem-guidance.md`, respecting the base path-safety rules. If it is unavailable, unreadable, or unsafe to read, report that and stop. The stage-specific NIEM guidance below applies **WITHIN the existing stage**, not as an extra phase or after completion. Retain all base prerequisites, permissions, paths, output contracts, hooks, and human approvals. Apply NIEM guidance only to relevant, in-scope information exchanges; do not broaden scope or force NIEM on unrelated work.

---

{CORE_TEMPLATE}

---

## NIEM guidance within research

- Investigate whether the recorded problem benefits from shared exchange semantics at all. Weigh NIEM reuse against existing contracts, non-NIEM alternatives, partner capabilities, and the cost of doing nothing. Keep **Evidence Against the Idea** even when findings favor NIEM; do not decide adoption or produce implementation schemas.
- Use NIEM 6.0 as the research baseline only when no explicit target exists; honor a declared legacy target and investigate its actual model and rules rather than assuming 6.0 identifiers or compatibility. Ground 6.0 principles in the [official NIEM Model 6.0](https://docs.oasis-open.org/niemopen/niem-model/v6.0/os/niem-model-v6.0-os.html) and [NDR 6.0](https://docs.oasis-open.org/niemopen/ndr/v6.0/ndr-v6.0.html), recording the revision consulted. These references do not expand the base URL allowlist or authorize fetching, redirects, linked downloads, or bypassing consent/connection safety.
- For any cited reuse candidate, record authoritative, pinned model-source evidence: release/tag/commit or digest, source location, namespace URI and local name, definition, and relevant structural constraints. Official prose establishes principles, not proof that a particular component exists or fits. If evidence cannot be inspected under the base permissions, label the item **unverified mapping candidate**, mark unsourced claims `ASSUMPTION`, and record the gap rather than inventing a mapping or namespace.
- Research reuse by business meaning before proposing new local vocabulary. Document a suspected reuse gap as a finding, not a design; local extension proposals are not official NIEM Core or domains. Distinguish XSD/CMF model representations from XML/JSON message formats and investigate only those relevant to the idea.
- Fit findings into the existing `research.md` lenses, **Data & Constraints**, **Gaps & Open Questions**, and **Sources**. Retain `high | medium | low` confidence and `cited` versus `assumption` evidence labels, sanitized-source/policy records, and the base next-stage report. Research confidence is not machine conformance, and a schema-validation claim alone is not complete NIEM conformance.
