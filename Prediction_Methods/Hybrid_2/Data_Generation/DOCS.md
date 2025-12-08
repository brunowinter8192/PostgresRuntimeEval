# Data_Generation - DOCS.md

## Shared Infrastructure

No shared config files. Single standalone script for pattern mining.

## Workflow Execution Order

```
01_Find_Patterns.py
```

Single script module. Run once per dataset variant (Training_Training, Training_Full).

---

## Script Documentation

### 01 - Find_Patterns.py

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
- `input_file`: Path to operator dataset CSV (e.g., Training_Training.csv, Training.csv)

**Outputs:**
- `{output-dir}/csv/01_patterns_{timestamp}.csv`
  - Columns: pattern_hash;pattern_string;pattern_length;operator_count;occurrence_count;example_query_file

**Usage:**
```
# For Training_Training (validation)
python3 01_Find_Patterns.py ../Dataset/Baseline/Training_Training.csv --output-dir csv

# For Training (full, final models)
python3 01_Find_Patterns.py ../Dataset/Baseline/Training.csv --output-dir Training_Full
```

**Output Structure:**
```
Data_Generation/
    csv/                          # Training_Training patterns
        01_patterns_*.csv
    Training_Full/                # Training (full) patterns
        csv/
            01_patterns_*.csv
```

**Note:** Pattern occurrence counts are dataset-specific. Use matching patterns CSV for Dataset extraction and verification (e.g., Training_Full patterns for Training_Full dataset pipeline).
