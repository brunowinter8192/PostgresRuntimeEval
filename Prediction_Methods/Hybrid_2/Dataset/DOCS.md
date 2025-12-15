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
├── A_01c_Verify_Split.py
├── A_01a_Verify_Extraction.py
├── A_01b_Verify_Aggregation.py
├── Baseline/
├── Operators/
├── Patterns/
└── Verification/
```

## Shared Infrastructure

No shared config files in this directory. Uses `mapping_config.py` from parent directory.

**Constants (01_Split_Data.py):**
- `RANDOM_SEED = 42`: Reproducible splits
- `TRAIN_TRAIN_SIZE = 96`: Queries per template for Training_Training
- `TRAIN_TEST_SIZE = 24`: Queries per template for Training_Test

## Workflow Execution Order

```
                    Hybrid_1/Datasets/Baseline_SVM/
                        training.csv (120/template)
                        test.csv (30/template)
                                |
                                v
                        01_Split_Data.py
                                |
                                v
                        Baseline/
                            Training.csv (120)
                            Test.csv (30)
                            Training_Training.csv (96)
                            Training_Test.csv (24)
                                |
        +-----------------------+------------------------+
        |                                                |
        v                                                v
02a_Split_Operators.py                    Data_Generation/01_Find_Patterns.py
        |                                                |
        v                                                v
Operators/{Training_Full,Training_Training}/    ../Data_Generation/{...}/csv/01_patterns.csv
                                                         |
                                                         v
                                              02b_Extract_Patterns.py
                                                         |
                                                         v
                                              03_Aggregate_Patterns.py
                                                         |
                                                         v
                                              04_Clean_Patterns.py
                                                         |
                                                         v
                                    Patterns/{Training_Full,Training_Training}/{hash}/
                                        training.csv
                                        training_aggregated.csv
                                        training_cleaned.csv
```

**Important:** Data_Generation/01_Find_Patterns.py must run BEFORE 02b_Extract_Patterns.py to generate pattern definitions.

---

## Module Documentation

### 01_Split_Data.py

**Purpose:** Copy and sub-split Hybrid_1 baseline data for Hybrid_2 pipeline.

**Input:**
- `training_csv`: Path to Hybrid_1 training.csv (120 queries/template, 14 templates)
- `test_csv`: Path to Hybrid_1 test.csv (30 queries/template, 14 templates)

**Output:**
- `{output-dir}/Training.csv` - Copy of input (120 queries/template)
- `{output-dir}/Test.csv` - Copy of input (30 queries/template)
- `{output-dir}/Training_Training.csv` - Sub-split (96 queries/template)
- `{output-dir}/Training_Test.csv` - Sub-split (24 queries/template)

**Split Logic:** Template-stratified with seed 42. Each template gets exactly 96 Training_Training + 24 Training_Test queries.

**Usage:**
```
python3 01_Split_Data.py \
    ../Hybrid_1/Datasets/Baseline_SVM/training.csv \
    ../Hybrid_1/Datasets/Baseline_SVM/test.csv \
    --output-dir Baseline
```

---

### 02a_Split_Operators.py

**Purpose:** Split training data by operator type for operator-level model training.

**Input:** Path to Training.csv or Training_Training.csv

**Output:** `{output-dir}/{OperatorType}/{OperatorType}.csv` per operator type

**Usage:**
```
python3 02a_Split_Operators.py Baseline/Training_Training.csv --output-dir Operators/Training_Training
python3 02a_Split_Operators.py Baseline/Training.csv --output-dir Operators/Training_Full
```

---

### 02b_Extract_Patterns.py

**Purpose:** Find all occurrences of known patterns in training data and extract operator rows.

**Input:**
- `input_file`: Path to Training_Training.csv or Training.csv
- `patterns_csv`: Path to 01_patterns.csv from Data_Generation

**Output:** `{output-dir}/{hash}/training.csv` per pattern

**Usage:**
```
python3 02b_Extract_Patterns.py Baseline/Training.csv \
    ../Data_Generation/Training_Full/csv/01_patterns.csv \
    --output-dir Patterns/Training_Full

python3 02b_Extract_Patterns.py Baseline/Training_Training.csv \
    ../Data_Generation/Training_Training/csv/01_patterns.csv \
    --output-dir Patterns/Training_Training
```

---

### 03_Aggregate_Patterns.py

**Purpose:** Aggregate multi-operator pattern occurrences into single-row feature vectors.

**Input:**
- `pattern_csv`: Path to 01_patterns.csv from Data_Generation
- `patterns_dir`: Path to Patterns/{Training_Full,Training_Training}/ directory

**Output:** `{patterns_dir}/{hash}/training_aggregated.csv` per pattern

**Usage:**
```
python3 03_Aggregate_Patterns.py ../Data_Generation/Training_Full/csv/01_patterns.csv Patterns/Training_Full
python3 03_Aggregate_Patterns.py ../Data_Generation/Training_Training/csv/01_patterns.csv Patterns/Training_Training
```

---

### 04_Clean_Patterns.py

**Purpose:** Remove non-predictable timing features from aggregated pattern data.

**Rationale:** At prediction time, only leaf operator timing (st1, rt1, st2, rt2) is known. Parent and intermediate operator timing must be removed from training data.

**Input:** Path to Patterns/{Training_Full,Training_Training}/ directory

**Output:** `{patterns_dir}/{hash}/training_cleaned.csv` per pattern

**Usage:**
```
python3 04_Clean_Patterns.py Patterns/Training_Full
python3 04_Clean_Patterns.py Patterns/Training_Training
```

---

### A_01c_Verify_Split.py

**Purpose:** Verify template-stratified split produced correct query counts per template.

**Input:** Path to Baseline directory with split files

**Output:**
- `{output-dir}/01c_main_split_verification.csv` (Training vs Test)
- `{output-dir}/01c_sub_split_verification.csv` (Training_Training vs Training_Test)

**Usage:**
```
python3 A_01c_Verify_Split.py Baseline --output-dir Verification
```

---

### A_01a_Verify_Extraction.py

**Purpose:** Verify pattern extraction produced correct row counts.

**Input:**
- `patterns_csv`: Path to 01_patterns.csv
- `patterns_dir`: Path to Patterns/{Training_Full,Training_Training}/ directory

**Output:** `{output-dir}/csv/A_01a_extraction_verification_{timestamp}.csv`

**Usage:**
```
python3 A_01a_Verify_Extraction.py ../Data_Generation/Training_Full/csv/01_patterns.csv Patterns/Training_Full --output-dir .
```

---

### A_01b_Verify_Aggregation.py

**Purpose:** Verify pattern aggregation produced correct occurrence counts.

**Input:**
- `patterns_csv`: Path to 01_patterns.csv
- `patterns_dir`: Path to Patterns/{Training_Full,Training_Training}/ directory

**Output:** `{output-dir}/csv/A_01b_aggregation_verification_{timestamp}.csv`

**Usage:**
```
python3 A_01b_Verify_Aggregation.py ../Data_Generation/Training_Full/csv/01_patterns.csv Patterns/Training_Full --output-dir .
```
