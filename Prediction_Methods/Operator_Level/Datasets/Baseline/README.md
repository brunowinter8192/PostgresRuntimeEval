# Baseline Dataset Processing

## Directory Structure

```
Baseline/
├── 00_InitSub_Analysis.py           # Analysis script for InitPlan/SubPlan template identification
├── 01_Leaf_Validation.py            # Validation script for Scan leaf node structure
├── 02_Filter_Templates.py           # Remove templates with InitPlan/SubPlan operators
├── 03_Child_Features.py             # Add child operator timing features
├── 04_Split_Data.py                 # Split dataset into training and test sets by seed ranges
├── 05_Split_Types.py                # Split training data by node type into separate folders
├── 06_Clean_Test.py                 # Remove child features from test dataset
├── [outputs]                         # Generated CSV files from scripts 00-06

```

## Workflow Execution Order

Execute scripts in this sequence:

```
1. 00_InitSub_Analysis.py             # Optional: Identify templates with InitPlan/SubPlan
2. 01_Leaf_Validation.py              # Optional: Validate Scan leaf node structure
3. 02_Filter_Templates.py             # Required: Remove problematic templates
4. 03_Child_Features.py               # Required: Add child operator features
5. 04_Split_Data.py                   # Required: Create training and test splits
6. 05_Split_Types.py                  # Optional: Organize training data by node type
7. 06_Clean_Test.py                   # Required: Prepare test dataset
```

**Script Dependency Note**: Script 02_Filter_Templates removes templates (Q2, Q11, Q16, Q22) that were identified by 00_InitSub_Analysis as containing InitPlan/SubPlan operators. While the template list is hardcoded in script 02, it was originally determined by analyzing the output of script 00.

Scripts 00 and 01 are optional analysis/validation scripts. Scripts 02-04 and 06 are required for dataset preparation. Script 05 is optional.

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
- Results inform which templates should be removed in script 02
- Templates Q2, Q11, Q16, Q22 were identified as containing InitPlan/SubPlan operators

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

### 02_Filter_Templates.py

**Purpose**: Remove operators from templates that contain InitPlan or SubPlan operators (Q2, Q11, Q16, Q22)

**Input**:
- `input_file` (positional): Path to raw operator dataset CSV

**Variables** (via argparse):
- `--output-dir`: Output directory for cleaned dataset (required)

**Output**:
- `02_operator_dataset_cleaned.csv` (semicolon-delimited): Dataset with problematic templates removed
  - Same schema as input dataset

**Important Notes**:
- Templates Q2, Q11, Q16, Q22 are removed based on findings from 00_InitSub_Analysis
- These templates contain InitPlan/SubPlan operators which complicate prediction modeling
- This is the first required step in the dataset preparation pipeline

### 03_Child_Features.py

**Purpose**: Add child operator timing features (st1, rt1, st2, rt2) to each operator based on immediate child operators

**Input**:
- `input_file` (positional): Path to cleaned operator dataset CSV (output from script 02)

**Variables** (via argparse):
- `--output-dir`: Output directory for dataset with child features (required)

**Output**:
- `03_operator_dataset_with_children.csv` (semicolon-delimited): Dataset with added child features
  - New columns: st1 (startup time child 1), rt1 (total time child 1), st2 (startup time child 2), rt2 (total time child 2)

**Important Notes**:
- Child features are computed based on parent_relationship (Outer/Inner)
- st1/rt1: timing from child with 'Outer' relationship
- st2/rt2: timing from child with 'Inner' relationship
- Values are 0.0 if no child exists for that relationship
- Child operators are identified by depth (current_depth + 1)

### 04_Split_Data.py

**Purpose**: Split dataset into training and test sets using seed-based partitioning per template

**Input**:
- `input_file` (positional): Path to operator dataset with child features CSV (output from script 03)

**Variables** (via argparse):
- `--output-dir`: Output directory for training and test datasets (required)

**Output**:
- `04_training.csv` (semicolon-delimited): Training dataset with first 120 seeds per template
  - Same schema as input dataset
- `04_test.csv` (semicolon-delimited): Test dataset with last 30 seeds per template
  - Same schema as input dataset

**Important Notes**:
- Each template is split independently to ensure balanced representation
- Training set: seeds 0-119 per template (120 seeds)
- Test set: seeds 120-149 per template (30 seeds)
- Seed ranges are extracted from query_file naming pattern (e.g., Q01_005_seed_...)
- Template and seed columns are temporary and removed from final output

### 05_Split_Types.py

**Purpose**: Organize training dataset by node type, creating separate folders and CSV files for each operator type

**Input**:
- `training_file` (positional): Path to training dataset CSV (output from script 04)

**Variables** (via argparse):
- `--output-dir`: Base directory for node type folders (required)

**Output**:
- `{NodeType}/{NodeType}.csv` (semicolon-delimited): One CSV per node type containing all training operators of that type
  - Folder and file names use underscores (e.g., Hash_Join/Hash_Join.csv)
  - Same schema as input dataset

**Important Notes**:
- Dynamically creates folders based on node_type values in dataset
- Current node types: Aggregate, Gather, Gather_Merge, Hash, Hash_Join, Index_Only_Scan, Index_Scan, Incremental_Sort, Limit, Merge_Join, Nested_Loop, Seq_Scan, Sort
- Each folder contains all training examples for that specific operator type
- This is an optional organizational step for specialized analysis

### 06_Clean_Test.py

**Purpose**: Remove child operator features (st1, rt1, st2, rt2) from test dataset to prepare for realistic prediction scenarios

**Input**:
- `test_file` (positional): Path to test dataset CSV (output from script 04)

**Variables** (via argparse):
- `--output-dir`: Output directory for cleaned test dataset (required)

**Output**:
- `06_test_cleaned.csv` (semicolon-delimited): Test dataset with child features removed
  - Removed columns: st1, rt1, st2, rt2

**Important Notes**:
- Child features must be removed from test set as they would not be available at prediction time
- Training set retains child features for model training
- This ensures realistic evaluation conditions where child operator timings are unknown during inference
