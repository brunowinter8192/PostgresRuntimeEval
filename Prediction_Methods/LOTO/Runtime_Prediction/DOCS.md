# Runtime_Prediction - DOCS

## Directory Structure

```
Runtime_Prediction/
├── DOCS.md
├── A_01_Evaluate_Template.py
├── A_02_Compare_Templates.py
├── Online_1/                    [See DOCS.md]
├── Operator_Level/              [See DOCS.md]
└── Plan_Level/                  [See DOCS.md]
```

---

## A_01_Evaluate_Template.py

**Purpose:** Calculate evaluation metrics for each template based on prediction results

**Input:** `Evaluation/` directory containing template subfolders with `predictions.csv`

**Output:** `metrics.csv` per template folder

**Usage:**
```bash
python3 A_01_Evaluate_Template.py <evaluation_dir>
```

### evaluate_workflow()
Orchestrator that iterates through all template folders in the evaluation directory and calls evaluate_template for each.

### evaluate_template()
Processes a single template folder: loads predictions, calculates metrics, exports results. Skips if predictions.csv does not exist.

### load_predictions()
Loads predictions.csv from a template folder using semicolon delimiter.

### calculate_metrics()
Calculates evaluation metrics from predictions DataFrame: query_count, mean_actual_ms, mean_predicted_ms, mean_mre, std_mre, mean_mre_pct.

### export_metrics()
Exports metrics dictionary to metrics.csv in the template folder.

---

## A_02_Compare_Templates.py

**Purpose:** Aggregate metrics across all templates and create comparison visualization

**Input:** `Evaluation/` directory containing template subfolders with `metrics.csv` (requires A_01 output)

**Output:** `comparison.csv` and `comparison_plot.png` in evaluation directory root

**Usage:**
```bash
python3 A_02_Compare_Templates.py <evaluation_dir> [--title "Plot Title"]
```

### compare_workflow()
Orchestrator that collects metrics from all templates, creates comparison table, exports CSV and generates plot.

### collect_all_metrics()
Iterates through template folders, reads metrics.csv from each, returns list of metric dictionaries with template name added.

### create_comparison_table()
Converts collected metrics list to DataFrame, sets template as index, sorts alphabetically.

### export_comparison()
Saves comparison DataFrame to comparison.csv in evaluation directory root.

### create_comparison_plot()
Generates bar plot showing mean_mre_pct per template with value labels. Saves as comparison_plot.png.
