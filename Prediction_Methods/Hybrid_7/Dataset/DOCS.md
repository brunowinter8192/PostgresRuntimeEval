# Dataset - DOCS.md

## Shared Infrastructure

No shared config files. All scripts use standard pandas/sklearn imports.

**Constants:**
- `RANDOM_SEED = 42`: Reproducible train/test splits
- `TRAIN_TEST_RATIO = 0.8`: 80% training, 20% test
- `TRAIN_TRAIN_RATIO = 0.8`: Further 80/20 split of training for validation

## Workflow Execution Order

```
01 -> 02 + 02b (parallel) -> 03 -> 04 -> A_01a + A_01b (verification)
```

**Data Flow:**
- Input: `Operator_Level/Datasets/Baseline/02_operator_dataset_with_children.csv`
- Output: `Baseline/Patterns/{hash}/training_cleaned.csv` per pattern

---

## Script Documentation

### 01 - Split_Data.py

**Purpose:** Split operator dataset into train/test sets at query level.

**Workflow:**
1. Load operator dataset
2. Extract unique query_file identifiers
3. Split queries 80/20 into Training/Test
4. Split Training 80/20 into Training_Training/Training_Test
5. Export all rows belonging to each query set

**Inputs:**
- `input`: Path to 02_operator_dataset_with_children.csv

**Outputs:**
- `{output-dir}/Training.csv` (80% of queries)
- `{output-dir}/Test.csv` (20% of queries)
- `{output-dir}/Training_Training.csv` (64% of queries)
- `{output-dir}/Training_Test.csv` (16% of queries)

**Usage:**
```
python3 01_Split_Data.py ../Operator_Level/Datasets/Baseline/02_operator_dataset_with_children.csv --output-dir Baseline
```

---

### 02 - Extract_Patterns.py

**Purpose:** Find all occurrences of known patterns in training data and extract operator rows.

**Workflow:**
1. Load Training_Training.csv and filter to main plan
2. Load pattern definitions from Data_Generation
3. For each query: build tree, compute hashes at each node
4. Match hashes against known patterns
5. Export matching operator rows per pattern

**Inputs:**
- `input_file`: Path to Training_Training.csv
- `patterns_csv`: Path to 01_patterns_*.csv from Data_Generation

**Outputs:**
- `{output-dir}/Patterns/{hash}/training.csv` per pattern

**Usage:**
```
python3 02_Extract_Patterns.py Baseline/Training_Training.csv ../Data_Generation/csv/01_patterns_*.csv --output-dir Baseline
```

---

### 02b - Extract_Leafs.py

**Purpose:** Identify leaf node positions within each pattern structure.

**Workflow:**
1. Load pattern definitions
2. For each pattern: find example occurrence in training data
3. Extract leaf prefixes (NodeType_ParentRelationship format)
4. Export pattern-leaf mapping

**Inputs:**
- `pattern_csv`: Path to 01_patterns_*.csv from Data_Generation
- `input_file`: Path to Training_Training.csv

**Outputs:**
- `{output-dir}/csv/02b_pattern_leafs_{timestamp}.csv`
  - Columns: pattern_hash;pattern_length;leaf_count;leaf_prefixes

**Usage:**
```
python3 02b_Extract_Leafs.py ../Data_Generation/csv/01_patterns_*.csv Baseline/Training_Training.csv --output-dir Baseline
```

---

### 03 - Aggregate_Patterns.py

**Purpose:** Aggregate multi-operator pattern occurrences into single-row feature vectors.

**Workflow:**
1. Load pattern definitions
2. For each pattern folder: load training.csv
3. Group rows by query_file (each group = one pattern occurrence)
4. Aggregate features: prefix columns with NodeType_ParentRelationship
5. Export one row per occurrence

**Inputs:**
- `pattern_csv`: Path to 01_patterns_*.csv from Data_Generation
- `patterns_dir`: Path to Patterns/ directory

**Outputs:**
- `{patterns_dir}/{hash}/training_aggregated.csv` per pattern

**Usage:**
```
python3 03_Aggregate_Patterns.py ../Data_Generation/csv/01_patterns_*.csv Baseline/Patterns
```

---

### 04 - Clean_Aggregated.py

**Purpose:** Remove parent timing features, keep only pattern-leaf timing features.

**Workflow:**
1. Load pattern-leaf mapping from 02b output
2. For each pattern: identify allowed timing features (leaf prefixes only)
3. Remove all *_st1, *_rt1, *_st2, *_rt2 columns except allowed
4. Export cleaned dataset

**Inputs:**
- `pattern_leafs_csv`: Path to 02b_pattern_leafs_*.csv
- `patterns_dir`: Path to Patterns/ directory

**Outputs:**
- `{patterns_dir}/{hash}/training_cleaned.csv` per pattern

**Usage:**
```
python3 04_Clean_Aggregated.py Baseline/csv/02b_pattern_leafs_*.csv Baseline/Patterns
```

---

### A_01a - Verify_Extraction.py

**Purpose:** Verify pattern extraction produced correct row counts.

**Workflow:**
1. Load pattern definitions with expected occurrence counts
2. For each pattern: count rows in training.csv
3. Compare expected (occurrence_count * operator_count) vs actual
4. Report OK/MISMATCH status

**Inputs:**
- `patterns_csv`: Path to 01_patterns_*.csv
- `patterns_dir`: Path to Patterns/ directory

**Outputs:**
- `{output-dir}/csv/A_01a_extraction_verification_{timestamp}.csv`

**Usage:**
```
python3 A_01a_Verify_Extraction.py ../Data_Generation/csv/01_patterns_*.csv Baseline/Patterns --output-dir Baseline
```

---

### A_01b - Verify_Aggregation.py

**Purpose:** Verify pattern aggregation produced correct occurrence counts.

**Workflow:**
1. Load pattern definitions with expected occurrence counts
2. For each pattern: count rows in training_aggregated.csv
3. Compare expected occurrence_count vs actual rows
4. Report OK/MISMATCH status

**Inputs:**
- `patterns_csv`: Path to 01_patterns_*.csv
- `patterns_dir`: Path to Patterns/ directory

**Outputs:**
- `{output-dir}/csv/A_01b_aggregation_verification_{timestamp}.csv`

**Usage:**
```
python3 A_01b_Verify_Aggregation.py ../Data_Generation/csv/01_patterns_*.csv Baseline/Patterns --output-dir Baseline
```
