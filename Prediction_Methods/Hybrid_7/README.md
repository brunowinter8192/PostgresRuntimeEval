# Hybrid_7 - Pattern-Level Prediction

Pattern-based query runtime prediction using greedy pattern selection. Combines operator-level models with pattern-level models for improved accuracy.

## Directory Structure

```
Hybrid_7/
    mapping_config.py
    Parameter.md
    README.md
    Data_Generation/                     [See DOCS.md]
    Dataset/                             [See DOCS.md]
    Runtime_Prediction/                  [See DOCS.md]
```

## Workflow

### Phase 1: Data_Generation

**Purpose:** Mine structural patterns from query execution plans.

**Input:** Operator dataset (from Operator_Level)

**Output:** Pattern definitions with occurrence counts

**Details:** [Data_Generation/DOCS.md](Data_Generation/DOCS.md)

---

### Phase 2: Dataset

**Purpose:** Split data and extract pattern-specific training sets.

**Input:** Operator dataset + Pattern definitions

**Output:** Train/Test splits + per-pattern training CSVs

**Details:** [Dataset/DOCS.md](Dataset/DOCS.md)

---

### Phase 3: Runtime_Prediction

**Purpose:** Feature selection, model training, pattern selection, and prediction.

**Input:** Pattern datasets + Operator models

**Output:** Predictions with evaluation metrics

**Details:** [Runtime_Prediction/DOCS.md](Runtime_Prediction/DOCS.md)
