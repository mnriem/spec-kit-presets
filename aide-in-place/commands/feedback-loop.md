---
description: "Analyze migration issues and suggest improvements to the process and documents."
---

# Feedback Loop — In-Place Migration

Analyze what went wrong and identify improvements needed for the migration process.

## Purpose

This is Step 7 of the AI-Driven Engineering workflow. Use this whenever migration work didn't go smoothly — when you needed help, found unclear requirements, hit unexpected Technology X/Y incompatibilities, or the process broke down. This step is available at any point in the workflow.

## Instructions

Analyze the current state of the project documents and recent migration work to identify improvements.

### 1. Document Gaps

- What should have been in `docs/aide/vision.md` but wasn't? (missing migration scope, unidentified breaking changes, incomplete risk assessment)
- What should have been in `docs/aide/roadmap.md`? (missing dependencies, wrong stage ordering, inadequate verification criteria)
- What should have been in `docs/aide/progress.md` for tracking? (missing migration components, incorrect granularity)
- Was the work item specification missing critical migration information? (missing API mappings, incomplete knowledge document, unclear rollback procedure)
- Does the migration knowledge document need updating? (`docs/aide/migrations/[x]-to-[y]-knowledge.md`)

### 2. Migration-Specific Issues

- Were there unexpected Technology X → Y incompatibilities?
- Were API mappings incomplete or incorrect?
- Did behavioral equivalence fail? Which features behaved differently?
- Were there performance regressions not anticipated?
- Did the rollback procedure work when tested?
- Were there transitive dependency conflicts?

### 3. Process Issues

- Did the human need to intervene? Why?
- Were requirements unclear or ambiguous?
- Were dependencies not identified upfront?
- Did migration scope expand unexpectedly?
- Was the stage ordering wrong? (e.g., should have migrated a different layer first)

### 4. Command Adaptations Needed

The AIDE commands may need project-specific adjustments. Because Spec Kit installs extension commands into agent-specific directories, the installed copies must be located and updated:

**Finding installed commands:**
- Look for AIDE command files in agent-specific directories such as:
  - `.claude/commands/` (Claude Code)
  - `.github/prompts/` (GitHub Copilot commands)
  - `.github/agents/` (GitHub Copilot agents)
  - `.gemini/commands/` (Gemini CLI)
  - `.cursor/commands/` (Cursor)
  - Or any other agent directory present in the project
- Search for files containing `speckit.aide` to locate all installed copies

**What to adapt:**
- Should the create-item command include additional migration-specific sections?
  - Example: Add "Data Migration" section for database-heavy migrations
  - Example: Add "Feature Flag" section for gradual rollout
  - Example: Add "Parallel Run" section for critical systems
- Should the knowledge document template be updated with project-specific patterns?
- What worked well that we should keep?

**When modifying commands**, update the installed copies in the agent-specific directories — these are the files that actually get executed.

### 5. Recommendations

Provide specific, actionable suggestions:
- Updates to vision/roadmap/progress
- Updates to migration knowledge documents
- Changes to command templates
- New commands to create
- Process improvements
- Stage reordering or rescoping

### Important Notes

- **Routine decisions** during smooth implementation belong in the work item's "Decisions" section, not here.
- This feedback loop is for **systemic issues** that need process, document, or command improvements.
- **Be minimal** — suggest the smallest set of changes that will prevent the problem from recurring.

## Next Step

After applying the recommended changes, resume the workflow from where you left off. Start a **new chat session** for the next step.
