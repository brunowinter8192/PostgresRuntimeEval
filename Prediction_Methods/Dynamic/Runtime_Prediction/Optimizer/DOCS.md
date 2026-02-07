## Working Directory

**CRITICAL:** All commands assume CWD = `Optimizer/`

```bash
cd /path/to/Dynamic/Runtime_Prediction/Optimizer
```

## Directory Structure

```
Optimizer/
├── DOCS.md
├── 01_Plan_Prediction.py
├── 02_Operator_Prediction.py
├── A_01a_Plan_Evaluation.py
├── A_01b_Operator_Evaluation.py
├── A_02_Overall_Comparison.py
├── A_03a_Plan_Static_Dynamic.py
├── A_03b_Operator_Static_Dynamic.py
├── A_04a_Plan_ML_Optimizer.py
├── A_04b_Operator_ML_Optimizer.py
├── Plan_Level/
│   ├── {Template}/predictions.csv
│   └── loto_mre.csv
└── Operator_Level/
    ├── {Template}/predictions.csv
    └── loto_mre.csv
```

## Workflow Dependency Graph

```
01_Plan_Prediction ──────────> A_01a_Plan_Evaluation ─────┐
                                                          ├──> A_02_Overall_Comparison
02_Operator_Prediction ──────> A_01b_Operator_Evaluation ─┘

A_01a_Plan_Evaluation + External Static CSV ──────> A_03a_Plan_Static_Dynamic
A_01b_Operator_Evaluation + External Static CSV ──> A_03b_Operator_Static_Dynamic

A_01a_Plan_Evaluation + External ML Plan CSV ─────────────────> A_04a_Plan_ML_Optimizer
A_01b_Operator_Evaluation + External ML Operator/Hybrid/Online CSVs ──> A_04b_Operator_ML_Optimizer
```

## Module Documentation

### 01 - Plan_Prediction.py

**Purpose:** Train LinearRegression on `p_tot_cost` to predict query runtime (Plan-Level)

**Inputs:**
- `--dataset-dir`: Path to Dataset_Plan (contains `{Template}/training.csv`, `{Template}/test.csv`)
- `--output-dir`: Output directory for predictions

**Outputs:**
- `{output-dir}/{Template}/predictions.csv`

**Usage:**
```bash
python3 01_Plan_Prediction.py --dataset-dir ../../Dataset/Dataset_Plan --output-dir Plan_Level
```

---

### 02 - Operator_Prediction.py

**Purpose:** Train LinearRegression on root operator `total_cost` to predict query runtime (Operator-Level)

**Inputs:**
- `--dataset-dir`: Path to Dataset_Operator (contains `{Template}/training.csv`, `{Template}/test.csv`)
- `--output-dir`: Output directory for predictions

**Outputs:**
- `{output-dir}/{Template}/predictions.csv`

**Usage:**
```bash
python3 02_Operator_Prediction.py --dataset-dir ../../Dataset/Dataset_Operator --output-dir Operator_Level
```

**Implementation Details:**
- Filters for root operators only (`depth == 0`)
- Uses `total_cost` as feature, `actual_total_time` as target

---

### A_01a - Plan_Evaluation.py

**Purpose:** Calculate MRE statistics for Plan-Level optimizer predictions

**Inputs:**
- `--predictions-dir`: Directory with `{Template}/predictions.csv`
- `--output-dir`: Output directory

**Outputs:**
- `{output-dir}/loto_mre.csv` - MRE per template
- `{output-dir}/A_01a_plan_mre_plot.png`

**Usage:**
```bash
python3 A_01a_Plan_Evaluation.py --predictions-dir Plan_Level --output-dir Plan_Level
```

---

### A_01b - Operator_Evaluation.py

**Purpose:** Calculate MRE statistics for Operator-Level optimizer predictions

**Inputs:**
- `--predictions-dir`: Directory with `{Template}/predictions.csv`
- `--output-dir`: Output directory

**Outputs:**
- `{output-dir}/loto_mre.csv` - MRE per template
- `{output-dir}/A_01b_operator_mre_plot.png`

**Usage:**
```bash
python3 A_01b_Operator_Evaluation.py --predictions-dir Operator_Level --output-dir Operator_Level
```

---

### A_02 - Overall_Comparison.py

**Purpose:** Compare Plan-Level vs Operator-Level optimizer (both Dynamic)

**Inputs:**
- `--plan-csv`: Path to `Plan_Level/loto_mre.csv`
- `--operator-csv`: Path to `Operator_Level/loto_mre.csv`
- `--output-dir`: Output directory

**Outputs:**
- `{output-dir}/A_02_comparison_plot.png`

**Usage:**
```bash
python3 A_02_Overall_Comparison.py --plan-csv Plan_Level/loto_mre.csv --operator-csv Operator_Level/loto_mre.csv --output-dir Plan_Level
python3 A_02_Overall_Comparison.py --plan-csv Plan_Level/loto_mre.csv --operator-csv Operator_Level/loto_mre.csv --output-dir Operator_Level
```

---

### A_03a - Plan_Static_Dynamic.py

**Purpose:** Compare Static vs Dynamic optimizer for Plan-Level

**Inputs:**
- `--static-csv`: External CSV with `template`, `mre_optimizer_pct` columns (from Plan_Level_1)
- `--dynamic-csv`: Path to `Plan_Level/loto_mre.csv`
- `--output-dir`: Output directory

**Outputs:**
- `{output-dir}/A_03a_plan_static_dynamic.png`

**Usage:**
```bash
python3 A_03a_Plan_Static_Dynamic.py \
  --static-csv ../../../Plan_Level_1/Runtime_Prediction/Baseline_SVM/Evaluation/A_01i_optimizer_baseline_template.csv \
  --dynamic-csv Plan_Level/loto_mre.csv \
  --output-dir Plan_Level
```

**Implementation Details:**
- Filters static CSV to 14 TEMPLATES (excludes Q2, Q11, Q16, Q21, Q22)

---

### A_03b - Operator_Static_Dynamic.py

**Purpose:** Compare Static vs Dynamic optimizer for Operator-Level

**Inputs:**
- `--static-csv`: External CSV with `template`, `mre_optimizer_pct` columns (from Operator_Level)
- `--dynamic-csv`: Path to `Operator_Level/loto_mre.csv`
- `--output-dir`: Output directory

**Outputs:**
- `{output-dir}/A_03b_operator_static_dynamic.png`

**Usage:**
```bash
python3 A_03b_Operator_Static_Dynamic.py \
  --static-csv ../../../Operator_Level/Runtime_Prediction/Baseline_SVM/Evaluation/A_01h_optimizer_baseline_template.csv \
  --dynamic-csv Operator_Level/loto_mre.csv \
  --output-dir Operator_Level
```

---

### A_04a - Plan_ML_Optimizer.py

**Purpose:** Compare Plan-Level ML vs Optimizer on dynamic workloads

**Inputs:**
- `--optimizer-csv`: Path to `Plan_Level/loto_mre.csv`
- `--ml-csv`: Path to Plan-Level ML loto_mre CSV
- `--output-dir`: Output directory

**Outputs:**
- `{output-dir}/A_04a_plan_ml_optimizer.png`

**Usage:**
```bash
python3 A_04a_Plan_ML_Optimizer.py \
  --optimizer-csv Plan_Level/loto_mre.csv \
  --ml-csv ../../Plan_Level/Evaluation/loto_mre.csv \
  --output-dir Plan_Level
```

---

### A_04b - Operator_ML_Optimizer.py

**Purpose:** Compare Operator-Level ML methods (Operator, Hybrid_1, Online_1) vs Optimizer on dynamic workloads

**Inputs:**
- `--optimizer-csv`: Path to `Operator_Level/loto_mre.csv`
- `--operator-csv`: Path to Operator-Level ML loto_mre CSV
- `--hybrid-csv`: Path to Hybrid_1 loto_mre CSV
- `--online-csv`: Path to Online_1 loto_mre CSV
- `--output-dir`: Output directory

**Outputs:**
- `{output-dir}/A_04b_operator_ml_optimizer.png`

**Usage:**
```bash
python3 A_04b_Operator_ML_Optimizer.py \
  --optimizer-csv Operator_Level/loto_mre.csv \
  --operator-csv ../../Operator_Level/Evaluation/loto_mre.csv \
  --hybrid-csv ../../Hybrid_1/Evaluation/approach_3/loto_mre.csv \
  --online-csv ../../Online_1/Evaluation/Analysis/Size/loto_mre.csv \
  --output-dir Operator_Level
```

## External Dependencies

**Static Optimizer Baselines (from other workflows):**
- Plan_Level_1: `Prediction_Methods/Plan_Level_1/Runtime_Prediction/Baseline_SVM/Evaluation/A_01i_optimizer_baseline_template.csv`
- Operator_Level: `Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Evaluation/A_01h_optimizer_baseline_template.csv`

**ML loto_mre CSVs (from Dynamic workflows):**
- Plan_Level ML: `Dynamic/Runtime_Prediction/Plan_Level/Evaluation/loto_mre.csv`
- Operator_Level ML: `Dynamic/Runtime_Prediction/Operator_Level/Evaluation/loto_mre.csv`
- Hybrid_1 ML: `Dynamic/Runtime_Prediction/Hybrid_1/Evaluation/approach_3/loto_mre.csv`
- Online_1 ML: `Dynamic/Runtime_Prediction/Online_1/Evaluation/Analysis/Size/loto_mre.csv`

## Templates

All scripts use 14 templates:
`Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q18, Q19`

Excluded from Dynamic (no LOTO data): Q2, Q11, Q16, Q21, Q22
