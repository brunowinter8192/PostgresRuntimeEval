---
description: Analyze mapping_config.py usage across workflow directory
---

# Check Mapping

Analyze mapping_config.py usage across all scripts in a workflow directory.

**Target:** $ARGUMENTS (directory containing mapping_config.py)

---

## Step Indicator Rule

**MANDATORY:** Every response in this workflow MUST start with:
`Phase X, Step Y: [Step-Name]`

---

## Phase 1: Context Loading

### Step 1: Read README.md
Read README.md in $ARGUMENTS directory. Extract directory structure only.

### Step 2: Identify DOCS.md Files
List all DOCS.md files found in subdirectories.

### Step 3: Read mapping_config.py
Extract all mapping exports (variables, lists, dicts).

-> Go to Phase 2

---

## Phase 2: Deep Analysis

### Step 1: Spawn Subagents
For each DOCS.md identified in Phase 1:
- Spawn one Explore subagent
- Subagent scope: Directory containing that DOCS.md
- Subagent task: Analyze mapping_config usage in all .py files

### Step 2: Subagent Reports
Each subagent returns:
- **Unclear mapping purposes:** Mappings imported but usage intent unclear
- **Ambiguous usage patterns:** Hardcoded values vs mapping inconsistencies

### Step 3: Consolidate
Main Agent merges all subagent reports.

-> Go to Phase 3

---

## Phase 3: Assessment

### Step 1: Present Findings

**A. Current Mapping Usage**

| Mapping | Scripts Using It |
|---------|------------------|
| ... | ... |

**B. Unused Mappings**

Mappings defined but never imported by any script.

**C. Mapping Chains**

Mappings that only exist to build other mappings (no direct external use).
Rule: MAPPING -> DIRECT USE, not MAPPING_A -> MAPPING_B -> MAPPING_C

**D. Hardcoded Values**

Values that appear hardcoded in multiple scripts but could use existing mappings.

**E. Inconsistencies**

Scripts that hardcode values which ARE defined in mapping_config but don't import them.

**STOP** - Present findings and wait for user remarks.

**CRITICAL:** If user requests adjustments, return to Step 1 and regenerate findings accordingly.

-> Go to Phase 4

---

## Phase 4: Plan

### Step 1: Write Plan

Write your plan to the **system-provided plan file** (the path shown in the Plan Mode system message, e.g. `~/.claude/plans/<random-name>.md`).

**DO NOT** create a `Plan.md` in the project directory.

Content:
- Mappings to remove
- Mappings to add
- Scripts to update

### Step 2: Exit
Call ExitPlanMode

---

## Principle

**Mapping nur wenn:**
1. Direkt von Script importiert UND genutzt
2. In 2+ Scripts verwendet (sonst hardcoden)
3. Keine Ketten - flache Struktur
