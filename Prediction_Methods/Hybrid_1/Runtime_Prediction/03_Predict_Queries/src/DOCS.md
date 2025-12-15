# src - Helper Modules

Helper modules for 03_Predict_Queries hybrid prediction.

## Directory Structure

```
src/
├── DOCS.md
├── tree.py
├── io.py
├── prediction.py
└── report.py
```

---

## tree.py

**Purpose:** Tree building from flat DataFrame, pattern hash computation, greedy pattern assignment

**Inputs:**
- `query_ops`: DataFrame with query operators (node_id, node_type, depth, parent_relationship)
- `pattern_info`: Dict mapping pattern_hash to {length, pattern_string}
- `pattern_order`: List of pattern_hashes sorted by priority

**Outputs:**
- `QueryNode`: Tree structure with node_type, parent_relationship, depth, node_id, children
- `consumed_nodes`: Set of node_ids consumed by patterns
- `pattern_assignments`: Dict mapping root node_id to pattern_hash

**Implementation Details:**

Pattern Overlap Resolution: Groessere Patterns haben Prioritaet. Bei Overlap wird das laengere Pattern verwendet, kleinere ueberlappende Patterns werden uebersprungen. Greedy matching mit pattern_order (sorted by length DESC, then occurrence DESC).

---

## io.py

**Purpose:** Data loading (test data, pattern/operator models and features) and export (predictions.csv, patterns.csv)

**Inputs:**
- `test_file`: Path to test CSV
- `patterns_csv`: Path to patterns.csv with pattern_hash, pattern_length, occurrence_count
- `overview_file`: Path to FFS overview CSV (pattern or operator)
- `model_dir`: Path to Model directory

**Outputs:**
- `df_test`: DataFrame filtered to main plan operators (no subplans)
- `pattern_info`, `pattern_order`: Pattern metadata and priority order
- `pattern_models`, `operator_models`: Dicts of loaded SVM models
- `pattern_features`, `operator_features`: Dicts of feature lists per target
- `predictions.csv`, `patterns.csv`: Exported result files

---

## prediction.py

**Purpose:** Two-phase bottom-up prediction algorithm with pattern and operator models, feature aggregation with prediction cache

**Inputs:**
- `query_ops`: DataFrame with query operators
- `operator_models`, `pattern_models`: Loaded SVM model dicts
- `operator_features`, `pattern_features`: Feature list dicts
- `pattern_info`, `pattern_order`: Pattern metadata
- `passthrough`: Bool flag for passthrough optimization

**Outputs:**
- `predictions`: List of prediction result dicts (query_file, node_id, actual, predicted, type)
- `steps`: List of prediction step dicts (for reporting)
- `prediction_cache`: Dict mapping node_id to {start, exec} predictions

**Implementation Details:**

Single-Pattern Constraint: Wenn genau EIN Pattern matched UND dieses Pattern ALLE Nodes des Query-Trees konsumiert, wird das Pattern verworfen und rein Operator-basiert predicted. Grund: Ein Pattern das den gesamten Tree abdeckt degeneriert zu Plan-Level Prediction - widerspricht dem Hybrid-Ansatz.

---

## report.py

**Purpose:** MD report generation for prediction traces (tree visualization, prediction chain, results table)

**Inputs:**
- `query_file`: Query identifier
- `df_query`: DataFrame with query operators
- `predictions`: List of prediction results
- `steps`: List of prediction steps
- `consumed_nodes`, `pattern_assignments`: Pattern matching results
- `pattern_info`: Pattern metadata
- `output_dir`: Output directory path

**Outputs:**
- `md/{template}_{plan_hash}_{timestamp}.md`: MD report file with sections for pattern assignments, query tree, prediction chain, results table
