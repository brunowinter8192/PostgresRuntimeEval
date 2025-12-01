# Runtime_Prediction - Operator-Level SVM Prediction

Workflow for SVM-based runtime prediction at operator level with Two-Step Forward Feature Selection.

---

## Directory Structure

```
Runtime_Prediction/
├── 01_Forward_Selection.py           # Two-step forward feature selection for all operators
├── 02_Train_Models.py                 # Train SVM models for all operator-target combinations
├── 03_Query_Prediction.py             # Bottom-up prediction workflow on test set
├── 04a_Query_Evaluation.py            # Evaluate query-level predictions and create visualizations
├── 04b_Operator_Analysis.py           # Cross-evaluation of node type prediction accuracy
├── A_01a_Time_Statistics.py           # Statistical analysis of operator timing patterns
├── ffs_config.py                      # FFS-specific configuration (seed, params, features)
├── DOCS.md                            # This file
├── Baseline_SVM/                      # Baseline dataset results
│   ├── SVM/                           # Feature selection results
│   │   ├── execution_time/            # Per-operator FFS results
│   │   ├── start_time/                # Per-operator FFS results
│   │   └── two_step_evaluation_overview.csv
│   ├── Model/                         # Trained models
│   │   ├── execution_time/{Operator}/model.pkl
│   │   └── start_time/{Operator}/model.pkl
│   ├── predictions.csv                # Predictions on test set
│   └── Evaluation/                    # Evaluation outputs
│       ├── overall_mre.csv
│       ├── template_mre.csv
│       ├── template_mre_plot.png
│       └── csv/                       # Cross-evaluation CSVs
└── All_Templates_SVM/                 # All-templates dataset results (same structure)
```

**External Config**:
- `/Operator_Level/mapping_config.py` - Central mapping configuration

---

## Shared Infrastructure

### mapping_config.py (Operator_Level Root)

Central configuration for all Operator-Level workflows.

**Constants**:
- `OPERATOR_FEATURES` - List of 10 operator features
- `OPERATOR_TARGETS` - List of 2 target columns
- `OPERATOR_METADATA` - List of 6 metadata columns
- `CHILD_FEATURES` - Child prediction features (st1, rt1, st2, rt2, nt1, nt2)
- `TARGET_NAME_MAP` - Mapping: execution_time/start_time to actual_total_time/actual_startup_time
- `TARGET_TYPES` - ['execution_time', 'start_time']
- `OPERATOR_CSV_TO_FOLDER` - Mapping: CSV names (with spaces) to folder names (with underscores)
- `OPERATORS_CSV_NAMES` - List of 13 operator names (CSV format)
- `OPERATORS_FOLDER_NAMES` - List of 13 operator names (folder format)
- `LEAF_OPERATORS` - List of 3 leaf operators

**Functions**:
- `csv_name_to_folder_name(csv_name)` - Convert "Gather Merge" to "Gather_Merge"
- `folder_name_to_csv_name(folder_name)` - Convert "Gather_Merge" to "Gather Merge"
- `is_leaf_operator(operator_csv_name)` - Check if operator is leaf
- `get_all_columns()` - Return Features + Targets + Metadata
- `get_feature_columns()` - Return only Features

**Used by**: All scripts (01-04b)

---

### ffs_config.py

FFS-specific configuration.

**Constants**:
- `SEED` - Random seed (42)
- `MIN_FEATURES` - Minimum features for selection (1)
- `SVM_PARAMS` - NuSVR hyperparameters (kernel, nu, C, gamma, cache_size)

**Used by**: 01_Forward_Selection.py, 02_Train_Models.py

---

## Workflow Execution Order

```
Input: Training Dataset (from Datasets/Baseline)
   |
[01] 01_Forward_Selection.py
   |
SVM/two_step_evaluation_overview.csv
   |
[02] 02_Train_Models.py
   |
Model/{target}/{operator}/model.pkl
   |
[03] 03_Query_Prediction.py
   |
predictions.csv
   |
   +---------------------------+
   |                           |
[04a] 04a_Query_Evaluation.py  [04b] 04b_Operator_Analysis.py
   |                           |
Evaluation/                    Evaluation/csv/
overall_mre.csv                node_type_mean_mre_*.csv
template_mre.csv
template_mre_plot.png
```

**Analysis Script** (standalone, not part of main workflow):
- `A_01a_Time_Statistics.py` - Operator time range analysis on training data

---

## Script Documentation

### 01 - 01_Forward_Selection.py

**Purpose**: Two-Step Forward Feature Selection for all operator-target combinations.

**Workflow**:
1. FFS until natural stopping point
2. Identify missing child features
3. Final Features = FFS Features + Missing Child Features
4. Evaluate both feature sets (MRE comparison)
5. Export overview with performance metrics

**Inputs**:
- `dataset_dir` - Base directory with operator training folders
- `--output-dir` - Output directory for FFS results

**Outputs** (per operator-target):
- `SVM/{target}/{operator}_csv/ffs_results_seed42.csv` - FFS iteration trace
- `SVM/{target}/{operator}_csv/selected_features_seed42.csv` - FFS selected features
- `SVM/{target}/{operator}_csv/final_features.csv` - Final features (FFS + Child)
- `SVM/two_step_evaluation_overview.csv` - Performance overview

**Usage**:
```bash
python3 01_Forward_Selection.py <dataset_dir> --output-dir <output_dir>
```

**Example**:
```bash
python3 01_Forward_Selection.py \
    ../../Datasets/Baseline \
    --output-dir ./Baseline_SVM
```

---

### 02 - 02_Train_Models.py

**Purpose**: Train SVM models for all 26 operator-target combinations (13 operators x 2 targets).

**Inputs**:
- `dataset_dir` - Base directory with operator training CSVs
- `overview_file` - Path to two_step_evaluation_overview.csv
- `--output-dir` - Output directory for trained models

**Outputs**:
- `Model/{target}/{operator}/model.pkl` - Trained SVM pipeline (Scaler + NuSVR)

**Usage**:
```bash
python3 02_Train_Models.py <dataset_dir> <overview_file> --output-dir <output_dir>
```

**Example**:
```bash
python3 02_Train_Models.py \
    ../../Datasets/Baseline \
    ./Baseline_SVM/SVM/two_step_evaluation_overview.csv \
    --output-dir ./Baseline_SVM
```

---

### 03 - 03_Query_Prediction.py

**Purpose**: Bottom-Up Prediction on test set with child feature propagation.

**Workflow**:
1. Predict leaf operators (Seq Scan, Index Scan, Index Only Scan)
2. Propagate child predictions (st1, rt1, st2, rt2) bottom-up
3. Predict parent operators with child features

**Inputs**:
- `test_file` - Path to test dataset CSV
- `overview_file` - Path to two_step_evaluation_overview.csv
- `models_dir` - Directory with trained models
- `--output-file` - Output CSV for predictions

**Outputs**:
- Predictions CSV with columns:
  - query_file, node_id, node_type, depth, parent_relationship, subplan_name
  - actual_startup_time, actual_total_time
  - predicted_startup_time, predicted_total_time

**Usage**:
```bash
python3 03_Query_Prediction.py <test_file> <overview_file> <models_dir> --output-file <output_file>
```

**Example**:
```bash
python3 03_Query_Prediction.py \
    ../../Datasets/Baseline/04b_test_cleaned.csv \
    ./Baseline_SVM/SVM/two_step_evaluation_overview.csv \
    ./Baseline_SVM/Model \
    --output-file ./Baseline_SVM/predictions.csv
```

---

### 04a - 04a_Query_Evaluation.py

**Purpose**: Query-level prediction evaluation and visualization at root operator level.

**Workflow**:
1. Extract root operators (depth=0) from predictions
2. Calculate overall Mean Relative Error (MRE)
3. Calculate per-template statistics
4. Generate CSV metrics and bar chart visualization

**Inputs**:
- `predictions_csv` - Path to predictions CSV from 03_Query_Prediction.py
- `--output-dir` - Output directory for evaluation results

**Outputs**:
- `Evaluation/overall_mre.csv` - Query-level aggregated error metrics
- `Evaluation/template_mre.csv` - Per-template MRE statistics
- `Evaluation/template_mre_plot.png` - Bar chart visualization of template performance

**Usage**:
```bash
python3 04a_Query_Evaluation.py <predictions_csv> --output-dir <output_dir>
```

**Example**:
```bash
python3 04a_Query_Evaluation.py \
    ./Baseline_SVM/predictions.csv \
    --output-dir ./Baseline_SVM
```

---

### 04b - 04b_Operator_Analysis.py

**Purpose**: Cross-evaluation of MRE per node type and template.

**Workflow**:
1. Calculate MRE for total time and startup time
2. Create pivot tables: Node Type x Template
3. Export mean MRE % per combination

**Inputs**:
- `predictions_csv` - Path to predictions CSV
- `--output-dir` - Output directory for evaluation results

**Outputs**:
- `Evaluation/csv/node_type_mean_mre_total_pct_{timestamp}.csv` - Total time MRE %
- `Evaluation/csv/node_type_mean_mre_startup_pct_{timestamp}.csv` - Startup time MRE %

**Usage**:
```bash
python3 04b_Operator_Analysis.py <predictions_csv> --output-dir <output_dir>
```

**Example**:
```bash
python3 04b_Operator_Analysis.py \
    ./Baseline_SVM/predictions.csv \
    --output-dir ./Baseline_SVM
```

---

### A_01a - A_01a_Time_Statistics.py

**Purpose**: Operator time range analysis with template extremes.

**Workflow**:
1. Calculate statistics per operator (mean, min, max)
2. Identify templates with min/max values
3. Calculate ranges (absolute and percentage)
4. Sort by total range descending

**Inputs**:
- `dataset_csv` - Path to dataset CSV
- `--output-dir` - Output directory for analysis results

**Outputs**:
- `Evaluation/operator_range_analysis_{timestamp}.csv` - Operator statistics with ranges

**Usage**:
```bash
python3 A_01a_Time_Statistics.py <dataset_csv> --output-dir <output_dir>
```

**Example**:
```bash
python3 A_01a_Time_Statistics.py \
    ../../Datasets/Baseline/03_training.csv \
    --output-dir ./Baseline_SVM
```

---

## Notes

Scripts are designed to work with any dataset variant (Baseline, All_Templates) through argparse parameters.
Output directories follow the pattern: `{Dataset}_SVM/` (e.g., Baseline_SVM, All_Templates_SVM).
