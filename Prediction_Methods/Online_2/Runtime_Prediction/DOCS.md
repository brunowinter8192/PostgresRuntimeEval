# Runtime_Prediction - Online Pattern Selection

Online learning workflow that trains operator models, mines patterns from a test query, and greedily selects patterns that improve prediction accuracy.

## Shared Infrastructure

**Constants from mapping_config.py:**
- `SVM_PARAMS` - NuSVR hyperparameters (kernel, nu, C, gamma)
- `EPSILON` - Minimum improvement threshold (0.01%)
- `MIN_SAMPLES` - Minimum samples for model training
- `OPERATOR_FEATURES` - Base operator features (10 features)
- `CHILD_FEATURES_TIMING` - Child timing features (st1, rt1, st2, rt2)
- `TARGET_TYPES` - Target types ['execution_time', 'start_time']
- `LEAF_OPERATORS` - Leaf node types without child timing
- `get_operator_features()` - Feature set per operator type
- `csv_name_to_folder_name()` - Operator name conversion

## Workflow Execution Order

**Main Pipeline (workflow.py):**
```
Phase A: Operator Training
    |
Phase B: Operator Baseline Prediction
    |
Phase C: Pattern Mining from Test Query
    |
Phase D: Greedy Pattern Selection Loop
    |
Phase E: Final Prediction with Selected Patterns
    |
Output: Models + CSV + Report
```

## Script Documentation

### workflow.py

**Purpose:** Main orchestrator for online prediction workflow

**Workflow:**
1. Load all datasets (Training_Training, Training_Test, Training, Test)
2. Train operator models on Training_Training
3. Predict Training_Test with operators only (baseline)
4. Mine patterns from test query
5. Find pattern occurrences in Training_Test
6. Run greedy pattern selection loop
7. Train final models on full Training set
8. Predict test query with selected patterns
9. Save models, CSV outputs, and report

**Inputs:**
- `test_query_file` - Name of the test query (positional)
- `training_training_csv` - Path to Training_Training.csv (positional)
- `training_test_csv` - Path to Training_Test.csv (positional)
- `training_csv` - Path to Training.csv (positional)
- `test_csv` - Path to Test.csv (positional)

**Outputs:**
- `{output-dir}/models/{query}/operators/` - Operator model pickles
- `{output-dir}/models/{query}/patterns/` - Pattern model pickles + features.json
- `{output-dir}/csv/selection_log_{query}.csv` - Pattern selection iterations
- `{output-dir}/csv/predictions_{query}.csv` - Final predictions
- `{output-dir}/md/02_online_prediction_{query}_{timestamp}.md` - Report

**Usage:**
```bash
python workflow.py Q1_100_seed_812199069 \
    Baseline/Training_Training.csv \
    Baseline/Training_Test.csv \
    Baseline/Training.csv \
    Baseline/Test.csv \
    --output-dir Baseline
```

**Variables:**
- `--output-dir` - Output directory for models, CSV, and reports (required)

---

### batch_predict.sh

**Purpose:** Run workflow.py for all test queries in parallel

**Workflow:**
1. Extract unique query_file values from Test.csv
2. Run workflow.py for each query in parallel (14 jobs)

**Inputs:**
- Hardcoded paths to `../../Hybrid_7/Dataset/Baseline/` datasets

**Outputs:**
- Same as workflow.py, for all 420 test queries

**Usage:**
```bash
./batch_predict.sh
```

---

## Source Modules (src/)

### src/tree.py

**Purpose:** Query tree data structures and traversal

**Functions:**
- `QueryNode` - Tree node class with node_type, depth, node_id, children
- `build_tree_from_dataframe()` - Build tree from flat DataFrame
- `extract_all_nodes()` - Get all nodes as flat list
- `has_children_at_length()` - Check if pattern length is valid
- `count_operators()` - Count operators in pattern subtree
- `extract_pattern_node_ids()` - Get all node IDs in pattern
- `get_children_from_full_query()` - Get direct children from DataFrame

---

### src/aggregation.py

**Purpose:** Aggregate pattern features for training and prediction

**Functions:**
- `aggregate_pattern_for_training()` - Aggregate with actual child times
- `aggregate_pattern_for_prediction()` - Aggregate with predicted child times
- `remove_non_leaf_timing_features()` - Remove non-leaf timing from aggregated data

---

### src/training.py

**Purpose:** Train operator and pattern SVM models

**Functions:**
- `train_all_operators()` - Train models for all operator types
- `train_single_pattern()` - Train model for specific pattern
- `train_selected_patterns()` - Train models for selected patterns

---

### src/prediction.py

**Purpose:** Bottom-up prediction with operators and patterns

**Functions:**
- `predict_all_queries_operator_only()` - Predict all queries with operator models
- `predict_single_query_operator_only()` - Predict single query with operators
- `predict_all_queries_with_patterns()` - Predict all queries with patterns
- `predict_single_query_with_patterns()` - Predict single query with patterns

---

### src/mining.py

**Purpose:** Pattern mining, hashing, and error ranking

**Functions:**
- `mine_patterns_from_query()` - Extract all patterns from query
- `find_pattern_occurrences_in_data()` - Find pattern occurrences in dataset
- `compute_pattern_hash()` - Compute MD5 hash for pattern
- `generate_pattern_string()` - Generate readable pattern string
- `calculate_error_ranking()` - Rank patterns by error contribution

---

### src/selection.py

**Purpose:** Greedy pattern selection loop

**Functions:**
- `run_pattern_selection()` - Main selection loop with epsilon threshold

---

### src/metrics.py

**Purpose:** MRE calculation and result creation

**Functions:**
- `calculate_mre()` - Calculate MRE on root operators
- `calculate_query_mre()` - Calculate MRE for single query
- `create_prediction_result()` - Create prediction result dict

---

### src/output.py

**Purpose:** Save models and CSV outputs

**Functions:**
- `save_models()` - Save operator and pattern models to pickle
- `save_csv_outputs()` - Save selection log and predictions

---

### src/report.py

**Purpose:** Markdown report generation

**Functions:**
- `ReportBuilder` - Class to build and save markdown reports
- `add_data_summary()` - Add data summary section
- `add_operator_baseline()` - Add operator baseline MRE
- `add_patterns_in_query()` - Add patterns table
- `add_selection_iteration()` - Add selection iteration row
- `add_final_prediction()` - Add final prediction results
- `save()` - Write report to file
