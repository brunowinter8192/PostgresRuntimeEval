# Data_Generation - Pattern Discovery

Discovers and catalogs all parent-child operator patterns from the baseline training dataset (excludes templates Q2, Q11, Q16, Q22 with InitPlan/SubPlan operators).

## Directory Structure

```
Data_Generation/
├── 01_Find_Patterns.py                         # Pattern discovery script
└── csv/                                        # [outputs]
    └── baseline_patterns_depth1plus_{ts}.csv   # Pattern inventory with occurrences
```

**Input data (external):** `Operator_Level/Datasets/Baseline/04_training.csv`

## Shared Infrastructure

**Constants from mapping_config.py:**
- `REQUIRED_OPERATORS` - Operators that must appear in patterns (Gather, Hash, Hash Join, Nested Loop, Seq Scan)

## Configuration Parameters

### Input Data Selection

Die entscheidende Stellschraube fuer Baseline vs All Templates:

| Approach | Input Datei | Templates |
|----------|-------------|-----------|
| **Baseline** | `Operator_Level/Datasets/Baseline/04_training.csv` | Ohne Q2, Q11, Q16, Q22 (InitPlan/SubPlan) |
| **All Templates** | `operator_dataset_{ts}.csv` | Alle 22 TPC-H Templates |

### In-Script Configuration (01_Find_Patterns.py)

**Depth Check (Zeile 46):**
```python
if parent_depth < 1:  # Hybrid_1: Nur Patterns ab Depth 1 (Root ausgeschlossen)
    continue
# vs Hybrid_2:
if parent_depth < 0:  # Alle Patterns ab Depth 0 (Root eingeschlossen)
    continue
```

**Operator Filter (Zeile 54-56):**
```python
pattern_operators = {parent_type} | {child['node_type'] for child in children}
if not pattern_operators.intersection(REQUIRED_OPERATORS):
    continue
# REQUIRED_OPERATORS = {'Gather', 'Hash', 'Hash Join', 'Nested Loop', 'Seq Scan'}
# Hybrid_2 hat diesen Filter NICHT
```

### Output Naming

- Hybrid_1: `baseline_patterns_depth1plus_{ts}.csv`
- Hybrid_2: `baseline_patterns_depth0plus_{ts}.csv`

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
1. Load baseline operator dataset and filter to main plan (exclude SubPlan nodes)
2. Extract template identifier from query filenames
3. Build parent-child relationship map for each query
4. Identify patterns by grouping parent with immediate children (starting from depth 1)
5. Filter patterns to include only those with required operators
6. Count pattern occurrences per template
7. Export pattern matrix with template breakdown

**Inputs:**
- `input_file` - Path to baseline training CSV (positional)

**Outputs:**
- `csv/baseline_patterns_depth1plus_{timestamp}.csv`
  - Columns: pattern, leaf_pattern, total, Q1, Q3, Q4, ... (per template)
  - Pattern format: "Parent → [Child1 (Outer), Child2 (Inner)]"
  - Templates Q2, Q11, Q16, Q22 not present (excluded from baseline data)

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
