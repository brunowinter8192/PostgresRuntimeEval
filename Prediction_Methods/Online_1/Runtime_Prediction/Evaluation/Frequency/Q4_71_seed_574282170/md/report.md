# Online Prediction Report

**Test Query:** Q4_71_seed_574282170
**Timestamp:** 2025-12-13 03:53:56

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 5.20%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 26.4017 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 19.6008 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 96 | 7.3257 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 141.6847 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 96 | 4.4662 |
| 715d5c92 | Gather Merge -> Sort -> Aggregate (Outer... | 3 | 48 | 4.3530 |
| f8231c4d | Aggregate -> Gather Merge -> Sort -> Agg... | 4 | 48 | 3.4083 |
| 3b447875 | Aggregate -> Nested Loop (Outer) | 2 | 44 | 3.5717 |
| f86f2b1b | Sort -> Aggregate -> Nested Loop (Outer)... | 3 | 24 | 0.5091 |
| 3f1648ef | Aggregate -> Nested Loop -> [Seq Scan (O... | 3 | 24 | 3.0380 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 1 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 3 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.92% |
| 9 | 3f1648ef | 3.0380 | 0.0002% | REJECTED | 17.92% |
## Query Tree

```
Node 6677 (Aggregate) - ROOT
  Node 6678 (Gather Merge)
    Node 6679 (Sort)
      Node 6680 (Aggregate)
        Node 6681 (Nested Loop)
          Node 6682 (Seq Scan) - LEAF
          Node 6683 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 4.79%
- Improvement: 0.41%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 6677 | Aggregate | 1073.88 | 1022.43 | 4.8% | operator |
| 6678 | Gather Merge | 1073.88 | 1112.86 | 3.6% | operator |
| 6679 | Sort | 1069.30 | 1061.19 | 0.8% | operator |
| 6680 | Aggregate | 1069.28 | 923.38 | 13.6% | operator |
| 6681 | Nested Loop | 1067.34 | 1106.44 | 3.7% | operator |
| 6682 | Seq Scan | 168.39 | 157.03 | 6.7% | operator |
| 6683 | Index Scan | 0.06 | 0.38 | 494.4% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 6682 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=17945
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=20
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0120
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=33394.0600
- **Output:** st=0.23, rt=157.03

### Step 2: Node 6683 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=2
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.4300
  - total_cost=2.3300
- **Output:** st=0.06, rt=0.38

### Step 3: Node 6681 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14634
  - nt1=17945
  - nt2=2
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=157.0300
  - rt2=0.3804
  - sel=0.4077
  - st1=0.2257
  - st2=0.0614
  - startup_cost=0.4300
  - total_cost=65569.1600
- **Output:** st=31.36, rt=1106.44

### Step 4: Node 6680 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=14634
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=1106.4423
  - rt2=0.0000
  - sel=0.0003
  - st1=31.3600
  - st2=0.0000
  - startup_cost=65642.3300
  - total_cost=65642.3800
- **Output:** st=912.26, rt=923.38

### Step 5: Node 6679 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=5
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=923.3810
  - rt2=0.0000
  - sel=1.0000
  - st1=912.2595
  - st2=0.0000
  - startup_cost=65642.4400
  - total_cost=65642.4500
- **Output:** st=1059.88, rt=1061.19

### Step 6: Node 6678 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15
  - nt1=5
  - nt2=0
  - parallel_workers=3
  - plan_width=24
  - reltuples=0.0000
  - rt1=1061.1899
  - rt2=0.0000
  - sel=3.0000
  - st1=1059.8768
  - st2=0.0000
  - startup_cost=66642.4800
  - total_cost=66644.2500
- **Output:** st=1109.62, rt=1112.86

### Step 7: Node 6677 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=15
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=1112.8640
  - rt2=0.0000
  - sel=0.3333
  - st1=1109.6205
  - st2=0.0000
  - startup_cost=66642.4800
  - total_cost=66644.3800
- **Output:** st=1025.25, rt=1022.43
