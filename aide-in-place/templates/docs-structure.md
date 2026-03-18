# AIDE Document Structure Reference — In-Place Migration

This document describes the file structure created and maintained by the AIDE workflow when using the in-place migration preset.

## Directory Layout

```
your-project/
├── docs/
│   └── aide/
│       ├── vision.md              # Step 1: Product vision with migration objectives
│       ├── roadmap.md             # Step 2: Staged migration plan with verification gates
│       ├── progress.md            # Step 3: Feature and migration component tracking
│       ├── migrations/
│       │   └── [x]-to-[y]-knowledge.md  # Migration knowledge documents
│       ├── queue/
│       │   ├── queue-001.md       # Step 4: First batch of migration work items
│       │   ├── queue-002.md       # Step 4: Second batch
│       │   └── ...
│       └── items/
│           ├── 001-migrate-*.md   # Step 5: Detailed migration work item spec
│           ├── 002-migrate-*.md   # Step 5: Another migration work item
│           └── ...
```

## Document Descriptions

### vision.md

The foundation document. Contains the complete project vision including migration objectives: current state (Technology X), target state (Technology Y), migration rationale, scope, risk assessment, and success criteria. Created once for the migration, updated via the feedback loop when scope changes.

### roadmap.md

A staged migration plan derived from the vision. Each stage migrates a logical subset of the codebase (by module, layer, or technology area) and includes verification gates: build, test, runtime, behavioral equivalence, and performance checks. Stages are sized for incremental delivery with rollback capability at each point.

### progress.md

A checklist tracking every migration component. Migration items use `[MIGRATION X→Y]` prefixes for clear identification. Uses status icons:

| Icon | Status |
|------|--------|
| 📋 | Planned |
| 🚧 | In Progress |
| ✅ | Complete |
| ⏸️ | Deferred |
| ❌ | Excluded |

Updated during work item execution (Step 6).

### migrations/[x]-to-[y]-knowledge.md

Knowledge documents for specific technology migrations. Contain API mappings, breaking changes, configuration changes, behavioral differences, and migration patterns. Referenced from work items. Created using the migration knowledge template.

### queue/queue-NNN.md

Batches of ~10 prioritized migration work items. Each queue is numbered sequentially. Work item numbers are sequential across all queues. Generated from the roadmap, progress, and vision documents.

### items/NNN-descriptive-name.md

Detailed migration work item specifications. Each item includes migration overview, knowledge document references, API mappings, implementation steps, acceptance criteria with behavioral equivalence verification, rollback procedures, and risk assessment. Granular API-level tracking (individual replacements with checkboxes) lives here, not in progress.md.
