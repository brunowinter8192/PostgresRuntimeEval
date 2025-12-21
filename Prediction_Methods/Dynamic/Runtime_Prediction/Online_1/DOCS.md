# Runtime_Prediction - Dynamic Online Pattern Selection

Online learning workflow that trains operator models, mines patterns from a test query, and greedily selects patterns that improve prediction accuracy. Adapted for LOTO cross-validation.

## Working Directory

**CRITICAL:** All commands assume CWD = `Runtime_Prediction/Online_1/`

```bash
cd /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Dynamic/Runtime_Prediction/Online_1
```

## Prerequisites

Dataset_Hybrid_2 must exist with LOTO splits per template:

```bash
ls ../../Dataset/Dataset_Hybrid_2/Q1/
# Expected: Training_Training.csv, Training_Test.csv
```

## Directory Structure

```
Online_1/
    DOCS.md
    workflow.py
    batch_predict.sh
    A_01a_Query_Evaluation.py
    A_02_Pattern_Analysis.py
    Evaluation/
        Size/
        Error/
        Frequency/
        Analysis/
    src/                                 [See DOCS.md](src/DOCS.md)
```

## Workflow Dependency Graph

```
workflow.py (per query, per template)
       |
       v
batch_predict.sh (14 templates, parallel queries)
       |
       v
Evaluation/{Strategy}/{query}/
       |
       v
A_01a_Query_Evaluation ──> Analysis/{Strategy}/
       |
       v
A_02_Pattern_Analysis ───> Analysis/{Strategy}/
```

## Output Structure

```
Evaluation/
    Size/
        {query}/
            csv/
                predictions.csv
                selection_log.csv
            md/
                report.md
            models/
                operators/
                patterns/
    Error/
        ...
    Frequency/
        ...
    Analysis/
        Size/
            overall_mre.csv
            template_mre.csv
            template_mre_plot.png
            patterns_selected.csv
            patterns_used.csv
            patterns_comparison.csv
        Error/
            ...
        Frequency/
            ...
```

## Shared Infrastructure

**Constants from Dynamic/mapping_config.py:**
- `SVM_PARAMS` - NuSVR hyperparameters (kernel, nu, C, gamma)
- `EPSILON` - Minimum improvement threshold (0.5%)
- `MIN_ERROR_THRESHOLD` - Skip patterns below this avg_mre (10%)
- `STRATEGIES` - Available strategies ['error', 'size', 'frequency']
- `DEFAULT_STRATEGY` - Default strategy 'error'
- `OPERATOR_FEATURES` - Base operator features (10 features)
- `CHILD_FEATURES_TIMING` - Child timing features (st1, rt1, st2, rt2)

## Module Documentation

## workflow.py

**Purpose:** Main orchestrator for online prediction workflow (single query)

**Inputs:**
- `test_query_file` - Name of the test query (positional)
- `training_training_csv` - Path to Training_Training.csv (positional)
- `training_test_csv` - Path to Training_Test.csv (positional)
- `training_csv` - Path to training.csv (positional)
- `test_csv` - Path to test.csv (positional)
- `--output-dir` - Output directory (required)

**Outputs:**
- `{output-dir}/{Strategy}/{query}/csv/predictions.csv`
- `{output-dir}/{Strategy}/{query}/csv/selection_log.csv`
- `{output-dir}/{Strategy}/{query}/md/report.md`
- `{output-dir}/{Strategy}/{query}/models/operators/`
- `{output-dir}/{Strategy}/{query}/models/patterns/`

**Usage:**
```bash
python3 workflow.py Q1_100_seed_812199069 \
    ../../Dataset/Dataset_Hybrid_2/Q1/Training_Training.csv \
    ../../Dataset/Dataset_Hybrid_2/Q1/Training_Test.csv \
    ../../Dataset/Dataset_Operator/Q1/training.csv \
    ../../Dataset/Dataset_Operator/Q1/test.csv \
    --output-dir Evaluation
```

**Variables:**
- `--strategy` - Pattern ordering strategy: error, size, frequency (default: error)

---

## batch_predict.sh

**Purpose:** Run workflow.py for all test queries across all 14 templates in parallel

**Inputs:**
- Reads test queries from `Dataset/Dataset_Operator/{template}/test.csv`
- Training data from `Dataset/Dataset_Hybrid_2/{template}/`
- Training data from `Dataset/Dataset_Operator/{template}/`

**Outputs:**
- Same as workflow.py for all test queries
- `Evaluation/progress.log`

**Variables:**
- `STRATEGIES` - Currently set to "size" (modify for other strategies)
- `MAX_JOBS` - Parallel job limit (default: 14)

**Usage:**
```bash
chmod +x batch_predict.sh
./batch_predict.sh
```

---

## A_01a - Query_Evaluation.py

**Purpose:** Calculate MRE per template and generate visualization

**Inputs:**
- `predictions_dir` - Directory containing query folders with predictions.csv (positional)
- `--output-dir` - Output directory (required)

**Outputs:**
- `{output-dir}/overall_mre.csv`
- `{output-dir}/template_mre.csv`
- `{output-dir}/template_mre_plot.png`

**Usage:**
```bash
python3 A_01a_Query_Evaluation.py Evaluation/Size --output-dir Evaluation/Analysis/Size
```

---

## A_02 - Pattern_Analysis.py

**Purpose:** Analyze selected vs actually used patterns across all queries

**Inputs:**
- `run_dir` - Directory containing query folders (positional)
- `--output-dir` - Output directory (required)

**Outputs:**
- `{output-dir}/patterns_selected.csv` - All ACCEPTED patterns from selection_log
- `{output-dir}/patterns_used.csv` - Patterns actually applied during prediction
- `{output-dir}/patterns_comparison.csv` - Selected vs used with usage_rate and status

**Usage:**
```bash
python3 A_02_Pattern_Analysis.py Evaluation/Size --output-dir Evaluation/Analysis/Size
```
