# Runtime_Prediction - DOCS.md

## Working Directory

**CRITICAL:** All commands assume CWD = `Runtime_Prediction/`

```bash
cd /path/to/Hybrid_2/Runtime_Prediction
```

---

## External Dependencies (Hybrid_1)

| Resource | Path (relative to CWD) |
|----------|------------------------|
| Operator FFS | `../../Hybrid_1/Runtime_Prediction/Baseline_SVM/SVM/Operators/operator_overview.csv` |
| Pattern FFS | `../../Hybrid_1/Runtime_Prediction/Baseline_SVM/SVM/Patterns/two_step_evaluation_overview.csv` |

---

## Workflow Dependency Graph

```
02_Operator_Train
       |
       v
04_Query_Prediction ----+
       |                |
       v                |
06_Extract_Test_Patterns|
       |                |
       v                |
07_Order_Patterns ------+-----> 08_Error_Baseline
       |                              |
       +------------------------------+
       |
       v
09_Pretrain_Patterns
       |
       v
10_Pattern_Selection (9 runs parallel)
       |
       v
12_Query_Prediction
```

**Key Dependencies:**
- 08 requires 07 output (07_patterns_by_frequency.csv)
- 07 and 08 require 04 output (predictions.csv for avg_mre)
- 09 requires 07 output (pattern metadata)
- 10 requires 09 output (pretrained models)

---

## Phase 1: Operator Baseline

| Step | Script | Input | Output |
|------|--------|-------|--------|
| 1 | 02_Operator_Train.py | Dataset/Operators/Training_Training | Model/Training_Training/Operator |
| 2 | 04_Query_Prediction.py | Dataset/Baseline/Training_Test.csv | Evaluation/Operator_Training_Test/predictions.csv |

---

## Phase 2: Pattern Preparation

| Step | Script | Depends On | Output |
|------|--------|------------|--------|
| 3 | 06_Extract_Test_Patterns.py | - | Pattern_Selection/06_test_pattern_occurrences.csv |
| 4 | 07_Order_Patterns.py | Step 2, 3 | Pattern_Selection/07_patterns_by_size.csv, 07_patterns_by_frequency.csv |
| 5 | 08_Error_Baseline.py | Step 2, 3, 4 | Pattern_Selection/08_patterns_by_error.csv |
| 6 | 09_Pretrain_Patterns.py | Step 4 | Model/Training_Training/Pattern/{hash}/ |

---

## Phase 3: Pattern Selection (9 Runs)

### Selection Matrix

| Strategy | Variant | sorted_patterns | Extra Flags | Output Dir |
|----------|---------|-----------------|-------------|------------|
| size | Baseline | 07_patterns_by_size.csv | - | Pattern_Selection/Size/Baseline |
| size | Epsilon | 07_patterns_by_size.csv | --epsilon 0.001 | Pattern_Selection/Size/Epsilon |
| frequency | Baseline | 07_patterns_by_frequency.csv | - | Pattern_Selection/Frequency/Baseline |
| frequency | Epsilon | 07_patterns_by_frequency.csv | --epsilon 0.001 | Pattern_Selection/Frequency/Epsilon |
| error | Baseline | 08_patterns_by_error.csv | - | Pattern_Selection/Error/Baseline |
| error | Epsilon | 08_patterns_by_error.csv | --epsilon 0.001 | Pattern_Selection/Error/Epsilon |

### Variant Descriptions

| Variant | Flag | Description |
|---------|------|-------------|
| Baseline | - | Accept any improvement (delta > 0) |
| Epsilon | --epsilon 0.001 | Require min 0.1% MRE improvement |

### Output per Run

- `selected_patterns.csv` - Patterns that improved MRE (used by 12_Query_Prediction)
- `selection_log.csv` - Full iteration log
- `selection_summary.csv` - Aggregate counts and final MRE

---

## Phase 4: Final Prediction

| Step | Script | Input | Output |
|------|--------|-------|--------|
| 10 | 12_Query_Prediction/ | Test.csv + selected_patterns.csv | Evaluation/{Strategy}/ |

---

## Output Structure

```
Runtime_Prediction/
├── Model/
│   └── Training_Training/
│       ├── Operator/{target}/{Operator}/model.pkl
│       └── Pattern/{hash}/model_*.pkl, features.json
├── Pattern_Selection/
│   ├── 06_test_pattern_occurrences.csv
│   ├── 07_patterns_by_size.csv
│   ├── 07_patterns_by_frequency.csv
│   ├── 08_patterns_by_error.csv
│   ├── Size/{Baseline,Epsilon}/selected_patterns.csv
│   ├── Frequency/{Baseline,Epsilon}/selected_patterns.csv
│   └── Error/{Baseline,Epsilon}/selected_patterns.csv
└── Evaluation/
    ├── Operator_Training_Test/12_predictions.csv
    ├── {Strategy}/{Config}/
    │   ├── 12_predictions.csv
    │   ├── A_01a_overall_mre.csv
    │   ├── A_01a_template_mre.csv
    │   └── A_01a_template_mre_plot.png
    └── PatternUsage/
        ├── A_02c_patterns.csv
        └── A_02c_summary.csv
```

## Script Documentation

### 02 - Operator_Train.py

**Purpose:** Train SVM models for each operator-target using final features from operator_overview.csv.

**Workflow:**
1. Load two_step_evaluation_overview.csv
2. For each operator-target: train NuSVR pipeline (MaxAbsScaler + NuSVR)
3. Save model.pkl

**Inputs:**
- `dataset_dir`: Directory with operator CSV files (e.g., Dataset/Operators/Training_Training/)
- `overview_file`: Path to two_step_evaluation_overview.csv

**Outputs:**
- `{output-dir}/{target}/{Operator}/model.pkl`

**Usage:**
```
# Training_Training models
python3 02_Operator_Train.py ../Dataset/Operators/Training_Training SVM/Operator/Training_Training/two_step_evaluation_overview.csv --output-dir Model/Operator/Training_Training

# Training_Full models
python3 02_Operator_Train.py ../Dataset/Operators/Training_Full SVM/Operator/Training_Full/two_step_evaluation_overview.csv --output-dir Model/Operator/Training_Full
```

---

### 04 - Query_Prediction.py

**Purpose:** Bottom-up query prediction using operator models only (baseline).

**Workflow:**
1. Load test data and operator models
2. For each query: predict leaf operators first
3. Propagate predictions upward (st1/rt1/st2/rt2 from children)
4. Export all operator predictions

**Inputs:**
- `test_file`: Path to Training_Test.csv
- `overview_file`: Path to two_step_evaluation_overview.csv
- `models_dir`: Path to Model/Operator/

**Outputs:**
- `{output-file}`: predictions.csv with actual/predicted times

**Usage:**
```
python3 04_Query_Prediction.py ../Dataset/Training_Test.csv SVM/Operator/two_step_evaluation_overview.csv Model/Operator --output-file Evaluation/Operator_Training_Test/predictions.csv
```

---

### 06 - Extract_Test_Patterns.py

**Purpose:** Find occurrences of known patterns in test set.

**Workflow:**
1. Load test data (Training_Test.csv)
2. Load known patterns from Data_Generation
3. Build tree for each query, compute pattern hashes
4. Match against known patterns, record occurrences

**Inputs:**
- `test_file`: Path to Training_Test.csv
- `patterns_file`: Path to 01_patterns.csv

**Outputs:**
- `06_test_pattern_occurrences.csv`

**Usage:**
```
python3 06_Extract_Test_Patterns.py ../Dataset/Baseline/Training_Test.csv ../Data_Generation/csv/Training_Training/01_patterns.csv --output-dir Pattern_Selection
```

---

### 07 - Order_Patterns.py

**Purpose:** Order patterns by two strategies for greedy selection, including avg_mre and unique_template_count.

**Workflow:**
1. Load test pattern occurrences from 06 (includes `template` column)
2. Load operator predictions to calculate avg_mre per pattern
3. Aggregate by pattern: count occurrences, count unique templates, calculate avg_mre
4. Sort by SIZE and FREQUENCY strategies

**unique_template_count:**
Pattern muss in mehreren Query-Templates vorkommen um generalisierbar zu sein.
- `template` = Query-Template (z.B. `Q1`, `Q9` - extrahiert aus query_file)
- `unique_template_count` = Anzahl distinct templates pro pattern (max 14 in TPC-H)

**Sorting Strategies:**

| Strategy | Primary | Secondary | Tiebreaker |
|----------|---------|-----------|------------|
| Size | operator_count ASC | occurrence_count DESC | pattern_hash ASC |
| Frequency | occurrence_count DESC | operator_count ASC | pattern_hash ASC |

**Tiebreaker:** `pattern_hash` (alphabetisch) garantiert deterministische Reihenfolge bei gleichen Werten.

**Inputs:**
- `occurrences_file`: Path to 06_test_pattern_occurrences.csv
- `--operator-predictions`: Path to operator predictions CSV (for avg_mre calculation)

**Outputs:**
- `07_patterns_by_size.csv` (includes occurrence_count, unique_template_count, avg_mre)
- `07_patterns_by_frequency.csv` (includes occurrence_count, unique_template_count, avg_mre)

**Usage:**
```
python3 07_Order_Patterns.py Pattern_Selection/06_test_pattern_occurrences.csv --operator-predictions Evaluation/Operator_Training_Training_on_Test/predictions.csv --output-dir Pattern_Selection
```

---

### 08 - Error_Baseline.py

**Purpose:** Calculate error score for each pattern based on operator baseline predictions.

**Workflow:**
1. Load pattern occurrences and operator predictions
2. For each pattern: lookup MRE at root_node_id in operator predictions
3. Calculate error_score = occurrence_count * avg_mre
4. Sort by error_score DESC (highest error = most potential improvement)

**Inputs:**
- `pattern_occurrences_file`: 06_test_pattern_occurrences.csv
- `operator_predictions_file`: Operator baseline predictions.csv
- `patterns_metadata_file`: 07_patterns_by_frequency.csv

**Outputs:**
- `08_patterns_by_error.csv`

**Usage:**
```
python3 08_Error_Baseline.py Pattern_Selection/06_*.csv Evaluation/Operator_Training_Test/predictions.csv Pattern_Selection/07_patterns_by_frequency.csv --output-dir Pattern_Selection
```

---

### 09 - Pretrain_Patterns.py

**Purpose:** Train SVM models for all patterns in parallel (speedup for selection).

**Workflow:**
1. Load pattern FFS features and metadata
2. Filter patterns with valid FFS for both targets
3. Parallel training: aggregate pattern data on-the-fly, train NuSVR
4. Save model_execution_time.pkl, model_start_time.pkl, features.json

**Inputs:**
- `pattern_ffs_file`: Path to pattern_ffs_overview.csv
- `patterns_metadata_file`: Path to 07_patterns_by_frequency.csv
- `training_file`: Path to Training_Training.csv

**Outputs:**
- `{output-dir}/{hash}/model_execution_time.pkl`
- `{output-dir}/{hash}/model_start_time.pkl`
- `{output-dir}/{hash}/features.json`

**Variables:**
- `--n-jobs`: Parallel jobs (-1 = all cores)

**Usage:**
```
python3 09_Pretrain_Patterns.py SVM/Pattern/pattern_ffs_overview.csv Pattern_Selection/07_patterns_by_frequency.csv ../Dataset/Baseline/Training_Training.csv --output-dir Model/Patterns_Pretrained --n-jobs -1
```

---

### 10_Pattern_Selection/

[See DOCS.md](10_Pattern_Selection/DOCS.md)

---

### 12_Query_Prediction/

[See DOCS.md](12_Query_Prediction/DOCS.md)

---

### A_01a - Query_Evaluation.py

**Purpose:** Evaluate query-level prediction accuracy on root operators.

**Workflow:**
1. Load predictions.csv
2. Filter depth=0 (root operators)
3. Calculate MRE per template and overall
4. Export metrics and bar plot

**Inputs:**
- `predictions_file`: Any predictions.csv

**Outputs:**
- `{output-dir}/overall_mre.csv`
- `{output-dir}/template_mre.csv`
- `{output-dir}/template_mre_plot.png`

**Usage:**
```
python3 A_02a_Query_Evaluation.py Evaluation/Operator_Training_Test/predictions.csv --output-dir Evaluation/Operator_Training_Test
```

---

### A_02a - Epsilon_Analysis.py

**Purpose:** Analyze delta distribution for EPSILON threshold determination.

**Workflow:**
1. Load selection_log.csv
2. Filter SELECTED patterns
3. Calculate delta statistics (mean, median, min, max)
4. Extract delta distribution sorted by delta DESC

**Inputs:**
- `selection_log_file`: Path to selection_log.csv

**Outputs:**
- `{output-dir}/{prefix}_delta_stats.csv`: Summary statistics
  - Columns: selected_count;mean_delta;median_delta;min_delta;max_delta
- `{output-dir}/{prefix}_delta_distribution.csv`: Full delta distribution for SELECTED patterns
  - Columns: iteration;pattern_hash;delta (sorted by delta DESC)

**Variables:**
- `--prefix`: Prefix for output filenames (default: none)

**Usage:**
```
python3 A_02a_Epsilon_Analysis.py Pattern_Selection/Size/Baseline/selection_log.csv --output-dir Pattern_Selection/Convergence --prefix Size_Baseline
```

---

### A_02b - Convergence_Analysis.py

**Purpose:** Determine early stopping point and recommended MRE threshold.

**Outputs:**
- `{output-dir}/{prefix}_A_02b_summary.csv`
- `{output-dir}/{prefix}_A_02b_mre_progression.png`

**Variables:**
- `--prefix`: Prefix for output filenames (default: none)

**Usage:**
```
python3 A_02b_Convergence_Analysis.py Pattern_Selection/Size/Baseline/selection_log.csv --output-dir Pattern_Selection/Convergence --prefix Size_Baseline
```

---

### A_02d - Convergence_Combined.py

**Purpose:** Create combined convergence plot with all 3 strategies overlaid.

**Outputs:** `{output-dir}/A_02d_convergence_{variant}.png`

**Usage:**
```
python3 A_02d_Convergence_Combined.py --base-dir Pattern_Selection --variant Baseline --output-dir Pattern_Selection/Convergence
```

---

### A_02c - Pattern_Usage.py

**Purpose:** Cross-strategy comparison of pattern usage and Beifang-Analyse.

**Workflow:**
1. Scan Evaluation directory for all `{Strategy}/{Config}/predictions.csv`
2. Filter rows where prediction_type == 'pattern'
3. Group by pattern_hash per strategy, count occurrences
4. Build cross-strategy table with count column (1-6)
5. Load selected pattern counts from Pattern_Selection
6. Compare selected vs. used patterns (Beifang = selected - used)

**Inputs:**
- `evaluation_dir`: Path to Evaluation directory (positional)
- `--selection-dir`: Path to Pattern_Selection directory (required)

**Outputs:**
- `{output-dir}/A_02c_patterns.csv` - Cross-strategy usage table
  - Columns: pattern_hash;Frequency_Baseline;...;Error_Epsilon;count
- `{output-dir}/A_02c_summary.csv` - Beifang summary
  - Columns: strategy;selected;used;beifang

**Usage:**
```
python3 A_02c_Pattern_Usage.py Evaluation/ --selection-dir Pattern_Selection --output-dir Evaluation/PatternUsage
```

---

### A_03a - Feature_Frequency.py

**Purpose:** Analyze feature usage frequency across FFS results.

**Workflow:**
1. Load FFS overview (Operators or Patterns) from Hybrid_1
2. Strip operator prefixes from features (e.g., HashJoin_np -> np)
3. Count base feature occurrences
4. Export frequency ranking per target

**Inputs:**
- `ffs_overview`: Path to Hybrid_1 FFS overview CSV

**Outputs:** `{output-dir}/A_03a_feature_frequency_{target}.csv`
- Columns: feature;count

**Usage:**
```bash
# Patterns
python3 A_03a_Feature_Frequency.py ../../Hybrid_1/Runtime_Prediction/Baseline_SVM/SVM/Patterns/two_step_evaluation_overview.csv --output-dir Evaluation/Features/Patterns

# Operators
python3 A_03a_Feature_Frequency.py ../../Hybrid_1/Runtime_Prediction/Baseline_SVM/SVM/Operators/operator_overview.csv --output-dir Evaluation/Features/Operators
```

---

### A_03b - Pattern_Lookup.py

**Purpose:** Find all occurrences of a specific pattern (by hash) in a dataset.

**Workflow:**
1. Load pattern metadata from patterns.csv
2. Build tree for each query in dataset
3. Compute pattern hashes at pattern_length
4. Match against target hash, record occurrences

**Inputs:**
- `pattern_hash`: Pattern hash to search for (positional)
- `--patterns-file`: Path to patterns.csv (pattern metadata)
- `--dataset-file`: Path to operator dataset CSV (e.g., Test.csv)
- `--output-dir`: Output directory

**Outputs:**
- `A_03b_{short_hash}_summary.csv`: Pattern info + match count
- `A_03b_{short_hash}_matches.csv`: All query/node combinations where pattern occurs

**Usage:**
```bash
python3 A_03b_Pattern_Lookup.py 634cdbe24fda21720ccd3dc746d5c979 \
  --patterns-file ../Data_Generation/Training_Training/csv/01_patterns.csv \
  --dataset-file ../Dataset/Baseline/Test.csv \
  --output-dir Evaluation/PatternUsage
```

