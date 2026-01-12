# Runtime_Prediction - Online Pattern Selection

Online learning workflow that trains operator models, mines patterns from a test query, and greedily selects patterns that improve prediction accuracy.

## Working Directory

**CRITICAL:** All commands assume CWD = `Runtime_Prediction/`

```bash
cd Prediction_Methods/Online_1/Runtime_Prediction
```

## Directory Structure

```
Runtime_Prediction/
    DOCS.md
    workflow.py
    batch_predict.sh
    A_01a_Query_Evaluation.py
    A_02_Pattern_Analysis.py
    A_03_Method_Comparison.py
    A_04_Strategy_Comparison.py
    A_05_Pattern_Count.py
    A_06_Strategy_MRE_Comparison.py
    Evaluation/
        Error/
        Size/
        Frequency/
        Analysis/
    src/                                 [See DOCS.md](src/DOCS.md)
```

## Workflow Dependency Graph

```
workflow.py (per query)
       |
       v
batch_predict.sh (420 queries parallel)
       |
       v
Evaluation/{Strategy}/
       |
       v
A_01a_Query_Evaluation ──> Analysis/{Strategy}/
       |
       v
A_02_Pattern_Analysis ───> Analysis/{Strategy}/
       |
       v
A_03_Method_Comparison ──> Analysis/Comparison/
```

## Output Structure

```
Evaluation/
    Error/
        {query_folder}/
            csv/
                predictions.csv
                selection_log.csv
            md/
                report.md
            models/
                operators/
                patterns/
    Size/
        ...
    Frequency/
        ...
    Analysis/
        Error/
            overall_mre.csv
            template_mre.csv
            template_mre_plot.png
            patterns_selected.csv
            patterns_used.csv
            patterns_comparison.csv
        Size/
            ...
        Frequency/
            ...
        Comparison/
            method_comparison.csv
            overall_comparison.csv
            method_comparison.md
```

## Shared Infrastructure

**Constants from mapping_config.py:**
- `SVM_PARAMS` - NuSVR hyperparameters (kernel, nu, C, gamma)
- `MIN_ERROR_THRESHOLD` - Skip patterns below this avg_mre (10%)
- `STRATEGIES` - Available strategies ['error', 'size', 'frequency']
- `DEFAULT_STRATEGY` - Default strategy 'error'
- `OPERATOR_FEATURES` - Base operator features (10 features)
- `CHILD_FEATURES_TIMING` - Child timing features (st1, rt1, st2, rt2)

## Selection Algorithm

**Ranking (mining.py):**
- Size: `operator_count` ASC, `occurrence_count` DESC, `pattern_hash` ASC
- Frequency: `occurrence_count` DESC, `operator_count` ASC, `pattern_hash` ASC
- Error: `error_score` DESC, `pattern_hash` ASC

**Selection Loop (selection.py):**

| Verhalten | Size/Frequency | Error |
|-----------|----------------|-------|
| avg_mre < 10% Skip | Ja | Nein |
| Reranking bei SELECT | Nein (statisch) | Ja (dynamisch) |

**Prediction Assignment (prediction.py):**
- Längere Patterns haben Vorrang (Length DESC)
- Bei gleicher Länge: Selection Order (stable sort)

## Module Documentation

## workflow.py

**Purpose:** Main orchestrator for online prediction workflow

**Inputs:**
- `test_query_file` - Name of the test query (positional)
- `training_training_csv` - Path to Training_Training.csv (positional)
- `training_test_csv` - Path to Training_Test.csv (positional)
- `training_csv` - Path to Training.csv (positional)
- `test_csv` - Path to Test.csv (positional)
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
    ../../Hybrid_2/Dataset/Baseline/Training_Training.csv \
    ../../Hybrid_2/Dataset/Baseline/Training_Test.csv \
    ../../Hybrid_2/Dataset/Baseline/Training.csv \
    ../../Hybrid_2/Dataset/Baseline/Test.csv \
    --output-dir Evaluation
```

**Variables:**
- `--strategy` - Pattern ordering strategy: error, size, frequency (default: error)
- `--epsilon` - Min MRE improvement for pattern acceptance (default: 0.0)

---

## batch_predict.sh

**Purpose:** Run workflow.py for all test queries in parallel

**Inputs:**
- Hardcoded paths to `../../Hybrid_2/Dataset/Baseline/` datasets

**Outputs:**
- Same as workflow.py for all 420 test queries
- `Evaluation/progress.log`

**Usage:**
```bash
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
python3 A_01a_Query_Evaluation.py Evaluation/Error --output-dir Evaluation/Analysis/Error
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
python3 A_02_Pattern_Analysis.py Evaluation/Error --output-dir Evaluation/Analysis/Error
```

---

## A_03 - Method_Comparison.py

**Purpose:** Compare pattern selection and MRE progression across Hybrid_1, Hybrid_2, and Online_1

**Inputs:**
- `h1_dir` - Hybrid_1 evaluation directory (positional)
- `h2_dir` - Hybrid_2 evaluation directory (positional)
- `o1_dir` - Online_1 analysis directory (positional)
- `--output-dir` - Output directory (required)

**Outputs:**
- `{output-dir}/method_comparison.csv` - Per-template MRE comparison with pattern hashes
- `{output-dir}/overall_comparison.csv` - Overall MRE comparison across approaches
- `{output-dir}/method_comparison.md` - Report with MRE progression and pattern breakdown

**Usage:**
```bash
python3 A_03_Method_Comparison.py \
  ../../Hybrid_1/Runtime_Prediction/Baseline_SVM/Evaluation/approach_3 \
  ../../Hybrid_2/Runtime_Prediction/Evaluation/Size/Epsilon \
  Evaluation/Analysis/Size \
  --output-dir Evaluation/Analysis/Comparison
```

---

## A_04 - Strategy_Comparison.py

**Purpose:** Compare pattern selection and usage across Error/Size/Frequency strategies within Online_1

**Inputs:**
- `evaluation_dir` - Path to Evaluation directory containing Error/, Size/, Frequency/ (positional)
- `--output-dir` - Output directory (required)

**Outputs:**
- `{output-dir}/A_04_strategy_summary.csv` - Count of queries with differences
- `{output-dir}/A_04_selection_differences.csv` - Queries where strategies selected different patterns
- `{output-dir}/A_04_usage_differences.csv` - Queries where strategies used different patterns

**Usage:**
```bash
python3 A_04_Strategy_Comparison.py Evaluation --output-dir Evaluation/Analysis/Overall
```

---

## A_05 - Pattern_Count.py

**Purpose:** Count patterns found per query and aggregate by template

**Inputs:**
- `evaluation_dir` - Path to Evaluation directory (positional)
- `--strategy` - Strategy to analyze: Error, Size, Frequency (default: Error)
- `--output-dir` - Output directory (required)

**Outputs:**
- `{output-dir}/A_05_pattern_counts_per_query.csv` - Pattern count for each query
- `{output-dir}/A_05_pattern_counts_per_template.csv` - Min/max/avg/std per template

**Usage:**
```bash
python3 A_05_Pattern_Count.py Evaluation --strategy Error --output-dir Evaluation/Analysis/Overall
```

---

## A_06 - Strategy_MRE_Comparison.py

**Purpose:** Create grouped bar chart comparing MRE across Error/Size/Frequency strategies

**Inputs:**
- Reads `Evaluation/Analysis/{Error,Size,Frequency}/template_mre.csv` automatically

**Outputs:**
- `{output-dir}/A_06_strategy_comparison.csv` - Combined MRE per template
- `{output-dir}/A_06_strategy_comparison.png` - Grouped bar plot (3 bars per template)

**Usage:**
```bash
python3 A_06_Strategy_MRE_Comparison.py
python3 A_06_Strategy_MRE_Comparison.py --output-dir Evaluation/Analysis/Overall
```
