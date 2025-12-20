# Dynamic Plan_Level Workflow

Plan-level runtime prediction for dynamic LOTO workloads.

**Basiert auf:** [Static Plan_Level_1](../../Plan_Level_1/README.md) - adaptiert für LOTO Cross-Validation.

## Konzept

Plan_Level prognostiziert die Query-Laufzeit direkt aus aggregierten Plan-Features ohne Operator-Zerlegung.

### Aggregation

Plan-Features werden aus dem gesamten Query-Plan aggregiert:
- Summen (rows, costs)
- Counts (operator types)
- Strukturelle Merkmale (depth, width)

## Directory Structure

```
Dynamic/
├── Dataset/
│   └── Dataset_Plan/               [See DOCS.md]
└── Runtime_Prediction/
    └── Plan_Level/                 [See DOCS.md]
```

## Workflow

### Phase 1: Dataset

**Purpose:** Create LOTO splits at plan-level

**Input:** `/Plan_Level_1/Data_Generation/csv/complete_dataset.csv`

**Output:** `Dataset_Plan/Qx/{training.csv, test.csv}`

**Details:** [Dataset/Dataset_Plan/DOCS.md](Dataset/Dataset_Plan/DOCS.md)

### Phase 2: Runtime_Prediction

**Purpose:** FFS, model training, and prediction

**Input:** LOTO plan datasets from Phase 1

**Output:** Predictions per template

**Details:** [Runtime_Prediction/Plan_Level/DOCS.md](Runtime_Prediction/Plan_Level/DOCS.md)

## Quick Reproduction

```bash
# Phase 1: Create LOTO splits
cd Dataset/Dataset_Plan
python3 01_LOTO_Split.py \
    ../../../Plan_Level_1/Data_Generation/csv/complete_dataset.csv \
    --output-dir .

# Phase 2: FFS + Train + Predict
cd ../../Runtime_Prediction/Plan_Level
python3 00_Batch_Workflow.py
```

## 14 LOTO Templates

```
Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q18, Q19
```
