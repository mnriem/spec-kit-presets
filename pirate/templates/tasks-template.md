---
description: "Crew assignment list fer feature plunderin'"
---

# Crew Assignments: [FEATURE NAME]

<!-- preset:pirate-full-preset -->

**Orders From**: Design charts in `/specs/[###-feature-name]/`
**Prerequisites**: battle plan (required), voyage manifest (required fer crew tales), scoutin' report, cargo manifest, treaties

**Sea Trials**: The examples below include test tasks. Tests be OPTIONAL — only include 'em if explicitly ordered in the voyage manifest.

**Organization**: Tasks be grouped by crew tale to enable independent plunderin' and testin' of each tale.

## Format: `[ID] [P?] [Tale] Description`

- **[P]**: Can sail in parallel (different ships, no dependencies)
- **[Tale]**: Which crew tale this task belongs to (e.g., CT1, CT2, CT3)
- Include exact file paths in descriptions, ye scallywag

## Path Conventions

- **Single vessel**: `src/`, `tests/` at the harbor root
- **Port & starboard**: `backend/src/`, `frontend/src/`
- **Flagship**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single vessel — adjust based on the battle plan

<!--
  ============================================================================
  AHOY! The tasks below be SAMPLE TASKS fer illustration only, ye landlubber!

  The /speckit.tasks command MUST replace these with actual tasks based on:
  - Crew tales from the voyage manifest (with their priorities P1, P2, P3...)
  - Demands from the battle plan
  - Treasures from the cargo manifest
  - Treaties from contracts/

  Tasks MUST be organized by crew tale so each tale can be:
  - Plundered independently
  - Tested independently
  - Delivered as an MVP increment o' booty

  DO NOT keep these sample tasks in the generated tasks.md file, savvy?
  ============================================================================
-->

## Phase 1: Preparin' the Ship (Setup)

**Purpose**: Riggin' the vessel and basic structure

- [ ] T001 Build the ship's frame per the battle plan
- [ ] T002 Stock the armory with [framework] weapons
- [ ] T003 [P] Hoist the flags and set the code style

---

## Phase 2: Layin' the Keel (Foundational)

**Purpose**: Core hull that MUST be seaworthy before ANY crew tale can commence

**AVAST!**: No crew tale work can begin until this phase be complete!

- [ ] T004 Lay the treasure vault schema and migration planks
- [ ] T005 [P] Rig the authentication cannons
- [ ] T006 [P] Chart the API routes and set up the watch
- [ ] T007 Forge the base models that all tales depend upon
- [ ] T008 Install the error handling bilge pumps
- [ ] T009 Configure the ship's environment (compass, maps, astrolabe)

**Checkpoint**: The keel be laid — crew tale plunderin' can now sail in parallel!

---

## Phase 3: Crew Tale 1 - [Title] (Priority: P1) — First Plunder

**Goal**: [Brief description o' what booty this tale delivers]

**Independent Sea Trial**: [How to verify this tale works on its own]

### Sea Trials fer Crew Tale 1 (OPTIONAL — only if ordered)

> **NOTE: Write these tests FIRST, ensure they FAIL before plunderin'**

- [ ] T010 [P] [CT1] Contract test fer [endpoint] in tests/contract/test_[name].py
- [ ] T011 [P] [CT1] Integration test fer [voyage] in tests/integration/test_[name].py

### Plunderin' fer Crew Tale 1

- [ ] T012 [P] [CT1] Forge [Treasure1] model in src/models/[treasure1].py
- [ ] T013 [P] [CT1] Forge [Treasure2] model in src/models/[treasure2].py
- [ ] T014 [CT1] Build [Service] in src/services/[service].py (depends on T012, T013)
- [ ] T015 [CT1] Build [endpoint/feature] in src/[location]/[file].py
- [ ] T016 [CT1] Add validation and error cannons
- [ ] T017 [CT1] Add the ship's log fer crew tale 1 operations

**Checkpoint**: At this point, Crew Tale 1 should be fully seaworthy and testable on its own!

---
