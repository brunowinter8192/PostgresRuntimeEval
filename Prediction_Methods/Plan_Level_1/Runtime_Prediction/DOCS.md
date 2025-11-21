# Runtime_Prediction Module Documentation

## Directory Structure

```
Runtime_Prediction/
├── ffs_config.py                        # FFS parameters and model registry
├── 01_Forward_Selection.py              # Unified FFS with configurable model
├── 02_Train_Model.py                    # Unified training with configurable model
├── 03_Summarize_Results.py              # Aggregate predictions by template
├── 04_Evaluation_Plot.py                # Create MRE bar plots
├── 05_Correlation_Analysis.py           # Feature correlation analysis
├── 06_Scatter_Plots.py                  # Feature vs runtime scatter plots
├── 07_Outlier_Analysis.py               # IQR-based outlier detection
├── 08_Template_Constancy.py             # Feature constancy per template
├── Baseline_SVM/                        # NuSVR outputs
│   ├── SVM/                             # [FFS outputs]
│   ├── Model/                           # [training outputs]
│   └── Evaluation/                      # [evaluation outputs]
├── Baseline_RandomForest/               # Random Forest outputs
│   ├── Random_Forest/                   # [FFS outputs]
│   ├── Model/                           # [training outputs]
│   └── Evaluation/                      # [evaluation outputs]
└── Baseline_XGBoost/                    # XGBoost outputs
    ├── XGBoost/                         # [FFS outputs]
    ├── Model/                           # [training outputs]
    └── Evaluation/                      # [evaluation outputs]
```

## Shared Infrastructure

Uses configuration files from parent directory:

**mapping_config.py:**
- METADATA_COLUMNS: Columns to exclude from features
- PLAN_TARGET: Target column name (runtime)
- PLAN_METADATA: Metadata column names (query_file, template)

**ffs_config.py:**
- FFS_CONFIG: Forward feature selection parameters
  - min_features: 10 (minimum features before stopping)
  - seeds: [42, 123, 456, 789, 999] (random seeds for multi-seed FFS)
  - n_splits: 5 (cross-validation folds)

- MODEL_REGISTRY: Model configurations for all baselines
  - svm: NuSVR with MaxAbsScaler (kernel=rbf, nu=0.5, C=5.0, gamma=scale, cache_size=500)
  - random_forest: RandomForestRegressor (n_estimators=1000, max_depth=None, max_features=sqrt, n_jobs=-1)
  - xgboost: XGBRegressor (max_depth=7, learning_rate=0.05, n_estimators=1000, subsample=0.8)

**Model Registry Keys (per model):**
- name: Display name
- class_name: Python class name
- module: Import module path
- use_scaler: Boolean (True for SVM, False for RF/XGBoost)
- scaler_class/scaler_module: Scaler configuration (if use_scaler=True)
- output_folder: Output directory name (SVM/, Random_Forest/, XGBoost/)
- params: Dictionary of model hyperparameters

**All models use CSV-based feature loading:** Features are dynamically loaded from FFS output (01_multi_seed_summary.csv)

## Workflow Execution Order

### Per Baseline Model:

```
01_Forward_Selection.py --model <svm|random_forest|xgboost>
         ↓
  Multi-seed feature selection results (Baseline_<Model>/<output_folder>/)
         ↓
02_Train_Model.py --model <svm|random_forest|xgboost>
         ↓
  Trained model and predictions (Baseline_<Model>/<output_folder>/)
         ↓
Optional: Analysis scripts (03-08)
```

### Example Workflow (SVM):

```bash
# 1. Forward feature selection
python 01_Forward_Selection.py ../../Datasets/Baseline/training_data.csv --model svm
# Output: Baseline_SVM/SVM/01_multi_seed_summary.csv, 01_feature_stability.csv

# 2. Train model with selected features
python 02_Train_Model.py ../../Datasets/Baseline/training_data.csv ../../Datasets/Baseline/test_data.csv --model svm
# Output: Baseline_SVM/SVM/02_model_<timestamp>.pkl, 02_predictions_<timestamp>.csv

# 3. Optional: Summarize results
python 03_Summarize_Results.py Baseline_SVM/SVM/02_predictions_<timestamp>.csv
```

## Script Documentation

---

### 01 - Forward_Selection.py

**Purpose**: Unified multi-seed forward feature selection with configurable model

**Workflow**:
1. Load model configuration from MODEL_REGISTRY based on --model flag
2. Load dataset with semicolon delimiter
3. Extract feature columns (exclude metadata from METADATA_COLUMNS)
4. Extract template IDs from PLAN_METADATA[1] for stratified cross-validation
5. For each seed in FFS_CONFIG['seeds']:
   - Initialize stratified k-fold CV with n_splits from FFS_CONFIG
   - Run forward selection algorithm:
     - Start with empty feature set
     - Iteratively add best feature based on MRE
     - Stop when no improvement (after min_features threshold)
   - Track selected features and final MRE
6. Export multi-seed summary and feature stability analysis

**Model Selection**: Dynamically instantiates model from MODEL_REGISTRY (handles SVM Pipeline with scaler, RF/XGBoost direct model)

**Inputs**:
- `input_csv` (positional): CSV file with features and runtime column
- `--model` (required): Model to use (choices: svm, random_forest, xgboost)

**Outputs**:
- `Baseline_<Model>/<output_folder>/01_multi_seed_summary.csv`: seed, n_features, final_mre, selected_features
- `Baseline_<Model>/<output_folder>/01_feature_stability.csv`: feature, count, percentage (across seeds)

**Usage**:
```bash
# SVM (outputs to Baseline_SVM/SVM/)
python 01_Forward_Selection.py ../../Datasets/Baseline/training_data.csv --model svm

# Random Forest (outputs to Baseline_RandomForest/Random_Forest/)
python 01_Forward_Selection.py ../../Datasets/Baseline/training_data.csv --model random_forest

# XGBoost (outputs to Baseline_XGBoost/XGBoost/)
python 01_Forward_Selection.py ../../Datasets/Baseline/training_data.csv --model xgboost

# Custom output directory
python 01_Forward_Selection.py dataset.csv --model svm --output-dir /custom/output
```

**Variables**:
- `--model` (required): svm | random_forest | xgboost
- `--output-dir`: Custom output directory (default: Baseline_<Model>/<output_folder>/)

**Configurable Parameters (in ffs_config.py MODEL_REGISTRY):**
- Model class and import module
- Hyperparameters (kernel, nu, C for SVM; n_estimators, max_depth for RF; learning_rate, subsample for XGBoost)
- Scaler configuration (use_scaler, scaler_class, scaler_module)
- Output folder name

---

### 02 - Train_Model.py

**Purpose**: Unified model training with CSV-based feature loading and configurable model

**Workflow**:
1. Load model configuration from MODEL_REGISTRY based on --model flag
2. Load selected features from FFS multi-seed summary CSV for specified seed
3. Load train and test datasets with semicolon delimiter
4. Prepare feature matrices using PLAN_TARGET for target column
5. Train model (with optional Pipeline + scaler for SVM)
6. Save trained model to pickle file with timestamp
7. Generate predictions on test set
8. Export predictions with error metrics using PLAN_METADATA[0] for query column

**Model Selection**: Dynamically instantiates model from MODEL_REGISTRY with hyperparameters

**Inputs**:
- `train_csv` (positional): Training dataset CSV
- `test_csv` (positional): Test dataset CSV
- `--model` (required): Model to use (choices: svm, random_forest, xgboost)

**Outputs**:
- `Baseline_<Model>/<output_folder>/02_model_{timestamp}.pkl`: Trained model (or Pipeline for SVM)
- `Baseline_<Model>/<output_folder>/02_predictions_{timestamp}.csv`: Columns: query_file, actual_ms, predicted_ms, error_ms, abs_error_ms, relative_error

**Usage**:
```bash
# SVM with default seed 42
python 02_Train_Model.py ../../Datasets/Baseline/training_data.csv ../../Datasets/Baseline/test_data.csv --model svm

# Random Forest with seed 123
python 02_Train_Model.py train.csv test.csv --model random_forest --seed 123

# XGBoost with custom FFS CSV
python 02_Train_Model.py train.csv test.csv --model xgboost --ffs-csv /custom/ffs_results.csv

# Custom output directory
python 02_Train_Model.py train.csv test.csv --model svm --output-dir /custom/output
```

**Variables**:
- `--model` (required): svm | random_forest | xgboost
- `--ffs-csv`: FFS results CSV (default: Baseline_<Model>/<output_folder>/01_multi_seed_summary.csv)
- `--seed`: Random seed to select features for (default: 42)
- `--output-dir`: Output directory (default: Baseline_<Model>/<output_folder>/)

**Configurable Parameters (in ffs_config.py MODEL_REGISTRY):**
- Same as 01_Forward_Selection.py (model class, hyperparameters, scaler settings)
- To adjust model hyperparameters: Edit MODEL_REGISTRY['model_key']['params'] in ffs_config.py
- To change default output folders: Edit MODEL_REGISTRY['model_key']['output_folder']

---

### 03 - Summarize_Results.py

**Purpose**: Aggregate prediction results by template and compute overall metrics

**Workflow**:
1. Load predictions CSV
2. Extract template ID from query_file
3. Compute per-template statistics (mean, std, min, max, count, MRE)
4. Compute overall summary (mean actual/predicted, overall MRE, counts)
5. Export both summaries

**Inputs**:
- `predictions_csv` (positional): Predictions CSV from train model script

**Outputs**:
- `03_template_summary_{timestamp}.csv`: Per-template statistics
- `03_overall_summary_{timestamp}.csv`: Overall metrics

**Usage**:
```bash
python 03_Summarize_Results.py Baseline_SVM/SVM/02_predictions_20251119.csv
python 03_Summarize_Results.py Baseline_RandomForest/Random_Forest/02_predictions_20251119.csv --output-dir custom/
```

**Variables**:
- `--output-dir`: Output directory (default: same directory as input predictions CSV)

---

### 04 - Evaluation_Plot.py

**Purpose**: Create MRE bar plot from template summary for visual performance analysis

**Workflow**:
1. Load template summary CSV
2. Convert MRE to percentage
3. Create bar chart with MRE (%) per template
4. Add percentage labels on top of bars
5. Save high-resolution plot to output directory

**Inputs**:
- `template_summary_csv` (positional): Template summary CSV from summarize results script

**Outputs**:
- `template_mre_plot.png`: Bar chart showing MRE per template (300 DPI)

**Plot Style**:
- Steelblue bars with black edges
- Percentage labels on top
- Grid lines for readability
- 16x8 figure size

**Usage**:
```bash
python 04_Evaluation_Plot.py Baseline_SVM/Evaluation/03_template_summary.csv
python 04_Evaluation_Plot.py summary.csv --output-dir custom_plots/
```

**Variables**:
- `--output-dir`: Output directory (default: Evaluation/)

---

### 05 - Correlation_Analysis.py

**Purpose**: Identify highly correlated feature pairs from dataset

**Inputs**:
- `dataset_csv` (positional): Dataset CSV with features

**Outputs**:
- `05_feature_correlations_{timestamp}.csv`: feature_1, feature_2, correlation

**Usage**:
```bash
python 05_Correlation_Analysis.py ../../Datasets/Baseline/training_data.csv --threshold 0.95
```

**Variables**:
- `--threshold`: Correlation threshold (default: 0.95)
- `--output-dir`: Output directory

---

### 06 - Scatter_Plots.py

**Purpose**: Create scatter plots of all features versus runtime

**Inputs**:
- `dataset_csv` (positional): Dataset CSV with features and runtime

**Outputs**:
- `06_scatter_plots_{timestamp}.png`: Grid of scatter plots with correlation coefficients

**Usage**:
```bash
python 06_Scatter_Plots.py ../../Datasets/Baseline/training_data.csv
```

**Variables**:
- `--output-dir`: Output directory

---

### 07 - Outlier_Analysis.py

**Purpose**: Analyze feature outliers using IQR method and zero value distribution

**Inputs**:
- `dataset_csv` (positional): Dataset CSV with features

**Outputs**:
- `07_feature_outliers_{timestamp}.csv`: Outlier statistics per feature
- `07_feature_zeros_{timestamp}.csv`: Zero count per feature

**Usage**:
```bash
python 07_Outlier_Analysis.py ../../Datasets/Baseline/training_data.csv
```

**Variables**:
- `--output-dir`: Output directory

---

### 08 - Template_Constancy.py

**Purpose**: Create matrix showing feature value constancy percentage per template

**Inputs**:
- `dataset_csv` (positional): Dataset CSV with features and template column

**Outputs**:
- `08_template_feature_constancy_{timestamp}.csv`: Matrix (templates x features) with constancy percentages

**Usage**:
```bash
python 08_Template_Constancy.py ../../Datasets/Baseline/training_data.csv
```

**Variables**:
- `--output-dir`: Output directory
