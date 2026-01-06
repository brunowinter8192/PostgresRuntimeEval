# src/ Module Documentation

## Module Overview

| Module | Functions | Responsibility |
|--------|-----------|----------------|
| tree.py | 8 + class | Tree structure + pattern hashing |
| io.py | 14 | Data loading + export |
| prediction.py | 12 | Training + prediction + aggregation |
| selection.py | 4 | Selection strategies |

---

## tree.py

Tree building and pattern matching utilities.

### QueryNode Class

Tree node representing a query plan operator.

**Attributes:**
- `node_type`: Operator type (e.g., "Hash Join")
- `parent_relationship`: "Outer" / "Inner" / ""
- `depth`: Tree depth (0 = root)
- `node_id`: Unique identifier
- `children`: List of child nodes

### Functions

| Function | Purpose |
|----------|---------|
| `build_tree_from_dataframe(query_ops)` | Build tree from flat DataFrame |
| `extract_all_nodes(node)` | Get all nodes recursively |
| `get_children_from_full_query(df, parent_id)` | Find direct children by depth |
| `has_children_at_length(node, length)` | Check subtree depth exists |
| `compute_pattern_hash(node, length)` | MD5 hash of subtree structure |
| `extract_pattern_node_ids(node, length)` | Get all node IDs in pattern |
| `match_pattern(node, pattern_info)` | Find longest matching pattern for node |

---

## io.py

Data loading and export functions.

### Loading Functions

| Function | Purpose |
|----------|---------|
| `load_operator_models(model_dir)` | Load pickled operator models |
| `load_operator_ffs(ffs_dir)` | Load operator FFS features |
| `load_pattern_ffs(file)` | Load pattern FFS from overview CSV |
| `load_sorted_patterns(file)` | Load ranked patterns CSV |
| `load_pattern_occurrences(file)` | Load pattern occurrences (error strategy) |
| `load_training_data(file)` | Load training CSV, filter main plan |
| `load_test_data(file)` | Load test CSV, filter main plan |
| `load_pretrained_model(dir, hash)` | Load pretrained pattern model |

### Export Functions

| Function | Purpose |
|----------|---------|
| `create_log_entry(...)` | Create selection log dict |
| `create_prediction_result(...)` | Create prediction result dict |
| `calculate_mre(predictions)` | Calculate MRE on root operators |
| `save_pattern_model(dir, hash, model)` | Save pattern model to disk |
| `export_pattern_results(...)` | Save per-pattern CSV + status |
| `export_selection_summary(dir, log)` | Save summary CSVs |

---

## prediction.py

Training, prediction, and feature aggregation.

### Training Functions

| Function | Purpose |
|----------|---------|
| `load_or_train_pattern_model(...)` | Load pretrained or train on-the-fly |
| `train_pattern_model(...)` | Train SVM model from aggregated samples |

### Prediction Functions

| Function | Purpose |
|----------|---------|
| `predict_all_queries(...)` | Iterate over unique queries |
| `predict_single_query(...)` | Bottom-up prediction for one query |
| `predict_pattern(...)` | Predict using pattern model |
| `predict_operator(...)` | Predict using operator model |
| `build_operator_features(...)` | Build feature vector with child predictions |

### Aggregation Functions

| Function | Purpose |
|----------|---------|
| `aggregate_pattern(rows, length)` | Aggregate for training (actual values) |
| `aggregate_subtree(...)` | Recursive aggregation for training |
| `aggregate_pattern_with_cache(...)` | Aggregate for prediction (cached children) |
| `aggregate_subtree_with_cache(...)` | Recursive aggregation with cache |

### Pattern Overlap Resolution

**IMPORTANT:** Bei der Prediction haben groessere Patterns Prioritaet ueber kleinere. Bei gleicher Laenge gewinnt das frueher selektierte Pattern.

Wenn ein 4-Operator-Pattern und ein 2-Operator-Pattern dieselben Nodes matchen, wird das 4-Operator-Pattern verwendet. Bei zwei 4-Operator-Patterns entscheidet die Selection-Reihenfolge (niedrigere Iteration = hoehere Prioritaet). Dies entspricht der Paper-Logik (Section 3.4, Algorithm 1): "occurrences of p are consumed by the newly added model".

**Implementation:** `predict_single_query()` sammelt zuerst alle Pattern-Matches, sortiert sie nach:
1. `pattern_length` (groesste zuerst)
2. `pattern_order` (frueher selektierte zuerst, als Tiebreaker)

Nodes, die von einem Pattern konsumiert wurden, werden nicht erneut von anderen Patterns gematcht.

**Konsistenz:** Diese Logik ist identisch mit `12_Query_Prediction/src/tree.py:build_pattern_assignments()` um sicherzustellen, dass Selection und Prediction das gleiche Verhalten zeigen.

---

## selection.py

Selection strategy implementations.

### Functions

| Function | Purpose |
|----------|---------|
| `calculate_pattern_avg_mre(...)` | Calculate avg MRE for pattern based on current predictions |
| `run_static_selection(...)` | Greedy selection for frequency/size |
| `run_error_selection(...)` | Dynamic selection with re-ranking |
| `calculate_error_ranking(...)` | Compute error scores for patterns |
| `select_next_candidate(...)` | Pick top pattern with FFS |

### Selection Algorithm

**Static (frequency/size):**
```
baseline_mre = 0.2297
for each pattern in sorted order:
    if no FFS: skip
    train/load model
    predict test set
    if MRE improves: SELECTED, update baseline
    else: REJECTED
export summary
```

**Error (dynamic):**
```
baseline_mre = 0.2297
predict test with operators only
while improvements possible:
    calculate error_ranking (occurrence * avg_mre)
    select top candidate with FFS
    train/load model
    predict test set
    if MRE improves: SELECTED, update predictions
    else: REJECTED
export summary
```
