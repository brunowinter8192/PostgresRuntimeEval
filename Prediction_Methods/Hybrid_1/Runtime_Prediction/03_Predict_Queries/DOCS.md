# 03_Predict_Queries - Hybrid Bottom-Up Prediction

Execute hybrid bottom-up prediction on test queries with multi-depth pattern matching.

## Directory Structure

```
03_Predict_Queries/
├── DOCS.md
├── 03_Predict_Queries.py    # Entry point
└── src/                     [See DOCS.md](src/DOCS.md)
    ├── tree.py
    ├── io.py
    ├── prediction.py
    └── report.py
```

## Working Directory

**CRITICAL:** All commands assume CWD = `Runtime_Prediction/`

```bash
cd /path/to/Hybrid_1/Runtime_Prediction
```

---

## 03_Predict_Queries.py

**Purpose:** Execute hybrid bottom-up prediction on test queries with multi-depth pattern matching

**Algorithm (Two-Phase Multi-Depth Pattern Matching):**

Phase 1 - Pattern Assignment:
1. Load patterns from patterns.csv, sort by pattern_length descending, then occurrence_count descending
2. For each pattern (longest first, ties broken by frequency):
   - Find all query nodes matching the pattern hash
   - Mark matched nodes as consumed (prevents overlap)
   - Assign pattern to root node of match
3. Single-pattern constraint: If only one pattern matches AND it consumes all nodes, discard pattern assignment and use operator-only prediction

Phase 2 - Bottom-Up Prediction:
1. Traverse nodes by depth (deepest first)
2. For each node:
   - If assigned to pattern -> use pattern model for root prediction
   - Else if passthrough enabled AND node is passthrough operator -> copy child prediction
   - Else -> use operator model
3. Cache predictions for child feature propagation (st1/rt1/st2/rt2)

**Passthrough Operators:** Incremental Sort, Gather Merge, Gather, Sort, Limit, Merge Join
When --passthrough flag is set, these operators copy their child's prediction if not part of a pattern.

**Inputs:**
- `test_file` - Path to baseline test.csv (positional)
- `patterns_csv` - Path to patterns_filtered.csv with pattern_hash and pattern_length (positional)
  - NOTE: Use patterns_filtered.csv for approaches with threshold filtering (approach_3/4)
  - patterns.csv and patterns_filtered.csv are identical for approach_1/2 (threshold=0)
- `pattern_overview` - Path to pattern FFS overview (two_step_evaluation_overview.csv) (positional)
- `operator_overview` - Path to operator overview (operator_overview.csv) (positional)
- `model_dir` - Path to Model directory (positional)

**Outputs:**
- `{output-dir}/predictions.csv`
  - Columns: query_file, node_id, node_type, depth, parent_relationship, subplan_name, actual_startup_time, actual_total_time, predicted_startup_time, predicted_total_time, prediction_type (pattern/operator/passthrough), pattern_hash
- `{output-dir}/patterns.csv` - Pattern usage summary (pattern_hash, usage_count, node_types)
- `{output-dir}/md/03_{template}_{plan_hash[:8]}_{timestamp}.md` - One MD report per unique plan structure (with --report flag)

**Usage:**
```bash
# All queries for approach_1 (no filtering, patterns.csv = patterns_filtered.csv)
python3 03_Predict_Queries/03_Predict_Queries.py \
  ../Datasets/Baseline_SVM/test.csv \
  ../Datasets/Baseline_SVM/approach_1/patterns_filtered.csv \
  Baseline_SVM/SVM/Patterns/two_step_evaluation_overview.csv \
  Baseline_SVM/SVM/Operators/operator_overview.csv \
  Baseline_SVM/Model \
  --output-dir Baseline_SVM/Predictions/approach_1

# With passthrough enabled (approach_2)
python3 03_Predict_Queries/03_Predict_Queries.py \
  ../Datasets/Baseline_SVM/test.csv \
  ../Datasets/Baseline_SVM/approach_2/patterns_filtered.csv \
  Baseline_SVM/SVM/Patterns/two_step_evaluation_overview.csv \
  Baseline_SVM/SVM/Operators/operator_overview.csv \
  Baseline_SVM/Model \
  --output-dir Baseline_SVM/Predictions/approach_2 \
  --passthrough

# approach_3 with threshold filtering (72 of 372 patterns), no passthrough
python3 03_Predict_Queries/03_Predict_Queries.py \
  ../Datasets/Baseline_SVM/test.csv \
  ../Datasets/Baseline_SVM/approach_3/patterns_filtered.csv \
  Baseline_SVM/SVM/Patterns/two_step_evaluation_overview.csv \
  Baseline_SVM/SVM/Operators/operator_overview.csv \
  Baseline_SVM/Model \
  --output-dir Baseline_SVM/Predictions/approach_3
```

**Variables:**
- `--output-dir` - Path to output directory for predictions (required)
- `--passthrough` - Enable passthrough for non-pattern passthrough operators (optional)
- `--report` - Generate MD report for first query of each unique plan structure (optional)

**Approach Flag Matrix:**

| Approach | Extraktion (03_Extract_Patterns) | Prediction (03_Predict_Queries) |
|----------|----------------------------------|--------------------------------|
| 1 | `--length 2 --required-operators` | - |
| 2 | `--length 2 --required-operators --no-passthrough` | `--passthrough` |
| 3 | - | - |
| 4 | `--no-passthrough` | `--passthrough` |

**Rule:** `--no-passthrough` at extraction → `--passthrough` at prediction
