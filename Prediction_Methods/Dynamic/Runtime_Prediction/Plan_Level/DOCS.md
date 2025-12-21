# Plan_Level - DOCS

## Working Directory

**CRITICAL:** All commands assume CWD = `Plan_Level/`

```bash
cd /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Dynamic/Runtime_Prediction/Plan_Level
```

---

## Directory Structure

```
Plan_Level/
├── DOCS.md
├── 00_Batch_Workflow.py
└── Q1/, Q3/, ... Q19/
    ├── SVM/
    └── 02_predictions_*.csv
```

---

## 00 - Batch_Workflow.py

**Purpose:** Run complete Plan_Level workflow (FFS, Train) for all 14 LOTO templates using Plan_Level_1 scripts.

**Inputs:**
- Dataset: `../../Dataset/Dataset_Plan/Qx/` (from 01_LOTO_Split.py)
- Scripts: `/Plan_Level_1/Runtime_Prediction/` (01, 02)

**Outputs per Template:**
- `Qx/SVM/01_ffs_summary.csv` - FFS results
- `Qx/SVM/01_ffs_stability.csv` - Feature stability
- `Qx/02_predictions_*.csv` - Predictions on test set

**Usage:**
```bash
python3 00_Batch_Workflow.py
```

**Workflow per Template:**
1. `01_Forward_Selection.py` - Multi-seed FFS with NuSVR
2. `02_Train_Model.py` - Train model and predict on test set

**Templates:** Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q18, Q19

**Note:** Uses Plan_Level_1 scripts via subprocess calls (no local copy needed).

---

## A_01a - Query_Evaluation.py

**Purpose:** Evaluate LOTO predictions and create MRE report with bar plot.

**Inputs:**
- Predictions: `Qx/02_predictions_*.csv` (from 00_Batch_Workflow.py)

**Outputs:**
- `{output-dir}/overall_mre.csv` - Overall MRE across all templates
- `{output-dir}/loto_mre.csv` - MRE per LOTO template
- `{output-dir}/loto_mre_plot.png` - Bar plot of MRE by template

**Usage:**
```bash
python3 A_01a_Query_Evaluation.py --output-dir Evaluation
```
