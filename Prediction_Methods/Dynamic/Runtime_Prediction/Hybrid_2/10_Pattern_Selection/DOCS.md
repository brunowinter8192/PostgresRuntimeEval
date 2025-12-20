# 10_Pattern_Selection

Greedy pattern selection for runtime prediction improvement. Iteratively evaluates patterns and selects those that improve MRE over operator-only baseline.

## Working Directory

**CRITICAL:** All commands assume CWD = `Runtime_Prediction/Hybrid_2/`

```bash
cd /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Dynamic/Runtime_Prediction/Hybrid_2
```

## Directory Structure

```
10_Pattern_Selection/
├── DOCS.md
├── 10_Pattern_Selection.py
└── src/                        [See DOCS.md](src/DOCS.md)
```

---

## 10 - Pattern_Selection.py

**Purpose:** Execute greedy pattern selection based on strategy (frequency, size, or error)

**Inputs:**
- `sorted_patterns_file` - Patterns ranked by strategy (07_patterns_by_*.csv)
- `training_file` - Training data (Training_Training.csv)
- `test_file` - Validation data (Training_Test.csv)
- `operator_model_dir` - Pre-trained operator models (Model/Operator/)
- `operator_ffs_dir` - Operator FFS results (SVM/Operator/)
- `--strategy` - Selection strategy: frequency, size, error (required)
- `--pattern-output-dir` - Per-pattern results output directory (required)
- `--pretrained-dir` - Path to pretrained pattern models (required)
- `--pattern-occurrences-file` - Path to 06_test_pattern_occurrences.csv (required)

**Outputs:**
- `{pattern_hash}/predictions.csv` - Per-pattern node-level predictions
- `{pattern_hash}/mre.csv` - Per-pattern MRE summary
- `{pattern_hash}/status.txt` - SELECTED/REJECTED/SKIPPED_*
- `selection_log.csv` - Full iteration log with all patterns
- `selected_patterns.csv` - Filtered log (SELECTED only)
- `selection_summary.csv` - Aggregate counts and final MRE

**Variables:**
- `--min-error-threshold` - Min avg_mre to consider pattern (default: 0.1, size/frequency only)
- `--epsilon` - Min MRE improvement required for SELECTED (default: 0.0)
- `--max-iteration` - Stop after N iterations (default: all)
- `--report` - Generate selection report markdown

**Usage:**
```bash
python3 10_Pattern_Selection/10_Pattern_Selection.py \
    --strategy size \
    Selected_Patterns/Q1/07_patterns_by_size.csv \
    ../../Dataset/Dataset_Hybrid_2/Training_Training/Q1/Training_Training.csv \
    ../../Dataset/Dataset_Hybrid_2/Training_Training/Q1/Training_Test.csv \
    Model/Training_Training/Q1/Operator \
    ../Operator_Level/Q1/SVM \
    --pattern-output-dir Selected_Patterns/Q1/Size/Epsilon \
    --pretrained-dir Model/Training_Training/Q1/Pattern \
    --pattern-occurrences-file Selected_Patterns/Q1/06_test_pattern_occurrences.csv \
    --epsilon 0.005 \
    --max-iteration 150
```

---

## Selection Strategies

| Strategy | Description | Pattern Order |
|----------|-------------|---------------|
| `frequency` | Static: iterate by occurrence count | 07_patterns_by_frequency.csv |
| `size` | Static: iterate by pattern size | 07_patterns_by_size.csv |
| `error` | Dynamic: re-rank by current error | 07_patterns_by_frequency.csv (initial) |

**Error-Score Formula (error strategy):**
```
error_score = occurrence_count * avg_mre
```
Combines frequency and current prediction error. After each SELECTED/REJECTED decision, error scores are recalculated based on updated predictions.

---

## Variable Details

**Min Error Threshold:**
Patterns with avg_mre < threshold are skipped for size/frequency strategies. avg_mre is calculated dynamically based on current predictions (updated after each SELECTED pattern). Error strategy does not use this filter.

**Pretrained Models:**
Patterns without pretrained models are skipped with status `SKIPPED_NO_MODEL`.
