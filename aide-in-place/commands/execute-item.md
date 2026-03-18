---
description: "Implement a migration work item and update progress tracking."
---

# Execute Work Item — In-Place Migration

Implement a migration work item as specified in the docs/aide/items/ directory.

## Purpose

This is Step 6 of the AI-Driven Engineering workflow. This step takes a detailed migration work item specification and implements it — replacing Technology X code with Technology Y equivalents, updating tests, configuration, and documentation as specified.

## User Input

$ARGUMENTS

## Instructions

### Item Selection

If `$ARGUMENTS` is provided, treat it as an item number. Find the matching file in `docs/aide/items/` (e.g., item 5 maps to `docs/aide/items/005-*.md`).

If `$ARGUMENTS` is empty, automatically pick the next item:
1. Read `docs/aide/progress.md` and scan `docs/aide/items/` for existing work item files
2. Select the first work item whose status in `docs/aide/progress.md` is 📋 (Planned) — i.e., it has a spec but hasn't been started yet
3. Tell the user which item was auto-selected before proceeding

### During Implementation

1. **Follow the specification** — implement exactly what the work item describes
2. **Document decisions** — as you make implementation choices, UPDATE the work item's "Decisions & Trade-offs" section with:
   - What was decided
   - Why this approach over alternatives
   - Any trade-offs or future considerations
3. **Update progress** — update `docs/aide/progress.md` status:
   - 📋 → 🚧 when starting implementation
   - 🚧 → ✅ when implementation is complete
4. **Scope your updates** — only update progress rows that correspond to YOUR item number. Do NOT mark other items as complete, even if their criteria happen to be satisfied as a side effect of your work.

### Migration-Specific Verification

Before marking a migration work item as complete, verify ALL of the following:

**Build Verification:**
- [ ] Application compiles with Technology Y changes
- [ ] No compiler warnings related to Technology X

**Test Verification:**
- [ ] All unit tests pass
- [ ] All integration tests pass
- [ ] Migration-specific tests pass

**Runtime Verification:**
- [ ] Application starts successfully with Technology Y
- [ ] No runtime errors or warnings

**Behavioral Equivalence:**
- [ ] Features work identically to Technology X version
- [ ] Integration points function correctly
- [ ] Edge cases handled
- [ ] Error handling equivalent or improved

**Performance Check:**
- [ ] No significant performance regression

**Rollback Readiness:**
- [ ] Rollback procedure documented and viable

### On Smooth Completion

- No feedback loop needed
- Ensure work item decisions are documented
- Mark progress as complete

### On Issues

If you encounter problems (unclear requirements, blocked, need help):
- Document the issue in the work item
- Tell the user to run `/speckit.aide.feedback-loop` to adjust the process

## Next Step

- **More items in queue?** Start a **new chat session** and run `/speckit.aide.create-item` for the next queue item, then `/speckit.aide.execute-item` to implement it.
- **Queue exhausted?** Start a **new chat session** and run `/speckit.aide.create-queue` to generate the next batch.
- **All stages complete?** The migration is done!
