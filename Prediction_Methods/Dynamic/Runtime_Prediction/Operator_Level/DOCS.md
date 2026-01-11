# Operator_Level - DOCS

## Working Directory

**CRITICAL:** All commands assume CWD = `Operator_Level/`

```bash
cd Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level
```

---

## Directory Structure

```
Operator_Level/
├── DOCS.md
├── 00_Batch_Workflow.py
├── 01_Forward_Selection.py
├── 02_Train_Models.py
├── 03_Query_Prediction.py
├── A_01a_Query_Evaluation.py
├── A_01b_Static_Dynamic_Comparison.py
└── Q1/, Q3/, ... Q19/
    ├── SVM/
    ├── Model/
    ├── md/
    │   └── 03_Qx_{hash}.md
    └── predictions.csv
```

---

## 00 - Batch_Workflow.py

**Purpose:** Run complete Operator_Level workflow (FFS, Train, Predict) for all 14 LOTO templates.

**Inputs:**
- Dataset: `../../Dataset/Dataset_Operator/Qx/` (from 01_LOTO_Split.py)
- All scripts are LOCAL (LOTO-compatible versions)

**Outputs per Template:**
- `Qx/SVM/two_step_evaluation_overview.csv` - FFS results
- `Qx/Model/{target}/{operator}/model.pkl` - Trained models
- `Qx/predictions.csv` - Bottom-up predictions

**Usage:**
```bash
python3 00_Batch_Workflow.py
```

**Workflow per Template:**
1. `01_Forward_Selection.py` (LOCAL) - Two-step FFS for available operators
2. `02_Train_Models.py` (LOCAL) - Train NuSVR models for available operators
3. `03_Query_Prediction.py` (LOCAL) - Bottom-up prediction with passthrough

**Templates:** Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q18, Q19

---

## Why Local Scripts?

LOTO splits may not contain all 13 operators. Example: `Index_Only_Scan` only exists in Q13. When Q13 is held-out, the training data for Q13 has no `Index_Only_Scan` operator.

**Static scripts crash because:**
- They iterate over fixed `OPERATORS_FOLDER_NAMES` (13 operators)
- Missing operators → crash or deadlock

**Local scripts solve this by:**
- Iterating over **available** operator folders
- Using **passthrough** for operators without models

---

## 01 - Forward_Selection.py

**Purpose:** Two-step forward feature selection for available operators in LOTO splits.

**Difference from Static:**
```python
# Static:  for operator in OPERATORS_FOLDER_NAMES:
# Local:   for operator in get_available_operators(dataset_dir):
```

**Import Dependencies:**
- `mapping_config.py` from `/Operator_Level/`
- `ffs_config.py` from `/Operator_Level/Runtime_Prediction/`

---

## 02 - Train_Models.py

**Purpose:** Train SVM models for available operators in LOTO splits.

**Difference from Static:**
```python
# Static:  for operator in OPERATORS_FOLDER_NAMES:
# Local:   for operator in get_available_operators(dataset_dir):
```

**Import Dependencies:**
- `mapping_config.py` from `/Operator_Level/`
- `ffs_config.py` from `/Operator_Level/Runtime_Prediction/`

---

## 03 - Query_Prediction.py

**Purpose:** Bottom-up prediction with passthrough for missing models.

**Differences from Static:**

1. **Passthrough for missing models:**
   - Static: Skips operator → Parents wait forever → Deadlock
   - Local: Uses **passthrough** → Copies max child prediction

2. **Clamping negative predictions:**
   - Static: No clamping (negative predictions possible)
   - Local: `max(0.0, prediction)` for all model outputs

**Passthrough Logic:**
```python
def predict_passthrough(node_id, children, predictions):
    max_exec = 0.0
    max_start = 0.0
    for child in children:
        if child['node_id'] in predictions:
            pred = predictions[child['node_id']]
            if pred['predicted_total_time'] > max_exec:
                max_exec = pred['predicted_total_time']
                max_start = pred['predicted_startup_time']
    return max_start, max_exec
```

**Output Column:** `prediction_type` = `model` or `passthrough`

**Inputs:**
- `test_file` (positional): Path to test dataset CSV
- `overview_file` (positional): Path to two_step_evaluation_overview.csv
- `models_dir` (positional): Directory with trained models
- `--output-file`: Output CSV for predictions (batch mode)

**Variables:**
- `--md-query`: Generate MD report for single query
- `--report`: Generate MD report for first query of each unique plan
- `--report-dir`: Output directory for MD reports (default: md/ in template dir)

**Usage:**
```bash
# Batch prediction
python3 03_Query_Prediction.py test.csv overview.csv Model/ --output-file predictions.csv

# Single query report
python3 03_Query_Prediction.py test.csv overview.csv Model/ --md-query Q1_100_seed_12345

# Reports for all unique plans
python3 03_Query_Prediction.py test.csv overview.csv Model/ --report --report-dir md/
```

**MD Report Contents:**
- Query Tree with ROOT/LEAF markers
- Prediction Chain (Bottom-Up) with model paths and features
- Passthrough steps marked with [PASSTHROUGH]
- Results table with Pred Type column (model/passthrough)

---

## A_01a - Query_Evaluation.py

**Purpose:** Evaluate LOTO predictions and create MRE report with bar plot.

**Inputs:**
- Predictions: `Qx/predictions.csv` (from 00_Batch_Workflow.py)

**Outputs:**
- `{output-dir}/overall_mre.csv` - Overall MRE across all templates
- `{output-dir}/loto_mre.csv` - MRE per LOTO template
- `{output-dir}/loto_mre_plot.png` - Bar plot of MRE by template

**Usage:**
```bash
python3 A_01a_Query_Evaluation.py --output-dir Evaluation
```

---

## A_01b - Static_Dynamic_Comparison.py

**Purpose:** Compare Static vs Dynamic MRE per template with grouped bar plot.

**Inputs:**
- `--static-csv`: Static template MRE CSV (from Baseline_SVM)
- Dynamic: `Evaluation/loto_mre.csv` (relative to script)

**Outputs:**
- `{output-dir}/A_01b_static_dynamic_comparison.csv` - Combined MRE data
- `{output-dir}/A_01b_static_dynamic_comparison.png` - Grouped bar plot

**Usage:**
```bash
python3 A_01b_Static_Dynamic_Comparison.py \
  --static-csv ../../Operator_Level/Runtime_Prediction/Baseline_SVM/Evaluation/A_01f_template_mre.csv \
  --output-dir Evaluation
```
