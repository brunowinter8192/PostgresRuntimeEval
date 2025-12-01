# Runtime_Prediction - DOCS.md

## Shared Infrastructure

**ffs_config.py:**
- `SEED = 42`: Random seed for reproducibility
- `MIN_FEATURES = 1`: Minimum features before stopping criterion applies
- `SVM_PARAMS`: NuSVR configuration (kernel='rbf', nu=0.65, C=1.5, gamma='scale')

## Workflow Execution Order

```
Phase 1: Operator Baseline (on Training_Training/Training_Test)
01 (FFS) -> 02 (Train) -> 04 (Predict) -> A_02a/A_02b

Phase 2: Pattern Preparation
05 (Pattern FFS) -> 06 -> 07 -> 08 (Error_Baseline) -+
                                 09 (Pretrain)       -+-> parallel

Phase 3: Pattern Selection (parallel, independent)
10 --strategy frequency -+
10 --strategy size      -+-> A_01a/A_01b per selection
10 --strategy error     -+

Phase 4: Final Training + Prediction (on Training.csv/Test.csv)
11a (Operators) -> 11b (Patterns per method) -> 12 (Predictions) -> A_01a/A_01b (Evaluation)

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

### 05 - Pattern_FFS.py

**Purpose:** Forward feature selection for each pattern with two-step evaluation.

**Workflow:**
1. Load pattern list from 01_patterns_*.csv
2. For each pattern: load training_cleaned.csv from Patterns/{hash}/
3. Run FFS with pattern-specific features
4. Identify missing child features (complex naming: {Op}_{Outer/Inner}_{st1/rt1/...})
5. Filter out child features for LEAF_OPERATORS (Seq Scan, Index Scan, Index Only Scan)
6. Export final features

**Inputs:**
- `patterns_csv`: Path to Data_Generation/csv/01_patterns_*.csv
- `dataset_dir`: Path to Dataset/Patterns/

**Outputs:**
- `{output-dir}/Pattern/{target}/{hash}_csv/final_features.csv`
- `{output-dir}/Pattern/pattern_ffs_overview.csv`

**Usage:**
```
python3 05_Pattern_FFS.py ../Data_Generation/csv/01_patterns_*.csv ../Dataset/Patterns --output-dir SVM
```

---

### 05b - Clean_Pattern_FFS.py

**Purpose:** Remove child features (st1/rt1/st2/rt2) for LEAF_OPERATORS from pattern_ffs_overview.csv.

**Workflow:**
1. Load pattern_ffs_overview.csv
2. For each pattern: filter out child features belonging to Seq Scan, Index Scan, Index Only Scan
3. Update final_features and final_feature_count
4. Export cleaned CSV

**Inputs:**
- `input_file`: Path to pattern_ffs_overview.csv

**Outputs:**
- Cleaned pattern_ffs_overview.csv (in-place or new file)

**Usage:**
```
python3 05b_Clean_Pattern_FFS.py SVM/Pattern/Training_Training/pattern_ffs_overview.csv --output-file SVM/Pattern/Training_Training/pattern_ffs_overview.csv
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

**Purpose:** Order patterns by two strategies for greedy selection.

**Workflow:**
1. Load test pattern occurrences from 06
2. Aggregate by pattern: count occurrences
3. Sort by SIZE: operator_count ASC, occurrence_count DESC
4. Sort by FREQUENCY: occurrence_count DESC, operator_count ASC

**Inputs:**
- `occurrences_file`: Path to 06_test_pattern_occurrences_*.csv

**Outputs:**
- `07_patterns_by_size.csv`
- `07_patterns_by_frequency.csv`

**Usage:**
```
python3 07_Order_Patterns.py Pattern_Selection/06_test_pattern_occurrences_*.csv --output-dir Pattern_Selection
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
- `{output-dir}/pretrain_summary.csv`

**Variables:**
- `--n-jobs`: Parallel jobs (-1 = all cores)

**Usage:**
```
python3 09_Pretrain_Patterns.py SVM/Pattern/pattern_ffs_overview.csv Pattern_Selection/07_patterns_by_frequency.csv ../Dataset/Baseline/Training_Training.csv --output-dir Model/Patterns_Pretrained --n-jobs -1
```

---

### 10 - Pattern_Selection.py

**Purpose:** Greedy pattern selection with configurable strategy.

**Strategies:**
- `frequency`: Static ordering by occurrence count DESC
- `size`: Static ordering by operator count ASC
- `error`: Dynamic re-ranking by error score after each selection

**Workflow:**
1. Load operator models, pattern FFS, sorted patterns
2. Set baseline MRE (operator-only)
3. For each pattern (static or dynamic order):
   - Load/train pattern model
   - Predict test set with current selected + candidate
   - If MRE improves: SELECT and update baseline
   - Else: REJECT
   - (error only) Re-rank remaining patterns based on updated predictions
4. Export selection log, selected patterns, per-pattern predictions

**Inputs:**
- `--strategy`: Selection strategy (frequency/size/error)
- `sorted_patterns_file`: 07_patterns_by_frequency.csv, 07_patterns_by_size.csv, or 08_patterns_by_error.csv
- `pattern_ffs_file`: pattern_ffs_overview.csv
- `training_file`: Training_Training.csv
- `test_file`: Training_Test.csv
- `operator_model_dir`: Model/Operator/
- `operator_ffs_dir`: SVM/Operator/

**Outputs:**
- `{pattern-output-dir}/{hash}/predictions.csv`
- `{pattern-output-dir}/selection_log.csv`
- `{pattern-output-dir}/selected_patterns.csv`
- `{model-dir}/{hash}/` (selected models)

**Variables:**
- `--pretrained-dir`: Path to pretrained models (skip re-training)
- `--pattern-occurrences-file`: Required for error strategy (06_test_pattern_occurrences_*.csv)

**Usage:**
```
# Frequency strategy
python3 10_Pattern_Selection.py --strategy frequency Pattern_Selection/07_patterns_by_frequency.csv SVM/Pattern/pattern_ffs_overview.csv ../Dataset/Baseline/Training_Training.csv ../Dataset/Baseline/Training_Test.csv Model/Operator SVM/Operator --pattern-output-dir Pattern_Selection/Frequency --model-dir Model/Selected_Pattern/Frequency --pretrained-dir Model/Patterns_Pretrained

# Size strategy
python3 10_Pattern_Selection.py --strategy size Pattern_Selection/07_patterns_by_size.csv SVM/Pattern/pattern_ffs_overview.csv ../Dataset/Baseline/Training_Training.csv ../Dataset/Baseline/Training_Test.csv Model/Operator SVM/Operator --pattern-output-dir Pattern_Selection/Size --model-dir Model/Selected_Pattern/Size --pretrained-dir Model/Patterns_Pretrained

# Error strategy (with dynamic re-ranking)
python3 10_Pattern_Selection.py --strategy error Pattern_Selection/08_patterns_by_error.csv SVM/Pattern/pattern_ffs_overview.csv ../Dataset/Baseline/Training_Training.csv ../Dataset/Baseline/Training_Test.csv Model/Operator SVM/Operator --pattern-output-dir Pattern_Selection/Error --model-dir Model/Selected_Pattern/Error --pretrained-dir Model/Patterns_Pretrained --pattern-occurrences-file Pattern_Selection/06_test_pattern_occurrences_*.csv
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

### 12 - Query_Prediction.py

**Purpose:** Bottom-up prediction on Test.csv using final models.

**Workflow:**
1. Load Test.csv (filter main plan)
2. Load operator models + features
3. If pattern args provided: Load pattern models + features + info
4. For each query:
   - Build tree structure
   - Bottom-up from leaves
   - Try pattern match first, fallback to operator
   - Store predictions
5. Export predictions.csv

**Inputs:**
- `test_file`: Path to Test.csv
- `operator_model_dir`: Path to Model/Final_Operator/
- `operator_overview_file`: Path to two_step_evaluation_overview.csv

**Optional Inputs (for pattern prediction):**
- `--pattern-model-dir`: Path to pattern models
- `--pattern-ffs-file`: Path to pattern_ffs_overview.csv
- `--selected-patterns`: Path to selected_patterns.csv

**Outputs:**
- `{output-dir}/predictions.csv`

**Usage:**
```
# Operator-only baseline
python3 12_Query_Prediction.py ../Dataset/Test.csv Model/Final_Operator SVM/Operator/two_step_evaluation_overview.csv --output-dir Evaluation/Operator_Test

# With patterns (e.g., Frequency)
python3 12_Query_Prediction.py ../Dataset/Test.csv Model/Final_Operator SVM/Operator/two_step_evaluation_overview.csv --pattern-model-dir Model/Final_Frequency --pattern-ffs-file SVM/Pattern/pattern_ffs_overview.csv --selected-patterns Selected_Patterns/Pattern_Freq/selected_patterns.csv --output-dir Evaluation/Frequency_Test
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

### A_01b - Operator_Analysis.py

**Purpose:** Cross-tabulation of MRE by node_type and template.

**Workflow:**
1. Load predictions.csv
2. Calculate MRE for all operators
3. Create pivot tables (node_type x template)
4. Export for total_time and startup_time

**Inputs:**
- `predictions_csv`: Any predictions.csv

**Outputs:**
- `{output-dir}/node_type_mean_mre_total_pct_{timestamp}.csv`
- `{output-dir}/node_type_mean_mre_startup_pct_{timestamp}.csv`

**Usage:**
```
python3 A_02b_Operator_Analysis.py Evaluation/Operator_Training_Test/predictions.csv --output-dir Evaluation/Operator_Training_Test
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

