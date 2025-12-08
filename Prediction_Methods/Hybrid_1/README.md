# Hybrid Pattern-Level Runtime Prediction

ML-based runtime prediction for SQL queries using pattern-level SVM models that group parent operators with their children as single prediction units.

## Directory Structure

```
Hybrid_1/
├── mapping_config.py                    # Shared patterns, targets, and constants
├── Data_Generation/                     [See DOCS.md]
├── Datasets/                            [See DOCS.md]
└── Runtime_Prediction/                  [See DOCS.md]
```

## External Dependencies

**Operator_Level Models (Fallback):**
```
Operator_Level/Runtime_Prediction/Baseline_SVM/
├── Model/
│   ├── execution_time/{operator_type}/model.pkl
│   └── start_time/{operator_type}/model.pkl
└── SVM/two_step_evaluation_overview.csv
```

This hybrid approach uses operator-level models from Operator_Level as fallback for operators not matching any pattern. Models are referenced from their original location, not copied.

## Shared Infrastructure

**mapping_config.py** - Central configuration shared across all three phases

**Constants:**
- `PATTERNS` - Pattern folder names (e.g., Hash_Join_Seq_Scan_Outer_Hash_Inner)
- `TARGET_TYPES` - Target variables (execution_time, start_time)
- `NON_FEATURE_SUFFIXES` - Metadata column suffixes to exclude
- `LEAF_OPERATORS` - Leaf node types (SeqScan, IndexScan, IndexOnlyScan)
- `REQUIRED_OPERATORS` - Operators required in patterns (Gather, Hash, Hash Join, Nested Loop, Seq Scan)
- `CHILD_FEATURES_TIMING` - Child timing features (st1, rt1, st2, rt2)
- `FFS_SEED` - Random seed for cross-validation (42)
- `FFS_MIN_FEATURES` - Minimum features to select (1)

**Functions:**
- `pattern_to_folder_name()` - Convert pattern string to folder format
- `folder_name_to_pattern()` - Reverse conversion
- `is_leaf_operator()` - Check if operator is leaf node
- `get_target_column_name()` - Get column name from target type

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

### Hybrid_1 vs Hybrid_2 vs Hybrid_3

| Aspekt | Hybrid_1 | Hybrid_2 | Hybrid_3 |
|--------|----------|----------|----------|
| **Depth Check** | `< 0` (Root inkl.) | `< 0` (Root inkl.) | `< 0` (Root inkl.) |
| **Filter Type** | INCLUDE (REQUIRED_OPERATORS) | Keiner | EXCLUDE (PASSTHROUGH_OPERATORS) |
| **MD5 Hash** | Ja | Ja | Nein |
| **Pattern-Anzahl** | ~29 | ~31 | ~20 |

## Workflow Overview

The hybrid pattern-level prediction pipeline consists of three sequential phases:

**Phase 1 → Phase 2 → Phase 3**

1. **Data_Generation**: Analyze operator dataset to identify recurring parent-child patterns → Produces pattern inventory with occurrence counts

2. **Datasets**: Extract pattern instances, aggregate parent+children into single rows, clean features → Produces pattern-specific training datasets

3. **Runtime_Prediction**: Train pattern-level SVM models, perform hybrid bottom-up prediction (pattern models for matched patterns, operator models for fallback) → Produces predictions and evaluation results

**Hybrid Concept:** Instead of predicting each operator individually, this approach groups parent operators with their immediate children into "patterns" (e.g., Hash_Join with Seq_Scan outer and Hash inner). Models are trained on these aggregated units. Operators not matching any pattern use fallback operator-level models from the Operator_Level workflow.

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
```
Baseline_SVM/
├── training.csv, test.csv
├── operators/{Type}/training.csv
└── patterns/{hash}/
    ├── pattern_info.json
    ├── training.csv
    ├── training_aggregated.csv
    └── training_cleaned.csv
```

**See Datasets/DOCS.md for detailed script documentation**

### Phase 3: Runtime_Prediction

**Purpose:** Train pattern-level models and perform hybrid bottom-up prediction

**Input:**
- Pattern training datasets from Phase 2 (patterns/{hash}/training_cleaned.csv)
- Operator-level models from Operator_Level (external dependency)

**Process:**
- Perform forward feature selection for each pattern-target combination
- Train pattern-level SVM models (NuSVR)
- Execute hybrid bottom-up prediction on test queries:
  - For operators matching a pattern → Use pattern model
  - For unmatched operators → Use operator-level model (fallback)
- Evaluate prediction accuracy by node type and template

**Output:**
- SVM/two_step_evaluation_overview.csv (features and MRE per pattern-target)
- Model/{target}/{pattern}/model.pkl (trained SVM models)
- predictions.csv with actual vs predicted times
- Evaluation metrics (overall MRE, template MRE, node type analysis)

**See Runtime_Prediction/DOCS.md for detailed script documentation**
