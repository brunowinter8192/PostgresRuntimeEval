# Data_Generation Module Documentation

## Shared Infrastructure

No external dependencies. All pattern discovery logic is self-contained.

### Configuration Parameters

**Depth Check (Line 44):**
- Hybrid_2: `if parent_depth < 0` - All patterns from depth 0 (root included)
- Hybrid_1: `if parent_depth < 1` - Only patterns from depth 1 (root excluded)

**Operator Filter:**
- Hybrid_2: No filter (all operator combinations)
- Hybrid_1: REQUIRED_OPERATORS filter (only Gather, Hash, Hash Join, Nested Loop, Seq Scan)

**Input Data Selection:**

| Approach | Input File | Templates |
|----------|------------|-----------|
| Baseline | `Operator_Level/Datasets/Baseline/03_training.csv` | Without Q2, Q11, Q16, Q22 (InitPlan/SubPlan) |
| All Templates | `operator_dataset_{ts}.csv` | All 22 TPC-H Templates |

## Workflow Execution Order

```
01_Find_Patterns.py → csv/01_baseline_patterns_depth0plus_{ts}.csv
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
5. Count pattern occurrences per template (no operator filtering)
6. Export pattern matrix with template breakdown

**Inputs:**
- `input_file` (positional): Path to operator dataset CSV

**Outputs:**
- `csv/01_baseline_patterns_depth0plus_{timestamp}.csv`
  - Columns: pattern, leaf_pattern, total, Q1, Q3, Q4, ... (per template)
  - Pattern format: "Parent -> [Child1 (Outer), Child2 (Inner)]"
  - Includes root-level patterns (depth 0) in addition to child patterns

**Usage:**

Baseline Approach (without Q2, Q11, Q16, Q22):
```bash
python 01_Find_Patterns.py ../../Operator_Level/Datasets/Baseline/03_training.csv --output-dir .
```

All Templates Approach (all 22 templates):
```bash
python 01_Find_Patterns.py operator_dataset_20251102_140747.csv --output-dir .
```

**Variables:**
- `--output-dir` (required): Output directory for CSV results
