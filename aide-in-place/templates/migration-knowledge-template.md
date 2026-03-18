# Migration Knowledge: [Technology X] to [Technology Y]

## Overview

This document provides specific migration knowledge for migrating from [Technology X] to [Technology Y]. Reference this document from migration work items created by `/speckit.aide.create-item`.

**Current Technology (X):**
- Technology name and version
- End of life date (if applicable)
- Known issues or limitations

**Target Technology (Y):**
- Technology name and version
- Release date and maturity
- Key improvements over X

## API Mappings (X → Y)

### Core APIs

| Technology X API | Technology Y API | Notes / Considerations |
|------------------|------------------|------------------------|
| `com.x.OldClass` | `com.y.NewClass` | Constructor signature changed |
| `x.method()` | `y.method()` | Return type changed |
| `x.deprecatedMethod()` | `y.modernMethod()` | Behavior difference: [explain] |

### Detailed Examples

#### Example 1: [Common Pattern]

**Technology X (Before):**
```
// Old code using Technology X
```

**Technology Y (After):**
```
// New code using Technology Y
```

**Considerations:**
- [Specific gotchas or differences]

## Configuration Changes

### Build Configuration

**Technology X:**
```
<!-- Old dependencies -->
```

**Technology Y:**
```
<!-- New dependencies -->
```

### Application Configuration

**Technology X:**
```
# Old configuration format
x.property.name=value
```

**Technology Y:**
```
# New configuration format
y.property-name=value
```

**Configuration Migration Notes:**
- Property naming convention changes
- Renamed properties
- New required properties
- Changed default values

## Breaking Changes

### 1. [Breaking Change Name]

**Description:** [What changed and why]

**Impact:** [Who/what is affected]

**Migration Path:**
- [Step-by-step instructions]

### 2. [Another Breaking Change]

[Continue pattern above]

## Behavioral Differences

### Difference 1: [Behavior Name]

**Technology X Behavior:**
- [How it worked in X]

**Technology Y Behavior:**
- [How it works in Y]

**Impact on Application:**
- [What to watch for during migration]

## Common Migration Tasks

High-level checklist of typical tasks:
- [ ] Update build file (pom.xml, build.gradle, package.json, etc.)
- [ ] Update dependencies (remove X, add Y)
- [ ] Replace core APIs
- [ ] Update configuration files
- [ ] Migrate data structures/DTOs
- [ ] Update exception handling
- [ ] Update logging
- [ ] Update tests
- [ ] Update documentation

## Rollback Procedure

If migration needs to be reverted:
1. Revert code changes
2. Restore Technology X dependencies
3. Restore Technology X configuration
4. Rebuild and verify
5. Confirm Technology X functionality restored

## References

- [Technology Y migration guide URL]
- [Technology Y release notes URL]
- [Community migration resources]
