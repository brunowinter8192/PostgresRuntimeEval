# Runtime_Prediction - Pattern Model Training and Hybrid Prediction

Performs forward feature selection, trains pattern-level SVM models, executes hybrid bottom-up prediction, and evaluates accuracy. Uses baseline test data (excludes templates Q2, Q11, Q16, Q22 with InitPlan/SubPlan operators).

## Directory Structure

```
Runtime_Prediction/
├── ffs_config.py                       # SVM hyperparameters and FFS settings
├── 01_Feature_Selection.py             # Forward feature selection for patterns
├── 02_Train_Models.py                  # Train SVM models for patterns
├── 03_Predict_Queries.py               # Hybrid bottom-up prediction
├── 04_Evaluate_Predictions.py          # Query-level MRE evaluation
├── 05_Node_Evaluation.py               # Node type evaluation by prediction source
├── 06_Time_Analysis.py                 # Operator time range analysis
└── Baseline_SVM/                       # [outputs] SVM baseline outputs
    ├── SVM/                            # Feature selection results
    │   ├── execution_time/{Pattern}_csv/
    │   │   ├── ffs_results_seed42.csv
    │   │   ├── selected_features_seed42.csv
    │   │   └── final_features.csv
    │   ├── start_time/{Pattern}_csv/
    │   │   └── ... (same as execution_time)
    │   └── two_step_evaluation_overview.csv
    ├── Model/                          # Trained SVM models
    │   ├── execution_time/{Pattern}/model.pkl
    │   └── start_time/{Pattern}/model.pkl
    └── Evaluation/                     # Prediction evaluation
        ├── predictions.csv
        ├── overall_mre.csv
        ├── template_mre.csv
        ├── template_mre_plot.png
        ├── operator_range_analysis_{ts}.csv
        └── csv/
            ├── pattern_mean_mre_total_pct_{ts}.csv
            ├── pattern_mean_mre_startup_pct_{ts}.csv
            ├── operator_mean_mre_total_pct_{ts}.csv
            └── operator_mean_mre_startup_pct_{ts}.csv
```

## External Dependencies

**Operator_Level Models (Fallback):**
```
Operator_Level/Runtime_Prediction/Baseline_SVM/
├── Model/
│   ├── execution_time/{operator_type}/model.pkl
│   └── start_time/{operator_type}/model.pkl
└── SVM/two_step_evaluation_overview.csv
```

Used as fallback for operators not matching any pattern.

## Shared Infrastructure

**ffs_config.py:**
- `SEED` - Random seed for reproducibility (42)
- `MIN_FEATURES` - Minimum features to select (1)
- `SVM_PARAMS` - NuSVR hyperparameters (kernel, nu, C, gamma, cache_size)

**Constants from mapping_config.py:**
- `PATTERNS` - List of pattern folder names
- `TARGET_TYPES` - ['execution_time', 'start_time']
- `NON_FEATURE_SUFFIXES` - Columns to exclude from features
- `FFS_SEED` - Random seed for cross-validation (42)
- `FFS_MIN_FEATURES` - Minimum features to select (1)

## Workflow Execution Order

```
01 - Feature_Selection  [Pattern datasets → SVM/ FFS results + overview CSV]
     ↓
02 - Train_Models       [Overview + Pattern datasets → Model/ directory]
     ↓
03 - Predict_Queries    [Test data + Pattern + Operator Models → predictions.csv]
     ↓
04 - Evaluate_Predictions [predictions.csv → MRE metrics]
     ↓
05 - Node_Evaluation    [predictions.csv → Node type analysis by source]
     ↓
06 - Time_Analysis      [operator_dataset.csv → Operator range statistics]
```

## Script Documentation

### 01 - Feature_Selection.py

**Purpose:** Perform two-step forward feature selection for all pattern-target combinations

**Workflow:**
1. For each pattern-target combination:
   - Load cleaned training data
   - Extract available features (exclude metadata and targets)
   - Perform forward feature selection with stratified CV
   - Select features that improve MRE
2. Evaluate final feature set with child timing features added
3. Export FFS results, selected features, and overview

**Inputs:**
- `dataset_dir` - Directory containing pattern training datasets (positional)

**Outputs:**
- `{output-dir}/SVM/{target}/{Pattern}_csv/ffs_results_seed42.csv`
- `{output-dir}/SVM/{target}/{Pattern}_csv/selected_features_seed42.csv`
- `{output-dir}/SVM/{target}/{Pattern}_csv/final_features.csv`
- `{output-dir}/SVM/two_step_evaluation_overview.csv`
  - Columns: pattern, target, ffs_feature_count, missing_child_count, final_feature_count, mre_ffs, mre_final, mre_delta, features

**Usage:**
```bash
python 01_Feature_Selection.py Baseline_SVM --output-dir Baseline_SVM
```

**Variables:**
- `--output-dir` - Output directory for FFS results and overview (required)

---

### 02 - Train_Models.py

**Purpose:** Train SVM models for each pattern-target combination

**Workflow:**
1. Load feature selection overview
2. For each pattern-target combination:
   - Load training data
   - Extract final selected features
   - Train NuSVR model with MaxAbsScaler
   - Save model pipeline to pickle file

**Inputs:**
- `dataset_dir` - Path to directory with pattern training datasets (positional)
- `overview_file` - Path to two_step_evaluation_overview.csv (positional)

**Outputs:**
- `{output-dir}/Model/{target}/{Pattern}/model.pkl` per pattern-target

**Usage:**
```bash
python 02_Train_Models.py Baseline_SVM SVM/two_step_evaluation_overview.csv --output-dir Baseline_SVM
```

**Variables:**
- `--output-dir` - Path to output directory (required)

---

### 03 - Predict_Queries.py

**Purpose:** Execute hybrid bottom-up prediction on test queries

**Workflow:**
1. Load test data and model overviews
2. For each query in test set:
   - Build execution tree from operators
   - Traverse bottom-up (leaves to root)
   - For each operator:
     - If parent matches pattern → use pattern model
     - Else → use operator-level fallback model
   - Propagate child predictions to parent features
3. Export predictions with actual vs predicted times

**Inputs:**
- `test_file` - Path to baseline test.csv (positional)
- `pattern_overview` - Path to pattern overview CSV (positional)
- `operator_overview` - Path to operator overview CSV from Operator_Level (positional)
- `pattern_model_dir` - Path to Pattern model directory (positional)
- `operator_model_dir` - Path to Operator model directory from Operator_Level (positional)

**Outputs:**
- `{output-dir}/predictions.csv`
  - Columns: query_file, node_id, node_type, prediction_type (pattern/operator), actual_startup_time, predicted_startup_time, actual_total_time, predicted_total_time

**Usage:**
```bash
python 03_Predict_Queries.py ../../Operator_Level/Datasets/Baseline/04_test.csv \
  Baseline_SVM/SVM/two_step_evaluation_overview.csv \
  ../../Operator_Level/Runtime_Prediction/Baseline_SVM/SVM/two_step_evaluation_overview.csv \
  Baseline_SVM/Model \
  ../../Operator_Level/Runtime_Prediction/Baseline_SVM/Model \
  --output-dir Baseline_SVM/Evaluation
```

**Variables:**
- `--output-dir` - Path to output directory for predictions (required)

---

### 04 - Evaluate_Predictions.py

**Purpose:** Evaluate query-level prediction accuracy using MRE

**Workflow:**
1. Load predictions
2. Calculate MRE per query (sum actuals vs sum predictions)
3. Group by template for template-level analysis
4. Calculate overall MRE
5. Generate template MRE plot

**Inputs:**
- `predictions_file` - Path to predictions.csv (positional)

**Outputs:**
- `{output-dir}/overall_mre.csv`
- `{output-dir}/template_mre.csv`
- `{output-dir}/template_mre_plot.png`

**Usage:**
```bash
python 04_Evaluate_Predictions.py Baseline_SVM/Evaluation/predictions.csv --output-dir Baseline_SVM/Evaluation
```

**Variables:**
- `--output-dir` - Path to output directory (required)

---

### 05 - Node_Evaluation.py

**Purpose:** Cross-evaluation split by prediction source (pattern vs operator)

**Workflow:**
1. Load predictions
2. Split by prediction_type column
3. Calculate MRE per node type for pattern predictions
4. Calculate MRE per node type for operator predictions
5. Export separate analysis for each source

**Inputs:**
- `predictions_file` - Path to predictions.csv (positional)

**Outputs:**
- `{output-dir}/csv/pattern_mean_mre_total_pct_{timestamp}.csv`
- `{output-dir}/csv/pattern_mean_mre_startup_pct_{timestamp}.csv`
- `{output-dir}/csv/operator_mean_mre_total_pct_{timestamp}.csv`
- `{output-dir}/csv/operator_mean_mre_startup_pct_{timestamp}.csv`

**Usage:**
```bash
python 05_Node_Evaluation.py Baseline_SVM/Evaluation/predictions.csv --output-dir Baseline_SVM/Evaluation
```

**Variables:**
- `--output-dir` - Path to Evaluation directory (required)

---

### 06 - Time_Analysis.py

**Purpose:** Analyze operator time ranges across dataset

**Workflow:**
1. Load operator dataset
2. Extract template identifiers
3. Calculate min/max/mean times per operator
4. Identify templates with extreme values
5. Calculate range metrics (absolute and percentage)

**Inputs:**
- `input_file` - Path to baseline training CSV (positional)

**Outputs:**
- `{output-dir}/csv/operator_range_analysis_{timestamp}.csv`
  - Columns: node_type, mean_startup_ms, min_startup_ms, max_startup_ms, count, mean_total_ms, min_total_ms, max_total_ms, template extremes, range metrics

**Usage:**
```bash
python 06_Time_Analysis.py ../../Operator_Level/Datasets/Baseline/04_training.csv --output-dir Baseline_SVM/Evaluation
```

**Variables:**
- `--output-dir` - Output directory for analysis results (required)
