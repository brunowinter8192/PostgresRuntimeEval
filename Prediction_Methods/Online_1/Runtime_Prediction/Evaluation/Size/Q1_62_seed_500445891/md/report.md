# Online Prediction Report

**Test Query:** Q1_62_seed_500445891
**Timestamp:** 2025-12-13 02:20:33

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 5.47%

## Phase C: Patterns in Query

- Total Patterns: 10

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 26.4017 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 19.6008 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 96 | 7.3257 |
| 184f44de | Aggregate -> Seq Scan (Outer) | 2 | 48 | 4.0548 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 96 | 4.4662 |
| 715d5c92 | Gather Merge -> Sort -> Aggregate (Outer... | 3 | 48 | 4.3530 |
| dc1b1da7 | Sort -> Aggregate -> Seq Scan (Outer) (O... | 3 | 24 | 5.2893 |
| f8231c4d | Aggregate -> Gather Merge -> Sort -> Agg... | 4 | 48 | 3.4083 |
| 52c5ec81 | Gather Merge -> Sort -> Aggregate -> Seq... | 4 | 24 | 3.1739 |
| 3dfa6025 | Aggregate -> Gather Merge -> Sort -> Agg... | 5 | 24 | 2.3734 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 1 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 6 | dc1b1da7 | 5.2893 | 0.0025% | REJECTED | 17.92% |
| 8 | 52c5ec81 | 3.1739 | 0.1045% | REJECTED | 17.92% |
## Query Tree

```
Node 541 (Aggregate) - ROOT
  Node 542 (Gather Merge)
    Node 543 (Sort)
      Node 544 (Aggregate)
        Node 545 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 5.65%
- Improvement: -0.17%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 541 | Aggregate | 995.78 | 1052.01 | 5.6% | operator |
| 542 | Gather Merge | 995.74 | 1079.37 | 8.4% | operator |
| 543 | Sort | 979.25 | 1152.41 | 17.7% | operator |
| 544 | Aggregate | 979.23 | 972.17 | 0.7% | operator |
| 545 | Seq Scan | 575.90 | 571.16 | 0.8% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 545 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=1180767
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=25
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1968
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=127603.0400
- **Output:** st=1.92, rt=571.16

### Step 2: Node 544 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=1180767
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=571.1627
  - rt2=0.0000
  - sel=0.0000
  - st1=1.9221
  - st2=0.0000
  - startup_cost=168929.8800
  - total_cost=168930.0200
- **Output:** st=951.34, rt=972.17

### Step 3: Node 543 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=6
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=972.1665
  - rt2=0.0000
  - sel=1.0000
  - st1=951.3430
  - st2=0.0000
  - startup_cost=168930.1000
  - total_cost=168930.1100
- **Output:** st=1150.43, rt=1152.41

### Step 4: Node 542 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=30
  - nt1=6
  - nt2=0
  - parallel_workers=5
  - plan_width=236
  - reltuples=0.0000
  - rt1=1152.4105
  - rt2=0.0000
  - sel=5.0000
  - st1=1150.4278
  - st2=0.0000
  - startup_cost=169930.1700
  - total_cost=169933.8000
- **Output:** st=1075.01, rt=1079.37

### Step 5: Node 541 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=30
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=1079.3715
  - rt2=0.0000
  - sel=0.2000
  - st1=1075.0066
  - st2=0.0000
  - startup_cost=169930.1700
  - total_cost=169934.9400
- **Output:** st=1039.51, rt=1052.01
