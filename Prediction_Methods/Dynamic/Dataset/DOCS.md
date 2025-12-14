# Dataset - DOCS

**Note:** This DOCS.md covers all dataset scripts at root level. Not CLAUDE.md compliant (should be per-directory), but avoids overengineering for simple batch wrappers.

---

## Working Directory

**CRITICAL:** All commands assume CWD = `Dataset/`

```bash
cd /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Dynamic/Dataset
```

---

## Directory Structure

```
Dataset/
├── DOCS.md
├── Dataset_Operator/
│   ├── 01_LOTO_Split.py
│   └── Q1/, Q3/, ... Q19/
│       ├── 04a_{Operator}/04a_{Operator}.csv
│       ├── training.csv
│       └── test.csv
└── Dataset_Plan/
    ├── 01_LOTO_Split.py
    └── Q1/, Q3/, ... Q19/
        ├── training.csv
        └── test.csv
```

---

## Dataset_Operator/01_LOTO_Split.py

**Purpose:** Create LOTO (Leave-One-Template-Out) splits with operator-level structure for all 14 templates.

**Input:**
- `input_file`: `/Operator_Level/Datasets/Baseline/02_operator_dataset_with_children.csv`

**Output per Template:**
- `Qx/training.csv` - All operators from 13 other templates
- `Qx/test.csv` - All operators from held-out template
- `Qx/04a_{Operator}/04a_{Operator}.csv` - Training data split by node_type

**Usage:**
```bash
cd Dataset_Operator
python3 01_LOTO_Split.py \
    /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Operator_Level/Datasets/Baseline/02_operator_dataset_with_children.csv \
    --output-dir .
```

**Templates:** Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q18, Q19

**LOTO Logic:**
- Template Qx as test set (150 queries worth of operators)
- All other templates as training set (1950 queries worth of operators)
- Training data additionally split into operator folders for FFS/Training scripts

---

## Dataset_Plan/01_LOTO_Split.py

**Purpose:** Create LOTO (Leave-One-Template-Out) splits at plan-level for all 14 templates.

**Input:**
- `input_file`: `/Plan_Level_1/Data_Generation/csv/complete_dataset.csv`

**Output per Template:**
- `Qx/training.csv` - All queries from 13 other templates
- `Qx/test.csv` - All queries from held-out template

**Usage:**
```bash
cd Dataset_Plan
python3 01_LOTO_Split.py \
    ../../../Plan_Level_1/Data_Generation/csv/complete_dataset.csv \
    --output-dir .
```

**Templates:** Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q18, Q19

**LOTO Logic:**
- Template Qx as test set (150 queries)
- All other templates as training set (1950 queries)
- No operator-level split (plan-level aggregation)

---

## Dataset_Hybrid_1/01_Batch_Extract_Patterns.py

**Purpose:** Extract patterns from training data for all 14 LOTO templates using Hybrid_1 scripts.

**Approach 4 Configuration:**
```python
APPROACHES = {
    'approach_4': {'length': 0, 'required_operators': False, 'no_passthrough': True, 'threshold': 120},
}
```

**Input:**
- `Dataset_Operator/Qx/training.csv` (from 01_LOTO_Split.py)

**Output per Template:**
- `Qx/approach_4/patterns.csv` - Pattern inventory
- `Qx/approach_4/patterns/{hash}/` - Pattern folders with training data
- `Qx/approach_4/patterns_filtered.csv` - Patterns after threshold filter

**Usage:**
```bash
cd Dataset_Hybrid_1
python3 01_Batch_Extract_Patterns.py
```

**Subprocess Calls:**
1. `Hybrid_1/Datasets/03_Extract_Patterns.py` - Extract patterns with `--no-passthrough`
2. `Hybrid_1/Datasets/04_Aggregate_Patterns.py` - Aggregate parent+children
3. `Hybrid_1/Datasets/05_Clean_Patterns.py` - Remove unavailable features
4. `Hybrid_1/Datasets/06_Filter_Patterns.py` - Apply threshold filter

---

## Dataset_Hybrid_1/00_Dry_Prediction.py

**Purpose:** Simulate pattern assignment on test queries to identify which patterns are actually used. Pre-filters patterns before FFS to reduce workload by 90-99%.

**Input:**
- `Dataset_Operator/Qx/test.csv`
- `Qx/approach_4/patterns.csv` or `patterns_filtered.csv`

**Output per Template:**
- `Qx/approach_4/used_patterns.csv` - Pattern hashes that match test query structures
- `Qx/approach_4/md/00_dry_prediction_report.md` - Statistics (patterns available vs used, reduction %)

**Usage:**
```bash
cd Dataset_Hybrid_1
python3 00_Dry_Prediction.py
```

**Algorithm:**
1. For each unique plan structure in test data
2. Build query tree and apply pattern matching (longest patterns first)
3. Collect which patterns are assigned to nodes
4. Export only those pattern hashes

**Reduction Examples:**
| Template | Available | Used | Reduction |
|----------|-----------|------|-----------|
| Q1 | 190 | 2 | 98.9% |
| Q9 | 151 | 10 | 93.4% |
