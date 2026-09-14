> **NIEM preset:** Before executing this command, read
> `.specify/presets/niem/templates/niem-guidance.md`; stop and report its path if
> unavailable. Apply the NIEM guidance below within the existing stage, not after
> completion. Preserve all base prerequisites, paths, permissions, hooks, and approvals.

{CORE_TEMPLATE}

## NIEM Checklist Guidance

- Use the composed checklist template to generate requirements-quality questions,
  not a schema-validation or implementation-verification procedure.
- Check whether exchange meaning, participants, scope, compatibility obligations,
  invalid/unsupported information behavior, and acceptance evidence are defined
  clearly and consistently.
- For design-focused review, ask whether mapping provenance, namespace/version
  choices, extension rationale, and applicable conformance targets are specified.
  Do not demand design details in a business-only specification.
- Retain the base question budget, item IDs, scope/depth selection, and traceability
  references. Generate only relevant questions rather than a generic NIEM audit.
- Leave generated items unchecked and preserve reviewer ownership. Do not run
  tools, certify artifacts, or mark a requirement satisfied because a validator
  happened to pass.
