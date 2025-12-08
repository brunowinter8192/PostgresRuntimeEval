# Datasets - Pattern Data Preparation

Splits data, extracts operators and patterns, aggregates parent-child rows, and prepares training datasets for pattern-level models.

## Directory Structure

```
Datasets/
├── 01_Split_Train_Test.py             # Split into train/test (template-stratified)
├── 02_Extract_Operators.py            # Extract operators to /operators/{type}/
├── 03_Extract_Patterns.py             # Extract patterns to /patterns/{hash}/
├── 04_Aggregate_Patterns.py           # Combine parent+children into single rows
├── 05_Clean_Patterns.py               # Remove unavailable features
├── A_01a_Verify_Extraction.py         # [ANALYSIS] Verify extraction completeness
├── A_01b_Verify_Aggregation.py        # [ANALYSIS] Verify aggregation correctness
└── Baseline_SVM/                      # [outputs] SVM baseline outputs
    ├── training.csv                   # Training split
    ├── test.csv                       # Test split
    ├── operators/                     # Per-operator datasets
    │   ├── Aggregate/training.csv
    │   ├── Hash_Join/training.csv
    │   └── ...
    ├── patterns/                      # Per-pattern datasets (hash-based)
    │   ├── {md5_hash}/
    │   │   ├── pattern_info.json      # Pattern metadata
    │   │   ├── training.csv           # Raw pattern instances
    │   │   ├── training_aggregated.csv # Parent+children combined
    │   │   └── training_cleaned.csv   # Production-ready features
    │   └── ...
    └── csv/                           # Verification results
        ├── A_01a_extraction_verification_{ts}.csv
        └── A_01b_aggregation_verification.csv
```

## Shared Infrastructure

**Constants from mapping_config.py:**
- `LEAF_OPERATORS` - Leaf node types (SeqScan, IndexScan, IndexOnlyScan)
- `CHILD_ACTUAL_SUFFIXES` - Child actual time columns to remove
- `CHILD_TIMING_SUFFIXES` - Child st/rt columns for leaf operators
- `PARENT_CHILD_FEATURES` - Parent timing feature suffixes
- `PASSTHROUGH_OPERATORS` - Pass-through operators (Hash, Sort, Limit, Incremental Sort, Merge Join)

**Functions from mapping_config.py:**
- `is_passthrough_operator()` - Check if operator is pass-through
- `pattern_to_folder_name()` - Convert pattern string to folder format

## Configuration Parameters

### Hybrid Evolution

**Hybrid_3:**
- Depth: `< 0` (Root included)
- Operator Filter: **Pass-Through Operator Filter**
- Folder Structure: **Hash-based** (`/patterns/{hash}/`)
- Result: **20 patterns** (PT parent patterns excluded)

**Hybrid_2:**
- Depth: `< 0` (Root included)
- Operator Filter: None (all pattern types)
- Folder Structure: **Hash-based** (`/patterns/{hash}/`)
- Result: **31 patterns** (all operators as parents)

## Workflow Execution Order

**Main Pipeline (01-05):**
```
01 - Split_Train_Test      [operator_dataset.csv -> training.csv, test.csv]
     |
02 - Extract_Operators     [training.csv -> operators/{type}/training.csv]
     |
03 - Extract_Patterns      [training.csv -> patterns/{hash}/training.csv + pattern_info.json]
     |
04 - Aggregate_Patterns    [patterns/{hash}/ -> training_aggregated.csv]
     |
05 - Clean_Patterns        [patterns/{hash}/ -> training_cleaned.csv]
```

**Analysis Scripts (optional verification):**
```
A_01a - Verify_Extraction   [pattern_csv + patterns/ -> verification CSV]
A_01b - Verify_Aggregation  [pattern_csv + patterns/ -> aggregation verification]
```

## Script Documentation

### 01 - Split_Train_Test.py

**Purpose:** Create template-stratified train/test split

**Workflow:**
1. Load operator dataset
2. Extract template from query_file column
3. Validate each template has expected query count
4. Split queries with stratification by template
5. Export training and test datasets

**Inputs:**
- `input_csv` - Path to operator dataset CSV (positional)

**Outputs:**
- `{output-dir}/training.csv` - Training split
- `{output-dir}/test.csv` - Test split

**Usage:**
```bash
python 01_Split_Train_Test.py operator_dataset.csv --output-dir Baseline_SVM
```

**Variables:**
- `--output-dir` - Output directory for train/test files (required)
- `--train-size` - Queries per template for training (default: 120)
- `--test-size` - Queries per template for testing (default: 30)
- `--seed` - Random seed (default: 42)

---

### 02 - Extract_Operators.py

**Purpose:** Extract operators to type-specific folders

**Workflow:**
1. Load training dataset
2. Split by node_type
3. Create folder per operator type
4. Export training.csv per operator

**Inputs:**
- `training_file` - Path to training dataset CSV (positional)

**Outputs:**
- `{output-dir}/operators/{Operator_Type}/training.csv` per operator

**Usage:**
```bash
python 02_Extract_Operators.py Baseline_SVM/training.csv --output-dir Baseline_SVM
```

**Variables:**
- `--output-dir` - Base directory for operator folders (required)

---

### 03 - Extract_Patterns.py

**Purpose:** Extract pattern instances to hash-based folders with metadata

**Workflow:**
1. Load training data and filter to main plan
2. Build parent-child relationship map
3. Skip pass-through operators as parents
4. Compute MD5 hash for each pattern structure
5. Create folder per pattern hash
6. Export training.csv and pattern_info.json

**Inputs:**
- `input_file` - Path to training dataset CSV (positional)

**Outputs:**
- `{output-dir}/patterns/{hash}/training.csv` - Pattern instances
- `{output-dir}/patterns/{hash}/pattern_info.json` - Pattern metadata:
  - `pattern_hash` - MD5 hash of pattern structure
  - `pattern_string` - Human-readable pattern format
  - `folder_name` - Folder name format (for model output)
  - `leaf_pattern` - Whether all children are leaf operators
  - `occurrence_count` - Number of pattern instances

**Usage:**
```bash
python 03_Extract_Patterns.py Baseline_SVM/training.csv --output-dir Baseline_SVM
```

**Variables:**
- `--output-dir` - Base directory for pattern folders (required)

---

### 04 - Aggregate_Patterns.py

**Purpose:** Aggregate parent and child rows into single feature vectors

**Workflow:**
1. Get all pattern folders from patterns/ subdirectory
2. Load pattern_info.json for each pattern
3. Parse pattern structure from folder_name
4. Match parent-child groups in training.csv
5. Combine features: parent_prefix + col, child_prefix + rel + col
6. Export training_aggregated.csv

**Inputs:**
- `patterns_dir` - Base directory containing patterns/ subfolder (positional)

**Outputs:**
- `{patterns_dir}/patterns/{hash}/training_aggregated.csv` per pattern

**Usage:**
```bash
python 04_Aggregate_Patterns.py Baseline_SVM
```

---

### 05 - Clean_Patterns.py

**Purpose:** Remove features unavailable at prediction time

**Workflow:**
1. Get all pattern folders from patterns/ subdirectory
2. Load pattern_info.json for each pattern
3. Identify and remove:
   - Child actual time columns
   - Parent st/rt columns (child timings)
   - Leaf operator st/rt columns
4. Export training_cleaned.csv

**Inputs:**
- `patterns_dir` - Base directory containing patterns/ subfolder (positional)

**Outputs:**
- `{patterns_dir}/patterns/{hash}/training_cleaned.csv` per pattern

**Usage:**
```bash
python 05_Clean_Patterns.py Baseline_SVM
```

---

## Analysis Scripts

### A_01a - Verify_Extraction.py

**Purpose:** Verify extraction completeness by comparing expected vs actual row counts

**Workflow:**
1. Load pattern inventory (with pattern_hash column)
2. Calculate expected rows (occurrences x operators per pattern)
3. Count actual rows in patterns/{hash}/training.csv
4. Report match/mismatch/missing status

**Inputs:**
- `pattern_csv` - Path to pattern inventory CSV with pattern_hash column (positional)
- `patterns_dir` - Base directory containing patterns/ subfolder (positional)

**Outputs:**
- `{output-dir}/csv/A_01a_extraction_verification_{timestamp}.csv`
  - Columns: pattern_hash, pattern, leaf_pattern, total_occurrences, num_operators, expected_rows, actual_rows, match, status

**Usage:**
```bash
python A_01a_Verify_Extraction.py ../Data_Generation/csv/01_baseline_patterns.csv Baseline_SVM --output-dir Baseline_SVM
```

**Variables:**
- `--output-dir` - Output directory for verification results (required)

---

### A_01b - Verify_Aggregation.py

**Purpose:** Verify aggregation correctness by comparing row counts

**Workflow:**
1. Load pattern inventory (with pattern_hash column)
2. Count rows in patterns/{hash}/training_aggregated.csv
3. Compare with expected occurrence count
4. Report verification status

**Inputs:**
- `pattern_csv` - Path to pattern inventory CSV with pattern_hash column (positional)
- `patterns_dir` - Base directory containing patterns/ subfolder (positional)

**Outputs:**
- `{output-dir}/csv/A_01b_aggregation_verification.csv`
  - Columns: pattern_hash, pattern, leaf_pattern, total_occurrences, aggregated_rows, match, status

**Usage:**
```bash
python A_01b_Verify_Aggregation.py ../Data_Generation/csv/01_baseline_patterns.csv Baseline_SVM --output-dir Baseline_SVM
```

**Variables:**
- `--output-dir` - Output directory for verification results (required)
