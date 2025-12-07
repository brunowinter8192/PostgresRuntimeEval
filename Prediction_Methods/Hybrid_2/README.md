# Hybrid Pattern-Level Runtime Prediction

ML-based runtime prediction for SQL queries using pattern-level SVM models that group parent operators with their children as single prediction units.

## Directory Structure

```
Hybrid_2/
├── mapping_config.py                        # Shared patterns, targets, and constants
├── README.md                                # Workflow documentation (THIS FILE)
├── Data_Generation/                         [See DOCS.md]
├── Datasets/                                [See DOCS.md]
└── Runtime_Prediction/                      [See DOCS.md]

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
- `TARGET_TYPES` - Target variables (execution_time, start_time)
- `NON_FEATURE_SUFFIXES` - Metadata column suffixes to exclude
- `LEAF_OPERATORS` - Leaf node types (SeqScan, IndexScan, IndexOnlyScan)
- `CHILD_ACTUAL_SUFFIXES` - Child actual time columns to remove
- `CHILD_TIMING_SUFFIXES` - Child st/rt columns for leaf operators
- `PARENT_CHILD_FEATURES` - Parent child timing feature column names
- `FFS_SEED` - Random seed for cross-validation (42)
- `FFS_MIN_FEATURES` - Minimum features to select (1)

**Functions:**
- `pattern_to_folder_name()` - Convert pattern string to folder format
- `folder_name_to_pattern()` - Reverse conversion
- `is_leaf_operator()` - Check if operator is leaf node

**Pattern Identification:** Patterns are identified by MD5 hash of their structure. Each pattern folder contains `pattern_info.json` with metadata (pattern_hash, pattern_string, folder_name, leaf_pattern, occurrence_count).

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

### Hybrid_2 vs Hybrid_1

| Aspekt | Hybrid_1 | Hybrid_2 |
|--------|----------|----------|
| **Depth Check** | `if parent_depth < 1:` (Root ausgeschlossen) | `if parent_depth < 0:` (Root eingeschlossen) |
| **Operator Filter** | REQUIRED_OPERATORS aktiv | Kein Filter (alle Operator-Typen) |
| **Root Patterns** | Nein | Ja (z.B. Sort_Aggregate_Outer) |
| **Pattern-Anzahl** | ~21 (gefiltert) | ~39 (ungefiltert) |

## Workflow Overview

The hybrid pattern-level prediction pipeline consists of three sequential phases:

**Phase 1 → Phase 2 → Phase 3**

1. **Data_Generation**: Analyze operator dataset to identify recurring parent-child patterns → Produces pattern inventory with occurrence counts

2. **Datasets**: Extract pattern instances, aggregate parent+children into single rows, clean features → Produces pattern-specific training datasets

3. **Runtime_Prediction**: Train pattern-level SVM models, perform hybrid bottom-up prediction (pattern models for matched patterns, operator models for fallback) → Produces predictions and evaluation results

**Hybrid Concept:** Instead of predicting each operator individually, this approach groups parent operators with their immediate children into "patterns" (e.g., Hash_Join with Seq_Scan outer and Hash inner). Models are trained on these aggregated units. Operators not matching any pattern use fallback operator-level models from the Operator_Level workflow.

## Phase Documentation

### Phase 1: Data_Generation

**Purpose:** Discover and catalog all parent-child patterns in the training data

**Input:** Baseline or All Templates dataset (see Data Configuration section)

**Process:**
- Identify all unique parent-child combinations (parent + outer child + inner child)
- Starting from depth 0 (includes root-level patterns unlike Hybrid_1)
- Count pattern occurrences across all queries
- Compute MD5 hash for each pattern structure
- No operator type filtering (all operator combinations considered)

**Output:** Pattern inventory CSV with pattern_hash, pattern names, and occurrence counts

**See Data_Generation/DOCS.md for detailed script documentation**

### Phase 2: Datasets

**Purpose:** Split data and prepare operator-level and pattern-level training datasets

**Input:** operator_dataset.csv from Data_Generation

**Process:**
- Template-stratified train/test split (120/30 per template, seed=42)
- Extract operators into type-specific folders
- Extract pattern instances into hash-named folders with pattern_info.json
- Aggregate parent and child rows into single feature vectors
- Clean features by removing unavailable columns (child actual times unknown at prediction)

**Output Structure:**
```
Baseline_SVM/
├── training.csv / test.csv
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
