# AIDE In-Place Migration Preset

A [Spec Kit](https://github.com/github/spec-kit) preset that adapts the [AIDE extension](https://github.com/mnriem/spec-kit-extensions) workflow for in-place technology migrations (X → Y pattern).

## When to Use This Preset

Use this preset when:
- Migrating from one technology to another (JDK 8→21, Spring 4→6, Maven→Gradle, React→Angular, etc.)
- Upgrading frameworks or platforms with breaking changes
- Replacing deprecated technologies with modern alternatives
- Modernizing legacy codebases systematically

## What It Does

This preset layers on top of the AIDE extension, overriding all 7 commands with migration-specific guidance:

| Command | What Changes |
|---------|-------------|
| `create-knowledge` | **New command.** Generates a migration knowledge document (`docs/aide/migrations/[x]-to-[y]-knowledge.md`) with API mappings, breaking changes, and configuration differences. Review and adapt for your specific codebase. |
| `create-vision` | Adds migration objectives, current/target state, risk assessment, rollback criteria |
| `create-roadmap` | Structures stages around incremental migration with verification gates at each stage |
| `create-progress` | Tracks migration components with `[MIGRATION X→Y]` prefixes |
| `create-queue` | Prioritizes migration work items with migration awareness |
| `create-item` | Adds knowledge documents, API mappings, behavioral equivalence criteria, rollback procedures |
| `execute-item` | Adds migration-specific verification: behavioral equivalence, performance checks, rollback readiness |
| `feedback-loop` | Adds migration-specific analysis: API mapping gaps, incompatibilities, knowledge document updates |

It also provides:
- **Migration knowledge template** — for creating `docs/aide/migrations/[x]-to-[y]-knowledge.md` documents with API mappings, breaking changes, and configuration changes
- **Updated docs structure** — reference for the migration-enhanced directory layout

## Prerequisites

- [Spec Kit](https://github.com/github/spec-kit) >= 0.2.0
- [AIDE extension](https://github.com/mnriem/spec-kit-extensions) installed

## Installation

```bash
specify preset add aide-in-place --from https://github.com/mnriem/spec-kit-presets/releases/download/aide-in-place-v1.0.0/aide-in-place.zip
```

## Usage

The workflow is identical to the standard AIDE workflow — same 7 commands, same order. The preset modifies what the commands produce, not how the workflow operates.

```
1. /speckit.aide.create-vision      — define migration objectives (X → Y)
2. /speckit.aide.create-roadmap     — plan incremental migration stages
3. /speckit.aide.create-progress    — track migration components
4. /speckit.aide.create-queue       — prioritize next batch of migration work
5. /speckit.aide.create-item        — create detailed migration work item
6. /speckit.aide.execute-item       — implement and verify behavioral equivalence
7. /speckit.aide.feedback-loop      — retrospective on migration issues
8. /speckit.aide.create-knowledge   — generate migration knowledge document (review and adapt)
```

Step 8 is run once per migration pair — e.g., once for JDK 11→21, once for Spring Boot 2→3, etc. Review and adapt each knowledge document for your specific codebase before proceeding. Then repeat steps 4-7 until all migration stages are complete.

## What Makes Migrations Different

### Unique Characteristics
1. **X → Y Pattern** — clear source and target technologies
2. **Knowledge Documents** — detailed API mappings and breaking changes
3. **Behavioral Equivalence** — must work identically (or better) than before
4. **Incremental & Verifiable** — each stage must compile, test, run, and be rollback-able
5. **Granular Tracking** — tracks specific API replacements with checkboxes within work items

### Success Criteria (Not Just Compilation)
- Code compiles with Technology Y
- All tests pass (unit, integration, end-to-end)
- Application runs with Technology Y
- Features work identically (behavioral equivalence verified)
- Performance acceptable (no significant regression)
- Rollback tested (can revert if needed)

## License

MIT
