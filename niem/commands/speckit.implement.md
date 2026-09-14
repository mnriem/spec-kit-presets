> **NIEM preset:** Before executing this command, read
> `.specify/presets/niem/templates/niem-guidance.md`; stop and report its path if
> unavailable. Apply the NIEM guidance below within the existing stage, not after
> completion. Preserve all base prerequisites, paths, permissions, hooks, and approvals.

{CORE_TEMPLATE}

## NIEM Implementation Guidance

- Implement the approved tasks, mappings, and exchange contracts using their
  selected model/rule versions. Do not replace an established baseline with a
  newer release or introduce unplanned domains, extensions, or message formats.
- Resolve unverified mapping dependencies before implementing affected tasks.
  Report unavailable source artifacts or tools explicitly; do not substitute
  plausible component names or unchecked generated schemas.
- Use project-approved generation and validation tools only within the task's
  authorization. Preserve local artifact provenance and distinguish generated
  code from maintained sources.
- Exercise the checks required by the tasks and acceptance criteria. Separate
  model/NDR, schema/message, business-rule, and producer/consumer evidence,
  including negative cases and compatibility where specified.
- Record actual command/tool versions, inputs, results, and unexecuted checks in
  the planned evidence destinations. Never infer full conformance from one
  passing check or an agent-generated draft.
- Preserve the read-only checklist gate and task-completion rules. An incomplete
  required check leaves its task incomplete; do not mark reviewer-owned
  checklists or conceal a blocker to report success.
