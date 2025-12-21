# Operator_Level - DOCS

## Working Directory

**CRITICAL:** All commands assume CWD = `Operator_Level/`

```bash
cd /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level
```

---

## Directory Structure

```
Operator_Level/
├── DOCS.md
├── 00_Batch_Workflow.py
├── 01_Forward_Selection.py
└── Q1/, Q3/, ... Q19/
    ├── SVM/
    ├── Model/
    └── predictions.csv
```

---

## 00 - Batch_Workflow.py

**Purpose:** Run complete Operator_Level workflow (FFS, Train, Predict) for all 14 LOTO templates.

**Inputs:**
- Dataset: `../../Dataset/Dataset_Operator/Qx/` (from 01_LOTO_Split.py)
- Scripts: `/Prediction_Methods/Operator_Level/Runtime_Prediction/` (02, 03)
- Local: `01_Forward_Selection.py`

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
2. `02_Train_Models.py` - Train NuSVR models for available operators
3. `03_Query_Prediction.py` - Bottom-up prediction with child propagation

**Templates:** Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q18, Q19

---

## 01 - Forward_Selection.py (Local Copy)

**Purpose:** Two-step forward feature selection for available operators in LOTO splits.

**Why local copy instead of using Operator_Level original:**

LOTO splits may not contain all 13 operators. Example: `Index_Only_Scan` only exists in Q13. When Q13 is held-out, the training data for Q13 has no `Index_Only_Scan` operator.

The original script iterates over a fixed `OPERATORS_FOLDER_NAMES` list and crashes on missing folders. This local copy iterates over **available** operator folders instead.

**Difference from original:**
```python
# Original: for operator in OPERATORS_FOLDER_NAMES:
# Local:    for operator in get_available_operators(dataset_dir):
```

**Import Dependencies:**
- `mapping_config.py` from `/Operator_Level/`
- `ffs_config.py` from `/Operator_Level/Runtime_Prediction/`

Both paths must be in sys.path for imports to work.

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

**Note:** Q13 and Q18 are excluded from results because they contain operators that don't exist in any other template.
