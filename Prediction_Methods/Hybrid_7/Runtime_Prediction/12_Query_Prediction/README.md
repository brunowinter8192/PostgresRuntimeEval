# 12_Query_Prediction

Query-level runtime prediction using pre-trained operator and pattern models.

## Directory Structure

```
12_Query_Prediction/
├── 12_Query_Prediction.py      # Entry-point (argparse + orchestrator)
├── README.md                   # This file
└── src/                        [See DOCS.md]
    ├── tree.py                 # Tree building + pattern matching
    ├── prediction.py           # Prediction logic + feature aggregation
    ├── io.py                   # Load/export functions
    ├── report.py               # MD report generation
    └── DOCS.md                 # Module documentation
```

## Workflow Overview

```
Input Files:
  ├── Test.csv                  # Query operators to predict
  ├── Model/Operators_Training/ # Pre-trained operator models
  ├── two_step_evaluation_overview.csv
  └── (Optional) Pattern models + metadata

Processing:
  1. Load test data (filter main plan)
  2. Load operator models + features
  3. (Optional) Load pattern models + features
  4. For each query:
     a. Build tree structure
     b. Match patterns (greedy, priority order)
     c. Predict bottom-up (patterns first, then operators)
  5. Export predictions + MD report

Output:
  ├── predictions.csv           # Node-level predictions
  └── md/                       # Per-query reports
      └── 12_query_prediction_{query}_{timestamp}.md
```

## Usage

### Operator-Only Prediction

```bash
python3 12_Query_Prediction.py \
    Dataset/Test.csv \
    Model/Operators_Training \
    two_step_evaluation_overview.csv \
    --output-dir Evaluation/Operator_Only
```

### Pattern-Enhanced Prediction

```bash
python3 12_Query_Prediction.py \
    Dataset/Test.csv \
    Model/Operators_Training \
    two_step_evaluation_overview.csv \
    --strategy frequency \
    --pattern-model-dir Model/Selected_Pattern/Frequency \
    --pattern-ffs-file Model/Selected_Pattern/Frequency/pattern_ffs_overview.csv \
    --selected-patterns 10_selected_patterns_frequency.csv \
    --pattern-metadata 06_patterns_by_frequency.csv \
    --output-dir Evaluation/Pattern_Frequency
```

## Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `test_file` | Positional | Path to Test.csv |
| `operator_model_dir` | Positional | Path to operator models |
| `operator_overview_file` | Positional | Path to feature overview CSV |
| `--strategy` | Optional | Selection strategy (frequency/size/error) |
| `--pattern-model-dir` | Optional | Path to pattern models |
| `--pattern-ffs-file` | Optional | Path to pattern FFS overview |
| `--selected-patterns` | Optional | Path to selected patterns CSV |
| `--pattern-metadata` | Optional | Path to pattern metadata CSV |
| `--output-dir` | Required | Output directory |

## Output Files

### predictions.csv

| Column | Description |
|--------|-------------|
| query_file | Query identifier |
| node_id | Operator node ID |
| node_type | Operator type |
| depth | Tree depth |
| parent_relationship | Outer/Inner |
| subplan_name | Subplan identifier |
| actual_startup_time | Ground truth (ms) |
| actual_total_time | Ground truth (ms) |
| predicted_startup_time | Prediction (ms) |
| predicted_total_time | Prediction (ms) |
| prediction_type | operator/pattern |

### MD Report Sections

1. **Header** - Query ID, strategy, timestamp
2. **Input Summary** - File paths, pattern count
3. **Pattern Assignments** - Which patterns applied where
4. **Query Tree** - ASCII visualization
5. **Prediction Results** - Per-node MRE table
6. **Summary** - Average MRE, prediction counts
7. **Prediction Chain** - Step-by-step with features
