# Dynamic

Runtime prediction for dynamic workloads using Leave-One-Template-Out (LOTO) cross-validation.

**Note:** This README does not fully follow CLAUDE.md standards. Dynamic contains multiple independent sub-workflows (Plan_Level, Operator_Level, Hybrid) that share Dataset infrastructure. Each sub-workflow is documented separately below.

## Directory Structure

```
Dynamic/
├── README.md
├── Data_Generation/                             [See DOCS.md]
├── Dataset/                                     [See DOCS.md]
│   ├── Dataset_Operator/
│   ├── Dataset_Plan/
│   └── Dataset_Hybrid_1/
└── Runtime_Prediction/                          [See DOCS.md]
    ├── Operator_Level/
    ├── Plan_Level/
    └── Hybrid_1/
```

## Shared Configuration

**14 Templates (LOTO):**
```
Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q18, Q19
```

**LOTO Principle:** For each template Qx, train on all other templates (13), test on Qx.

---

## Plan_Level Workflow

Plan-level runtime prediction using aggregated query features.

### Pipeline

```
Dataset/Dataset_Plan/01_LOTO_Split.py
            |
            v
    Q1/, Q3/, ... Q19/
    (training.csv + test.csv)
            |
            v
Runtime_Prediction/Plan_Level/00_Batch_Workflow.py
            |
            v
    Q1/, Q3/, ... Q19/
    (SVM/ + 02_predictions_*.csv)
```

### Step 1: LOTO Split

**Script:** `Dataset/Dataset_Plan/01_LOTO_Split.py`

**Input:** `Plan_Level_1/Data_Generation/csv/complete_dataset.csv`

**Output:** 14 template directories with `training.csv` and `test.csv`

```bash
cd Dataset/Dataset_Plan
python3 01_LOTO_Split.py ../../../Plan_Level_1/Data_Generation/csv/complete_dataset.csv --output-dir .
```

### Step 2: Batch Workflow (FFS + Train)

**Script:** `Runtime_Prediction/Plan_Level/00_Batch_Workflow.py`

**Dependency:** Uses scripts from `Plan_Level_1/Runtime_Prediction/` via subprocess

**Output per Template:**
- `Qx/SVM/01_ffs_summary.csv` - Feature selection results
- `Qx/SVM/01_ffs_stability.csv` - Feature stability
- `Qx/02_model_*.pkl` - Trained SVM model
- `Qx/02_predictions_*.csv` - Predictions on test set

```bash
cd Runtime_Prediction/Plan_Level
python3 00_Batch_Workflow.py
```

---

## Operator_Level Workflow

(Documentation pending)

---

## Hybrid_1 Workflow

Pattern-based hybrid prediction combining operator-level and pattern-level models.

### Pipeline

```
Dataset/Dataset_Hybrid_1/01_Batch_Extract_Patterns.py
            |
            v
    Q1/, Q3/, ... Q19/
    (patterns.csv + patterns/)
            |
            v
Dataset/Dataset_Hybrid_1/00_Dry_Prediction.py
            |
            v
    Q1/.../used_patterns.csv + md/00_dry_prediction_report.md
            |
            v
Runtime_Prediction/Hybrid_1/01_Batch_Hybrid_Prediction.py
            |
            v
    Q1/, Q3/, ... Q19/
    (SVM/ + Model/ + predictions)
```

### Step 1: Extract Patterns

**Script:** `Dataset/Dataset_Hybrid_1/01_Batch_Extract_Patterns.py`

**Input:** `Dataset/Dataset_Operator/Qx/training.csv`

**Output per Template:** `Qx/approach_3/patterns.csv` + `patterns/` folder

```bash
cd Dataset/Dataset_Hybrid_1
python3 01_Batch_Extract_Patterns.py
```

### Step 2: Dry Prediction (Pattern Filtering)

**Script:** `Dataset/Dataset_Hybrid_1/00_Dry_Prediction.py`

**Purpose:** Identifies which patterns are actually used for test data prediction (reduces FFS workload by ~90%)

**Input:** `Dataset/Dataset_Operator/Qx/test.csv` + `patterns.csv`

**Output per Template:**
- `Qx/approach_3/used_patterns.csv` - Pattern hashes that match test queries
- `Qx/approach_3/md/00_dry_prediction_report.md` - Statistics report

```bash
cd Dataset/Dataset_Hybrid_1
python3 00_Dry_Prediction.py
```

### Step 3: Batch Hybrid Prediction (FFS + Train + Predict)

**Script:** `Runtime_Prediction/Hybrid_1/01_Batch_Hybrid_Prediction.py`

**Dependency:** Uses scripts from `Hybrid_1/Runtime_Prediction/` via subprocess

**Output per Template:**
- `Qx/approach_3/SVM/two_step_evaluation_overview.csv` - FFS results
- `Qx/approach_3/Model/` - Trained pattern models
- Predictions on test set

```bash
cd Runtime_Prediction/Hybrid_1
python3 01_Batch_Hybrid_Prediction.py
```
