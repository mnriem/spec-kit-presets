---
description: "Update the progress file with migration component tracking using [MIGRATION X→Y] tags."
---

# Create Progress File — In-Place Migration

Update the progress tracking file to add migration component tracking.

## Purpose

This is Step 3 of the AI-Driven Engineering workflow, adapted for in-place technology migration. The progress file tracks migration components with `[MIGRATION X→Y]` prefixes so migration work is clearly distinguished from regular feature work.

## Prerequisites

- `docs/aide/vision.md` must exist with migration objectives
- `docs/aide/roadmap.md` must exist with migration stages

## Instructions

Read both `docs/aide/vision.md` and `docs/aide/roadmap.md`. If `docs/aide/progress.md` already exists, **UPDATE it** — do not regenerate from scratch. If it does not exist, create it.

### Updating an Existing Progress File

When updating an existing progress file:

1. **Preserve all existing statuses** — never change a ✅, 🚧, ⏸️, or ❌ status back to 📋.
2. **Add migration items** with `[MIGRATION X→Y]` prefix in the feature name.
3. **Do not remove items** — keep existing items even if they no longer appear in the roadmap.
4. **Preserve acceptance criteria checkboxes** — do not uncheck any already-checked criteria.

### Migration Tracking Format

Add a "Technology Migration" section (or update existing) with this format:

```markdown
## Technology Migration: [X] to [Y]

| # | Deliverable | Status |
|---|-------------|--------|
| N.1 | [MIGRATION X→Y] Dependency management — update build files | 📋 |
| N.2 | [MIGRATION X→Y] Core API replacements — replace X APIs with Y | 📋 |
| N.3 | [MIGRATION X→Y] Configuration updates — migrate config files | 📋 |
| N.4 | [MIGRATION X→Y] Authentication module — migrate auth to Y | 📋 |
| N.5 | [MIGRATION X→Y] Data access layer — migrate database access | 📋 |
| N.6 | [MIGRATION X→Y] Integration tests — update tests for Y | 📋 |
| N.7 | [MIGRATION X→Y] Performance validation — verify no regression | 📋 |
```

### Status Icons

- 📋 Planned
- 🚧 In Progress
- ✅ Complete
- ⏸️ Deferred
- ❌ Excluded

### Granular Tracking Note

`progress.md` tracks **high-level migration components** (with status icons). Granular API-level tracking (individual API replacements with checkboxes) belongs in the work items themselves (`docs/aide/items/NNN-*.md`), not in the progress file.

### Output

Save the completed progress file to `docs/aide/progress.md`.

## Next Step

After reviewing the progress file, start a **new chat session** and run `/speckit.aide.create-queue` to generate the first batch of prioritized migration work items.
