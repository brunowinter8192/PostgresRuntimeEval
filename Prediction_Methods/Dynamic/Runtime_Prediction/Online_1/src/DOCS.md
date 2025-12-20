# src/ - Helper Modules

Function-level documentation for Online_1 Runtime_Prediction helper modules.

## Directory Structure

```
src/
    DOCS.md
    __init__.py
    tree.py
    aggregation.py
    training.py
    prediction.py
    mining.py
    selection.py
    metrics.py
    output.py
    report.py
```

## tree.py

Query tree data structures and traversal.

| Function | Description |
|----------|-------------|
| `QueryNode` | Tree node class with node_type, depth, node_id, children |
| `build_tree_from_dataframe()` | Build tree from flat DataFrame |
| `extract_all_nodes()` | Get all nodes as flat list |
| `has_children_at_length()` | Check if pattern length is valid for node |
| `count_operators()` | Count operators in pattern subtree |
| `extract_pattern_node_ids()` | Get all node IDs consumed by pattern |
| `get_children_from_full_query()` | Get direct children from DataFrame |

## aggregation.py

Aggregate pattern features for training and prediction.

| Function | Description |
|----------|-------------|
| `aggregate_pattern_for_training()` | Aggregate with actual child times |
| `aggregate_pattern_for_prediction()` | Aggregate with predicted child times |
| `remove_non_leaf_timing_features()` | Remove non-leaf timing from aggregated data |

## training.py

Train operator and pattern SVM models.

| Function | Description |
|----------|-------------|
| `train_all_operators()` | Train NuSVR models for all operator types |
| `train_single_pattern()` | Train NuSVR model for specific pattern |
| `train_selected_patterns()` | Train models for all selected patterns |

## prediction.py

Bottom-up prediction with operators and patterns.

| Function | Description |
|----------|-------------|
| `predict_all_queries_operator_only()` | Predict all queries with operator models |
| `predict_single_query_operator_only()` | Predict single query bottom-up with operators |
| `predict_all_queries_with_patterns()` | Predict all queries with pattern models |
| `predict_single_query_with_patterns()` | Two-phase prediction: assign patterns, then predict bottom-up |
| `_build_pattern_assignments()` | Assign patterns to nodes by error_score priority |
| `_predict_operator()` | Predict single operator node |
| `_predict_pattern()` | Predict using pattern model |

## mining.py

Pattern mining, hashing, and ranking.

| Function | Description |
|----------|-------------|
| `mine_patterns_from_query()` | Extract all patterns (depth 2-6) from query |
| `find_pattern_occurrences_in_data()` | Find pattern occurrences in dataset |
| `compute_pattern_hash()` | Compute MD5 hash for pattern structure |
| `generate_pattern_string()` | Generate readable pattern string |
| `calculate_ranking()` | Rank patterns by strategy (error/size/frequency) |

## selection.py

Greedy pattern selection loop.

| Function | Description |
|----------|-------------|
| `run_pattern_selection()` | Main loop: iterate patterns, train, evaluate, accept/reject |
| `_create_selection_log_entry()` | Create log entry dict |

## metrics.py

MRE calculation and result creation.

| Function | Description |
|----------|-------------|
| `calculate_mre()` | Calculate MRE on root operators (depth=0) |
| `calculate_query_mre()` | Calculate MRE for single query root |
| `create_prediction_result()` | Create prediction result dict |

## output.py

Save models and CSV outputs.

| Function | Description |
|----------|-------------|
| `save_models()` | Save operator and pattern models to pickle |
| `save_csv_outputs()` | Save selection_log.csv and predictions.csv |

## report.py

Markdown report generation.

| Class/Function | Description |
|----------------|-------------|
| `ReportBuilder` | Class to build markdown report sections |
| `add_data_summary()` | Add dataset summary table |
| `add_operator_baseline()` | Add operator-only baseline MRE |
| `add_patterns_in_query()` | Add patterns table with ranking |
| `add_selection_iteration()` | Add row to selection log table |
| `add_query_tree()` | Add ASCII tree with pattern assignments |
| `add_pattern_assignments()` | Add pattern assignments table |
| `add_final_prediction()` | Add final prediction results |
| `add_prediction_chain()` | Add detailed bottom-up prediction steps |
| `save()` | Write report to file |
