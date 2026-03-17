# Pirate Speak (Full) Preset

Arrr! This full preset transforms all Spec Kit output into authentic pirate speak — replacing every core template and command. Specs become "Voyage Manifests", plans become "Battle Plans", tasks become "Crew Assignments", and your constitution becomes "The Pirate Code".

## Templates Included

| Template | Type | Description |
|----------|------|-------------|
| `spec-template` | template | Voyage Manifest — feature specs written in pirate speak |
| `plan-template` | template | Battle Plan — implementation plans in pirate speak |
| `tasks-template` | template | Crew Assignments — task lists in pirate speak |
| `checklist-template` | template | Ship's Inspection — checklists in pirate speak |
| `constitution-template` | template | The Pirate Code — project constitution in pirate speak |
| `agent-file-template` | template | Ship's Standing Orders — agent file in pirate speak |
| `speckit.specify` | command | Specify command instructing the AI to write in pirate speak |

## Installation

### From local directory (development)

```bash
specify preset add --dev ./pirate-full-preset
```

### From release archive

```bash
specify preset add --from https://github.com/mnriem/spec-kit-presets/releases/download/v1.0.0/pirate-full-preset.zip
```

## Usage

Once installed, all Spec Kit commands will produce pirate-speak output:

```bash
# Create a voyage manifest (spec) in pirate speak
/speckit.specify Add user authentication

# The resulting spec will have headings like:
# - "Crew Tales & Sea Trials" instead of "User Scenarios & Testing"
# - "Demands o' the Voyage" instead of "Requirements"
# - "Measures o' Success" instead of "Success Criteria"
```

## Verification

```bash
# Check that the pirate preset is installed
specify preset list

# Verify which template resolves for specs
specify preset resolve spec-template
# Should show: pirate-full-preset/templates/spec-template.md
```

## Removal

```bash
specify preset remove pirate-full-preset
```

## License

MIT
