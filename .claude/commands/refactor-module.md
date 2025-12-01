# Refactor Module

Refactor a module directory to comply with CLAUDE.md standards.

**Target:** $ARGUMENTS

## Workflow

### Phase 1: Analyse

1. Read all Python scripts in the directory
2. Read existing DOCS.md (if present)
3. Understand the workflow and dependencies between scripts

### Phase 2: Assessment + Recommendation

**Step 1: Questions**

Ask user clarifying questions about:
- Unclear script purposes or dependencies
- Missing scripts (orphan output directories)
- Ambiguous workflow order

**Step 2: Assessment + Recommendation**

Present findings AND concrete plan to user:

**A. Workflow Structure (CRITICAL)**

Analyze script dependencies and determine correct numbering:

| Script | Current | Recommended | Relationship |
|--------|---------|-------------|--------------|
| ... | 01 | 01a | parallel with X |
| ... | 02 | 01b | parallel with X |
| ... | 03 | 02 | sequential (needs 01a, 01b) |

**Parallel (NNx):** Scripts that can run independently, no dependencies between them
**Sequential (NN):** Script that requires output from previous scripts

**B. Compliance Issues**
- Print statements found
- Inline comments in function bodies
- Missing section markers (INFRASTRUCTURE/ORCHESTRATOR/FUNCTIONS)
- Hardcoded paths
- Wrong CSV delimiter

**C. Refactoring Plan**
- Script renames (if any)
- Code changes per script
- CSV file renames (if any)

**Step 3: User Feedback**

Ask user explicitly:
- "Sind dir weitere Issues aufgefallen?"
- "Hast du Anmerkungen zur Workflow-Struktur?"

**Step 4: User Confirmation**

Wait for explicit user confirmation before implementing.

### Phase 3: Implementation

Execute approved refactoring plan:

1. **Script Refactoring**
   - Apply INFRASTRUCTURE -> ORCHESTRATOR -> FUNCTIONS structure
   - Remove print statements
   - Remove inline comments
   - Add header comments to functions
   - Fix CSV delimiters to semicolon

2. **File Renames**
   - Rename scripts if numbering changed
   - Rename CSV outputs to match script numbers

### Phase 4: Compliance Check

Verify against CLAUDE.md:
- [ ] NO comments inside function bodies
- [ ] NO print statements (silent execution)
- [ ] NO hardcoded paths (argparse only)
- [ ] Structure: INFRASTRUCTURE -> ORCHESTRATOR -> FUNCTIONS
- [ ] Semicolon CSV delimiter
- [ ] Header comments on functions

### Phase 5: Report

Present final report to user:
- Changes made per file
- Compliance status

### Phase 6: README Summary

**Step 1: Assessment**

Analysiere was aus diesem Modul in die Workflow-README soll:

**Proposed README Summary:**
- Module name and purpose (1 sentence)
- Input: What does this module consume?
- Output: What does this module produce?
- Key outputs table (if applicable)

**Step 2: User Feedback**

Ask user explicitly:
- "Passt diese Zusammenfassung?"
- "Soll etwas hinzugefuegt/entfernt werden?"

**Step 3: Create Temporary README**

Create `README.md` in module directory with approved summary.

Note: This README.md is TEMPORARY and will be consumed by `/readme-check`.

## Note

For mapping analysis, use `/check-mapping` command separately on the workflow root directory.

## Reference

- CLAUDE.md: `/Users/brunowinter2000/Documents/Thesis/Thesis_Final/CLAUDE.md`
- Example (Data_Generation): `/Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Plan_Level_1/Data_Generation/`
