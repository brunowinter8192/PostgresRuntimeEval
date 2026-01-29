# Hybrid Pattern-Level Runtime Prediction

ML-based runtime prediction for SQL queries using pattern-level SVM models that group parent operators with their children as single prediction units.

## Static Workload

Dieses Verzeichnis verwendet **Static Workloads**: Train und Test sehen dieselben Templates.

**Datenaufteilung pro Template:**
- **Training:** 120 Queries (Seeds)
- **Test:** 30 Queries (Seeds)

Gegensatz: [Dynamic Workloads](../Dynamic/README_Hybrid_1.md) - LOTO (Leave-One-Template-Out)

## Terminology

**Length:** Number of depth levels a pattern spans (vertical depth)
- Length 2: Parent → Child (depths 0,1)
- Length 3: Parent → Child → Grandchild (depths 0,1,2)

**Size:** Number of operators in a pattern (all nodes including branches)
- `Hash Join → Seq Scan` has Length 2, Size 2
- `Hash Join → [Seq Scan, Hash → Seq Scan]` has Length 3, Size 4

**Passthrough Operators:** Operators with execution time approximately equal to their slowest child (~100-102% ratio). These operators primarily forward data without significant own computation.

Based on analysis (`02_Passthrough_Analysis.py`):

| Operator | Ratio | Classification |
|----------|-------|----------------|
| Incremental Sort | 100.00% | Passthrough |
| Gather Merge | 100.97% | Passthrough |
| Gather | 101.48% | Passthrough |
| Sort | 101.67% | Passthrough |
| Limit | 101.78% | Passthrough |
| Merge Join | 102.24% | Passthrough |

## Directory Structure

```
Hybrid_1/
├── mapping_config.py                    # Shared patterns, targets, and constants
├── Data_Generation/                     [See DOCS.md]
├── Datasets/                            [See DOCS.md]
└── Runtime_Prediction/                  [See DOCS.md]
```

## Shared Infrastructure

**mapping_config.py** - Central configuration shared across all three phases

**Constants:**
- `TARGET_TYPES` - Target variables (execution_time, start_time)
- `NON_FEATURE_SUFFIXES` - Metadata column suffixes to exclude
- `LEAF_OPERATORS` - Leaf node types (SeqScan, IndexScan, IndexOnlyScan)
- `REQUIRED_OPERATORS` - Operators for INCLUDE filter (Hash, Hash Join, Seq Scan, Sort, Nested Loop)
- `PASSTHROUGH_OPERATORS` - Operators for EXCLUDE filter (Incremental Sort, Gather Merge, Gather, Sort, Limit, Merge Join)
- `CHILD_FEATURES_TIMING` - Child timing features (st1, rt1, st2, rt2)
- `FFS_SEED` - Random seed for cross-validation (42)
- `FFS_MIN_FEATURES` - Minimum features to select (1)

**Functions:**
- `pattern_to_folder_name()` - Convert pattern string to folder format
- `is_leaf_operator()` - Check if operator is leaf node
- `is_passthrough_operator()` - Check if operator is passthrough

**Used by:** Scripts in Data_Generation, Datasets, and Runtime_Prediction phases

## Data Configuration

### Baseline Approach

**Definition:** Training/Test-Daten ohne Templates Q2, Q11, Q16, Q22

**Warum entfernt:** Diese Templates enthalten InitPlan/SubPlan Operatoren, die:
- Nicht-standard Parent-Child Beziehungen erzeugen
- Operator-Level Predictions stark verzerren
- Pattern-Matching komplizieren (verschachtelte Subqueries)

**Dateien:** `Operator_Level/Datasets/Baseline/04_training.csv` und `04_test.csv`

### All Templates Approach

**Definition:** Kompletter Datensatz mit allen 22 TPC-H Templates (inkl. Q2, Q11, Q16, Q22)

**Wann verwenden:** Wenn InitPlan/SubPlan Patterns explizit analysiert werden sollen

**Dateien:** `Operator_Level/Data_Generation/csv/operator_dataset_{ts}.csv`

## Workflow Overview

The hybrid pattern-level prediction pipeline consists of three sequential phases:

**Phase 1 → Phase 2 → Phase 3**

1. **Data_Generation**: Analyze operator dataset to identify recurring parent-child patterns → Produces pattern inventory with occurrence counts

2. **Datasets**: Extract pattern instances, aggregate parent+children into single rows, clean features → Produces pattern-specific training datasets

3. **Runtime_Prediction**: Train pattern-level SVM models, perform hybrid bottom-up prediction (pattern models for matched patterns, operator models for fallback) → Produces predictions and evaluation results

**Hybrid Concept:** Instead of predicting each operator individually, this approach groups parent operators with their immediate children into "patterns" (e.g., Hash_Join with Seq_Scan outer and Hash inner). Models are trained on these aggregated units. Operators not matching any pattern use fallback operator-level models trained within Hybrid_1.

## Model Training Architecture

**Train Once, Use Flexibly:**

FFS and model training is performed ONCE for all 372 mined patterns:
- `01_Feature_Selection.py` - FFS for all 372 patterns
- `02_Train_Models.py` - Train models for all 372 patterns

Each approach then selects a SUBSET at prediction time via `patterns_filtered.csv`:
- approach_1: 14 patterns (length=2, required_operators)
- approach_2: 10 patterns (length=2, no_passthrough)
- approach_3: 72 patterns (all lengths, threshold>150)
- approach_4: 53 patterns (all lengths, no_passthrough, threshold>150)

This avoids redundant training and allows flexible experimentation with different pattern subsets.

## Phase Documentation

### Phase 1: Data_Generation

**Purpose:** Discover and catalog all parent-child patterns in the training data with MD5 hash identification

**Input:** Operator dataset CSV

**Process:**
- Identify all unique parent-child combinations (parent + outer child + inner child)
- Starting from depth 0 (includes root-level patterns)
- Filter patterns by REQUIRED_OPERATORS (Gather, Hash, Hash Join, Nested Loop, Seq Scan)
- Compute MD5 hash for each pattern structure
- Count pattern occurrences across all queries

**Output:** Pattern inventory CSV with pattern_hash, pattern names, and occurrence counts

**See Data_Generation/DOCS.md for detailed script documentation**

### Phase 2: Datasets

**Purpose:** Split data, extract operators and patterns, prepare training datasets

**Input:** Operator dataset CSV

**Process (5-Script Pipeline):**
1. Split into training/test sets (template-stratified, 120/30 per template)
2. Extract operators to type-specific folders
3. Extract patterns to MD5 hash folders with pattern_info.json
4. Aggregate parent and child rows into single feature vectors
5. Clean features by removing unavailable columns

**Output:**
- `training.csv` / `test.csv` - Template-stratified train/test split
- `Operators/{Type}/training.csv` - Operator-specific training datasets (13 types)
- `approach_X/patterns.csv` - Pattern inventory with hash, string, length, occurrence count
- `approach_X/patterns/{hash}/` - Pattern folders with training.csv, training_aggregated.csv, training_cleaned.csv, pattern_info.json
- `Verification/` - Extraction and aggregation verification results

**Pattern Filtering Approaches:**

| Approach | Filter | Length | Patterns (selected) |
|----------|--------|--------|---------------------|
| 1 | `required_operators` | 2 | 14 |
| 2 | `no_passthrough` | 2 | 10 |
| 3 | `none` | all | 72 |
| 4 | `no_passthrough` | all | 53 |

**See Datasets/DOCS.md for detailed script documentation**

### Phase 3: Runtime_Prediction

**Purpose:** Train pattern-level and operator-level models, perform hybrid bottom-up prediction

**Input:**
- Pattern training datasets from Phase 2 (patterns/{hash}/training_cleaned.csv)
- Operator training datasets from Phase 2 (operators/{type}/training.csv)

**Process:**
- Perform forward feature selection for patterns (01_Feature_Selection.py)
- Perform forward feature selection for operators (01b_Feature_Selection_Operators.py)
- Train pattern-level SVM models (02_Train_Models.py)
- Train operator-level SVM models (02b_Train_Models_Operators.py)
- Execute hybrid bottom-up prediction on test queries:
  - For operators matching a pattern → Use pattern model
  - For unmatched operators → Use operator-level model (fallback)
- Evaluate prediction accuracy by node type and template

**Output:**
- `SVM/Patterns/two_step_evaluation_overview.csv` - Pattern FFS results with selected features per pattern-target
- `SVM/Operators/operator_overview.csv` - Operator FFS results with selected features per operator-target
- `Model/Patterns/{target}/{hash}/model.pkl` - Trained pattern SVM models (372 patterns x 2 targets)
- `Model/{target}/operators/{type}/model.pkl` - Trained operator SVM models (13 operators x 2 targets)
- `Predictions/approach_X/predictions.csv` - Hybrid predictions per approach with pattern/operator/passthrough types

**See Runtime_Prediction/DOCS.md for detailed script documentation**
