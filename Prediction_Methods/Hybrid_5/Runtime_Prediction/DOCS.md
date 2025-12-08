# Runtime Prediction - Module Documentation

## Directory Structure

```
Runtime_Prediction/
├── 01_Feature_Selection.py        # Forward Feature Selection for patterns
├── 02_Train_Models.py             # Train SVM models for pattern predictions
├── 03_Predict_Queries.py          # Bottom-up prediction with pattern/operator fallback
├── A_01a_Evaluate_Predictions.py  # Evaluate root-level predictions (MRE)
├── A_01b_Node_Evaluation.py       # Node-level evaluation split by prediction type
├── A_01c_Time_Analysis.py         # Operator range analysis
├── ffs_config.py                  # Feature selection configuration
├── csv/                           # Script outputs
│   └── predictions.csv            [outputs]
├── Baseline_SVM/                  # Feature selection and model outputs
│   ├── SVM/
│   │   ├── two_step_evaluation_overview.csv
│   │   └── {target}/{pattern}_csv/
│   └── Model/
│       ├── execution_time/{pattern}/model.pkl
│       └── start_time/{pattern}/model.pkl
└── DOCS.md                        # This file
```

## Shared Infrastructure

**ffs_config.py:** Feature selection parameters
- `SEED` - Random seed for cross-validation (42)
- `MIN_FEATURES` - Minimum features to select (1)
- `SVM_PARAMS` - NuSVR hyperparameters (kernel, nu, C, gamma, cache_size)

**Parent Module:** `../mapping_config.py`
- `build_pattern_hash_map()` - Map folder names to pattern hashes
- `TARGET_TYPES` - Target variables (execution_time, start_time)
- `NON_FEATURE_SUFFIXES` - Metadata columns to exclude from features
- `is_passthrough_operator()` - Check if operator inherits child prediction

## Workflow Execution Order

```
Datasets/patterns/<hash>/training_cleaned.csv
    |
    v
01_Feature_Selection.py (uses build_pattern_hash_map)
    |
    v
Baseline_SVM/SVM/two_step_evaluation_overview.csv
    |
    v
02_Train_Models.py (uses build_pattern_hash_map)
    |
    v
Baseline_SVM/Model/{target}/{pattern}/model.pkl
    |
    v
03_Predict_Queries.py (bottom-up: pattern -> passthrough -> operator)
    |
    v
predictions.csv
    |
    +---> A_01a_Evaluate_Predictions.py ---> Root-level MRE metrics
    |
    +---> A_01b_Node_Evaluation.py ---> Node-level MRE by prediction_type
    |
    +---> A_01c_Time_Analysis.py ---> Operator range analysis
```

**Dependencies:**
- 01 requires: Datasets/patterns/ with training_cleaned.csv and pattern_info.json
- 02 requires: 01 output (overview CSV) + Datasets/patterns/
- 03 requires: Test data + 01 overview + 02 models + Operator_Level models

## Script Documentation

### 01 - Feature_Selection.py

**Purpose:** Run two-step Forward Feature Selection for all pattern-target combinations

**Key Feature:** Uses `build_pattern_hash_map()` to discover patterns dynamically from pattern_info.json files

**Workflow:**
1. Build pattern hash map from patterns/<hash>/pattern_info.json
2. For each pattern x target combination:
   - Load training_cleaned.csv using hash mapping
   - Extract available features (excluding NON_FEATURE_SUFFIXES)
   - Run forward feature selection with stratified 5-fold CV
   - Export FFS results
3. Run two-step evaluation (add missing child features)
4. Export overview CSV

**Inputs:**
- `dataset_dir` - Directory containing patterns/ subfolder

**Outputs:**
- `SVM/{target}/{pattern}_csv/ffs_results_seed{N}.csv` - FFS iteration results
- `SVM/{target}/{pattern}_csv/selected_features_seed{N}.csv` - Selected features
- `SVM/{target}/{pattern}_csv/final_features.csv` - Final feature set
- `SVM/two_step_evaluation_overview.csv` - Overview of all pattern-target combinations

**Usage:**
```bash
python3 01_Feature_Selection.py <dataset_dir> --output-dir <output_directory>
```

**Example:**
```bash
python3 01_Feature_Selection.py ../Datasets --output-dir Baseline_SVM
```

**Variables:**
- `--output-dir` (required): Output directory for FFS results

---

### 02 - Train_Models.py

**Purpose:** Train SVM models for all pattern-target combinations

**Workflow:**
1. Build pattern hash map from patterns/
2. Load feature selection overview CSV
3. For each pattern x target combination:
   - Extract features from overview
   - Load training_cleaned.csv using hash mapping
   - Create SVM pipeline (MaxAbsScaler + NuSVR)
   - Train model and save to Model/{target}/{pattern}/model.pkl

**Inputs:**
- `dataset_dir` - Directory containing patterns/ subfolder
- `overview_file` - Path to two_step_evaluation_overview.csv

**Outputs:**
- `Model/{target}/{pattern}/model.pkl` - Trained SVM models

**Usage:**
```bash
python3 02_Train_Models.py <dataset_dir> <overview_file> --output-dir <output_directory>
```

**Example:**
```bash
python3 02_Train_Models.py ../Datasets Baseline_SVM/SVM/two_step_evaluation_overview.csv \
  --output-dir Baseline_SVM
```

**Variables:**
- `--output-dir` (required): Output directory for trained models

**Model Parameters (from ffs_config.py):**
- Kernel: RBF
- Nu: 0.65
- C: 1.5
- Gamma: scale
- Cache: 500 MB

---

### 03 - Predict_Queries.py

**Purpose:** Bottom-up prediction with pattern matching and operator fallback

**Prediction Strategy (Bottom-Up):**
1. Start from deepest depth, work up to root
2. For each operator at current depth:
   - Try to match parent + children as pattern -> pattern model
   - If passthrough operator -> inherit child prediction
   - Otherwise -> operator model (fallback)
3. Cache predictions for parent operators to use

**Workflow:**
1. Load test data, pattern features, operator features, models
2. For each query:
   - Filter to main plan (exclude subplans)
   - Sort by node_id
   - Predict bottom-up from max depth to 0
   - Cache predictions for use by parent operators
3. Export all predictions

**Inputs:**
- `test_file` - Test dataset CSV
- `pattern_overview` - Pattern FFS overview CSV
- `operator_overview` - Operator FFS overview CSV (from Operator_Level)
- `pattern_model_dir` - Pattern Model directory
- `operator_model_dir` - Operator Model directory (from Operator_Level)

**Outputs:**
- `predictions.csv` - Predictions with columns:
  - query_file, node_id, node_type, depth, parent_relationship
  - actual_startup_time, actual_total_time
  - predicted_startup_time, predicted_total_time
  - prediction_type (pattern/passthrough/operator)

**Usage:**
```bash
python3 03_Predict_Queries.py <test_file> <pattern_overview> <operator_overview> \
  <pattern_model_dir> <operator_model_dir> --output-dir <output_directory>
```

**Example:**
```bash
python3 03_Predict_Queries.py \
  ../Datasets/test.csv \
  Baseline_SVM/SVM/two_step_evaluation_overview.csv \
  ../../Operator_Level/Runtime_Prediction/Baseline_SVM/SVM/two_step_evaluation_overview.csv \
  Baseline_SVM/Model \
  ../../Operator_Level/Runtime_Prediction/Baseline_SVM/Model \
  --output-dir .
```

**Variables:**
- `--output-dir` (required): Output directory for predictions

**Pattern Matching:**
Pattern key built from: `{parent_type}_{child1_type}_{child1_rel}_{child2_type}_{child2_rel}`
- Example: `Hash_Join_Seq_Scan_Outer_Hash_Inner`

---

## Analysis Scripts

### A_01a - Evaluate_Predictions.py

**Purpose:** Evaluate root-level predictions and calculate query-level MRE by template

**Outputs:**
- `overall_mre.csv` - Overall mean relative error
- `template_mre.csv` - MRE statistics per template
- `template_mre_plot.png` - Bar plot of MRE by template

**Usage:**
```bash
python3 A_01a_Evaluate_Predictions.py <predictions_file> --output-dir <output_dir>
```

---

### A_01b - Node_Evaluation.py

**Purpose:** Node-level evaluation split by prediction type (pattern/operator/passthrough)

**Outputs:**
- `csv/pattern_mean_mre_total_pct_{timestamp}.csv`
- `csv/pattern_mean_mre_startup_pct_{timestamp}.csv`
- `csv/operator_mean_mre_total_pct_{timestamp}.csv`
- `csv/operator_mean_mre_startup_pct_{timestamp}.csv`
- `csv/node_type_mean_mre_total_pct_{timestamp}.csv`
- `csv/node_type_mean_mre_startup_pct_{timestamp}.csv`

**Usage:**
```bash
python3 A_01b_Node_Evaluation.py <predictions_file> --output-dir <output_dir>
```

---

### A_01c - Time_Analysis.py

**Purpose:** Analyze operator runtime ranges across templates

**Outputs:**
- `operator_range_analysis_{timestamp}.csv`

**Usage:**
```bash
python3 A_01c_Time_Analysis.py <operator_dataset> --output-dir <output_dir>
```

---

## Notes

**Hash-Based Pattern Access:**
- Scripts use `build_pattern_hash_map()` to dynamically discover patterns
- Maps human-readable folder names to MD5 hashes
- No hardcoded pattern list needed in scripts

**Bottom-Up Prediction Order:**
1. Predict deepest operators first
2. Cache predictions in `predictions[(node_type, depth)]`
3. Use cached predictions as child features for parent operators
4. Passthrough operators inherit child prediction directly
