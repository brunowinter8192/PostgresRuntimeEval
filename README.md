# PostgresRuntimeEval

ML-based runtime prediction for SQL queries on the TPC-H benchmark (Scale Factor 1) using PostgreSQL. Implements and evaluates multiple prediction methods at different granularities — from plan-level regression to operator-level and pattern-level hybrid approaches.

Based on: Akdere, Cetintemel, Upfal — *"Learning-based Query Performance Modeling and Prediction"* (Brown University, 2012)

## Directory Structure

```
PostgresRuntimeEval/
    plot_config.py                           Centralized plot styling
    README.md
    Misc/                                    [See DOCS.md](Misc/DOCS.md)
    Prediction_Methods/
        Plan_Level_1/                        [See README.md](Prediction_Methods/Plan_Level_1/README.md)
        Operator_Level/                      [See README.md](Prediction_Methods/Operator_Level/README.md)
        Hybrid_1/                            [See README.md](Prediction_Methods/Hybrid_1/README.md)
        Hybrid_2/                            [See README.md](Prediction_Methods/Hybrid_2/README.md)
        Online_1/                            [See README.md](Prediction_Methods/Online_1/README.md)
        Dynamic/                             [See README.md](Prediction_Methods/Dynamic/README.md)
```

## Prediction Methods

Two workload types are evaluated:

- **Static:** Train and test sets share the same templates (120 train / 30 test per template)
- **Dynamic (LOTO):** Leave-One-Template-Out cross-validation — the test template is entirely unseen during training

| Method | Granularity | Workload | Description |
|--------|-------------|----------|-------------|
| Plan_Level_1 | Query/Plan | Static | Direct prediction from aggregated plan features |
| Operator_Level | Operator | Static | Per-operator SVM models, bottom-up aggregation |
| Hybrid_1 | Pattern | Static | Pattern-level models (parent + children) with operator fallback |
| Hybrid_2 | Pattern | Static | Greedy pattern selection with operator fallback |
| Online_1 | Pattern | Static | Online pattern mining and selection at query time |
| Dynamic | All above | LOTO | LOTO cross-validation for Plan, Operator, Hybrid_1, Online_1 |

### Plan_Level_1

Direct query runtime prediction from aggregated plan-level features (row counts, cost estimates, structural metrics). Uses forward feature selection and SVM regression.

**Details:** [Prediction_Methods/Plan_Level_1/README.md](Prediction_Methods/Plan_Level_1/README.md)

### Operator_Level

Predicts runtime for each operator individually using per-type SVM models (13 operator types × 2 targets). Query runtime is reconstructed via bottom-up aggregation through the plan tree.

**Details:** [Prediction_Methods/Operator_Level/README.md](Prediction_Methods/Operator_Level/README.md)

### Hybrid_1

Groups parent operators with their children into patterns (e.g., Hash Join + Seq Scan + Hash). Trains pattern-level SVM models; unmatched operators fall back to operator-level models.

**Details:** [Prediction_Methods/Hybrid_1/README.md](Prediction_Methods/Hybrid_1/README.md)

### Hybrid_2

Extends Hybrid_1 with greedy pattern selection — iteratively picks patterns that maximize prediction improvement over the operator-level baseline.

**Details:** [Prediction_Methods/Hybrid_2/README.md](Prediction_Methods/Hybrid_2/README.md)

### Online_1

Online variant where patterns are mined and selected at query time rather than precomputed. Greedy selection per test query with configurable ranking strategies.

**Details:** [Prediction_Methods/Online_1/README.md](Prediction_Methods/Online_1/README.md)

### Dynamic

LOTO cross-validation wrapper that runs Plan_Level, Operator_Level, Hybrid_1, and Online_1 workflows across 14 template folds.

**Details:** [Prediction_Methods/Dynamic/README.md](Prediction_Methods/Dynamic/README.md)

## Misc

Setup (including modified TPC-H dbgen V3.0.1), query generation, cache validation, SVM parameter comparison, and passthrough operator analysis.

**Details:** [Misc/DOCS.md](Misc/DOCS.md)

## Base Paper

Akdere, M., Çetintemel, U., Upfal, E. (2012). *Learning-based Query Performance Modeling and Prediction.* IEEE 28th International Conference on Data Engineering (ICDE).
