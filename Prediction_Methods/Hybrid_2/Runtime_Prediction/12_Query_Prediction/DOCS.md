# 12_Query_Prediction

Bottom-up query prediction using operator and pattern models. Generates per-query MD reports showing prediction steps.

## Working Directory

**CRITICAL:** All commands assume CWD = `Runtime_Prediction/`

```bash
cd Prediction_Methods/Hybrid_2/Runtime_Prediction
```

## Directory Structure

```
12_Query_Prediction/
├── DOCS.md
├── 12_Query_Prediction.py
└── src/                        [See DOCS.md](src/DOCS.md)
```

---

## 12 - Query_Prediction.py

**Purpose:** Execute bottom-up query prediction with optional pattern models

**Inputs:**
- `test_file` - Query operators to predict (Test.csv)
- `operator_model_dir` - Pre-trained operator models (Model/Operators_Training/)
- `operator_overview_file` - Feature overview (operator_overview.csv)
- `--output-dir` - Output directory for predictions (required)

**Outputs:**
- `predictions.csv` - Node-level predictions with actual/predicted times, pattern_hash column
- `md/12_{template}_{plan_hash[:8]}_{timestamp}.md` - One MD report per unique plan structure

**Variables:**
- `--strategy` - Selection strategy for pattern priority: frequency, size, error (default: None)
- `--pattern-model-dir` - Path to pattern models (default: None)
- `--selected-patterns` - Path to selected_patterns.csv (default: None)
- `--pattern-metadata` - Path to pattern metadata CSV (default: None)

**Usage (Operator-Only):**
```bash
python3 12_Query_Prediction/12_Query_Prediction.py \
    ../Dataset/Test.csv \
    Model/Operators_Training \
    SVM/Operator/operator_overview.csv \
    --output-dir Evaluation/Operator_Only
```

**Usage (Pattern-Enhanced):**
```bash
python3 12_Query_Prediction/12_Query_Prediction.py \
    ../Dataset/Test.csv \
    Model/Operators_Training \
    SVM/Operator/operator_overview.csv \
    --strategy frequency \
    --pattern-model-dir Model/Selected_Pattern/Frequency \
    --selected-patterns Pattern_Selection/Frequency/selected_patterns.csv \
    --pattern-metadata Pattern_Selection/07_patterns_by_frequency.csv \
    --output-dir Evaluation/Pattern_Frequency
```

---

## Pattern-Matching Priority

- `pattern_order` is read from `selected_patterns.csv` (selection order from 10_Pattern_Selection)
- `build_pattern_assignments()` iterates patterns in this order: **first match wins**
- If Pattern A (position 1) and Pattern B (position 5) both match Node X, Pattern A is used
- Matched nodes are "consumed" and unavailable for later patterns
