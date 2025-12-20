# Dataset_Plan - DOCS

## Working Directory

**CRITICAL:** All commands assume CWD = `Dataset_Plan/`

```bash
cd /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Dynamic/Dataset/Dataset_Plan
```

---

## Directory Structure

```
Dataset_Plan/
├── DOCS.md
├── 01_LOTO_Split.py
└── Q1/, Q3/, ... Q19/
    ├── training.csv
    └── test.csv
```

---

## 01 - LOTO_Split.py

**Purpose:** Create LOTO (Leave-One-Template-Out) splits at plan-level for all 14 templates.

**Inputs:**
- `input_file`: Path to complete plan-level dataset (positional)
- `--output-dir`: Output directory for LOTO splits (required)

**Outputs per Template:**
- `Qx/training.csv` - All queries from 13 other templates
- `Qx/test.csv` - All queries from held-out template

**Usage:**
```bash
python3 01_LOTO_Split.py \
    ../../../Plan_Level_1/Data_Generation/csv/complete_dataset.csv \
    --output-dir .
```

**Templates:** Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q18, Q19

**LOTO Logic:**
- Template Qx as test set (150 queries)
- All other templates as training set (1950 queries)
- No operator-level split (plan-level aggregation)
