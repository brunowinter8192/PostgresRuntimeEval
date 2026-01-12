# Data_Generation Module Documentation

## Working Directory

**CRITICAL:** All commands assume CWD = `Data_Generation/`

```bash
cd /path/to/Plan_Level_1/Data_Generation
```

## Directory Structure

```
Data_Generation/
├── DOCS.md
├── features.md
├── targets.md
├── 01a_Runtime_Data.py
├── 01b_Plan_Features.py
├── 01c_Row_Features.py
├── 02_Merge_Data.py
├── A_01a_Explain_JSON.py
├── csv/
└── md/
```

## Shared Infrastructure

### Parent mapping_config.py
- `DB_CONFIG`: PostgreSQL connection parameters (host, port, database, user, password)
- `CONTAINER_NAME`: Docker container name for TPC-H database
- `OPERATOR_TYPES`: List of plan operator types for feature extraction

## Workflow Dependency Graph

```
01a_Runtime_Data.py ─┐
01b_Plan_Features.py ├─→ 02_Merge_Data.py
01c_Row_Features.py ─┘
```

**Dependencies:**
- 01a, 01b, 01c can run independently (parallel)
- 02 requires outputs from all 01x scripts

### 01a - Runtime_Data.py

**Purpose**: Execute TPC-H queries with cold cache restart and measure actual runtime

**Workflow**:
1. Load all SQL files from template directories
2. For each query:
   - Restart OrbStack and purge system cache
   - Wait for Docker and PostgreSQL to be ready
   - Execute query and measure runtime in milliseconds
3. Export results to CSV

**Inputs**:
- `query_dir` (positional): Directory containing Q* template folders with SQL files

**Outputs**:
- `csv/01a_runtimes.csv`: Columns: query_file, template, runtime

**Usage**:
```bash
python 01a_Runtime_Data.py /path/to/queries
python 01a_Runtime_Data.py /path/to/queries --output-dir /custom/output
```

**Variables**:
- `--output-dir`: Custom output directory (default: script_dir/csv)

---

### 01b - Plan_Features.py

**Purpose**: Extract plan-level features from PostgreSQL EXPLAIN JSON output

**Workflow**:
1. Connect to PostgreSQL database
2. For each query file:
   - Run EXPLAIN (FORMAT JSON) to get query plan
   - Extract root metrics (startup cost, total cost, rows, width)
   - Count operators by type and aggregate rows
   - Extract parallel execution settings
   - Count aggregation strategies and partial modes
   - Calculate tree depth and plan structure metrics
3. Sort results by template and seed number
4. Export to CSV

**Inputs**:
- `query_dir` (positional): Directory containing Q* template folders with SQL files

**Outputs**:
- `csv/01b_plan_features.csv`: Columns include:
  - Metadata: query_file, template
  - Root metrics: p_st_cost, p_tot_cost, p_rows, p_width
  - Operator counts: op_count, {OperatorType}_cnt, {OperatorType}_rows
  - Parallel: workers_planned, parallel_aware_count
  - Strategies: strategy_hashed, strategy_plain, strategy_sorted
  - Partial modes: partial_mode_simple, partial_mode_partial, partial_mode_finalize
  - Structure: group_key_count, group_key_columns, sort_key_count, sort_key_columns
  - Plan info: subplan_count, initplan_count, max_tree_depth, planning_time_ms, jit_functions

**Usage**:
```bash
python 01b_Plan_Features.py /path/to/queries
python 01b_Plan_Features.py /path/to/queries --output-dir /custom/output
```

**Variables**:
- `--output-dir`: Custom output directory (default: script_dir/csv)

---

### 01c - Row_Features.py

**Purpose**: Extract total row and byte counts from plan tree traversal

**Workflow**:
1. Connect to PostgreSQL database
2. For each query file:
   - Run EXPLAIN (FORMAT JSON)
   - Traverse plan tree recursively
   - Calculate total row count (input + output rows, excluding InitPlans)
   - Calculate total byte count (rows * width)
3. Sort results by template and seed number
4. Export to CSV

**Inputs**:
- `query_dir` (positional): Directory containing Q* template folders with SQL files

**Outputs**:
- `csv/01c_row_features.csv`: Columns: query_file, template, row_count, byte_count

**Usage**:
```bash
python 01c_Row_Features.py /path/to/queries
python 01c_Row_Features.py /path/to/queries --output-dir /custom/output
```

**Variables**:
- `--output-dir`: Custom output directory (default: script_dir/csv)

---

### 02 - Merge_Data.py

**Purpose**: Merge runtime, plan features, and row features into complete dataset

**Workflow**:
1. Load 01a_runtimes.csv
2. Load 01b_plan_features.csv
3. Load 01c_row_features.csv
4. Inner join all datasets on query_file and template columns
5. Export merged dataset to CSV

**Inputs**:
- `csv_dir` (positional): Directory containing the three CSV files

**Outputs**:
- `csv/complete_dataset.csv`: All columns from plan_features + row_count + byte_count + runtime

**Usage**:
```bash
python 02_Merge_Data.py csv/
```

---

## Analysis Scripts

### A_01a - Explain_JSON.py

**Purpose**: Export raw EXPLAIN JSON output for feature exploration and documentation

**Workflow**:
1. Connect to PostgreSQL database
2. For each template (Q1-Q22, excluding Q15):
   - Load first seed query file
   - Run EXPLAIN (ANALYZE false, VERBOSE true, COSTS true, SUMMARY true, FORMAT JSON)
   - Write complete JSON to markdown
3. Export all results to single markdown file

**Inputs**:
- `query_dir` (positional): Directory containing Q* template folders with SQL files
- `--output-dir` (required): Output directory for markdown file

**Outputs**:
- `md/A_01a_explain_json_export_{timestamp}.md`: Raw EXPLAIN JSON for each template

**Usage**:
```bash
python A_01a_Explain_JSON.py /path/to/queries --output-dir md/
```
