# Baseline SVM - Operator-Level Runtime Prediction

Workflow für SVM-basierte Runtime-Vorhersage auf Operator-Ebene mit Two-Step Forward Feature Selection.

---

## Directory Structure

```
Runtime_Prediction/
├── 00_Forward_Selection.py          # Two-step forward feature selection for all operators
├── 01_Train_Models.py                # Train SVM models for all operator-target combinations
├── 02_Bottom_Up_Prediction.py        # Bottom-up prediction workflow on test set
├── 03_Node_Type_Evaluation.py        # Cross-evaluation of node type prediction accuracy
├── 04_Operator_Time_Analysis.py      # Statistical analysis of operator timing patterns
├── evaluate_query_predictions.py     # Evaluate query-level predictions and create visualizations
├── ffs_config.py                     # FFS-specific configuration (seed, params, features)
├── README.md                          # This file
├── csv/                               # Output directory for analysis results
│   └── [outputs]                      # Generated CSV and PNG files
├── execution_time/                    # Trained models for execution time prediction
│   └── {Operator}/                    # One folder per operator type
│       └── model.pkl                  # Trained SVM model
└── start_time/                        # Trained models for start time prediction
    └── {Operator}/                    # One folder per operator type
        └── model.pkl                  # Trained SVM model
```

**External Config**:
- `/Operator_Level/mapping_config.py` - Zentrale Mapping-Konfiguration

---

## Shared Infrastructure

### mapping_config.py (Operator_Level Root)

Zentrale Konfiguration für alle Operator-Level Workflows.

**Constants**:
- `OPERATOR_FEATURES` - Liste der 10 Operator Features
- `OPERATOR_TARGETS` - Liste der 2 Target Columns
- `OPERATOR_METADATA` - Liste der 6 Metadata Columns
- `CHILD_FEATURES` - Child Prediction Features (st1, rt1, st2, rt2, nt1, nt2)
- `TARGET_NAME_MAP` - Mapping: execution_time/start_time → actual_total_time/actual_startup_time
- `TARGET_TYPES` - ['execution_time', 'start_time']
- `OPERATOR_CSV_TO_FOLDER` - Mapping: CSV Namen (mit Spaces) → Folder Namen (mit Underscores)
- `OPERATORS_CSV_NAMES` - Liste der 13 Operator Namen (CSV Format)
- `OPERATORS_FOLDER_NAMES` - Liste der 13 Operator Namen (Folder Format)
- `LEAF_OPERATORS` - Liste der 3 Leaf Operators

**Functions**:
- `csv_name_to_folder_name(csv_name)` - Convert "Gather Merge" → "Gather_Merge"
- `folder_name_to_csv_name(folder_name)` - Convert "Gather_Merge" → "Gather Merge"
- `is_leaf_operator(operator_csv_name)` - Check if operator is leaf
- `get_all_columns()` - Return Features + Targets + Metadata
- `get_feature_columns()` - Return only Features

**Used by**: All scripts (00-04)

---

### ffs_config.py (SVM Folder)

FFS-spezifische Konfiguration.

**Constants**:
- `SEED` - Random seed (42)
- `MIN_FEATURES` - Minimum features for selection (1)
- `SPARSE_FEATURES_MAP` - Features to exclude for Seq_Scan, Index_Scan, Index_Only_Scan
- `SVM_PARAMS` - NuSVR hyperparameters (kernel, nu, C, gamma, cache_size)

**Used by**: 00_Forward_Selection.py, 01_Train_Models.py

---

## Workflow Execution Order

```
Input: Training Dataset (from Datasets/Baseline)
   ↓
[00] forward_selection.py
   ↓
two_step_evaluation_overview.csv
   ↓
[01] 01_Train_Models.py
   ↓
Model Files (execution_time/{operator}/model.pkl, start_time/{operator}/model.pkl)
   ↓
[02] 02_Bottom_Up_Prediction.py
   ↓
predictions.csv
   ↓
┌─────────────────────────┬──────────────────────────┐
│                         │                          │
[03] 03_Node_Type_Evaluation.py    [04] 04_Operator_Time_Analysis.py
│                         │                          │
CSV Outputs               CSV Outputs
```

---

## Script Documentation

### 00 - forward_selection.py

**Purpose**: Two-Step Forward Feature Selection für alle Operator-Target Kombinationen.

**Workflow**:
1. FFS bis natural stopping point
2. Identifiziere fehlende Child Features
3. Final Features = FFS Features + Missing Child Features
4. Evaluiere beide Feature-Sets (MRE Vergleich)
5. Exportiere Overview mit Performance-Metriken

**Inputs**:
- `dataset_dir` - Base directory mit Operator Training Folders
- `output_dir` - Output directory für FFS Results

**Outputs** (pro Operator-Target):
- `{target}/{operator}_csv/ffs_results_seed42.csv` - FFS Iteration Trace
- `{target}/{operator}_csv/selected_features_seed42.csv` - FFS Selected Features
- `{target}/{operator}_csv/final_features.csv` - Final Features (FFS + Child)
- `two_step_evaluation_overview.csv` - Performance Overview

**Usage**:
```bash
python3 forward_selection.py <dataset_dir> <output_dir>
```

**Example**:
```bash
python3 forward_selection.py \
    ../../../Datasets/Baseline/Training \
    ./ffs_results
```

---

### 01 - 01_Train_Models.py

**Purpose**: Trainiert SVM Models für alle 26 Operator-Target Kombinationen (13 Operators × 2 Targets).

**Inputs**:
- `dataset_dir` - Base directory mit Operator Training CSVs
- `overview_file` - Path zu two_step_evaluation_overview.csv
- `--output-dir` - Output directory für trainierte Models

**Outputs**:
- `{output_dir}/{target}/{operator}/model.pkl` - Trainiertes SVM Pipeline (Scaler + NuSVR)

**Usage**:
```bash
python3 01_Train_Models.py <dataset_dir> <overview_file> --output-dir <output_dir>
```

**Example**:
```bash
python3 01_Train_Models.py \
    ../../../Datasets/Baseline/Training \
    ../SVM/ffs_results/two_step_evaluation_overview.csv \
    --output-dir ./trained_models
```

---

### 02 - 02_Bottom_Up_Prediction.py

**Purpose**: Bottom-Up Prediction auf Test Set mit Child Feature Propagation.

**Workflow**:
1. Predict Leaf Operators (Seq Scan, Index Scan, Index Only Scan)
2. Propagate Child Predictions (st1, rt1, st2, rt2) bottom-up
3. Predict Parent Operators mit Child Features

**Inputs**:
- `test_file` - Path zu Test Dataset CSV
- `overview_file` - Path zu two_step_evaluation_overview.csv
- `models_dir` - Directory mit trainierten Models
- `--output-file` - Output CSV für Predictions

**Outputs**:
- Predictions CSV mit Columns:
  - query_file, node_id, node_type, depth, parent_relationship, subplan_name
  - actual_startup_time, actual_total_time
  - predicted_startup_time, predicted_total_time

**Usage**:
```bash
python3 02_Bottom_Up_Prediction.py <test_file> <overview_file> <models_dir> --output-file <output_file>
```

**Example**:
```bash
python3 02_Bottom_Up_Prediction.py \
    ../../../Datasets/Baseline/Test/test.csv \
    ../SVM/ffs_results/two_step_evaluation_overview.csv \
    ./trained_models \
    --output-file ./predictions/predictions.csv
```

---

### 03 - 03_Node_Type_Evaluation.py

**Purpose**: Cross-Evaluation von MRE per Node Type und Template.

**Workflow**:
1. Calculate MRE für Total Time und Startup Time
2. Create Pivot Tables: Node Type × Template
3. Export Mean MRE % per Combination

**Inputs**:
- `predictions_csv` - Path zu Predictions CSV
- `--output-dir` - Output directory für Evaluation Results

**Outputs**:
- `node_type_mean_mre_total_pct_{timestamp}.csv` - Total Time MRE %
- `node_type_mean_mre_startup_pct_{timestamp}.csv` - Startup Time MRE %

**Usage**:
```bash
python3 03_Node_Type_Evaluation.py <predictions_csv> --output-dir <output_dir>
```

**Example**:
```bash
python3 03_Node_Type_Evaluation.py \
    ../Model/predictions/predictions.csv \
    --output-dir ./evaluation_results
```

---

### 04 - 04_Operator_Time_Analysis.py

**Purpose**: Operator Time Range Analysis mit Template Extremes.

**Workflow**:
1. Calculate Statistics per Operator (Mean, Min, Max)
2. Identify Templates mit Min/Max Values
3. Calculate Ranges (Absolute & Percentage)
4. Sort by Total Range descending

**Inputs**:
- `dataset_csv` - Path zu Dataset CSV
- `--output-dir` - Output directory für Analysis Results

**Outputs**:
- `operator_range_analysis_{timestamp}.csv` - Operator Statistics mit Ranges

**Usage**:
```bash
python3 04_Operator_Time_Analysis.py <dataset_csv> --output-dir <output_dir>
```

**Example**:
```bash
python3 04_Operator_Time_Analysis.py \
    ../../../Datasets/Baseline/Training/combined_training.csv \
    --output-dir ./evaluation_results
```

---

## Notes

(Zusätzliche Insider-Informationen werden hier später ergänzt)
