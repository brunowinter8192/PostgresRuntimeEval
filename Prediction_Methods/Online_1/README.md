# Online_1 - Online Pattern Selection

Online pattern-level prediction that builds pattern models at query-time. For each test query, patterns are mined, ranked by strategy, and greedily selected based on improvement threshold.

## Directory Structure

```
Online_1/
    mapping_config.py
    README.md
    Runtime_Prediction/                  [See DOCS.md](Runtime_Prediction/DOCS.md)
```

## Workflow

### Phase 1: Runtime_Prediction

**Purpose:** Online prediction workflow per test query

**Input:** Test query + Hybrid_2 baseline datasets (Training_Training, Training_Test, Training, Test)

**Output:** Predictions, selection logs, trained models, reports per query

**Details:** [Runtime_Prediction/DOCS.md](Runtime_Prediction/DOCS.md)
