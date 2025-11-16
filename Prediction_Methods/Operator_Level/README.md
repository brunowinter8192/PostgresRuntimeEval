# Operator-Level Runtime Prediction

ML-based runtime prediction for SQL query operators using SVM models trained on PostgreSQL query execution plans.

## Directory Structure

```
Operator_Level/
├── mapping_config.py       # Shared operator mappings, features, targets, and constants
├── Data_Generation/        # Phase 1: Feature/target extraction from EXPLAIN → operator_dataset.csv [See README]
├── Datasets/              # Phase 2: Dataset preparation and train/test splits → Baseline/ [See README]
└── Runtime_Prediction/    # Phase 3: SVM model training and evaluation → Baseline_SVM/ [See README]
```

## Shared Infrastructure

**mapping_config.py** - Central configuration shared across all three phases

**Constants:**
- `OPERATOR_FEATURES` - 10 operator features (np, nt, nt1, nt2, sel, startup_cost, total_cost, plan_width, reltuples, parallel_workers)
- `OPERATOR_TARGETS` - 2 target variables (actual_startup_time, actual_total_time)
- `OPERATOR_METADATA` - 6 metadata fields (query_file, node_id, node_type, depth, parent_relationship, subplan_name)
- `CHILD_FEATURES_TIMING` - 4 child timing features (st1, rt1, st2, rt2) - unknown at prediction time
- `CHILD_FEATURES_STRUCTURAL` - 2 child type features (nt1, nt2) - known at prediction time
- `CHILD_FEATURES` - Combined list of all child features (TIMING + STRUCTURAL)
- `LEAF_OPERATORS` - 3 leaf node types (Seq Scan, Index Scan, Index Only Scan)

**Functions:**
- `csv_name_to_folder_name()` - Convert operator names with spaces to underscores
- `folder_name_to_csv_name()` - Reverse conversion for operator names
- `is_leaf_operator()` - Check if operator is a leaf node
- `get_all_columns()` - Return complete column list (features + targets + metadata)
- `get_feature_columns()` - Return feature columns only

**Used by:** All scripts across Data_Generation, Datasets, and Runtime_Prediction phases

## Workflow Overview

The operator-level prediction pipeline consists of three sequential phases:

**Phase 1 → Phase 2 → Phase 3**

1. **Data_Generation**: Extract features from EXPLAIN and targets from EXPLAIN ANALYSE for all TPC-H queries → Produces operator_dataset.csv with 18 columns (6 metadata + 10 features + 2 targets)

2. **Datasets**: Filter templates, create train/test splits → Produces Baseline/ folder with organized training and test data

3. **Runtime_Prediction**: Perform forward feature selection, train 26 SVM models (13 operators × 2 targets), generate predictions, evaluate accuracy → Produces Baseline_SVM/ folder with models and evaluation results

**Baseline Concept:** The Baseline version represents the first dataset/model configuration. Future iterations may use different template filters or feature sets, producing variants like All_Templates or domain-specific configurations.

## Phase Documentation

### Phase 1: Data_Generation

**Purpose:** Extract operator-level features and runtime targets from PostgreSQL query execution plans

**Input:** TPC-H queries (Q1-Q22, excluding Q15) executed against PostgreSQL database

**Process:**
- Extract 10 features from EXPLAIN output (plan structure and cost estimates)
- Extract 2 targets from EXPLAIN ANALYSE output (requires cold cache per query)
- Merge features and targets with metadata (query file, node ID, node type, depth, parent relationship, subplan name)

**Output:** `operator_dataset_{timestamp}.csv` (18 columns total)

**See Data_Generation/README.md for detailed script documentation**

### Phase 2: Datasets

**Purpose:** Prepare baseline dataset by filtering templates, adding child features, and creating train/test splits

**Input:** operator_dataset.csv from Phase 1 (placed in Raw/ folder)

**Process:**
- Filter problematic templates containing InitPlan/SubPlan nodes (removes Q2, Q11, Q16, Q22)
- Add child operator timing features (st1, rt1, st2, rt2) for bottom-up prediction
- Split data by seed (120 training, 30 test samples per template)
- Organize training data by operator type
- Clean test set (remove child features to simulate real prediction scenario)

**Output:** Baseline/ folder containing Training/ and Test/ subdirectories with organized data splits

**Toolset:** The Datasets/ directory contains scripts for various data preparation tasks. For baseline, scripts 02-06 are applied. Future dataset variants may use different script combinations.

**See Datasets/README.md for detailed script documentation**

### Phase 3: Runtime_Prediction

**Purpose:** Train SVM models with forward feature selection, generate predictions, and evaluate accuracy

**Input:** Baseline/Training/ and Baseline/Test/ folders from Phase 2

**Process:**
- Perform two-step forward feature selection for all operator-target combinations
- Train 26 SVM models using NuSVR (13 operators × 2 targets: execution_time and start_time)
- Generate bottom-up predictions on test set (child predictions propagated to parents)
- Evaluate prediction accuracy by node type and template using MRE (Mean Relative Error)

**Output:** Baseline_SVM/ folder containing:
- SVM/ - Feature selection results per operator-target combination
  - execution_time/<Operator>_csv/ - FFS iteration traces and selected features
  - start_time/<Operator>_csv/ - FFS iteration traces and selected features
  - two_step_evaluation_overview.csv - Final features and MRE per operator-target
- Model/ - Trained SVM models organized by target
  - execution_time/<Operator>/model.pkl
  - start_time/<Operator>/model.pkl

**Operators (13 total):** Aggregate, Gather, Gather_Merge, Hash, Hash_Join, Index_Only_Scan, Index_Scan, Incremental_Sort, Limit, Merge_Join, Nested_Loop, Seq_Scan, Sort

**Toolset:** The Runtime_Prediction/ directory contains scripts for model training, prediction, and various evaluation analyses. Scripts 00-02 form the core pipeline. Script 03 provides query-level evaluation, while scripts 04-05 provide operator and timing analysis.

**See Runtime_Prediction/README.md for detailed script documentation**
