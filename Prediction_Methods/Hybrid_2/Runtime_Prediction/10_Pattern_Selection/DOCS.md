# 10_Pattern_Selection

Greedy pattern selection for runtime prediction improvement. Iteratively evaluates patterns and selects those that improve MRE over operator-only baseline.

## Working Directory

**CRITICAL:** All commands assume CWD = `Runtime_Prediction/`

```bash
cd /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Hybrid_2/Runtime_Prediction
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

**Baseline:** Operator-only prediction on Training_Test = 22.97% MRE. Selection accepts patterns that improve this baseline.

**Inputs:**
- `sorted_patterns_file` - Patterns ranked by strategy (07_patterns_by_*.csv or 08_patterns_by_error.csv)
- `pattern_ffs_file` - Pattern feature selection results (pattern_ffs_overview.csv)
- `training_file` - Training data (Training_Training.csv)
- `test_file` - Validation data (Training_Test.csv)
- `operator_model_dir` - Pre-trained operator models (Model/Operator/)
- `operator_ffs_dir` - Operator FFS results (SVM/Operator/)
- `--strategy` - Selection strategy: frequency, size, error (required)
- `--pattern-output-dir` - Per-pattern results output directory (required)
- `--pattern-occurrences-file` - Path to 06_test_pattern_occurrences.csv (required)

**Outputs:**
- `{pattern_hash}/predictions.csv` - Per-pattern node-level predictions
- `{pattern_hash}/mre.csv` - Per-pattern MRE summary
- `{pattern_hash}/status.txt` - SELECTED/REJECTED/SKIPPED_*
- `selection_log.csv` - Full iteration log with all patterns
- `selected_patterns.csv` - Filtered log (SELECTED only)
- `selection_summary.csv` - Aggregate counts and final MRE

**Variables:**
- `--pretrained-dir` - Path to pretrained models (default: None)
- `--min-error-threshold` - Min avg_mre to consider pattern (default: 0.1, size/frequency only)
- `--epsilon` - Min MRE improvement required for SELECTED (default: 0.0)
- `--min-template-count` - Min unique templates a pattern must appear in (default: 1 = disabled)

**Usage (Static - Frequency):**
```bash
python3 10_Pattern_Selection/10_Pattern_Selection.py \
    --strategy frequency \
    Pattern_Selection/07_patterns_by_frequency.csv \
    SVM/Pattern/Training_Training/pattern_ffs_overview.csv \
    ../Dataset/Baseline/Training_Training.csv \
    ../Dataset/Baseline/Training_Test.csv \
    Model/Training_Training/Operator \
    SVM/Operator/Training_Training \
    --pattern-output-dir Pattern_Selection/Training_Training/Frequency/Baseline \
    --pretrained-dir Model/Training_Training/Pattern \
    --pattern-occurrences-file Pattern_Selection/06_test_pattern_occurrences.csv
```

**Usage (Dynamic - Error):**
```bash
python3 10_Pattern_Selection/10_Pattern_Selection.py \
    --strategy error \
    Pattern_Selection/08_patterns_by_error.csv \
    SVM/Pattern/Training_Training/pattern_ffs_overview.csv \
    ../Dataset/Baseline/Training_Training.csv \
    ../Dataset/Baseline/Training_Test.csv \
    Model/Training_Training/Operator \
    SVM/Operator/Training_Training \
    --pattern-output-dir Pattern_Selection/Training_Training/Error/Baseline \
    --pretrained-dir Model/Training_Training/Pattern \
    --pattern-occurrences-file Pattern_Selection/06_test_pattern_occurrences.csv
```

---

## Selection Strategies

| Strategy | Description | Pattern Order |
|----------|-------------|---------------|
| `frequency` | Static: iterate by occurrence count | 07_patterns_by_frequency.csv |
| `size` | Static: iterate by pattern size | 07_patterns_by_size.csv |
| `error` | Dynamic: re-rank by current error | 08_patterns_by_error.csv |

**Error-Score Formula (error strategy):**
```
error_score = occurrence_count * avg_mre
```
Combines frequency and current prediction error. After each SELECTED/REJECTED decision, error scores are recalculated based on updated predictions.

---

## Variable Details

**Min Error Threshold:**
Patterns with avg_mre < threshold are skipped for size/frequency strategies. avg_mre is calculated dynamically based on current predictions (updated after each SELECTED pattern). Error strategy does not use this filter.

**Min Template Count:**
Patterns appearing in fewer than N unique templates are skipped. A pattern in only 1 template is unlikely to generalize. Default=1 (disabled).
