# Data_Generation - Pattern Discovery

Discovers and catalogs all parent-child operator patterns from the operator dataset with MD5 hash identification. Supports multi-length patterns and optional filtering.

## Directory Structure

```
Data_Generation/
├── 01_Find_Patterns.py                   # Pattern discovery (all lengths)
├── 02_Passthrough_Analysis.py            # Operator passthrough ratio analysis
└── csv/                                  # [outputs]
    ├── 01_patterns_{ts}.csv              # Pattern inventory with occurrences
    └── 02_passthrough_analysis_{ts}.csv  # Operator passthrough ratios
```

**Input data (external):** `Operator_Level/Datasets/Baseline/01_operator_dataset_cleaned.csv`

## Shared Infrastructure

**Constants from mapping_config.py:**
- `REQUIRED_OPERATORS` - Operators for INCLUDE filter (Gather, Hash, Hash Join, Nested Loop, Seq Scan)
- `PASSTHROUGH_OPERATORS` - Operators for EXCLUDE filter (Incremental Sort, Gather Merge, Gather, Sort, Limit, Merge Join)

## Workflow Execution Order

```
01 - Find_Patterns         [operator_dataset.csv -> pattern inventory CSV]

02 - Passthrough_Analysis  [operator_dataset.csv -> passthrough ratios CSV]
```

Scripts are independent. 02 is optional analysis for determining passthrough operators.

## Script Documentation

### 01 - Find_Patterns.py

**Purpose:** Discover all unique patterns at all lengths (2 to max_depth+1), compute MD5 hashes, count occurrences

**Workflow:**
1. Load operator dataset and filter to main plan (exclude SubPlan nodes)
2. Build tree structure for each query
3. For each node, iterate through all possible pattern lengths
4. Compute MD5 hash for each pattern at each length
5. Count pattern occurrences across all queries
6. Export pattern inventory sorted by size

**Inputs:**
- `input_file` - Path to operator dataset CSV (positional)

**Outputs:**
- `csv/01_patterns_{timestamp}.csv`
  - Columns: pattern_hash, pattern_string, pattern_length, operator_count, occurrence_count, example_query_file
  - pattern_length: Number of depth levels (see README Terminology)
  - operator_count: Total nodes in pattern (Size)

**Usage:**
```bash
python 01_Find_Patterns.py operator_dataset.csv --output-dir .
```

**Variables:**
- `--output-dir` - Output directory for CSV results (required)

---

### 02 - Passthrough_Analysis.py

**Purpose:** Analyze which operators have execution time approximately equal to their children (passthrough behavior)

**Workflow:**
1. Load operator dataset
2. Build parent-child map for each query
3. For each parent with children: compute ratio = parent_time / max(children_time)
4. Group by operator type, calculate mean ratio
5. Export sorted by ratio (lowest = most passthrough)

**Inputs:**
- `input_file` - Path to operator dataset CSV (positional)

**Outputs:**
- `csv/02_passthrough_analysis_{timestamp}.csv`
  - Columns: node_type, instance_count, mean_parent_time, mean_max_child_time, ratio_pct
  - ratio_pct ~100% indicates passthrough behavior

**Usage:**
```bash
python 02_Passthrough_Analysis.py operator_dataset.csv --output-dir .
```

**Variables:**
- `--output-dir` - Output directory for CSV results (required)
