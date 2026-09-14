> **NIEM preset — define.** Before starting the base stage, read the installed `.specify/presets/niem/templates/niem-guidance.md`, respecting the base path-safety rules. If it is unavailable, unreadable, or unsafe to read, report that and stop. The stage-specific NIEM guidance below applies **WITHIN the existing stage**, not as an extra phase or after completion. Retain all base prerequisites, permissions, paths, output contracts, hooks, and human approvals. Apply NIEM guidance only to relevant, in-scope information exchanges; do not broaden scope or force NIEM on unrelated work.

---

{CORE_TEMPLATE}

---

## NIEM guidance within define

- Frame the underlying problem in `problem.md`: who needs to exchange or interpret information, what currently fails, and the observable consequences. An input such as “adopt NIEM” is not itself a problem statement. Do not choose NIEM, map fields, design a data model, or generate schemas here.
- Carry forward confirmed partner obligations and existing NIEM/legacy-version compatibility constraints as requirements, citing the inputs. Keep preferences, assumptions, and proposals separate. NIEM 6.0 is the preset baseline if later NIEM work has no explicit target; it does not establish a mandate or replace a declared legacy target.
- Use **Goals**, **Non-Goals**, and **Success Metrics** to express bounded interoperability outcomes such as fewer semantic misunderstandings or reduced partner onboarding effort, only where supported. Mark missing baselines, users, ownership, and targets `[NEEDS CLARIFICATION: …]`; do not invent measurements or make adoption itself evidence of success.
- Preserve the cost-of-inaction comparison and room for non-NIEM or do-nothing outcomes. Keep unrelated storage, UI, and internal processing outside NIEM scope unless the evidence makes them part of the problem. Do not confuse XSD/CMF model representation choices with XML/JSON message-format requirements.
- Carry missing authoritative pinned model-source evidence and **unverified mapping candidates** into **Open Questions** only when material to defining the problem, not as new mappings. Do not invent official components/namespaces, promote local extension proposals to official NIEM Core/domains, or report conformance from prose. Preserve the base direct-input entry path, skipped-stage recording, artifact structure, open-question count, and next-stage report.
