# Datasets - Pattern Data Preparation

Extracts pattern instances, aggregates parent-child rows, and prepares training datasets for pattern-level models.

## Shared Infrastructure

**Constants from mapping_config.py:**
- `LEAF_OPERATORS` - Leaf node types (SeqScan, IndexScan, IndexOnlyScan)
- `CHILD_ACTUAL_SUFFIXES` - Child actual time columns to remove
- `CHILD_TIMING_SUFFIXES` - Child st/rt columns for leaf operators
- `CHILD_FEATURES_TIMING` - Child timing feature column names (st1, rt1, st2, rt2)
- `PASSTHROUGH_OPERATORS` - Pass-through operators (Hash, Sort, Limit, Incremental Sort, Merge Join, Gather Merge, Aggregate)
- `is_passthrough_operator()` - Check if operator is pass-through

## Configuration Parameters

### Hybrid Evolution

**Hybrid_4:**
- Depth: `< 0` (Root eingeschlossen)
- Operator Filter: **Extended Pass-Through Filter** (excludes Hash, Sort, Limit, Incremental Sort, Merge Join, Gather Merge, Aggregate as parents)
- Result: **9 patterns** (extended PT parent patterns excluded)

**Hybrid_3:**
- Depth: `< 0` (Root eingeschlossen)
- Operator Filter: **Pass-Through Operator Filter** (excludes Hash, Sort, Limit, Incremental Sort, Merge Join as parents)
- Result: **20 patterns** (PT parent patterns excluded)

**Hybrid_2:**
- Depth: `< 0` (Root eingeschlossen)
- Operator Filter: KEIN Filter (alle Pattern-Typen)
- Result: **31 patterns** (alle Operatoren als Parents)

**Hybrid_1:**
- Depth: `< 1` (Root ausgeschlossen)
- Operator Filter: REQUIRED_OPERATORS (nur Gather, Hash, Hash Join, Nested Loop, Seq Scan)
- Result: **21 patterns** (gefiltert, ohne Root-Level)

## Workflow Execution Order

**Main Pipeline (01-03):**
```
01 - Extract_Patterns    [operator_dataset.csv -> Pattern folders with training.csv]
     |
02 - Aggregate_Patterns  [Pattern folders -> training_aggregated.csv per pattern]
     |
03 - Clean_Patterns      [Pattern folders + leaf_csv -> training_cleaned.csv per pattern]
```

**Analysis Scripts (optional):**
```
A_01a - Verify_Extraction   [pattern_csv + Pattern folders -> verification CSV]
A_01b - Verify_Aggregation  [pattern_csv + Pattern folders -> aggregation verification]
```

## Script Documentation

### 01 - Extract_Patterns.py

**Purpose:** Extract all instances of each pattern to dedicated folders

**Workflow:**
1. Load training data and filter to main plan
2. Build parent-child relationship map
3. Identify pattern occurrences with row indices
4. Create folder for each pattern
5. Export pattern instances (parent + children rows) to training.csv

**Inputs:**
- `input_file` - Path to operator dataset CSV (positional)

**Outputs:**
- `{output-dir}/{Pattern_Name}/training.csv` per pattern
  - Contains all parent and child rows for pattern instances

**Usage:**
```bash
python 01_Extract_Patterns.py operator_dataset.csv --output-dir Baseline_SVM
```

**Variables:**
- `--output-dir` - Base directory for pattern folders (required)

---

### 02 - Aggregate_Patterns.py

**Purpose:** Aggregate parent and child rows into single feature vectors

**Workflow:**
1. Load training.csv for each pattern folder
2. Parse pattern structure from folder name
3. Match parent-child groups in data
4. Combine features: parent_prefix + col, child_prefix + rel + col
5. Export aggregated rows to training_aggregated.csv

**Inputs:**
- `patterns_dir` - Base directory containing pattern folders (positional)

**Outputs:**
- `{patterns_dir}/{Pattern_Name}/training_aggregated.csv` per pattern
  - One row per pattern occurrence with all features combined

**Usage:**
```bash
python 02_Aggregate_Patterns.py Baseline_SVM
```

---

### 03 - Clean_Patterns.py

**Purpose:** Remove features unavailable at prediction time (child actuals)

**Workflow:**
1. Load leaf pattern mapping from inventory
2. For each pattern folder:
   - Identify child actual time columns
   - Identify parent st/rt columns (child timings)
   - Identify leaf operator st/rt columns
3. Remove these unavailable features
4. Export training_cleaned.csv

**Inputs:**
- `patterns_dir` - Directory containing pattern folders (positional)
- `leaf_csv` - Path to leaf pattern CSV (positional)

**Outputs:**
- `{patterns_dir}/{Pattern_Name}/training_cleaned.csv` per pattern

**Usage:**
```bash
python 03_Clean_Patterns.py Baseline_SVM baseline_patterns.csv
```

---

## Analysis Scripts

### A_01a - Verify_Extraction.py

**Purpose:** Verify extraction completeness by comparing expected vs actual row counts

**Workflow:**
1. Load pattern inventory from find_all_patterns output
2. Calculate expected rows (occurrences x operators per pattern)
3. Count actual rows in each pattern folder
4. Report match/mismatch/missing status

**Inputs:**
- `pattern_csv` - Path to pattern inventory CSV (positional)
- `patterns_dir` - Base directory with extracted patterns (positional)

**Outputs:**
- `{output-dir}/csv/pattern_extraction_verification_{timestamp}.csv`
  - Columns: pattern, leaf_pattern, total_occurrences, num_operators, expected_rows, actual_rows, match, status

**Usage:**
```bash
python A_01a_Verify_Extraction.py baseline_patterns.csv Baseline_SVM --output-dir Baseline_SVM
```

**Variables:**
- `--output-dir` - Output directory for verification results (required)

---

### A_01b - Verify_Aggregation.py

**Purpose:** Verify aggregation correctness by comparing row counts

**Workflow:**
1. Load pattern inventory
2. Count rows in training_aggregated.csv per pattern
3. Compare with expected occurrence count
4. Report verification status

**Inputs:**
- `pattern_csv` - Path to pattern inventory CSV (positional)
- `patterns_dir` - Base directory with aggregated patterns (positional)

**Outputs:**
- `{output-dir}/csv/aggregation_verification.csv`
  - Columns: pattern, leaf_pattern, total_occurrences, aggregated_rows, match, status

**Usage:**
```bash
python A_01b_Verify_Aggregation.py baseline_patterns.csv Baseline_SVM --output-dir Baseline_SVM
```

**Variables:**
- `--output-dir` - Output directory for verification results (required)
