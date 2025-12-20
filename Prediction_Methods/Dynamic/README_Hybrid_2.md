# Dynamic Hybrid_2 Workflow

Greedy pattern selection for dynamic LOTO workloads.

**Basiert auf:** [Static Hybrid_2](../Hybrid_2/README.md) - adaptiert für LOTO Cross-Validation.

## Konzept

Hybrid_2 verwendet Greedy Pattern Selection:
- **Pattern Selection:** Iterativ Patterns auswählen die MRE verbessern
- **Validation Split:** 80/20 Split für Selection-Validierung vor finaler Evaluation

### Daten-Splits

| Split | Anteil | Verwendung |
|-------|--------|------------|
| Training_Training | 80% | Model Training |
| Training_Test | 20% | Pattern Selection Validation |
| Test | 100% | Finale Evaluation |

## Directory Structure

```
Dynamic/
├── Dataset/
│   ├── Dataset_Operator/            # LOTO Splits (shared)
│   ├── Dataset_Hybrid_1/            # Pattern Data für Training (100%)
│   └── Dataset_Hybrid_2/            [See DOCS.md]
│       └── Training_Training/       # Pattern Data für Training_Training (80%)
└── Runtime_Prediction/
    └── Hybrid_2/                    [See DOCS.md]
```

## Workflow

### Phase 1: Dataset

**Purpose:** Split training data and extract patterns

**Input:** `Dataset/Dataset_Operator/{Q*}/training.csv`

**Output:**
- `Dataset/Dataset_Hybrid_2/Training_Training/{Q*}/Training_Training.csv` (80%)
- `Dataset/Dataset_Hybrid_2/Training_Training/{Q*}/Training_Test.csv` (20%)
- `Dataset/Dataset_Hybrid_2/Training_Training/{Q*}/patterns/{hash}/training_cleaned.csv`

**Details:** [Dataset/Dataset_Hybrid_2/DOCS.md](Dataset/Dataset_Hybrid_2/DOCS.md)

### Phase 2: Pretrain Models

**Purpose:** Train operator and pattern models for selection

**Input:**
- `Dataset/Dataset_Hybrid_2/Training_Training/{Q*}/Training_Training.csv`
- `Dataset/Dataset_Hybrid_2/Training_Training/{Q*}/patterns/{hash}/training_cleaned.csv`

**Output:** `Runtime_Prediction/Hybrid_2/Model/Training_Training/{Q*}/`

**Script:** `Runtime_Prediction/Hybrid_2/02_Pretrain_Models.py`

### Phase 3: Pattern Selection

**Purpose:** Greedy selection of patterns that improve MRE

**Input:**
- Pretrained models from Phase 2
- `Dataset/Dataset_Hybrid_2/Training_Training/{Q*}/Training_Test.csv`

**Output:** Selected patterns per template

**Details:** [Runtime_Prediction/Hybrid_2/10_Pattern_Selection/DOCS.md](Runtime_Prediction/Hybrid_2/10_Pattern_Selection/DOCS.md)

### Phase 4: Final Prediction

**Purpose:** Predict on test set using selected patterns

**Input:**
- Selected patterns from Phase 3
- Models trained on full training data (100%)

**Output:** Predictions per template

**Details:** [Runtime_Prediction/Hybrid_2/12_Query_Prediction/DOCS.md](Runtime_Prediction/Hybrid_2/12_Query_Prediction/DOCS.md)

## Quick Reproduction

```bash
# Phase 1: Split + Extract patterns (80%)
cd Dataset/Dataset_Hybrid_2
python3 01_LOTO_Split_Training.py --input-dir ../Dataset_Operator --output-dir Training_Training
python3 02_Extract_Pattern_Data.py

# Phase 2: Pretrain models
cd ../../Runtime_Prediction/Hybrid_2
python3 02_Pretrain_Models.py --split Training_Training  # 80% für Selection
python3 02_Pretrain_Models.py --split Training           # 100% für Prediction

# Phase 3: Pattern Selection
# (TODO: Batch script)

# Phase 4: Final Prediction
# (TODO: Batch script)
```

## Model Splits

| Split | Trainiert auf | Verwendet für |
|-------|---------------|---------------|
| `Model/Training_Training/` | 80% (Training_Training.csv) | Pattern Selection |
| `Model/Training/` | 100% (training.csv) | Final Prediction |

**14 LOTO Templates:**
```
Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q18, Q19
```
