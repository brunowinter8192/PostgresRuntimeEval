---
description: Check if README.md and DOCS.md need updates after code changes
---

# Documentation Update Check

---

## Phase 1: Analyze Changes

### Step 1: List Modified Files
List all files modified in this session with brief description of changes.

### Step 2: Categorize Changes
For each change, determine:
- **WHAT changed:** User-visible behavior, contract, workflow
- **HOW changed:** Internal implementation only

-> Go to Phase 2

---

## Phase 2: Impact Assessment

### Step 1: README Check

**Update Required When:**
1. Phase structure changes (new phase, reordering, removed)
2. Modules change (new folder, renamed, removed, dependencies)
3. Shared infrastructure changes (mapping_config.py, new config)
4. Dataset variants change (new variant, train/test split, feature count)
5. External dependencies change (new dependency, paths)

**NO Update When:**
- Bug fixes, internal refactoring, performance improvements
- Code reorganization without behavioral changes
- Variable/function renaming

### Step 2: DOCS Check

**Update Required When:**
1. New script added (0N_Script.py)
2. Script workflow changes (reordering, removed, merged)
3. Argparse parameters change (new args, removed, renamed, defaults)
4. Output format changes (CSV columns, new folder, filenames)
5. Module-specific config changes

**NO Update When:**
- Bug fixes, internal refactoring within function body
- Performance improvements, algorithm changes without contract change
- Variable/function renaming (internal only)

-> Go to Phase 3

---

## Phase 3: Recommendation

### Step 1: Present Recommendation

Format:
```
RECOMMENDATION:
- README.md: UPDATE / NO UPDATE
- DOCS.md: UPDATE / NO UPDATE

REASONING: [Explanation for each decision]

UNCERTAINTY: [If any, formulate specific question]
```

### Step 2: Wait for Approval

STOP - Present recommendation and ask for remarks from the user. DONT go to Phase 4 unless the user explicitly states it
    **Critical** if the user has remarks that dont go with the current recommended changes, roll back to ### Step 1: Present Recommendation, adjust the recommendation accordingly

-> Go to Phase 4

---

## Phase 4: Implementation

### Step 1: Execute Updates

### Step 2: Committ Changes

Report which sections were updated.

---