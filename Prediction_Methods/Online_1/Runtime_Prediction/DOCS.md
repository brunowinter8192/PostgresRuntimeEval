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
    A_07_Strategy_Pattern_Comparison.py
    A_08_Optimizer_Baseline.py
    A_09_Combined_Strategy_Plot.py
    A_10_Q4_MRE_Plot.py
    A_11_Method_Size_Comparison.py
    A_12_Unrounded_Template_MRE.py
    A_13_Size_Freq_Comparison.py
    A_14_Size_Freq_Propagation.py
    A_15_Negative_Predictions.py
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

---

## A_10 - Q4_MRE_Plot.py

**Purpose:** Generate bar plot showing MRE for all 30 Q4 queries with overall MRE annotation

**Inputs:**
- `predictions_dir` - Directory containing Q4_* query folders with predictions.csv (positional)
- `--output-dir` - Output directory (required)

**Outputs:**
- `{output-dir}/q4_mre_barplot.png` - Bar plot with 30 bars (one per Q4 query), overall MRE in top-right corner

**Usage:**
```bash
python3 A_10_Q4_MRE_Plot.py Evaluation/Error --output-dir Evaluation/Analysis/Error
python3 A_10_Q4_MRE_Plot.py Evaluation/Size --output-dir Evaluation/Analysis/Size
python3 A_10_Q4_MRE_Plot.py Evaluation/Frequency --output-dir Evaluation/Analysis/Frequency
```

---

## A_11 - Method_Size_Comparison.py

**Purpose:** Compare Online_1 Size vs Hybrid_2 Size (Baseline) per template

**Inputs:**
- `online1_mre` - Path to Online_1 Size template_mre.csv (positional)
- `hybrid2_mre` - Path to Hybrid_2 Size template_mre.csv (positional)
- `--output-dir` - Output directory (required)

**Outputs:**
- `A_11_size_comparison.png` - Bar plot with 2 bars per template (Online_1 vs Hybrid_2)

**Usage:**
```bash
python3 A_11_Method_Size_Comparison.py \
  Evaluation/Analysis/Size/template_mre.csv \
  ../../Hybrid_2/Runtime_Prediction/Evaluation/Size/Baseline/A_01a_template_mre.csv \
  --output-dir Evaluation/Analysis/Overall
```

---

## A_12 - Unrounded_Template_MRE.py

**Purpose:** Compute unrounded MRE per template for all three strategies from raw predictions

**Inputs:**
- Reads `Evaluation/{Size,Frequency,Error}/*/csv/predictions.csv` automatically

**Outputs:**
- `{output-dir}/A_12_unrounded_template_mre.csv` - MRE per template with full floating-point precision

**Usage:**
```bash
python3 A_12_Unrounded_Template_MRE.py
python3 A_12_Unrounded_Template_MRE.py --output-dir Evaluation/Analysis/Overall
```

---

## A_13 - Size_Freq_Comparison.py

**Purpose:** Compare actually assigned patterns between Size and Frequency strategies per query, aggregated to template level

**Inputs:**
- `evaluation_dir` - Path to Evaluation directory containing Size/, Frequency/ (positional)
- `--output-dir` - Output directory (required)

**Outputs:**
- `{output-dir}/A_13_template_comparison.csv` - Per-template match rate (IDENTICAL/DIFFERS)
- `{output-dir}/A_13_query_differences.csv` - Detail for queries where assignments differ

**Usage:**
```bash
python3 A_13_Size_Freq_Comparison.py Evaluation --output-dir Evaluation/Analysis/Overall
```

**Implementation Details:**

Compares patterns from `[PATTERN: hash]` tags in report.md Query Tree section (actually assigned patterns), not from `models/patterns/` (all selected patterns). Selected patterns include models trained but never assigned to any node; assigned patterns are only those placed in the query tree.

---

## A_14 - Size_Freq_Propagation.py

**Purpose:** Visualize Mean Predicted Total Time per operator (Leaf to Root) for Size vs Frequency in a given template

**Inputs:**
- `evaluation_dir` - Path to Evaluation directory containing Size/, Frequency/ (positional)
- `--template` - Template to analyze (required)
- `--output-dir` - Output directory (required)

**Outputs:**
- `{output-dir}/A_14_propagation_{template}.png` - Line plot showing prediction values per operator for both strategies

**Usage:**
```bash
python3 A_14_Size_Freq_Propagation.py Evaluation --template Q5 --output-dir Evaluation/Analysis/Overall
```

---

## A_15 - Negative_Predictions.py

**Purpose:** Count and detail negative predicted values across all strategies

**Inputs:**
- `evaluation_dir` - Path to Evaluation directory (positional)
- `--output-dir` - Output directory (required)

**Outputs:**
- `{output-dir}/A_15_negative_predictions.csv` - All negative predictions with query, node, strategy detail
- `{output-dir}/A_15_negative_summary.csv` - Count per strategy and node_type with affected templates

**Usage:**
```bash
python3 A_15_Negative_Predictions.py Evaluation --output-dir Evaluation/Analysis/Overall
```
