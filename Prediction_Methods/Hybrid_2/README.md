# Hybrid_2 - Pattern-Level Prediction

Pattern-based query runtime prediction using greedy pattern selection. Combines operator-level models with pattern-level models for improved accuracy.

## Directory Structure

```
Hybrid_2/
    mapping_config.py                    Shared config (self-documenting)
    Parameter.md
    README.md
    Data_Generation/                     [See DOCS.md](Data_Generation/DOCS.md)
    Dataset/                             [See DOCS.md](Dataset/DOCS.md)
    Runtime_Prediction/                  [See DOCS.md](Runtime_Prediction/DOCS.md)
```

## Directories

Die drei Unterordner sind konzeptionelle Abgrenzungen, keine lineare Pipeline.

### Dataset

**Purpose:** Split data, extract pattern occurrences, and prepare training sets.

**Input:** Hybrid_1 baseline data + Pattern definitions from Data_Generation

**Output:** Train/Test splits, Operator splits, Pattern datasets

**Details:** [Dataset/DOCS.md](Dataset/DOCS.md)

---

### Data_Generation

**Purpose:** Mine structural patterns from query execution plans.

**Input:** Operator dataset (from Dataset/Baseline/)

**Output:** Pattern definitions (`01_patterns.csv`)

**Details:** [Data_Generation/DOCS.md](Data_Generation/DOCS.md)

---

### Runtime_Prediction

**Purpose:** Model training, pattern selection, and prediction.

**Input:** Pattern datasets + Operator/Pattern FFS features (from Hybrid_1)

**Output:** Predictions with evaluation metrics

**Details:** [Runtime_Prediction/DOCS.md](Runtime_Prediction/DOCS.md)

---

## Workflow

Die Ausführungsreihenfolge ist nicht identisch mit der Ordnerstruktur.

```
Dataset/01_Split_Data.py
         |
         v
    +----+----+
    |         |
    v         v
Dataset/    Data_Generation/
02a         01_Find_Patterns.py
    |         |
    v         v
Operators/  01_patterns.csv
              |
              v
         Dataset/02b,03,04
              |
              v
         Patterns/{hash}/
              |
              v
         Runtime_Prediction/*
```

**Schritt-für-Schritt:**

1. `Dataset/01_Split_Data.py` - Daten von Hybrid_1 kopieren und splitten
2. Parallel:
   - `Dataset/02a_Split_Operators.py` - Operator-Splits erstellen
   - `Data_Generation/01_Find_Patterns.py` - Patterns aus Plänen extrahieren
3. `Dataset/02b_Extract_Patterns.py` - Pattern-Vorkommen finden (braucht 01_patterns.csv)
4. `Dataset/03_Aggregate_Patterns.py` - Zu Feature-Vektoren aggregieren
5. `Dataset/04_Clean_Patterns.py` - Nicht-vorhersagbare Features entfernen
6. `Runtime_Prediction/*` - Modelltraining und Evaluation
