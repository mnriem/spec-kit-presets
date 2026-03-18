---
description: "Create or update the vision document with migration objectives (X → Y)."
---

# Create Vision — In-Place Migration

Create or update the vision document to define a technology migration from X to Y.

## Purpose

This is Step 1 of the AI-Driven Engineering workflow, adapted for in-place technology migration. The vision document defines the current state (Technology X), the target state (Technology Y), migration rationale, scope, risks, and success criteria.

## User Input

$ARGUMENTS

## Instructions

### Existing Vision Check

Before creating, check if `docs/aide/vision.md` already exists.
- If it exists, **UPDATE it** by adding a "Technology Migration" section. Do not replace the existing content.
- If it does not exist, create it with migration-focused content.

### Migration Context

The user input should describe the migration. Extract or ask for:

- **From (Technology X)**: Current technology, version, and why it needs to change
- **To (Technology Y)**: Target technology, version, and why it's the right choice

### Creating or Updating the Vision

Create (or update) the vision document and store it in `docs/aide/vision.md`.

### Required Migration Sections

The vision document MUST include these migration-specific sections (in addition to standard vision content):

#### Current State (Technology X)
- Current technology/framework/platform and version
- Why it's no longer suitable (EOL, performance, security, lack of features, etc.)
- Dependencies and integrations using Technology X
- Team's familiarity with Technology X

#### Target State (Technology Y)
- Target technology/framework/platform and version
- Why Technology Y is the right choice
- New capabilities and improvements
- Training needs (if any)

#### Migration Rationale
- Business drivers (cost reduction, compliance, competitive advantage)
- Technical drivers (performance, security, maintainability, developer experience)
- Risk of NOT migrating (security vulnerabilities, vendor lock-in, recruiting challenges)

#### Expected Benefits
- Performance improvements
- Security enhancements
- Developer productivity gains
- Cost savings
- New feature capabilities

#### Migration Scope

**What's Included:**
- Specific components/modules to migrate
- API replacements and mappings
- Configuration changes
- Build system updates
- Dependency updates

**What's Excluded:**
- Features/modules that will remain on Technology X (if any)
- Infrastructure changes handled separately
- Related but separate modernization efforts

#### Breaking Changes and Impacts
- Known breaking changes in Technology Y
- Impact on existing integrations
- Impact on downstream consumers/clients
- Database schema changes (if applicable)
- API contract changes (if applicable)

#### Risk Assessment
- Technical risks (compatibility issues, data migration complexity)
- Business risks (downtime, user impact)
- Mitigation strategies
- Rollback procedures

#### Success Criteria
- Application compiles and builds with Technology Y
- All tests pass (unit, integration, end-to-end)
- Application runs with Technology Y
- Features work identically to Technology X (behavioral equivalence)
- Performance meets or exceeds Technology X benchmarks
- No new security vulnerabilities introduced
- Documentation updated

### Output

Save the completed vision document to `docs/aide/vision.md`.

## Next Step

After reviewing the vision document, start a **new chat session** and run `/speckit.aide.create-roadmap` to generate a staged migration roadmap.
