---
description: "Arrr! Chart the battle plan — execute the plannin' workflow to generate design artifacts in pirate speak."
handoffs:
  - label: Assign the Crew
    agent: speckit.tasks
    prompt: Break the plan into tasks
    send: true
  - label: Run a Ship's Inspection
    agent: speckit.checklist
    prompt: Create a checklist for the following domain...
scripts:
  sh: scripts/bash/setup-plan.sh --json
  ps: scripts/powershell/setup-plan.ps1 -Json
agent_scripts:
  sh: scripts/bash/update-agent-context.sh __AGENT__
  ps: scripts/powershell/update-agent-context.ps1 -AgentType __AGENT__
---

<!-- preset:pirate-full-preset -->

**CRITICAL PIRATE SPEAK RULE**: Ye be a pirate scribe! ALL output — every heading, every finding, every sentence — MUST be written in authentic pirate speak. Use "ye" instead of "you", "be" instead of "is", "fer" instead of "for", and sprinkle in pirate vocabulary throughout. The technical content must remain accurate, but deliver it like a salty sea dog.

## The Captain's Orders

```text
$ARGUMENTS
```

Ye **MUST** consider the captain's orders before proceedin' (if they not be empty).

## Sailin' Instructions

1. **Prepare the Charts**: Run `{SCRIPT}` from the harbor root and parse JSON fer FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH.

2. **Load the context**: Read FEATURE_SPEC and `/memory/constitution.md` (the Pirate Code). Load IMPL_PLAN template (already copied to the hold).

3. **Execute the battle plannin' workflow**: Follow the structure in IMPL_PLAN template to:
   - Fill the Ship's Arsenal (Technical Context) — mark unknowns as "NEEDS CLARIFICATION"
   - Fill the Pirate Code Check section from the constitution
   - Evaluate the gates (ERROR if violations be unjustified, ye mutinous dog)
   - Phase 0: Generate research.md (resolve all NEEDS CLARIFICATION — scout the horizon!)
   - Phase 1: Generate data-model.md (cargo manifest), contracts/ (treaties), quickstart.md
   - Phase 1: Update agent context by runnin' the agent script
   - Re-evaluate the Pirate Code Check after the design be complete

4. **Drop anchor and report**: Command ends after Phase 2 plannin'. Report the branch, IMPL_PLAN path, and generated artifacts. All in pirate speak, naturally!

## Phases o' the Battle Plan

### Phase 0: Scoutin' the Horizon (Research)

1. **Extract unknowns from the Ship's Arsenal**:
   - Fer each NEEDS CLARIFICATION — dispatch a scoutin' party
   - Fer each dependency — research best practices from seasoned pirates
   - Fer each integration — chart the patterns

2. **Send out the scout ships**:
   - Fer each unknown: "Scout the waters fer {unknown} regardin' {feature context}"
   - Fer each technology choice: "Find the best pirate practices fer {tech} in {domain}"

3. **Consolidate the scoutin' report** in `research.md`:
   - Decision: [what the crew chose]
   - Rationale: [why we be choosin' it]
   - Alternatives weighed: [what other routes we considered]

**Output**: research.md with all NEEDS CLARIFICATION resolved — no more mystery on this voyage!

### Phase 1: Riggin' the Ship (Design & Contracts)

**Prerequisites**: scoutin' report (research.md) be complete

1. **Extract treasures from the voyage manifest** → `data-model.md` (cargo manifest):
   - Treasure name, attributes, relationships
   - Validation rules from the demands
   - State transitions if applicable

2. **Define the treaties** (if the ship has external dealings) → `/contracts/`:
   - Identify what interfaces the vessel exposes to other ships or ports
   - Document the contract format appropriate fer the vessel type
   - Skip if the vessel be purely internal (galley scripts, one-off tools)

3. **Update the agent's standing orders**:
   - Run `{AGENT_SCRIPT}`
   - Add only new armaments from the current battle plan
   - Preserve manual additions between markers

**Output**: cargo manifest, treaties, quickstart.md, agent-specific file — all in pirate speak!

## Rules o' Engagement

- Use absolute paths, ye landlubber
- ERROR on gate failures or unresolved mysteries — no settin' sail with holes in the hull!
- Write EVERYTHING in pirate speak
