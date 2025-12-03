# Dataset_Operator - DOCS.md

LOTO (Leave-One-Template-Out) dataset preparation at operator granularity for bottom-up prediction.

---

## Directory Structure

```
Dataset_Operator/
├── DOCS.md
├── 01_Split_Operators.py
└── Q1/, Q3/, ... Q22/
    ├── training.csv
    └── test.csv
```

---

## Difference from Dataset/ (Plan-Level)

| Aspect | Dataset/ (Plan-Level) | Dataset_Operator/ |
|--------|----------------------|-------------------|
| Granularity | 1 row per query | Multiple rows per query (1 per operator) |
| Features | Plan-aggregated (p_st_cost, Aggregate_cnt, ...) | Operator-level (node_type, startup_cost, st1, rt1, ...) |
| Source | Plan_Level complete_dataset.csv | Operator_Level 02_operator_dataset_with_children.csv |

---

## 01_Split_Operators.py

**Purpose:** Create LOTO splits at operator granularity from existing operator dataset.

**Input:** Operator_Level/Datasets/Baseline/02_operator_dataset_with_children.csv (positional)

**Output:** QX/training.csv and QX/test.csv per template in --output-dir

**Usage:**
```bash
python3 01_Split_Operators.py \
  ../../Operator_Level/Datasets/Baseline/02_operator_dataset_with_children.csv \
  --output-dir .
```

### split_workflow()
Orchestrator that coordinates LOTO splitting. Loads data, adds template column, creates all splits.

### load_dataset()
Loads operator dataset from CSV with semicolon delimiter. Returns DataFrame.

### add_template_column()
Extracts template from query_file column (Q1_001 -> Q1) and adds as new column.

### extract_template()
Parses query filename to extract template ID using regex pattern (Q\d+)_.

### get_unique_templates()
Extracts sorted list of unique template values from DataFrame.

### create_splits()
For each template: creates directory, exports test.csv (only this template's operators) and training.csv (all other templates' operators). Drops temporary template column before export.

---

## Output Structure

| Path | Content |
|------|---------|
| `QX/test.csv` | All operator rows from template QX queries |
| `QX/training.csv` | All operator rows from all other templates |

**Columns (22):** query_file, node_id, node_type, depth, parent_relationship, subplan_name, np, nt, nt1, nt2, sel, startup_cost, total_cost, plan_width, reltuples, parallel_workers, actual_startup_time, actual_total_time, st1, rt1, st2, rt2
