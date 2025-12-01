# Datasets Module Documentation

## Directory Structure

```
Datasets/
├── 01_Extract_Patterns.py             # Extract pattern occurrences from Operator_Level dataset
├── 02_Aggregate_Patterns.py           # Aggregate operator rows to pattern rows
├── 03_Clean_Aggregated.py             # Remove non-leaf timing features
├── A_01a_Calculate_Operator_Counts.py # Calculate operators per pattern (initial setup)
├── A_01b_Verify_Extraction.py         # Verify extraction row counts
├── A_01c_Verify_Aggregation.py        # Verify aggregation row counts
├── A_01d_Analyze_NaN.py               # Analyze NaN in cleaned datasets
├── A_01e_Check_Training_NaN.py        # Analyze NaN in training datasets
├── A_01f_Verify_Operator_Counts.py    # Verify operator counts per pattern
├── A_01g_Show_Example_Instances.py    # Show example pattern instances
├── A_01h_Check_Multiples.py           # Check operator count multiples
├── A_01i_Check_Node_Types.py          # Check node type combinations
├── Baseline/                           # Pattern datasets organized by hash
│   ├── <pattern_hash_1>/
│   │   ├── training.csv               # [outputs] Extracted operator-level data
│   │   ├── training_aggregated.csv    # [outputs] Aggregated pattern-level data
│   │   └── training_cleaned.csv       # [outputs] Cleaned data (leaf timing features only)
│   ├── <pattern_hash_2>/
│   │   └── ...
│   └── ...                             # (72 pattern directories total)
└── csv/                                # Verification reports
    ├── A_01a_operator_counts_*.csv    # [outputs] Operator counts per pattern
    ├── A_01b_verification_*.csv       # [outputs] Extraction verification
    └── A_01c_verification_*.csv       # [outputs] Aggregation verification
```

---

## Shared Infrastructure

**Parent Module:** `../mapping_config.py`
- `PATTERNS`: List of 72 pattern hash IDs (from Data_Generation mining)
- `PATTERN_OPERATOR_COUNT`: Dict mapping pattern hash to operator count
- `PATTERN_LEAF_TIMING_FEATURES`: Dict mapping pattern hash to leaf timing features to retain

---

## Workflow Execution Order

```
01_Extract_Patterns.py
    ↓ Extracts pattern occurrences → Baseline/<hash>/training.csv

02_Aggregate_Patterns.py
    ↓ Aggregates operators → Baseline/<hash>/training_aggregated.csv

03_Clean_Aggregated.py
    ↓ Removes non-leaf timing features → Baseline/<hash>/training_cleaned.csv
```

**Dependencies:**
- 01 requires Data_Generation mining results + Operator_Level dataset
- 02 requires 01 outputs + mapping_config.PATTERN_OPERATOR_COUNT
- 03 requires 02 outputs + mapping_config.PATTERN_LEAF_TIMING_FEATURES

---

## Script Documentation

### 01 - Extract_Patterns.py

**Purpose:** Extract pattern occurrences from Operator_Level dataset into separate folders

**Workflow:**
1. Load Operator_Level training dataset (operator-level features)
2. Load pattern mining results (hash IDs, lengths, occurrence counts)
3. For each query:
   - Build tree structure from operators
   - Search for all pattern occurrences
   - Extract operator rows belonging to each pattern
4. Group by pattern hash and export to `Baseline/<hash>/training.csv`

**Inputs:**
- `input_file`: Path to Operator_Level dataset (e.g., `../../Operator_Level/Datasets/Baseline/training_cleaned.csv`)
- `patterns_csv`: Path to Data_Generation mining CSV
- `--output-dir`: Output directory (creates Baseline/ subdirectory)

**Outputs:**
- `Baseline/<pattern_hash>/training.csv` (72 files):
  - Columns: All operator-level features (node_type, depth, actual_startup_time, actual_total_time, st1, rt1, st2, rt2, etc.)
  - Format: Semicolon-delimited CSV
  - Rows: `operator_count * occurrence_count` per pattern

**Usage:**
```bash
python3 01_Extract_Patterns.py \
  ../../Operator_Level/Datasets/Baseline/training_cleaned.csv \
  ../Data_Generation/csv/01_patterns_20251123_170530.csv \
  --output-dir .
```

---

### 02 - Aggregate_Patterns.py

**Purpose:** Aggregate operator-level rows into pattern-level rows with hierarchical features

**Workflow:**
1. Load pattern hash and length from mining CSV
2. Load operator count from mapping_config.PATTERN_OPERATOR_COUNT
3. For each pattern:
   - Read `Baseline/<hash>/training.csv`
   - Group by query_file
   - For each query: Chunk rows into groups of `operator_count`
   - For each chunk:
     - Build tree structure from operators
     - Aggregate features with hierarchical prefixes
     - Keep targets only for root node (actual_startup_time, actual_total_time)
4. Export aggregated dataset

**Aggregation Logic:**
- **Root node:** Features get prefix (e.g., `HashJoin_node_type`), targets unprefixed
- **Child nodes:** Features get hierarchical prefix (e.g., `SeqScan_Outer_node_type`)
- **Targets removed:** Child node targets excluded (only root keeps actual_startup_time, actual_total_time)

**Inputs:**
- `pattern_csv`: Path to Data_Generation mining CSV
- `patterns_dir`: Base directory containing Baseline/ folder

**Outputs:**
- `Baseline/<pattern_hash>/training_aggregated.csv` (72 files):
  - Columns: `query_file`, aggregated features with prefixes, `actual_startup_time`, `actual_total_time`
  - Format: Semicolon-delimited CSV
  - Rows: `occurrence_count` (one row per pattern occurrence)

**Usage:**
```bash
python3 02_Aggregate_Patterns.py \
  ../Data_Generation/csv/01_patterns_20251123_170530.csv \
  Baseline
```

---

### 03 - Clean_Aggregated.py

**Purpose:** Remove non-leaf timing features from aggregated datasets to prevent training on unavailable features

**Rationale:**
During bottom-up prediction, only pattern-leaf nodes have their children predicted separately (below the pattern). Non-leaf nodes within the pattern are consumed as a group, so their child predictions (st1, rt1, st2, rt2) will never be available at prediction time.

**Workflow:**
1. Load pattern hash list from mapping_config.PATTERNS
2. For each pattern:
   - Load `Baseline/<hash>/training_aggregated.csv`
   - Load allowed timing features from `mapping_config.PATTERN_LEAF_TIMING_FEATURES[hash]`
   - Identify all timing columns (ending with _st1, _rt1, _st2, _rt2)
   - Drop all timing columns NOT in allowed list
   - Export cleaned dataset

**Inputs:**
- `dataset_base_dir`: Base directory containing pattern subdirectories (e.g., `Baseline/`)

**Outputs:**
- `Baseline/<pattern_hash>/training_cleaned.csv` (72 files):
  - Columns: Same as aggregated, except non-leaf timing features removed
  - Format: Semicolon-delimited CSV
  - Rows: Same as training_aggregated.csv (occurrence_count)

**Usage:**
```bash
python3 03_Clean_Aggregated.py Baseline/
```

---

## Analysis Scripts

Analysis scripts are standalone tools for verification and debugging. They are NOT part of the main workflow.

### A_01a - Calculate_Operator_Counts.py

**Purpose:** Calculate number of operators per pattern for verification and aggregation (initial setup)

**Outputs:** `csv/A_01a_operator_counts_{timestamp}.csv`

**Usage:**
```bash
python3 A_01a_Calculate_Operator_Counts.py \
  ../Data_Generation/csv/01_patterns_*.csv \
  . \
  --output-dir .
```

**Post-Execution:** Manual step - copy operator counts to `mapping_config.PATTERN_OPERATOR_COUNT`

---

### A_01b - Verify_Extraction.py

**Purpose:** Verify extraction correctness by comparing expected vs actual row counts

**Outputs:** `csv/A_01b_verification_{timestamp}.csv`

**Usage:**
```bash
python3 A_01b_Verify_Extraction.py \
  ../Data_Generation/csv/01_patterns_*.csv \
  . \
  --output-dir .
```

---

### A_01c - Verify_Aggregation.py

**Purpose:** Verify aggregation correctness by comparing expected vs actual aggregated row counts

**Outputs:** `csv/A_01c_verification_{timestamp}.csv`

**Usage:**
```bash
python3 A_01c_Verify_Aggregation.py \
  ../Data_Generation/csv/01_patterns_*.csv \
  Baseline \
  --output-dir .
```

---

### A_01d - Analyze_NaN.py

**Purpose:** Analyze NaN values in FFS-relevant features of cleaned datasets

**Outputs:** `A_01d_nan_analysis.md`

---

### A_01e - Check_Training_NaN.py

**Purpose:** Analyze NaN values in training.csv before aggregation

**Outputs:** `A_01e_training_nan_analysis.md`

---

### A_01f - Verify_Operator_Counts.py

**Purpose:** Verify operator counts match expected PATTERN_OPERATOR_COUNT values

**Outputs:** `A_01f_operator_count_verification.md`

---

### A_01g - Show_Example_Instances.py

**Purpose:** Show example pattern instances with different operator counts

**Outputs:** `A_01g_example_instances_{pattern_hash}.md`

---

### A_01h - Check_Multiples.py

**Purpose:** Check if all query instances have operator counts that are multiples of expected

**Outputs:** `A_01h_multiples_check.md`

---

### A_01i - Check_Node_Types.py

**Purpose:** Check node type + parent relationship combinations in dataset

**Outputs:** `A_01i_node_types_{pattern_hash}.md`

---

## Notes

**Pattern Organization:**
- Patterns identified by MD5 hash of structure (node types + relationships)
- Each pattern has dedicated folder: `Baseline/<hash>/`
- Hash IDs stored in `mapping_config.PATTERNS` for consistency

**Verification Reports:**
- Timestamped CSVs track execution history
- Manual review required: Check for MISMATCH status
- 100% OK rate indicates pipeline correctness
