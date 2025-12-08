# Data_Generation - Pattern Discovery

Discovers and catalogs all parent-child operator patterns from the operator dataset with MD5 hash identification. Applies REQUIRED_OPERATORS filter to focus on patterns containing specific operator types.

## Directory Structure

```
Data_Generation/
├── 01_Find_Patterns.py                            # Pattern discovery script
└── csv/                                           # [outputs]
    └── 01_baseline_patterns_depth0plus_{ts}.csv   # Pattern inventory with occurrences
```

**Input data (external):** `Operator_Level/Data_Generation/operator_dataset_{ts}.csv`

## Shared Infrastructure

**Constants from mapping_config.py:**
- `REQUIRED_OPERATORS` - Operators that must appear in patterns (Gather, Hash, Hash Join, Nested Loop, Seq Scan)

## Configuration Parameters

### In-Script Configuration (01_Find_Patterns.py)

**Depth Check (Line 47):**
```python
if parent_depth < 0:  # All patterns from depth 0+ (root included)
    continue
```

**Operator Filter (Line 55-57):**
```python
pattern_operators = {parent_type} | {child['node_type'] for child in children}
if not pattern_operators.intersection(REQUIRED_OPERATORS):
    continue
# REQUIRED_OPERATORS = {'Gather', 'Hash', 'Hash Join', 'Nested Loop', 'Seq Scan'}
# This is Hybrid_1's INCLUDE filter (pattern must contain at least one required operator)
```

**MD5 Hash Computation (Lines 117-128):**
```python
def compute_pattern_hash(parent_type: str, children: list) -> str:
    # Creates deterministic hash from pattern structure
    # Format: parent_type|child1_type:child1_rel|child2_type:child2_rel
```

## Hybrid Differences

| Aspect | Hybrid_1 | Hybrid_2 | Hybrid_3 |
|--------|----------|----------|----------|
| Depth Check | `< 0` (root included) | `< 0` (root included) | `< 0` (root included) |
| Filter Type | INCLUDE (REQUIRED_OPERATORS) | None | EXCLUDE (PASSTHROUGH_OPERATORS) |
| MD5 Hash | Yes | Yes | No |
| Pattern Count | ~21 | ~31 | ~20 |

## Workflow Execution Order

```
01 - Find_Patterns
     ↓
Pattern inventory CSV with MD5 hashes
```

Single script phase. Input dataset must exist before execution.

## Script Documentation

### 01 - Find_Patterns.py

**Purpose:** Identify all unique parent-child patterns, compute MD5 hashes, and count occurrences per template

**Workflow:**
1. Load operator dataset and filter to main plan (exclude SubPlan nodes)
2. Extract template identifier from query filenames
3. Build parent-child relationship map for each query
4. Identify patterns by grouping parent with immediate children
5. Filter patterns to include only those with REQUIRED_OPERATORS
6. Compute MD5 hash for each pattern structure
7. Count pattern occurrences per template
8. Export pattern matrix with hashes and template breakdown

**Inputs:**
- `input_file` - Path to operator dataset CSV (positional)

**Outputs:**
- `csv/01_baseline_patterns_depth0plus_{timestamp}.csv`
  - Columns: pattern_hash, pattern, leaf_pattern, total, Q1, Q3, Q4, ... (per template)
  - Pattern format: "Parent -> [Child1 (Outer), Child2 (Inner)]"
  - Hash format: 32-character MD5 hexdigest

**Usage:**
```bash
python 01_Find_Patterns.py operator_dataset.csv --output-dir .
```

**Variables:**
- `--output-dir` - Output directory for CSV results (required)
