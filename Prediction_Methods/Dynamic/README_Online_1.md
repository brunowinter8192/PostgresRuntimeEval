# Dynamic Online_1 Workflow

Online pattern selection for dynamic LOTO workloads.

**Basiert auf:** [Static Online_1](../Online_1/README.md) - adaptiert für LOTO Cross-Validation.

## Dynamic Workload (LOTO)

**LOTO = Leave-One-Template-Out:** Ein komplettes Template ist für Test reserviert, alle anderen für Training.

**Datenaufteilung pro LOTO-Fold:**
- **Training:** 13 Templates (je 150 Queries = 1950 total)
- **Test:** 1 Template (150 Queries) - vollständig ungesehen

**14 LOTO-Templates:** Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q18, Q19

Gegensatz: [Static Workloads](../Online_1/README.md) - Train/Test sehen gleiche Templates

## Konzept

Online_1 führt Pattern-Mining und -Selektion zur Query-Zeit durch:
- **Pattern Mining:** Patterns werden aus der Test-Query extrahiert (depth 2-6)
- **Pattern Ranking:** Sortiert nach Strategie (error, size, frequency)
- **Greedy Selection:** Iterativ Patterns hinzufügen wenn sie MRE verbessern
- **Operator Fallback:** Operatoren ohne Pattern-Match nutzen Operator-Modelle

### Unterschied zu Hybrid_1/Hybrid_2

- **Hybrid:** Patterns werden offline aus Training-Daten extrahiert
- **Online:** Patterns werden online aus der Test-Query extrahiert

## Directory Structure

```
Dynamic/
├── Dataset/
│   ├── Dataset_Hybrid_2/            (Training_Training, Training_Test)
│   └── Dataset_Operator/            (training, test)
└── Runtime_Prediction/
    └── Online_1/                    [See DOCS.md](Runtime_Prediction/Online_1/DOCS.md)
```

## Workflow

### Phase 1: Runtime_Prediction

**Purpose:** Online prediction workflow per test query

**Input:**
- `Dataset/Dataset_Hybrid_2/Training_Training/{Q}/Training_Training.csv` - Pattern selection training
- `Dataset/Dataset_Hybrid_2/Training_Training/{Q}/Training_Test.csv` - Pattern selection validation
- `Dataset/Dataset_Operator/{Q}/training.csv` - Final model training
- `Dataset/Dataset_Operator/{Q}/test.csv` - Final prediction

**Output:** Predictions, selection logs, trained models, reports per query

**Details:** [Runtime_Prediction/Online_1/DOCS.md](Runtime_Prediction/Online_1/DOCS.md)

## Quick Reproduction

```bash
# Run all templates with size strategy
cd Runtime_Prediction/Online_1
./batch_predict.sh

# Evaluate results
python3 A_01a_Query_Evaluation.py Evaluation/Size --output-dir Evaluation/Analysis/Size
python3 A_02_Pattern_Analysis.py Evaluation/Size --output-dir Evaluation/Analysis/Size
```

## Strategies

- **error:** Rank by `occurrence_count × avg_mre` (default)
- **size:** Rank by `pattern_length` (larger patterns first)
- **frequency:** Rank by `occurrence_count` (more frequent patterns first)

## 14 LOTO Templates

```
Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q18, Q19
```

## Evaluation

```bash
cd Runtime_Prediction/Online_1
python3 A_01a_Query_Evaluation.py Evaluation/Size --output-dir Evaluation/Analysis/Size
```

Output: MRE pro LOTO-Template + Gesamt-MRE + Bar Plot
