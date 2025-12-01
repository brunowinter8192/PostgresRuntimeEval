# Data Generation - Module Documentation

## Directory Structure

```
Data_Generation/
├── 01_Find_Patterns.py                   # Pattern mining script
├── 02a_Extract_Pattern_Leafs.py          # Extract leaf nodes for each pattern
├── 02b_Identify_Pattern_Plan_Leafs.py    # Identify pattern leafs that are also plan leafs
├── 03_Generate_Mapping.py                # Generate PATTERN_LEAF_TIMING_FEATURES mapping
├── csv/                                   # Pattern outputs
│   ├── 01_patterns_YYYYMMDD_HHMMSS.csv               [outputs]
│   ├── 02a_pattern_leafs_YYYYMMDD_HHMMSS.csv         [outputs]
│   └── 02b_pattern_plan_leafs_YYYYMMDD_HHMMSS.csv    [outputs]
├── mapping_addition.txt                   # [outputs] Generated mapping code
└── DOCS.md                                # This file
```

## Shared Infrastructure

**Pattern Length Concept:**
Pattern Length refers to the number of levels (depth) within a pattern structure, distinct from the operator's depth in the overall execution plan. A pattern of length 2 contains 2 levels (parent + children), length 3 contains 3 levels (parent + children + grandchildren), etc.

**QueryNode Class:**
Internal tree node representation with attributes: node_type, parent_relationship, depth, node_id, children list.

## Workflow Execution Order

```
Operator_Level Dataset (03_training.csv)
    |
    v
01_Find_Patterns.py
    |
    v
csv/01_patterns_{timestamp}.csv
    |
    +---> 02a_Extract_Pattern_Leafs.py ---> csv/02a_pattern_leafs_{timestamp}.csv
    |                                            |
    |                                            v
    |                                   03_Generate_Mapping.py
    |                                            |
    |                                            v
    |                                   mapping_addition.txt --> Append to ../mapping_config.py
    |
    +---> 02b_Identify_Pattern_Plan_Leafs.py ---> csv/02b_pattern_plan_leafs_{timestamp}.csv
                                                       |
                                                       v
                                               Used by Runtime_Prediction/00_Clean_FFS.py
```

**Dependencies:**
- 01 requires: Operator_Level/Datasets/Baseline/03_training.csv
- 02a requires: 01 output + same Operator_Level dataset
- 02b requires: 01 output + same Operator_Level dataset
- 03 requires: 02a output
- Manual step: Append mapping_addition.txt to mapping_config.py

## Script Documentation

### 01 - Find_Patterns.py

**Purpose:** Extract recurring structural patterns from query execution plans using iterative depth-based mining

**Workflow:**
1. Load Operator_Level dataset and filter to main plan (exclude subplans)
2. Scan dataset to determine maximum depth
3. Build tree structure for each query from flat DataFrame
4. For each node in each query tree:
   - Extract patterns at length 2, then 3, up to max_depth
   - Compute structural hash (MD5 of node_type + children structure + parent_relationships)
   - Generate readable pattern string
   - Count occurrences across all queries
5. Filter patterns with occurrence count > 120
6. Sort by pattern_length (ascending), then occurrence_count (descending)
7. Export to timestamped CSV

**Inputs:**
- `input_file` - Path to Operator_Level dataset CSV (e.g., Operator_Level/Datasets/Baseline/03_training.csv)

**Outputs:**
- `csv/01_patterns_{timestamp}.csv` - Semicolon-delimited CSV with columns:
  - pattern_hash: MD5 hash for deduplication
  - pattern_string: Human-readable pattern representation
  - pattern_length: Number of levels in pattern (2 to max_depth)
  - occurrence_count: Total occurrences across all queries
  - example_query_file: Sample query containing this pattern

**Usage:**
```bash
python3 01_Find_Patterns.py <input_file> --output-dir <output_directory>
```

**Example:**
```bash
python3 01_Find_Patterns.py \
  /path/to/Operator_Level/Datasets/Baseline/03_training.csv \
  --output-dir Data_Generation
```

**Variables:**
- `--output-dir` (required): Output directory for pattern analysis results

**Notes:**
- All operator types are considered as potential pattern roots (no pass-through filtering)
- Patterns with exactly 120 occurrences are excluded (threshold is > 120, not >= 120)
- Maximum pattern length is dynamically determined from dataset depth
- Patterns are sorted first by length, then by frequency

---

### 02a - Extract_Pattern_Leafs.py

**Purpose:** Extract pattern-leaf nodes (deepest operators within each pattern) for timing feature retention

**Rationale:**
During bottom-up hybrid prediction, patterns consume multiple operators as a single unit. Only the deepest operators within a pattern (pattern-leafs) have children that are predicted separately. Non-leaf operators within the pattern do not have their children predicted, so their child timing features (st1, rt1, st2, rt2) will never be available during prediction. Training on these unavailable features causes data leakage.

**Pattern-Leaf Definition:**
- **Pattern-Leaf:** Operators at maximum depth within the pattern structure (no children in pattern tree)
- **Non-Leaf:** Operators with children within the pattern (root + intermediate nodes)

**Workflow:**
1. Load pattern definitions from 01_Find_Patterns.py output
2. Load Operator_Level dataset to access example queries
3. For each pattern:
   - Extract example query from dataset
   - Build tree structure from query operators
   - Find pattern match using hash computation
   - Traverse pattern tree to depth = pattern_length
   - Identify leaf nodes (nodes without children at max depth)
   - Generate column prefixes for each leaf (e.g., `SeqScan_Outer`, `Hash_Inner`)
   - Deduplicate leaf prefixes (multiple nodes may share same type+relationship)
4. Export pattern hash -> leaf prefixes mapping

**Inputs:**
- `pattern_csv` - Path to 01_patterns_*.csv from Data_Generation
- `input_file` - Path to Operator_Level dataset (e.g., Operator_Level/Datasets/Baseline/02_operator_dataset_with_children.csv)

**Outputs:**
- `csv/02a_pattern_leafs_{timestamp}.csv` - Semicolon-delimited CSV with columns:
  - pattern_hash: Pattern MD5 hash
  - pattern_length: Number of levels in pattern
  - leaf_count: Number of unique leaf prefixes
  - leaf_prefixes: Comma-separated list of leaf prefixes (e.g., `Hash_Inner,SeqScan_Outer`)

**Usage:**
```bash
python3 02a_Extract_Pattern_Leafs.py \
  csv/01_patterns_20251123_170530.csv \
  ../../Operator_Level/Datasets/Baseline/02_operator_dataset_with_children.csv \
  --output-dir .
```

**Variables:**
- `--output-dir` (required): Output directory for pattern leaf extraction results

**Example Output:**
```
pattern_hash;pattern_length;leaf_count;leaf_prefixes
895c6e8c1a30a094329d71cef3111fbd;2;2;Hash_Inner,SeqScan_Outer
9d0e407c0aa5052a4246612a4a2e0ad2;5;3;Hash_Inner,IndexScan_Inner,SeqScan_Outer
```

**Notes:**
- Leaf prefixes are deduplicated (complex patterns may have multiple nodes with same type+relationship)
- Prefixes follow format: `<NodeType>_<ParentRelationship>` (e.g., `SeqScan_Outer`, `Hash_Inner`)
- Root node never included in leaf list (root has no parent relationship prefix)

---

### 02b - Identify_Pattern_Plan_Leafs.py

**Purpose:** Identify pattern leaf operators that are also plan leaf operators (have no children in the overall query plan)

**Rationale:**
During feature selection, child timing features (rt1, rt2, st1, st2) are added for all pattern leafs. However, if a pattern leaf is also a plan leaf (no children in the entire query), these child features will always be zero and should not be used for training. This script identifies which pattern leafs are plan leafs so their child features can be removed during FFS cleaning.

**Concept Distinction:**
- **Pattern Leaf:** Deepest operator within the pattern structure (relative to pattern boundary)
- **Plan Leaf:** Operator with no children in the entire query execution plan
- **Pattern + Plan Leaf:** Operator that is both (e.g., Seq Scan at bottom of a pattern)

**Workflow:**
1. Load pattern definitions from 01_Find_Patterns.py output
2. Load Operator_Level dataset with all queries
3. For each pattern:
   - Find all occurrences across all queries
   - For each occurrence, identify pattern leafs
   - Check if each pattern leaf has children in the query plan
   - Aggregate results: If a pattern leaf is ALWAYS a plan leaf across all occurrences -> is_plan_leaf = ja
4. Export pattern_hash -> pattern_leaf_prefix -> is_plan_leaf mapping

**Inputs:**
- `pattern_csv` - Path to 01_patterns_*.csv from Data_Generation
- `input_file` - Path to Operator_Level dataset (e.g., Operator_Level/Datasets/Baseline/03_training.csv)

**Outputs:**
- `csv/02b_pattern_plan_leafs_{timestamp}.csv` - Semicolon-delimited CSV with columns:
  - pattern_hash: Pattern MD5 hash
  - pattern_length: Number of levels in pattern
  - pattern_leaf_prefix: Leaf prefix (e.g., `SeqScan_Outer`, `Hash_Inner`)
  - node_type: Operator type (e.g., `Seq Scan`, `Hash`)
  - is_plan_leaf: `ja` if always a plan leaf, `nein` if has children in any occurrence

**Usage:**
```bash
python3 02b_Identify_Pattern_Plan_Leafs.py \
  csv/01_patterns_20251123_170530.csv \
  ../../Operator_Level/Datasets/Baseline/03_training.csv \
  --output-dir .
```

**Variables:**
- `--output-dir` (required): Output directory for pattern plan leaf analysis

**Example Output:**
```
pattern_hash;pattern_length;pattern_leaf_prefix;node_type;is_plan_leaf
895c6e8c1a30a094329d71cef3111fbd;2;SeqScan_Outer;Seq Scan;ja
895c6e8c1a30a094329d71cef3111fbd;2;Hash_Inner;Hash;nein
3aab37bea1a884da206eb32f2c1ae5ba;2;SeqScan_Outer;Seq Scan;ja
```

**Interpretation:**
- Pattern `895c6e8c1a30a094329d71cef3111fbd`:
  - `SeqScan_Outer` is always a plan leaf -> Child features (rt1, rt2, st1, st2) should be removed
  - `Hash_Inner` sometimes has children -> Keep child features

**Downstream Usage:**
Output is used by `Runtime_Prediction/00_Clean_FFS.py` to remove child features from pattern+plan leaf operators before training.

---

### 03 - Generate_Mapping.py

**Purpose:** Generate PATTERN_LEAF_TIMING_FEATURES mapping dictionary for inclusion in mapping_config.py

**Workflow:**
1. Load pattern leaf data from 02a_Extract_Pattern_Leafs.py output
2. For each pattern:
   - Parse comma-separated leaf prefixes
   - For each leaf prefix, generate 4 timing feature column names:
     - `<prefix>_st1`, `<prefix>_rt1`, `<prefix>_st2`, `<prefix>_rt2`
   - Combine into list of allowed timing features
3. Export as Python dictionary code to mapping_addition.txt

**Inputs:**
- `leaf_csv` - Path to 02a_pattern_leafs_*.csv from Data_Generation

**Outputs:**
- `mapping_addition.txt`: Python code for PATTERN_LEAF_TIMING_FEATURES dictionary

**Usage:**
```bash
python3 03_Generate_Mapping.py csv/02a_pattern_leafs_20251123_193112.csv --output-dir .
```

**Variables:**
- `--output-dir` (required): Output directory for mapping file

**Example Output (mapping_addition.txt):**
```python
# Pattern leaf timing features to retain during cleaning
# Generated from Data_Generation/csv/02a_pattern_leafs_*.csv
# Format: {hash: [list of timing feature column names]}
PATTERN_LEAF_TIMING_FEATURES = {
    '895c6e8c1a30a094329d71cef3111fbd': ['Hash_Inner_st1', 'Hash_Inner_rt1', 'Hash_Inner_st2', 'Hash_Inner_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    '9d0e407c0aa5052a4246612a4a2e0ad2': ['Hash_Inner_st1', 'Hash_Inner_rt1', 'Hash_Inner_st2', 'Hash_Inner_rt2', 'IndexScan_Inner_st1', 'IndexScan_Inner_rt1', 'IndexScan_Inner_st2', 'IndexScan_Inner_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    ...
}
```

**Post-Execution:**
Manual step: Append `mapping_addition.txt` contents to `../mapping_config.py`
