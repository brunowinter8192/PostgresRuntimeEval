---
description: Refactor module or directory to CLAUDE.md standards
argument-hint: [Path/to/Module or Directory]
---

# Refactor Module/Directory

Refactor a module (single .py file) or directory (folder with modules) to comply with CLAUDE.md standards.

**Target:** $ARGUMENTS

**Terminology:**
- **Module:** Single .py file
- **Directory:** Folder containing multiple modules

---

## Step Indicator Rule

**MANDATORY:** Every response in this workflow MUST start with:
`Phase X, Step Y: [Step-Name]`

---

## Phase 1: Analyse

### Step 1: Identify Target Type
Determine if target is:
- **Module:** Single .py file -> analyze that file only
- **Directory:** Folder -> analyze all .py files within

### Step 2: Read Target Content
- For module: Read the .py file
- For directory: Read all Python scripts and existing DOCS.md (if present)

### Step 3: Collect Metrics

For each module, analyze:

| Metric | OK | Warning | Critical |
|--------|-------|-----------|-------------|
| Module LOC | < 400 | 400-600 | > 600 |
| Functions | < 15 | 15-20 | > 20 |
| Function LOC | < 30 | 30-50 | > 50 |
| Cross-Module Imports | < 5 | 5-8 | > 8 |

Additional indicators:
- **Single Responsibility:** Multiple unrelated concerns in one module?
- **Code Duplication:** Repeated logic across functions?
- **Deep Nesting:** > 4 indentation levels?
- **Naming Clarity:** Unclear function/variable names?
- **CLAUDE.md Compliance:** Missing section markers, inline comments, print statements?

### Step 4: Understand Workflow
- Identify dependencies between scripts (if directory)
- Determine execution order
- Note input/output relationships

-> Go to Phase 2

---

## Phase 2: Identify Refactoring Opportunities

### Step 1: Categorize Findings

Based on metrics, identify opportunities by type:

**1. Extract Module**
- Trigger: > 400 LOC with distinct functional groups
- Example: "HTML parsing + Markdown conversion" -> split into 2 modules

**2. Extract Function**
- Trigger: Functions > 50 LOC
- Example: Large orchestrator -> extract sub-tasks

**3. Consolidate Duplication**
- Trigger: Similar code in multiple places
- Example: Common validation -> move to shared utility

**4. Simplify Dependencies**
- Trigger: > 5 cross-module imports
- Example: 8 imports -> refactor to 3 via abstraction

**5. Improve Clarity**
- Trigger: Unclear naming, missing structure
- Example: Rename functions, add section separators

**6. CLAUDE.md Compliance**
- Trigger: Missing INFRASTRUCTURE/ORCHESTRATOR/FUNCTIONS structure
- Trigger: Inline comments in function bodies
- Trigger: Print statements found

### Step 2: Present Findings

For each module with issues:

```
MODULE: [path].py
LOC: [X] | Functions: [Y] | Imports: [Z]
Issues: [list threshold violations]

Opportunities:
- [Type]: [specific suggestion]
- [Type]: [specific suggestion]
```

**STOP** - Present findings and ask for user remarks.

**CRITICAL:** If user identifies edge cases or disagrees with findings:
1. Discuss and clarify
2. Adjust findings based on feedback
3. Return to Step 2 and present updated findings

-> Go to Phase 3

---

## Phase 3: Propose Solutions

### Step 1: Present 3 Approaches

Based on opportunities found, present 3 distinct refactoring strategies.
Each approach must be a valid, complete solution - not a scope variation.

**Approach A: [Strategy Name]**
- Strategy: [How this approach tackles the problem]
- Trade-off: [What you gain vs what you sacrifice]

**Approach B: [Strategy Name]**
- Strategy: [Different way to tackle the same problem]
- Trade-off: [What you gain vs what you sacrifice]

**Approach C: [Strategy Name]**
- Strategy: [Third distinct way]
- Trade-off: [What you gain vs what you sacrifice]

**Recommendation:** Approach [X]
**Reasoning:** [Why this is the best fit for this specific case]

**STOP** - Present approaches with recommendation and wait for user selection.

**CRITICAL:** If user does not select an approach or requests adjustments:
1. Refine approaches based on feedback
2. Return to Step 1 and present updated options

-> Go to Phase 4

---

## Phase 4: Create Plan

### Step 1: Write Refactoring Plan

Write your plan to the **system-provided plan file** (the path shown in the Plan Mode system message, e.g. `~/.claude/plans/<random-name>.md`).

  **DO NOT** create a `Plan.md` in the project directory.
  
Contents:
  - Clear implementation steps
  - Files to modify/ create
  - Expected outcome

### Step 2: Exit Plan Mode

- call ExitPlanMode.

-> Go to Phase 5

---

## Phase 5: Execute Plan