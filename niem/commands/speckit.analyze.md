> **NIEM preset:** Before executing this command, read
> `.specify/presets/niem/templates/niem-guidance.md`; stop and report its path if
> unavailable. Apply the NIEM guidance below within the existing stage, not after
> completion. Preserve all base prerequisites, paths, permissions, hooks, and approvals.

{CORE_TEMPLATE}

## NIEM Analysis Guidance

- Remain strictly read-only. Do not amend mappings, schemas, tasks, checklists, or
  governance and do not run commands that generate validation artifacts.
- Include NIEM issues in the existing analysis categories, severity rules, and
  finding limit: unsupported conformance claims, unverified reuse, conflicting
  namespace/release identities, semantic drift, unjustified local extensions,
  and required evidence with no task coverage.
- Trace exchange requirements through the plan and tasks. Read referenced mapping
  and contract sections only as needed to establish a finding.
- Distinguish missing requirements from missing implementation. A design-stage
  artifact is not defective merely because implementation checks have not run.
- Report unavailable source evidence as uncertainty, not a fabricated rule
  violation. Do not equate an XML/JSON schema check or a checked checklist with
  full NIEM conformance.
- Preserve the constitution's authority and the base approval requirement for
  any remediation; do not add requirements during analysis.
