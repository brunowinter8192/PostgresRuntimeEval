# Runtime_Prediction Module Documentation

## Directory Structure

```
Runtime_Prediction/
├── workflow.py                     # Main orchestrator
├── DOCS.md                         # This documentation
└── src/
    ├── __init__.py                 # Module exports
    ├── tree.py                     # QueryNode, tree building
    ├── aggregation.py              # Pattern aggregation
    ├── training.py                 # Operator + pattern training
    ├── prediction.py               # Bottom-up prediction
    ├── mining.py                   # Pattern mining + ranking
    ├── selection.py                # Pattern selection loop
    ├── metrics.py                  # MRE calculation
    ├── output.py                   # Save models/CSV
    └── report.py                   # ReportBuilder class
```

---

## Shared Infrastructure

**mapping_config.py** (parent directory):
- `SVM_PARAMS`: NuSVR hyperparameters
- `EPSILON`: Minimum improvement threshold (0.01%)
- `MIN_SAMPLES`: Minimum training samples
- `OPERATOR_FEATURES`: Base operator features
- `CHILD_FEATURES_TIMING`: Child timing features
- `TARGET_TYPES`: ['execution_time', 'start_time']
- `get_operator_features()`: Feature set per operator type
- `csv_name_to_folder_name()`: Operator name conversion

---

## Workflow Execution

```
workflow.py
├── Phase A: Operator Training
│   └── train_all_operators() [training.py]
│
├── Phase B: Operator Baseline
│   ├── predict_all_queries_operator_only() [prediction.py]
│   └── calculate_mre() [metrics.py]
│
├── Phase C: Pattern Mining
│   ├── mine_patterns_from_query() [mining.py]
│   ├── find_pattern_occurrences_in_data() [mining.py]
│   └── calculate_error_ranking() [mining.py]
│
├── Phase D: Pattern Selection
│   └── run_pattern_selection() [selection.py]
│       ├── train_single_pattern() [training.py]
│       ├── predict_all_queries_with_patterns() [prediction.py]
│       └── calculate_error_ranking() [mining.py]
│
├── Phase E: Final Prediction
│   ├── train_all_operators() [training.py]
│   ├── train_selected_patterns() [training.py]
│   ├── predict_single_query_with_patterns() [prediction.py]
│   └── calculate_query_mre() [metrics.py]
│
└── Output
    ├── save_models() [output.py]
    ├── save_csv_outputs() [output.py]
    └── report.save() [report.py]
```

---

## Module Documentation

### workflow.py

**Purpose:** Main orchestrator for online prediction workflow

**Functions:**
- `online_prediction_workflow()`: Orchestrates all phases
- `load_data()`: Load CSV and filter to main plan
- `get_query_operators()`: Filter operators for specific query

**Usage:**
```bash
python workflow.py <test_query_file> <training_training_csv> <training_test_csv> \
    <training_csv> <test_csv> --output-dir <output_dir>
```

---

### src/tree.py

**Purpose:** Query tree data structures and traversal

**Classes:**
- `QueryNode`: Tree node with node_type, depth, node_id, children

**Functions:**
- `build_tree_from_dataframe()`: Build tree from flat DataFrame
- `extract_all_nodes()`: Get all nodes as flat list
- `has_children_at_length()`: Check if pattern length is valid
- `count_operators()`: Count operators in pattern subtree
- `extract_pattern_node_ids()`: Get all node IDs in pattern
- `get_children_from_full_query()`: Get direct children from DataFrame

---

### src/aggregation.py

**Purpose:** Aggregate pattern features for training and prediction

**Functions:**
- `aggregate_pattern_for_training()`: Aggregate with actual child times
- `aggregate_pattern_for_prediction()`: Aggregate with predicted child times
- `remove_non_leaf_timing_features()`: Remove non-leaf timing from aggregated data

---

### src/training.py

**Purpose:** Train operator and pattern SVM models

**Functions:**
- `train_all_operators()`: Train models for all operator types
- `train_single_pattern()`: Train model for specific pattern
- `train_selected_patterns()`: Train models for selected patterns

---

### src/prediction.py

**Purpose:** Bottom-up prediction with operators and patterns

**Functions:**
- `predict_all_queries_operator_only()`: Predict all queries with operator models
- `predict_single_query_operator_only()`: Predict single query with operators
- `predict_all_queries_with_patterns()`: Predict all queries with patterns
- `predict_single_query_with_patterns()`: Predict single query with patterns

---

### src/mining.py

**Purpose:** Pattern mining, hashing, and error ranking

**Functions:**
- `mine_patterns_from_query()`: Extract all patterns from query
- `find_pattern_occurrences_in_data()`: Find pattern occurrences in dataset
- `compute_pattern_hash()`: Compute MD5 hash for pattern
- `generate_pattern_string()`: Generate readable pattern string
- `calculate_error_ranking()`: Rank patterns by error contribution

---

### src/selection.py

**Purpose:** Greedy pattern selection loop

**Functions:**
- `run_pattern_selection()`: Main selection loop with epsilon threshold

---

### src/metrics.py

**Purpose:** MRE calculation and result creation

**Functions:**
- `calculate_mre()`: Calculate MRE on root operators
- `calculate_query_mre()`: Calculate MRE for single query
- `create_prediction_result()`: Create prediction result dict

---

### src/output.py

**Purpose:** Save models and CSV outputs

**Functions:**
- `save_models()`: Save operator and pattern models
- `save_csv_outputs()`: Save selection log and predictions

---

### src/report.py

**Purpose:** Markdown report generation

**Classes:**
- `ReportBuilder`: Build and save markdown reports

**Methods:**
- `add_data_summary()`: Add data summary section
- `add_operator_baseline()`: Add operator baseline MRE
- `add_patterns_in_query()`: Add patterns table
- `add_selection_iteration()`: Add selection iteration row
- `add_final_prediction()`: Add final prediction results
- `save()`: Write report to file
