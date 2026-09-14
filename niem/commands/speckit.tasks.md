> **NIEM preset:** Before executing this command, read
> `.specify/presets/niem/templates/niem-guidance.md`; stop and report its path if
> unavailable. Apply the NIEM guidance below within the existing stage, not after
> completion. Preserve all base prerequisites, paths, permissions, hooks, and approvals.

{CORE_TEMPLATE}

## NIEM Task Guidance

- Use the composed task template. Map exchange requirements and design decisions
  to existing story phases and populate the NIEM coverage table with task IDs.
- Decompose only approved work: model/source preparation, verified component
  mappings, justified extensions, message schemas, producer/consumer
  transformations, evidence, and documentation as required by the spec and plan.
- Preserve the base test-selection rules. Include test tasks when the feature
  specification requests them or the user requests TDD; identify missing required
  acceptance evidence without silently broadening the approved scope.
- Make schema/model dependencies explicit before code binding or serialization
  tasks. Shared namespaces and schema files are not independent parallel work.
- Preserve task IDs, checkbox syntax, story labels, concrete file paths, and
  dependency ordering. Separate producing a draft from executing its required
  checks; neither task may claim the other is complete.
- Do not repair unresolved model decisions by inventing components or expanding
  into an unapproved migration. Report the prerequisite decision instead.
