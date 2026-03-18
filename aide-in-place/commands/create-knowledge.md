---
description: "Generate a migration knowledge document with API mappings, breaking changes, and configuration differences for a specific X → Y migration."
---

# Create Migration Knowledge Document

Generate a migration knowledge document for a specific Technology X → Technology Y migration.

## Purpose

This command creates a knowledge document that captures API mappings, breaking changes, configuration differences, and migration patterns for a specific technology migration. The knowledge document is referenced by migration work items and serves as the shared reference for all migration stages.

## User Input

$ARGUMENTS

The user should describe the migration — e.g., "Spring Boot 2 to Spring Boot 3" or "JDK 11 to JDK 21". If not provided, check `docs/aide/vision.md` for the migration definition.

## Instructions

### Prerequisites

- `docs/aide/vision.md` should exist with migration objectives (to understand scope)
- The codebase should be available for analysis

### Knowledge Document Creation

1. **Analyze the codebase** to identify all usages of Technology X:
   - Scan imports, dependencies, configuration files, and API calls
   - Identify which modules/packages use Technology X
   - Determine the scope of changes needed

2. **Research the migration path** from Technology X to Technology Y:
   - Known API replacements and equivalents
   - Deprecated APIs and their modern alternatives
   - Configuration format changes
   - Dependency changes (what to remove, what to add)
   - Behavioral differences between X and Y

3. **Generate the knowledge document** using the migration knowledge template structure

### Required Sections

The knowledge document MUST include:

#### Overview
- Current Technology (X): name, version, known issues
- Target Technology (Y): name, version, key improvements

#### API Mappings (X → Y)
- Table of specific API/class/method replacements
- Detailed examples for the most common migration patterns
- Notes on behavioral differences for each mapping

#### Configuration Changes
- Build configuration (dependencies to remove/add)
- Application configuration (property renames, format changes, new required properties)
- Environment-specific configuration changes

#### Breaking Changes
- APIs without direct equivalents
- Behavioral differences requiring code changes
- Data format changes
- Each with description, impact, and migration path

#### Behavioral Differences
- How specific behaviors changed between X and Y
- Impact on the application
- What to watch for during migration

#### Common Migration Tasks
- High-level checklist of typical migration tasks for this X → Y pair

#### Rollback Procedure
- How to revert the migration if needed

### Important Notes

- **This is a starting point, not a final document.** The generated knowledge document should be reviewed and adapted by the user for their specific scenario. Edge cases, internal conventions, custom integrations, and project-specific patterns will need human input.
- **Update as you go.** As migration work items are executed and new patterns or issues are discovered, update the knowledge document so subsequent work items benefit.
- **One document per migration pair.** If migrating multiple technologies (e.g., both JDK and Spring Boot), create separate knowledge documents for each by running this command once per pair.

### Output

Save the knowledge document to `docs/aide/migrations/[x]-to-[y]-knowledge.md`.

Use lowercase, hyphenated names — e.g., `spring-boot-2-to-spring-boot-3-knowledge.md`, `jdk-11-to-jdk-21-knowledge.md`.

Create the `docs/aide/migrations/` directory if it does not exist.

## Next Step

Review and adapt the generated knowledge document for your specific codebase, then continue the AIDE workflow. The knowledge document will be referenced automatically by `/speckit.aide.create-item` when generating migration work items.
