---
description: "Create migration-specific work items with knowledge documents, API mappings, and behavioral equivalence criteria."
---

# Create Work Item — In-Place Migration

Create a comprehensive migration work item specification.

## Purpose

This is Step 5 of the AI-Driven Engineering workflow, adapted for in-place technology migration. Migration work items include knowledge documents, API mappings, rollback procedures, and behavioral equivalence verification — in addition to standard work item content.

## User Input

$ARGUMENTS

## Instructions

### Item Selection

If `$ARGUMENTS` is provided, treat it as an item number. Look up that item in the queue files under `docs/aide/queue/` and use its description to create the work item.

If `$ARGUMENTS` is empty, automatically pick the next item:
1. Read the most recent queue file in `docs/aide/queue/` (highest numbered `queue-NNN.md`)
2. Cross-reference with existing work items in `docs/aide/items/` and status in `docs/aide/progress.md`
3. Select the first item from the queue that does **not** already have a corresponding work item file in `docs/aide/items/`. A ✅ or 🚧 mark in progress.md alone is NOT sufficient to skip an item — the work item file must also exist.
4. Tell the user which item was auto-selected before proceeding

### Work Item Creation

Create a comprehensive migration work item specification for the selected item and save it to `docs/aide/items/NNN-descriptive-name.md`.

### Required Sections

The work item MUST include all of the following:

#### 1. Migration Overview
- **Component/Module**: What part of the system is being migrated
- **Current State**: How it works with Technology X
- **Target State**: How it will work with Technology Y
- **Migration Rationale**: Why this component needs to migrate

#### 2. Knowledge Document Reference

Reference or include migration knowledge for this X → Y migration:

**API Mappings (X → Y):**
- List specific API/class/method replacements
- Include behavior differences and gotchas
- Note any APIs without direct equivalents

**Configuration Changes:**
- Old configuration format → New configuration format
- Property name changes, default value changes

**Dependency Changes:**
- Old dependencies to remove
- New dependencies to add (with versions)
- Transitive dependency impacts

**Breaking Changes:**
- APIs without direct equivalents
- Behavioral differences requiring code changes
- Data format changes

If a knowledge document exists at `docs/aide/migrations/[x]-to-[y]-knowledge.md`, reference it.

**If no knowledge document exists, STOP and ask the user:**

> No migration knowledge document found for this X → Y migration. Run `/speckit.aide.create-knowledge` to generate one first? Knowledge documents significantly improve migration work item quality. Proceeding without one in 30 seconds...

Wait for user confirmation. If the user confirms to proceed without one, include key knowledge inline in the work item. If the user does not respond within 30 seconds (for automated agents), proceed with inline knowledge as a fallback.

**In either case, if proceeding without a knowledge document, clearly inform the user:**

> ⚠️ No migration knowledge document was used. Inline knowledge was included as a best-effort fallback. Consider running `/speckit.aide.create-knowledge` to generate a dedicated knowledge document for improved accuracy in subsequent work items.

#### 3. Implementation Steps

1. **Preparation:**
   - [ ] Review knowledge document
   - [ ] Identify all usages of Technology X in this component
   - [ ] Create feature flag (if applicable) to toggle between X and Y

2. **Dependency Updates:**
   - [ ] Update build file (pom.xml, build.gradle, package.json, etc.)
   - [ ] Remove Technology X dependencies
   - [ ] Add Technology Y dependencies
   - [ ] Verify dependency resolution

3. **Code Migration (Granular Tasks):**
   - [ ] Replace [X API] with [Y API] in [File:Line]
   - [ ] Update [method call] in [File:Line]
   - [ ] Refactor [class] to use [Y pattern]
   (Populate specific locations during implementation as they are discovered)

4. **Configuration Updates:**
   - [ ] Update config files for Technology Y
   - [ ] Migrate properties from X format to Y format
   - [ ] Update environment-specific configurations

5. **Test Updates:**
   - [ ] Update unit tests for Technology Y behavior
   - [ ] Update integration tests
   - [ ] Add migration-specific test cases
   - [ ] Verify test coverage maintained

#### 4. Acceptance Criteria

**Code Complete:**
- [ ] All Technology X APIs replaced with Technology Y equivalents
- [ ] All imports updated
- [ ] All configuration files updated
- [ ] Code follows Technology Y best practices

**Compilation and Build:**
- [ ] Build succeeds
- [ ] No compiler warnings related to Technology X
- [ ] Dependencies resolve correctly

**Testing Complete:**
- [ ] All unit tests pass
- [ ] All integration tests pass
- [ ] Migration-specific tests pass
- [ ] Test coverage maintained or improved

**Runtime Validation:**
- [ ] Application starts successfully with Technology Y
- [ ] Component functions identically to Technology X version
- [ ] No runtime errors or warnings
- [ ] Logging shows Technology Y is active

**Behavioral Equivalence:**
- [ ] Feature verification — specific features work correctly
- [ ] Integration points work — upstream/downstream systems function correctly
- [ ] Edge cases handled — specific edge cases tested
- [ ] Error handling equivalent — errors handled same way or better

**Performance:**
- [ ] Performance baseline established with Technology X
- [ ] Performance measured with Technology Y
- [ ] No significant regression (or improvement documented)

#### 5. Rollback Procedure

**How to revert if issues are found:**
1. Revert code changes: `git revert [commit-hash]`
2. Restore Technology X dependencies in build file
3. Restore Technology X configuration
4. Rebuild and redeploy
5. Verify Technology X functionality restored

**Rollback time estimate:** [X minutes/hours]

#### 6. Risk Assessment

**Technical Risks:**
- [Specific risk]: Mitigation: [how to mitigate]
- [Compatibility concern]: Mitigation: [how to address]

**Known Issues with Technology Y:**
- [Known limitation or bug]
- [Workaround if any]

#### 7. Dependencies and Order

**Must be completed first:**
- Previous migration work items
- Infrastructure changes
- Third-party library updates

**Blocks these work items:**
- Dependent migration tasks
- Features that depend on this migration

#### 8. Decisions & Trade-offs

To be updated during implementation.

Document:
- Why certain Technology Y APIs were chosen over alternatives
- Any deviations from knowledge document
- Unexpected issues discovered and how they were resolved
- Performance insights
- Lessons learned for future migration work items

#### 9. Completion Reminder

Note that `docs/aide/progress.md` MUST be updated (📋 → 🚧 → ✅) when the item is completed.

### Output

Save the work item to `docs/aide/items/NNN-descriptive-name.md`.
