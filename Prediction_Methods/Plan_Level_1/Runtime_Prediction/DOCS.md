# Runtime_Prediction Module Documentation

## Working Directory

**CRITICAL:** All commands assume CWD = `Runtime_Prediction/`

```bash
cd /path/to/Plan_Level_1/Runtime_Prediction
```

## Directory Structure

```
Runtime_Prediction/
├── ffs_config.py                        # FFS parameters and model registry
├── 01_Forward_Selection.py              # Unified FFS with configurable model
├── 02_Train_Model.py                    # Unified training with configurable model
├── A_01a_Correlation_Analysis.py        # Analysis: Feature correlations
├── A_01b_Scatter_Plots.py               # Analysis: Feature vs runtime plots
├── A_01c_Sparsity.py                    # Analysis: Feature sparsity (zero counts)
├── A_01d_Template_Constancy.py          # Analysis: Feature constancy per template
├── A_01e_Template_Feature_Values.py     # Analysis: Constant feature values per template
├── A_01g_Evaluation_Plot.py             # Analysis: MRE bar plots
├── A_01h_Runtime_Plot.py                # Analysis: Mean runtime bar plots
├── A_01i_Optimizer_Baseline.py          # Analysis: ML vs optimizer cost comparison
├── A_01j_Summarize_Results.py           # Analysis: Template and overall summaries
├── A_01k_Runtime_Histograms.py          # Analysis: Runtime distribution histograms
├── D_Alternative_Modelle.md             # Thesis appendix: RF/XGBoost results
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
  - min_features: 1 (minimum features before stopping)
  - seeds: [42] (random seed for cross-validation)
  - n_splits: 5 (cross-validation folds)

- MODEL_REGISTRY: Model configurations for all baselines
  - svm: NuSVR with MaxAbsScaler (kernel=rbf, nu=0.65, C=5.0, gamma=scale, cache_size=500)
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

**All models use CSV-based feature loading:** Features are dynamically loaded from FFS output (01_ffs_summary.csv)

## Workflow Dependency Graph

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
Optional: Analysis scripts (A_01a-j, parallel)
```

### Example Workflow (SVM):

```bash
# 1. Forward feature selection
python 01_Forward_Selection.py ../Datasets/Baseline/training_data.csv --model svm
# Output: Baseline_SVM/SVM/01_ffs_summary.csv, 01_ffs_stability.csv

# 2. Train model with selected features
python 02_Train_Model.py ../Datasets/Baseline/training_data.csv ../Datasets/Baseline/test_data.csv --model svm
# Output: Baseline_SVM/SVM/02_model.pkl, 02_predictions.csv

# 3. Optional: Analysis (e.g., summarize results)
python A_01j_Summarize_Results.py Baseline_SVM/Evaluation/02_predictions.csv --output-dir Baseline_SVM/Evaluation
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
- `Baseline_<Model>/<output_folder>/01_ffs_summary.csv`: seed, n_features, final_mre, selected_features

**Usage**:
```bash
# SVM (outputs to Baseline_SVM/SVM/)
python 01_Forward_Selection.py ../Datasets/Baseline/training_data.csv --model svm

# Random Forest (outputs to Baseline_RandomForest/Random_Forest/)
python 01_Forward_Selection.py ../Datasets/Baseline/training_data.csv --model random_forest

# XGBoost (outputs to Baseline_XGBoost/XGBoost/)
python 01_Forward_Selection.py ../Datasets/Baseline/training_data.csv --model xgboost

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
6. Save trained model to pickle file
7. Generate predictions on test set
8. Export predictions with error metrics using PLAN_METADATA[0] for query column

**Model Selection**: Dynamically instantiates model from MODEL_REGISTRY with hyperparameters

**Inputs**:
- `train_csv` (positional): Training dataset CSV
- `test_csv` (positional): Test dataset CSV
- `--model` (required): Model to use (choices: svm, random_forest, xgboost)

**Outputs**:
- `Baseline_<Model>/<output_folder>/02_model.pkl`: Trained model (or Pipeline for SVM)
- `Baseline_<Model>/<output_folder>/02_predictions.csv`: Columns: query_file, actual_ms, predicted_ms, error_ms, abs_error_ms, relative_error

**Usage**:
```bash
# SVM with default seed 42
python 02_Train_Model.py ../Datasets/Baseline/training_data.csv ../Datasets/Baseline/test_data.csv --model svm

# Random Forest with seed 123
python 02_Train_Model.py train.csv test.csv --model random_forest --seed 123

# XGBoost with custom FFS CSV
python 02_Train_Model.py train.csv test.csv --model xgboost --ffs-csv /custom/ffs_results.csv

# Custom output directory
python 02_Train_Model.py train.csv test.csv --model svm --output-dir /custom/output
```

**Variables**:
- `--model` (required): svm | random_forest | xgboost
- `--ffs-csv`: FFS results CSV (default: Baseline_<Model>/<output_folder>/01_ffs_summary.csv)
- `--seed`: Random seed to select features for (default: 42)
- `--output-dir`: Output directory (default: Baseline_<Model>/<output_folder>/)

**Configurable Parameters (in ffs_config.py MODEL_REGISTRY):**
- Same as 01_Forward_Selection.py (model class, hyperparameters, scaler settings)
- To adjust model hyperparameters: Edit MODEL_REGISTRY['model_key']['params'] in ffs_config.py
- To change default output folders: Edit MODEL_REGISTRY['model_key']['output_folder']

---

## Analysis Scripts (A_01a-k)

Analysis scripts are standalone tools, NOT part of the main workflow. They can be run in parallel as needed.

---

### A_01a - Correlation_Analysis.py

**Purpose**: Identify highly correlated feature pairs from dataset

**Inputs**:
- `dataset_csv` (positional): Dataset CSV with features

**Outputs**:
- `A_01a_feature_correlations.csv`: feature_1, feature_2, correlation
- `A_01a_ffs_correlation_matrix.csv`: Full correlation matrix (only when --ffs-csv provided)

**Usage**:
```bash
# All features with high correlation threshold
python A_01a_Correlation_Analysis.py ../Datasets/Baseline/training_data.csv --threshold 0.95

# Only FFS-selected features with lower threshold
python A_01a_Correlation_Analysis.py ../Datasets/Baseline/complete_dataset.csv \
    --ffs-csv Baseline_SVM/SVM/01_ffs_summary.csv \
    --output-dir Baseline_SVM/Evaluation \
    --threshold 0.5
```

**Variables**:
- `--threshold`: Correlation threshold (default: 0.95)
- `--ffs-csv`: FFS summary CSV (optional, restricts analysis to FFS-selected features)
- `--output-dir`: Output directory

---

### A_01b - Scatter_Plots.py

**Purpose**: Create scatter plots of FFS-selected features versus runtime

**Inputs**:
- `dataset_csv` (positional): Dataset CSV with features and runtime
- `--ffs-csv` (required): FFS summary CSV with selected_features column

**Outputs**:
- `A_01b_scatter_plots.png`: Grid of scatter plots with correlation coefficients

**Usage**:
```bash
python A_01b_Scatter_Plots.py ../Datasets/Baseline/training_data.csv --ffs-csv Baseline_SVM/SVM/01_ffs_summary.csv
```

**Variables**:
- `--output-dir`: Output directory

---

### A_01c - Sparsity.py

**Purpose**: Analyze feature sparsity (zero counts per feature)

**Inputs**:
- `dataset_csv` (positional): Dataset CSV with features

**Outputs**:
- `A_01c_feature_sparsity.csv`: Zero count and percentage per feature

**Usage**:
```bash
python A_01c_Sparsity.py ../Datasets/Baseline/training_data.csv
```

**Variables**:
- `--output-dir`: Output directory

---

### A_01d - Template_Constancy.py

**Purpose**: Create matrix showing feature value constancy percentage per template

**Inputs**:
- `dataset_csv` (positional): Dataset CSV with features and template column

**Outputs**:
- `A_01d_template_feature_constancy.csv`: Matrix (templates x features) with constancy percentages

**Usage**:
```bash
# All features
python A_01d_Template_Constancy.py ../Datasets/Baseline/training_data.csv

# Only FFS-selected features
python A_01d_Template_Constancy.py ../Datasets/Baseline/training_data.csv --features-file Baseline_SVM/SVM/01_ffs_summary.csv
```

**Variables**:
- `--features-file`: FFS summary CSV with selected_features column (optional, default: all features)
- `--output-dir`: Output directory

---

### A_01e - Template_Feature_Values.py

**Purpose**: Create matrix showing constant feature values per template (excludes Q9 due to plan variability)

**Inputs**:
- `dataset_csv` (positional): Dataset CSV with features and template column

**Outputs**:
- `A_01e_template_feature_values.csv`: Matrix (templates x features) with actual values

**Usage**:
```bash
python A_01e_Template_Feature_Values.py ../Datasets/Baseline/training_data.csv --features-file Baseline_SVM/SVM/01_ffs_summary.csv
```

**Variables**:
- `--features-file` (required): FFS summary CSV with selected_features column
- `--output-dir`: Output directory

---

### A_01g - Evaluation_Plot.py

**Purpose**: Create MRE bar plot from template summary

**Inputs**:
- `template_summary_csv` (positional): Template summary CSV from 03_Summarize_Results.py

**Outputs**:
- `A_01g_template_mre_plot.png`: Bar chart showing MRE per template (300 DPI)

**Usage**:
```bash
python A_01g_Evaluation_Plot.py Baseline_SVM/SVM/03_template_summary.csv
```

**Variables**:
- `--output-dir`: Output directory (default: Evaluation/)

---

### A_01h - Runtime_Plot.py

**Purpose**: Create mean runtime bar plot per template (sorted ascending)

**Inputs**:
- `dataset_csv` (positional): Complete dataset CSV with runtime column

**Outputs**:
- `A_01h_template_runtime_plot.png`: Bar chart showing mean runtime per template (300 DPI, sorted low to high)

**Usage**:
```bash
python A_01h_Runtime_Plot.py ../Datasets/Baseline/complete_dataset.csv --output-dir Baseline_SVM/Evaluation
```

**Variables**:
- `--output-dir`: Output directory (default: Evaluation/)

---

### A_01i - Optimizer_Baseline.py

**Purpose**: Compare ML predictions with simple optimizer cost baseline (LinReg on p_tot_cost)

**Inputs**:
- `train_csv` (positional): Training dataset CSV
- `test_csv` (positional): Test dataset CSV
- `predictions_csv` (positional): ML predictions CSV
- `--output-dir` (required): Output directory

**Outputs**:
- `A_01i_optimizer_baseline_overall.csv`: Overall MRE comparison (ML vs LinReg)
- `A_01i_optimizer_baseline_template.csv`: Per-template MRE comparison
- `A_01i_optimizer_baseline_plot.png`: Bar chart comparing both methods

**Usage**:
```bash
python A_01i_Optimizer_Baseline.py ../Datasets/Baseline/training_data.csv ../Datasets/Baseline/test_data.csv Baseline_SVM/Evaluation/02_predictions.csv --output-dir Baseline_SVM/Evaluation/Optimizer
```

---

### A_01j - Summarize_Results.py

**Purpose**: Aggregate prediction results by template and compute overall metrics

**Inputs**:
- `predictions_csv` (positional): Predictions CSV from train model script

**Outputs**:
- `A_01j_template_summary.csv`: Per-template statistics (mean, std, min, max, count, MRE)
- `A_01j_overall_summary.csv`: Overall metrics (mean actual/predicted, overall MRE, counts)

**Usage**:
```bash
python A_01j_Summarize_Results.py Baseline_SVM/Evaluation/02_predictions.csv --output-dir Baseline_SVM/Evaluation
```

**Variables**:
- `--output-dir`: Output directory (default: same directory as input predictions CSV)

---

### A_01k - Runtime_Histograms.py

**Purpose**: Visualize runtime distribution per template with histograms

**Inputs**:
- `dataset_csv` (positional): Complete dataset CSV file

**Outputs**:
- `A_01k_runtime_histograms.png`: Grid of histograms (5 columns) showing runtime distribution per template with mean and CV

**Usage**:
```bash
python A_01k_Runtime_Histograms.py ../Datasets/Baseline/complete_dataset.csv --output-dir Baseline_SVM/Evaluation
```

**Variables**:
- `--output-dir`: Output directory (default: Baseline_SVM/Evaluation/)

---

## Additional Documentation

### D_Alternative_Modelle.md

**Purpose**: Thesis appendix documenting alternative models (Random Forest, XGBoost)

**Content**:
- MRE comparison: SVM (8.28%), Random Forest (2.66%), XGBoost (2.68%)
- Explains why SVM is used as baseline despite higher MRE (paper comparability)
- References to model output directories
