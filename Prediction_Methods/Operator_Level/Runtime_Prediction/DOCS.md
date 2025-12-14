# Runtime_Prediction - Operator-Level SVM Prediction

Workflow for SVM-based runtime prediction at operator level with Two-Step Forward Feature Selection.

## Working Directory

**CRITICAL:** All commands assume CWD = `Runtime_Prediction/`

```bash
cd /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Operator_Level/Runtime_Prediction
```

---

## Directory Structure

```
Runtime_Prediction/
├── 01_Forward_Selection.py           # Two-step forward feature selection for all operators
├── 02_Train_Models.py                 # Train SVM models for all operator-target combinations
├── 03_Query_Prediction.py             # Bottom-up prediction workflow on test set
├── A_01a_Time_Statistics.py           # Statistical analysis of operator timing patterns
├── A_01b_Template_Operators.py        # Count operators in specified templates
├── A_01c_Operator_Distribution.py     # Histograms of operator time distributions
├── A_01d_Depth_Propagation.py         # Depth propagation plots per template
├── A_01e_Plan_Variability.py          # Analyze plan variability across templates
├── A_01f_Query_Evaluation.py          # Query-level MRE evaluation and template bar chart
├── A_01g_Operator_Analysis.py         # Cross-evaluation of MRE per node type and template
├── ffs_config.py                      # FFS-specific configuration (seed, params, features)
├── DOCS.md                            # This file
├── md/                                # MD reports for single query predictions
├── Baseline_SVM/                      # Baseline dataset results (nu=0.65)
├── Nu_0.5_SVM/                        # Alternative nu=0.5 results (same structure)
│   ├── SVM/                           # Feature selection results
│   │   ├── execution_time/            # Per-operator FFS results
│   │   ├── start_time/                # Per-operator FFS results
│   │   └── two_step_evaluation_overview.csv
│   ├── Model/                         # Trained models
│   │   ├── execution_time/{Operator}/model.pkl
│   │   └── start_time/{Operator}/model.pkl
│   ├── predictions.csv                # Predictions on test set
│   └── Evaluation/                    # Evaluation outputs
│       ├── A_01a_time_statistics_*.csv
│       ├── A_01b_template_operators_*.csv
│       ├── A_01c_histogram_*.png
│       ├── A_01d_depth_*.png
│       ├── A_01e_plan_variability_*.csv
│       ├── A_01f_overall_mre.csv
│       ├── A_01f_template_mre.csv
│       ├── A_01f_template_mre_plot.png
│       ├── A_01g_mre_total_pct_*.csv
│       └── A_01g_mre_startup_pct_*.csv
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

## Input Locations

| Input | Relative Path (from Runtime_Prediction/) |
|-------|------------------------------------------|
| Operator Training Data | `../Datasets/Baseline/` |
| Test Dataset | `../Datasets/Baseline/04b_test_cleaned.csv` |

---

## Workflow Execution Order

```
Input: ../Datasets/Baseline (Operator Training Data)
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
```

**Analysis Scripts** (standalone, not part of main workflow):
- `A_01a_Time_Statistics.py` - Operator time range analysis
- `A_01b_Template_Operators.py` - Count operators in specified templates
- `A_01c_Operator_Distribution.py` - Histograms of operator time distributions
- `A_01d_Depth_Propagation.py` - Depth propagation plots per template
- `A_01e_Plan_Variability.py` - Analyze plan variability across templates
- `A_01f_Query_Evaluation.py` - Query-level MRE evaluation and template bar chart
- `A_01g_Operator_Analysis.py` - Cross-evaluation of MRE per node type and template

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
    ../Datasets/Baseline \
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
    ../Datasets/Baseline \
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
- `--output-file` - Output CSV for predictions (batch mode)
- `--md-query` - Generate MD report for single query (optional)

**Outputs**:

*Batch Mode (--output-file):*
- Predictions CSV with columns:
  - query_file, node_id, node_type, depth, parent_relationship, subplan_name
  - actual_startup_time, actual_total_time
  - predicted_startup_time, predicted_total_time

*Single Query Mode (--md-query):*
- `md/03_query_prediction_{query}_{timestamp}.md` - Detailed prediction report with:
  - Input Summary (absolute paths to test file, overview, models)
  - Query Tree visualization
  - Prediction Chain (Bottom-Up) with model paths, input features, outputs per step
  - Prediction Results table with MRE

**Usage**:
```bash
# Batch mode
python3 03_Query_Prediction.py <test_file> <overview_file> <models_dir> --output-file <output_file>

# Single query MD report
python3 03_Query_Prediction.py <test_file> <overview_file> <models_dir> --md-query <query_file>
```

**Example**:
```bash
# Batch mode
python3 03_Query_Prediction.py \
    ../Datasets/Baseline/04b_test_cleaned.csv \
    ./Baseline_SVM/SVM/two_step_evaluation_overview.csv \
    ./Baseline_SVM/Model \
    --output-file ./Baseline_SVM/predictions.csv

# Single query MD report
python3 03_Query_Prediction.py \
    ../Datasets/Baseline/03_test.csv \
    ./Baseline_SVM/SVM/two_step_evaluation_overview.csv \
    ./Baseline_SVM/Model \
    --md-query Q1_121_seed_984483720
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
- `Evaluation/A_01a_time_statistics_{timestamp}.csv` - Operator statistics with ranges

**Usage**:
```bash
python3 A_01a_Time_Statistics.py <dataset_csv> --output-dir <output_dir>
```

**Example**:
```bash
python3 A_01a_Time_Statistics.py \
    ./Baseline_SVM/predictions.csv \
    --output-dir ./Baseline_SVM
```

---

### A_01b - A_01b_Template_Operators.py

**Purpose**: Count operator occurrences in specified templates.

**Inputs**:
- `predictions_csv` - Path to predictions CSV
- `--templates` - Comma-separated templates (e.g. "Q10,Q7,Q8")
- `--output-dir` - Output directory

**Outputs**:
- `Evaluation/A_01b_template_operators_{templates}_{timestamp}.csv` - Operator counts sorted by occurrence

**Usage**:
```bash
python3 A_01b_Template_Operators.py <predictions_csv> --templates <templates> --output-dir <output_dir>
```

**Example**:
```bash
python3 A_01b_Template_Operators.py \
    ./Baseline_SVM/predictions.csv \
    --templates "Q10,Q7,Q8" \
    --output-dir ./Baseline_SVM
```

---

### A_01c - A_01c_Operator_Distribution.py

**Purpose**: Create histograms showing time distribution per operator.

**Inputs**:
- `predictions_csv` - Path to predictions CSV
- `--output-dir` - Output directory

**Outputs**:
- `Evaluation/A_01c_histogram_startup_time_{timestamp}.png` - 13 subplots for startup time
- `Evaluation/A_01c_histogram_total_time_{timestamp}.png` - 13 subplots for total time

**Usage**:
```bash
python3 A_01c_Operator_Distribution.py <predictions_csv> --output-dir <output_dir>
```

**Example**:
```bash
python3 A_01c_Operator_Distribution.py \
    ./Baseline_SVM/predictions.csv \
    --output-dir ./Baseline_SVM
```

---

### A_01d - A_01d_Depth_Propagation.py

**Purpose**: Create depth propagation plots showing predicted vs actual time per depth level (averaged per plan hash within template).

**Inputs**:
- `structure_csv` - Path to structure CSV (test.csv) for correct plan hash calculation
- `predictions_csv` - Path to predictions CSV
- `--output-dir` - Output directory

**Outputs**:
- `{output-dir}/A_01d_depth_{template}_{plan_hash[:8]}.png` - One plot per unique plan within template

**Usage**:
```bash
python3 A_01d_Depth_Propagation.py <structure_csv> <predictions_csv> --output-dir <output_dir>
```

**Example**:
```bash
python3 A_01d_Depth_Propagation.py \
    ../Datasets/Baseline/03_test.csv \
    ./Baseline_SVM/predictions.csv \
    --output-dir ./Baseline_SVM/Evaluation
```

---

### A_01e - A_01e_Plan_Variability.py

**Purpose**: Analyze whether templates have consistent query plans or variations across seeds.

**Inputs**:
- `predictions_csv` - Path to dataset CSV (use raw dataset for full coverage)
- `--output-dir` - Output directory

**Outputs**:
- `Evaluation/A_01e_plan_variability_summary_{timestamp}.csv` - Summary per template
- `Evaluation/A_01e_plan_variability_detail_{timestamp}.csv` - Detail per query with plan signature

**Usage**:
```bash
python3 A_01e_Plan_Variability.py <predictions_csv> --output-dir <output_dir>
```

**Example**:
```bash
python3 A_01e_Plan_Variability.py \
    ../Datasets/Raw/operator_dataset_20251102_140747.csv \
    --output-dir ./Baseline_SVM
```

---

### A_01f - A_01f_Query_Evaluation.py

**Purpose**: Query-level prediction evaluation and visualization at root operator level.

**Workflow**:
1. Extract root operators (depth=0) from predictions
2. Calculate overall Mean Relative Error (MRE)
3. Calculate per-template statistics
4. Generate CSV metrics and bar chart visualization

**Inputs**:
- `predictions_csv` - Path to predictions CSV
- `--output-dir` - Output directory for evaluation results

**Outputs**:
- `Evaluation/A_01f_overall_mre.csv` - Query-level aggregated error metrics
- `Evaluation/A_01f_template_mre.csv` - Per-template MRE statistics
- `Evaluation/A_01f_template_mre_plot.png` - Bar chart visualization of template performance

**Usage**:
```bash
python3 A_01f_Query_Evaluation.py <predictions_csv> --output-dir <output_dir>
```

**Example**:
```bash
python3 A_01f_Query_Evaluation.py \
    ./Baseline_SVM/predictions.csv \
    --output-dir ./Baseline_SVM
```

---

### A_01g - A_01g_Operator_Analysis.py

**Purpose**: Cross-evaluation of MRE per node type and template.

**Workflow**:
1. Calculate MRE for total time and startup time
2. Create pivot tables: Node Type x Template
3. Export mean MRE % per combination

**Inputs**:
- `predictions_csv` - Path to predictions CSV
- `--output-dir` - Output directory for evaluation results

**Outputs**:
- `Evaluation/A_01g_mre_total_pct_{timestamp}.csv` - Total time MRE %
- `Evaluation/A_01g_mre_startup_pct_{timestamp}.csv` - Startup time MRE %

**Usage**:
```bash
python3 A_01g_Operator_Analysis.py <predictions_csv> --output-dir <output_dir>
```

**Example**:
```bash
python3 A_01g_Operator_Analysis.py \
    ./Baseline_SVM/predictions.csv \
    --output-dir ./Baseline_SVM
```

---

## Notes

Scripts are designed to work with any dataset variant (Baseline, All_Templates) through argparse parameters.
Output directories follow the pattern: `{Dataset}_SVM/` (e.g., Baseline_SVM, All_Templates_SVM).
