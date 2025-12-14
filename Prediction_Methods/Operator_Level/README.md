# Operator_Level - Operator-Level Prediction

SVM-based runtime prediction at operator level. Trains 26 models (13 operators x 2 targets) using features from PostgreSQL EXPLAIN output.

## Directory Structure

```
Operator_Level/
    mapping_config.py                    Shared config (self-documenting)
    README.md
    Data_Generation/                     [See DOCS.md](Data_Generation/DOCS.md)
    Datasets/                            [See DOCS.md](Datasets/DOCS.md)
    Runtime_Prediction/                  [See DOCS.md](Runtime_Prediction/DOCS.md)
```

## Workflow

### Phase 1: Data_Generation

**Purpose:** Extract operator features and runtime targets from PostgreSQL query plans.

**Input:** TPC-H queries (Q1-Q22, excluding Q15)

**Output:** `operator_dataset.csv` (18 columns: 6 metadata + 10 features + 2 targets)

**Details:** [Data_Generation/DOCS.md](Data_Generation/DOCS.md)

---

### Phase 2: Datasets

**Purpose:** Filter templates, add child features, create train/test splits.

**Input:** operator_dataset.csv

**Output:** Baseline/ folder with training and test CSVs

**Details:** [Datasets/DOCS.md](Datasets/DOCS.md)

---

### Phase 3: Runtime_Prediction

**Purpose:** Forward feature selection, SVM training, bottom-up prediction, evaluation.

**Input:** Baseline/ training and test data

**Output:** Baseline_SVM/ with models, predictions, and evaluation metrics

**Details:** [Runtime_Prediction/DOCS.md](Runtime_Prediction/DOCS.md)
