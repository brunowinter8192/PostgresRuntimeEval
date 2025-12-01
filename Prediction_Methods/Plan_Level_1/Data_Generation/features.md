# Plan-Level Features

## Root Metrics (from EXPLAIN JSON)

### p_st_cost - Root Startup Cost

Estimated cost until the first output tuple of the root operator.

**Extraction:** `Startup Cost` from Root-Plan Node

**Example:** `"Startup Cost": 170311.11` -> p_st_cost = 170311.11

---

### p_tot_cost - Root Total Cost

Estimated total cost for all output tuples of the root operator.

**Extraction:** `Total Cost` from Root-Plan Node

**Example:** `"Total Cost": 170315.88` -> p_tot_cost = 170315.88

---

### p_rows - Root Plan Rows

Estimated number of output tuples of the root operator.

**Extraction:** `Plan Rows` from Root-Plan Node

**Example:** `"Plan Rows": 1` -> p_rows = 1

---

### p_width - Root Plan Width

Average width of an output tuple in bytes.

**Extraction:** `Plan Width` from Root-Plan Node

**Example:** `"Plan Width": 236` -> p_width = 236

---

## Structural Features

### op_count - Total Operator Count

Total number of all operators in the query plan.

**Extraction:** Sum of all node type counts from tree traversal

**Example:** Plan with 3 Seq Scan + 2 Hash Join + 1 Aggregate -> op_count = 6

---

### workers_planned - Workers Planned

Total number of planned parallel worker processes.

**Extraction:** Sum of all `Workers Planned` values in the plan tree

**Example:** Gather with 4 workers -> workers_planned = 4

**Edge case:** Non-parallel queries -> workers_planned = 0

---

### parallel_aware_count - Parallel Aware Operators

Number of operators with `Parallel Aware = true`.

**Extraction:** Count of all nodes with `"Parallel Aware": true`

**Example:** 2 parallel aware Seq Scans -> parallel_aware_count = 2

---

### max_tree_depth - Maximum Tree Depth

Maximum depth of the query plan tree.

**Extraction:** Recursive depth-first traversal, root = depth 1

**Example:**
```
Aggregate (depth=1)
└─ Sort (depth=2)
   └─ Seq Scan (depth=3)
```
-> max_tree_depth = 3

---

### planning_time_ms - Planning Time

Time for query planning in milliseconds.

**Extraction:** `Planning Time` from EXPLAIN JSON Summary

**Example:** `"Planning Time": 1.234` -> planning_time_ms = 1.234

---

### jit_functions - JIT Functions

Number of JIT-compiled functions.

**Extraction:** `JIT.Functions` from EXPLAIN JSON (if present)

**Example:** `"JIT": {"Functions": 12}` -> jit_functions = 12

**Edge case:** No JIT -> jit_functions = 0

---

### subplan_count - SubPlan Count

Number of SubPlan nodes in the query plan.

**Extraction:** Count of all nodes with `Parent Relationship = "SubPlan"`

**Example:** Query with 2 correlated subqueries -> subplan_count = 2

---

### initplan_count - InitPlan Count

Number of InitPlan nodes in the query plan.

**Extraction:** Count of all nodes with `Parent Relationship = "InitPlan"`

**Example:** Query with 1 uncorrelated subquery -> initplan_count = 1

---

## Strategy Features

### strategy_hashed - Hashed Strategy Count

Number of aggregate operators with hash strategy.

**Extraction:** Count of all nodes with `Strategy = "Hashed"`

---

### strategy_plain - Plain Strategy Count

Number of aggregate operators with plain strategy.

**Extraction:** Count of all nodes with `Strategy = "Plain"`

---

### strategy_sorted - Sorted Strategy Count

Number of aggregate operators with sorted strategy.

**Extraction:** Count of all nodes with `Strategy = "Sorted"`

---

### partial_mode_simple - Simple Partial Mode Count

Number of operators with `Partial Mode = "Simple"`.

**Extraction:** Count of all nodes with `Partial Mode = "Simple"`

---

### partial_mode_partial - Partial Mode Count

Number of operators with `Partial Mode = "Partial"`.

**Extraction:** Count of all nodes with `Partial Mode = "Partial"`

---

### partial_mode_finalize - Finalize Mode Count

Number of operators with `Partial Mode = "Finalize"`.

**Extraction:** Count of all nodes with `Partial Mode = "Finalize"`

---

## Key Features

### group_key_count - Group Key Operators

Number of operators with group key.

**Extraction:** Count of all nodes with `Group Key` attribute

---

### group_key_columns - Total Group Key Columns

Total number of group key columns across all operators.

**Extraction:** Sum of lengths of all `Group Key` arrays

**Example:** Aggregate with `Group Key: ["a", "b"]` -> +2

---

### sort_key_count - Sort Key Operators

Number of operators with sort key.

**Extraction:** Count of all nodes with `Sort Key` attribute

---

### sort_key_columns - Total Sort Key Columns

Total number of sort key columns across all operators.

**Extraction:** Sum of lengths of all `Sort Key` arrays

**Example:** Sort with `Sort Key: ["a DESC", "b"]` -> +2

---

## Result Features (Tree Traversal)

### row_count - Total Row Count

Total number of rows processed through the entire plan tree.

**Extraction:** Recursive tree traversal:
```python
row_count = output_rows + input_rows + children_total
```
- output_rows: `Plan Rows` of current node
- input_rows: Sum of `Plan Rows` of all non-InitPlan children
- children_total: Recursive for all children

**Edge case:** InitPlan children are not counted in input_rows (avoids double counting)

---

### byte_count - Total Byte Count

Total number of bytes processed through the entire plan tree.

**Extraction:** Recursive tree traversal:
```python
byte_count = output_bytes + input_bytes + children_total
```
- output_bytes: `Plan Rows * Plan Width` of current node
- input_bytes: Sum of `Plan Rows * Plan Width` of all non-InitPlan children
- children_total: Recursive for all children

---

## Operator Features (13 Operators x 2 Metrics = 26 Features)

For each operator type, two features are extracted:
- `{Operator}_cnt`: Number of occurrences of the operator
- `{Operator}_rows`: Sum of `Plan Rows` of all occurrences

**Operator Types:**

| Operator | Count Feature | Rows Feature |
|----------|---------------|--------------|
| Aggregate | Aggregate_cnt | Aggregate_rows |
| Gather | Gather_cnt | Gather_rows |
| Gather Merge | Gather_Merge_cnt | Gather_Merge_rows |
| Hash | Hash_cnt | Hash_rows |
| Hash Join | Hash_Join_cnt | Hash_Join_rows |
| Incremental Sort | Incremental_Sort_cnt | Incremental_Sort_rows |
| Index Only Scan | Index_Only_Scan_cnt | Index_Only_Scan_rows |
| Index Scan | Index_Scan_cnt | Index_Scan_rows |
| Limit | Limit_cnt | Limit_rows |
| Merge Join | Merge_Join_cnt | Merge_Join_rows |
| Nested Loop | Nested_Loop_cnt | Nested_Loop_rows |
| Seq Scan | Seq_Scan_cnt | Seq_Scan_rows |
| Sort | Sort_cnt | Sort_rows |

**Extraction:**
```python
for node_type in OPERATOR_TYPES:
    node_metrics[node_type]['count'] += 1
    node_metrics[node_type]['rows'] += plan_node.get("Plan Rows", 0)
```

**Example:** Query with 2 Seq Scans (1000 + 5000 rows):
- Seq_Scan_cnt = 2
- Seq_Scan_rows = 6000

**Edge case:** Operator not in plan -> _cnt = 0, _rows = 0

---

## Feature Summary

| Category | Count | Features |
|----------|-------|----------|
| Root Metrics | 4 | p_st_cost, p_tot_cost, p_rows, p_width |
| Structural | 8 | op_count, workers_planned, parallel_aware_count, max_tree_depth, planning_time_ms, jit_functions, subplan_count, initplan_count |
| Strategy | 6 | strategy_*, partial_mode_* |
| Key | 4 | group_key_*, sort_key_* |
| Result | 2 | row_count, byte_count |
| Operator | 26 | 13 operators x 2 metrics |
| **Total** | **50** | |
