# Baseline Dataset Processing

## Working Directory

**CRITICAL:** All commands assume CWD = `Datasets/`

```bash
cd Prediction_Methods/Operator_Level/Datasets
```

## Directory Structure

```
Datasets/
├── DOCS.md                              # This file
├── 01_Filter_Templates.py               # Remove templates with InitPlan/SubPlan operators
├── 02_Child_Features.py                 # Add child operator timing features
├── 03_Split_Data.py                     # Template-stratified query-level train/test split
├── 04a_Split_Types.py                   # Split training data by node type into separate folders
├── 04b_Clean_Test.py                    # Remove child features from test dataset
├── A_01a_InitSub_Analysis.py            # Analysis script for InitPlan/SubPlan template identification
├── A_01b_Leaf_Validation.py             # Validation script for Scan leaf node structure
├── A_01e_Verify_Plans.py                # Verify plan hash distribution across datasets
├── Raw/                                 # Raw input data
│   └── operator_dataset_*.csv           # Input from Data_Generation
└── Baseline/                            # Output directory for all generated CSV files
    ├── A_01a_InitSub_Templates.csv      # From A_01a (optional)
    ├── A_01b_scan_leaf_issues.csv       # From A_01b (optional)
    ├── 01_operator_dataset_cleaned.csv  # From 01
    ├── 02_operator_dataset_with_children.csv  # From 02
    ├── 03_training.csv                  # From 03
    ├── 03_test.csv                      # From 03
    ├── 04b_test_cleaned.csv             # From 04b
    └── 04a_{NodeType}/                  # From 04a (optional)
        └── 04a_{NodeType}.csv           # One folder per operator type
```

## Workflow Execution Order

```
Analysis Scripts (Optional):
A_01a_InitSub_Analysis.py     # Identify templates with InitPlan/SubPlan
A_01b_Leaf_Validation.py      # Validate Scan leaf node structure
A_01e_Verify_Plans.py         # Verify plan hash distribution

Main Workflow:
01_Filter_Templates.py ──> 02_Child_Features.py ──> 03_Split_Data.py
                                                           │
                                                   ┌───────┴───────┐
                                                   ↓               ↓
                                         04a_Split_Types.py  04b_Clean_Test.py
```

**Script Dependency Note**: Script 01_Filter_Templates removes templates (Q2, Q11, Q16, Q22) that were identified by A_01a_InitSub_Analysis as containing InitPlan/SubPlan operators. While the template list is hardcoded in script 01, it was originally determined by analyzing the output of script A_01a.

Scripts A_01a and A_01b are optional analysis/validation scripts. Scripts 01-03 are required for dataset preparation. Scripts 04a and 04b can run in parallel after 03 completes.

## Shared Infrastructure

### mapping_config.py

**Location**: `/Prediction_Methods/Operator_Level/mapping_config.py`

**Purpose**: Centralized configuration for operator features, targets, metadata, and naming conventions.

**Used by**: Scripts 02, 04a (indirectly via feature column names)

**Constants**:
- `OPERATOR_FEATURES`: List of feature column names for model training
- `OPERATOR_TARGETS`: List of target column names (actual_startup_time, actual_total_time)
- `OPERATOR_METADATA`: List of metadata column names (query_file, node_id, etc.)
- `CHILD_FEATURES_TIMING`: Child operator timing features (st1, rt1, st2, rt2)
- `TARGET_NAME_MAP`: Mapping between execution_time/start_time and actual column names
- `TARGET_TYPES`: List of target types (execution_time, start_time)
- `OPERATOR_CSV_TO_FOLDER`: Mapping from CSV operator names to folder names
- `OPERATORS_FOLDER_NAMES`: List of operator names as folder names
- `LEAF_OPERATORS`: List of leaf operator types (Seq Scan, Index Scan, Index Only Scan)

**Functions**:
- `csv_name_to_folder_name()`: Convert operator CSV name to folder name format

## Script Documentation

### A_01a_InitSub_Analysis.py

**Purpose**: Analyze and identify templates that use InitPlan or SubPlan operators

**Input**:
- `input_file` (positional): Path to raw operator dataset CSV

**Variables** (via argparse):
- `--output-dir`: Output directory for analysis results (required)

**Output**:
- `A_01a_InitSub_Templates.csv` (semicolon-delimited): Templates using InitPlan/SubPlan
  - Columns: template, operator_count, plan_types

**Important Notes**:
- This is an optional analysis script
- Results inform which templates should be removed in script 01
- Templates Q2, Q11, Q16, Q22 were identified as containing InitPlan/SubPlan operators

**Usage:**
```bash
python3 A_01a_InitSub_Analysis.py Raw/operator_dataset_20251102_140747.csv --output-dir Baseline
```

---

### A_01b_Leaf_Validation.py

**Purpose**: Validate that all Scan operators (Seq Scan, Index Scan, Index Only Scan) are leaf nodes in query execution plans

**Input**:
- `input_file` (positional): Path to raw operator dataset CSV

**Variables** (via argparse):
- `--output-dir`: Output directory for validation results (required)

**Output**:
- `A_01b_scan_leaf_issues.csv` (semicolon-delimited): Scan operators that violate leaf structure
  - Columns: template, scan_with_child_count, non_scan_leaf_count

**Important Notes**:
- This is an optional validation script
- Empty or zero-count output indicates all Scan operators are correctly positioned as leaf nodes
- Helps identify data quality issues in query execution plans

**Usage:**
```bash
python3 A_01b_Leaf_Validation.py Raw/operator_dataset_20251102_140747.csv --output-dir Baseline
```

---

### 01_Filter_Templates.py

**Purpose**: Remove operators from templates that contain InitPlan or SubPlan operators (Q2, Q11, Q16, Q22)

**Input**:
- `input_file` (positional): Path to raw operator dataset CSV

**Variables** (via argparse):
- `--output-dir`: Output directory for cleaned dataset (required)

**Output**:
- `01_operator_dataset_cleaned.csv` (semicolon-delimited): Dataset with problematic templates removed
  - Same schema as input dataset

**Important Notes**:
- Templates Q2, Q11, Q16, Q22 are removed based on findings from A_01a_InitSub_Analysis
- These templates contain InitPlan/SubPlan operators which complicate prediction modeling
- This is the first required step in the dataset preparation pipeline

**Usage:**
```bash
python3 01_Filter_Templates.py Raw/operator_dataset_20251102_140747.csv --output-dir Baseline
```

---

### 02_Child_Features.py

**Purpose**: Add child operator timing features (st1, rt1, st2, rt2) to each operator based on immediate child operators

**Input**:
- `input_file` (positional): Path to cleaned operator dataset CSV (output from script 01)

**Variables** (via argparse):
- `--output-dir`: Output directory for dataset with child features (required)

**Output**:
- `02_operator_dataset_with_children.csv` (semicolon-delimited): Dataset with added child features
  - New columns: st1 (startup time child 1), rt1 (total time child 1), st2 (startup time child 2), rt2 (total time child 2)

**Important Notes**:
- Child features are computed based on parent_relationship (Outer/Inner)
- st1/rt1: timing from child with 'Outer' relationship
- st2/rt2: timing from child with 'Inner' relationship
- Values are 0.0 if no child exists for that relationship
- Child operators are identified by depth (current_depth + 1)

**Usage:**
```bash
python3 02_Child_Features.py Baseline/01_operator_dataset_cleaned.csv --output-dir Baseline
```

---

### 03_Split_Data.py

**Purpose**: Split dataset into training and test sets using template-stratified query-level split

**Input**:
- `input_file` (positional): Path to operator dataset with child features CSV (output from script 02)

**Variables** (via argparse):
- `--output-dir`: Output directory for training and test datasets (required)
- `--train-size`: Queries per template for training (default: 120)
- `--test-size`: Queries per template for testing (default: 30)
- `--seed`: Random seed for reproducibility (default: 42)

**Output**:
- `03_training.csv` (semicolon-delimited): Training dataset (120 queries per template)
  - Same schema as input dataset
- `03_test.csv` (semicolon-delimited): Test dataset (30 queries per template)
  - Same schema as input dataset

**Important Notes**:
- Split occurs at query-level (query_file), not operator-row level
- All operators from a query stay together in either training or test set
- Template-stratified: Each template contributes equal number of queries to both sets
- Prevents data leakage where operators from same query appear in both sets
- With 14 templates: 1680 training queries, 420 test queries

**Usage:**
```bash
python3 03_Split_Data.py Baseline/02_operator_dataset_with_children.csv --output-dir Baseline
```

---

### 04a_Split_Types.py

**Purpose**: Organize training dataset by node type, creating separate folders and CSV files for each operator type

**Input**:
- `training_file` (positional): Path to training dataset CSV (output from script 03)

**Variables** (via argparse):
- `--output-dir`: Base directory for node type folders (required)

**Output**:
- `04a_{NodeType}/04a_{NodeType}.csv` (semicolon-delimited): One CSV per node type containing all training operators of that type
  - Folder and file names use underscores with 04a prefix (e.g., 04a_Hash_Join/04a_Hash_Join.csv)
  - Same schema as input dataset

**Important Notes**:
- Dynamically creates folders based on node_type values in dataset
- Current node types: Aggregate, Gather, Gather_Merge, Hash, Hash_Join, Index_Only_Scan, Index_Scan, Incremental_Sort, Limit, Merge_Join, Nested_Loop, Seq_Scan, Sort
- Each folder contains all training examples for that specific operator type
- This is an optional organizational step for specialized analysis

**Usage:**
```bash
python3 04a_Split_Types.py Baseline/03_training.csv --output-dir Baseline
```

---

### 04b_Clean_Test.py

**Purpose**: Remove child operator features (st1, rt1, st2, rt2) from test dataset to prepare for realistic prediction scenarios

**Input**:
- `test_file` (positional): Path to test dataset CSV (output from script 03)

**Variables** (via argparse):
- `--output-dir`: Output directory for cleaned test dataset (required)

**Output**:
- `04b_test_cleaned.csv` (semicolon-delimited): Test dataset with child features removed
  - Removed columns: st1, rt1, st2, rt2

**Important Notes**:
- Child features must be removed from test set as they would not be available at prediction time
- Training set retains child features for model training
- This ensures realistic evaluation conditions where child operator timings are unknown during inference

**Usage:**
```bash
python3 04b_Clean_Test.py Baseline/03_test.csv --output-dir Baseline
```

---

### A_01e_Verify_Plans.py

**Purpose**: Verify plan hash distribution across training and test datasets to ensure all unique plans are represented in both sets

**Input**:
- `dataset_csv` (positional): Path to dataset CSV (training.csv or test.csv)

**Variables** (via argparse):
- `--output-dir`: Output directory for distribution results (required)

**Output**:
- `plan_hash_distribution.csv` (semicolon-delimited): Plan hash counts per template
  - Columns: template, plan_hash, query_count, plan_hash_short

**Important Notes**:
- Run on both training.csv and test.csv to compare distributions
- Useful for identifying templates with multiple query plan variants (e.g., Q9 has 2 different plans)
- Helps ensure train/test split preserves all plan variants

**Usage:**
```bash
python3 A_01e_Verify_Plans.py Baseline/03_training.csv --output-dir Baseline
python3 A_01e_Verify_Plans.py Baseline/03_test.csv --output-dir Baseline
```
