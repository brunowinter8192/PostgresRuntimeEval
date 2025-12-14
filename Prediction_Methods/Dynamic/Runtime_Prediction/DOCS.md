# Runtime_Prediction - DOCS

**Note:** This DOCS.md covers all batch scripts at root level. Not CLAUDE.md compliant (should be per-directory), but avoids overengineering for simple batch wrappers.

---

## Working Directory

**CRITICAL:** All commands assume CWD = `Runtime_Prediction/`

```bash
cd /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Dynamic/Runtime_Prediction
```

---

## Directory Structure

```
Runtime_Prediction/
├── DOCS.md
├── Operator_Level/
│   ├── 00_Batch_Workflow.py
│   ├── 01_Forward_Selection.py
│   └── Q1/, Q3/, ... Q19/
│       ├── SVM/
│       ├── Model/
│       └── predictions.csv
└── Plan_Level/
    ├── 00_Batch_Workflow.py
    └── Q1/, Q3/, ... Q19/
        ├── SVM/
        └── 02_predictions_*.csv
```

---

## Operator_Level/00_Batch_Workflow.py

**Purpose:** Run complete Operator_Level workflow (FFS, Train, Predict) for all 14 LOTO templates.

**Input:**
- Dataset: `../Dataset/Dataset_Operator/Qx/` (from 01_LOTO_Split.py)
- Scripts: `/Prediction_Methods/Operator_Level/Runtime_Prediction/` (02, 03)
- Local: `01_Forward_Selection.py` (see below)

**Output per Template:**
- `Qx/SVM/two_step_evaluation_overview.csv` - FFS results
- `Qx/Model/{target}/{operator}/model.pkl` - Trained models
- `Qx/predictions.csv` - Bottom-up predictions

**Usage:**
```bash
cd Operator_Level
python3 00_Batch_Workflow.py
```

**Workflow per Template:**
1. `01_Forward_Selection.py` (LOCAL) - Two-step FFS for available operators
2. `02_Train_Models.py` - Train NuSVR models for available operators
3. `03_Query_Prediction.py` - Bottom-up prediction with child propagation

**Templates:** Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q18, Q19

---

## Operator_Level/01_Forward_Selection.py (Local Copy)

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

## Plan_Level/00_Batch_Workflow.py

**Purpose:** Run complete Plan_Level workflow (FFS, Train) for all 14 LOTO templates using Plan_Level_1 scripts.

**Input:**
- Dataset: `../Dataset/Dataset_Plan/Qx/` (from 01_LOTO_Split.py)
- Scripts: `/Plan_Level_1/Runtime_Prediction/` (01, 02)

**Output per Template:**
- `Qx/SVM/01_ffs_summary.csv` - FFS results
- `Qx/SVM/01_ffs_stability.csv` - Feature stability
- `Qx/02_predictions_*.csv` - Predictions on test set

**Usage:**
```bash
cd Plan_Level
python3 00_Batch_Workflow.py
```

**Workflow per Template:**
1. `01_Forward_Selection.py` - Multi-seed FFS with NuSVR
2. `02_Train_Model.py` - Train model and predict on test set

**Templates:** Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q18, Q19

**Note:** Uses Plan_Level_1 scripts via subprocess calls (no local copy needed).

---

## Hybrid_1/01_Batch_Hybrid_Prediction.py

**Purpose:** Run complete Hybrid_1 workflow (FFS, Train, Predict) for all 14 LOTO templates using only pre-filtered patterns.

**Input:**
- Pattern datasets: `../Dataset/Dataset_Hybrid_1/Qx/approach_4/`
- Pattern filter: `used_patterns.csv` (from 00_Dry_Prediction.py)
- Operator models: `Operator_Level/Qx/Model/` (symlinked)
- Scripts: `Hybrid_1/Runtime_Prediction/` (01, 02, 03_Predict_Queries)

**Output per Template:**
- `Qx/approach_4/SVM/two_step_evaluation_overview.csv` - Pattern FFS results
- `Qx/approach_4/Model/Patterns/{target}/{hash}/model.pkl` - Trained pattern models
- `Qx/approach_4/Model/Operators/` - Symlinks to operator models
- `Qx/approach_4/predictions.csv` - Hybrid predictions
- `Qx/approach_4/patterns.csv` - Pattern usage summary

**Usage:**
```bash
cd Hybrid_1
python3 01_Batch_Hybrid_Prediction.py
```

**Workflow per Template:**
1. `01_Feature_Selection.py` with `--pattern-filter used_patterns.csv` - FFS only for used patterns
2. `02_Train_Models.py` with `--pattern-filter used_patterns.csv` - Train only used pattern models
3. Symlink operator models from `Operator_Level/Qx/Model/`
4. `03_Predict_Queries.py` - Hybrid bottom-up prediction

**Key Optimization:** The `--pattern-filter` flag ensures FFS and training only process patterns that will actually be used for prediction. Combined with `00_Dry_Prediction.py`, this reduces processing from 100+ patterns to typically 2-10 per template.

**Templates:** Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q18, Q19

**Prerequisites:**
- `Dataset/Dataset_Operator/` LOTO splits must exist
- `Dataset/Dataset_Hybrid_1/` pattern extraction must be complete
- `Runtime_Prediction/Operator_Level/` must have trained operator models
