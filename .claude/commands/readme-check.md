# README Check

Consolidate module README summaries into workflow-level README.

**Target:** $ARGUMENTS (workflow root directory)

## Workflow

### Phase 1: Analyse

1. Find all subdirectories with README.md files
2. Read each module README.md
3. Read existing workflow README.md (if present)
4. Read mapping_config.py for shared infrastructure

### Phase 2: Assessment + Recommendation

**Step 1: Assessment**

Present consolidated README structure:

**A. Directory Structure**
- Tree view (without output files)
- `[See DOCS.md]` references for each module

**B. Shared Infrastructure**
- mapping_config.py contents summary
- Other shared config files

**C. Module Summaries**

| Module | Input | Output |
|--------|-------|--------|
| Data_Generation | queries/ | complete_dataset.csv |
| Datasets | complete_dataset.csv | train/test splits |
| Runtime_Prediction | train/test data | predictions |

**D. Datasets** (if applicable)
- Dataset variants (Baseline, State_1, State_2)
- Feature counts and purposes

**E. Workflow Order**
Phase 1 (Data_Generation) -> Phase 2 (Datasets) -> Phase 3 (Runtime_Prediction)

**Step 2: User Feedback**

Ask user explicitly:
- "Sind dir weitere Sections aufgefallen die fehlen?"
- "Hast du Anmerkungen zur Struktur?"

**Step 3: User Confirmation**

Wait for explicit user confirmation before implementing.

### Phase 3: Implementation

1. Create/Update workflow README.md at target directory
2. Delete all temporary module README.md files in subdirectories

### Phase 4: Report

Present final report:
- README.md created/updated at: [path]
- Temporary README.md files deleted: [list]

## Principle

**README Hierarchy:**
- Workflow-Level README.md = Permanent (at workflow root)
- Module-Level README.md = Temporary (consumed and deleted by this command)
- Module-Level DOCS.md = Permanent (detailed script documentation)
