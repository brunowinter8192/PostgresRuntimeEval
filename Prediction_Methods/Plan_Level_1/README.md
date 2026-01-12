# Plan_Level_1

Plan-level runtime prediction for TPC-H queries using ML-based feature selection and regression models.

## Directory Structure

```
Plan_Level_1/
    mapping_config.py
    README.md
    Data_Generation/                      [See DOCS.md]
    Datasets/                             [See DOCS.md]
    Runtime_Prediction/                   [See DOCS.md]
```

## Workflow

### Phase 1: Data_Generation

**Purpose:** Extract features and measure runtime for TPC-H queries

**Input:** Query directory with Q1/-Q22/ template folders containing SQL files

**Output:** `complete_dataset.csv` (2850 samples x 53 columns)

**Details:** [Data_Generation/DOCS.md](Data_Generation/DOCS.md)

---

### Phase 2: Datasets

**Purpose:** Create train/test splits and dataset transformations

**Input:** `complete_dataset.csv` from Data_Generation

**Output:** Train/test CSVs in Baseline/, State_1/ directories

**Details:** [Datasets/DOCS.md](Datasets/DOCS.md)

---

### Phase 3: Runtime_Prediction

**Purpose:** ML model training and evaluation for query runtime prediction

**Input:** `training_data.csv`, `test_data.csv` from Datasets

**Output:** FFS results, trained models, predictions, evaluation plots

**Details:** [Runtime_Prediction/DOCS.md](Runtime_Prediction/DOCS.md)
