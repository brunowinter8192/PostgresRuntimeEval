# Data_Generation - Pattern Discovery

Discovers and catalogs all parent-child operator patterns from the training dataset. Patterns are searched starting from depth 0 (root operator). Pass-through operators including Aggregate are excluded as parents.

## Shared Infrastructure

**mapping_config.py** (parent directory):
- `is_passthrough_operator()`: Pass-through operator detection
- `PASSTHROUGH_OPERATORS`: Extended list including Aggregate

## Workflow Execution Order

```
01 - Find_Patterns
     |
     v
Pattern inventory CSV
```

Single script phase. Input dataset must be referenced via argparse.

## Script Documentation

### 01 - Find_Patterns.py

**Purpose:** Identify all unique parent-child patterns and count occurrences per template

**Workflow:**
1. Load operator dataset and filter to main plan (exclude SubPlan nodes)
2. Extract template identifier from query filenames
3. Build parent-child relationship map for each query
4. Skip pass-through operators as parents (Hash, Sort, Limit, Incremental Sort, Merge Join, Gather Merge, Aggregate)
5. Identify patterns by grouping parent with immediate children (starting from depth 0)
6. Count pattern occurrences per template
7. Export pattern matrix with template breakdown

**Inputs:**
- `input_file` - Path to operator dataset CSV (positional)

**Outputs:**
- `csv/baseline_patterns_depth0plus_{timestamp}.csv`
  - Columns: pattern, leaf_pattern, total, Q1, Q3, Q4, ... (per template)
  - Pattern format: "Parent -> [Child1 (Outer), Child2 (Inner)]"
  - Includes root-level patterns (depth 0)
  - 9 patterns (extended PT exclusion including Aggregate)

**Usage:**

Baseline Approach (ohne Q2, Q11, Q16, Q22):
```bash
python 01_Find_Patterns.py ../../Operator_Level/Datasets/Baseline/03_training.csv --output-dir .
```

**Variables:**
- `--output-dir` - Output directory for CSV results (required)
