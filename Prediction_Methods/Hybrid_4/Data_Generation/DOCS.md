# Data_Generation - Pattern Discovery

Discovers and catalogs all parent-child operator patterns from the training dataset. Patterns are searched starting from depth 0 (root operator), including root-level patterns in addition to all child patterns.

## Directory Structure

```
Data_Generation/
├── 01_Find_Patterns.py                         # Pattern discovery script
├── 02_Compare_Patterns.py                      # Pattern comparison script (Hybrid_2 vs Hybrid_3)
├── operator_dataset_{timestamp}.csv            # Input dataset from Operator_Level
├── csv/                                        # [outputs]
│   └── baseline_patterns_depth0plus_{ts}.csv   # Pattern inventory with occurrences
└── md/                                         # [outputs]
    └── pattern_comparison_{ts}.md              # Comparison report Hybrid_2 vs Hybrid_3
```

## Shared Infrastructure

No external dependencies. All pattern discovery logic is self-contained.

## Configuration Parameters

### Input Data Selection

Die entscheidende Stellschraube fuer Baseline vs All Templates:

| Approach | Input Datei | Templates |
|----------|-------------|-----------|
| **Baseline** | `Operator_Level/Datasets/Baseline/04_training.csv` | Ohne Q2, Q11, Q16, Q22 (InitPlan/SubPlan) |
| **All Templates** | `operator_dataset_{ts}.csv` | Alle 22 TPC-H Templates |

### In-Script Configuration (01_Find_Patterns.py)

**Depth Check (Zeile 44):**
```python
if parent_depth < 0:  # Hybrid_2: Alle Patterns ab Depth 0 (Root eingeschlossen)
    continue
# vs Hybrid_1:
if parent_depth < 1:  # Nur Patterns ab Depth 1 (Root ausgeschlossen)
    continue
```

**Operator Filter:**
- Hybrid_3: Pass-Through Operator Filter (excludes Hash, Sort, Limit, Incremental Sort, Merge Join as parents)
- Hybrid_2: KEIN Filter (alle Operator-Kombinationen)
- Hybrid_1: REQUIRED_OPERATORS Filter (nur Gather, Hash, Hash Join, Nested Loop, Seq Scan)

### Output Naming

- Hybrid_3: `baseline_patterns_depth0plus_{ts}.csv` (20 patterns, PT parents excluded)
- Hybrid_2: `baseline_patterns_depth0plus_{ts}.csv` (31 patterns, all operators)
- Hybrid_1: `baseline_patterns_depth1plus_{ts}.csv`

## Workflow Execution Order

```
01 - Find_Patterns
     ↓
Pattern inventory CSV
```

Single script phase. Input dataset must be placed in this directory before execution.

## Script Documentation

### 01 - Find_Patterns.py

**Purpose:** Identify all unique parent-child patterns and count occurrences per template

**Workflow:**
1. Load operator dataset and filter to main plan (exclude SubPlan nodes)
2. Extract template identifier from query filenames
3. Build parent-child relationship map for each query
4. Skip pass-through operators as parents (Hash, Sort, Limit, Incremental Sort, Merge Join)
5. Identify patterns by grouping parent with immediate children (starting from depth 0)
6. Count pattern occurrences per template
7. Export pattern matrix with template breakdown

**Inputs:**
- `input_file` - Path to operator dataset CSV (positional)

**Outputs:**
- `csv/baseline_patterns_depth0plus_{timestamp}.csv`
  - Columns: pattern, leaf_pattern, total, Q1, Q3, Q4, ... (per template)
  - Pattern format: "Parent → [Child1 (Outer), Child2 (Inner)]"
  - Includes root-level patterns (depth 0) in addition to child patterns
  - Hybrid_3: 20 patterns (PT parent patterns excluded)
  - Hybrid_2: 31 patterns (all operators included)

**Usage:**

Baseline Approach (ohne Q2, Q11, Q16, Q22) - **RECOMMENDED for Hybrid_3**:
```bash
python 01_Find_Patterns.py ../../Operator_Level/Datasets/Baseline/04_training.csv --output-dir .
```

All Templates Approach (alle 22 Templates):
```bash
python 01_Find_Patterns.py ../../Operator_Level/Datasets/Raw/operator_dataset_20251102_140747.csv --output-dir .
```

**Variables:**
- `--output-dir` - Output directory for CSV results (required)

---

### 02 - Compare_Patterns.py

**Purpose:** Compare pattern inventories between Hybrid_2 and Hybrid_3 to verify Pass-Through pattern removal

**Workflow:**
1. Load pattern lists from both Hybrid_2 and Hybrid_3 CSV files
2. Identify patterns that exist in Hybrid_2 but not in Hybrid_3
3. Verify removed patterns are Pass-Through parent patterns
4. Report new patterns that appear only in Hybrid_3
5. Print detailed comparison report with verification status

**Inputs:**
- Hardcoded paths to Hybrid_2 and Hybrid_3 pattern CSV files

**Outputs:**
- `md/pattern_comparison_{timestamp}.md`
  - Pattern count summary
  - Removed patterns categorized by PT/Non-PT
  - New patterns in Hybrid_3
  - Verification status

**Usage:**
```bash
python 02_Compare_Patterns.py
```

**Expected Results:**
- Hybrid_2: 31 patterns
- Hybrid_3: 20 patterns
- Removed: 11 PT parent patterns
- New patterns: 0 (when using same baseline dataset)
- All removed patterns should have Pass-Through operators as parents
- PT operators: Hash, Sort, Limit, Incremental Sort, Merge Join

**Actual Results (Baseline Dataset):**
- ✓ 11 PT parent patterns removed (4× Hash, 4× Sort, 1× Incremental Sort, 1× Limit, 1× Merge Join)
- ✓ No new patterns
- ✓ Perfect 31 → 20 pattern reduction
