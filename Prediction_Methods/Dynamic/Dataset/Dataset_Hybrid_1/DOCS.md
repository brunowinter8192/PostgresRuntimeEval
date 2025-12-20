# Dataset_Hybrid_1

Pattern dataset preparation for Dynamic LOTO Hybrid_1 workflow.

## Basis: Static Hybrid_1

**Übernommen von** `Hybrid_1/Datasets/`:
- `03_Extract_Patterns.py` - Pattern extraction
- `04_Aggregate_Patterns.py` - Parent+Children aggregation
- `05_Clean_Patterns.py` - Feature cleanup
- `06_Filter_Patterns.py` - Occurrence threshold filter

**Neu in Dynamic:**
- `01_Batch_Extract_Patterns.py` - Batch wrapper für LOTO templates
- `00_Dry_Prediction.py` - Pre-filter auf tatsächlich genutzte Patterns

## Working Directory

**CRITICAL:** All commands assume CWD = `Dataset/Dataset_Hybrid_1/`

```bash
cd /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Dynamic/Dataset/Dataset_Hybrid_1
```

## Konzept

**Pattern Pool:** Verwendet Static Hybrid_1 patterns (372) als gemeinsame Referenz.

Pattern-Filterung erfolgt in zwei Stufen:

1. **Threshold-Filter (150)** → Nur Patterns mit genug Trainingsdaten (aus Static Pool)
2. **Dry Prediction** → Welche Patterns werden auf Test-Queries tatsächlich zugewiesen

Nur Patterns die BEIDE Kriterien erfüllen werden trainiert:
- **Threshold:** Genug Samples für statistisch valide Modelle
- **Dry Prediction:** Tatsächlich verwendet bei Prediction
- **Single-Pattern-Constraint:** Kein Template darf von nur einem Pattern predicted werden

## Directory Structure

```
Dataset_Hybrid_1/
├── DOCS.md
├── 00_Dry_Prediction.py
├── 01_Batch_Extract_Patterns.py
└── Q*/
    └── approach_4/
        ├── patterns.csv              # Alle extrahierten Patterns
        ├── patterns_filtered.csv     # Nach Threshold 150 gefiltert
        ├── used_patterns.csv         # Von Dry Prediction tatsächlich zugewiesen
        ├── patterns/                 # Pattern-spezifische Trainingsdaten
        │   └── {hash}/
        │       ├── pattern_info.json
        │       ├── training.csv
        │       ├── training_aggregated.csv
        │       └── training_cleaned.csv
        └── md/
            └── 00_dry_prediction_report.md
```

## Workflow Dependency Graph

```
Hybrid_1/Data_Generation/csv/01_patterns_*.csv (Static Pool)
                    |
                    v
        01_Batch_Extract_Patterns.py
                    |
                    v
           00_Dry_Prediction.py
```

## 01 - Batch_Extract_Patterns.py

**Purpose:** Extract, aggregate, clean and filter patterns for all 14 LOTO templates.

**Inputs:**
- `../Dataset_Operator/{Q*}/training.csv` - Operator-level training data

**Dependency:**
- `../../../Hybrid_1/Data_Generation/csv/01_patterns_*.csv` - Static pattern pool with occurrence counts

**Outputs per Template:**
- `{Q*}/approach_4/patterns.csv` - All extracted patterns
- `{Q*}/approach_4/patterns_filtered.csv` - Patterns meeting threshold
- `{Q*}/approach_4/patterns/{hash}/` - Pattern training datasets

**Configuration (APPROACHES dict):**
- `length: 0` - All pattern lengths (not restricted)
- `no_passthrough: True` - Exclude passthrough operators as roots
- `threshold: 150` - Minimum occurrence count in training data

**Usage:**
```bash
python3 01_Batch_Extract_Patterns.py
```

**Pipeline per Template:**
1. `03_Extract_Patterns.py` - Extract patterns from training.csv
2. `04_Aggregate_Patterns.py` - Merge parent+children rows
3. `05_Clean_Patterns.py` - Remove unavailable features
4. `06_Filter_Patterns.py` - Apply occurrence threshold

## 00 - Dry_Prediction.py

**Purpose:** Simulate pattern assignment on test queries to identify actually used patterns.

**Inputs:**
- `../Dataset_Operator/{Q*}/test.csv` - Operator-level test data
- `{Q*}/approach_4/patterns_filtered.csv` - Threshold-filtered patterns

**Outputs per Template:**
- `{Q*}/approach_4/used_patterns.csv` - Patterns actually assigned to test queries
- `{Q*}/approach_4/md/00_dry_prediction_report.md` - Statistics report

**Variables:**
- `--templates` - Templates to process (default: all 14)

**Usage:**
```bash
python3 00_Dry_Prediction.py
python3 00_Dry_Prediction.py --templates Q1 Q3
```

**Why Dry Prediction?**

Greedy pattern matching consumes nodes - longer patterns shadow shorter ones. A pattern may exist in test data but never be assigned if a longer pattern matches first.

**Single-Pattern-Constraint:** If only ONE pattern matches AND it consumes ALL nodes of a query, the pattern is discarded. This prevents degeneration to plan-level prediction.

Example reduction: Q1 has 51 filtered patterns, but only 1 is actually assigned (98% reduction).
