> **NIEM preset:** Before executing this command, read
> `.specify/presets/niem/templates/niem-guidance.md`; stop and report its path if
> unavailable. Apply the NIEM guidance below within the existing stage, not after
> completion. Preserve all base prerequisites, paths, permissions, hooks, and approvals.

{CORE_TEMPLATE}

## NIEM Convergence Guidance

- Treat the existing spec, plan, tasks, and constitution as the sole source of
  intent. Installing this preset does not authorize additional NIEM obligations.
- Compare the current implementation with the approved exchange mappings,
  contracts, partner compatibility requirements, and required evidence.
  Distinguish missing, partial, contradicting, and unrequested work using the
  base command's gap types and severity rules.
- Inspect existing evidence; do not execute generators or tests that write files.
  A missing required validation result may justify a traceable follow-up task,
  but absence of an unrequested certification does not.
- Preserve append-only behavior: the only permitted write is a new Convergence
  phase in `tasks.md`, using fresh IDs and references to existing intent.
  Do not rewrite mappings, schemas, existing tasks, or application code.
- If no actionable gaps remain, leave `tasks.md` byte-for-byte unchanged. The
  base converged result means the specified work is satisfied, not independent
  NIEM certification.
