# Datasets Module Documentation

## Directory Structure

```
Datasets/
├── 01_Split_Train_Test.py             # Template-stratified train/test split
├── 02_Extract_Operators.py            # Split by node_type into operators/
├── 03_Extract_Patterns.py             # Extract patterns into patterns/<hash>/
├── 04_Aggregate_Patterns.py           # Aggregate operator rows to pattern rows
├── 05_Clean_Patterns.py               # Remove child actuals and leaf timing
├── A_01a_Verify_Extraction.py         # Verify extraction row counts
├── A_01b_Verify_Aggregation.py        # Verify aggregation row counts
├── training.csv                       # [outputs] Training split
├── test.csv                           # [outputs] Test split
├── operators/                         # [outputs] Operator-specific datasets
│   └── {operator_type}/training.csv
├── patterns/                          # [outputs] Pattern datasets by hash
│   └── <hash>/
│       ├── training.csv
│       ├── training_aggregated.csv
│       ├── training_cleaned.csv
│       └── pattern_info.json
├── csv/                               # Verification reports
│   ├── A_01a_extraction_verification_{timestamp}.csv
│   └── A_01b_aggregation_verification.csv
└── DOCS.md                            # This file
```

## Shared Infrastructure

**Parent Module:** `../mapping_config.py`
- `pattern_to_folder_name()` - Convert pattern string to folder name format
- `is_passthrough_operator()` - Check if operator should be excluded
- `LEAF_OPERATORS` - Operators that are typically plan leafs
- `CHILD_ACTUAL_SUFFIXES` - Child actual timing columns to remove
- `CHILD_TIMING_SUFFIXES` - Child predicted timing suffixes
- `PARENT_CHILD_FEATURES` - Parent child timing features

## Workflow Execution Order

```
Operator_Level Dataset
    |
    v
01_Split_Train_Test.py
    |
    v
training.csv + test.csv
    |
    +---> 02_Extract_Operators.py ---> operators/{type}/training.csv
    |
    v
03_Extract_Patterns.py (requires pattern CSV from Data_Generation)
    |
    v
patterns/<hash>/training.csv + pattern_info.json
    |
    v
04_Aggregate_Patterns.py
    |
    v
patterns/<hash>/training_aggregated.csv
    |
    v
05_Clean_Patterns.py
    |
    v
patterns/<hash>/training_cleaned.csv
```

**Dependencies:**
- 01 requires: Operator_Level dataset
- 02 requires: 01 output (training.csv)
- 03 requires: 01 output + Data_Generation pattern CSV
- 04 requires: 03 outputs (patterns/)
- 05 requires: 04 outputs (training_aggregated.csv)

## Script Documentation

### 01 - Split_Train_Test.py

**Purpose:** Create template-stratified train/test split

**Workflow:**
1. Load operator dataset
2. Extract template from query_file column
3. Validate each template has expected query count
4. Split queries per template (120 train, 30 test)
5. Export training.csv and test.csv

**Inputs:**
- `input_csv` - Path to Operator_Level dataset CSV

**Outputs:**
- `training.csv` - Training split (120 queries per template)
- `test.csv` - Test split (30 queries per template)

**Usage:**
```bash
python3 01_Split_Train_Test.py <input_csv> --output-dir <output_directory> \
  --train-size 120 --test-size 30 --seed 42
```

**Variables:**
- `--output-dir` (required): Output directory for split files
- `--train-size` (optional, default=120): Queries per template for training
- `--test-size` (optional, default=30): Queries per template for testing
- `--seed` (optional, default=42): Random seed

---

### 02 - Extract_Operators.py

**Purpose:** Split training data by node_type into operator-specific folders

**Workflow:**
1. Load training dataset
2. Split by node_type column
3. Create folder per operator type
4. Export training.csv per operator

**Inputs:**
- `training_file` - Path to training.csv from 01

**Outputs:**
- `operators/{operator_type}/training.csv` - One file per operator type

**Usage:**
```bash
python3 02_Extract_Operators.py <training_file> --output-dir <output_directory>
```

**Variables:**
- `--output-dir` (required): Base directory for operator folders

---

### 03 - Extract_Patterns.py

**Purpose:** Extract pattern occurrences from training data into hash-organized folders

**Workflow:**
1. Load training data and filter to main plan
2. Build children map for each query
3. For each pattern occurrence:
   - Match parent + children against patterns
   - Compute pattern hash
   - Collect row indices
4. For each unique pattern:
   - Create patterns/<hash>/ folder
   - Export training.csv with matched rows
   - Create pattern_info.json with metadata

**Inputs:**
- `input_file` - Path to training.csv
- `--output-dir` - Base directory for patterns/ folder

**Outputs:**
- `patterns/<hash>/training.csv` - Operator rows for this pattern
- `patterns/<hash>/pattern_info.json` - Pattern metadata:
  - pattern_hash: MD5 hash
  - pattern_string: Human-readable pattern
  - folder_name: Folder name format (e.g., `Hash_Join_Seq_Scan_Outer_Hash_Inner`)
  - leaf_pattern: Boolean
  - occurrence_count: Number of occurrences

**Usage:**
```bash
python3 03_Extract_Patterns.py <training_file> --output-dir <output_directory>
```

**Variables:**
- `--output-dir` (required): Output directory for pattern folders

---

### 04 - Aggregate_Patterns.py

**Purpose:** Aggregate operator-level rows into pattern-level rows with hierarchical features

**Workflow:**
1. Get all pattern folders from patterns/
2. For each pattern:
   - Load training.csv
   - Load pattern_info.json for structure
   - Build children map per query
   - Match pattern structure and aggregate:
     - Parent features get prefix (e.g., `HashJoin_`)
     - Child features get hierarchical prefix (e.g., `SeqScan_Outer_`)
   - Export training_aggregated.csv

**Aggregation Logic:**
- **Root node:** Features prefixed with cleaned node type
- **Child nodes:** Features prefixed with node type + relationship
- **Targets:** Only root keeps actual_startup_time, actual_total_time

**Inputs:**
- `patterns_dir` - Base directory containing patterns/ subfolder

**Outputs:**
- `patterns/<hash>/training_aggregated.csv` - One row per pattern occurrence

**Usage:**
```bash
python3 04_Aggregate_Patterns.py <patterns_directory>
```

---

### 05 - Clean_Patterns.py

**Purpose:** Remove child actual timing and leaf operator timing features

**Workflow:**
1. For each pattern in patterns/:
   - Load training_aggregated.csv
   - Identify parent operator prefix
   - Remove child actual timing columns (CHILD_ACTUAL_SUFFIXES)
   - Remove parent child timing features (PARENT_CHILD_FEATURES)
   - Remove leaf operator timing features (for operators in LEAF_OPERATORS)
   - Export training_cleaned.csv

**Cleaning Rules:**
- Remove all `*_Outer_actual_startup_time`, `*_Outer_actual_total_time`, etc.
- Remove parent's st1, rt1, st2, rt2 features
- Remove child timing (st1, rt1, st2, rt2) for leaf operators (SeqScan, IndexScan, IndexOnlyScan)

**Inputs:**
- `patterns_dir` - Base directory containing patterns/ subfolder

**Outputs:**
- `patterns/<hash>/training_cleaned.csv` - Production-ready features

**Usage:**
```bash
python3 05_Clean_Patterns.py <patterns_directory>
```

---

## Analysis Scripts

### A_01a - Verify_Extraction.py

**Purpose:** Verify extraction correctness by comparing expected vs actual row counts

**Inputs:**
- `pattern_csv` - Pattern analysis CSV from Data_Generation
- `patterns_dir` - Base directory containing patterns/ subfolder

**Outputs:**
- `csv/A_01a_extraction_verification_{timestamp}.csv`

**Usage:**
```bash
python3 A_01a_Verify_Extraction.py <pattern_csv> <patterns_dir> --output-dir .
```

---

### A_01b - Verify_Aggregation.py

**Purpose:** Verify aggregation correctness (one row per occurrence)

**Inputs:**
- `pattern_csv` - Pattern analysis CSV from Data_Generation
- `patterns_dir` - Base directory containing patterns/ subfolder

**Outputs:**
- `csv/A_01b_aggregation_verification.csv`

**Usage:**
```bash
python3 A_01b_Verify_Aggregation.py <pattern_csv> <patterns_dir> --output-dir .
```

---

## Notes

**Pattern Organization:**
- Patterns identified by MD5 hash of structure
- Each pattern has dedicated folder: `patterns/<hash>/`
- `pattern_info.json` provides human-readable metadata
- `build_pattern_hash_map()` in mapping_config.py maps folder names to hashes

**Verification Reports:**
- Check for MISMATCH or MISSING status
- 100% OK rate indicates pipeline correctness
