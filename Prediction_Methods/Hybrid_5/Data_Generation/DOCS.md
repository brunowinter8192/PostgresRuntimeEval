# Data Generation - Module Documentation

## Directory Structure

```
Data_Generation/
├── 01_Find_Patterns.py                   # Depth-1 pattern discovery
├── csv/                                   # Pattern outputs
│   └── 01_baseline_patterns_depth0plus_{timestamp}.csv
└── DOCS.md                                # This file
```

## Shared Infrastructure

**Parent Module:** `../mapping_config.py`
- `is_passthrough_operator()` - Check if operator should be excluded as pattern root

## Workflow Execution Order

```
Operator_Level Dataset (training.csv)
    |
    v
01_Find_Patterns.py
    |
    v
csv/01_baseline_patterns_depth0plus_{timestamp}.csv
    |
    v
Used by Datasets/03_Extract_Patterns.py
```

**Dependencies:**
- 01 requires: Operator_Level training dataset

## Script Documentation

### 01 - Find_Patterns.py

**Purpose:** Discover depth-1 patterns (Parent + Children) from query execution plans

**Pattern Structure:**
- Depth-1 only: Parent operator + immediate children
- Children sorted by parent_relationship (Outer, Inner)
- Passthrough operators excluded as pattern roots

**Workflow:**
1. Load training dataset and filter to main plan (exclude subplans)
2. Extract template from query_file column
3. Build children map for each query
4. For each non-passthrough operator with children:
   - Format pattern key (e.g., `Hash Join -> [Seq Scan (Outer), Hash (Inner)]`)
   - Compute MD5 hash of pattern structure
   - Determine if all children are leaf nodes (leaf_pattern)
   - Count occurrences per template
5. Create pattern matrix with template columns
6. Export to timestamped CSV

**Inputs:**
- `input_file` - Path to Operator_Level training dataset CSV

**Outputs:**
- `csv/01_baseline_patterns_depth0plus_{timestamp}.csv` - Semicolon-delimited CSV:
  - pattern_hash: MD5 hash for pattern identification
  - pattern: Human-readable pattern string
  - leaf_pattern: Boolean indicating if all children are leaf nodes
  - total: Total occurrences across all templates
  - Q1, Q3, Q4, ... : Occurrence count per template

**Usage:**
```bash
python3 01_Find_Patterns.py <input_file> --output-dir <output_directory>
```

**Example:**
```bash
python3 01_Find_Patterns.py \
  ../../Operator_Level/Datasets/Baseline/training.csv \
  --output-dir .
```

**Variables:**
- `--output-dir` (required): Output directory for pattern analysis results

**Passthrough Operators (excluded as pattern roots):**
- Incremental Sort
- Merge Join
- Limit
- Sort
- Hash

**Hash Computation:**
Pattern hash is MD5 of: `parent_type|child1_type:child1_rel|child2_type:child2_rel|...`
- Children are sorted before hashing for consistency
- Example: `Hash Join|Hash:Inner|Seq Scan:Outer`

**Example Output:**
```
pattern_hash;pattern;leaf_pattern;total;Q1;Q3;Q4;...
a1b2c3d4...;Hash Join -> [Seq Scan (Outer), Hash (Inner)];True;1680;120;120;120;...
e5f6g7h8...;Aggregate -> Hash Join (Outer);False;840;60;60;60;...
```
