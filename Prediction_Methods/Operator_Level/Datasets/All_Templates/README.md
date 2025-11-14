# All Templates Dataset Processing

## Directory Structure

```
All_Templates/
├── 00_InitSub_Analysis.py           # Analysis script for InitPlan/SubPlan template identification
├── 01_Leaf_Validation.py            # Validation script for Scan leaf node structure
├── 02_Child_Features.py             # Add child operator timing features
├── 03_Split_Data.py                 # Split dataset into training and test sets by seed ranges
├── 04_Split_Types.py                # Split training data by node type into separate folders
├── 05_Clean_Test.py                 # Remove child features from test dataset
└── [outputs]                         # Generated CSV files and node type folders

```

## Workflow Execution Order

Execute scripts in this sequence:

```
1. 00_InitSub_Analysis.py             # Optional: Identify templates with InitPlan/SubPlan
2. 01_Leaf_Validation.py              # Optional: Validate Scan leaf node structure
3. 02_Child_Features.py               # Required: Add child operator features
4. 03_Split_Data.py                   # Required: Create training and test splits
5. 04_Split_Types.py                  # Optional: Organize training data by node type
6. 05_Clean_Test.py                   # Required: Prepare test dataset
```

**Key Difference from Baseline**: This dataset includes ALL templates, including those with InitPlan/SubPlan operators (Q2, Q11, Q16, Q22). No template filtering is applied.

Scripts 00 and 01 are optional analysis/validation scripts. Scripts 02-03 and 05 are required for dataset preparation. Script 04 is optional.

## Script Documentation

### 00_InitSub_Analysis.py

**Purpose**: Analyze and identify templates that use InitPlan or SubPlan operators

**Input**:
- `input_file` (positional): Path to raw operator dataset CSV

**Variables** (via argparse):
- `--output-dir`: Output directory for analysis results (required)

**Output**:
- `00_InitSub_Templates.csv` (semicolon-delimited): Templates using InitPlan/SubPlan
  - Columns: template, operator_count, plan_types

**Important Notes**:
- This is an optional analysis script
- In this dataset, templates with InitPlan/SubPlan are retained for analysis
- Templates Q2, Q11, Q16, Q22 typically contain InitPlan/SubPlan operators

### 01_Leaf_Validation.py

**Purpose**: Validate that all Scan operators (Seq Scan, Index Scan, Index Only Scan) are leaf nodes in query execution plans

**Input**:
- `input_file` (positional): Path to raw operator dataset CSV

**Variables** (via argparse):
- `--output-dir`: Output directory for validation results (required)

**Output**:
- `01_scan_leaf_issues.csv` (semicolon-delimited): Scan operators that violate leaf structure
  - Columns: template, scan_with_child_count, non_scan_leaf_count

**Important Notes**:
- This is an optional validation script
- Empty or zero-count output indicates all Scan operators are correctly positioned as leaf nodes
- Helps identify data quality issues in query execution plans

### 02_Child_Features.py

**Purpose**: Add child operator timing features (st1, rt1, st2, rt2) to each operator based on immediate child operators

**Input**:
- `input_file` (positional): Path to raw operator dataset CSV

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
- This is the first required step as no template filtering is applied

### 03_Split_Data.py

**Purpose**: Split dataset into training and test sets using seed-based partitioning per template

**Input**:
- `input_file` (positional): Path to operator dataset with child features CSV (output from script 02)

**Variables** (via argparse):
- `--output-dir`: Output directory for training and test datasets (required)

**Output**:
- `03_training.csv` (semicolon-delimited): Training dataset with first 120 seeds per template
  - Same schema as input dataset
- `03_test.csv` (semicolon-delimited): Test dataset with last 30 seeds per template
  - Same schema as input dataset

**Important Notes**:
- Each template is split independently to ensure balanced representation
- Training set: seeds 0-119 per template (120 seeds)
- Test set: seeds 120-149 per template (30 seeds)
- Seed ranges are extracted from query_file naming pattern (e.g., Q01_005_seed_...)
- Template and seed columns are temporary and removed from final output
- All templates are included, unlike Baseline dataset which excludes Q2, Q11, Q16, Q22

### 04_Split_Types.py

**Purpose**: Organize training dataset by node type, creating separate folders and CSV files for each operator type

**Input**:
- `training_file` (positional): Path to training dataset CSV (output from script 03)

**Variables** (via argparse):
- `--output-dir`: Base directory for node type folders (required)

**Output**:
- `04_{NodeType}/04_{NodeType}.csv` (semicolon-delimited): One folder and CSV per node type containing all training operators of that type
  - Folder and file names use script number prefix (e.g., 04_Hash_Join/04_Hash_Join.csv)
  - Same schema as input dataset

**Important Notes**:
- Dynamically creates folders based on node_type values in dataset
- Folders and CSVs are prefixed with "04" to match script number
- Current node types: Aggregate, Gather, Gather_Merge, Hash, Hash_Join, Index_Only_Scan, Index_Scan, Incremental_Sort, Limit, Merge_Join, Nested_Loop, Seq_Scan, Sort
- Each folder contains all training examples for that specific operator type
- This is an optional organizational step for specialized analysis

### 05_Clean_Test.py

**Purpose**: Remove child operator features (st1, rt1, st2, rt2) from test dataset to prepare for realistic prediction scenarios

**Input**:
- `test_file` (positional): Path to test dataset CSV (output from script 03)

**Variables** (via argparse):
- `--output-dir`: Output directory for cleaned test dataset (required)

**Output**:
- `05_test_cleaned.csv` (semicolon-delimited): Test dataset with child features removed
  - Removed columns: st1, rt1, st2, rt2

**Important Notes**:
- Child features must be removed from test set as they would not be available at prediction time
- Training set retains child features for model training
- This ensures realistic evaluation conditions where child operator timings are unknown during inference
