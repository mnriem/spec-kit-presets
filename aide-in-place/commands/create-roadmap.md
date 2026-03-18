---
description: "Create or extend the roadmap with incremental, verifiable migration stages."
---

# Create Roadmap — In-Place Migration

Generate or extend the roadmap to break down the Technology X → Technology Y migration into incremental, verifiable stages.

## Purpose

This is Step 2 of the AI-Driven Engineering workflow, adapted for in-place technology migration. The roadmap breaks the migration into stages where each stage migrates a logical subset of the codebase and includes verification gates to ensure stability.

## Prerequisites

- `docs/aide/vision.md` must exist with migration objectives (created by `/speckit.aide.create-vision`)

## Instructions

Read `docs/aide/vision.md`. If `docs/aide/roadmap.md` already exists, **EXTEND it** by adding migration stages after existing stages. If it does not exist, create it.

### Updating an Existing Roadmap

When updating an existing roadmap:

1. **Read `docs/aide/progress.md` first** to determine which stages are completed or in progress.
2. **Completed and in-progress stages are immutable** — never modify their goals, deliverables, dependencies, or acceptance criteria.
3. **Add migration stages** at the end of the roadmap, after any existing stages.
4. **Only planned/not-started stages may be edited.**

### Migration Stage Structure

Each migration stage MUST follow this structure:

#### Stage N: [Migration Phase Name]

**Objective**: What this stage accomplishes in the migration

**Duration**: ~X weeks

**Deliverables:**
- Specific components/modules migrated
- API replacements completed
- Configuration changes applied

**API Migrations (X → Y):**
- List specific API/class replacements for this stage

**Verification Criteria:**
- [ ] **Build succeeds**: Application compiles with Technology Y changes
- [ ] **Unit tests pass**: All existing tests pass
- [ ] **Integration tests pass**: Technology Y integrates correctly
- [ ] **Application starts**: Application runs with Technology Y
- [ ] **Feature verification**: Specific features work identically
- [ ] **Performance check**: No significant regression
- [ ] **Rollback tested**: Can revert to Technology X if needed

**Dependencies on Previous Stages:**
- What must be complete before this stage starts

### Migration Stage Guidelines

1. **Incremental approach** — each stage migrates a logical subset:
   - By module/component (e.g., "Migrate authentication module")
   - By layer (e.g., "Migrate data access layer")
   - By technology area (e.g., "Migrate JDK APIs before framework APIs")

2. **Verification gates** — each stage MUST include:
   - Build verification
   - Test verification
   - Runtime verification
   - Feature verification (behavioral equivalence)
   - Performance check

3. **Maintain stability** — after each stage:
   - Application must be in a working state
   - Can be deployed if needed
   - Rollback is possible

4. **Dependencies** — clearly indicate stage dependencies:
   - Infrastructure before application code
   - Core libraries before dependent modules
   - Data layer before business layer before presentation layer

5. **Knowledge documents** — reference or create:
   - `docs/aide/migrations/[x]-to-[y]-knowledge.md`
   - List specific API changes, deprecations, behavioral differences

### Recommended Stage Ordering

Consider this ordering for most migrations:

1. **Stage 0: Pre-migration preparation** — baseline documentation, compatibility analysis, test coverage, rollback procedures, proof-of-concept
2. **Infrastructure and build system** — dependency management, build tool changes
3. **Core libraries and utilities** — shared code, utility classes
4. **Data access layer** — database access, ORM changes
5. **Business logic layer** — service classes, domain logic
6. **Presentation/API layer** — controllers, views, API endpoints
7. **Integration and validation** — end-to-end testing, performance benchmarking

### Output

Save the completed roadmap to `docs/aide/roadmap.md`.

## Next Step

After reviewing the roadmap, start a **new chat session** and run `/speckit.aide.create-progress` to update the progress tracking file with migration components.
