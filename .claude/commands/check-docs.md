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

**README Sections (per CLAUDE.md):**
1. Title + Description
2. Directory Structure (root-level files + [See DOCS.md] links)
3. Workflow Phases (Purpose, Input, Output, Details)

**Update Required When:**
1. Phase structure changes (new phase, reordering, removed)
2. Directories change (new folder, renamed, removed)
3. Root-level config files change (mapping_config.py, new config)
4. Phase inputs/outputs change

**NO Update When:**
- Bug fixes, internal refactoring, performance improvements
- Script changes inside directories (those go in DOCS.md)
- Variable/function renaming

### Step 2: DOCS Check

**DOCS Sections (per CLAUDE.md):**
1. Working Directory (CRITICAL)
2. Directory Structure
3. Workflow Dependency Graph (if applicable)
4. Output Structure (if applicable)
5. Shared Infrastructure (if applicable)
6. Module Documentation (Purpose, Inputs, Outputs, Variables, Usage)

**Update Required When:**
1. New script added (0N_Script.py)
2. Script dependencies change (Workflow Dependency Graph)
3. Argparse parameters change (Inputs/Variables in Module Documentation)
4. Output paths/formats change (Output Structure)
5. Script removed or renamed (Directory Structure + Module Documentation)

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