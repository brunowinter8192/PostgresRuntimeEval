# Hybrid_5: Unrestricted Pattern Length with Occurrence Filtering

ML-based runtime prediction using patterns of arbitrary length with occurrence threshold. Removes length restrictions from pattern discovery, allowing patterns of 2-15 levels with minimum 120 occurrences. Focuses on accuracy improvement through complex pattern structures.

## Directory Structure

```
Hybrid_5/
├── mapping_config.py                    # Shared patterns, targets, features, operator counts
├── README.md                            # Workflow documentation (THIS FILE)
├── Data_Generation/                     [See DOCS.md]
│   ├── 01_Find_Patterns.py
│   ├── 02a_Extract_Pattern_Leafs.py
│   ├── 02b_Identify_Pattern_Plan_Leafs.py
│   ├── 03_Generate_Mapping.py
│   └── csv/
├── Datasets/                            [See DOCS.md]
│   ├── 01_Extract_Patterns.py
│   ├── 02_Aggregate_Patterns.py
│   ├── 03_Clean_Aggregated.py
│   ├── A_01a-i (Analysis scripts)
│   └── Baseline/<pattern_hash>/
└── Runtime_Prediction/                  [See DOCS.md]
    ├── ffs_config.py
    ├── 01_Clean_FFS.py
    ├── 02_Feature_Selection.py
    ├── 03_Train_Models.py
    ├── 04_Predict_Queries.py
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
- `PATTERNS` - **72 pattern hash IDs** (occurrence > 120, lengths 2-15)
- `PATTERN_OPERATOR_COUNT` - Dict mapping pattern hash to operator count
- `PATTERN_LEAF_TIMING_FEATURES` - Dict mapping pattern hash to leaf timing features
- `TARGET_TYPES` - Target variables (execution_time, start_time)
- `TARGET_NAME_MAP` - Target type to column name mapping
- `NON_FEATURE_SUFFIXES` - Metadata column suffixes to exclude
- `FFS_SEED` - Random seed for cross-validation (42)
- `FFS_MIN_FEATURES` - Minimum features to select (1)

**Used by:** All scripts across Data_Generation, Datasets, and Runtime_Prediction phases

## Data Configuration

### Baseline Approach

**Definition:** Training/Test-Daten ohne Templates Q2, Q11, Q16, Q22

**Warum entfernt:** Diese Templates enthalten InitPlan/SubPlan Operatoren, die:
- Nicht-standard Parent-Child Beziehungen erzeugen
- Operator-Level Predictions stark verzerren
- Pattern-Matching komplizieren (verschachtelte Subqueries)

**Dateien:** `Operator_Level/Datasets/Baseline/04_training.csv` und `04_test.csv`

### Hybrid Evolution: 1 → 2 → 3 → 4 → 5

| Aspekt | Hybrid_1 | Hybrid_2 | Hybrid_3 | Hybrid_4 | Hybrid_5 |
|--------|----------|----------|----------|----------|----------|
| **Depth Check** | `< 1` (ohne Root) | `< 0` (mit Root) | `< 0` (mit Root) | `< 0` (mit Root) | `< 0` (mit Root) |
| **Operator Filter** | REQUIRED_OPERATORS | Kein Filter | PT Filter (≥99%) | PT Filter (≥95%) | **Kein Filter** |
| **PT Threshold** | N/A | N/A | 0.99 | 0.95 | **N/A** |
| **PT Operators** | N/A | Als Parents | 5 excluded | 7 excluded | **Keine** |
| **Pattern Length** | 2 | 2 | 2 | 2 | **2-15** |
| **Pattern Filter** | N/A | N/A | N/A | N/A | **> 120 occurrences** |
| **Pattern Count** | 21 | 31 | 20 | 20 | **72** |
| **Model Count** | 42 (21×2) | 62 (31×2) | 40 (20×2) | 40 (20×2) | **144 (72×2)** |
| **Prediction Types** | 2 (pattern, operator) | 2 (pattern, operator) | 3 (pattern, operator, passthrough) | 3 (pattern, operator, passthrough) | **2 (pattern, operator)** |
| **Key Innovation** | Patterns mit Root | Alle Operators | PT Inheritance | Extended PT | **Unrestricted Length** |

## Pattern Concept

**Definition:** Patterns are recurring structural combinations of operators (parent + children) extracted from query execution plans.

**Hybrid_5 Pattern Discovery:**
- **Length:** Unrestricted (2-15 levels deep)
- **Filter:** Occurrence count > 120 across training dataset
- **Result:** 72 patterns of varying complexity
- **No Pass-Through filtering:** All operator types can be pattern roots

**Pattern Length Concept:**
- Length 2: Parent + 1 level of children
- Length 3: Parent + children + grandchildren
- Length 15: Deepest pattern (15 levels of hierarchy)

**Examples:**
- Simple (Length 2): `Hash Join → [Seq Scan (Outer), Hash (Inner)]`
- Complex (Length 9): Multi-level nested joins with multiple operators
- Complex (Length 15): Deepest discovered pattern structure

**Pattern Distribution:**
- Lengths 2-4: Most common (simple structures)
- Lengths 5-9: Medium complexity
- Lengths 10-15: Rare but captured (complex nested structures)

## Pattern Plan Leaf Concept

**Critical Distinction:**
- **Pattern Leaf:** Deepest operator within pattern structure (no children in pattern)
- **Plan Leaf:** Operator with no children in entire query plan
- **Pattern+Plan Leaf:** Operator that is both

**Issue:** Pattern+Plan Leafs have no children, so their child timing features (st1, rt1, st2, rt2) are always zero.

**Solution:**
1. `Data_Generation/02b_Identify_Pattern_Plan_Leafs.py` identifies which pattern leafs are plan leafs
2. `Runtime_Prediction/01_Clean_FFS.py` removes child features for Pattern+Plan Leafs before training

**Example:**
Pattern `895c6e8c1a30a094329d71cef3111fbd` (Hash Join → [Seq Scan, Hash]):
- `SeqScan_Outer` is Plan Leaf → Child features removed
- `Hash_Inner` has children → Keep child features

## Workflow Overview

**Phase 1 → Phase 2 → Phase 3**

1. **Data_Generation**: Discover patterns (length 2-15, occurrence > 120) → 72 patterns

2. **Datasets**: Extract pattern instances → 72 pattern folders with aggregated features

3. **Runtime_Prediction**: Train 144 models (72×2), predict with 2-level fallback → pattern or operator

**Hybrid Concept:** Groups parent+children into patterns (e.g., Hash_Join → Seq_Scan + Hash). Bottom-up prediction with 2 fallback levels:
1. Pattern match → pattern model
2. No match → operator model

**Hybrid_5 Hypothesis:** Removing length restrictions and allowing complex patterns (2-15 levels) with occurrence filtering (> 120) improves prediction accuracy by capturing more structural context.

## Phase Documentation

### Phase 1: Data_Generation

**Purpose:** Discover and catalog all parent-child patterns in the training data

**Input:** Baseline dataset (without Q2, Q11, Q16, Q22)

**Process:**
- Identify all unique parent-child combinations of arbitrary length (2-15)
- Starting from depth 0 (includes root-level patterns)
- Count pattern occurrences across all queries
- Filter by occurrence threshold (> 120)
- No operator type filtering (all operator combinations considered)

**Output:**
- Pattern inventory CSV with pattern names and occurrence counts
- Pattern leaf extraction (leaf nodes per pattern)
- Pattern plan leaf mapping (pattern leafs that are also plan leafs)
- PATTERN_LEAF_TIMING_FEATURES mapping for mapping_config.py

**See Data_Generation/DOCS.md for detailed script documentation**

### Phase 2: Datasets

**Purpose:** Extract pattern instances and prepare pattern-specific training datasets

**Input:** operator_dataset.csv and pattern inventory from Phase 1

**Process:**
- Extract all instances of each pattern into separate folders (72 patterns)
- Verify extraction completeness and correctness
- Aggregate parent and child rows into single feature vectors (parent features + child features)
- Verify aggregation consistency
- Clean features by removing non-leaf timing features (prevent data leakage)

**Output:** Pattern-specific folders containing:
- training.csv - Raw pattern instances
- training_aggregated.csv - Parent+children combined
- training_cleaned.csv - Production-ready features (only leaf timing features)

**See Datasets/DOCS.md for detailed script documentation**

### Phase 3: Runtime_Prediction

**Purpose:** Train pattern-level models and perform hybrid bottom-up prediction

**Input:**
- Pattern training datasets from Phase 2
- Operator-level models from Operator_Level (external dependency)

**Process:**
- Clean FFS by removing Pattern+Plan Leaf child features
- Perform forward feature selection for each pattern-target combination
- Train pattern-level SVM models (NuSVR)
- Execute hybrid bottom-up prediction on test queries:
  - For operators matching a pattern → Use pattern model
  - For unmatched operators → Use operator-level model (fallback)
- Evaluate prediction accuracy by node type and template

**Output:**
- SVM/two_step_evaluation_overview.csv (features and MRE per pattern-target)
- Model/{target}/{pattern}/model.pkl (trained SVM models, 144 total)
- predictions.csv with actual vs predicted times
- Evaluation metrics (overall MRE, template MRE, node type analysis)

**See Runtime_Prediction/DOCS.md for detailed script documentation**
