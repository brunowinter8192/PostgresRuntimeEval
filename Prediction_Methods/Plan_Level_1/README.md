# Plan_Level_1

Plan-level runtime prediction for TPC-H queries using ML-based feature selection and regression models.

## Directory Structure

```
Plan_Level_1/
├── mapping_config.py                    # Shared configuration
├── README.md                            # Workflow documentation (THIS FILE)
├── Data_Generation/                     [See DOCS.md]
│   ├── 01a_Runtime_Data.py
│   ├── 01b_Plan_Features.py
│   ├── 01c_Row_Features.py
│   ├── 02_Merge_Data.py
│   ├── features.md                      # Feature documentation
│   ├── targets.md                       # Target documentation
│   └── csv/
├── Datasets/                            [See DOCS.md]
│   ├── 01_Split_Train_Test.py
│   ├── 02_Create_State_1.py
│   ├── Baseline/
│   ├── State_1/
│   └── State_2/
└── Runtime_Prediction/                  [See DOCS.md]
    ├── ffs_config.py
    ├── 01_Forward_Selection.py
    ├── 02_Train_Model.py
    ├── 03_Summarize_Results.py
    ├── 04_Evaluation_Plot.py
    ├── A_01a_Correlation_Analysis.py
    ├── A_01b_Scatter_Plots.py
    ├── A_01c_Outlier_Analysis.py
    ├── A_01d_Template_Constancy.py
    ├── Baseline_SVM/
    ├── Baseline_RandomForest/
    └── Baseline_XGBoost/
```

## Shared Infrastructure

**mapping_config.py:**
- `DB_CONFIG`: PostgreSQL connection parameters
- `CONTAINER_NAME`: Docker container name for TPC-H
- `OPERATOR_TYPES`: 13 plan operator types for feature extraction
- `PLAN_METADATA`: ['query_file', 'template']
- `PLAN_TARGET`: 'runtime'
- `FEATURES_TO_REMOVE_FOR_STATE_1`: 17 advanced features to drop
- `get_state_1_columns()`: Column order for State_1 dataset

## Datasets

| State | Features | Samples | Train/Test | Purpose |
|-------|----------|---------|------------|---------|
| Baseline | 50 | 2,850 | 2,280/570 | Full feature set reference |
| State_1 | 33 | 2,850 | 2,280/570 | Feature reduction impact |
| State_2 | 50 | 2,850 | 2,280/570 | Runtime variability |

## Workflow Overview

```
Phase 1: Data_Generation
├── 01a_Runtime_Data.py ──┐
├── 01b_Plan_Features.py ─┼──→ 02_Merge_Data.py → complete_dataset.csv
└── 01c_Row_Features.py ──┘

Phase 2: Datasets
01_Split_Train_Test.py → 02_Create_State_1.py

Phase 3: Runtime_Prediction
01_Forward_Selection.py → 02_Train_Model.py → 03_Summarize_Results.py → 04_Evaluation_Plot.py
```

## Phase Documentation

### Phase 1: Data_Generation

**Purpose:** Extract features and measure runtime for TPC-H queries

**Input:** Query directory with Q1/-Q22/ template folders containing SQL files

**Output:** `complete_dataset.csv` (2850 samples x 53 columns)
- 2 Metadata columns (query_file, template)
- 50 Feature columns (plan-level + operator metrics)
- 1 Target column (runtime in ms, cold cache)

**Details:** See [Data_Generation/DOCS.md](Data_Generation/DOCS.md)

---

### Phase 2: Datasets

**Purpose:** Create train/test splits and dataset transformations

**Input:** `complete_dataset.csv` from Data_Generation

**Processing:**
- Stratified 80/20 train/test split (by template)
- Dataset transformations (State_1: feature reduction)

**Output:** Train/test CSVs in Baseline/, State_1/, State_2/ directories

**Details:** See [Datasets/DOCS.md](Datasets/DOCS.md)

---

### Phase 3: Runtime_Prediction

**Purpose:** ML model training and evaluation for query runtime prediction

**Input:** `training_data.csv`, `test_data.csv` from Datasets

**Processing:**
- Forward Feature Selection (multi-seed)
- Model Training (SVM, Random Forest, XGBoost)
- Prediction and Evaluation

**Output:**
- FFS Results: Selected features per seed
- Trained Models: Serialized model pipelines
- Predictions: Test set predictions with errors
- Evaluation: MRE plots per template

**Details:** See [Runtime_Prediction/DOCS.md](Runtime_Prediction/DOCS.md)
