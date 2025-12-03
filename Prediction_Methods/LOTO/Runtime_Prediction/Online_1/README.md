# Dynamic - On-The-Fly Pattern-Based Query Runtime Prediction

## Introduction

Dynamic implements a complete on-the-fly modeling pipeline for SQL query runtime prediction using pattern-based feature engineering. Unlike pre-trained approaches (Hybrid methods), Dynamic trains models during prediction time, enabling true evaluation of unseen query templates through 13-out-of-14 leave-one-template-out (LOTO) cross-validation.

## Core Concept: On-The-Fly Modeling

**Problem:** Pre-trained models (Hybrid_1-5) cannot truly evaluate unseen queries because models are trained on ALL templates, including the test template. This creates data leakage.

**Solution:** Dynamic trains models on-the-fly for each test query:
1. Split training data by template (13 templates for training, 1 for testing)
2. For each test query:
   - Extract patterns from test query operators
   - Train pattern-specific models on 13 training templates
   - Train operator-specific models on 13 training templates
   - Predict test query using newly trained models

**Result:** True unseen query evaluation - test template is completely excluded from model training.

## 13-Out-of-14 Leave-One-Template-Out (LOTO) Cross-Validation

TPC-H provides 14 query templates: Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q18, Q19

**Cross-Validation Strategy:**
```
Fold 1: Train on [Q3-Q19], Test on [Q1]
Fold 2: Train on [Q1, Q4-Q19], Test on [Q3]
Fold 3: Train on [Q1, Q3, Q5-Q19], Test on [Q4]
...
Fold 14: Train on [Q1-Q18], Test on [Q19]
```

Each fold:
- Training set: 13 templates (13 × 150 = 1,950 query variants)
- Test set: 1 template (1 × 150 = 150 query variants)
- Models trained fresh for each fold

## Key Differences from Other Methods

### vs. Operator_Level
| Aspect | Operator_Level | Dynamic |
|--------|----------------|---------|
| **Granularity** | Individual operators | Patterns + Operators (fallback) |
| **Context** | Single operator features | Hierarchical pattern features |
| **Training** | One-time, all data | On-the-fly, per fold |
| **Prediction** | Operator-by-operator | Pattern-first, operator-fallback |

### vs. Hybrid_5
| Aspect | Hybrid_5 | Dynamic |
|--------|----------|---------|
| **Model Training** | Pre-trained (offline) | On-the-fly (online) |
| **Pattern Discovery** | Pre-mined 72 patterns | Uses same 72 patterns |
| **Feature Extraction** | Pre-computed datasets | Extracted during prediction |
| **Aggregation** | Pre-aggregated features | Aggregated during prediction |
| **Data Leakage** | Possible (all templates in training) | None (test template excluded) |
| **Evaluation** | Cannot test truly unseen queries | True unseen query evaluation |

### Why On-The-Fly?

Hybrid_5 pipeline:
```
All Data → Pattern Mining → Feature Extraction → Aggregation → Training → Prediction
         [Offline Phase - All Templates]                       [Test on Same Templates]
```

Dynamic pipeline:
```
For each fold:
  13 Templates → Pattern Extraction → Aggregation → Training → Prediction on 1 Template
                [On-The-Fly - Excluded Test Template]          [Truly Unseen]
```

## Workflow Overview

### Phase 1: Datasets

**Module:** `Datasets/`
**Documentation:** [See Datasets/DOCS.md]

**Purpose:** Prepare 13-out-of-14 train/test splits

**Scripts:**
1. `01_Split_Templates.py` - Create 14 subdirectories with LOTO splits
2. `02_Clean_Test.py` - Remove child timing features from test sets

**Output:** 14 template folders in `Datasets/Baseline/`, each containing:
- `training_cleaned.csv` (13 templates)
- `test_cleaned.csv` (1 template)
- `02_test_cleaned.csv` (test without child timing features)

### Phase 2: Runtime_Prediction

**Module:** `Runtime_Prediction/`
**Documentation:** [See Runtime_Prediction/DOCS.md]

**Purpose:** Complete on-the-fly modeling and prediction pipeline

**Scripts:**
1. `01_Predict_OnTheFly.py` - End-to-end prediction with on-the-fly training

**Output:** 14 prediction files in `Runtime_Prediction/Predictions/`, each containing:
- `predictions.csv` (all test query predictions with actual vs. predicted times)

## Shared Infrastructure

### mapping_config.py

**Location:** `Dynamic/mapping_config.py`

**Contents:**
- `PATTERNS` - List of 72 pattern hashes (from Hybrid_5 pattern mining)
- `PATTERN_OPERATOR_COUNT` - Operator count per pattern (for chunking)
- `CHILD_FEATURES_TIMING` - Child timing features to remove from test sets

**Purpose:** Central configuration for pattern definitions and feature mappings

**Note:** PATTERNS are discovered from Hybrid_5's Data_Generation phase. Dynamic reuses these patterns but applies them on-the-fly rather than pre-computing datasets.

## Technical Architecture

### Pattern-Based Prediction

Dynamic uses the same pattern-matching approach as Hybrid_5:
1. **Hash-Based Matching:** MD5 structural hashing of operator subtrees
2. **Greedy Selection:** Longest patterns first, depth-first processing
3. **Conflict Resolution:** Consumed node tracking prevents overlaps
4. **Fallback:** Operator-level models for unmatched operators

### On-The-Fly Execution

For each test query, Dynamic performs:
```
Query Operators (Flat Table)
    ↓
[Phase 1: Extract Patterns]
    → Build tree from operators
    → Match patterns using structural hashing
    → Extract operator rows for each pattern
    ↓
[Phase 2: Aggregate Features]
    → Chunk by PATTERN_OPERATOR_COUNT
    → Build tree and aggregate hierarchical features
    → Create pattern-level feature vectors
    ↓
[Phase 3: Train Models]
    → Train pattern-specific SVM models (on 13 templates)
    → Train operator-specific SVM models (on 13 templates)
    ↓
[Phase 4: Build Execution Plan]
    → Greedy pattern matching (top-down, depth-first)
    → Identify pattern steps and operator steps
    ↓
[Phase 5: Execute Predictions]
    → Bottom-up propagation
    → Cache child predictions
    → Aggregate features with child timings
    → Predict with trained models
    ↓
Predictions (Node-Level + Root-Level)
```

### Why This Matters

**Hybrid_5 Problem:**
- Trains models on all 14 templates
- Tests on same 14 templates
- Cannot simulate real-world "unseen query" scenario

**Dynamic Solution:**
- Trains models on 13 templates only
- Tests on the 14th (completely unseen) template
- Simulates real production scenario: new query type arrives

## Execution Flow

### Complete Pipeline

```bash
# Step 1: Split data into 14 LOTO folds
python3 Datasets/01_Split_Templates.py \
    Operator_Level/Datasets/Baseline/02_operator_dataset_cleaned.csv \
    --output-dir Datasets/Baseline

# Step 2: Clean test sets (remove child timing features)
python3 Datasets/02_Clean_Test.py \
    Datasets/Baseline

# Step 3: Run on-the-fly prediction for all 14 folds
python3 Runtime_Prediction/01_Predict_OnTheFly.py \
    Datasets/Baseline \
    Operator_Level/Datasets/Baseline/02_operator_dataset_cleaned.csv \
    --output-dir Runtime_Prediction/Predictions
```

### Output

```
Runtime_Prediction/Predictions/
├── Q1/predictions.csv    (Q1 test queries predicted with Q3-Q19 training)
├── Q3/predictions.csv    (Q3 test queries predicted with Q1,Q4-Q19 training)
├── Q4/predictions.csv
...
└── Q19/predictions.csv   (Q19 test queries predicted with Q1-Q18 training)
```

## Datasets Philosophy

### Template-Based Splitting

Dynamic uses template-level splitting (not random query splitting) because:
1. **Structural Similarity:** Queries from the same template have identical structure
2. **Real-World Scenario:** New query types (templates) arrive in production
3. **True Generalization:** Models must generalize to unseen query structures

### Feature Engineering

**Operator-Level Features:**
- Single operator attributes (e.g., `row_estimate`, `plan_width`)
- Child timing features (e.g., `st1`, `rt1`, `st2`, `rt2`)

**Pattern-Level Features:**
- Hierarchical prefixes (e.g., `HashJoin_node_type`, `SeqScan_Outer_row_estimate`)
- Aggregated subtree information
- Child timing features for leaf operators only

### Why Remove Child Timing from Test?

Child timing features (`st1`, `rt1`, `st2`, `rt2`) represent actual runtimes of child operators. During prediction:
- These values are UNKNOWN (haven't executed yet)
- Removing them simulates real prediction scenario
- Bottom-up propagation fills them with predicted values

## Comparison Summary

| Method | Training | Patterns | Unseen Eval | Data Leakage |
|--------|----------|----------|-------------|--------------|
| **Operator_Level** | One-time | No | Random split | Minimal |
| **Hybrid_1-5** | One-time | Yes | No | Yes (all templates) |
| **Dynamic** | On-the-fly | Yes | Yes (LOTO) | None |

**Dynamic is the only method that provides true unseen template evaluation.**

## Performance Considerations

### Computational Cost

**Hybrid_5:**
- Training: Once (offline, ~10 minutes for 72 patterns)
- Prediction: Fast (~1 second per query)

**Dynamic:**
- Training: 14 times (one per fold, ~10 minutes each)
- Prediction: Slower (~5-10 seconds per query due to on-the-fly extraction/aggregation)
- Total: ~2-3 hours for complete 14-fold evaluation

**Trade-off:** Dynamic sacrifices speed for true unseen query evaluation.

### Memory Requirements

- Pattern extraction: Builds trees for each query (~100 MB per fold)
- Model training: Holds models in memory (~50 MB per fold)
- Total peak memory: ~500 MB per fold (manageable)

## Future Enhancements

1. **Parallel Fold Execution:** Run 14 folds in parallel to reduce total time
2. **Incremental Pattern Discovery:** Discover patterns from training folds only
3. **Adaptive Feature Selection:** Perform FFS on-the-fly per pattern
4. **Caching:** Cache extracted patterns across queries with same structure

## Related Methods

- **Operator_Level:** Baseline operator-level prediction (no patterns)
- **Hybrid_1:** Pattern-level with depth 0 only
- **Hybrid_2:** Pattern-level with all depths
- **Hybrid_3:** Pattern-level with extended pass-through
- **Hybrid_4:** Pattern-level with full pass-through
- **Hybrid_5:** Pattern + Plan Leaf optimization

Dynamic builds on Hybrid_5's pattern-matching logic but applies it on-the-fly for true unseen query evaluation.
