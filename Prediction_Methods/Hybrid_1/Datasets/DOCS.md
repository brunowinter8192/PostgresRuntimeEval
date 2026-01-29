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
├── 06_Filter_Patterns.py               # Filter patterns by approach criteria
├── A_01a_Verify_Extraction.py          # [analysis] Verify extraction completeness
├── A_01b_Verify_Aggregation.py         # [analysis] Verify aggregation correctness
└── Baseline_SVM/                       # [outputs] SVM baseline outputs
    ├── training.csv                    # Training split
    ├── test.csv                        # Test split
    ├── operators/                      # Operator-level datasets (13 types)
    │   ├── Hash_Join/training.csv
    │   └── Seq_Scan/training.csv
    ├── approach_1/                     
    │   ├── patterns.csv                
    │   ├── patterns_filtered.csv       
    │   └── patterns/{hash}/
    │       ├── pattern_info.json
    │       ├── training.csv
    │       ├── training_aggregated.csv
    │       └── training_cleaned.csv
    ├── approach_2/                     
    ├── approach_3/                    
    ├── approach_4/                    
    └── Verification/approach_X/csv/    # Verification results per approach
```

## Working Directory

**CRITICAL:** All commands assume CWD = `Datasets/`

```bash
cd /path/to/Hybrid_1/Datasets
```

## Shared Infrastructure

**Constants from mapping_config.py:**
- `LEAF_OPERATORS` - Leaf node types (SeqScan, IndexScan, IndexOnlyScan)
- `REQUIRED_OPERATORS` - Operators for INCLUDE filter (Hash, Hash Join, Seq Scan, Sort, Nested Loop)
- `PASSTHROUGH_OPERATORS` - Operators for EXCLUDE filter (Incremental Sort, Gather Merge, Gather, Sort, Limit, Merge Join)
- `CHILD_ACTUAL_SUFFIXES` - Child actual time columns to remove
- `CHILD_TIMING_SUFFIXES` - Child st/rt columns for leaf operators
- `PARENT_CHILD_FEATURES` - Parent timing feature column names (st1, rt1, st2, rt2)

**Input data (external):** `Operator_Level/Datasets/Baseline/01_operator_dataset_cleaned.csv`

## Workflow Execution Order

**Main Pipeline (01-06):**
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
     |
06 - Filter_Patterns      [Data_Generation patterns CSV -> approach_X/patterns_filtered.csv]
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

**Purpose:** Extract pattern instances to MD5 hash-named folders with metadata. Supports multi-length patterns and configurable filters.

**Workflow:**
1. Load training data and filter to main plan
2. Build tree structure for each query
3. Apply filters based on --required-operators and --no-passthrough flags
4. For each node at specified --length (or all lengths if 0)
5. Compute MD5 hash for each pattern
6. Extract pattern rows by node_id matching
7. Export training.csv, pattern_info.json per pattern, and patterns.csv inventory

**Inputs:**
- `input_file` - Path to training CSV (positional)

**Outputs:**
- `{output-dir}/patterns.csv` - Pattern inventory for aggregation step
- `{output-dir}/patterns/{hash}/training.csv` - Pattern instances
- `{output-dir}/patterns/{hash}/pattern_info.json` - Pattern metadata

**pattern_info.json structure:**
```json
{
  "pattern_hash": "a1b2c3d4...",
  "pattern_string": "Hash Join -> [Seq Scan (Outer), Hash (Inner)]",
  "folder_name": "Hash_Join_Seq_Scan_Outer_Hash_Inner",
  "pattern_length": 2,
  "occurrence_count": 150
}
```

**Usage:**
```bash
# Approach 3: All patterns, all lengths - MASTER for FFS/Training (372 patterns)
python 03_Extract_Patterns.py training.csv --output-dir approach_3

# Approach 1: Length 2, required operators only (14 patterns)
python 03_Extract_Patterns.py training.csv --output-dir approach_1 --length 2 --required-operators

# Approach 2: Length 2, required operators, no passthrough parents (10 patterns)
python 03_Extract_Patterns.py training.csv --output-dir approach_2 --length 2 --required-operators --no-passthrough

# Approach 4: All lengths, no passthrough parents (53 patterns)
python 03_Extract_Patterns.py training.csv --output-dir approach_4 --no-passthrough
```

**Note:** approach_3 contains all 372 pattern datasets and serves as the source for FFS and model training in Runtime_Prediction. Approaches 1, 2, 4 contain only their selected subsets.

**Variables:**
- `--output-dir` - Base directory for pattern folders (required)
- `--length` - Pattern length to extract: 0 = all lengths, N = specific length (default: 0)
- `--required-operators` - Filter to patterns containing REQUIRED_OPERATORS (flag)
- `--no-passthrough` - Exclude patterns with PASSTHROUGH_OPERATORS as parent (flag)

---

### 04 - Aggregate_Patterns.py

**Purpose:** Aggregate parent and child rows into single feature vectors using recursive tree aggregation

**Workflow:**
1. Load pattern inventory CSV with pattern_hash, pattern_length, operator_count
2. For each pattern in inventory:
   - Load training.csv from pattern folder
   - Build tree structure per query using operator_count for chunking
   - Recursively aggregate subtree into single row
   - Parent features: `{NodeType}_{col}`
   - Child features: `{NodeType}_{Relationship}_{col}`
   - Target columns (actual_startup_time, actual_total_time) at root level
3. Export training_aggregated.csv

**Inputs:**
- `pattern_csv` - Path to pattern inventory CSV (positional)
- `patterns_dir` - Base directory containing patterns/ subfolder (positional)

**Outputs:**
- `{patterns_dir}/patterns/{hash}/training_aggregated.csv` per pattern

**Usage:**
```bash
python 04_Aggregate_Patterns.py Baseline_SVM/approach_1/patterns.csv Baseline_SVM/approach_1
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

### 06 - Filter_Patterns.py

**Purpose:** Apply occurrence threshold filter to approach patterns

**Workflow:**
1. Load Data_Generation mining CSV (has occurrence_count from full dataset)
2. Load approach patterns.csv (already filtered by 03_Extract_Patterns)
3. If threshold > 0: filter by occurrence_count, return matching approach rows
4. If threshold = 0: return all approach rows unchanged
5. Export patterns_filtered.csv

**Inputs:**
- `mining_csv` - Path to Data_Generation pattern mining CSV (positional)
- `approach_csv` - Path to approach patterns.csv (positional)

**Outputs:**
- `{output-dir}/patterns_filtered.csv`
  - Same columns as input patterns.csv

**Usage:**
```bash
# Approach 1/2: no threshold (all patterns)
python 06_Filter_Patterns.py ../Data_Generation/csv/01_patterns_*.csv Baseline_SVM/approach_1/patterns.csv --output-dir Baseline_SVM/approach_1 --threshold 0
python 06_Filter_Patterns.py ../Data_Generation/csv/01_patterns_*.csv Baseline_SVM/approach_2/patterns.csv --output-dir Baseline_SVM/approach_2 --threshold 0

# Approach 3/4: threshold >150 (default)
python 06_Filter_Patterns.py ../Data_Generation/csv/01_patterns_*.csv Baseline_SVM/approach_3/patterns.csv --output-dir Baseline_SVM/approach_3
python 06_Filter_Patterns.py ../Data_Generation/csv/01_patterns_*.csv Baseline_SVM/approach_4/patterns.csv --output-dir Baseline_SVM/approach_4
```

**Variables:**
- `--output-dir` - Output directory for patterns_filtered.csv (required)
- `--threshold` - Occurrence threshold, 0 = no filter (default: 150)

---

## Analysis Scripts

### A_01a - Verify_Extraction.py

**Purpose:** Verify extraction completeness by comparing expected vs actual row counts

**Workflow:**
1. Load pattern inventory CSV (columns: pattern_hash, pattern_string, operator_count, occurrence_count)
2. Calculate expected rows (occurrence_count x operator_count per pattern)
3. Count actual rows in each pattern folder
4. Report match/mismatch/missing status

**Inputs:**
- `pattern_csv` - Path to pattern inventory CSV (positional)
- `patterns_dir` - Base directory with extracted patterns (positional)

**Outputs:**
- `{output-dir}/csv/A_01a_extraction_verification_{timestamp}.csv`
  - Columns: pattern_hash, pattern_string, total_occurrences, num_operators, expected_rows, actual_rows, match, status

**Usage:**
```bash
python A_01a_Verify_Extraction.py Baseline_SVM/approach_1/patterns.csv Baseline_SVM/approach_1 --output-dir Baseline_SVM/Verification/approach_1
```

---

### A_01b - Verify_Aggregation.py

**Purpose:** Verify aggregation correctness by comparing row counts

**Workflow:**
1. Load pattern inventory CSV (columns: pattern_hash, pattern_string, occurrence_count)
2. Count rows in training_aggregated.csv per pattern
3. Compare with occurrence_count
4. Report verification status

**Inputs:**
- `pattern_csv` - Path to pattern inventory CSV (positional)
- `patterns_dir` - Base directory with aggregated patterns (positional)

**Outputs:**
- `{output-dir}/csv/A_01b_aggregation_verification.csv`
  - Columns: pattern_hash, pattern_string, total_occurrences, aggregated_rows, match, status

**Usage:**
```bash
python A_01b_Verify_Aggregation.py Baseline_SVM/approach_1/patterns.csv Baseline_SVM/approach_1 --output-dir Baseline_SVM/Verification/approach_1
```
