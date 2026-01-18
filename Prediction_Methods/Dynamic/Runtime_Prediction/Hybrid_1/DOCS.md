# Runtime_Prediction/Hybrid_1

Hybrid pattern-level prediction for Dynamic LOTO workflow.

## Working Directory

**CRITICAL:** All commands assume CWD = `Runtime_Prediction/Hybrid_1/`

```bash
cd Prediction_Methods/Dynamic/Runtime_Prediction/Hybrid_1
```

## Prerequisite

**CRITICAL:** `Operator_Level/` muss vor Hybrid_1 durchgelaufen sein.

Hybrid_1 verwendet die FFS-trainierten Operator-Models aus Operator_Level:
- Models: `../Operator_Level/{Q*}/Model/{target}/{operator}/model.pkl`
- Features: `../Operator_Level/{Q*}/SVM/two_step_evaluation_overview.csv`

## Directory Structure

```
Runtime_Prediction/Hybrid_1/
├── DOCS.md
├── 00_Batch_Workflow.py
├── 01_Feature_Selection.py
├── 02_Pretrain_Models.py
├── 03_Predict.py
├── A_01a_Query_Evaluation.py
├── A_01b_Static_Dynamic_Comparison.py
├── A_01c_Pattern_Comparison.py
├── A_01d_Pattern_Statistics.py
├── Evaluation/
│   └── {approach}/
│       ├── overall_mre.csv
│       ├── loto_mre.csv
│       ├── loto_mre_plot.png
│       ├── A_01b_static_dynamic_comparison.csv/.png
│       ├── A_01c_pattern_comparison.csv
│       └── A_01d_pattern_statistics.csv
└── Q*/
    └── {approach}/
        ├── SVM/
        │   ├── two_step_evaluation_overview.csv
        │   └── {target}/{hash}_csv/
        │       ├── ffs_results_seed42.csv
        │       ├── selected_features_seed42.csv
        │       └── final_features.csv
        ├── Model/
        │   ├── execution_time/{hash}/model.pkl
        │   └── start_time/{hash}/model.pkl
        ├── predictions.csv
        └── md/                    (--report only)
            └── 03_{template}.md
```

## Workflow Dependency Graph

```
../Operator_Level/{Q*}/Model/          (Operator Models - FFS trained)
../Operator_Level/{Q*}/SVM/two_step_evaluation_overview.csv (Operator Features)
                    |
                    v
Dataset/Dataset_Hybrid_1/{Q*}/{approach}/used_patterns.csv (from 00_Dry_Prediction)
Dataset/Dataset_Hybrid_1/{Q*}/{approach}/patterns/{hash}/training_cleaned.csv
                    |
                    v
         01_Feature_Selection.py (Pattern FFS)
                    |
                    v
         {Q*}/{approach}/SVM/two_step_evaluation_overview.csv
                    |
                    v
         02_Pretrain_Models.py (Pattern-Training with FFS features)
                    |
                    v
         {Q*}/{approach}/Model/{target}/{hash}/model.pkl
                    |
                    v
              03_Predict.py
                    |
                    v
         {Q*}/{approach}/predictions.csv
```

## 00 - Batch_Workflow.py

**Purpose:** Run complete Hybrid_1 workflow (Pattern-Training + Prediction).

**Usage:**
```bash
python3 00_Batch_Workflow.py
```

**Executes:**
1. `02_Pretrain_Models.py` - Train pattern models
2. `03_Predict.py` - Run hybrid prediction

## 01 - Feature_Selection.py

**Purpose:** Forward feature selection for pattern models using used_patterns from Dry-Run.

**Inputs:**
- `../../Dataset/Dataset_Hybrid_1/{Q*}/{approach}/used_patterns.csv` - Patterns to process (from Dry-Run)
- `../../Dataset/Dataset_Hybrid_1/{Q*}/{approach}/patterns/{hash}/training_cleaned.csv` - Training data

**Outputs per Template:**
- `{Q*}/{approach}/SVM/two_step_evaluation_overview.csv` - FFS results with final_features
- `{Q*}/{approach}/SVM/{target}/{hash}_csv/ffs_results_seed42.csv`
- `{Q*}/{approach}/SVM/{target}/{hash}_csv/selected_features_seed42.csv`
- `{Q*}/{approach}/SVM/{target}/{hash}_csv/final_features.csv`

**Variables:**
- `--templates` - Templates to process (default: all 14)
- `--approaches` - Approaches to process (default: approach_3)

**Usage:**
```bash
python3 01_Feature_Selection.py
python3 01_Feature_Selection.py --templates Q1 Q3
```

## 02 - Pretrain_Models.py

**Purpose:** Train SVM models for patterns using FFS-selected features. Operators come from Operator_Level.

**Inputs:**
- `{Q*}/{approach}/SVM/two_step_evaluation_overview.csv` - FFS results with features (from 01_Feature_Selection)
- `../../Dataset/Dataset_Hybrid_1/{Q*}/{approach}/patterns/{hash}/training_cleaned.csv` - Training data

**Outputs per Template:**
- `{Q*}/{approach}/Model/{target}/{hash}/model.pkl` - Pattern models

**Pattern Features:**
- All columns except metadata and targets
- **Timing-Features excluded:** `*_st1`, `*_rt1`, `*_st2`, `*_rt2` (filled from prediction cache at runtime)

**Variables:**
- `--templates` - Templates to process (default: all 14)
- `--approaches` - Approaches to process (default: approach_3)

**Usage:**
```bash
python3 02_Pretrain_Models.py
python3 02_Pretrain_Models.py --templates Q1 Q3
```

## 03 - Predict.py

**Purpose:** Hybrid bottom-up prediction using pattern models + Operator_Level models.

**Inputs:**
- `../../Dataset/Dataset_Operator/{Q*}/test.csv` - Test data
- `../../Dataset/Dataset_Hybrid_1/{Q*}/{approach}/patterns_filtered.csv` - Pattern matching list
- `{Q*}/{approach}/Model/` - Pattern models from 02_Pretrain_Models.py
- `../Operator_Level/{Q*}/Model/` - Operator models (FFS-trained)
- `../Operator_Level/{Q*}/SVM/two_step_evaluation_overview.csv` - Operator features

**Outputs per Template:**
- `{Q*}/{approach}/predictions.csv` - Hybrid predictions
- `{Q*}/{approach}/md/03_{template}.md` - Debug reports (--report only)

**Variables:**
- `--templates` - Templates to process (default: all 14)
- `--approaches` - Approaches to process (default: approach_3)
- `--report` - Generate MD reports for debugging (default: off)

**Usage:**
```bash
python3 03_Predict.py
python3 03_Predict.py --templates Q1 Q3
python3 03_Predict.py --templates Q1 --report
```

**Pattern Matching:**
- Greedy assignment: longest patterns first
- Tie-breaking: `pattern_length` DESC, then `occurrence_count` DESC
- Single-Pattern-Constraint: Skip if pattern would consume ALL nodes

**Operator Fallback:**
- Model exists → Prediction with `max(0.0, ...)`
- No model + Leaf → `{start: 0.0, exec: 0.0}`
- No model + Non-Leaf → `max(child predictions)` (Passthrough)

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

## A_01b - Static_Dynamic_Comparison.py

**Purpose:** Compare Static (Baseline_SVM) vs Dynamic (LOTO) MRE per template.

**Inputs:**
- `--static-csv` - Path to Static template MRE CSV (from Hybrid_1/Runtime_Prediction/Baseline_SVM)
- `Evaluation/{approach}/loto_mre.csv` - Dynamic MRE from A_01a

**Outputs:**
- `{output-dir}/A_01b_static_dynamic_comparison.csv` - Combined MRE data
- `{output-dir}/A_01b_static_dynamic_comparison.png` - Grouped bar plot

**Usage:**
```bash
python3 A_01b_Static_Dynamic_Comparison.py \
  --static-csv /path/to/Hybrid_1/Runtime_Prediction/Baseline_SVM/Evaluation/approach_3/A_01a_template_mre.csv \
  --output-dir Evaluation/approach_3
```

## A_01c - Pattern_Comparison.py

**Purpose:** Compare pattern usage between Static and Dynamic per template.

**Inputs:**
- `--static-predictions` - Path to Static predictions.csv
- `--static-patterns` - Path to Static patterns.csv
- Dynamic data loaded from local `{Q*}/{approach}/predictions.csv` and `Dataset/Dataset_Hybrid_1/{Q*}/{approach}/used_patterns.csv`

**Outputs:**
- `{output-dir}/A_01c_pattern_comparison.csv` - Pattern details (hash, string, length, source)

**Usage:**
```bash
python3 A_01c_Pattern_Comparison.py \
  --static-predictions /path/to/Hybrid_1/.../predictions.csv \
  --static-patterns /path/to/Hybrid_1/.../patterns.csv
```

## A_01d - Pattern_Statistics.py

**Purpose:** Export pattern reduction statistics (available vs used patterns per template).

**Inputs:**
- `../../Dataset/Dataset_Hybrid_1/{Q*}/{approach}/patterns_filtered.csv` - Available patterns
- `../../Dataset/Dataset_Hybrid_1/{Q*}/{approach}/used_patterns.csv` - Used patterns (from Dry-Run)

**Outputs:**
- `{output-dir}/A_01d_pattern_statistics.csv` - Statistics with columns: template, available_patterns, used_patterns, reduction_pct

**Usage:**
```bash
python3 A_01d_Pattern_Statistics.py --output-dir Evaluation/approach_3
```

**Variables:**
- `--approach` - Approach to analyze (default: approach_3)
- `--output-dir` - Output directory for CSV (required)
