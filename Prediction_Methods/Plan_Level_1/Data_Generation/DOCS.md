# Data_Generation Module Documentation

## Directory Structure

```
Data_Generation/
├── config.py                       # Database and container settings
├── 01_Runtime_Data.py              # Collect query runtimes with cold cache
├── 02_Plan_Features.py             # Extract plan-level features from EXPLAIN
├── 03_Row_Features.py              # Extract row and byte count features
├── 04_Merge_Data.py                # Merge all features into complete dataset
└── csv/                            # [outputs]
    ├── 01_runtimes.csv
    ├── 02_plan_features.csv
    ├── 03_row_features.csv
    └── complete_dataset.csv
```

## Shared Infrastructure

### config.py
- `DB_CONFIG`: PostgreSQL connection parameters (host, port, database, user, password)
- `CONTAINER_NAME`: Docker container name for TPC-H database

### Parent mapping_config.py
- `OPERATOR_TYPES`: List of plan operator types for feature extraction

## Workflow Execution Order

```
01_Runtime_Data.py
        ↓
02_Plan_Features.py
        ↓
03_Row_Features.py
        ↓
04_Merge_Data.py
```

**Dependencies:**
- 01, 02, 03 can run independently (only need query directory)
- 04 requires outputs from 01, 02, 03

## Script Documentation

### 01 - Runtime_Data.py

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
- `csv/01_runtimes.csv`: Columns: query_file, template, runtime

**Usage**:
```bash
python 01_Runtime_Data.py /path/to/queries
python 01_Runtime_Data.py /path/to/queries --output-dir /custom/output
```

**Variables**:
- `--output-dir`: Custom output directory (default: script_dir/csv)

---

### 02 - Plan_Features.py

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
- `csv/02_plan_features.csv`: Columns include:
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
python 02_Plan_Features.py /path/to/queries
python 02_Plan_Features.py /path/to/queries --output-dir /custom/output
```

**Variables**:
- `--output-dir`: Custom output directory (default: script_dir/csv)

---

### 03 - Row_Features.py

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
- `csv/03_row_features.csv`: Columns: query_file, template, row_count, byte_count

**Usage**:
```bash
python 03_Row_Features.py /path/to/queries
python 03_Row_Features.py /path/to/queries --output-dir /custom/output
```

**Variables**:
- `--output-dir`: Custom output directory (default: script_dir/csv)

---

### 04 - Merge_Data.py

**Purpose**: Merge runtime, plan features, and row features into complete dataset

**Workflow**:
1. Load 01_runtimes.csv
2. Load 02_plan_features.csv
3. Load 03_row_features.csv
4. Inner join all datasets on query_file and template columns
5. Export merged dataset to CSV

**Inputs**:
- `csv_dir` (positional): Directory containing the three CSV files

**Outputs**:
- `csv/complete_dataset.csv`: All columns from plan_features + row_count + byte_count + runtime

**Usage**:
```bash
python 04_Merge_Data.py csv/
```
