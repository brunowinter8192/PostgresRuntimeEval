# Misc

Supporting materials, query generation, and validation tools.

## Structure Note

This DOCS.md covers multiple subdirectories at root level. Per CLAUDE.md convention, each directory should have its own DOCS.md - but sparse directories with few scripts don't warrant individual documentation files. This consolidated approach is pragmatic, not canonical.

## Directory Structure

```
Misc/
    DOCS.md
    Learning-based_Query_Performance_Modeling_and_Pred.md   (Base paper)
    Setup.md                                                 (Environment setup)
    Generated_Queries/                                       [documented below]
    Cache_Validation/                                        [documented below]
    FFS_Comparison/                                          [documented below]
    Konzepte/
    specification/
```

---

## Generated_Queries

TPC-H query variants generated with different random seeds for benchmark testing.

### Directory Structure

```
Generated_Queries/
    generate_all_variants.sh
    Q1/ ... Q22/
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

## Cache_Validation

Runtime variance analysis across different cache states and prediction levels.

### Directory Structure

```
Cache_Validation/
    Plan_Level_CC/
        A_01_Runtime_Variance.py
        csv/
    cold_cache_validation/
    warm_cache/
    Comparison_Cold_Warm/
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

---

## FFS_Comparison

Comparison tools for evaluating SVM nu parameter impact on Forward Feature Selection.

### Directory Structure

```
FFS_Comparison/
    Plan_Level/
        01_Compare_Nu.py
        nu_0.5_summary.csv
        nu_0.65_summary.csv
    Operator_Level/
        01_Compare_Nu.py
        nu_0.5_overview.csv
        nu_0.65_overview.csv
```

### Plan_Level/01 - Compare_Nu.py

**Purpose:** Compare FFS results between nu=0.5 and nu=0.65 at plan level.

**Inputs:**
- `--baseline`: Baseline summary CSV (default: `nu_0.5_summary.csv`)
- `--alternative`: Alternative summary CSV (default: `nu_0.65_summary.csv`)
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
- `--baseline`: Baseline overview CSV (default: `nu_0.65_overview.csv`)
- `--alternative`: Alternative overview CSV (default: `nu_0.5_overview.csv`)
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
