# Operator_Level - DOCS.md

LOTO Operator-Level runtime prediction using bottom-up approach with child-timing propagation.

---

## Directory Structure

```
Operator_Level/
├── DOCS.md
├── mapping_config.py
├── ffs_config.py
├── 01_Forward_Selection.py
├── 02_Train_Models.py
├── 03_Predict.py
├── SVM/{template}/
│   ├── two_step_evaluation_overview.csv
│   └── {target}/{operator}_csv/
└── Model/{template}/{target}/{operator}/
    └── model.pkl
```

---

## Methodology

**Models:** 26 NuSVR models per template (13 operators x 2 targets)

**Targets:**
- `start_time` -> actual_startup_time
- `execution_time` -> actual_total_time

**Prediction:** Bottom-up with child-timing propagation
1. Predict leaf operators (Seq Scan, Index Scan, Index Only Scan)
2. Propagate predicted times (st1, rt1, st2, rt2) to parent operators
3. Predict parent operators using propagated child times

---

## ffs_config.py

**Purpose:** FFS and SVM configuration parameters.

**Exports:**
- `SEED`: Cross-validation random seed (42)
- `MIN_FEATURES`: Minimum features before evaluating improvement (1)
- `SVM_PARAMS`: NuSVR hyperparameters (kernel, nu, C, gamma, cache_size)

---

## mapping_config.py

**Purpose:** Operator types, feature sets, and target mappings.

**Exports:**
- `OPERATOR_FEATURES`: Base operator features
- `OPERATOR_TARGETS`: Target columns
- `OPERATOR_METADATA`: Non-feature columns
- `CHILD_FEATURES`: Child timing features (st1, rt1, st2, rt2, nt1, nt2)
- `LEAF_OPERATORS`: Scan operators without children
- `TARGET_NAME_MAP`: Maps target type to column name
- `csv_name_to_folder_name()`: Converts operator name to folder format

---

## 01_Forward_Selection.py

**Purpose:** Run two-step forward feature selection for all operator-target combinations.

**Input:** Template training.csv (positional), --template

**Output:** SVM/{template}/ with FFS results and feature lists

**Usage:**
```bash
python3 01_Forward_Selection.py \
  ../../../Dataset_Operator/Q1/training.csv \
  --output-dir . \
  --template Q1
```

### run_ffs_workflow()
Orchestrator that loads data, runs FFS for all operators, exports overview.

### load_training_data()
Loads training CSV with semicolon delimiter.

### collect_operator_results()
Iterates through all operator-target combinations and collects FFS results.

### process_operator_target()
Runs FFS for single operator-target: filters data, performs selection, evaluates two-step.

### filter_operator_data()
Filters DataFrame to rows matching specific node_type.

### prepare_features_and_target()
Extracts feature columns and target from DataFrame.

### perform_forward_selection()
Greedy forward feature selection with cross-validated MRE evaluation.

### evaluate_feature_set()
Cross-validates feature set using NuSVR pipeline and MRE scorer.

### identify_missing_child_features()
Finds child features (st1, rt1, st2, rt2) not selected by FFS.

### evaluate_operator_two_step()
Evaluates FFS-only features vs FFS + missing child features.

### export_final_features()
Saves final feature list (FFS + missing child) to CSV.

### generate_two_step_overview()
Creates DataFrame with all operator-target results.

### export_two_step_overview()
Saves overview CSV with feature counts, MRE scores, and feature lists.

---

## 02_Train_Models.py

**Purpose:** Train NuSVR models for all operator-target combinations.

**Input:** Template training.csv, FFS overview CSV, --template

**Output:** Model/{template}/{target}/{operator}/model.pkl

**Usage:**
```bash
python3 02_Train_Models.py \
  ../../../Dataset_Operator/Q1/training.csv \
  SVM/Q1/two_step_evaluation_overview.csv \
  --output-dir . \
  --template Q1
```

### train_all_models_workflow()
Orchestrator that loads data and trains models for all operator-target pairs.

### load_training_data()
Loads training CSV with semicolon delimiter.

### load_overview()
Loads FFS overview CSV with feature selections.

### train_single_model()
Trains single NuSVR model: gets features, filters data, creates pipeline, saves model.

### filter_operator_data()
Filters DataFrame to rows matching specific node_type.

### get_selected_features()
Extracts final features from overview for operator-target pair.

### prepare_training_data()
Extracts X (features) and y (target) from training data.

### create_and_train_pipeline()
Creates MaxAbsScaler + NuSVR pipeline and fits on training data.

### save_model()
Saves trained pipeline to Model/{template}/{target}/{operator}/model.pkl.

---

## 03_Predict.py

**Purpose:** Bottom-up prediction with child-timing propagation.

**Input:** Template test.csv, FFS overview, models directory

**Output:** predictions.csv with actual and predicted times

**Usage:**
```bash
python3 03_Predict.py \
  ../../../Dataset_Operator/Q1/test.csv \
  SVM/Q1/two_step_evaluation_overview.csv \
  Model/Q1 \
  --output-file predictions/Q1_predictions.csv
```

### run_prediction_workflow()
Orchestrator that loads data and models, predicts all queries, exports results.

### load_test_data()
Loads test CSV with semicolon delimiter.

### predict_all_queries()
Iterates through unique queries and collects all operator predictions.

### predict_single_query()
Predicts all operators in a query using bottom-up approach.

### filter_main_plan_operators()
Filters out SubPlan/InitPlan operators (subplan_name column).

### build_children_map()
Creates mapping of node_id to list of children with relationships (Outer/Inner).

### predict_operators_bottom_up()
Core prediction logic: predicts leaves first, then propagates child times upward.

### load_model()
Loads trained model from Model/{target}/{operator}/model.pkl.

### get_model_features()
Extracts final features from overview for operator-target pair.

### build_feature_vector()
Creates feature vector with operator features and child timing values.

### export_predictions()
Saves predictions DataFrame to CSV with semicolon delimiter.

---

## Execution Flow (per Template)

```bash
# 1. Forward Selection
python3 01_Forward_Selection.py ../../../Dataset_Operator/Q1/training.csv --output-dir . --template Q1

# 2. Train Models
python3 02_Train_Models.py ../../../Dataset_Operator/Q1/training.csv SVM/Q1/two_step_evaluation_overview.csv --output-dir . --template Q1

# 3. Predict
python3 03_Predict.py ../../../Dataset_Operator/Q1/test.csv SVM/Q1/two_step_evaluation_overview.csv Model/Q1 --output-file predictions/Q1_predictions.csv

# 4. Evaluate (shared scripts)
python3 ../A_01_Evaluate_Template.py predictions/Q1_predictions.csv --template Q1
```
