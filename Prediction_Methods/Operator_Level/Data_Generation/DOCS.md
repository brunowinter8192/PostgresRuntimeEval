# Data Generation - Operator-Level Prediction Methods

## Working Directory

**CRITICAL:** All commands assume CWD = `Data_Generation/`

```bash
cd Prediction_Methods/Operator_Level/Data_Generation
```

## Directory Structure

```
Data_Generation/
├── config.py                         # Shared infrastructure and utilities
├── features.md                       # Feature definitions and extraction logic
├── targets.md                        # Target variable definitions
├── DOCS.md                           # This file
├── 01a_Extract_Features.py           # Extract static features from EXPLAIN
├── 01b_Extract_Targets.py            # Extract runtime targets from EXPLAIN ANALYSE
├── 02_Merge_Data.py                  # Merge features and targets
├── A_01b_PG_Class.py                 # Analysis: pg_class statistics export
├── A_01c_Explain_JSON.py             # Analysis: EXPLAIN JSON export
├── A_01d_Explain_Analyse.py          # Analysis: EXPLAIN ANALYSE JSON export
├── Basic_Explain/                    # Output folder for A_01b, A_01c, A_01d
│   └── md/                           # Generated markdown exports
└── csv/                              # Dataset outputs
```

---

## Shared Infrastructure (config.py)

### Database Configuration

Database connection via argparse flags:
- `--db-host`: Database host (default: `localhost`)
- `--db-port`: Database port (default: `5432`)
- `--db-name`: Database name (default: `tpch`)
- `--db-user`: Database user (default: `postgres`)
- `--db-password`: Database password (default: `postgres`)

### Functions

- `get_db_config()`: Build database configuration dict from parameters
- `wait_for_postgres()`: Wait for PostgreSQL to be ready
- `wait_for_docker_ready()`: Wait for Docker daemon to be ready
- `wait_for_orbstack_stopped()`: Wait for OrbStack to stop
- `wait_for_orbstack_running()`: Wait for OrbStack to be running
- `restart_orbstack_and_purge()`: Restart OrbStack and purge macOS cache
- `start_container()`: Start Docker container by name
- `get_query_files_all_templates()`: Get all query files from Q1-Q22 (excluding Q15)
- `get_first_seed_per_template()`: Get first seed file per template Q1-Q22 (excluding Q15)

### Constants

- `DEFAULT_DB_CONFIG`: Default database configuration dict
- `DEFAULT_CONTAINER_NAME`: Default Docker container name (`tpch-postgres`)

---

## Workflow Execution Order

### Main Workflow (Required)

```
01a_Extract_Features.py ──┐
                          ├──→ 02_Merge_Data.py → operator_dataset.csv
01b_Extract_Targets.py ───┘
```

- 01a and 01b can run in **parallel** (no dependencies)
- 02 requires outputs from **both** 01a and 01b

### Analysis Tools (Optional)

```
A_01b_PG_Class.py        # pg_class statistics (first seeds)
A_01c_Explain_JSON.py    # EXPLAIN JSON export (first seeds)
A_01d_Explain_Analyse.py # EXPLAIN ANALYSE JSON (first seeds, cold cache)
```

All A_ scripts are **independent** and can run in any order.

---

## Script Documentation

### 01a_Extract_Features.py

**Purpose:** Extract static operator-level features from EXPLAIN (no ANALYZE) for all TPC-H queries

**Input:**
- `query_dir` (positional): Path to query directory containing Q1-Q22 templates

**Variables:**
- `--output-dir`: Output directory for CSV file (required)
- Database configuration flags (see config.py)

**Output:**
- `features_{timestamp}.csv` (semicolon-delimited): 16 columns
  - Metadata: query_file, node_id, node_type, depth, parent_relationship, subplan_name
  - Features: np, nt, nt1, nt2, sel, startup_cost, total_cost, plan_width, reltuples, parallel_workers

**Notes:**
- Processes ALL queries in Q1-Q22 (excluding Q15)
- Uses EXPLAIN (no ANALYZE) for fast extraction
- No cold cache restarts required

**Usage:**
```bash
python3 01a_Extract_Features.py ../../../Misc/Generated_Queries --output-dir csv
```

---

### 01b_Extract_Targets.py

**Purpose:** Extract actual runtime targets from EXPLAIN ANALYSE with cold cache restarts

**Input:**
- `query_dir` (positional): Path to query directory containing Q1-Q22 templates

**Variables:**
- `--output-dir`: Output directory for CSV file (required)
- `--container-name`: Docker container name (default: `tpch-postgres`)
- Database configuration flags (see config.py)

**Output:**
- `targets_{timestamp}.csv` (semicolon-delimited): 8 columns
  - Metadata: query_file, node_id, node_type, depth, parent_relationship, subplan_name
  - Targets: actual_startup_time, actual_total_time

**Notes:**
- Requires sudo privileges for macOS `purge` command
- Restarts OrbStack and purges cache before EACH query execution
- Execution time: Several hours due to cold cache restarts

**Usage:**
```bash
python3 01b_Extract_Targets.py ../../../Misc/Generated_Queries --output-dir csv
```

---

### 02_Merge_Data.py

**Purpose:** Merge features and targets CSVs into single operator-level dataset

**Input:** None (all inputs via argparse)

**Variables:**
- `--features-csv`: Path to features CSV file (required)
- `--targets-csv`: Path to targets CSV file (required)
- `--output-dir`: Output directory for merged CSV (required)

**Output:**
- `operator_dataset_{timestamp}.csv` (semicolon-delimited): 18 columns
  - Metadata (6): query_file, node_id, node_type, depth, parent_relationship, subplan_name
  - Features (10): np, nt, nt1, nt2, sel, startup_cost, total_cost, plan_width, reltuples, parallel_workers
  - Targets (2): actual_startup_time, actual_total_time

**Notes:**
- Performs inner join on [query_file, node_id]
- Validates row count consistency before and after merge

**Usage:**
```bash
python3 02_Merge_Data.py \
    --features-csv csv/features_20251102_135531.csv \
    --targets-csv csv/targets_20251102_113110.csv \
    --output-dir csv
```

---

### A_01b_PG_Class.py

**Purpose:** Export pg_class statistics for tables referenced by each operator

**Input:**
- `query_dir` (positional): Path to query directory

**Variables:**
- `--output-dir`: Output directory for markdown file (required)
- Database configuration flags (see config.py)

**Output:**
- `pg_class_per_operator_{timestamp}.md`: pg_class statistics per operator

**Notes:**
- Processes only first seed of each template (Q1-Q22, excluding Q15)

**Usage:**
```bash
python3 A_01b_PG_Class.py ../../../Misc/Generated_Queries --output-dir Basic_Explain/md
```

---

### A_01c_Explain_JSON.py

**Purpose:** Export complete EXPLAIN JSON for first seed of each query template

**Input:**
- `query_dir` (positional): Path to query directory

**Variables:**
- `--output-dir`: Output directory for markdown file (required)
- Database configuration flags (see config.py)

**Output:**
- `explain_json_export_{timestamp}.md`: Full EXPLAIN JSON plans

**Notes:**
- Processes only first seed of each template (Q1-Q22, excluding Q15)

**Usage:**
```bash
python3 A_01c_Explain_JSON.py ../../../Misc/Generated_Queries --output-dir Basic_Explain/md
```

---

### A_01d_Explain_Analyse.py

**Purpose:** Export EXPLAIN ANALYSE JSON with cold cache for first seed of each template

**Input:**
- `query_dir` (positional): Path to query directory

**Variables:**
- `--output-dir`: Output directory for markdown file (required)
- `--container-name`: Docker container name (default: `tpch-postgres`)
- Database configuration flags (see config.py)

**Output:**
- `explain_analyse_cold_cache_{timestamp}.md`: EXPLAIN ANALYSE JSON

**Notes:**
- Requires sudo privileges
- Restarts OrbStack and purges cache before each query

**Usage:**
```bash
python3 A_01d_Explain_Analyse.py ../../../Misc/Generated_Queries --output-dir Basic_Explain/md
```

---

## Documentation Files

### features.md

Defines all 11 feature variables extracted from PostgreSQL EXPLAIN output:
- Core features: np, nt, nt1, nt2, sel
- Additional features: startup_cost, total_cost, plan_width, reltuples, parallel_workers

### targets.md

Defines target variables and metadata extracted from EXPLAIN ANALYSE output:
- Target variables: actual_startup_time, actual_total_time
- Metadata: query_file, node_type, node_id, depth, parent_relationship, subplan_name
