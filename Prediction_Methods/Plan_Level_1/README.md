# Plan_Level_1: Plan-Level Query Runtime Prediction

## Directory Structure

```
Plan_Level_1/
├── mapping_config.py                    # Shared configuration (DB, operators, features)
├── README.md                            # This file (Workflow-Level documentation)
├── Data_Generation/                     # Phase 1: Feature extraction [See DOCS.md]
│   ├── 01_Runtime_Data.py              # Collect query runtimes with cold cache
│   ├── 02_Plan_Features.py             # Extract plan-level features from EXPLAIN
│   ├── 03_Row_Features.py              # Extract row/byte counts from plan tree
│   ├── 04_Merge_Data.py                # Merge all features into complete dataset
│   └── csv/                            # [outputs]
├── Datasets/                            # Phase 2: Dataset preparation [See DOCS.md]
│   ├── 01_Split_Train_Test.py          # Stratified train/test split
│   ├── 02_Create_State_1.py            # Transform Baseline to State_1
│   ├── Baseline/                       # Full feature set (50 features)
│   │   ├── training_data.csv           # 2,280 samples (80%)
│   │   └── test_data.csv               # 570 samples (20%)
│   ├── State_1/                        # Basic feature set (34 features)
│   │   ├── complete_dataset.csv        # 2,850 samples
│   │   ├── training_data.csv           # 2,280 samples (80%)
│   │   └── test_data.csv               # 570 samples (20%)
│   └── State_2/                        # Second cold-cache execution (50 features)
│       ├── complete_dataset.csv        # 2,850 samples
│       ├── training_data.csv           # 2,280 samples (80%)
│       └── test_data.csv               # 570 samples (20%)
└── Runtime_Prediction/                  # Phase 3: Model training [See DOCS.md]
    ├── ffs_config.py                   # FFS parameters + model registry
    ├── 01_Forward_Selection.py         # Unified FFS with configurable model
    ├── 02_Train_Model.py               # Unified training with configurable model
    ├── 03_Summarize_Results.py         # Aggregate predictions by template
    ├── 04_Evaluation_Plot.py           # Create MRE bar plots
    ├── 05_Correlation_Analysis.py      # Feature correlation analysis
    ├── 06_Scatter_Plots.py             # Feature vs runtime scatter plots
    ├── 07_Outlier_Analysis.py          # IQR-based outlier detection
    ├── 08_Template_Constancy.py        # Feature constancy per template
    ├── Baseline_SVM/                   # NuSVR outputs
    │   ├── SVM/                        # [FFS + training outputs]
    │   ├── Model/                      # [alternative training outputs]
    │   └── Evaluation/                 # [evaluation outputs]
    ├── Baseline_RandomForest/          # Random Forest outputs
    │   ├── Random_Forest/              # [FFS + training outputs]
    │   ├── Model/                      # [alternative training outputs]
    │   └── Evaluation/                 # [evaluation outputs]
    └── Baseline_XGBoost/               # XGBoost outputs
        ├── XGBoost/                    # [FFS + training outputs]
        ├── Model/                      # [alternative training outputs]
        └── Evaluation/                 # [evaluation outputs]
```

## Shared Infrastructure

### mapping_config.py

Central configuration file containing:

- **DB_CONFIG**: PostgreSQL connection settings (host, port, database, user, password)
  - Database: `tpch` on localhost:5432
- **CONTAINER_NAME**: Docker container name (`tpch-postgres`)
- **PLAN_METADATA**: Metadata column names (`query_file`, `template`)
- **PLAN_TARGET**: Target column name (`runtime`)
- **PLAN_STRUCTURAL_FEATURES** (12): Root plan metrics (p_st_cost, p_tot_cost, p_rows, p_width, etc.)
- **PLAN_STRATEGY_FEATURES** (6): Execution strategies (strategy_hashed, partial_mode_finalize, etc.)
- **PLAN_KEY_FEATURES** (4): Key/sorting features (group_key_count, sort_key_columns, etc.)
- **PLAN_RESULT_FEATURES** (2): Volume metrics (row_count, byte_count)
- **OPERATOR_TYPES** (13): Tracked operator types (Aggregate, Hash Join, Seq Scan, Sort, etc.)
- **METADATA_COLUMNS**: Columns excluded from feature analysis (query_file, template, runtime)

**State_1 Dataset Configuration**:
- **STATE_1_METADATA**: State_1 metadata columns (`query_file`, `template`)
- **STATE_1_STRUCTURAL_FEATURES** (5): Basic plan metrics (p_st_cost, p_tot_cost, p_rows, p_width, op_count)
- **STATE_1_FEATURES** (7): STATE_1_STRUCTURAL_FEATURES + PLAN_RESULT_FEATURES
- **FEATURES_TO_REMOVE_FOR_STATE_1** (17): Advanced features excluded from State_1

**Helper Functions**:
- `get_operator_feature_columns()`: Returns all operator-based feature names (26 features)
- `get_all_feature_columns()`: Returns complete feature set (50 features)
- `get_state_1_feature_columns()`: Returns State_1 feature set (34 features)
- `get_state_1_columns()`: Returns all State_1 columns (36 total)

### Runtime_Prediction/ffs_config.py

Forward feature selection configuration and model registry:

**FFS_CONFIG**:
- **min_features**: 10 (minimum features selected before stopping)
- **seeds**: [42, 123, 456, 789, 999] (random seeds for multi-seed FFS)
- **n_splits**: 5 (cross-validation folds for stratified k-fold)

**MODEL_REGISTRY**: Unified model configurations for all baselines

Each model entry contains:
- **name**: Display name (SVM, RandomForest, XGBoost)
- **class_name**: Python class name (NuSVR, RandomForestRegressor, XGBRegressor)
- **module**: Import module path (sklearn.svm, sklearn.ensemble, xgboost)
- **use_scaler**: Boolean flag (True for SVM, False for RF/XGBoost)
- **scaler_class/scaler_module**: Scaler configuration (MaxAbsScaler for SVM)
- **output_folder**: Output directory name (SVM/, Random_Forest/, XGBoost/)
- **params**: Dictionary of model hyperparameters

**Model Configurations**:

| Model | Key Hyperparameters | Scaler |
|-------|---------------------|--------|
| SVM | kernel=rbf, nu=0.5, C=5.0, gamma=scale, cache_size=500 | MaxAbsScaler |
| Random Forest | n_estimators=1000, max_depth=None, max_features=sqrt, n_jobs=-1 | None |
| XGBoost | max_depth=7, learning_rate=0.05, n_estimators=1000, subsample=0.8 | None |

**Key Design**: All models use CSV-based feature loading. Features are dynamically loaded from FFS output (01_multi_seed_summary.csv), not hardcoded.

## Datasets

### Datasets/Baseline/

**Dataset Source**: `Data_Generation/csv/complete_dataset.csv`

**Characteristics**:
- **Full feature set**: All 50 extracted features without modifications
- **No adjustments**: Raw features as extracted from PostgreSQL EXPLAIN output
- **Complete observations**: All 2,850 query instances included

**Dataset Structure**:
- **Total samples**: 2,850 TPC-H query instances
- **Total columns**: 53 (3 metadata + 50 features)
- **Delimiter**: Semicolon (`;`)
- **Train/Test split**: 80/20 (2,280/570 samples)
- **Stratification**: By template (ensures equal representation across 19 TPC-H templates)

**Columns**:
- **Metadata** (3): `query_file`, `template`, `runtime` (target variable in milliseconds)
- **Features** (50): Extracted from PostgreSQL query execution plan

**Feature Categories**:

| Category | Count | Examples |
|----------|-------|----------|
| Root Plan Metrics | 4 | `p_st_cost`, `p_tot_cost`, `p_rows`, `p_width` |
| Operator Counts/Rows | 26 | `Hash_Join_cnt`, `Seq_Scan_rows`, `Sort_cnt` |
| Parallelization | 3 | `workers_planned`, `parallel_aware_count`, `op_count` |
| Strategies/Modes | 6 | `strategy_hashed`, `partial_mode_finalize` |
| Keys/Sorting | 4 | `group_key_count`, `sort_key_columns` |
| Structure | 5 | `max_tree_depth`, `subplan_count`, `jit_functions` |
| Volume | 2 | `row_count`, `byte_count` |

### Datasets/State_1/

**Dataset Source**: `Data_Generation/csv/complete_dataset.csv` (transformed via `02_Create_State_1.py`)

**Characteristics**:
- **Reduced feature set**: 34 features (16 fewer than Baseline)
- **Basic plan metrics only**: Excludes advanced parallelization, strategy, and key features
- **First research iteration**: Represents initial feature engineering approach

**Dataset Structure**:
- **Total samples**: 2,850 TPC-H query instances (same as Baseline)
- **Total columns**: 36 (2 metadata + 34 features)
- **Delimiter**: Semicolon (`;`)
- **Train/Test split**: 80/20 (2,280/570 samples)
- **Stratification**: By template (same as Baseline)

**Columns**:
- **Metadata** (2): `query_file`, `template` (template used for splitting, not as feature)
- **Target** (1): `runtime` (milliseconds)
- **Features** (34): Basic plan metrics, operator features, and result features

**Feature Categories**:

| Category | Count | Examples |
|----------|-------|----------|
| Root Plan Metrics | 4 | `p_st_cost`, `p_tot_cost`, `p_rows`, `p_width` |
| Operator Count | 1 | `op_count` |
| Operator Counts/Rows | 26 | `Hash_Join_cnt`, `Seq_Scan_rows`, `Sort_cnt` |
| Volume | 2 | `row_count`, `byte_count` |

**Features Removed from Baseline** (16 advanced features):
- Parallelization metrics (3): `workers_planned`, `parallel_aware_count`
- Plan structure (5): `max_tree_depth`, `planning_time_ms`, `jit_functions`, `subplan_count`, `initplan_count`
- Aggregation strategies (6): `strategy_hashed`, `strategy_plain`, `strategy_sorted`, `partial_mode_simple`, `partial_mode_partial`, `partial_mode_finalize`
- Key/sorting metrics (4): `group_key_count`, `group_key_columns`, `sort_key_count`, `sort_key_columns`

**State_1 vs Baseline**:

State_1 represents the **first research iteration** with a simpler feature set focused on basic plan costs and operator counting. Baseline extends this with advanced plan analysis features. This progression demonstrates:

1. **Didactic value**: Shows feature engineering evolution from basic to advanced
2. **Performance comparison**: Quantifies improvement from adding sophisticated features
3. **Research documentation**: Preserves first iteration alongside refined approach

The Baseline dataset (50 features) was developed after State_1 by adding advanced PostgreSQL plan analysis. For didactic purposes, State_1 is preserved to demonstrate how incremental feature engineering improves prediction accuracy.

**Plan_Level_1 Philosophy**:

Plan_Level_1 focuses on **dataset variations** while keeping prediction methods constant. Different dataset preparations (feature engineering, selection, transformations) are explored within this level. For fundamentally different prediction approaches or methodologies, a new level (e.g., Plan_Level_2) would be created.

- **Within Plan_Level_1**: Dataset adjustments, feature selection, preprocessing variations (State_1, Baseline, State_2, future variations)
- **New Plan_Level_X**: Fundamental changes to prediction methodology or problem formulation

### Datasets/State_2/

**Dataset Source**: `Data_Generation/csv/complete_dataset.csv` (second cold-cache execution)

**Characteristics**:
- **Identical feature set to Baseline**: All 50 extracted features (same schema)
- **Different runtime measurements**: Second cold-cache execution of same 2,850 queries
- **Benchmark variability documentation**: Demonstrates inherent variance in database query execution

**Dataset Structure**:
- **Total samples**: 2,850 TPC-H query instances (identical queries as Baseline)
- **Total columns**: 53 (3 metadata + 50 features)
- **Delimiter**: Semicolon (`;`)
- **Train/Test split**: 80/20 (2,280/570 samples)
- **Stratification**: By template (same as Baseline)

**Columns**:
- **Metadata** (3): `query_file`, `template`, `runtime` (target variable in milliseconds)
- **Features** (50): Identical to Baseline feature set

**Feature Categories**:

| Category | Count | Examples |
|----------|-------|----------|
| Root Plan Metrics | 4 | `p_st_cost`, `p_tot_cost`, `p_rows`, `p_width` |
| Operator Counts/Rows | 26 | `Hash_Join_cnt`, `Seq_Scan_rows`, `Sort_cnt` |
| Parallelization | 3 | `workers_planned`, `parallel_aware_count`, `op_count` |
| Strategies/Modes | 6 | `strategy_hashed`, `partial_mode_finalize` |
| Keys/Sorting | 4 | `group_key_count`, `sort_key_columns` |
| Structure | 5 | `max_tree_depth`, `subplan_count`, `jit_functions` |
| Volume | 2 | `row_count`, `byte_count` |

**State_2 vs Baseline**:

State_2 contains the **same feature set** as Baseline (50 features) but represents a **second independent execution** of all 2,850 queries with cold cache. Key differences:

1. **Runtime measurements**: Different execution times due to system variability
   - Training set: Mean difference ~14ms (1.3% faster)
   - Test set: Mean difference ~15ms (1.3% faster)
2. **Same queries**: Identical `query_file` values across both datasets
3. **Feature consistency**: All 50 features have identical values (plan-based, not runtime-based)

**Purpose and Rationale**:

State_2 demonstrates **cold-cache benchmark variability**. Even with identical:
- Hardware configuration
- Database state
- Query execution plan
- PostgreSQL settings

Runtime measurements vary due to:
- System I/O conditions
- Background processes
- Cache state variations
- OS scheduler decisions

This variability (1-2%) is typical for database benchmarks and validates that:
- Prediction models must handle inherent execution variance
- Multiple measurement runs provide statistical robustness
- Feature-based prediction can generalize across execution variations

**State_2 is NOT a feature engineering iteration** - it serves to quantify and document the natural variance in query execution when repeating the same benchmark under identical conditions.

## Output Folder Organization

Each `Baseline_*` directory follows a standardized 3-folder structure:

### 1. Method Folder (SVM/, Random_Forest/, XGBoost/)

Primary output location for FFS and training:
- **FFS results**:
  - `01_multi_seed_summary.csv`: Selected features per seed with MRE
  - `01_feature_stability.csv`: Feature frequency across seeds
- **Trained models**:
  - `02_model_{timestamp}.pkl`: Serialized model (or Pipeline for SVM)
- **Predictions**:
  - `02_predictions_{timestamp}.csv`: Test predictions with error metrics

### 2. Model/ Folder

Alternative location for training outputs (used by some baseline configurations):
- Trained models (PKL files)
- Prediction CSVs
- Can contain nested subdirectories (Model_1/, Model_2/) for different configurations

### 3. Evaluation/ Folder

Evaluation suite outputs:
- **Template summaries**: `03_template_summary_{timestamp}.csv` (per-template statistics)
- **Overall summaries**: `03_overall_summary_{timestamp}.csv` (aggregate metrics)
- **MRE plots**: `template_mre_plot.png` (bar chart visualization)

## Workflow Overview

### Phase 1: Data Generation
Collect query runtimes and extract plan-level features from PostgreSQL EXPLAIN output.

**Execution**:
```bash
cd Data_Generation
python 01_Runtime_Data.py /path/to/queries/ --scale-factor 1
python 02_Plan_Features.py /path/to/queries/
python 03_Row_Features.py /path/to/queries/
python 04_Merge_Data.py csv/02_plan_features.csv csv/03_row_features.csv --runtime-csv csv/01_runtimes.csv
```

**Output**: `csv/complete_dataset.csv` (2,850 samples × 53 columns)

---

### Phase 2: Dataset Preparation
Create dataset variations and stratified train/test splits.

**Baseline Dataset** (full feature set):
```bash
cd Datasets
python 01_Split_Train_Test.py ../Data_Generation/csv/complete_dataset.csv --output-dir Baseline
```

**Output**:
- `Baseline/training_data.csv` (2,280 samples, 50 features)
- `Baseline/test_data.csv` (570 samples, 50 features)

**State_1 Dataset** (basic feature set):
```bash
cd Datasets
python 02_Create_State_1.py ../Data_Generation/csv/complete_dataset.csv --output-csv State_1/complete_dataset.csv
python 01_Split_Train_Test.py State_1/complete_dataset.csv --output-dir State_1
```

**Output**:
- `State_1/complete_dataset.csv` (2,850 samples, 34 features)
- `State_1/training_data.csv` (2,280 samples, 34 features)
- `State_1/test_data.csv` (570 samples, 34 features)

**State_2 Dataset** (second cold-cache execution):
```bash
# State_2 created by re-running Phase 1 Data_Generation (cold-cache execution)
cd Datasets
python 01_Split_Train_Test.py State_2/complete_dataset.csv --output-dir State_2
```

**Output**:
- `State_2/training_data.csv` (2,280 samples, 50 features)
- `State_2/test_data.csv` (570 samples, 50 features)

**Note**: State_2 complete_dataset.csv comes from a second independent execution of Phase 1 with cold cache, not from transforming the Baseline dataset.

---

### Phase 3: Runtime Prediction
Train models with forward feature selection and evaluate predictions.

**Unified Script Workflow** (example with SVM):

```bash
cd Runtime_Prediction

# Step 1: Forward Feature Selection
python 01_Forward_Selection.py ../Datasets/Baseline/training_data.csv --model svm
# Output: Baseline_SVM/SVM/01_multi_seed_summary.csv, 01_feature_stability.csv

# Step 2: Train Model
python 02_Train_Model.py ../Datasets/Baseline/training_data.csv ../Datasets/Baseline/test_data.csv --model svm
# Output: Baseline_SVM/SVM/02_model_{timestamp}.pkl, 02_predictions_{timestamp}.csv

# Step 3: Summarize Results
python 03_Summarize_Results.py Baseline_SVM/SVM/02_predictions_{timestamp}.csv
# Output: Baseline_SVM/SVM/03_template_summary_{timestamp}.csv, 03_overall_summary_{timestamp}.csv

# Step 4: Create Evaluation Plot
python 04_Evaluation_Plot.py Baseline_SVM/SVM/03_template_summary_{timestamp}.csv --output-dir Baseline_SVM/Evaluation
# Output: Baseline_SVM/Evaluation/template_mre_plot.png
```

**Multi-Model Execution**:

```bash
# Run FFS for all three models
python 01_Forward_Selection.py ../Datasets/Baseline/training_data.csv --model svm
python 01_Forward_Selection.py ../Datasets/Baseline/training_data.csv --model random_forest
python 01_Forward_Selection.py ../Datasets/Baseline/training_data.csv --model xgboost

# Train all three models
python 02_Train_Model.py ../Datasets/Baseline/training_data.csv ../Datasets/Baseline/test_data.csv --model svm
python 02_Train_Model.py ../Datasets/Baseline/training_data.csv ../Datasets/Baseline/test_data.csv --model random_forest
python 02_Train_Model.py ../Datasets/Baseline/training_data.csv ../Datasets/Baseline/test_data.csv --model xgboost
```

**Model Selection**: Use `--model` flag with choices: `svm`, `random_forest`, `xgboost`

**Optional Parameters**:
- `--seed`: Random seed for feature selection (default: 42)
- `--output-dir`: Custom output directory
- `--ffs-csv`: Custom FFS results path

## Phase Documentation

### Phase 1: Data Generation
Extracts features from PostgreSQL EXPLAIN JSON output for TPC-H queries.

**Purpose**: Generate feature datasets for plan-level runtime prediction
**Input**: Directory of SQL query files organized by template
**Output**: CSV files with plan metrics, operator counts, and runtime measurements

See `Data_Generation/DOCS.md` for detailed script documentation.

### Phase 2: Dataset Preparation
Stratified train/test split with template-based stratification.

**Purpose**: Prepare balanced training and test sets
**Input**: Complete dataset from Phase 1
**Output**: Train/test splits with equal template representation

See `Datasets/DOCS.md` for detailed script documentation.

### Phase 3: Runtime Prediction
Train and evaluate baseline ML models for query runtime prediction.

**Purpose**: Compare different ML approaches (SVM, Random Forest, XGBoost)
**Input**: Prepared datasets from Phase 2
**Output**: Trained models, predictions, and evaluation metrics

**Key Features**:
- Unified scripts with configurable model selection
- CSV-based feature loading (no hardcoded feature lists)
- Multi-seed forward feature selection
- Standardized output folder structure across baselines

See `Runtime_Prediction/DOCS.md` for detailed script documentation.
