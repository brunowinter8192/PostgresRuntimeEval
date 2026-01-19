# Misc

Supporting materials, query generation, and validation tools.

## Structure Note

This DOCS.md covers multiple subdirectories at root level. Per CLAUDE.md convention, each directory should have its own DOCS.md - but sparse directories with few scripts don't warrant individual documentation files. This consolidated approach is pragmatic, not canonical.

## Directory Structure

```
Misc/
├── DOCS.md
├── Learning-based_Query_Performance_Modeling_and_Pred.md   (Base paper)
├── Setup/                                                   [documented below]
│   ├── Setup.md                                            (Environment setup)
│   ├── Postgres_Docker/                                    [documented below]
│   └── Diff_TPCH/                                          [documented below]
├── Generated_Queries/                                       [documented below]
├── Cache_Validation/                                        [documented below]
├── FFS_Comparison/                                          [documented below]
├── Pass_Through/                                            [documented below]
├── Q17_Q20/                                                 [documented below]
└── specification/
    └── auto/
        ├── specification.md                                 (TPC-H Specification)
        └── specification_clean.md                           (TPC-H Specification, cleaned)
```

---

## Setup/Diff_TPCH

Unified diff between original TPC-H dbgen and PostgreSQL-adapted version.

### Directory Structure

```
Setup/Diff_TPCH/
├── generate_diff.sh
└── diff_output.md
```

### generate_diff.sh

**Purpose:** Generate unified diff between original and modified TPC-H dbgen directories.

**Inputs:**
- `$1` OLD_DIR: Path to original TPC-H dbgen directory
- `$2` NEW_DIR: Path to modified TPC-H dbgen directory
- `$3` OUTPUT_FILE: Output file path (.md or .txt)

**Excludes:** `*.o`, `*.tbl`, `dbgen`, `qgen`, `.DS_Store`

**Usage:**
```bash
cd Misc/Setup/Diff_TPCH
./generate_diff.sh \
  "<path-to-original-tpch>/dbgen" \
  "<repo-root>/TPC-H V3.0.1/dbgen" \
  diff_output.md
```

---

## Setup/Postgres_Docker

Docker Compose configuration for PostgreSQL TPC-H environment.

### Directory Structure

```
Setup/Postgres_Docker/
├── docker-compose.yaml
├── README.md
└── init/
    └── 01-schema.sql
```

### Configuration

- **docker-compose.yaml:** PostgreSQL 17-alpine3.22 with pgtune-optimized settings
- **init/01-schema.sql:** TPC-H schema with trailing delimiter workaround
- **README.md:** Setup instructions
- **.env:** Located at repo root (not in this folder)

**Usage:**
```bash
cd Misc/Setup/Postgres_Docker
docker compose up -d
```

---

## Generated_Queries

TPC-H query variants generated with different random seeds for benchmark testing.

### Directory Structure

```
Generated_Queries/
├── generate_all_variants.sh
└── Q1/ ... Q22/
```

Each `Q{N}/` folder contains 150 SQL files with naming pattern: `Q{N}_{counter}_seed_{seed}.sql`

### generate_all_variants.sh

**Purpose:** Generate TPC-H query variants using qgen with seeds from reference file.

**Inputs:**
- `$1` DBGEN_DIR: Path to TPC-H dbgen directory (contains `qgen`, `queries/`, `reference/`)
- `$2` OUTPUT_DIR: Output directory for generated query folders

**Configuration:**
- Line 9: `TEMPLATES=(15 17 20)` - which query templates to generate
- Uses seeds from `$DBGEN_DIR/reference/cmd_qgen_sf1`

**Usage:**
```bash
cd Generated_Queries
./generate_all_variants.sh "/path/to/TPC-H V3.0.1/dbgen" .
```

### Excluded Templates

| Template | Reason |
|----------|--------|
| Q15 | Uses `CREATE VIEW` - multi-statement, not compatible with `EXPLAIN ANALYZE` |
| Q17 | Execution time > 1 hour at SF1 |
| Q20 | Execution time > 1 hour at SF1 |

---

## Q17_Q20

Runtime demonstration for excluded templates Q17 and Q20.

### Directory Structure

```
Q17_Q20/
├── 01_Runtime_Demo.py
└── md/
    └── 01_runtime_demo.md
```

### 01 - Runtime_Demo.py

**Purpose:** Demonstrate that Q17 and Q20 have exceptionally long runtimes compared to other templates.

**Inputs:**
- `queries_dir` (positional): Directory containing Q17/ and Q20/ folders with SQL files
- `--output-dir` (required): Output directory for MD export
- `--runs` (optional): Number of query executions per type (default: 5)

**Outputs:**
- `01_runtime_demo.md`: Runtime listing with averages for Q17 and Q20

**Usage:**
```bash
# From repository root:
python3 Misc/Q17_Q20/01_Runtime_Demo.py Misc/Generated_Queries --output-dir Misc/Q17_Q20/md
```

---

## Cache_Validation

Runtime variance analysis across different cache states and prediction levels.

### Directory Structure

```
Cache_Validation/
├── Plan_Level_CC/
│   ├── A_01_Runtime_Variance.py
│   └── csv/
├── cold_cache_validation/
│   └── restart_docker/
│       ├── execute_queries.py
│       └── csv/
├── warm_cache/
│   ├── warm_cache.py
│   └── csv/
└── Comparison_Cold_Warm/
    ├── compare_cold_warm.py
    └── csv/
```

### Plan_Level_CC/A_01 - Runtime_Variance.py

**Purpose:** Analyze runtime variance per template for two datasets and compare them visually.

**Inputs:**
- `baseline_csv` (positional): Path to baseline dataset CSV
- `state1_csv` (positional): Path to State_1 dataset CSV
- `--output-dir` (required): Output directory for CSVs and PNGs

**Outputs:**
- `A_01_baseline_variance.csv`: Per-template variance stats
- `A_01_state1_variance.csv`: Per-template variance stats
- `A_01_comparison.csv`: Side-by-side comparison with absolute deltas
- `A_01_cv_*.png`: CV bar plots

**Usage:**
```bash
cd Cache_Validation/Plan_Level_CC
python3 A_01_Runtime_Variance.py \
  ../../Prediction_Methods/Plan_Level_1/Datasets/Baseline/complete_dataset.csv \
  ../../Prediction_Methods/Plan_Level_1/Datasets/State_1/complete_dataset.csv \
  --output-dir csv
```

**Metrics:**
| Column | Description |
|--------|-------------|
| count | Number of samples per template |
| mean | Mean runtime (ms) |
| std | Standard deviation |
| cv | Coefficient of variation (std/mean * 100) |
| min/max | Runtime range |
| range | max - min |

### cold_cache_validation/restart_docker/execute_queries.py

**Purpose:** Cold cache runtime measurement - restarts OrbStack + purges macOS cache before each query execution to ensure true cold cache state.

**Inputs:**
- `$1` queries_dir: Path to Generated_Queries directory

**Outputs:**
- `csv/runtime_{timestamp}.csv`: Per-template runtime with mean, std_dev, cv, individual runs

**Configuration:**
- RUNS=5 per template
- Skips Q15 (VIEW-based)

**Usage:**
```bash
cd Cache_Validation/cold_cache_validation/restart_docker
python3 execute_queries.py ../../Generated_Queries
```

### warm_cache/warm_cache.py

**Purpose:** Warm cache runtime measurement - executes 5 runs per template without restart.

**Inputs:**
- `$1` queries_dir: Path to Generated_Queries directory

**Outputs:**
- `csv/warm_cache_{timestamp}.csv`: Per-template runtime with mean, std_dev, cv, individual runs

**Usage:**
```bash
cd Cache_Validation/warm_cache
python3 warm_cache.py ../Generated_Queries
```

### Comparison_Cold_Warm/compare_cold_warm.py

**Purpose:** Compare cold vs warm cache runtimes and analyze first-run effect in warm cache.

**Inputs:**
- `$1` cold_csv: Path to cold cache runtime CSV
- `$2` warm_csv: Path to warm cache runtime CSV

**Outputs:**
- `csv/warm_first_run_effect_{ts}.csv`: Analysis of run_1 vs runs_2-5 in warm cache
- `csv/cold_vs_warm_{ts}.csv`: Comparison with speedup factor

**Usage:**
```bash
cd Cache_Validation/Comparison_Cold_Warm
python3 compare_cold_warm.py ../cold_cache_validation/restart_docker/csv/runtime_*.csv ../warm_cache/csv/warm_cache_*.csv
```

---

## FFS_Comparison

Comparison tools for evaluating SVM nu parameter impact on Forward Feature Selection.

### Directory Structure

```
FFS_Comparison/
├── C_SVM_Parameter.md                    (Thesis appendix: SVM parameter documentation)
├── Plan_Level/
│   ├── 01_Compare_Nu.py
│   └── Nu_0.5/                           (FFS results with nu=0.5)
│       ├── 01_ffs_progress.csv
│       ├── 01_ffs_summary.csv
│       └── 01_ffs_stability.csv
└── Operator_Level/
    ├── 01_Compare_Nu.py
    └── Nu_0.5/                           (FFS results with nu=0.5)
        └── SVM/{target}/{Operator}_csv/
```

### C_SVM_Parameter.md

Thesis appendix documenting SVM configuration and nu parameter exploration. Source for Anhang C.

### Plan_Level/01 - Compare_Nu.py

**Purpose:** Compare FFS results between nu=0.5 and nu=0.65 at plan level.

**Inputs:**
- `--baseline`: Baseline summary CSV (default: `Nu_0.5/01_ffs_summary.csv`)
- `--alternative`: Alternative summary CSV path
- `--output-dir`: Output directory (default: `.`)

**Outputs:**
- `01_nu_comparison.csv`: mre_0.5, mre_0.65, delta_mre, n_features_*, features_*, better

**Usage:**
```bash
cd Misc/FFS_Comparison/Plan_Level
python3 01_Compare_Nu.py
```

### Operator_Level/01 - Compare_Nu.py

**Purpose:** Compare FFS results between nu=0.65 and nu=0.5 at operator level.

**Inputs:**
- `--baseline`: Baseline overview CSV
- `--alternative`: Alternative overview CSV
- `--output-dir`: Output directory (default: `.`)

**Outputs:**
- `01_nu_comparison.csv`: operator, target, mre_ffs_*, mre_final_*, delta_mre_*, better_ffs, better_final

**Usage:**
```bash
cd Misc/FFS_Comparison/Operator_Level
python3 01_Compare_Nu.py
```

### Delta Interpretation

| Script | delta_mre > 0 means |
|--------|---------------------|
| Plan_Level | nu=0.65 is better |
| Operator_Level | nu=0.5 is better |

---

## Pass_Through

Analysis tool for identifying pass-through operators (operators whose execution time equals their children's time).

### Directory Structure

```
Pass_Through/
├── 02_Passthrough_Analysis.py
└── csv/
    └── 02_passthrough_analysis.csv
```

### 02 - Passthrough_Analysis.py

**Purpose:** Analyze which operators have execution time approximately equal to their children (passthrough behavior).

**Inputs:**
- `input_file` (positional): Path to operator dataset CSV
- `--output-dir` (required): Output directory for CSV results

**Outputs:**
- `csv/02_passthrough_analysis.csv`
  - Columns: node_type, instance_count, mean_parent_time, mean_max_child_time, ratio_pct
  - ratio_pct ~100% indicates passthrough behavior

**Usage:**
```bash
cd Misc/Pass_Through
python3 02_Passthrough_Analysis.py \
  ../../Prediction_Methods/Hybrid_1/Datasets/Baseline_SVM/training.csv \
  --output-dir .
```

**Interpretation:**

| ratio_pct | Meaning |
|-----------|---------|
| ~100% | Pure passthrough - operator adds no time |
| 100-105% | Near passthrough - minimal own computation |
| >110% | Computing operator - significant own work |
