# Online Prediction Report

**Test Query:** Q1_35_seed_278937054
**Timestamp:** 2025-12-13 03:29:20

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 10.94%

## Phase C: Patterns in Query

- Total Patterns: 10

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 26.4017 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 19.6008 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 96 | 7.3257 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 96 | 4.4662 |
| 184f44de | Aggregate -> Seq Scan (Outer) | 2 | 48 | 4.0548 |
| 715d5c92 | Gather Merge -> Sort -> Aggregate (Outer... | 3 | 48 | 4.3530 |
| f8231c4d | Aggregate -> Gather Merge -> Sort -> Agg... | 4 | 48 | 3.4083 |
| dc1b1da7 | Sort -> Aggregate -> Seq Scan (Outer) (O... | 3 | 24 | 5.2893 |
| 52c5ec81 | Gather Merge -> Sort -> Aggregate -> Seq... | 4 | 24 | 3.1739 |
| 3dfa6025 | Aggregate -> Gather Merge -> Sort -> Agg... | 5 | 24 | 2.3734 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 1 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 7 | dc1b1da7 | 5.2893 | 0.0025% | REJECTED | 17.92% |
| 8 | 52c5ec81 | 3.1739 | 0.1045% | REJECTED | 17.92% |
## Query Tree

```
Node 391 (Aggregate) - ROOT
  Node 392 (Gather Merge)
    Node 393 (Sort)
      Node 394 (Aggregate)
        Node 395 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 11.12%
- Improvement: -0.18%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 391 | Aggregate | 946.72 | 1052.02 | 11.1% | operator |
| 392 | Gather Merge | 946.66 | 1079.35 | 14.0% | operator |
| 393 | Sort | 926.94 | 1152.47 | 24.3% | operator |
| 394 | Aggregate | 926.91 | 972.43 | 4.9% | operator |
| 395 | Seq Scan | 498.02 | 568.71 | 14.2% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 395 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=1191078
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=25
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1985
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=127603.0400
- **Output:** st=1.90, rt=568.71

### Step 2: Node 394 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=1191078
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=568.7055
  - rt2=0.0000
  - sel=0.0000
  - st1=1.9022
  - st2=0.0000
  - startup_cost=169290.7700
  - total_cost=169290.9000
- **Output:** st=951.37, rt=972.43

### Step 3: Node 393 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=6
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=972.4261
  - rt2=0.0000
  - sel=1.0000
  - st1=951.3739
  - st2=0.0000
  - startup_cost=169290.9800
  - total_cost=169291.0000
- **Output:** st=1150.49, rt=1152.47

### Step 4: Node 392 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=30
  - nt1=6
  - nt2=0
  - parallel_workers=5
  - plan_width=236
  - reltuples=0.0000
  - rt1=1152.4730
  - rt2=0.0000
  - sel=5.0000
  - st1=1150.4889
  - st2=0.0000
  - startup_cost=170291.0600
  - total_cost=170294.6900
- **Output:** st=1074.99, rt=1079.35

### Step 5: Node 391 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=30
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=1079.3549
  - rt2=0.0000
  - sel=0.2000
  - st1=1074.9891
  - st2=0.0000
  - startup_cost=170291.0600
  - total_cost=170295.8300
- **Output:** st=1039.45, rt=1052.02
