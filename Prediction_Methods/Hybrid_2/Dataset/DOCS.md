# Dataset - DOCS.md

## Directory Structure

```
Dataset/
├── DOCS.md
├── 01_Split_Data.py
├── 02a_Split_Operators.py
├── 02b_Extract_Patterns.py
├── 03_Aggregate_Patterns.py
├── 04_Clean_Patterns.py
├── A_01a_Verify_Extraction.py
├── A_01b_Verify_Aggregation.py
├── Baseline/
└── Patterns/
```

## Shared Infrastructure

No shared config files in this directory. Uses `mapping_config.py` from parent directory.

**Constants:**
- `RANDOM_SEED = 42`: Reproducible train/test splits
- `TRAIN_TEST_RATIO = 0.8`: 80% training, 20% test
- `TRAIN_TRAIN_RATIO = 0.8`: Further 80/20 split of training for validation

## Workflow Execution Order

```
01 -> 02a (Operator) + 02b (Pattern) -> 03 -> 04 -> A_01a + A_01b (verification)
```

**Data Flow:**
- Input: `Operator_Level/Datasets/Baseline/02_operator_dataset_with_children.csv`
- Output Operator: `Baseline/Operators/{OperatorType}/{OperatorType}.csv`
- Output Pattern: `Patterns/Training_Training/{hash}/training_cleaned.csv`

---

## Module Documentation

### 01_Split_Data.py

**Purpose:** Split operator dataset into train/test sets at query level.

**Input:** Path to 02_operator_dataset_with_children.csv

**Output:**
- `{output-dir}/Training.csv` (80% of queries)
- `{output-dir}/Test.csv` (20% of queries)
- `{output-dir}/Training_Training.csv` (64% of queries)
- `{output-dir}/Training_Test.csv` (16% of queries)

**Usage:**
```
python3 01_Split_Data.py ../Operator_Level/Datasets/Baseline/02_operator_dataset_with_children.csv --output-dir Baseline
```

### load_data()
Load operator dataset with semicolon delimiter.

### get_unique_queries()
Extract unique query_file identifiers from dataset.

### split_queries()
Split queries into two sets based on ratio using sklearn train_test_split.

### export_split()
Export rows belonging to specified queries to CSV.

---

### 02a_Split_Operators.py

**Purpose:** Split training data by operator type for operator-level model training.

**Input:** Path to Training.csv or Training_Training.csv

**Output:** `{output-dir}/{OperatorType}/{OperatorType}.csv` per operator type

**Usage:**
```
python3 02a_Split_Operators.py Baseline/Training_Training.csv --output-dir Baseline/Operators
```

### load_data()
Load operator dataset with semicolon delimiter.

### get_unique_operators()
Get set of unique operator types from dataset.

### export_operator_data()
Export rows for single operator type to dedicated folder.

---

### 02b_Extract_Patterns.py

**Purpose:** Find all occurrences of known patterns in training data and extract operator rows.

**Input:**
- `input_file`: Path to Training_Training.csv
- `patterns_csv`: Path to 01_patterns_*.csv from Data_Generation

**Output:** `{output-dir}/Patterns/Training_Training/{hash}/training.csv` per pattern

**Usage:**
```
python3 02b_Extract_Patterns.py Baseline/Training_Training.csv ../Data_Generation/Training_Full/csv/01_patterns_*.csv --output-dir .
```

### load_and_filter_data()
Load training data and filter to main plan (exclude subplans).

### load_pattern_info()
Load pattern definitions from mining CSV into dictionary.

### extract_all_pattern_occurrences()
For each query build tree, compute hashes, match against known patterns.

### build_tree_from_dataframe()
Build QueryNode tree structure from flat DataFrame.

### extract_all_nodes()
Extract all nodes from tree recursively into list.

### has_children_at_length()
Check if node has children at target pattern length.

### compute_pattern_hash_at_length()
Compute structural MD5 hash for pattern at specific depth.

### extract_pattern_node_ids()
Extract node IDs of all nodes in pattern up to specified length.

### export_pattern_datasets()
Export pattern datasets to separate directories.

---

### 03_Aggregate_Patterns.py

**Purpose:** Aggregate multi-operator pattern occurrences into single-row feature vectors.

**Input:**
- `pattern_csv`: Path to 01_patterns_*.csv from Data_Generation
- `patterns_dir`: Path to Patterns/Training_Training/ directory

**Output:** `{patterns_dir}/{hash}/training_aggregated.csv` per pattern

**Usage:**
```
python3 03_Aggregate_Patterns.py ../Data_Generation/Training_Full/csv/01_patterns_*.csv Patterns/Training_Training
```

### load_pattern_data()
Load pattern definitions from Data_Generation output.

### build_tree_from_query()
Build tree structure from flat DataFrame for single query chunk.

### clean_node_type()
Remove spaces from node type for column naming.

### aggregate_subtree()
Aggregate subtree into single row with hierarchical prefixes.

### process_pattern_folder()
Process single pattern folder: load, chunk, aggregate, export.

---

### 04_Clean_Patterns.py

**Purpose:** Remove non-predictable timing features from aggregated pattern data.

**Rationale:** At prediction time, only leaf operator timing (st1, rt1, st2, rt2) is known.
Parent and intermediate operator timing must be removed from training data.

**Input:** Path to Patterns/Training_Training/ directory

**Output:** `{patterns_dir}/{hash}/training_cleaned.csv` per pattern

**Usage:**
```
python3 04_Clean_Patterns.py Patterns/Training_Training
```

### get_pattern_folders()
Get all pattern subdirectories.

### process_all_patterns()
Iterate over all pattern folders and clean each.

### load_aggregated_data()
Load aggregated training data from CSV.

### identify_parent_prefix()
Identify parent operator prefix from column names (column ending with _actual_startup_time without _Outer_ or _Inner_).

### identify_columns_to_remove()
Identify columns to remove:
- All CHILD_ACTUAL_SUFFIXES (actual timing of children)
- Parent's PARENT_CHILD_FEATURES (st1, rt1, st2, rt2)
- CHILD_TIMING_SUFFIXES for LEAF_OPERATORS

### remove_columns()
Remove specified columns from dataframe.

### export_cleaned_data()
Save cleaned dataset to pattern folder.

---

### A_01a_Verify_Extraction.py

**Purpose:** Verify pattern extraction produced correct row counts.

**Input:**
- `patterns_csv`: Path to 01_patterns_*.csv
- `patterns_dir`: Path to Patterns/Training_Training/ directory

**Output:** `{output-dir}/csv/A_01a_extraction_verification_{timestamp}.csv`

**Usage:**
```
python3 A_01a_Verify_Extraction.py ../Data_Generation/Training_Full/csv/01_patterns_*.csv Patterns/Training_Training --output-dir .
```

---

### A_01b_Verify_Aggregation.py

**Purpose:** Verify pattern aggregation produced correct occurrence counts.

**Input:**
- `patterns_csv`: Path to 01_patterns_*.csv
- `patterns_dir`: Path to Patterns/Training_Training/ directory

**Output:** `{output-dir}/csv/A_01b_aggregation_verification_{timestamp}.csv`

**Usage:**
```
python3 A_01b_Verify_Aggregation.py ../Data_Generation/Training_Full/csv/01_patterns_*.csv Patterns/Training_Training --output-dir .
```
