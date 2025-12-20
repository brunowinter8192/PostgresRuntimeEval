# Runtime_Prediction/Hybrid_2

Greedy pattern selection for Dynamic LOTO workflow.

## Working Directory

**CRITICAL:** All commands assume CWD = `Runtime_Prediction/Hybrid_2/`

```bash
cd /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Dynamic/Runtime_Prediction/Hybrid_2
```

## Directory Structure

```
Runtime_Prediction/Hybrid_2/
├── DOCS.md
├── 00_Batch_Workflow.py
├── 02_Pretrain_Models.py
├── 06_Extract_Test_Patterns.py
├── 07_Order_Patterns.py
├── 10_Pattern_Selection/           [See DOCS.md]
├── 12_Query_Prediction/            [See DOCS.md]
└── Model/
    ├── Training_Training/          # 80% - für Pattern Selection
    │   └── {Q*}/
    │       ├── Operator/{target}/{op}/model.pkl
    │       └── Pattern/{hash}/model_*.pkl, features.json
    └── Training/                   # 100% - für Final Prediction
        └── {Q*}/
            ├── Operator/{target}/{op}/model.pkl
            └── Pattern/{hash}/model_*.pkl, features.json
```

## Workflow Dependency Graph

```
Dataset_Hybrid_2/{Q*}/Training_Training.csv
              |
              v
    02_Pretrain_Models.py --split Training_Training
              |
              v
    Model/Training_Training/{Q*}/
              |
              +---> 06_Extract_Test_Patterns.py
              |              |
              |              v
              |     {Q*}/Pattern_Selection/06_test_pattern_occurrences.csv
              |              |
              |              v
              |     07_Order_Patterns.py
              |              |
              |              v
              |     {Q*}/Pattern_Selection/07_patterns_by_*.csv
              |              |
              v              v
    10_Pattern_Selection.py
              |
              v
    {Q*}/Pattern_Selection/{Strategy}/selected_patterns.csv
              |
              v
    02_Pretrain_Models.py --split Training
              |
              v
    Model/Training/{Q*}/
              |
              v
    12_Query_Prediction.py
              |
              v
    {Q*}/Evaluation/predictions.csv
```

## Output Structure

```
Runtime_Prediction/Hybrid_2/
├── Model/
│   ├── Training_Training/{Q*}/     # Selection models
│   └── Training/{Q*}/              # Prediction models
└── {Q*}/
    ├── Pattern_Selection/
    │   ├── 06_test_pattern_occurrences.csv
    │   ├── 07_patterns_by_size.csv
    │   ├── 07_patterns_by_frequency.csv
    │   └── {Strategy}/
    │       ├── selected_patterns.csv
    │       └── {hash}/predictions.csv, mre.csv, status.txt
    └── Evaluation/
        └── predictions.csv
```

---

## 00 - Batch_Workflow.py

**Purpose:** Run complete Hybrid_2 workflow for all 14 LOTO templates

**Inputs:**
- Pre-trained models from Hybrid_1 and Operator_Level
- `Dataset_Hybrid_2/{Q*}/Training_*.csv`

**Outputs per Template:**
- `{Q*}/Pattern_Selection/` - Selection results
- `{Q*}/Evaluation/predictions.csv` - Final predictions

**Workflow per Template:**
1. `06_Extract_Test_Patterns.py` - Find patterns in Training_Test
2. `07_Order_Patterns.py` - Sort patterns by strategy
3. `10_Pattern_Selection.py` - Greedy selection (Size/Epsilon)
4. `12_Query_Prediction.py` - Final prediction on test set

**Usage:**
```bash
python3 00_Batch_Workflow.py
```

**Note:** Currently uses pre-trained models from Hybrid_1. Update paths to use `Model/` after pretraining.

---

## 02 - Pretrain_Models.py

**Purpose:** Train operator and pattern models for selection and prediction

**Inputs:**
- `--split Training_Training`: Uses `Dataset_Hybrid_2/Training_Training/{Q*}/`
- `--split Training`: Uses `Dataset_Operator/{Q*}/training.csv` + `Dataset_Hybrid_1/{Q*}/approach_3/patterns/`

**Outputs per Template:**
- `Model/{split}/{Q*}/Operator/{target}/{op}/model.pkl`
- `Model/{split}/{Q*}/Pattern/{hash}/model_execution_time.pkl`
- `Model/{split}/{Q*}/Pattern/{hash}/model_start_time.pkl`
- `Model/{split}/{Q*}/Pattern/{hash}/features.json`

**Variables:**
- `--split` - Training_Training (80%) or Training (100%) (required)
- `--templates` - Templates to process (default: all 14)

**Usage:**
```bash
python3 02_Pretrain_Models.py --split Training_Training
python3 02_Pretrain_Models.py --split Training
python3 02_Pretrain_Models.py --split Training --templates Q1 Q3
```

---

## 06 - Extract_Test_Patterns.py

**Purpose:** Find pattern occurrences in Training_Test for selection

**Inputs:**
- `test_file` - Path to Training_Test.csv
- `patterns_file` - Path to global patterns CSV (01_patterns_*.csv)
- `--output-dir` - Output directory (required)

**Outputs:**
- `06_test_pattern_occurrences.csv` - Pattern occurrences with query_file, root_node_id, template

**Usage:**
```bash
python3 06_Extract_Test_Patterns.py \
    ../../Dataset/Dataset_Hybrid_2/Q1/Training_Test.csv \
    ../../../Hybrid_1/Data_Generation/csv/01_patterns_*.csv \
    --output-dir Q1/Pattern_Selection
```

---

## 07 - Order_Patterns.py

**Purpose:** Sort patterns by size or frequency strategy for greedy selection

**Inputs:**
- `occurrences_file` - Path to 06_test_pattern_occurrences.csv
- `--operator-predictions` - Path to baseline predictions for avg_mre calculation (required)
- `--output-dir` - Output directory (required)

**Outputs:**
- `07_patterns_by_size.csv` - Sorted by operator_count ASC, occurrence_count DESC
- `07_patterns_by_frequency.csv` - Sorted by occurrence_count DESC, operator_count ASC

**Sorting Strategies:**

- **Size:** Smaller patterns first (more general), tie-break by frequency
- **Frequency:** Most common patterns first, tie-break by size

**Usage:**
```bash
python3 07_Order_Patterns.py \
    Q1/Pattern_Selection/06_test_pattern_occurrences.csv \
    --operator-predictions ../Hybrid_1/Q1/approach_4/predictions.csv \
    --output-dir Q1/Pattern_Selection
```

---

## Subdirectory Modules

### 10_Pattern_Selection/

Greedy pattern selection. [See DOCS.md](10_Pattern_Selection/DOCS.md)

### 12_Query_Prediction/

Bottom-up query prediction. [See DOCS.md](12_Query_Prediction/DOCS.md)

---

## Shared Infrastructure

### mapping_config.py (from Dynamic/)

- `SVM_PARAMS` - NuSVR hyperparameters
- `TARGET_TYPES` - ['execution_time', 'start_time']
- `TARGET_NAME_MAP` - Column name mapping
- `get_operator_features()` - Feature set per operator type
- `csv_name_to_folder_name()` - Operator name normalization
