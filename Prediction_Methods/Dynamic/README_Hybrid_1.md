# Dynamic Hybrid_1 Workflow

Pattern-based runtime prediction for dynamic LOTO workloads.

**Basiert auf:** [Static Hybrid_1](../Hybrid_1/README.md) - adaptiert für LOTO Cross-Validation.

## Dynamic Workload (LOTO)

**LOTO = Leave-One-Template-Out:** Ein komplettes Template ist für Test reserviert, alle anderen für Training.

**Datenaufteilung pro LOTO-Fold:**
- **Training:** 13 Templates (je 150 Queries = 1950 total)
- **Test:** 1 Template (150 Queries) - vollständig ungesehen

**14 LOTO-Templates:** Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q18, Q19

Gegensatz: [Static Workloads](../Hybrid_1/README.md) - Train/Test sehen gleiche Templates

## Konzept

Hybrid_1 kombiniert Pattern-Level und Operator-Level Modelle:
- **Pattern-Level:** Gruppiert Parent + Children als Vorhersage-Einheit
- **Operator-Level:** Fallback für Operatoren ohne Pattern-Match

### Pattern-Filterung (2 Stufen)

1. **Threshold (150):** Nur Patterns mit genug Training-Samples für valide Modelle
2. **Dry Prediction:** Nur Patterns die auf Test-Queries tatsächlich zugewiesen werden

Beide Filter sind notwendig:
- Threshold sichert Modellqualität
- Dry Prediction reduziert FFS/Training-Aufwand (typisch 90-99% Reduktion)

## Directory Structure

```
Dynamic/
├── Data_Generation/
│   └── Hybrid_1/                    [See DOCS.md]
├── Dataset/
│   └── Dataset_Hybrid_1/            [See DOCS.md]
└── Runtime_Prediction/
    └── Hybrid_1/                    [See DOCS.md]
```

## Workflow

### Phase 1: Data_Generation

**Purpose:** Mine patterns with occurrence counts from training data

**Input:** `Dataset/Dataset_Operator/{Q*}/training.csv`

**Output:** `Data_Generation/Hybrid_1/{Q*}/csv/01_patterns_*.csv`

**Details:** [Data_Generation/Hybrid_1/DOCS.md](Data_Generation/Hybrid_1/DOCS.md)

### Phase 2: Dataset

**Purpose:** Extract, filter and prepare pattern training datasets

**Input:**
- `Dataset/Dataset_Operator/{Q*}/training.csv`
- `Data_Generation/Hybrid_1/{Q*}/csv/01_patterns_*.csv` (occurrence counts)

**Output:** `Dataset/Dataset_Hybrid_1/{Q*}/approach_4/`
- `patterns_filtered.csv` - Patterns meeting threshold
- `used_patterns.csv` - Patterns actually assigned
- `patterns/{hash}/training_cleaned.csv` - Training data per pattern

**Details:** [Dataset/Dataset_Hybrid_1/DOCS.md](Dataset/Dataset_Hybrid_1/DOCS.md)

### Phase 3: Runtime_Prediction

**Purpose:** FFS, model training, and hybrid prediction

**Input:** Pattern and operator training datasets from Phase 2

**Output:** Predictions per template

**Details:** [Runtime_Prediction/Hybrid_1/DOCS.md](Runtime_Prediction/Hybrid_1/DOCS.md)

## Quick Reproduction

```bash
# Phase 1: Mine patterns
cd Data_Generation/Hybrid_1
python3 00_Batch_Mine_Patterns.py

# Phase 2: Extract + Filter + Dry Prediction
cd ../../Dataset/Dataset_Hybrid_1
python3 01_Batch_Extract_Patterns.py
python3 00_Dry_Prediction.py

# Phase 3: FFS + Train + Predict
cd ../../Runtime_Prediction/Hybrid_1
python3 01_Batch_Hybrid_Prediction.py
```

## Approach Definitions

**Vergleich Static vs. Dynamic:**

| Approach | Filter | Static Patterns | Dynamic Patterns |
|----------|--------|-----------------|------------------|
| approach_3 | none | 372 (fix) | variiert pro LOTO-Fold |
| approach_4 | no_passthrough | 191 (fix) | variiert pro LOTO-Fold |

**LOTO-spezifisch:** In Dynamic ist je ein Template komplett im Test. Die Training-Daten enthalten nur 13 Templates, daher variiert die Pattern-Anzahl pro Fold.

**approach_3:**
- `no_passthrough: False` - Keine Filter auf Passthrough-Operatoren
- `length: 0` - Alle Pattern-Längen
- `threshold: 150` - Min. Occurrences für Modellqualität

**approach_4:**
- `no_passthrough: True` - Exclude Passthrough-Operatoren als Root
- `length: 0` - Alle Pattern-Längen
- `threshold: 150` - Min. Occurrences für Modellqualität

**14 LOTO Templates:**
```
Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q18, Q19
```

## Evaluation

```bash
cd Runtime_Prediction/Hybrid_1
python3 A_01a_Query_Evaluation.py approach_3 --output-dir Evaluation/approach_3
```

Output: MRE pro LOTO-Template + Gesamt-MRE + Bar Plot
