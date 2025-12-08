# Datasets - Pattern Data Preparation

Splits operator dataset, extracts pattern instances with MD5 hash identification, aggregates parent-child rows, and prepares training datasets for pattern-level models.

## Directory Structure

```
Datasets/
├── 01_Split_Train_Test.py              # Template-stratified train/test split
├── 02_Extract_Operators.py             # Extract operators to type folders
├── 03_Extract_Patterns.py              # Extract patterns to hash folders
├── 04_Aggregate_Patterns.py            # Combine parent+children into single rows
├── 05_Clean_Patterns.py                # Remove unavailable features
├── A_01a_Verify_Extraction.py          # [analysis] Verify extraction completeness
├── A_01b_Verify_Aggregation.py         # [analysis] Verify aggregation correctness
└── Baseline_SVM/                       # [outputs] SVM baseline outputs
    ├── training.csv                    # Training split
    ├── test.csv                        # Test split
    ├── operators/                      # Operator-level datasets
    │   ├── Hash_Join/training.csv
    │   └── Seq_Scan/training.csv
    └── patterns/                       # Pattern datasets by MD5 hash
        ├── a1b2c3d4.../
        │   ├── pattern_info.json       # Pattern metadata
        │   ├── training.csv            # Raw pattern instances
        │   ├── training_aggregated.csv # Parent+children combined
        │   └── training_cleaned.csv    # Production-ready features
        └── e5f6g7h8.../
            └── ...
```

## Shared Infrastructure

**Constants from mapping_config.py:**
- `LEAF_OPERATORS` - Leaf node types (SeqScan, IndexScan, IndexOnlyScan)
- `REQUIRED_OPERATORS` - Operators required in patterns (INCLUDE filter)
- `CHILD_ACTUAL_SUFFIXES` - Child actual time columns to remove
- `CHILD_TIMING_SUFFIXES` - Child st/rt columns for leaf operators
- `PARENT_CHILD_FEATURES` - Parent timing feature column names (st1, rt1, st2, rt2)

**Input data (external):** `Operator_Level/Data_Generation/operator_dataset_{ts}.csv`

## Workflow Execution Order

**Main Pipeline (01-05):**
```
01 - Split_Train_Test     [operator_dataset.csv -> training.csv, test.csv]
     |
02 - Extract_Operators    [training.csv -> operators/{Type}/training.csv]
     |
03 - Extract_Patterns     [training.csv -> patterns/{hash}/training.csv + pattern_info.json]
     |
04 - Aggregate_Patterns   [patterns/{hash}/ -> training_aggregated.csv per pattern]
     |
05 - Clean_Patterns       [patterns/{hash}/ -> training_cleaned.csv per pattern]
```

**Analysis Scripts (A_):**
```
A_01a - Verify_Extraction   [patterns/{hash}/ -> verification CSV]
A_01b - Verify_Aggregation  [patterns/{hash}/ -> aggregation verification]
```

## Script Documentation

### 01 - Split_Train_Test.py

**Purpose:** Split operator dataset into training and test sets with template stratification

**Workflow:**
1. Load operator dataset CSV
2. Add template column from query_file
3. Validate each template has expected query count
4. Split queries per template (120 train / 30 test)
5. Export training.csv and test.csv

**Inputs:**
- `input_csv` - Path to operator dataset CSV (positional)

**Outputs:**
- `{output-dir}/training.csv` - Training operators
- `{output-dir}/test.csv` - Test operators

**Usage:**
```bash
python 01_Split_Train_Test.py operator_dataset.csv --output-dir Baseline_SVM --train-size 120 --test-size 30 --seed 42
```

**Variables:**
- `--output-dir` - Output directory (required)
- `--train-size` - Queries per template for training (default: 120)
- `--test-size` - Queries per template for testing (default: 30)
- `--seed` - Random seed (default: 42)

---

### 02 - Extract_Operators.py

**Purpose:** Extract operators into type-specific folders for operator-level models

**Workflow:**
1. Load training dataset
2. Split by node_type
3. Create folder per operator type
4. Export training.csv per type

**Inputs:**
- `training_file` - Path to training CSV (positional)

**Outputs:**
- `{output-dir}/operators/{Type}/training.csv` per operator type

**Usage:**
```bash
python 02_Extract_Operators.py Baseline_SVM/training.csv --output-dir Baseline_SVM
```

**Variables:**
- `--output-dir` - Base directory for operator folders (required)

---

### 03 - Extract_Patterns.py

**Purpose:** Extract pattern instances to MD5 hash-named folders with metadata

**Workflow:**
1. Load training data and filter to main plan
2. Build parent-child relationship map
3. Apply REQUIRED_OPERATORS filter
4. Compute MD5 hash for each pattern
5. Create folder per pattern hash
6. Export training.csv and pattern_info.json

**Inputs:**
- `input_file` - Path to training CSV (positional)

**Outputs:**
- `{output-dir}/patterns/{hash}/training.csv` - Pattern instances
- `{output-dir}/patterns/{hash}/pattern_info.json` - Pattern metadata

**pattern_info.json structure:**
```json
{
  "pattern_hash": "a1b2c3d4...",
  "pattern_string": "Hash Join -> [Seq Scan (Outer), Hash (Inner)]",
  "folder_name": "Hash_Join_Seq_Scan_Outer_Hash_Inner",
  "leaf_pattern": true,
  "occurrence_count": 150
}
```

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
1. Load pattern_info.json for each pattern hash folder
2. Load training.csv for each pattern
3. Parse pattern structure from folder_name in metadata
4. Match parent-child groups in data
5. Combine features: parent_prefix + col, child_prefix + rel + col
6. Export training_aggregated.csv

**Inputs:**
- `patterns_dir` - Base directory containing patterns subfolder (positional)

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
1. Load pattern_info.json for each pattern
2. Identify columns to remove:
   - Child actual time columns
   - Parent st/rt columns (child timings)
   - Leaf operator st/rt columns
3. Export training_cleaned.csv

**Inputs:**
- `patterns_dir` - Base directory containing patterns subfolder (positional)

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
1. Load pattern inventory from find_all_patterns output
2. Calculate expected rows (occurrences x operators per pattern)
3. Count actual rows in each pattern folder
4. Report match/mismatch/missing status

**Inputs:**
- `pattern_csv` - Path to pattern inventory CSV (positional)
- `patterns_dir` - Base directory with extracted patterns (positional)

**Outputs:**
- `{output-dir}/csv/A_01a_extraction_verification_{timestamp}.csv`

**Usage:**
```bash
python A_01a_Verify_Extraction.py baseline_patterns.csv Baseline_SVM --output-dir Baseline_SVM
```

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
- `{output-dir}/csv/A_01b_aggregation_verification.csv`

**Usage:**
```bash
python A_01b_Verify_Aggregation.py baseline_patterns.csv Baseline_SVM --output-dir Baseline_SVM
```
