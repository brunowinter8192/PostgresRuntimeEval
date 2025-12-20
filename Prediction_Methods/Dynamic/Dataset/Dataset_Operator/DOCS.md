# Dataset_Operator - DOCS

## Working Directory

**CRITICAL:** All commands assume CWD = `Dataset_Operator/`

```bash
cd /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Dynamic/Dataset/Dataset_Operator
```

---

## Directory Structure

```
Dataset_Operator/
├── DOCS.md
├── 01_LOTO_Split.py
└── Q1/, Q3/, ... Q19/
    ├── training.csv
    ├── test.csv
    └── 04a_{Operator}/04a_{Operator}.csv
```

---

## 01 - LOTO_Split.py

**Purpose:** Create LOTO (Leave-One-Template-Out) splits with operator-level structure for all 14 templates.

**Inputs:**
- `input_file`: Path to operator dataset with children (positional)
- `--output-dir`: Output directory for LOTO splits (required)

**Outputs per Template:**
- `Qx/training.csv` - All operators from 13 other templates
- `Qx/test.csv` - All operators from held-out template
- `Qx/04a_{Operator}/04a_{Operator}.csv` - Training data split by node_type

**Usage:**
```bash
python3 01_LOTO_Split.py \
    /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Operator_Level/Datasets/Baseline/02_operator_dataset_with_children.csv \
    --output-dir .
```

**Templates:** Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q18, Q19

**LOTO Logic:**
- Template Qx as test set (150 queries worth of operators)
- All other templates as training set (1950 queries worth of operators)
- Training data additionally split into operator folders for FFS/Training scripts
