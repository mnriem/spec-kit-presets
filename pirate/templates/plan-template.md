# Battle Plan: [FEATURE]

<!-- preset:pirate-full-preset -->

**Vessel**: `[###-feature-name]` | **Charted**: [DATE] | **Voyage Manifest**: [link]
**Orders**: Feature specification from `/specs/[###-feature-name]/spec.md`

## Captain's Summary

[Extract from the voyage manifest: primary demand + tactical approach from scoutin']

## Ship's Arsenal (Technical Context)

<!--
  ACTION REQUIRED: Replace this with the actual rigging and armaments
  of yer vessel. The structure be advisory to guide the plunderin'.
-->

**Tongue o' the Code**: [e.g., Python 3.11, Swift 5.9, Rust 1.75 or NEEDS CLARIFICATION]
**Weapons & Tools**: [e.g., FastAPI, UIKit, LLVM or NEEDS CLARIFICATION]
**Treasure Vault**: [if applicable, e.g., PostgreSQL, CoreData, files or N/A]
**Sea Trials**: [e.g., pytest, XCTest, cargo test or NEEDS CLARIFICATION]
**Targetted Waters**: [e.g., Linux server, iOS 15+, WASM or NEEDS CLARIFICATION]
**Vessel Type**: [e.g., library/cli/web-service/mobile-app or NEEDS CLARIFICATION]
**Speed Goals**: [e.g., 1000 req/s, 10k lines/sec, 60 fps or NEEDS CLARIFICATION]
**Constraints o' the Sea**: [e.g., <200ms p95, <100MB memory or NEEDS CLARIFICATION]
**Fleet Size**: [e.g., 10k sailors, 1M LOC, 50 screens or NEEDS CLARIFICATION]

## Pirate Code Check

*GATE: Must pass before Phase 0 scoutin'. Re-check after Phase 1 design.*

[Gates determined based on the Pirate Code (constitution file)]

## Ship's Layout (Project Structure)

### Charts & Maps (documentation fer this voyage)

```text
specs/[###-feature]/
├── plan.md              # This here battle plan
├── research.md          # Phase 0 scoutin' report
├── data-model.md        # Phase 1 cargo manifest
├── quickstart.md        # Phase 1 quick start guide
├── contracts/           # Phase 1 treaties and accords
└── tasks.md             # Phase 2 crew assignments (/speckit.tasks)
```

### Below Deck (source code at repository root)

<!--
  ACTION REQUIRED: Replace the placeholder layout below with the actual
  structure o' yer vessel. Delete unused options and expand with real paths.
-->

```text
# [REMOVE IF UNUSED] Option 1: Single vessel (DEFAULT)
src/
├── models/
├── services/
├── cli/
└── lib/

tests/
├── contract/
├── integration/
└── unit/

# [REMOVE IF UNUSED] Option 2: Port & starboard (web app)
backend/
├── src/
│   ├── models/
│   ├── services/
│   └── api/
└── tests/

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   └── services/
└── tests/
```

**Structure Decision**: [Document the chosen layout and reference the actual decks]

## Complexity Log

> **Fill ONLY if Pirate Code Check has violations that must be justified**

| Violation | Justification | Captain's Approval |
|-----------|---------------|-------------------|
| [Which article o' the Code] | [Why we be breakin' it] | [Aye or Nay] |

## Phases o' the Voyage

### Phase 0: Scoutin' the Horizon

[Research the waters, chart the unknown, identify dangers]

### Phase 1: Riggin' the Ship (Design)

[Design the solution, define contracts, model the cargo]

### Phase 2: Crew Assignments

[Break the work into tasks — done by /speckit.tasks, not this command]
