# Runtime Prediction - Module Documentation

## Directory Structure

```
Runtime_Prediction/
├── 01_Clean_FFS.py                # Remove Pattern+Plan Leaf child features from FFS
├── 02_Feature_Selection.py        # Forward Feature Selection for patterns
├── 03_Train_Models.py             # Train SVM models for pattern predictions
├── 04_Predict_Queries.py          # Predict queries using optimized execution plan
├── A_01a_Evaluate_Predictions.py  # Evaluate root-level predictions (MRE)
├── A_01b_Node_Evaluation.py       # Node-level evaluation split by prediction type
├── A_01c_Time_Analysis.py         # Operator range analysis
├── ffs_config.py                  # Feature selection configuration
├── csv/                           # Script outputs
│   ├── 01_cleaned_ffs_YYYYMMDD_HHMMSS.csv         [outputs]
│   └── predictions.csv                             [outputs]
├── Model/                         # Trained pattern models
│   ├── execution_time/
│   │   └── {pattern_hash}/model.pkl
│   └── start_time/
│       └── {pattern_hash}/model.pkl
└── DOCS.md                        # This file
```

## Shared Infrastructure

**ffs_config.py:** Feature selection parameters (k_min, k_max, cv_folds, random_state)

**Pattern Plan Leaf Concept:**
- **Pattern Leaf:** Deepest operator within pattern structure
- **Plan Leaf:** Operator with no children in entire query plan
- **Pattern+Plan Leaf:** Operator that is both - Child features (st1, rt1, st2, rt2) always 0

## Workflow Execution Order

```
Pattern FFS (Baseline_SVM/SVM/two_step_evaluation_overview.csv)
    +
Pattern Plan Leaf Mapping (Data_Generation/04_pattern_plan_leafs_*.csv)
    |
    v
01_Clean_FFS.py
    |
    v
csv/01_cleaned_ffs_{timestamp}.csv  (Pattern+Plan Leaf child features removed)
    |
    v
03_Train_Models.py  (Train on cleaned FFS)
    |
    v
Model/{target}/{pattern_hash}/model.pkl  (144 models: 72 patterns x 2 targets)
    |
    v
04_Predict_Queries.py  (Optimized plan + Top-Down predictions)
    |
    v
csv/predictions.csv
    |
    +---> A_01a_Evaluate_Predictions.py ---> Root-level MRE metrics
    |
    +---> A_01b_Node_Evaluation.py ---> Node-level MRE by prediction_type
    |
    +---> A_01c_Time_Analysis.py ---> Operator range analysis
```

**Dependencies:**
- 01 requires: FFS CSV + Pattern Plan Leaf Mapping
- 02 skipped (FFS already done in Baseline_SVM)
- 03 requires: Cleaned FFS + Pattern Datasets
- 04 requires: Test Data + Pattern Info + Models (Pattern + Operator)
- A_01a requires: Predictions CSV
- A_01b requires: Predictions CSV
- A_01c requires: Operator Dataset

## Script Documentation

### 01 - Clean_FFS.py

**Purpose:** Remove child features from Pattern+Plan Leaf operators before training

**Rationale:**
Pattern Leafs that are also Plan Leafs have no children, so their child timing features (rt1, rt2, st1, st2) are always zero and should not be used for training. FFS adds these features without checking if the Pattern Leaf is also a Plan Leaf.

**Workflow:**
1. Load FFS overview CSV
2. Load Pattern Plan Leaf Mapping (from Data_Generation/04)
3. For each pattern-target combination:
   - Check Pattern Plan Leaf Mapping
   - If Pattern Leaf is Plan Leaf - Remove st1, rt1, st2, rt2 from final_features
4. Export cleaned FFS with corrected final_feature_count

**Inputs:**
- `ffs_csv` - FFS overview CSV (e.g., Baseline_SVM/SVM/two_step_evaluation_overview.csv)
- `pattern_plan_leafs_csv` - Pattern Plan Leaf Mapping from Data_Generation/04

**Outputs:**
- `csv/01_cleaned_ffs_{timestamp}.csv` - Cleaned FFS with removed Pattern+Plan Leaf child features

**Usage:**
```bash
python3 01_Clean_FFS.py \
  Baseline_SVM/SVM/two_step_evaluation_overview.csv \
  ../Data_Generation/csv/04_pattern_plan_leafs_20251123_231155.csv \
  --output-dir .
```

**Variables:**
- `--output-dir` (required): Output directory for cleaned FFS

**Example:**
Pattern `895c6e8c1a30a094329d71cef3111fbd`:
- Before: 9 features (incl. SeqScan_Outer_rt1, rt2, st1, st2)
- After: 5 features (removed SeqScan_Outer child features because Plan Leaf)

---

### 02 - Feature_Selection.py

**Purpose:** Run two-step Forward Feature Selection for all pattern-target combinations

**Workflow:**
1. For each pattern x target combination:
   - Load pattern training data
   - Extract available features (excluding non-feature columns)
   - Run forward feature selection with stratified CV
   - Export FFS results and selected features
2. Run two-step evaluation (add missing child features)
3. Export overview CSV

**Inputs:**
- `dataset_dir` - Directory containing pattern training datasets

**Outputs:**
- `SVM/{target}/{pattern}_csv/ffs_results_seed{N}.csv` - FFS iteration results
- `SVM/{target}/{pattern}_csv/selected_features_seed{N}.csv` - Selected features
- `SVM/{target}/{pattern}_csv/final_features.csv` - Final feature set (after two-step)
- `SVM/two_step_evaluation_overview.csv` - Overview of all pattern-target combinations

**Usage:**
```bash
python3 02_Feature_Selection.py \
  ../Datasets/Baseline \
  --output-dir .
```

**Variables:**
- `--output-dir` (required): Output directory for FFS results

---

### 03 - Train_Models.py

**Purpose:** Train SVM models for all pattern-target combinations using cleaned FFS

**Workflow:**
1. Load cleaned FFS overview CSV (from 01_Clean_FFS.py)
2. Load pattern training datasets (from Datasets/Baseline/{pattern_hash}/training_cleaned.csv)
3. For each pattern x target combination:
   - Extract features from cleaned FFS
   - Load training data
   - Create SVM pipeline (MaxAbsScaler + NuSVR)
   - Train model
   - Save to Model/{target}/{pattern_hash}/model.pkl

**Inputs:**
- `dataset_dir` - Path to Datasets/Baseline directory
- `overview_file` - Path to cleaned FFS CSV (from 01_Clean_FFS.py)

**Outputs:**
- `Model/{target}/{pattern_hash}/model.pkl` - Trained SVM models (144 models total)

**Usage:**
```bash
python3 03_Train_Models.py \
  ../Datasets/Baseline \
  csv/01_cleaned_ffs_20251123_231322.csv \
  --output-dir .
```

**Variables:**
- `--output-dir` (required): Output directory for trained models

**Model Parameters:**
- Kernel: RBF
- Nu: 0.65
- C: 1.5
- Gamma: scale
- Cache: 500 MB

---

### 04 - Predict_Queries.py

**Purpose:** Predict queries using optimized execution plan (Top-Down, Greedy Pattern Matching)

**Rationale:**
Implements the established logic from 02_create_optimized_plan.py: For each query, create an optimized execution plan using greedy pattern matching (largest patterns first, top-down), then execute the plan step-by-step, propagating child predictions upward.

**Workflow:**
1. Load test dataset, pattern info, plan leaf mapping, FFS features, models
2. For each query:
   - Build query tree from operators
   - Create optimized execution plan (Greedy, Top-Down, Hash-based pattern matching)
   - Execute plan step by step:
     - Pattern Steps: Aggregate pattern features + child predictions - Predict with Pattern Model
     - Operator Steps: Aggregate operator features + child predictions - Predict with Operator Model
   - Cache predictions for parent operators
3. Export all predictions to CSV

**Inputs:**
- `test_file` - Test dataset CSV
- `pattern_csv` - Pattern mining CSV (01_patterns_*.csv)
- `pattern_plan_leafs_csv` - Pattern Plan Leaf Mapping (04_pattern_plan_leafs_*.csv)
- `pattern_ffs_csv` - Cleaned Pattern FFS
- `operator_ffs_csv` - Operator FFS (from Operator_Level)
- `pattern_model_dir` - Pattern Model directory
- `operator_model_dir` - Operator Model directory (from Operator_Level)

**Outputs:**
- `csv/predictions.csv` - Predictions with columns:
  - query_file, node_id, node_type, depth, parent_relationship
  - actual_startup_time, actual_total_time
  - predicted_startup_time, predicted_total_time
  - prediction_type (pattern/operator)

**Usage:**
```bash
python3 04_Predict_Queries.py \
  /path/to/test.csv \
  ../Data_Generation/csv/01_patterns_20251123_170530.csv \
  ../Data_Generation/csv/04_pattern_plan_leafs_20251123_231155.csv \
  csv/01_cleaned_ffs_20251123_231322.csv \
  /path/to/Operator_Level/Runtime_Prediction/Baseline_SVM/SVM/two_step_evaluation_overview.csv \
  Model \
  /path/to/Operator_Level/Runtime_Prediction/Baseline_SVM/Model \
  --output-dir .
```

**Variables:**
- `--output-dir` (required): Output directory for predictions

**Key Features:**
- Hash-based pattern matching (not name-based)
- Top-Down greedy matching (largest patterns first)
- Pattern+Plan Leaf aware child feature handling
- Operator name mapping: `"Hash Join"` - `"Hash_Join"`

---

## Analysis Scripts

### A_01a - Evaluate_Predictions.py

**Purpose:** Evaluate root-level predictions and calculate query-level MRE by template

**Workflow:**
1. Load predictions CSV
2. Extract root operators (depth=0)
3. Calculate MRE: |predicted - actual| / actual
4. Compute overall MRE and per-template statistics
5. Export metrics to CSV
6. Create MRE bar plot by template

**Inputs:**
- `predictions_file` - Predictions CSV from 04_Predict_Queries.py

**Outputs:**
- `overall_mre.csv` - Overall mean relative error
- `template_mre.csv` - MRE statistics per template
- `template_mre_plot.png` - Bar plot of MRE by template

**Usage:**
```bash
python3 A_01a_Evaluate_Predictions.py \
  csv/predictions.csv \
  --output-dir results
```

**Variables:**
- `--output-dir` (required): Output directory for evaluation results

---

### A_01b - Node_Evaluation.py

**Purpose:** Node-level evaluation split by prediction type (pattern/operator/passthrough)

**Workflow:**
1. Load predictions CSV
2. Calculate MRE for startup_time and total_time
3. Split by prediction_type (pattern/operator/passthrough)
4. Create pivot tables: node_type x template for each prediction type
5. Export 6+ CSV files with MRE percentages

**Inputs:**
- `predictions_file` - Predictions CSV from 04_Predict_Queries.py

**Outputs:**
- `csv/pattern_mean_mre_total_pct_{timestamp}.csv`
- `csv/pattern_mean_mre_startup_pct_{timestamp}.csv`
- `csv/operator_mean_mre_total_pct_{timestamp}.csv`
- `csv/operator_mean_mre_startup_pct_{timestamp}.csv`
- `csv/node_type_mean_mre_total_pct_{timestamp}.csv`
- `csv/node_type_mean_mre_startup_pct_{timestamp}.csv`

**Usage:**
```bash
python3 A_01b_Node_Evaluation.py \
  csv/predictions.csv \
  --output-dir results
```

**Variables:**
- `--output-dir` (required): Output directory for node evaluation results

---

### A_01c - Time_Analysis.py

**Purpose:** Analyze operator runtime ranges across templates (independent analysis)

**Workflow:**
1. Load operator dataset
2. Add template column
3. Compute mean, min, max statistics per operator
4. Identify templates with min/max values
5. Calculate range metrics (absolute and percentage)
6. Export sorted by total_range_ms (descending)

**Inputs:**
- `input_file` - Operator dataset CSV

**Outputs:**
- `operator_range_analysis_{timestamp}.csv` - Operator statistics with range metrics

**Usage:**
```bash
python3 A_01c_Time_Analysis.py \
  /path/to/operator_dataset.csv \
  --output-dir analysis
```

**Variables:**
- `--output-dir` (required): Output directory for analysis results

**Note:** This script is independent of the prediction workflow and can be run on any operator dataset.
