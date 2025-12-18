# Data_Generation - Pattern Discovery

Discovers and catalogs all parent-child operator patterns from the operator dataset with MD5 hash identification. Extracts all patterns without filtering - filtering happens in Phase 2 (Datasets).

## Directory Structure

```
Data_Generation/
├── 01_Find_Patterns.py                   # Pattern discovery (all lengths)
└── csv/                                  # [outputs]
    └── 01_patterns_{ts}.csv              # Pattern inventory with occurrences
```

**Input data (external):** `Operator_Level/Datasets/Baseline/03_training.csv`

## Workflow Execution Order

```
01 - Find_Patterns         [operator_dataset.csv -> pattern inventory CSV]
```

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

