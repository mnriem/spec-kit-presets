> **NIEM preset:** Before executing this command, read
> `.specify/presets/niem/templates/niem-guidance.md`; stop and report its path if
> unavailable. Apply the NIEM guidance below within the existing stage, not after
> completion. Preserve all base prerequisites, paths, permissions, hooks, and approvals.

{CORE_TEMPLATE}

## NIEM Planning Guidance

- Fill the composed plan's NIEM design section for exchanges in scope. Confirm
  the model baseline, applicable NDR edition/targets, domains, and partner
  compatibility constraints before claiming a complete mapping.
- During research, inspect approved authoritative model artifacts. Document
  provenance, semantic reuse candidates, rejected alternatives, and gaps in
  `research.md`; unavailable sources are explicit unresolved evidence.
- During design, read
  `.specify/presets/niem/templates/niem-mapping-template.md` and use it within
  `data-model.md`. Stop and report a missing mapping template. Verify namespace
  URIs, definitions, types, cardinalities, code lists, and extension rationale.
- Use `contracts/` for exchange requirements and design-level message/schema
  contracts. Distinguish the semantic model (XSD/CMF) from XML/JSON message
  formats. Label unvalidated schema drafts and do not generate application code.
- Define checks and expected positive/negative outcomes required by the approved
  spec/constitution, including the limits of each conformance claim. Record
  prerequisites and invocations in `quickstart.md`; verify tool capabilities
  before prescribing them, without installing or executing them here.
- Apply the normal planning gates to unresolved mappings and compatibility
  decisions. End at design; do not create `tasks.md` or execute implementation.
