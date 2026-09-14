> **NIEM preset:** Before executing this command, read
> `.specify/presets/niem/templates/niem-guidance.md`; stop and report its path if
> unavailable. Apply the NIEM guidance below within the existing stage, not after
> completion. Preserve all base prerequisites, paths, permissions, hooks, and approvals.

{CORE_TEMPLATE}

## NIEM Issue Handoff Guidance

- Convert only existing tasks. Preserve canonical task IDs, deduplication,
  dependencies, and the base command's repository/remote restrictions.
- Carry relevant requirement IDs, mapping/contract references, selected model
  baseline, and task-specific evidence expectations into issue descriptions.
  Keep draft, unverified, and blocked qualifications intact.
- Link to approved artifacts rather than copying entire reference models or
  sensitive sample messages into issues. Respect publication permissions.
- Do not add model-design tasks, change the target NIEM version, claim checks
  passed, or submit upstream NIEM contributions as a side effect of handoff.
