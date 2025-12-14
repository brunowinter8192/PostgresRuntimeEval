# Data_Generation - DOCS.md

## Directory Structure

```
Data_Generation/
├── DOCS.md
├── 01_Find_Patterns.py
├── Training_Full/
│   └── csv/
│       └── 01_patterns_*.csv
└── Training_Training/
    └── csv/
        └── 01_patterns_*.csv
```

## Shared Infrastructure

No shared config files. Single standalone script for pattern mining.

## Workflow Execution Order

```
01_Find_Patterns.py (Training.csv) -> Training_Full/csv/01_patterns_*.csv
01_Find_Patterns.py (Training_Training.csv) -> Training_Training/csv/01_patterns_*.csv
```

Run once per dataset variant. Output is used by Dataset/02b_Extract_Patterns.py.

**Important:** Must run BEFORE Dataset/02b_Extract_Patterns.py.

---

## Script Documentation

### 01_Find_Patterns.py

**Purpose:** Mine structural patterns from query execution plans.

**Workflow:**
1. Load operator dataset and filter to main plan (exclude subplans)
2. Scan maximum tree depth across all queries
3. For each query: build tree structure from flat DataFrame
4. For each node: compute pattern hashes at lengths 2 to max_depth
5. Aggregate patterns by hash: count occurrences, track example query
6. Sort by operator_count ASC, occurrence_count DESC
7. Export all patterns (no threshold filtering)

**Pattern Definition:**
- Structural hash based on node_type + child relationships
- Pattern length = tree depth from root to deepest included node
- Pattern string = human-readable representation (e.g., "Hash -> Seq Scan (Outer)")

**Inputs:**
- `input_file`: Path to operator dataset CSV (Training_Training.csv or Training.csv from Dataset/Baseline/)

**Outputs:**
- `{output-dir}/csv/01_patterns.csv`
  - Columns: pattern_hash;pattern_string;pattern_length;operator_count;occurrence_count;example_query_file

**Usage:**
```
cd Data_Generation/

# For Training_Full (120 queries/template - full training set)
python3 01_Find_Patterns.py ../Dataset/Baseline/Training.csv --output-dir Training_Full

# For Training_Training (96 queries/template - validation subset)
python3 01_Find_Patterns.py ../Dataset/Baseline/Training_Training.csv --output-dir Training_Training
```

**Output Structure:**
```
Data_Generation/
├── Training_Full/
│   └── csv/
│       └── 01_patterns.csv
└── Training_Training/
    └── csv/
        └── 01_patterns.csv
```

**Note:** Pattern occurrence counts are dataset-specific. Use matching patterns CSV for Dataset extraction:
- Training_Full patterns for Patterns/Training_Full
- Training_Training patterns for Patterns/Training_Training

### load_and_filter_data()
Load training data and filter to main plan (exclude subplans).

### scan_max_depth()
Find maximum depth in dataset.

### mine_patterns_iteratively()
Mine patterns iteratively from length 2 to max_depth.

### build_tree_from_dataframe()
Build tree structure from flat DataFrame.

### extract_all_nodes()
Extract all nodes from tree recursively.

### has_children_at_length()
Check if node has children at target pattern length.

### count_operators_at_length()
Count total operators in pattern at specific length.

### compute_pattern_hash_at_length()
Compute structural hash for pattern at specific length.

### generate_pattern_string_at_length()
Generate readable pattern string at specific length.

### collect_all_patterns()
Collect all patterns without threshold filtering.

### sort_by_size()
Sort patterns by size (operator_count ASC), then by occurrence (DESC).

### export_results()
Save patterns to CSV with timestamp.
