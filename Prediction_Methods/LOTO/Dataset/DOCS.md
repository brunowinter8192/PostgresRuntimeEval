# Dataset - DOCS.md

LOTO (Leave-One-Template-Out) dataset preparation for dynamic workload evaluation.

---

## Directory Structure

```
Dataset/
├── DOCS.md
├── 00_Clean_Dataset.py
│   ├── clean_workflow()
│   ├── load_dataset()
│   ├── filter_templates()
│   └── export_cleaned()
├── 01_Split_Dataset.py
│   ├── split_workflow()
│   ├── load_dataset()
│   ├── get_unique_templates()
│   └── create_splits()
├── cleaned_dataset.csv
└── Q1/, Q3/, Q4/, Q5/, Q6/, Q7/, Q8/, Q9/, Q10/, Q12/, Q13/, Q14/, Q18/, Q19/
    ├── training.csv
    └── test.csv
```

---

## LOTO Methodology

Based on paper Section 5.4 "Dynamic Workload": Train on N-1 templates, test on the held-out template. This evaluates generalization to unseen query structures.

**Excluded Templates:** Q2, Q11, Q16, Q21, Q22
- Reason: Contain InitPlans/SubPlans requiring separate modeling approach

**Resulting Templates:** 14 (Q1, Q3-Q10, Q12-Q14, Q18, Q19)
- Per template: 150 queries in test.csv, 1950 queries in training.csv

---

## 00_Clean_Dataset.py

**Purpose:** Filter complete dataset to exclude templates with InitPlans/SubPlans.

**Input:** complete_dataset.csv (positional)

**Output:** cleaned_dataset.csv in --output-dir

**Usage:**
```bash
python3 00_Clean_Dataset.py ../complete_dataset.csv --output-dir .
```

### clean_workflow()
Orchestrator that coordinates dataset cleaning. Loads data, filters templates, exports result.

### load_dataset()
Loads dataset from CSV with semicolon delimiter. Returns DataFrame.

### filter_templates()
Removes rows where template is in EXCLUDE_TEMPLATES (Q2, Q11, Q16, Q21, Q22). Returns filtered DataFrame.

### export_cleaned()
Saves cleaned dataset to output directory as cleaned_dataset.csv with semicolon delimiter.

---

## 01_Split_Dataset.py

**Purpose:** Create LOTO train/test splits for each template.

**Input:** cleaned_dataset.csv (positional)

**Output:** QX/training.csv and QX/test.csv per template in --output-dir

**Usage:**
```bash
python3 01_Split_Dataset.py cleaned_dataset.csv --output-dir .
```

### split_workflow()
Orchestrator that coordinates LOTO splitting. Loads data, gets templates, creates all splits.

### load_dataset()
Loads dataset from CSV with semicolon delimiter. Returns DataFrame.

### get_unique_templates()
Extracts sorted list of unique template values from DataFrame.

### create_splits()
For each template: creates directory, exports test.csv (only this template) and training.csv (all other templates).

---

## Output Structure

| Path | Content |
|------|---------|
| `cleaned_dataset.csv` | 2100 rows (14 templates x 150 queries) |
| `QX/test.csv` | 150 rows (only template QX) |
| `QX/training.csv` | 1950 rows (all templates except QX) |
