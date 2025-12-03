# 10_Pattern_Selection

Greedy pattern selection for runtime prediction improvement.

## Directory Structure

```
10_Pattern_Selection/
├── 10_Pattern_Selection.py     # Entry-point (argparse + orchestrator)
├── README.md                   # This file
└── src/                        [See DOCS.md]
    ├── tree.py                 # Tree building + pattern hashing
    ├── io.py                   # Load/export functions
    ├── prediction.py           # Training + prediction + aggregation
    ├── selection.py            # Selection strategies
    └── DOCS.md                 # Module documentation
```

## Workflow Overview

```
Input Files:
  ├── sorted_patterns.csv       # Patterns ranked by strategy
  ├── pattern_ffs_overview.csv  # Pattern feature selection results
  ├── Training_Training.csv     # Training data
  ├── Training_Test.csv         # Validation data
  ├── Model/Operator/           # Pre-trained operator models
  └── SVM/Operator/             # Operator FFS results

Processing:
  1. Load all components
  2. For each pattern (in priority order):
     a. Load or train pattern model
     b. Predict test set with current + accumulated patterns
     c. Calculate MRE on root operators
     d. If improves baseline -> SELECTED, else -> REJECTED
  3. Export per-pattern results + summary

Output:
  ├── {pattern_hash}/predictions.csv   # Per-pattern predictions
  ├── {pattern_hash}/mre.csv           # Per-pattern MRE
  ├── {pattern_hash}/status.txt        # SELECTED/REJECTED
  ├── selection_log.csv                # Full iteration log
  ├── selected_patterns.csv            # Selected patterns only
  └── selection_summary.csv            # Aggregate statistics
```

## Selection Strategies

| Strategy | Description | Pattern Order |
|----------|-------------|---------------|
| `frequency` | Static: iterate by occurrence count | 06_patterns_by_frequency.csv |
| `size` | Static: iterate by pattern size | 06_patterns_by_size.csv |
| `error` | Dynamic: re-rank by current error | 10_patterns_by_error.csv |

## Usage

### Static Selection (Frequency)

```bash
python3 10_Pattern_Selection.py \
    --strategy frequency \
    Pattern_Selection/06_patterns_by_frequency.csv \
    SVM/Pattern/Training_Training/pattern_ffs_overview.csv \
    Dataset/Baseline/Training_Training.csv \
    Dataset/Baseline/Training_Test.csv \
    Model/Operator/Training_Training \
    SVM/Operator/Training_Training \
    --pattern-output-dir Pattern_Selection/Frequency \
    --model-dir Model/Selected_Pattern/Frequency \
    --pretrained-dir Model/Patterns/Training_Training
```

### Error-Based Selection

```bash
python3 10_Pattern_Selection.py \
    --strategy error \
    Pattern_Selection/10_patterns_by_error.csv \
    SVM/Pattern/Training_Training/pattern_ffs_overview.csv \
    Dataset/Baseline/Training_Training.csv \
    Dataset/Baseline/Training_Test.csv \
    Model/Operator/Training_Training \
    SVM/Operator/Training_Training \
    --pattern-output-dir Pattern_Selection/Error \
    --model-dir Model/Selected_Pattern/Error \
    --pretrained-dir Model/Patterns/Training_Training \
    --pattern-occurrences-file Pattern_Selection/05_test_pattern_occurrences_error.csv
```

## Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `--strategy` | Required | Selection strategy: frequency/size/error |
| `sorted_patterns_file` | Positional | Path to ranked patterns CSV |
| `pattern_ffs_file` | Positional | Path to pattern FFS overview |
| `training_file` | Positional | Path to Training_Training.csv |
| `test_file` | Positional | Path to Training_Test.csv |
| `operator_model_dir` | Positional | Path to operator models |
| `operator_ffs_dir` | Positional | Path to operator FFS results |
| `--pattern-output-dir` | Required | Per-pattern results directory |
| `--model-dir` | Required | Model output directory |
| `--pretrained-dir` | Optional | Path to pretrained pattern models |
| `--pattern-occurrences-file` | Optional | Required for error strategy |

## Output Files

### Per-Pattern Results

| File | Format | Contents |
|------|--------|----------|
| predictions.csv | CSV (;) | Node-level predictions |
| mre.csv | CSV (;) | Pattern MRE summary |
| status.txt | Text | SELECTED/REJECTED/SKIPPED_* |

### Summary Files

| File | Contents |
|------|----------|
| selection_log.csv | Full iteration log with all patterns |
| selected_patterns.csv | Filtered log (SELECTED only) |
| selection_summary.csv | Aggregate counts and final MRE |
