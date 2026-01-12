# Dynamic - LOTO Cross-Validation Workflows

Runtime prediction workflows for dynamic LOTO (Leave-One-Template-Out) workloads.

## LOTO Cross-Validation

**LOTO = Leave-One-Template-Out:** Ein komplettes Template ist für Test reserviert, alle anderen für Training.

**Datenaufteilung pro LOTO-Fold:**
- **Training:** 13 Templates (je 150 Queries = 1950 total)
- **Test:** 1 Template (150 Queries) - vollständig ungesehen

**14 LOTO-Templates:** Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q18, Q19

Gegensatz: [Static Workloads](../README.md) - Train/Test sehen gleiche Templates

## Directory Structure

```
Dynamic/
    mapping_config.py
    README.md
    Dataset/
        Dataset_Operator/            [See DOCS.md](Dataset/Dataset_Operator/DOCS.md)
        Dataset_Plan/                [See DOCS.md](Dataset/Dataset_Plan/DOCS.md)
        Dataset_Hybrid_1/            [See DOCS.md](Dataset/Dataset_Hybrid_1/DOCS.md)
        Dataset_Hybrid_2/            [See DOCS.md](Dataset/Dataset_Hybrid_2/DOCS.md)
    Data_Generation/
        Hybrid_1/                    [See DOCS.md](Data_Generation/Hybrid_1/DOCS.md)
    Runtime_Prediction/
        Operator_Level/              [See DOCS.md](Runtime_Prediction/Operator_Level/DOCS.md)
        Plan_Level/                  [See DOCS.md](Runtime_Prediction/Plan_Level/DOCS.md)
        Hybrid_1/                    [See DOCS.md](Runtime_Prediction/Hybrid_1/DOCS.md)
        Online_1/                    [See DOCS.md](Runtime_Prediction/Online_1/DOCS.md)
```

## Workflows

### Operator_Level

Operator-level prediction: Laufzeit jedes Query-Operators einzeln prognostizieren und bottom-up zur Query-Gesamtzeit aggregieren.

**Quick Reproduction:**
```bash
cd Dataset/Dataset_Operator
python3 01_LOTO_Split.py ../../Operator_Level/Datasets/Baseline/02_operator_dataset_with_children.csv --output-dir .

cd ../../Runtime_Prediction/Operator_Level
python3 00_Batch_Workflow.py
```

**Details:** [Runtime_Prediction/Operator_Level/DOCS.md](Runtime_Prediction/Operator_Level/DOCS.md)

---

### Plan_Level

Plan-level prediction: Query-Laufzeit direkt aus aggregierten Plan-Features (Summen, Counts, Struktur) ohne Operator-Zerlegung.

**Quick Reproduction:**
```bash
cd Dataset/Dataset_Plan
python3 01_LOTO_Split.py ../../Plan_Level_1/Data_Generation/csv/complete_dataset.csv --output-dir .

cd ../../Runtime_Prediction/Plan_Level
python3 00_Batch_Workflow.py
```

**Details:** [Runtime_Prediction/Plan_Level/DOCS.md](Runtime_Prediction/Plan_Level/DOCS.md)

---

### Hybrid_1

Pattern-based prediction: Pattern-Level Modelle (Parent + Children als Einheit) mit Operator-Level Fallback. Patterns offline aus Training-Daten extrahiert.

**Quick Reproduction:**
```bash
cd Data_Generation/Hybrid_1
python3 00_Batch_Mine_Patterns.py

cd ../../Dataset/Dataset_Hybrid_1
python3 01_Batch_Extract_Patterns.py
python3 00_Dry_Prediction.py

cd ../../Runtime_Prediction/Hybrid_1
python3 01_Batch_Hybrid_Prediction.py
```

**Details:** [Runtime_Prediction/Hybrid_1/DOCS.md](Runtime_Prediction/Hybrid_1/DOCS.md)

---

### Online_1

Online pattern selection: Pattern-Mining und Greedy Selection zur Query-Zeit. Patterns online aus Test-Query extrahiert.

**Quick Reproduction:**
```bash
cd Runtime_Prediction/Online_1
./batch_predict.sh

python3 A_01a_Query_Evaluation.py Evaluation/Size --output-dir Evaluation/Analysis/Size
python3 A_02_Pattern_Analysis.py Evaluation/Size --output-dir Evaluation/Analysis/Size
```

**Details:** [Runtime_Prediction/Online_1/DOCS.md](Runtime_Prediction/Online_1/DOCS.md)
