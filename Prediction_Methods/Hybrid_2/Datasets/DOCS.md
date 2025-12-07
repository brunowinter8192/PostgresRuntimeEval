# Datasets - Hybrid_2 Data Preparation

Prepares training datasets for hybrid pattern-level and operator-level models with template-stratified split.

## Directory Structure

```
Datasets/
├── 01_Split_Train_Test.py           # Template-stratified 120/30 split
├── 02_Extract_Operators.py          # Extract operators to operators/{Type}/
├── 03_Extract_Patterns.py           # Extract patterns to patterns/{hash}/
├── 04_Aggregate_Patterns.py         # Combine parent+children into single rows
├── 05_Clean_Patterns.py             # Remove unavailable features
├── A_01a_Verify_Extraction.py       # [Analysis] Verify extraction completeness
├── A_01b_Verify_Aggregation.py      # [Analysis] Verify aggregation correctness
└── Baseline_SVM/                    # [outputs]
    ├── training.csv                 # Training data (all operators)
    ├── test.csv                     # Test data (all operators)
    ├── operators/
    │   ├── Aggregate/
    │   │   └── training.csv
    │   ├── Hash/
    │   │   └── training.csv
    │   └── {13 Operator Types}/
    └── patterns/
        ├── {md5hash}/
        │   ├── pattern_info.json    # Pattern metadata
        │   ├── training.csv         # Raw pattern instances
        │   ├── training_aggregated.csv
        │   └── training_cleaned.csv
        └── .../
```

## Shared Infrastructure

**Constants from mapping_config.py:**
- `LEAF_OPERATORS` - Leaf node types (SeqScan, IndexScan, IndexOnlyScan)
- `CHILD_ACTUAL_SUFFIXES` - Child actual time columns to remove
- `CHILD_TIMING_SUFFIXES` - Child st/rt columns for leaf operators
- `PARENT_CHILD_FEATURES` - Parent child timing feature column names

## Workflow Execution Order

```
01 - Split_Train_Test     [operator_dataset.csv -> training.csv, test.csv]
     |
     +-> 02 - Extract_Operators    [training.csv -> operators/{Type}/training.csv]
     |
     +-> 03 - Extract_Patterns     [training.csv -> patterns/{hash}/training.csv]
              |
              v
         04 - Aggregate_Patterns   [patterns/ -> training_aggregated.csv]
              |
              v
         05 - Clean_Patterns       [patterns/ -> training_cleaned.csv]
```

## Script Documentation

### 01 - Split_Train_Test.py

**Purpose:** Template-stratified train/test split at query level

**Workflow:**
1. Load operator dataset from Data_Generation
2. Extract template from query_file column
3. Split 120/30 per template with seed=42
4. Export training.csv and test.csv

**Inputs:**
- `input_csv` - Path to operator dataset CSV (positional)

**Outputs:**
- `{output-dir}/training.csv` - Training data (all operators from training queries)
- `{output-dir}/test.csv` - Test data (all operators from test queries)

**Usage:**
```bash
python 01_Split_Train_Test.py ../Data_Generation/operator_dataset.csv --output-dir Baseline_SVM
```

**Variables:**
- `--output-dir` - Output directory (required)
- `--train-size` - Queries per template for training (default: 120)
- `--test-size` - Queries per template for testing (default: 30)
- `--seed` - Random seed (default: 42)

---

### 02 - Extract_Operators.py

**Purpose:** Extract operators into type-specific folders

**Workflow:**
1. Load training.csv
2. Group by node_type
3. Export to operators/{Type}/training.csv

**Inputs:**
- `training_file` - Path to training CSV (positional)

**Outputs:**
- `{output-dir}/operators/{Type}/training.csv` per operator type

**Usage:**
```bash
python 02_Extract_Operators.py Baseline_SVM/training.csv --output-dir Baseline_SVM
```

---

### 03 - Extract_Patterns.py

**Purpose:** Extract pattern instances to hash-named folders

**Workflow:**
1. Load training data and filter to main plan
2. Build parent-child relationship map
3. Identify pattern occurrences with MD5 hash
4. Create folder for each pattern (named by hash)
5. Export training.csv and pattern_info.json

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

---

### 04 - Aggregate_Patterns.py

**Purpose:** Aggregate parent and child rows into single feature vectors

**Workflow:**
1. Iterate over pattern folders in patterns/
2. Load pattern_info.json for pattern structure
3. Match parent-child groups in training.csv
4. Combine features: parent_prefix + col, child_prefix + rel + col
5. Export training_aggregated.csv

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
1. Iterate over pattern folders in patterns/
2. Identify child actual time columns
3. Identify parent st/rt columns (child timings)
4. Identify leaf operator st/rt columns
5. Remove unavailable features
6. Export training_cleaned.csv

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

**Note:** May need update to work with hash-based folder structure.

---

### A_01b - Verify_Aggregation.py

**Purpose:** Verify aggregation correctness by comparing row counts

**Note:** May need update to work with hash-based folder structure.
