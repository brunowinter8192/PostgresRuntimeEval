# Datasets Module Documentation

## Directory Structure

```
Datasets/
├── 01_Calculate_Counts.py            # Calculate operators per pattern
├── 02_Extract_Patterns.py            # Extract pattern occurrences from Operator_Level dataset
├── 03_Aggregate_Patterns.py          # Aggregate operator rows to pattern rows
├── 04_Clean_Aggregated.py            # Remove non-leaf timing features
├── A_01a_Verify_Extraction.py        # [Analysis] Verify extraction row counts
├── A_01b_Verify_Aggregation.py       # [Analysis] Verify aggregation row counts
├── A_01c_Analyze_NaN.py              # [Analysis] Analyze NaN values in cleaned datasets
├── Baseline/                          # Pattern datasets organized by hash
│   ├── <pattern_hash_1>/
│   │   ├── training.csv              # [outputs] Extracted operator-level data
│   │   ├── training_aggregated.csv   # [outputs] Aggregated pattern-level data
│   │   └── training_cleaned.csv      # [outputs] Cleaned data (leaf timing features only)
│   ├── <pattern_hash_2>/
│   │   └── ...
│   └── ...                            # (32 pattern directories total)
├── csv/                               # Verification reports
│   ├── 01_operator_counts_*.csv      # [outputs] Operator counts per pattern
│   ├── A_01a_verification_*.csv      # [outputs] Extraction verification
│   └── A_01b_verification_*.csv      # [outputs] Aggregation verification
└── md/
    └── A_01c_nan_analysis.md         # [outputs] NaN analysis report
```

---

## Shared Infrastructure

**Parent Module:** `../mapping_config.py`
- `PATTERNS`: List of 32 pattern hash IDs (from Data_Generation mining with PT filter)
- `PATTERN_OPERATOR_COUNT`: Dict mapping pattern hash to operator count
- `PATTERN_LEAF_TIMING_FEATURES`: Dict mapping pattern hash to leaf timing features to retain
- `PASSTHROUGH_OPERATORS`: List of 7 operators excluded as pattern roots (startup_total_ratio > 0.95)
- `is_passthrough_operator()`: Function to check if operator is pass-through
- `NON_FEATURE_SUFFIXES`: List of column suffixes excluded from FFS

---

## Workflow Execution Order

```
01_Calculate_Counts.py
    ↓ Calculates operator_count for each pattern

02_Extract_Patterns.py
    ↓ Extracts pattern occurrences → Baseline/<hash>/training.csv

03_Aggregate_Patterns.py
    ↓ Aggregates operators → Baseline/<hash>/training_aggregated.csv

04_Clean_Aggregated.py
    ↓ Removes non-leaf timing features → Baseline/<hash>/training_cleaned.csv
```

**Analysis Scripts (optional, run after respective workflow steps):**
- `A_01a_Verify_Extraction.py` - Verifies 02 outputs
- `A_01b_Verify_Aggregation.py` - Verifies 03 outputs
- `A_01c_Analyze_NaN.py` - Analyzes 04 outputs for NaN values

**Dependencies:**
- 01 must run before updating mapping_config.py with PATTERN_OPERATOR_COUNT
- 02 requires Data_Generation mining results + Operator_Level dataset
- 03 requires 02 outputs + mapping_config.PATTERN_OPERATOR_COUNT
- 04 requires 03 outputs + mapping_config.PATTERN_LEAF_TIMING_FEATURES

---

## Script Documentation

### 01 - Calculate_Counts.py

**Purpose:** Calculate number of operators per pattern for verification and aggregation

**Workflow:**
1. Read extracted pattern datasets from Baseline/ folders
2. For each pattern: Calculate `operator_count = actual_rows / occurrence_count`
3. Verify all patterns have consistent operator counts
4. Export results to CSV

**Inputs:**
- `patterns_csv`: Path to Data_Generation mining CSV (e.g., `01_patterns_*.csv`)
- `datasets_dir`: Path to Datasets directory (contains Baseline/)

**Outputs:**
- `csv/01_operator_counts_{timestamp}.csv`:
  - Columns: `pattern_hash`, `pattern_string`, `operator_count`
  - Format: Semicolon-delimited CSV
  - Purpose: Manual verification before updating mapping_config.py

**Usage:**
```bash
python3 01_Calculate_Counts.py \
  ../Data_Generation/csv/01_patterns_20251123_170530.csv \
  . \
  --output-dir .
```

**Variables:**
- `--output-dir`: Output directory for CSV export (required)

**Post-Execution:**
Manual step: Copy operator counts to `mapping_config.PATTERN_OPERATOR_COUNT`

---

### 02 - Extract_Patterns.py

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
- `Baseline/<pattern_hash>/training.csv` (32 files):
  - Columns: All operator-level features (node_type, depth, actual_startup_time, actual_total_time, st1, rt1, st2, rt2, etc.)
  - Format: Semicolon-delimited CSV
  - Rows: `operator_count * occurrence_count` per pattern
  - Purpose: Operator-level data for each pattern occurrence

**Usage:**
```bash
python3 02_Extract_Patterns.py \
  ../../Operator_Level/Datasets/Baseline/training_cleaned.csv \
  ../Data_Generation/csv/01_patterns_20251123_170530.csv \
  --output-dir .
```

**Variables:**
- `--output-dir`: Output directory for pattern datasets (required)

---

### 03 - Aggregate_Patterns.py

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
- **Chunk-based:** Simple grouping by operator_count, no pattern matching needed

**Inputs:**
- `pattern_csv`: Path to Data_Generation mining CSV
- `patterns_dir`: Base directory containing Baseline/ folder

**Outputs:**
- `Baseline/<pattern_hash>/training_aggregated.csv` (32 files):
  - Columns: `query_file`, aggregated features with prefixes, `actual_startup_time`, `actual_total_time`
  - Format: Semicolon-delimited CSV
  - Rows: `occurrence_count` (one row per pattern occurrence)
  - Purpose: Pattern-level dataset ready for model training

**Usage:**
```bash
python3 03_Aggregate_Patterns.py \
  ../Data_Generation/csv/01_patterns_20251123_170530.csv \
  Baseline
```

**Variables:**
None (all positional)

**Key Implementation Detail:**
Uses simplified chunk-based aggregation: Groups rows by `operator_count` instead of complex tree traversal with hash matching. Assumes extraction already filtered correct pattern nodes.

---

### 04 - Clean_Aggregated.py

**Purpose:** Remove non-leaf timing features from aggregated datasets to prevent training on unavailable features

**Rationale:**
During bottom-up prediction, only pattern-leaf nodes have their children predicted separately (below the pattern). Non-leaf nodes within the pattern are consumed as a group, so their child predictions (st1, rt1, st2, rt2) will never be available at prediction time. Training on these features would cause data leakage.

**Workflow:**
1. Load pattern hash list from mapping_config.PATTERNS
2. For each pattern:
   - Load `Baseline/<hash>/training_aggregated.csv`
   - Load allowed timing features from `mapping_config.PATTERN_LEAF_TIMING_FEATURES[hash]`
   - Identify all timing columns (ending with _st1, _rt1, _st2, _rt2)
   - Drop all timing columns NOT in allowed list
   - Export cleaned dataset

**Pattern-Leaf Concept:**
- **Pattern-Leaf:** Deepest operators within the pattern structure (no children in pattern)
- **Non-Leaf:** Operators with children within the pattern (root + intermediate nodes)
- **Example Pattern:** `Hash Join → [Seq Scan (Outer), Hash (Inner)]`
  - Leafs: `SeqScan_Outer`, `Hash_Inner` → Keep their st1/rt1/st2/rt2
  - Non-Leaf: `HashJoin` → Drop its st1/rt1/st2/rt2

**Inputs:**
- `dataset_base_dir`: Base directory containing Baseline/ folder with pattern subdirectories

**Outputs:**
- `Baseline/<pattern_hash>/training_cleaned.csv` (32 files):
  - Columns: Same as aggregated, except non-leaf timing features removed
  - Format: Semicolon-delimited CSV
  - Rows: Same as training_aggregated.csv (occurrence_count)
  - Purpose: Clean dataset for Feature Selection without data leakage

**Usage:**
```bash
python3 04_Clean_Aggregated.py Baseline/
```

**Variables:**
None (single positional argument)

**Verification:**
- Simple pattern (length 2): Root timing features removed, 2 leaf timing features retained
- Complex pattern (length 5+): Root + intermediate timing features removed, 3+ leaf timing features retained
- File size: Cleaned CSV smaller than aggregated CSV

---

## Analysis Scripts

### A_01a - Verify_Extraction.py

**Purpose:** Verify extraction correctness by comparing expected vs actual row counts

**Workflow:**
1. Load pattern information (hash, occurrence_count, operator_count)
2. For each pattern:
   - Expected rows = `operator_count * occurrence_count`
   - Actual rows = `len(Baseline/<hash>/training.csv)`
   - Status = OK if match, MISMATCH otherwise
3. Export verification report

**Inputs:**
- `patterns_csv`: Path to Data_Generation mining CSV
- `datasets_dir`: Path to Datasets directory (contains Baseline/)
- `--output-dir`: Output directory for verification report

**Outputs:**
- `csv/A_01a_verification_{timestamp}.csv`:
  - Columns: `pattern_hash`, `pattern_string`, `pattern_length`, `operator_count`, `occurrence_count`, `expected_rows`, `actual_rows`, `status`
  - Format: Semicolon-delimited CSV
  - Expected: All patterns with status = OK

**Usage:**
```bash
python3 A_01a_Verify_Extraction.py \
  ../Data_Generation/csv/01_patterns_20251123_170530.csv \
  . \
  --output-dir .
```

**Variables:**
- `--output-dir`: Output directory for verification CSV (required)

**Success Criteria:**
All 32 patterns show `status = OK`

---

### A_01b - Verify_Aggregation.py

**Purpose:** Verify aggregation correctness by comparing expected vs actual aggregated row counts

**Workflow:**
1. Load pattern information (hash, occurrence_count)
2. For each pattern:
   - Expected rows = `occurrence_count`
   - Actual rows = `len(Baseline/<hash>/training_aggregated.csv)`
   - Status = OK if match, MISMATCH otherwise
3. Export verification report

**Inputs:**
- `patterns_csv`: Path to Data_Generation mining CSV
- `datasets_dir`: Path to Datasets directory (contains Baseline/)
- `--output-dir`: Output directory for verification report

**Outputs:**
- `csv/A_01b_verification_{timestamp}.csv`:
  - Columns: `pattern_hash`, `pattern_string`, `pattern_length`, `occurrence_count`, `expected_rows`, `actual_rows`, `status`
  - Format: Semicolon-delimited CSV
  - Expected: All patterns with status = OK

**Usage:**
```bash
python3 A_01b_Verify_Aggregation.py \
  ../Data_Generation/csv/01_patterns_20251123_170530.csv \
  Baseline \
  --output-dir .
```

**Variables:**
- `--output-dir`: Output directory for verification CSV (required)

**Success Criteria:**
All 32 patterns show `status = OK`

---

### A_01c - Analyze_NaN.py

**Purpose:** Analyze NaN values in cleaned datasets for FFS-relevant features only

**Workflow:**
1. Load pattern hash list from mapping_config.PATTERNS
2. For each pattern:
   - Load `Baseline/<hash>/training_cleaned.csv`
   - Extract FFS-relevant features (exclude metadata columns)
   - Identify columns with NaN values and count
3. Export markdown report

**Inputs:**
- `dataset_base_dir`: Base directory containing pattern subdirectories (e.g., Baseline/)
- `--output-dir`: Output directory for markdown report

**Outputs:**
- `md/A_01c_nan_analysis.md`:
  - Lists patterns with NaN values
  - Shows affected columns and NaN counts
  - Reports percentage of affected rows

**Usage:**
```bash
python3 A_01c_Analyze_NaN.py Baseline/ --output-dir .
```

**Variables:**
- `--output-dir`: Output directory for markdown report (required)

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

**Aggregation Target Handling:**
- Root node: Keeps `actual_startup_time`, `actual_total_time` unprefixed
- Child nodes: Targets excluded (st1/rt1/st2/rt2 features retained)
- Prevents data leakage: Only root targets available at prediction time
