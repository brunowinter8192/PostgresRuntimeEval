# Dataset_Hybrid_1

Pattern dataset preparation for Dynamic LOTO Hybrid_1 workflow.

## Basis: Static Hybrid_1

**Übernommen von** `Hybrid_1/Datasets/`:
- `03_Extract_Patterns.py` - Pattern extraction
- `04_Aggregate_Patterns.py` - Parent+Children aggregation
- `05_Clean_Patterns.py` - Feature cleanup

**Neu in Dynamic:**
- `01_Batch_Extract_Patterns.py` - Batch wrapper für LOTO templates
- `00_Dry_Prediction.py` - Pre-filter auf tatsächlich genutzte Patterns

## Working Directory

**CRITICAL:** All commands assume CWD = `Dataset/Dataset_Hybrid_1/`

```bash
cd Prediction_Methods/Dynamic/Dataset/Dataset_Hybrid_1
```

## Konzept

**LOTO-korrekter Pattern Pool:** Jeder Fold nutzt nur Patterns aus seinen 13 Training-Templates - kein globaler Static Pool (das wäre Data Leakage).

Pattern-Filterung erfolgt in zwei Stufen:

1. **Lokaler Threshold-Filter (>150)** → Nur Patterns mit genug Trainingsdaten im Fold
2. **Dry Prediction** → Welche Patterns werden auf Test-Queries tatsächlich zugewiesen

Nur Patterns die BEIDE Kriterien erfüllen werden trainiert:
- **Threshold:** Genug Samples für statistisch valide Modelle (aus Fold's eigener `patterns.csv`)
- **Dry Prediction:** Tatsächlich verwendet bei Prediction
- **Single-Pattern-Constraint:** Kein Query darf von nur einem Pattern vollständig predicted werden

## Directory Structure

```
Dataset_Hybrid_1/
├── DOCS.md
├── 00_Dry_Prediction.py
├── 01_Batch_Extract_Patterns.py
└── Q*/
    └── approach_3/
        ├── patterns.csv              # Alle extrahierten Patterns (aus Fold's training.csv)
        ├── patterns_filtered.csv     # Nach lokalem Threshold >150 gefiltert
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
../Dataset_Operator/{Q*}/training.csv
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

**Outputs per Template:**
- `{Q*}/approach_3/patterns.csv` - All extracted patterns
- `{Q*}/approach_3/patterns_filtered.csv` - Patterns meeting local threshold
- `{Q*}/approach_3/patterns/{hash}/` - Pattern training datasets

**Configuration (APPROACHES dict):**
- `length: 0` - All pattern lengths (not restricted)
- `no_passthrough: False` - Include all operators as pattern roots
- `threshold: 150` - Patterns mit `occurrence_count > 150` (strikt größer)

**Usage:**
```bash
python3 01_Batch_Extract_Patterns.py
```

**Pipeline per Template:**
1. `03_Extract_Patterns.py` - Extract patterns from training.csv
2. `04_Aggregate_Patterns.py` - Merge parent+children rows
3. `05_Clean_Patterns.py` - Remove unavailable features
4. `filter_by_threshold()` - Apply local occurrence threshold (inline, no static pool)

## 00 - Dry_Prediction.py

**Purpose:** Simulate pattern assignment on test queries to identify actually used patterns.

**Inputs:**
- `../Dataset_Operator/{Q*}/test.csv` - Operator-level test data
- `{Q*}/approach_3/patterns_filtered.csv` - Threshold-filtered patterns

**Outputs per Template:**
- `{Q*}/approach_3/used_patterns.csv` - Patterns actually assigned to test queries
- `{Q*}/approach_3/md/00_dry_prediction_report.md` - Report mit Query Tree Visualisierung

**Variables:**
- `--templates` - Templates to process (default: all 14)

**Usage:**
```bash
python3 00_Dry_Prediction.py
python3 00_Dry_Prediction.py --templates Q1 Q3
```

**Source:** `Hybrid_1/Runtime_Prediction/03_Predict_Queries/src/tree.py`
- `build_pattern_assignments()` - Pattern matching logic
- `compute_pattern_hash()` - Hash computation

**Pattern Matching Logic:**
- Patterns werden in Reihenfolge von `patterns_filtered.csv` gematcht
- Subtree-Check: Pattern wird nur gematcht wenn KEIN Node im Subtree bereits konsumiert
- Greedy: Frühere Patterns haben Priorität über spätere

**Single-Pattern-Constraint:** Wenn nur EIN Pattern matched UND es ALLE Nodes konsumiert, wird es verworfen (verhindert Plan-Level Degeneration).

**MD Report enthält:**
- Summary (Queries, unique Plans, Pattern count, Reduction)
- Used Patterns Liste
- Query Tree Visualisierung mit `[PATTERN ROOT]` und `[consumed]` Markern

**Beispiel Query Tree:**
```
Node 1 (Aggregate) [PATTERN ROOT] - ROOT
  Node 2 (Gather Merge) [consumed]
    Node 3 (Sort) [PATTERN ROOT]
      Node 4 (Aggregate) [consumed]
        Node 5 (Seq Scan)
```
