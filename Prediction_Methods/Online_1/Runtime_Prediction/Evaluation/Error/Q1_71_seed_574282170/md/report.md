# Online Prediction Report

**Test Query:** Q1_71_seed_574282170
**Timestamp:** 2025-12-13 01:02:37

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 5.34%

## Phase C: Patterns in Query

- Total Patterns: 10

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 26.4017 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 19.6008 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 96 | 7.3257 |
| dc1b1da7 | Sort -> Aggregate -> Seq Scan (Outer) (O... | 3 | 24 | 5.2893 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 96 | 4.4662 |
| 715d5c92 | Gather Merge -> Sort -> Aggregate (Outer... | 3 | 48 | 4.3530 |
| 184f44de | Aggregate -> Seq Scan (Outer) | 2 | 48 | 4.0548 |
| f8231c4d | Aggregate -> Gather Merge -> Sort -> Agg... | 4 | 48 | 3.4083 |
| 52c5ec81 | Gather Merge -> Sort -> Aggregate -> Seq... | 4 | 24 | 3.1739 |
| 3dfa6025 | Aggregate -> Gather Merge -> Sort -> Agg... | 5 | 24 | 2.3734 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 1 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 3 | dc1b1da7 | 5.2893 | 0.0025% | REJECTED | 17.92% |
| 8 | 52c5ec81 | 3.1739 | 0.1045% | REJECTED | 17.92% |
## Query Tree

```
Node 591 (Aggregate) - ROOT
  Node 592 (Gather Merge)
    Node 593 (Sort)
      Node 594 (Aggregate)
        Node 595 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 5.51%
- Improvement: -0.17%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 591 | Aggregate | 997.05 | 1052.02 | 5.5% | operator |
| 592 | Gather Merge | 997.01 | 1079.37 | 8.3% | operator |
| 593 | Sort | 978.85 | 1152.43 | 17.7% | operator |
| 594 | Aggregate | 978.82 | 972.26 | 0.7% | operator |
| 595 | Seq Scan | 571.66 | 570.25 | 0.2% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 595 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=1184586
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=25
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1974
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=127603.0400
- **Output:** st=1.91, rt=570.25

### Step 2: Node 594 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=1184586
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=570.2522
  - rt2=0.0000
  - sel=0.0000
  - st1=1.9148
  - st2=0.0000
  - startup_cost=169063.5500
  - total_cost=169063.6800
- **Output:** st=951.35, rt=972.26

### Step 3: Node 593 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=6
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=972.2621
  - rt2=0.0000
  - sel=1.0000
  - st1=951.3542
  - st2=0.0000
  - startup_cost=169063.7600
  - total_cost=169063.7800
- **Output:** st=1150.45, rt=1152.43

### Step 4: Node 592 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=30
  - nt1=6
  - nt2=0
  - parallel_workers=5
  - plan_width=236
  - reltuples=0.0000
  - rt1=1152.4336
  - rt2=0.0000
  - sel=5.0000
  - st1=1150.4504
  - st2=0.0000
  - startup_cost=170063.8400
  - total_cost=170067.4700
- **Output:** st=1075.00, rt=1079.37

### Step 5: Node 591 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=30
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=1079.3653
  - rt2=0.0000
  - sel=0.2000
  - st1=1075.0001
  - st2=0.0000
  - startup_cost=170063.8400
  - total_cost=170068.6100
- **Output:** st=1039.49, rt=1052.02
