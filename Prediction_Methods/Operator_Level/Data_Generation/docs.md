# Data Generation - Operator-Level Prediction Methods

## Directory Structure

```
Data_Generation/
├── config.py                         # Shared infrastructure and utilities. Used by: 01, 02, 03,
                                      # 04, 05, 06
├── features.md                       # Feature definitions and extraction logic
├── targets.md                        # Target variable definitions and extraction logic
├── 05_Extract_Features.py            # Main feature extraction script
├── 06_Extract_Targets.py             # Main target extraction script
├── Cache_Validation/                 # Cold cache consistency validation
│   ├── 01_Cache_Val.py
│   └── [outputs]                     # Generated CSV files
├── Basic_Explain/                    # Exploratory EXPLAIN analysis
│   ├── 02_PG_Class.py
│   ├── 03_Explain_JSON.py
│   ├── 04_Explain_Analyse.py
│   └── md/                           # Generated markdown exports
└── csv/                              # Dataset outputs
    ├── 07_Merge_Data.py
    └── [outputs]                     # Generated CSV files
```

---

## Documentation Files

### features.md
Defines all 11 feature variables extracted from PostgreSQL EXPLAIN output:
- Core features: np, nt, nt1, nt2, sel
- Additional features: startup_cost, total_cost, plan_width, reltuples, parallel_workers
- Extraction logic and examples for each feature

### targets.md
Defines target variables and metadata extracted from EXPLAIN ANALYSE output:
- Target variables: actual_startup_time, actual_total_time
- Metadata: query_file, node_type, node_id, depth, parent_relationship, subplan_name
- Extraction logic with traversal order specification

---

## Shared Infrastructure (config.py)

### Database Configuration
Provides database connection configuration via argparse flags:
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

### Used By
Scripts: 01_Cache_Val.py, 02_PG_Class.py, 03_Explain_JSON.py, 04_Explain_Analyse.py, 05_Extract_Features.py, 06_Extract_Targets.py

---

## Workflow Execution Order

Execute scripts in this sequence:

```
1. Cache_Validation/01_Cache_Val.py       # Optional: Validate cold cache consistency
2. Basic_Explain/02_PG_Class.py           # Optional: Explore pg_class statistics
3. Basic_Explain/03_Explain_JSON.py       # Optional: Export EXPLAIN JSON
4. Basic_Explain/04_Explain_Analyse.py    # Optional: Export EXPLAIN ANALYSE JSON
5. 05_Extract_Features.py                 # Required: Extract features from all queries
6. 06_Extract_Targets.py                  # Required: Extract targets from all queries
7. CSV/07_Merge_Data.py                   # Required: Merge features and targets
```

Scripts 01-04 are optional exploratory tools. Scripts 05-07 are required for dataset generation.

---

## Script Documentation

### Cache_Validation/01_Cache_Val.py

**Purpose**: Validate cold cache consistency by running Q1 first seed multiple times with OrbStack restarts between runs

**Input**:
- `query_dir` (positional): Path to query directory containing Q1-Q22 templates

**Variables** (via argparse):
- `--output-dir`: Output directory for CSV files (default: `./`)
- `--runs`: Number of cold cache runs to execute (default: `5`)
- `--container-name`: Docker container name (default: `tpch-postgres`)

Database configuration flags: see config.py

**Output**:
- `cold_cache_runs.csv` (semicolon-delimited): All individual run times
  - Columns: query_file, runtime
- `cold_cache_stats.csv` (semicolon-delimited): Statistics (mean, span %, span ms)
  - Columns: query_file, mean, spannweite_percent, spannweite_ms

**Important Notes**:
- Requires sudo privileges for macOS `purge` command
- Restarts OrbStack and purges macOS cache between each run
- Only processes Q1 template for validation

---

### Basic_Explain/02_PG_Class.py

**Purpose**: Export pg_class statistics for tables referenced by each operator in EXPLAIN plans

**Input**:
- `query_dir` (positional): Path to query directory containing Q1-Q22 templates

**Variables** (via argparse):
- `--output-dir`: Output directory for markdown file (required)

Database configuration flags: see config.py

**Output**:
- `pg_class_per_operator_{timestamp}.md`: Markdown file with pg_class statistics per operator

**Important Notes**:
- Processes only first seed of each template (Q1-Q22, excluding Q15)
- Uses EXPLAIN (no ANALYZE) for plan extraction

---

### Basic_Explain/03_Explain_JSON.py

**Purpose**: Export complete EXPLAIN JSON for first seed of each query template

**Input**:
- `query_dir` (positional): Path to query directory containing Q1-Q22 templates

**Variables** (via argparse):
- `--output-dir`: Output directory for markdown file (required)

Database configuration flags: see config.py

**Output**:
- `explain_json_export_{timestamp}.md`: Markdown file with full EXPLAIN JSON plans

**Important Notes**:
- Processes only first seed of each template (Q1-Q22, excluding Q15)
- Uses EXPLAIN (no ANALYZE) for plan extraction

---

### Basic_Explain/04_Explain_Analyse.py

**Purpose**: Export EXPLAIN ANALYSE JSON with cold cache for first seed of each query template

**Input**:
- `query_dir` (positional): Path to query directory containing Q1-Q22 templates

**Variables** (via argparse):
- `--output-dir`: Output directory for markdown file (required)
- `--container-name`: Docker container name (default: `tpch-postgres`)

Database configuration flags: see config.py

**Output**:
- `explain_analyse_cold_cache_{timestamp}.md`: Markdown file with EXPLAIN ANALYSE JSON

**Important Notes**:
- Requires sudo privileges for macOS `purge` command
- Restarts OrbStack and purges cache before each query
- Processes only first seed of each template (Q1-Q22, excluding Q15)

---

### 05_Extract_Features.py

**Purpose**: Extract static operator-level features from EXPLAIN (no ANALYZE) for all TPC-H queries

**Input**:
- `query_dir` (positional): Path to query directory containing Q1-Q22 templates

**Variables** (via argparse):
- `--output-dir`: Output directory for CSV file (required)

Database configuration flags: see config.py

**Output**:
- `features_{timestamp}.csv` (semicolon-delimited): 16 columns
  - Metadata: query_file, node_id, node_type, depth, parent_relationship, subplan_name
  - Features: np, nt, nt1, nt2, sel, startup_cost, total_cost, plan_width, reltuples, parallel_workers

**Important Notes**:
- Processes ALL queries in Q1-Q22 (excluding Q15)
- Uses EXPLAIN (no ANALYZE) for fast extraction
- No cold cache restarts required

---

### 06_Extract_Targets.py

**Purpose**: Extract actual runtime targets from EXPLAIN ANALYSE with cold cache restarts for all TPC-H queries

**Input**:
- `query_dir` (positional): Path to query directory containing Q1-Q22 templates

**Variables** (via argparse):
- `--output-dir`: Output directory for CSV file (required)
- `--container-name`: Docker container name (default: `tpch-postgres`)

Database configuration flags: see config.py

**Output**:
- `targets_{timestamp}.csv` (semicolon-delimited): 8 columns
  - Metadata: query_file, node_id, node_type, depth, parent_relationship, subplan_name
  - Targets: actual_startup_time, actual_total_time

**Important Notes**:
- Requires sudo privileges for macOS `purge` command
- Restarts OrbStack and purges cache before EACH query execution
- Processes ALL queries in Q1-Q22 (excluding Q15)
- Execution time: Several hours due to cold cache restarts

---

### CSV/07_Merge_Data.py

**Purpose**: Merge features and targets CSVs into single operator-level dataset

**Input**: None (all inputs via argparse)

**Variables** (via argparse):
- `--features-csv`: Path to features CSV file (required)
- `--targets-csv`: Path to targets CSV file (required)
- `--output-dir`: Output directory for merged CSV (required)

**Output**:
- `operator_dataset_{timestamp}.csv` (semicolon-delimited): 18 columns
  - Metadata (6): query_file, node_id, node_type, depth, parent_relationship, subplan_name
  - Features (10): np, nt, nt1, nt2, sel, startup_cost, total_cost, plan_width, reltuples, parallel_workers
  - Targets (2): actual_startup_time, actual_total_time

**Important Notes**:
- Performs inner join on [query_file, node_id]
- Validates row count consistency before and after merge
- Raises error if row counts don't match
