# Dynamic Operator_Level Workflow

Operator-level runtime prediction for dynamic LOTO workloads.

**Basiert auf:** [Static Operator_Level](../../Operator_Level/README.md) - adaptiert für LOTO Cross-Validation.

## Dynamic Workload (LOTO)

**LOTO = Leave-One-Template-Out:** Ein komplettes Template ist für Test reserviert, alle anderen für Training.

**Datenaufteilung pro LOTO-Fold:**
- **Training:** 13 Templates (je 150 Queries = 1950 total)
- **Test:** 1 Template (150 Queries) - vollständig ungesehen

**14 LOTO-Templates:** Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q18, Q19

Gegensatz: [Static Workloads](../../Operator_Level/README.md) - Train/Test sehen gleiche Templates

## Konzept

Operator_Level prognostiziert die Laufzeit jedes Query-Operators einzeln und aggregiert bottom-up zur Query-Gesamtzeit.

### LOTO-spezifisch

LOTO-Splits können nicht alle 13 Operatoren enthalten. Beispiel: `Index_Only_Scan` existiert nur in Q13. Wenn Q13 als Test gehalten wird, fehlt dieser Operator in den Training-Daten.

Das lokale `01_Forward_Selection.py` Script iteriert daher über **verfügbare** Operator-Ordner statt über eine fixe Liste.

## Directory Structure

```
Dynamic/
├── Dataset/
│   └── Dataset_Operator/           [See DOCS.md]
└── Runtime_Prediction/
    └── Operator_Level/             [See DOCS.md]
```

## Workflow

### Phase 1: Dataset

**Purpose:** Create LOTO splits with operator-level structure

**Input:** `/Operator_Level/Datasets/Baseline/02_operator_dataset_with_children.csv`

**Output:** `Dataset_Operator/Qx/{training.csv, test.csv, 04a_{Operator}/}`

**Details:** [Dataset/Dataset_Operator/DOCS.md](Dataset/Dataset_Operator/DOCS.md)

### Phase 2: Runtime_Prediction

**Purpose:** FFS, model training, and bottom-up prediction

**Input:** LOTO operator datasets from Phase 1

**Output:** Predictions per template

**Details:** [Runtime_Prediction/Operator_Level/DOCS.md](Runtime_Prediction/Operator_Level/DOCS.md)

## Quick Reproduction

```bash
# Phase 1: Create LOTO splits
cd Dataset/Dataset_Operator
python3 01_LOTO_Split.py \
    Prediction_Methods/Operator_Level/Datasets/Baseline/02_operator_dataset_with_children.csv \
    --output-dir .

# Phase 2: FFS + Train + Predict
cd ../../Runtime_Prediction/Operator_Level
python3 00_Batch_Workflow.py
```

## 14 LOTO Templates

```
Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q18, Q19
```
