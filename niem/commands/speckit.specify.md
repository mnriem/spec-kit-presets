> **NIEM preset:** Before executing this command, read
> `.specify/presets/niem/templates/niem-guidance.md`; stop and report its path if
> unavailable. Apply the NIEM guidance below within the existing stage, not after
> completion. Preserve all base prerequisites, paths, permissions, hooks, and approvals.

{CORE_TEMPLATE}

## NIEM Specification Guidance

- During the base template-loading step, obtain the full composed spec template,
  not just the top file path printed by `specify preset resolve`. Use the
  installed resolver matching the project's selected script type:
  - `sh`: `.specify/scripts/bash/resolve-template.sh spec-template --json`
  - `ps`: `.specify/scripts/powershell/resolve-template.ps1 spec-template -Json`
  - `py`: `.specify/scripts/python/resolve_template.py spec-template --json`
  Invoke it through the appropriate shell/interpreter as other project helpers
  are invoked. Parse `TEMPLATE_CONTENT` and use it as the initial spec content;
  stop and report resolver errors instead of falling back to one layer.
- Retain all core sections. Complete the NIEM exchange section only for
  information crossing a boundary in this feature.
- Describe producers, consumers, business concepts, required information, sharing
  restrictions, and observable interoperability outcomes in stakeholder language.
  Record NIEM adoption or an existing version as a constraint only when supported
  by the request, prior decision, or constitution.
- Specify required handling of missing, ambiguous, invalid, or unsupported
  information and the evidence needed for the requested conformance claim.
- Keep QName selection, namespace design, XSD/CMF structures, and tool choices in
  planning. Do not generate schemas or invent NIEM mappings during specification.
- Preserve the base limit on clarification markers and its built-in quality
  checklist lifecycle. Installing this preset does not itself request TDD or
  authorize a NIEM migration.
