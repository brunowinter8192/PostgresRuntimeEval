# src/ Module Documentation

## Shared Infrastructure

All modules use semicolon-delimited CSVs per project standards.

## Module Overview

| Module | Functions | Responsibility |
|--------|-----------|----------------|
| tree.py | 8 | Tree structure + pattern matching |
| io.py | 8 | Data loading + export |
| prediction.py | 7 | Prediction logic + aggregation |
| report.py | 1 class | MD report generation |

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
| `compute_pattern_hash(node, length)` | MD5 hash of subtree structure |
| `has_children_at_length(node, length)` | Check subtree depth exists |
| `extract_pattern_node_ids(node, length)` | Get all node IDs in pattern |
| `build_pattern_assignments(nodes, info, order)` | Match patterns to query (larger first) |

### Pattern Overlap Resolution

**IMPORTANT:** Bei der Prediction haben groessere Patterns Prioritaet ueber kleinere.

`build_pattern_assignments()` sortiert Patterns nach `length` (groesste zuerst), bevor sie gematcht werden. Dies entspricht der Paper-Logik (Section 3.4): "occurrences of p are consumed by the newly added model".

---

## io.py

Data loading and export functions.

### Functions

| Function | Purpose |
|----------|---------|
| `load_test_data(file_path)` | Load test CSV, filter main plan |
| `load_operator_models(model_dir)` | Load pickled operator models |
| `load_operator_features(overview_file)` | Parse feature overview CSV |
| `load_pattern_models(model_dir)` | Load pattern models + features.json |
| `load_pattern_features(ffs_file, models)` | Parse pattern FFS overview |
| `load_pattern_info(selected, metadata)` | Merge pattern metadata |
| `create_prediction_result(row, st, rt, type)` | Create result dictionary |
| `export_predictions(predictions, output_dir)` | Write predictions.csv |

---

## prediction.py

Prediction logic and feature aggregation.

### Functions

| Function | Purpose |
|----------|---------|
| `predict_all_queries(...)` | Iterate over unique queries |
| `predict_single_query(...)` | Two-phase bottom-up prediction |
| `predict_pattern(node, ops, model, cache, len)` | Pattern model prediction |
| `predict_operator(node, ops, models, feats, cache)` | Operator model prediction |
| `build_operator_features(row, node, cache)` | Extract features + child predictions |
| `aggregate_pattern_with_cache(...)` | Build pattern feature vector |
| `aggregate_subtree_with_cache(...)` | Recursive subtree aggregation |

### Prediction Workflow

```
For each query:
  1. Build tree from DataFrame
  2. Extract all nodes
  3. Sort by depth (deepest first)
  4. Phase 1: Match patterns (greedy, priority order)
     - Mark consumed nodes
     - Create pattern_assignments dict
  5. Phase 2: Bottom-up prediction
     - If node is pattern root: predict_pattern()
     - If node is consumed: skip (already predicted)
     - Else: predict_operator()
  6. Cache predictions for child feature lookup
```

---

## report.py

MD report generation using builder pattern.

### ReportBuilder Class

**Methods:**

| Method | Purpose |
|--------|---------|
| `__init__(output_dir, strategy)` | Initialize with output path |
| `set_query_data(...)` | Set current query context |
| `add_input_summary(...)` | Add input file summary |
| `add_pattern_assignments_section()` | Add pattern table |
| `add_query_tree_section()` | Add ASCII tree |
| `add_prediction_results(predictions)` | Add results table + summary |
| `add_prediction_chain(...)` | Add step-by-step chain |
| `save()` | Write to md/ folder |

### Report Sections

1. Header (query, strategy, timestamp)
2. Input Summary (file paths)
3. Pattern Assignments (table)
4. Query Tree (ASCII)
5. Prediction Results (table)
6. Summary (MRE, counts)
7. Prediction Chain (steps)

### Output Filename

`md/12_query_prediction_{query_file}_{YYYYMMDD_HHMMSS}.md`
