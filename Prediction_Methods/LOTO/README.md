# LOTO - README

Leave-One-Template-Out (LOTO) evaluation workflow for TPC-H query runtime prediction.

---

## Directory Structure

```
LOTO/
├── README.md                    # This file
├── Dataset/                     [See DOCS.md]
├── Dataset_Operator/            [See DOCS.md]
└── Runtime_Prediction/          [See DOCS.md]
```

---

## Workflow Overview

```
Phase 1: Dataset
Phase 2: Runtime_Prediction

Dataset -> Runtime_Prediction
```

---

## Phase 1: Dataset

**Purpose:** Create LOTO train/test splits (13 templates training, 1 template test)

**Input:** complete_dataset.csv (from Plan_Level_1 or other source)

**Output:** QX/{training.csv, test.csv} per template

**Details:** [Dataset/DOCS.md](Dataset/DOCS.md)

---

## Phase 2: Runtime_Prediction

**Purpose:** Predict query runtime using ML models

**General Pipeline:**
1. Feature Selection (FFS with cross-validation)
2. Model Training (per held-out template)
3. Prediction (on test template)
4. Evaluation (metrics + comparison)

**Input:** Dataset/QX/{training.csv, test.csv}

**Output:** Evaluation/comparison.csv, comparison_plot.png

**Details:** [Runtime_Prediction/DOCS.md](Runtime_Prediction/DOCS.md)
