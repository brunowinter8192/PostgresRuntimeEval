# Datasets Module - Dynamic Prediction Method

This module prepares datasets for 13-out-of-14 leave-one-template-out (LOTO) cross-validation, enabling on-the-fly model training with completely unseen test templates.

## Directory Structure

```
Datasets/
├── 01_Split_Templates.py          # Create 13-of-14 train/test splits
├── 02_Clean_Test.py                # Remove child timing features from test sets
├── Baseline/                       # Output directory for template-based splits
│   ├── Q1/                         # Template Q1 as test set
│   │   ├── training_cleaned.csv    # 13 templates (Q3-Q19)
│   │   ├── test_cleaned.csv        # 1 template (Q1)
│   │   └── 02_test_cleaned.csv     # [output] Test set without child timing features
│   ├── Q3/                         # Template Q3 as test set
│   │   ├── training_cleaned.csv    # 13 templates (Q1, Q4-Q19)
│   │   ├── test_cleaned.csv        # 1 template (Q3)
│   │   └── 02_test_cleaned.csv     # [output] Test set without child timing features
│   ├── Q4/
│   ├── Q5/
│   ├── Q6/
│   ├── Q7/
│   ├── Q8/
│   ├── Q9/
│   ├── Q10/
│   ├── Q12/
│   ├── Q13/
│   ├── Q14/
│   ├── Q18/
│   └── Q19/                        # 14 template subdirectories total
└── DOCS.md
```

## Shared Infrastructure

### mapping_config.py

Located at: `../mapping_config.py`

**CHILD_FEATURES_TIMING**
- List of child operator timing features: `['st1', 'rt1', 'st2', 'rt2']`
- Purpose: Identifies features unknown at prediction time
- Used by: 02_Clean_Test.py to remove these features from test datasets
- Rationale: In real prediction scenarios, child operator runtimes are not available until after execution

## Workflow Execution Order

```
01_Split_Templates.py
    |
    v
Baseline/{Q1, Q3, Q4, ..., Q19}/
    ├── training_cleaned.csv    (13 templates)
    └── test_cleaned.csv        (1 template)
    |
    v
02_Clean_Test.py
    |
    v
Baseline/{Q1, Q3, Q4, ..., Q19}/
    └── 02_test_cleaned.csv     (test without st1, rt1, st2, rt2)
```

**Execution Flow:**
1. Script 01 creates 14 subdirectories with train/test splits
2. Script 02 processes all test sets and removes child timing features

## Script Documentation

### 01 - Split_Templates.py

**Purpose:** Create 13-out-of-14 leave-one-template-out train/test splits for all TPC-H templates

**Workflow:**
1. Load complete operator dataset from input CSV
2. Extract template name from query_file column (e.g., "Q1_100_seed_123" → "Q1")
3. For each of 14 templates (Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q18, Q19):
   - Create template subdirectory (e.g., "Q1/")
   - Test set: All rows where template matches current template
   - Training set: All rows where template does NOT match current template
   - Export training_cleaned.csv (13 templates)
   - Export test_cleaned.csv (1 template)

**Inputs:**
- `input`: Path to complete operator dataset CSV
  - Example: `/path/to/Operator_Level/Datasets/Baseline/02_operator_dataset_cleaned.csv`
  - Format: Semicolon-delimited CSV with operator-level features
  - Required columns: query_file, node_id, node_type, depth, np, nt, nt1, nt2, st1, rt1, st2, rt2, sel, startup_cost, total_cost, plan_width, reltuples, parallel_workers, actual_startup_time, actual_total_time

**Outputs:**
- `training_cleaned.csv` (14 files, one per template directory)
  - Format: Semicolon-delimited CSV
  - Content: All operator data from 13 templates (excluding test template)
  - Location: `Baseline/{template_name}/training_cleaned.csv`

- `test_cleaned.csv` (14 files, one per template directory)
  - Format: Semicolon-delimited CSV
  - Content: All operator data from 1 template (test template only)
  - Location: `Baseline/{template_name}/test_cleaned.csv`

**Usage:**
```bash
python3 01_Split_Templates.py \
    /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Operator_Level/Datasets/Baseline/02_operator_dataset_cleaned.csv \
    --output-dir /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Dynamic/Datasets/Baseline
```

**Variables:**
- `--output-dir` (required): Base directory where template subdirectories will be created

---

### 02 - Clean_Test.py

**Purpose:** Remove child timing features from all test datasets to simulate real prediction scenarios

**Workflow:**
1. Find all template subdirectories in Baseline/ folder
2. For each template directory:
   - Load test_cleaned.csv
   - Identify child timing features present in dataset (st1, rt1, st2, rt2)
   - Remove these features from dataset
   - Export as 02_test_cleaned.csv in same directory

**Inputs:**
- `baseline_dir`: Path to Baseline directory containing template subdirectories
  - Example: `/path/to/Dynamic/Datasets/Baseline`
  - Expected structure: 14 subdirectories (Q1, Q3, Q4, etc.) each containing test_cleaned.csv

**Outputs:**
- `02_test_cleaned.csv` (14 files, one per template directory)
  - Format: Semicolon-delimited CSV
  - Content: Test dataset without child timing features (st1, rt1, st2, rt2 removed)
  - Location: `Baseline/{template_name}/02_test_cleaned.csv`
  - Purpose: Prediction-ready test set simulating real-world scenario

**Usage:**
```bash
python3 02_Clean_Test.py \
    /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Dynamic/Datasets/Baseline
```

**Variables:**
None (all positional)
