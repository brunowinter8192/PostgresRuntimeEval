# Runtime_Prediction

SVM-based runtime prediction at operator level with Two-Step Forward Feature Selection.

**Input:** Training dataset with per-operator CSVs from Datasets module

**Output:**
- Trained SVM models (per operator, per target)
- Query-level predictions on test set
- Evaluation metrics (MRE per template, per operator type)

**Key Outputs:**

| Output | Description |
|--------|-------------|
| `SVM/two_step_evaluation_overview.csv` | Feature selection results for all operator-target combinations |
| `Model/{target}/{operator}/model.pkl` | Trained SVM pipelines |
| `predictions.csv` | Bottom-up predictions on test set |
| `Evaluation/overall_mre.csv` | Aggregated query-level error |
| `Evaluation/template_mre.csv` | Per-template MRE statistics |

**Details:** See [DOCS.md](DOCS.md)
