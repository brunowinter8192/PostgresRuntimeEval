# Runtime_Prediction - DOCS.md

## Shared Infrastructure

**ffs_config.py:**
- `SEED = 42`: Random seed for reproducibility
- `MIN_FEATURES = 1`: Minimum features before stopping criterion applies
- `SVM_PARAMS`: NuSVR configuration (kernel='rbf', nu=0.65, C=1.5, gamma='scale')

## Workflow Execution Order

```
Phase 1: Operator Baseline (on Training_Training/Training_Test)
01 (FFS) -> 02 (Train) -> 04 (Predict) -> A_02a

Phase 2: Pattern Preparation (FFS features inherited from Training_Full)
06 -> 07 -> 08 (Error_Baseline) -+
             09 (Pretrain)       -+-> parallel

Phase 3: Pattern Selection (parallel, independent)
10_Pattern_Selection/ --strategy frequency -+
10_Pattern_Selection/ --strategy size      -+-> A_01a per selection
10_Pattern_Selection/ --strategy error     -+

Phase 4: Final Training + Prediction (on Training.csv/Test.csv)
11a (Operators) -> 11b (Patterns per method) -> 12_Query_Prediction/ -> A_01a (Evaluation)

Phase 5: Parameter Analysis (parallel, standalone)
A_02a-A_02c, A_03a
```

## Script Documentation

### 01 - Operator_FFS.py

**Purpose:** Forward feature selection for each operator-target combination with two-step evaluation (add missing child features).

**Workflow:**
1. For each operator and target (execution_time, start_time)
2. Run forward feature selection with 5-fold stratified CV
3. Identify missing child features (st1, rt1, st2, rt2)
4. Evaluate MRE with and without child features
5. Export final features and overview

**Inputs:**
- `dataset_dir`: Directory with operator folders (Dataset/Operators/Training_Training/)

**Outputs:**
- `{output-dir}/{target}/{Operator}_csv/ffs_results_seed42.csv`
- `{output-dir}/{target}/{Operator}_csv/selected_features_seed42.csv`
- `{output-dir}/{target}/{Operator}_csv/final_features.csv`
- `{output-dir}/two_step_evaluation_overview.csv`

**Usage:**
```
python3 01_Operator_FFS.py ../Dataset/Operators/Training_Training --output-dir SVM/Operator/Training_Training
```

---

### 02 - Operator_Train.py

**Purpose:** Train SVM models for each operator-target using final features from 01.

**Workflow:**
1. Load two_step_evaluation_overview.csv
2. For each operator-target: train NuSVR pipeline (MaxAbsScaler + NuSVR)
3. Save model.pkl

**Inputs:**
- `dataset_dir`: Directory with operator CSV files (e.g., Dataset/Operators/Training_Training/)
- `overview_file`: Path to two_step_evaluation_overview.csv

**Outputs:**
- `{output-dir}/{target}/{Operator}/model.pkl`

**Usage:**
```
# Training_Training models
python3 02_Operator_Train.py ../Dataset/Operators/Training_Training SVM/Operator/Training_Training/two_step_evaluation_overview.csv --output-dir Model/Operator/Training_Training

# Training_Full models
python3 02_Operator_Train.py ../Dataset/Operators/Training_Full SVM/Operator/Training_Full/two_step_evaluation_overview.csv --output-dir Model/Operator/Training_Full
```

---

### 04 - Query_Prediction.py

**Purpose:** Bottom-up query prediction using operator models only (baseline).

**Workflow:**
1. Load test data and operator models
2. For each query: predict leaf operators first
3. Propagate predictions upward (st1/rt1/st2/rt2 from children)
4. Export all operator predictions

**Inputs:**
- `test_file`: Path to Training_Test.csv
- `overview_file`: Path to two_step_evaluation_overview.csv
- `models_dir`: Path to Model/Operator/

**Outputs:**
- `{output-file}`: predictions.csv with actual/predicted times

**Usage:**
```
python3 04_Query_Prediction.py ../Dataset/Training_Test.csv SVM/Operator/two_step_evaluation_overview.csv Model/Operator --output-file Evaluation/Operator_Training_Test/predictions.csv
```

---

### 06 - Extract_Test_Patterns.py

**Purpose:** Find occurrences of known patterns in test set.

**Workflow:**
1. Load test data (Training_Test.csv)
2. Load known patterns from Data_Generation
3. Build tree for each query, compute pattern hashes
4. Match against known patterns, record occurrences

**Inputs:**
- `test_file`: Path to Training_Test.csv
- `patterns_file`: Path to 01_patterns_*.csv

**Outputs:**
- `06_test_pattern_occurrences_{timestamp}.csv`

**Usage:**
```
python3 06_Extract_Test_Patterns.py ../Dataset/Baseline/Training_Test.csv ../Data_Generation/csv/Training_Training/01_patterns_*.csv --output-dir Pattern_Selection
```

---

### 07 - Order_Patterns.py

**Purpose:** Order patterns by two strategies for greedy selection, including avg_mre for threshold filtering.

**Workflow:**
1. Load test pattern occurrences from 06
2. Load operator predictions to calculate avg_mre per pattern
3. Aggregate by pattern: count occurrences, calculate avg_mre
4. Sort by SIZE and FREQUENCY strategies

**Sorting Strategies:**

| Strategy | Primary | Secondary | Tiebreaker |
|----------|---------|-----------|------------|
| Size | operator_count ASC | occurrence_count DESC | pattern_hash ASC |
| Frequency | occurrence_count DESC | operator_count ASC | pattern_hash ASC |

**Tiebreaker:** `pattern_hash` (alphabetisch) garantiert deterministische Reihenfolge bei gleichen Werten.

**Inputs:**
- `occurrences_file`: Path to 06_test_pattern_occurrences_*.csv
- `--operator-predictions`: Path to operator predictions CSV (for avg_mre calculation)

**Outputs:**
- `07_patterns_by_size.csv` (includes avg_mre column)
- `07_patterns_by_frequency.csv` (includes avg_mre column)

**Usage:**
```
python3 07_Order_Patterns.py Pattern_Selection/06_test_pattern_occurrences_*.csv --operator-predictions Evaluation/Operator_Training_Training_on_Test/predictions.csv --output-dir Pattern_Selection
```

---

### 08 - Error_Baseline.py

**Purpose:** Calculate error score for each pattern based on operator baseline predictions.

**Workflow:**
1. Load pattern occurrences and operator predictions
2. For each pattern: lookup MRE at root_node_id in operator predictions
3. Calculate error_score = occurrence_count * avg_mre
4. Sort by error_score DESC (highest error = most potential improvement)

**Inputs:**
- `pattern_occurrences_file`: 06_test_pattern_occurrences_*.csv
- `operator_predictions_file`: Operator baseline predictions.csv
- `patterns_metadata_file`: 07_patterns_by_frequency.csv

**Outputs:**
- `08_patterns_by_error.csv`

**Usage:**
```
python3 08_Error_Baseline.py Pattern_Selection/06_*.csv Evaluation/Operator_Training_Test/predictions.csv Pattern_Selection/07_patterns_by_frequency.csv --output-dir Pattern_Selection
```

---

### 09 - Pretrain_Patterns.py

**Purpose:** Train SVM models for all patterns in parallel (speedup for selection).

**Workflow:**
1. Load pattern FFS features and metadata
2. Filter patterns with valid FFS for both targets
3. Parallel training: aggregate pattern data on-the-fly, train NuSVR
4. Save model_execution_time.pkl, model_start_time.pkl, features.json

**Inputs:**
- `pattern_ffs_file`: Path to pattern_ffs_overview.csv
- `patterns_metadata_file`: Path to 07_patterns_by_frequency.csv
- `training_file`: Path to Training_Training.csv

**Outputs:**
- `{output-dir}/{hash}/model_execution_time.pkl`
- `{output-dir}/{hash}/model_start_time.pkl`
- `{output-dir}/{hash}/features.json`

**Variables:**
- `--n-jobs`: Parallel jobs (-1 = all cores)

**Usage:**
```
python3 09_Pretrain_Patterns.py SVM/Pattern/pattern_ffs_overview.csv Pattern_Selection/07_patterns_by_frequency.csv ../Dataset/Baseline/Training_Training.csv --output-dir Model/Patterns_Pretrained --n-jobs -1
```

---

### 10 - Pattern_Selection/

**Purpose:** Greedy pattern selection for runtime prediction improvement. Iteratively evaluates patterns and selects those that improve MRE over operator-only baseline.

**Structure:**
```
10_Pattern_Selection/
├── 10_Pattern_Selection.py     # Entry-point (argparse + orchestrator)
└── src/
    ├── tree.py                 # Tree building + pattern hashing
    ├── io.py                   # Load/export functions
    ├── prediction.py           # Training + prediction + aggregation
    ├── selection.py            # Selection strategies
    └── DOCS.md                 # Function documentation
```

**Baseline:** Operator-only prediction on Training_Test = 22.97% MRE. Selection accepts patterns that improve this baseline.

**Selection Strategies:**

| Strategy | Description | Pattern Order |
|----------|-------------|---------------|
| `frequency` | Static: iterate by occurrence count | 06_patterns_by_frequency.csv |
| `size` | Static: iterate by pattern size | 06_patterns_by_size.csv |
| `error` | Dynamic: re-rank by current error | 10_patterns_by_error.csv |

**Error-Score Formula (error strategy):**
```
error_score = occurrence_count * avg_mre
```
Combines frequency and current prediction error. After each SELECTED/REJECTED decision, error scores are recalculated based on updated predictions.

**Inputs:**
- `sorted_patterns_file`: Patterns ranked by strategy (07_patterns_by_*.csv or 08_patterns_by_error.csv)
- `pattern_ffs_file`: Pattern feature selection results (pattern_ffs_overview.csv)
- `training_file`: Training data (Training_Training.csv)
- `test_file`: Validation data (Training_Test.csv)
- `operator_model_dir`: Pre-trained operator models (Model/Operator/)
- `operator_ffs_dir`: Operator FFS results (SVM/Operator/)
- `--pattern-occurrences-file`: Required for error strategy (06_test_pattern_occurrences_*.csv)
- `--min-error-threshold`: Min avg_mre to consider pattern (default: 0.1, size/frequency only)

**Min Error Threshold (Paper Section 5.3.4):**
Patterns with avg_mre < threshold are skipped for size/frequency strategies. Prevents low-error patterns from consuming nodes that could be better served by high-error patterns. Error strategy does not use this filter (error_score naturally deprioritizes low-error patterns).

**Outputs:**
- `{pattern_hash}/predictions.csv`: Per-pattern node-level predictions
- `{pattern_hash}/mre.csv`: Per-pattern MRE summary
- `{pattern_hash}/status.txt`: SELECTED/REJECTED/SKIPPED_NO_FFS/SKIPPED_LOW_ERROR
- `selection_log.csv`: Full iteration log with all patterns
- `selected_patterns.csv`: Filtered log (SELECTED only) - **used as pattern_order in 12_Query_Prediction**
- `selection_summary.csv`: Aggregate counts and final MRE

**Usage (Static - Frequency):**
```bash
python3 10_Pattern_Selection/10_Pattern_Selection.py \
    --strategy frequency \
    Pattern_Selection/06_patterns_by_frequency.csv \
    SVM/Pattern/Training_Training/pattern_ffs_overview.csv \
    ../Dataset/Baseline/Training_Training.csv \
    ../Dataset/Baseline/Training_Test.csv \
    Model/Operator/Training_Training \
    SVM/Operator/Training_Training \
    --pattern-output-dir Pattern_Selection/Frequency \
    --model-dir Model/Selected_Pattern/Frequency \
    --pretrained-dir Model/Patterns/Training_Training
```

**Usage (Dynamic - Error):**
```bash
python3 10_Pattern_Selection/10_Pattern_Selection.py \
    --strategy error \
    Pattern_Selection/08_patterns_by_error.csv \
    SVM/Pattern/Training_Training/pattern_ffs_overview.csv \
    ../Dataset/Baseline/Training_Training.csv \
    ../Dataset/Baseline/Training_Test.csv \
    Model/Operator/Training_Training \
    SVM/Operator/Training_Training \
    --pattern-output-dir Pattern_Selection/Error \
    --model-dir Model/Selected_Pattern/Error \
    --pretrained-dir Model/Patterns/Training_Training \
    --pattern-occurrences-file Pattern_Selection/06_test_pattern_occurrences_*.csv
```

---

### 11a - Train_Final_Operators.py

**Purpose:** Train operator models on full Training.csv (not Training_Training.csv).

**Workflow:**
1. Load Training.csv (filter main plan)
2. Load feature overview (final_features per operator-target)
3. For each operator-target: train NuSVR with selected features
4. Save models + training summary

**Inputs:**
- `training_file`: Path to Training.csv
- `overview_file`: Path to two_step_evaluation_overview.csv

**Outputs:**
- `Model/Final_Operator/{target}/{Operator}/model.pkl`
- `Model/Final_Operator/training_summary.csv`

**Usage:**
```
python3 11a_Train_Final_Operators.py ../Dataset/Training.csv SVM/Operator/two_step_evaluation_overview.csv --output-dir Model/Final_Operator
```

---

### 11b - Train_Final_Patterns.py

**Purpose:** Train selected patterns on full Training.csv.

**Workflow:**
1. Load selected pattern hashes from selected_patterns.csv
2. Load pattern FFS features
3. For each selected pattern (parallel):
   - Find all occurrences in Training.csv
   - Aggregate pattern features
   - Train NuSVR for execution_time and start_time
   - Save models + features.json
4. Export training summary

**Inputs:**
- `selected_patterns_file`: Path to selected_patterns.csv
- `pattern_ffs_file`: Path to pattern_ffs_overview.csv
- `training_file`: Path to Training.csv

**Outputs:**
- `{output-dir}/{hash}/model_execution_time.pkl`
- `{output-dir}/{hash}/model_start_time.pkl`
- `{output-dir}/{hash}/features.json`
- `{output-dir}/training_summary.csv`

**Variables:**
- `--n-jobs`: Parallel jobs (-1 = all cores)

**Usage:**
```
python3 11b_Train_Final_Patterns.py Selected_Patterns/Pattern_Freq/selected_patterns.csv SVM/Pattern/pattern_ffs_overview.csv ../Dataset/Training.csv --output-dir Model/Final_Frequency --n-jobs -1
```

---

### 12 - Query_Prediction/

**Purpose:** Bottom-up query prediction using operator and pattern models. Generates per-query MD reports showing prediction steps.

**Structure:**
```
12_Query_Prediction/
├── 12_Query_Prediction.py      # Entry-point (argparse + orchestrator)
└── src/
    ├── tree.py                 # Tree building + pattern matching
    ├── prediction.py           # Prediction logic + feature aggregation
    ├── io.py                   # Load/export functions
    ├── report.py               # MD report generation
    └── DOCS.md                 # Function documentation
```

**Pattern-Matching Priority:**
- `pattern_order` is read from `selected_patterns.csv` (selection order from 10_Pattern_Selection)
- `build_pattern_assignments()` iterates patterns in this order: **first match wins**
- If Pattern A (position 1) and Pattern B (position 5) both match Node X, Pattern A is used
- Matched nodes are "consumed" and unavailable for later patterns

**Inputs:**
- `test_file`: Query operators to predict (Test.csv)
- `operator_model_dir`: Pre-trained operator models (Model/Operators_Training/)
- `operator_overview_file`: Feature overview (two_step_evaluation_overview.csv)
- `--pattern-model-dir`: Path to pattern models (optional)
- `--pattern-ffs-file`: Path to pattern FFS overview (optional)
- `--selected-patterns`: Path to selected_patterns.csv (optional)
- `--pattern-metadata`: Path to pattern metadata CSV (optional)

**Outputs:**
- `predictions.csv`: Node-level predictions with actual/predicted times, pattern_hash column
- `patterns.csv`: Pattern usage summary (pattern_hash, usage_count, node_types)
- `md/12_{template}_{plan_hash[:8]}_{timestamp}.md`: One MD report per unique plan structure

**Usage (Operator-Only):**
```bash
python3 12_Query_Prediction/12_Query_Prediction.py \
    ../Dataset/Test.csv \
    Model/Operators_Training \
    SVM/Operator/two_step_evaluation_overview.csv \
    --output-dir Evaluation/Operator_Only
```

**Usage (Pattern-Enhanced):**
```bash
python3 12_Query_Prediction/12_Query_Prediction.py \
    ../Dataset/Test.csv \
    Model/Operators_Training \
    SVM/Operator/two_step_evaluation_overview.csv \
    --strategy frequency \
    --pattern-model-dir Model/Selected_Pattern/Frequency \
    --pattern-ffs-file SVM/Pattern/pattern_ffs_overview.csv \
    --selected-patterns Pattern_Selection/Frequency/selected_patterns.csv \
    --pattern-metadata Pattern_Selection/07_patterns_by_frequency.csv \
    --output-dir Evaluation/Pattern_Frequency
```

---

### A_01a - Query_Evaluation.py

**Purpose:** Evaluate query-level prediction accuracy on root operators.

**Workflow:**
1. Load predictions.csv
2. Filter depth=0 (root operators)
3. Calculate MRE per template and overall
4. Export metrics and bar plot

**Inputs:**
- `predictions_file`: Any predictions.csv

**Outputs:**
- `{output-dir}/overall_mre.csv`
- `{output-dir}/template_mre.csv`
- `{output-dir}/template_mre_plot.png`

**Usage:**
```
python3 A_02a_Query_Evaluation.py Evaluation/Operator_Training_Test/predictions.csv --output-dir Evaluation/Operator_Training_Test
```

---

### A_02a - Epsilon_Analysis.py

**Purpose:** Analyze delta distribution for EPSILON threshold determination.

**Workflow:**
1. Load selection_log.csv
2. Filter SELECTED patterns
3. Calculate delta statistics (mean, median, min, max)

**Inputs:**
- `selection_log_file`: Path to selection_log.csv

**Outputs:** `{output-dir}/delta_stats.csv`
- Columns: selected_count;mean_delta;median_delta;min_delta;max_delta

**Usage:**
```
python3 A_02a_Epsilon_Analysis.py Pattern_Selection/Error/selection_log.csv --output-dir Evaluation/Pattern_Test_Full_Error/Epsilon
```

---

### A_02b - Convergence_Analysis.py

**Purpose:** Determine early stopping point and recommended MRE threshold.

**Outputs:** `{output-dir}/A_02b_phases.csv`, `A_02b_summary.csv`, `A_02b_mre_progression.png`

**Usage:**
```
python3 A_02b_Convergence_Analysis.py Pattern_Selection/Error/selection_log.csv --output-dir Evaluation/Pattern_Test_Full_Error/Convergenz
```

---

### A_02c - Occurrence_Analysis.py

**Purpose:** Analyze correlation between pattern occurrence and selection impact.

**Inputs:**
- `selection_log`: Path to selection_log.csv (one method)
- `patterns_metadata`: Path to 07_patterns_by_frequency.csv

**Outputs:** `{output-dir}/A_02c_occurrence.csv`
- Columns: occurrence_class;occ_min;occ_max;patterns_total;patterns_selected;selection_rate;total_delta;avg_delta

**Usage:**
```
python3 A_02c_Occurrence_Analysis.py Pattern_Selection/Error/selection_log.csv Pattern_Selection/07_patterns_by_frequency.csv --output-dir Evaluation/Pattern_Test_Full_Error/Occurrence
```

---

### A_03a - Feature_Frequency.py

**Purpose:** Determine universal feature set for Online prediction (no FFS possible online).

**Workflow:**
1. Load pattern_ffs_overview.csv (all pattern FFS results)
2. Strip operator prefixes from features (e.g., HashJoin_np -> np)
3. Count base feature occurrences across all patterns
4. Export frequency ranking

**Inputs:**
- `ffs_overview`: Path to SVM/Pattern/Training_Training/pattern_ffs_overview.csv

**Outputs:** `{output-dir}/A_03a_feature_frequency.csv`
- Columns: feature;count;percentage

**Usage:**
```
python3 A_03a_Feature_Frequency.py SVM/Pattern/Training_Training/pattern_ffs_overview.csv --output-dir Parameter_Evaluation
```

**Online-Relevanz:** Features mit hoher Frequenz bilden das feste Feature-Set fuer Online-Pattern-Modelle (keine individuelle FFS moeglich).

