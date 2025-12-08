# Online_2 - Online Pattern Selection

Online pattern-level prediction based on Section 4 of the base paper. Builds pattern models at query-time instead of using pre-selected patterns from offline training.

## Approach

**Offline (Hybrid_7):** Select patterns once on training data, use fixed set for all predictions

**Online (this):** For each test query, evaluate which patterns improve prediction on training data, then apply selected patterns to that query

## Key Difference to Offline

- Hybrid_7: Uses `selected_patterns.csv` as fixed whitelist
- Online_2: Evaluates every pattern of the incoming query against training data
  - Can discover patterns that offline strategy would have rejected
  - Pattern acceptance based on EPSILON threshold per query

## Dataset

**No local Dataset folder.** References Hybrid_7 baseline data directly.

**Training Data:** `../Hybrid_7/Dataset/Baseline/Training.csv`
- 19538 operators from 80% of queries
- Used for: Operator model training, pattern model training, online pattern evaluation

**Test Data:** `../Hybrid_7/Dataset/Baseline/Test.csv`
- 4781 operators from 20% of queries
- Used for: Final prediction evaluation

**Schema:** See Hybrid_7/Dataset/DOCS.md for column definitions.

## Parameters (from Hybrid_7 convergence analysis)

| Parameter | Value | Description |
|-----------|-------|-------------|
| EPSILON | 0.0001 (0.01%) | Minimum improvement to accept pattern |
| TARGET_MRE | 0.10 (10%) | Early-stop when MRE falls below |
| Strategy | Error-based | Order patterns by frequency x avg_error DESC |

## Workflow Overview

```
Phase 1: Preparation (one-time, from Hybrid_7)
- Operator models trained on Training.csv
- Pattern occurrence counts from Training.csv
- Error scores per pattern from Training.csv

Phase 2: Online Prediction (per test query)
01_Online_Prediction.py
  - Extract patterns from test query
  - Filter: only patterns with min_occurrence in training
  - Order by error-score (from Phase 1)
  - For each pattern:
    - Evaluate MRE improvement on training
    - Accept if delta > EPSILON
    - Stop early if MRE < TARGET_MRE
  - Predict query with accepted patterns

Phase 3: Evaluation
A_01a_Evaluation.py
  - Compare online vs offline pattern selection
  - Measure: MRE, selected patterns per query, runtime
```

## Directory Structure

```
Online_2/
    mapping_config.py
    README.md                        (THIS FILE)
    DESIGN.md                        Design rationale and decisions
    Runtime_Prediction/              [See DOCS.md]
        01_Online_Prediction.py
        A_01a_Evaluation.py
        csv/
```

## References

- Base Paper Section 4: Online Model Building
- Hybrid_7: Offline pattern selection baseline
- DESIGN.md: Detailed design decisions
