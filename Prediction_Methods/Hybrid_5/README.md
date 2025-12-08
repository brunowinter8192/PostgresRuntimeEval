# Hybrid_5: Depth-1 Patterns with Passthrough Filtering

ML-based runtime prediction using depth-1 patterns (Parent + Children) with passthrough operator filtering. Follows the same architecture as Hybrid_3 with hash-based pattern organization.

## Directory Structure

```
Hybrid_5/
├── mapping_config.py                    # Shared patterns, targets, features, helper functions
├── README.md                            # Workflow documentation (THIS FILE)
├── Data_Generation/                     [See DOCS.md]
│   ├── 01_Find_Patterns.py
│   └── csv/
├── Datasets/                            [See DOCS.md]
│   ├── 01_Split_Train_Test.py
│   ├── 02_Extract_Operators.py
│   ├── 03_Extract_Patterns.py
│   ├── 04_Aggregate_Patterns.py
│   ├── 05_Clean_Patterns.py
│   ├── A_01a_Verify_Extraction.py
│   ├── A_01b_Verify_Aggregation.py
│   └── patterns/<hash>/
└── Runtime_Prediction/                  [See DOCS.md]
    ├── ffs_config.py
    ├── 01_Feature_Selection.py
    ├── 02_Train_Models.py
    ├── 03_Predict_Queries.py
    ├── A_01a_Evaluate_Predictions.py
    ├── A_01b_Node_Evaluation.py
    ├── A_01c_Time_Analysis.py
    └── Baseline_SVM/
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
- `PATTERNS` - List of pattern folder names (e.g., `Aggregate_Hash_Join_Outer`)
- `TARGET_TYPES` - Target variables (execution_time, start_time)
- `NON_FEATURE_SUFFIXES` - Metadata column suffixes to exclude
- `LEAF_OPERATORS` - Operators that are typically plan leafs
- `PASSTHROUGH_OPERATORS` - Operators excluded from pattern roots
- `CHILD_ACTUAL_SUFFIXES` - Child actual timing columns to remove
- `CHILD_TIMING_SUFFIXES` - Child predicted timing suffixes
- `FFS_SEED` - Random seed for cross-validation (42)
- `FFS_MIN_FEATURES` - Minimum features to select (1)

**Functions:**
- `is_passthrough_operator()` - Check if operator is pass-through
- `pattern_to_folder_name()` - Convert pattern string to folder name
- `build_pattern_hash_map()` - Build pattern name to hash mapping from pattern_info.json

**Used by:** All scripts across Data_Generation, Datasets, and Runtime_Prediction phases

## Data Configuration

### Baseline Approach

**Definition:** Training/Test-Daten ohne Templates Q2, Q11, Q16, Q22

**Warum entfernt:** Diese Templates enthalten InitPlan/SubPlan Operatoren, die:
- Nicht-standard Parent-Child Beziehungen erzeugen
- Operator-Level Predictions stark verzerren
- Pattern-Matching komplizieren (verschachtelte Subqueries)

**Dateien:** `Operator_Level/Datasets/Baseline/04_training.csv` und `04_test.csv`

## Pattern Concept

**Definition:** Patterns are recurring structural combinations of operators (parent + direct children) extracted from query execution plans.

**Depth-1 Patterns:**
- Parent operator + immediate children only
- No multi-level nesting within pattern
- Children sorted by parent_relationship (Outer first, then Inner)

**Passthrough Filtering:**
Passthrough operators are excluded from pattern roots:
- Incremental Sort, Merge Join, Limit, Sort, Hash

**Hash-Based Organization:**
- Each pattern stored in `patterns/<md5_hash>/` directory
- `pattern_info.json` contains folder_name and metadata
- `build_pattern_hash_map()` maps folder names to hashes

**Example Patterns:**
- `Aggregate_Hash_Join_Outer` - Aggregate with Hash Join child
- `Hash_Join_Seq_Scan_Outer_Hash_Inner` - Hash Join with Seq Scan and Hash children

## Workflow Overview

**Phase 1 -> Phase 2 -> Phase 3**

1. **Data_Generation**: Discover depth-1 patterns with passthrough filtering

2. **Datasets**: Split train/test, extract patterns into hash-based folders

3. **Runtime_Prediction**: Train pattern models, predict with bottom-up fallback

**Hybrid Concept:** Groups parent+children into patterns. Bottom-up prediction with 3 fallback levels:
1. Pattern match -> pattern model
2. Passthrough operator -> inherit child prediction
3. No match -> operator model

## Phase Documentation

### Phase 1: Data_Generation

**Purpose:** Discover and catalog all depth-1 parent-children patterns in the training data

**Input:** Operator_Level training dataset

**Process:**
- Identify all unique parent-children combinations (depth-1 only)
- Filter out passthrough operators as pattern roots
- Compute MD5 hash for each pattern structure
- Count pattern occurrences per template

**Output:**
- `csv/01_baseline_patterns_depth0plus_{timestamp}.csv`

**See Data_Generation/DOCS.md for detailed script documentation**

### Phase 2: Datasets

**Purpose:** Split data and extract pattern instances into hash-organized folders

**Input:** Operator_Level dataset and pattern discovery from Phase 1

**Process:**
1. Split train/test with template stratification (120/30 per template)
2. Extract operators by node_type
3. Extract pattern instances into `patterns/<hash>/` folders with pattern_info.json
4. Aggregate parent+children rows into single feature vectors
5. Clean features (remove child actuals, leaf timing)

**Output:** Pattern-specific folders containing:
- `training.csv` - Raw pattern instances
- `training_aggregated.csv` - Parent+children combined
- `training_cleaned.csv` - Production-ready features
- `pattern_info.json` - Pattern metadata

**See Datasets/DOCS.md for detailed script documentation**

### Phase 3: Runtime_Prediction

**Purpose:** Train pattern-level models and perform hybrid bottom-up prediction

**Input:**
- Pattern training datasets from Phase 2
- Operator-level models from Operator_Level (external dependency)

**Process:**
- Perform forward feature selection using `build_pattern_hash_map()`
- Train pattern-level SVM models (NuSVR)
- Execute hybrid bottom-up prediction:
  - Pattern match -> pattern model
  - Passthrough -> inherit child prediction
  - No match -> operator model

**Output:**
- `SVM/two_step_evaluation_overview.csv`
- `Model/{target}/{pattern}/model.pkl`
- `predictions.csv`

**See Runtime_Prediction/DOCS.md for detailed script documentation**
