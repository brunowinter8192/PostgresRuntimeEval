# Plan_Level - DOCS.md

Plan-level LOTO (Leave-One-Template-Out) prediction using SVM with Forward Feature Selection.

---

## Shared Infrastructure

**ffs_config.py:**
- `METADATA_COLUMNS`: ['query_file', 'template', 'runtime'] - excluded from features
- `TARGET`: 'runtime' - prediction target (milliseconds)
- `FFS_CONFIG`: Forward feature selection parameters
  - `min_features: 10` - minimum features before early stopping
  - `seeds: [42]` - random seeds for reproducibility
  - `n_splits: 5` - cross-validation folds (StratifiedKFold)
- `SVM_CONFIG`: Model configuration
  - Model: NuSVR (kernel='rbf', nu=0.5, C=5.0, gamma='scale')
  - Scaler: MaxAbsScaler

---

## Workflow Execution Order

```
/LOTO/Dataset/{training,test}.csv
         |
         v
02_Forward_Selection.py  -->  SVM/QX/ffs_summary.csv
         |
         v
03_Train_Model.py  -->  Model/QX/model.pkl
         |
         v
04_Predict.py  -->  Evaluation/QX/predictions.csv
         |
         v
[SHARED] ../01_Evaluate_Template.py  -->  Evaluation/QX/metrics.csv
         |
         v
[SHARED] ../02_Compare_Templates.py  -->  comparison.csv + comparison_plot.png
```

**01_Feature_Ranking.py** is optional (analysis script, not part of main workflow).

---

## Script Documentation

### 01 - Feature_Ranking.py

**Purpose:** Collect selected features from all FFS results into summary file.

**Inputs:**
- `svm_dir` (positional): Path to SVM/ containing QX/ffs_summary.csv

**Outputs:**
- `output_dir/feature_sets.csv`: template, selected_features, n_features, final_mre

**Usage:**
```bash
python3 01_Feature_Ranking.py SVM --output-dir csv/
```

---

### 02 - Forward_Selection.py

**Purpose:** Greedy forward feature selection with cross-validation per template.

**Inputs:**
- `dataset_dir` (positional): Path to /LOTO/Dataset/ containing QX/{training,test}.csv

**Outputs:**
- `output_dir/QX/ffs_summary.csv`: seed, n_features, final_mre, selected_features

**Algorithm:**
1. For each template, load training.csv (all templates EXCEPT this one)
2. Iteratively add best feature based on CV score (MRE)
3. Stop when min_features reached AND no improvement

**Usage:**
```bash
python3 02_Forward_Selection.py ../../Dataset --output-dir SVM
```

---

### 03 - Train_Model.py

**Purpose:** Train SVM models using selected features from Forward Selection.

**Inputs:**
- `dataset_dir` (positional): Path to /LOTO/Dataset/
- `svm_dir` (positional): Path to SVM/ with ffs_summary.csv per template

**Outputs:**
- `output_dir/QX/model.pkl`: Pickled dict with 'model' (Pipeline) and 'features' (list)

**Usage:**
```bash
python3 03_Train_Model.py ../../Dataset SVM --output-dir Model
```

---

### 04 - Predict.py

**Purpose:** Generate predictions on test data using trained models.

**Inputs:**
- `dataset_dir` (positional): Path to /LOTO/Dataset/
- `model_dir` (positional): Path to Model/ with model.pkl per template

**Outputs:**
- `output_dir/QX/predictions.csv`: query_file, actual_ms, predicted_ms, error_ms, abs_error_ms, relative_error

**Usage:**
```bash
python3 04_Predict.py ../../Dataset Model --output-dir Evaluation
```

---

## Shared Evaluation Scripts

Located at `/Runtime_Prediction/` level for use by all prediction methods.

### ../01_Evaluate_Template.py

**Purpose:** Calculate evaluation metrics per template from predictions.

**Inputs:**
- `evaluation_dir` (positional): Path to Evaluation/ containing QX/predictions.csv

**Outputs:**
- `QX/metrics.csv`: query_count, mean_actual_ms, mean_predicted_ms, mean_mre, std_mre, mean_mre_pct

**Usage:**
```bash
python3 ../01_Evaluate_Template.py Evaluation
```

---

### ../02_Compare_Templates.py

**Purpose:** Create cross-template comparison summary and visualization.

**Inputs:**
- `evaluation_dir` (positional): Path to Evaluation/ containing QX/metrics.csv

**Outputs:**
- `comparison.csv`: Aggregated metrics across all templates
- `comparison_plot.png`: Bar chart of mean_mre_pct per template

**Usage:**
```bash
python3 ../02_Compare_Templates.py Evaluation
python3 ../02_Compare_Templates.py Evaluation --title "Plan Level"
```

**Variables:**
- `--title`: Plot title prefix (default: "LOTO Prediction")

---

## Output Folders

| Folder | Content |
|--------|---------|
| `SVM/QX/` | ffs_summary.csv (selected features per template) |
| `Model/QX/` | model.pkl (trained SVM pipeline) |
| `Evaluation/QX/` | predictions.csv, metrics.csv |

---

## Full Workflow Example

```bash
cd /Prediction_Methods/LOTO/Runtime_Prediction/Plan_Level

# 1. Forward Feature Selection (uses ../../Dataset)
python3 02_Forward_Selection.py ../../Dataset --output-dir SVM

# 2. Train Models
python3 03_Train_Model.py ../../Dataset SVM --output-dir Model

# 3. Predict
python3 04_Predict.py ../../Dataset Model --output-dir Evaluation

# 4. Evaluate (shared scripts)
python3 ../01_Evaluate_Template.py Evaluation
python3 ../02_Compare_Templates.py Evaluation
```
