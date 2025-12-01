# Hybrid_3: Pass-Through Pattern-Level Runtime Prediction

ML-based runtime prediction with pass-through operator inheritance. Reduces model count from 62 to 40 by excluding Hash, Sort, Limit, Incremental Sort, and Merge Join as pattern parents. These pass-through operators inherit predictions from their children without model training.

## Directory Structure

```
Hybrid_3/
├── mapping_config.py                    # Shared patterns, targets, PT operators
├── Data_Generation/                     [See DOCS.md]
│   ├── 01_Find_Patterns.py
│   └── A_01a_Compare_Patterns.py
├── Datasets/                            [See DOCS.md]
│   ├── 01_Extract_Patterns.py
│   ├── 02_Aggregate_Patterns.py
│   ├── 03_Clean_Patterns.py
│   ├── A_01a_Verify_Extraction.py
│   └── A_01b_Verify_Aggregation.py
└── Runtime_Prediction/                  [See DOCS.md]
    ├── ffs_config.py
    ├── 01_Feature_Selection.py
    ├── 02_Train_Models.py
    ├── 03_Predict_Queries.py            # Includes PT inheritance logic
    ├── A_01a_Evaluate_Predictions.py
    ├── A_01b_Node_Evaluation.py         # Includes PT evaluation
    └── A_01c_Time_Analysis.py
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
- `PATTERNS` - **20 pattern folder names** (PT parent patterns excluded)
- `TARGET_TYPES` - Target variables (execution_time, start_time)
- `NON_FEATURE_SUFFIXES` - Metadata column suffixes to exclude
- `LEAF_OPERATORS` - Leaf node types (SeqScan, IndexScan, IndexOnlyScan)
- `PASSTHROUGH_OPERATORS` - **PT operators** (Incremental Sort, Merge Join, Limit, Sort, Hash)
- `FFS_SEED` - Random seed for cross-validation (42)
- `FFS_MIN_FEATURES` - Minimum features to select (1)

**Functions:**
- `pattern_to_folder_name()` - Convert pattern string to folder format
- `folder_name_to_pattern()` - Reverse conversion
- `is_leaf_operator()` - Check if operator is leaf node
- `is_passthrough_operator()` - **Check if operator is pass-through**
- `get_target_column_name()` - Get column name from target type

**Used by:** All scripts across Data_Generation, Datasets, and Runtime_Prediction phases

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

### Hybrid Evolution: 1 → 2 → 3

| Aspekt | Hybrid_1 | Hybrid_2 | Hybrid_3 |
|--------|----------|----------|----------|
| **Depth Check** | `< 1` (ohne Root) | `< 0` (mit Root) | `< 0` (mit Root) |
| **Operator Filter** | REQUIRED_OPERATORS | Kein Filter | **Pass-Through Filter** |
| **PT Operators** | N/A | Als Parents | **Excluded als Parents** |
| **Pattern Count** | 21 | 31 | **20** |
| **Model Count** | 42 (21×2) | 62 (31×2) | **40 (20×2)** |
| **Prediction Types** | 2 (pattern, operator) | 2 (pattern, operator) | **3 (pattern, operator, passthrough)** |
| **Key Innovation** | Patterns mit Root | Alle Operators | **PT Inheritance** |

## Pass-Through Concept

**Definition:** Pass-through operators (startup_total_ratio ≥ 0.99) have minimal processing overhead. Execution time is dominated by child operators.

**PT Operators:** Hash, Sort, Limit, Incremental Sort, Merge Join

**Strategy:**
- **Excluded as pattern parents** → Reduces patterns from 31 to 20
- **Inherit child predictions** → No model training/inference needed
- **prediction_type = 'passthrough'** → Identified in evaluation

**Example Chain:**
```
Limit (depth 0) → passthrough → inherits from Sort
  ↓
Sort (depth 1) → passthrough → inherits from Aggregate
  ↓
Aggregate (depth 2) → pattern prediction → actual model call
```

Result: Limit and Sort predictions = Aggregate prediction (perfect inheritance, no approximation error)

## Workflow Overview

**Phase 1 → Phase 2 → Phase 3**

1. **Data_Generation**: Discover patterns, skip PT parents → 20 patterns (vs 31 in Hybrid_2)

2. **Datasets**: Extract pattern instances, skip PT parents → 20 pattern folders

3. **Runtime_Prediction**: Train 40 models (20×2), predict with PT inheritance → 3 prediction types

**Hybrid Concept:** Groups parent+children into patterns (e.g., Hash_Join → Seq_Scan + Hash). Bottom-up prediction with 3 fallback levels:
1. Pattern match → pattern model
2. No match → operator model
3. PT operator → inherit from child (no model)

## Phase Documentation

### Phase 1: Data_Generation

**Purpose:** Discover and catalog all parent-child patterns in the training data

**Input:** Baseline or All Templates dataset (see Data Configuration section)

**Process:**
- Identify all unique parent-child combinations (parent + outer child + inner child)
- Starting from depth 0 (includes root-level patterns unlike Hybrid_1)
- Count pattern occurrences across all queries
- No operator type filtering (all operator combinations considered)

**Output:** Pattern inventory CSV with pattern names and occurrence counts

**See Data_Generation/DOCS.md for detailed script documentation**

### Phase 2: Datasets

**Purpose:** Extract pattern instances and prepare pattern-specific training datasets

**Input:** operator_dataset.csv and pattern inventory from Phase 1

**Process:**
- Extract all instances of each pattern into separate folders
- Verify extraction completeness and correctness
- Aggregate parent and child rows into single feature vectors (parent features + child features)
- Verify aggregation consistency
- Clean features by removing unavailable columns (child actual times unknown at prediction)

**Output:** Pattern-specific folders containing:
- training.csv - Raw pattern instances
- training_aggregated.csv - Parent+children combined
- training_cleaned.csv - Production-ready features

**See Datasets/DOCS.md for detailed script documentation**

### Phase 3: Runtime_Prediction

**Purpose:** Train pattern-level models and perform hybrid bottom-up prediction

**Input:**
- Pattern training datasets from Phase 2
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
