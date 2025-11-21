# OperatorEngineering - Operator Analysis Module

Analysis module for operator runtime characteristics, pattern performance evaluation, and execution plan generation with pass-through logic.

## Directory Structure

```
OperatorEngineering/
├── 01_Analyze_Operators.py
├── 02_Analyze_Template_Patterns.py
├── 03_Pattern_Complete_Evaluation.py
├── 04_Filter_Passthrough_Patterns.py
├── 05_create_execution_plan.py
├── operator_dataset_20251102_140747.csv  # [source] Complete operator dataset
├── 04_test.csv                           # [source] Test split for pattern analysis
├── predictions.csv                       # [source] Pattern predictions from Hybrid_2
├── two_step_evaluation_overview.csv      # [source] Pattern overview from Hybrid_2
├── csv/                                  # [outputs] Analysis results
│   ├── operator_runtime_analysis_{timestamp}.csv
│   ├── template_pattern_analysis_{timestamp}.csv
│   ├── pattern_complete_mean_mre_execution_time_pct_{timestamp}.csv
│   ├── pattern_complete_mean_mre_start_time_pct_{timestamp}.csv
│   ├── 04_filtered_execution_time_passthrough_{timestamp}.csv
│   └── 04_filtered_start_time_passthrough_{timestamp}.csv
├── md/                                   # [outputs] Execution plans
│   └── {query_name}_execution_plan_{timestamp}.md
└── DOCS.md
```

## Key Concepts

### Pass-Through Operators

Operators that forward data without significant processing overhead. Identified by `startup_total_ratio >= 0.99`.

**Pass-Through Operators:**
- Incremental Sort (1.000)
- Merge Join (0.999)
- Limit (0.999)
- Sort (0.997)
- Hash (0.996)

**Characteristics:**
- Minimal own processing time
- Execution time dominated by child operator time
- Startup time ≈ Total time

**Pass-Through Logic:**
- Pass-through operators inherit predictions from their child
- `predicted_startup_time = child.predicted_startup_time`
- `predicted_total_time = child.predicted_total_time`

### Pattern Naming Convention

**Single Child Pattern:**
```
Format: Parent_Child_Relationship
Example: Hash_Seq_Scan_Outer
```

**Two Children Pattern:**
```
Format: Parent_Child1_Outer_Child2_Inner
Example: Hash_Join_Seq_Scan_Outer_Hash_Inner
```

**Component Order:**
- Parent operator comes first
- Children ordered: Outer before Inner
- Underscores separate components
- Relationship suffix: `_Outer` or `_Inner`

### Leaf vs Non-Leaf Patterns

**Leaf Patterns:**
- No `missing_child_features`
- Can predict from static features alone
- Example: `Hash_Seq_Scan_Outer` (only needs static features from Hash and Seq Scan)

**Non-Leaf Patterns:**
- Have `missing_child_features` (st1, rt1, st2, rt2)
- Require child predictions to complete feature set
- Example: `Hash_Join_Hash_Join_Outer_Hash_Inner` (needs predictions from Hash child's grandchildren)

### Bottom-Up Execution Plan Logic

**Processing Order:**
1. Start at deepest depth (max depth → 0)
2. For each operator at current depth:
   - Try pattern matching with children
   - If pattern parent is pass-through → reject pattern
   - If no pattern match → operator-level prediction
   - If operator is pass-through → inherit child predictions

**Prediction Flow:**
- Child predictions become parent features (st1/rt1, st2/rt2)
- Pass-through operators forward predictions upward
- Pattern predictions consume all children
- Operator predictions require available child predictions

**Pattern Exclusion Rules:**
- Patterns with pass-through parents are NOT matched
- Example: `Sort_Aggregate_Outer` rejected (Sort is pass-through)
- Individual Sort operators handled via pass-through logic instead

## Source Data Documentation

**IMPORTANT:** Source data files are NOT emitted by this module. They are copied from other modules for analysis.

### operator_dataset_20251102_140747.csv

**Source:** `Prediction_Methods/Hybrid_2/Data_Generation/operator_dataset_20251102_140747.csv`

**Purpose:** Complete operator dataset (all queries, all operators) for runtime analysis and execution plan generation

**Format:**
- Delimiter: Semicolon (;)
- Columns: query_file, node_id, node_type, depth, parent_relationship, subplan_name, features, actual_startup_time, actual_total_time

### 04_test.csv

**Source:** `Prediction_Methods/Hybrid_2/Datasets/Baseline_SVM/04_test.csv`

**Purpose:** Test split for pattern analysis and evaluation

**Format:**
- Delimiter: Semicolon (;)
- Columns: Same as operator_dataset

### predictions.csv

**Source:** `Prediction_Methods/Hybrid_2/Runtime_Prediction/Baseline_SVM/Evaluation/predictions.csv`

**Purpose:** Pattern predictions for MRE evaluation

**Format:**
- Delimiter: Semicolon (;)
- Columns: query_file, node_id, node_type, depth, parent_relationship, subplan_name, actual_startup_time, actual_total_time, predicted_startup_time, predicted_total_time, prediction_type

### two_step_evaluation_overview.csv

**Source:** `Prediction_Methods/Hybrid_2/Runtime_Prediction/Baseline_SVM/SVM/two_step_evaluation_overview.csv`

**Purpose:** Pattern overview with missing_child_features for pattern matching

**Format:**
- Delimiter: Semicolon (;)
- Columns: pattern, target, ffs_feature_count, missing_child_count, final_feature_count, mre_ffs, mre_final, mre_delta, ffs_features, missing_child_features, final_features

## Workflow Execution Order

```
01 - Analyze_Operators
     ↓ operator_runtime_analysis.csv

02 - Analyze_Template_Patterns (uses 04_test.csv + two_step_evaluation_overview.csv)
     ↓ template_pattern_analysis.csv

03 - Pattern_Complete_Evaluation (uses predictions.csv + operator_dataset)
     ↓ pattern_complete_mean_mre_execution_time_pct.csv
     ↓ pattern_complete_mean_mre_start_time_pct.csv

04 - Filter_Passthrough_Patterns (uses operator_runtime_analysis + 03 outputs)
     ↓ 04_filtered_execution_time_passthrough.csv
     ↓ 04_filtered_start_time_passthrough.csv

05 - create_execution_plan (uses operator_dataset + query_name + two_step_evaluation_overview + operator_runtime_analysis)
     ↓ {query_name}_execution_plan.md
```

## Script Documentation

### 01 - Analyze_Operators.py

**Purpose:** Analyze operator runtime characteristics and identify pass-through vs computational operators

**Workflow:**
1. Load operator dataset and filter to main plan (exclude SubPlans)
2. Extract all unique operator types
3. Calculate statistics per operator:
   - Count (occurrence frequency)
   - Mean, Std, Min, Max for actual_total_time
   - Mean, Std, Min, Max for actual_startup_time
   - Startup/Total ratio (pass-through indicator)
4. Rank operators by mean total time (descending)
5. Export analysis results

**Inputs:**
- `input` - Path to operator dataset CSV (positional)

**Outputs:**
- `{output-dir}/csv/operator_runtime_analysis_{timestamp}.csv`
  - Columns: node_type, count, mean_total_ms, std_total_ms, min_total_ms, max_total_ms, mean_startup_ms, std_startup_ms, min_startup_ms, max_startup_ms, startup_total_ratio
  - Ranked by mean_total_ms descending

**Usage:**
```bash
python 01_Analyze_Operators.py operator_dataset_20251102_140747.csv --output-dir .
```

**Example:**
```bash
python 01_Analyze_Operators.py operator_dataset_20251102_140747.csv --output-dir .
```

**Variables:**
- `--output-dir` - Output directory for analysis results (required)

### 02 - Analyze_Template_Patterns.py

**Purpose:** Detect template variants based on pattern combinations using bottom-up pattern extraction

**Workflow:**
1. Load test data and pattern overview
2. Extract pattern features (missing_child_features per pattern)
3. For each query in test data:
   - Extract template ID from query filename
   - Apply bottom-up pattern matching (depth=max → 0)
   - Track consumed operators (pattern vs operator)
   - Validate child feature availability for non-leaf patterns
4. Group queries by pattern combination
5. Detect variants: queries with same pattern set = one variant
6. Export template variant analysis

**Inputs:**
- `test_file` - Path to test.csv (positional)
- `pattern_overview` - Path to pattern overview CSV (positional)

**Outputs:**
- `{output-dir}/csv/template_pattern_analysis_{timestamp}.csv`
  - Columns: template, variant_id, variant_count, patterns, pattern_depths
  - One row per variant per template

**Usage:**
```bash
python 02_Analyze_Template_Patterns.py 04_test.csv two_step_evaluation_overview.csv --output-dir .
```

**Example:**
```bash
python 02_Analyze_Template_Patterns.py 04_test.csv two_step_evaluation_overview.csv --output-dir .
```

**Variables:**
- `--output-dir` - Output directory for analysis results (required)

### 03 - Pattern_Complete_Evaluation.py

**Purpose:** Calculate MRE per complete pattern (not just parent operator) across templates

**Workflow:**
1. Load predictions (filter prediction_type='pattern')
2. Load operator dataset for pattern reconstruction
3. For each pattern prediction:
   - Lookup query in operator_dataset
   - Find children using depth+1 lookup
   - Reconstruct complete pattern name (e.g., Hash_Join_Seq_Scan_Outer_Hash_Inner)
4. Calculate MRE for execution_time and start_time
5. Group by (pattern_name, template) and calculate mean MRE
6. Create pivot tables: pattern_name × template
7. Export two CSV files (execution_time, start_time)

**Inputs:**
- `predictions_file` - Path to predictions.csv (positional)
- `operator_dataset` - Path to operator_dataset.csv (positional)

**Outputs:**
- `{output-dir}/csv/pattern_complete_mean_mre_execution_time_pct_{timestamp}.csv`
  - Rows: Complete pattern names (e.g., Aggregate_Gather_Merge_Outer)
  - Columns: Q1, Q10, Q12, Q13, Q14, Q18, Q19, Q3, Q4, Q5, Q6, Q7, Q8, Q9
  - Values: Mean MRE percentage per pattern per template

- `{output-dir}/csv/pattern_complete_mean_mre_start_time_pct_{timestamp}.csv`
  - Same structure as execution_time variant

**Usage:**
```bash
python 03_Pattern_Complete_Evaluation.py predictions.csv operator_dataset_20251102_140747.csv --output-dir .
```

**Example:**
```bash
python 03_Pattern_Complete_Evaluation.py predictions.csv operator_dataset_20251102_140747.csv --output-dir .
```

**Variables:**
- `--output-dir` - Output directory for analysis results (required)

### 04 - Filter_Passthrough_Patterns.py

**Purpose:** Filter patterns to show only those with non-pass-through parent AND pass-through child

**Workflow:**
1. Load pass-through operators (startup_total_ratio >= 0.99)
2. Load all operator names for compound operator matching
3. For each pattern in MRE files:
   - Parse pattern name to extract parent and children
   - Check if parent is pass-through → reject
   - Check if any child is pass-through → keep
4. Filter MRE tables to keep only matching patterns
5. Export filtered results

**Inputs:**
- `operator_analysis` - Path to operator runtime analysis CSV (positional)
- `execution_time_file` - Path to pattern execution_time MRE CSV (positional)
- `start_time_file` - Path to pattern start_time MRE CSV (positional)

**Outputs:**
- `{output-dir}/csv/04_filtered_execution_time_passthrough_{timestamp}.csv`
  - Same structure as input but filtered rows

- `{output-dir}/csv/04_filtered_start_time_passthrough_{timestamp}.csv`
  - Same structure as input but filtered rows

**Usage:**
```bash
python 04_Filter_Passthrough_Patterns.py \
  csv/operator_runtime_analysis_20251121_160138.csv \
  csv/pattern_complete_mean_mre_execution_time_pct_20251121_185425.csv \
  csv/pattern_complete_mean_mre_start_time_pct_20251121_185425.csv \
  --output-dir .
```

**Example:**
```bash
python 04_Filter_Passthrough_Patterns.py \
  csv/operator_runtime_analysis_20251121_160138.csv \
  csv/pattern_complete_mean_mre_execution_time_pct_20251121_185425.csv \
  csv/pattern_complete_mean_mre_start_time_pct_20251121_185425.csv \
  --output-dir .
```

**Variables:**
- `--output-dir` - Output directory for filtered results (required)

### 05 - create_execution_plan.py

**Purpose:** Generate bottom-up execution plan for single query with pass-through logic

**Workflow:**
1. Load operator dataset and filter for specified query
2. Load pattern overview and operator overview
3. Extract pattern features and operator features
4. Build execution plan bottom-up (depth=max → 0):
   - For each operator at current depth:
     - Find parent operator
     - Find all siblings (children of same parent)
     - Try pattern matching:
       - Reject if parent is pass-through
       - Check if pattern exists in PATTERNS list
       - Validate child feature availability
     - If pattern matched:
       - Create pattern step
       - Mark parent and children as consumed by pattern
       - Store pattern prediction
     - If no pattern:
       - Check if operator is pass-through:
         - If yes: inherit child predictions
         - If no: create operator step
       - Mark operator as consumed
       - Store operator/pass-through prediction
5. Generate markdown with step-by-step explanation
6. Export execution plan

**Inputs:**
- `operator_dataset_file` - Path to operator dataset CSV (positional)
- `query_name` - Query filename (e.g., Q3_121_seed_984483720) (positional)
- `pattern_overview_file` - Path to pattern overview CSV (positional)
- `operator_overview_file` - Path to operator overview CSV (positional)
- `output_dir` - Output directory (positional)

**Outputs:**
- `{output_dir}/md/{query_name}_execution_plan_{timestamp}.md`
  - Overview: Total steps, pattern steps, operator steps, pass-through steps
  - Step-by-step execution plan (bottom-up)
  - For each step:
    - Type (Pattern, Operator, Pass-Through)
    - Required features
    - Feature aggregation/mapping
    - Emitted targets

**Usage:**
```bash
python 05_create_execution_plan.py \
  operator_dataset_20251102_140747.csv \
  Q3_121_seed_984483720 \
  two_step_evaluation_overview.csv \
  csv/operator_runtime_analysis_20251121_160138.csv \
  .
```

**Example:**
```bash
python 05_create_execution_plan.py \
  operator_dataset_20251102_140747.csv \
  Q3_121_seed_984483720 \
  two_step_evaluation_overview.csv \
  csv/operator_runtime_analysis_20251121_160138.csv \
  .
```

**Variables:**
None - All arguments are positional
