# Runtime_Prediction - Pattern Model Training and Hybrid Prediction

Performs forward feature selection, trains pattern-level SVM models, and executes hybrid bottom-up prediction. Uses baseline test data (excludes templates Q2, Q11, Q16, Q22 with InitPlan/SubPlan operators).

## Directory Structure

```
Runtime_Prediction/
├── ffs_config.py                       # SVM hyperparameters and FFS settings
├── 01_Feature_Selection.py             # Forward feature selection for patterns
├── 01b_Feature_Selection_Operators.py  # Forward feature selection for operators
├── 02_Train_Models.py                  # Train SVM models for patterns
├── 02b_Train_Models_Operators.py       # Train SVM models for operators
├── 03_Predict_Queries/                 # Hybrid bottom-up prediction (modular)
├── A_01a_Evaluate_Predictions.py       # [analysis] Query-level MRE evaluation
├── A_01b_Node_Evaluation.py            # [analysis] Node type evaluation by source
├── A_01c_Time_Analysis.py              # [analysis] Operator time range analysis
├── A_01d_Depth_Propagation.py          # [analysis] Depth propagation visualization
├── md/                                 # [outputs] Query prediction MD reports
└── Baseline_SVM/                       # [outputs] SVM baseline outputs
    ├── SVM/
    │   ├── two_step_evaluation_overview.csv   # Pattern FFS results
    │   ├── operator_overview.csv               # Operator FFS results
    │   ├── execution_time/
    │   │   ├── {pattern_hash}_csv/            # Pattern FFS
    │   │   └── operators/{type}_csv/          # Operator FFS
    │   └── start_time/...
    ├── Model/
    │   ├── execution_time/
    │   │   ├── {pattern_hash}/model.pkl       # Pattern models
    │   │   └── operators/{type}/model.pkl     # Operator models
    │   └── start_time/...
    └── Evaluation/
        ├── predictions.csv
        ├── overall_mre.csv
        ├── template_mre.csv
        └── csv/...
```

## Shared Infrastructure

**ffs_config.py:**
- `SEED` - Random seed for reproducibility (42)
- `MIN_FEATURES` - Minimum features to select (1)
- `SVM_PARAMS` - NuSVR hyperparameters (kernel, nu, C, gamma, cache_size)

**Constants from mapping_config.py:**
- `TARGET_TYPES` - ['execution_time', 'start_time']
- `NON_FEATURE_SUFFIXES` - Columns to exclude from features
- `FFS_SEED` - Random seed for cross-validation (42)
- `FFS_MIN_FEATURES` - Minimum features to select (1)

## Workflow Execution Order

```
01  - Feature_Selection           [Pattern datasets → SVM/ FFS results]
01b - Feature_Selection_Operators [Operator datasets → SVM/operators/ FFS results]
     ↓
02  - Train_Models                [Pattern overview → Model/{pattern}/model.pkl]
02b - Train_Models_Operators      [Operator overview → Model/operators/{type}/model.pkl]
     ↓
03  - Predict_Queries             [Test data + All models → predictions.csv]
```

## Analysis Scripts

```
A_01a - Evaluate_Predictions  [predictions.csv → MRE metrics, optional baseline comparison]
A_01b - Node_Evaluation       [predictions.csv → Node type analysis by source]
A_01c - Time_Analysis         [operator_dataset.csv → Operator range statistics]
A_01d - Depth_Propagation     [predictions.csv → Depth propagation plots per plan]
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

### 01b - Feature_Selection_Operators.py

**Purpose:** Perform two-step forward feature selection for all operator-target combinations

**Workflow:**
1. For each operator-target combination:
   - Load training data
   - Extract available features (exclude metadata and targets)
   - Perform forward feature selection with stratified CV
   - Select features that improve MRE
2. Add missing child timing features (st1, rt1, st2, rt2)
3. Export FFS results, selected features, and overview

**Inputs:**
- `dataset_dir` - Directory containing operator training datasets (positional)

**Outputs:**
- `{output-dir}/SVM/{target}/operators/{Operator}_csv/ffs_results_seed42.csv`
- `{output-dir}/SVM/{target}/operators/{Operator}_csv/selected_features_seed42.csv`
- `{output-dir}/SVM/{target}/operators/{Operator}_csv/final_features.csv`
- `{output-dir}/SVM/operator_overview.csv`

**Usage:**
```bash
python 01b_Feature_Selection_Operators.py ../Datasets/Baseline_SVM --output-dir Baseline_SVM
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

### 02b - Train_Models_Operators.py

**Purpose:** Train SVM models for each operator-target combination

**Workflow:**
1. Load operator feature selection overview
2. For each operator-target combination:
   - Load training data
   - Extract final selected features
   - Train NuSVR model with MaxAbsScaler
   - Save model pipeline to pickle file

**Inputs:**
- `dataset_dir` - Path to directory with operator training datasets (positional)
- `overview_file` - Path to operator_overview.csv (positional)

**Outputs:**
- `{output-dir}/Model/{target}/operators/{Operator}/model.pkl` per operator-target

**Usage:**
```bash
python 02b_Train_Models_Operators.py ../Datasets/Baseline_SVM Baseline_SVM/SVM/operator_overview.csv --output-dir Baseline_SVM
```

**Variables:**
- `--output-dir` - Path to output directory (required)

---

### 03 - Predict_Queries/

**Purpose:** Execute hybrid bottom-up prediction on test queries with multi-depth pattern matching

**Structure:** Modular directory with entry-point and src/ modules.

```
03_Predict_Queries/
├── 03_Predict_Queries.py    # Entry point
└── src/
    ├── tree.py              # QueryNode class, multi-depth hash, pattern assignment
    ├── io.py                # Load patterns.csv, models, features
    ├── prediction.py        # Two-phase prediction, passthrough logic
    └── report.py            # MD report generation
```

**Algorithm (Two-Phase Multi-Depth Pattern Matching):**

Phase 1 - Pattern Assignment:
1. Load patterns from patterns.csv, sort by pattern_length descending, then occurrence_count descending
2. For each pattern (longest first, ties broken by frequency):
   - Find all query nodes matching the pattern hash
   - Mark matched nodes as consumed (prevents overlap)
   - Assign pattern to root node of match
3. Single-pattern constraint: If only one pattern matches AND it consumes all nodes, discard pattern assignment and use operator-only prediction

Phase 2 - Bottom-Up Prediction:
1. Traverse nodes by depth (deepest first)
2. For each node:
   - If assigned to pattern -> use pattern model for root prediction
   - Else if passthrough enabled AND node is passthrough operator -> copy child prediction
   - Else -> use operator model
3. Cache predictions for child feature propagation (st1/rt1/st2/rt2)

**Passthrough Operators:** Incremental Sort, Gather Merge, Gather, Sort, Limit, Merge Join
When --passthrough flag is set, these operators copy their child's prediction if not part of a pattern.

**Inputs:**
- `test_file` - Path to baseline test.csv (positional)
- `patterns_csv` - Path to patterns.csv with pattern_hash and pattern_length (positional)
- `pattern_overview` - Path to pattern FFS overview (two_step_evaluation_overview.csv) (positional)
- `operator_overview` - Path to operator overview (operator_overview.csv) (positional)
- `model_dir` - Path to Model directory (positional)

**Outputs:**
- `{output-dir}/predictions.csv`
  - Columns: query_file, node_id, node_type, depth, parent_relationship, subplan_name, actual_startup_time, actual_total_time, predicted_startup_time, predicted_total_time, prediction_type (pattern/operator/passthrough), pattern_hash
- `{output-dir}/patterns.csv` - Pattern usage summary (pattern_hash, usage_count, node_types)
- `{output-dir}/md/03_{template}_{plan_hash[:8]}_{timestamp}.md` - One MD report per unique plan structure (with --report flag)

**Usage:**
```bash
# All queries for approach_1
python 03_Predict_Queries/03_Predict_Queries.py \
  ../Datasets/Baseline_SVM/test.csv \
  ../Datasets/Baseline_SVM/approach_1/patterns.csv \
  Baseline_SVM/SVM/Patterns/two_step_evaluation_overview.csv \
  Baseline_SVM/SVM/Operators/operator_overview.csv \
  Baseline_SVM/Model \
  --output-dir Baseline_SVM/Predictions/approach_1

# With passthrough enabled
python 03_Predict_Queries/03_Predict_Queries.py \
  ../Datasets/Baseline_SVM/test.csv \
  ../Datasets/Baseline_SVM/approach_2/patterns.csv \
  Baseline_SVM/SVM/Patterns/two_step_evaluation_overview.csv \
  Baseline_SVM/SVM/Operators/operator_overview.csv \
  Baseline_SVM/Model \
  --output-dir Baseline_SVM/Predictions/approach_2 \
  --passthrough
```

**Variables:**
- `--output-dir` - Path to output directory for predictions (required)
- `--passthrough` - Enable passthrough for non-pattern passthrough operators (optional)
- `--report` - Generate MD report for first query of each unique plan structure (optional)

---

### A_01a - Evaluate_Predictions.py

**Purpose:** Evaluate query-level prediction accuracy using MRE, optionally compare against baseline

**Workflow:**
1. Load predictions
2. Calculate MRE per query (sum actuals vs sum predictions)
3. Group by template for template-level analysis
4. Calculate overall MRE
5. If --compare: Load baseline MRE, calculate delta (baseline - hybrid)
6. Generate template MRE plot

**Inputs:**
- `predictions_file` - Path to predictions.csv (positional)

**Outputs:**
- `{output-dir}/overall_mre.csv`
- `{output-dir}/template_mre.csv`
  - Additional columns when --compare used: baseline_mre_pct, delta_mre_pct, delta_formula
- `{output-dir}/template_mre_plot.png`

**Usage:**
```bash
# Basic evaluation
python A_01a_Evaluate_Predictions.py Baseline_SVM/Evaluation/predictions.csv --output-dir Baseline_SVM/Evaluation

# With baseline comparison
python A_01a_Evaluate_Predictions.py Baseline_SVM/Evaluation/predictions.csv --output-dir Baseline_SVM/Evaluation --compare ../../Operator_Level/Runtime_Prediction/Baseline_SVM/Evaluation/A_01f_template_mre.csv
```

**Variables:**
- `--output-dir` - Path to output directory (required)
- `--compare` - Path to baseline template_mre.csv for delta calculation (optional)

---

### A_01b - Node_Evaluation.py

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
python A_01b_Node_Evaluation.py Baseline_SVM/Evaluation/predictions.csv --output-dir Baseline_SVM/Evaluation
```

**Variables:**
- `--output-dir` - Path to Evaluation directory (required)

---

### A_01c - Time_Analysis.py

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
python A_01c_Time_Analysis.py ../../Operator_Level/Datasets/Baseline/03_training.csv --output-dir Baseline_SVM/Evaluation
```

**Variables:**
- `--output-dir` - Output directory for analysis results (required)

---

### A_01d - Depth_Propagation.py

**Purpose:** Visualize actual vs predicted times across depth levels per query plan

**Workflow:**
1. Load structure CSV for correct plan hash calculation
2. Load predictions
3. Compute plan_hash per query from structure (based on node_type, depth, parent_relationship)
4. Group by plan_hash and depth, calculate mean actual/predicted times
5. Generate line plot with automatic label positioning (adjustText)

**Inputs:**
- `structure_csv` - Path to structure CSV (test.csv) for correct plan hash calculation (positional)
- `predictions_csv` - Path to predictions.csv (positional)

**Outputs:**
- `{output-dir}/A_01d_depth_{template}_{plan_hash[:8]}.png` per unique plan within template

**Usage:**
```bash
python A_01d_Depth_Propagation.py ../Datasets/Baseline_SVM/test.csv Baseline_SVM/Predictions/approach_1/predictions.csv --output-dir Baseline_SVM/Evaluation/approach_1
```

**Variables:**
- `--output-dir` - Output directory (required)
