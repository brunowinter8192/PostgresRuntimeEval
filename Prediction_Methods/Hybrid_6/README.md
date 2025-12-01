# Hybrid_6 - Pattern-Level Prediction with 3-Level Fallback

Pattern-level runtime prediction combining greedy pattern matching with pass-through inheritance and operator fallback.

## Directory Structure

```
Hybrid_6/
├── mapping_config.py                      # Shared configuration
├── README.md                              # Workflow documentation (THIS FILE)
├── Datasets/                              [See DOCS.md]
│   ├── 01_Calculate_Counts.py
│   ├── 02_Extract_Patterns.py
│   ├── 03_Aggregate_Patterns.py
│   ├── 04_Clean_Aggregated.py
│   ├── A_01a_Verify_Extraction.py
│   ├── A_01b_Verify_Aggregation.py
│   ├── A_01c_Analyze_NaN.py
│   ├── Baseline/                          # Pattern datasets (32 pattern folders)
│   └── csv/                               # Verification reports
└── Runtime_Prediction/                    [See DOCS.md]
    ├── 01_Clean_FFS.py
    ├── 02_Train_Models.py
    ├── 03_Predict_Queries.py
    ├── A_01a_Evaluate_Predictions.py
    ├── A_01b_Node_Evaluation.py
    ├── A_01c_Time_Analysis.py
    ├── Baseline_SVM/                      # SVM outputs, Models, Evaluation
    └── csv/                               # Cleaned FFS
```

## Shared Infrastructure

**mapping_config.py:**
- `PATTERNS`: List of 32 pattern hash IDs
- `PATTERN_OPERATOR_COUNT`: Dict mapping pattern hash to operator count (2-15)
- `PATTERN_LEAF_TIMING_FEATURES`: Dict mapping pattern hash to leaf timing features
- `TARGET_TYPES`: ['execution_time', 'start_time']
- `TARGET_NAME_MAP`: Target type to column name mapping
- `NON_FEATURE_SUFFIXES`: Column suffixes excluded from FFS
- `PASSTHROUGH_OPERATORS`: 7 operators with startup_total_ratio > 0.95
- `is_passthrough_operator()`: Helper function

## Datasets

| Dataset | Patterns | Samples/Pattern | Purpose |
|---------|----------|-----------------|---------|
| Baseline | 32 | Variable (120-1000+) | Pattern-level training data with cleaned leaf features |

## Workflow Overview

```
Phase 1: Datasets (Extract + Aggregate)
01_Calculate_Counts.py --> 02_Extract_Patterns.py --> 03_Aggregate_Patterns.py --> 04_Clean_Aggregated.py
                                    |                          |
                        A_01a_Verify_Extraction      A_01b_Verify_Aggregation
                                                               |
                                                     A_01c_Analyze_NaN

Phase 2: Runtime_Prediction (Train + Predict)
01_Clean_FFS.py --> 02_Train_Models.py --> 03_Predict_Queries.py
                                                   |
                           A_01a/A_01b/A_01c (Evaluation + Analysis)
```

## Phase Documentation

### Phase 1: Datasets

**Purpose:** Extract, aggregate, and clean pattern-level datasets from Operator_Level data

**Input:**
- Operator_Level training dataset (`../../Operator_Level/Datasets/Baseline/training_cleaned.csv`)
- Pattern mining results (`../Data_Generation/csv/01_patterns_*.csv`)

**Output:**
- `Baseline/<pattern_hash>/training_cleaned.csv` (32 pattern datasets, aggregated and cleaned)

**Details:** See [Datasets/DOCS.md](Datasets/DOCS.md)

---

### Phase 2: Runtime_Prediction

**Purpose:** Train pattern models and predict query runtimes using 3-level fallback

**Input:**
- FFS overview CSV (from Baseline_SVM)
- Pattern Plan Leaf Mapping (from Data_Generation)
- Pattern Datasets (from Datasets/Baseline)
- Test Dataset
- Operator Models (from Operator_Level)

**Output:**
- Trained Pattern Models (`Model/{target}/{pattern_hash}/model.pkl`)
- `predictions.csv` with query-level predictions
- Evaluation metrics (MRE by template, node type)

**Details:** See [Runtime_Prediction/DOCS.md](Runtime_Prediction/DOCS.md)

## Key Concepts

### 3-Level Fallback Strategy

1. **Pattern Match:** If operator matches a pattern - Use pattern model
2. **Pass-Through:** If PT operator with children - Inherit child prediction
3. **Operator Fallback:** Otherwise - Use operator-level model

### Pass-Through Operators

Operators with startup_total_ratio > 0.95 (excluded as pattern roots):
- Incremental Sort
- Merge Join
- Sort
- Hash
- Limit
- Gather Merge
- Aggregate

### Pattern+Plan Leaf Concept

- **Pattern Leaf:** Deepest operator within pattern structure
- **Plan Leaf:** Operator with no children in entire query plan
- **Pattern+Plan Leaf:** Both - Child features (st1, rt1, st2, rt2) always 0, removed from FFS
