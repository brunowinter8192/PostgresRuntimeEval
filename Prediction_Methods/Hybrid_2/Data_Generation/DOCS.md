# Data_Generation - Pattern Discovery

Discovers and catalogs all parent-child operator patterns from the training dataset. Patterns are searched starting from depth 0 (root operator), including root-level patterns in addition to all child patterns.

## Directory Structure

```
Data_Generation/
├── 01_Find_Patterns.py                         # Pattern discovery script
├── operator_dataset_{timestamp}.csv            # Input dataset from Operator_Level
└── csv/                                        # [outputs]
    └── baseline_patterns_depth0plus_{ts}.csv   # Pattern inventory with occurrences
```

## Shared Infrastructure

No external dependencies. All pattern discovery logic is self-contained.

## Configuration Parameters

### Input Data Selection

Die entscheidende Stellschraube fuer Baseline vs All Templates:

| Approach | Input Datei | Templates |
|----------|-------------|-----------|
| **Baseline** | `Operator_Level/Datasets/Baseline/04_training.csv` | Ohne Q2, Q11, Q16, Q22 (InitPlan/SubPlan) |
| **All Templates** | `operator_dataset_{ts}.csv` | Alle 22 TPC-H Templates |

### In-Script Configuration (01_Find_Patterns.py)

**Depth Check (Zeile 44):**
```python
if parent_depth < 0:  # Hybrid_2: Alle Patterns ab Depth 0 (Root eingeschlossen)
    continue
# vs Hybrid_1:
if parent_depth < 1:  # Nur Patterns ab Depth 1 (Root ausgeschlossen)
    continue
```

**Operator Filter:**
- Hybrid_2: KEIN Filter (alle Operator-Kombinationen)
- Hybrid_1: REQUIRED_OPERATORS Filter (nur Gather, Hash, Hash Join, Nested Loop, Seq Scan)

### Output Naming

- Hybrid_2: `baseline_patterns_depth0plus_{ts}.csv`
- Hybrid_1: `baseline_patterns_depth1plus_{ts}.csv`

## Workflow Execution Order

```
01 - Find_Patterns
     ↓
Pattern inventory CSV
```

Single script phase. Input dataset must be placed in this directory before execution.

## Script Documentation

### 01 - Find_Patterns.py

**Purpose:** Identify all unique parent-child patterns and count occurrences per template

**Workflow:**
1. Load operator dataset and filter to main plan (exclude SubPlan nodes)
2. Extract template identifier from query filenames
3. Build parent-child relationship map for each query
4. Identify patterns by grouping parent with immediate children (starting from depth 0)
5. Count pattern occurrences per template (keine Operator-Filterung)
6. Export pattern matrix with template breakdown

**Inputs:**
- `input_file` - Path to operator dataset CSV (positional)

**Outputs:**
- `csv/baseline_patterns_depth0plus_{timestamp}.csv`
  - Columns: pattern, leaf_pattern, total, Q1, Q3, Q4, ... (per template)
  - Pattern format: "Parent → [Child1 (Outer), Child2 (Inner)]"
  - Includes root-level patterns (depth 0) in addition to child patterns

**Usage:**

Baseline Approach (ohne Q2, Q11, Q16, Q22):
```bash
python 01_Find_Patterns.py ../../Operator_Level/Datasets/Baseline/04_training.csv --output-dir .
```

All Templates Approach (alle 22 Templates):
```bash
python 01_Find_Patterns.py operator_dataset_20251102_140747.csv --output-dir .
```

**Variables:**
- `--output-dir` - Output directory for CSV results (required)
