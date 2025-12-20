# Runtime_Prediction/Hybrid_1

Hybrid pattern-level prediction for Dynamic LOTO workflow.

## Basis: Static Hybrid_1

**Übernommen von** `Hybrid_1/Runtime_Prediction/`:
- `01_Feature_Selection.py` - Forward Feature Selection für Patterns
- `02_Train_Models.py` - SVM Model Training
- `03_Predict_Queries/` - Hybrid Bottom-Up Prediction

**Neu in Dynamic:**
- `02_Pretrain_Models.py` - FFS + Training für alle LOTO templates
- `03_Predict.py` - Prediction für alle LOTO templates
- `A_01a_Query_Evaluation.py` - LOTO-aggregierte Evaluation

## Working Directory

**CRITICAL:** All commands assume CWD = `Runtime_Prediction/Hybrid_1/`

```bash
cd /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Dynamic/Runtime_Prediction/Hybrid_1
```

## Approach Definitions

**Pattern Pool:** Verwendet Static Hybrid_1 patterns (372) als gemeinsame Referenz.

| Approach | no_passthrough | threshold | Beschreibung |
|----------|---------------|-----------|--------------|
| approach_3 | False | 150 | Alle Patterns, keine Filter |
| approach_4 | True | 150 | Ohne Passthrough-Operatoren als Root |

## Directory Structure

```
Runtime_Prediction/Hybrid_1/
├── DOCS.md
├── 02_Pretrain_Models.py
├── 03_Predict.py
├── A_01a_Query_Evaluation.py
├── Evaluation/
│   └── {approach}/
│       ├── overall_mre.csv
│       ├── loto_mre.csv
│       └── loto_mre_plot.png
└── Q*/
    └── {approach}/
        ├── SVM/
        │   └── two_step_evaluation_overview.csv
        ├── Model/
        │   ├── execution_time/{hash}/model.pkl
        │   ├── start_time/{hash}/model.pkl
        │   └── Operators/ (symlinks to Operator_Level)
        └── predictions.csv
```

## Workflow Dependency Graph

```
Dataset/Dataset_Hybrid_1/{Q*}/{approach}/used_patterns.csv
                         |
                         v
              02_Pretrain_Models.py
                         |
                         v
              {Q*}/{approach}/Model/
                         |
                         v
                  03_Predict.py
                         |
                         v
              {Q*}/{approach}/predictions.csv
                         |
                         v
              A_01a_Query_Evaluation.py
                         |
                         v
              Evaluation/{approach}/loto_mre_plot.png
```

## 02 - Pretrain_Models.py

**Purpose:** FFS and model training for all LOTO templates. Run once before prediction.

**Inputs:**
- `../../Dataset/Dataset_Hybrid_1/{Q*}/{approach}/` - Pattern training datasets
- `../../Dataset/Dataset_Hybrid_1/{Q*}/{approach}/used_patterns.csv` - Patterns to train

**Dependency:**
- `../Operator_Level/{Q*}/Model/` - Operator-level fallback models (symlinked)

**Outputs per Template:**
- `{Q*}/{approach}/SVM/two_step_evaluation_overview.csv` - FFS results
- `{Q*}/{approach}/Model/{target}/{hash}/model.pkl` - Pattern models
- `{Q*}/{approach}/Model/Operators/` - Symlinks to Operator_Level

**Variables:**
- `--templates` - Templates to process (default: all 14)
- `--approaches` - Approaches to process (default: approach_3, approach_4)

**Usage:**
```bash
python3 02_Pretrain_Models.py
python3 02_Pretrain_Models.py --templates Q1 Q3 --approaches approach_3
```

## 03 - Predict.py

**Purpose:** Hybrid bottom-up prediction using pretrained models.

**Inputs:**
- `../../Dataset/Dataset_Operator/{Q*}/test.csv` - Test data
- `../../Dataset/Dataset_Hybrid_1/{Q*}/{approach}/used_patterns.csv` - Pattern matching list
- `{Q*}/{approach}/Model/` - Pretrained models from 02_Pretrain_Models.py

**Outputs per Template:**
- `{Q*}/{approach}/predictions.csv` - Hybrid predictions

**Variables:**
- `--templates` - Templates to process (default: all 14)
- `--approaches` - Approaches to process (default: approach_3, approach_4)

**Usage:**
```bash
python3 03_Predict.py
python3 03_Predict.py --templates Q1 Q3 --approaches approach_3
```

**Pattern Matching:** Uses `used_patterns.csv` for matching - same patterns that were trained.

## A_01a - Query_Evaluation.py

**Purpose:** Aggregate predictions from all 14 LOTO folds and calculate MRE.

**Inputs:**
- `{Q*}/{approach}/predictions.csv` - Predictions from all LOTO templates

**Outputs:**
- `{output-dir}/overall_mre.csv` - Overall MRE across all templates
- `{output-dir}/loto_mre.csv` - MRE per LOTO template
- `{output-dir}/loto_mre_plot.png` - Bar plot visualization

**Usage:**
```bash
python3 A_01a_Query_Evaluation.py approach_3 --output-dir Evaluation/approach_3
```

**LOTO Aggregation:**
- Collects predictions from all 14 templates
- Each template was test set exactly once
- Plot shows MRE when each template was held out
