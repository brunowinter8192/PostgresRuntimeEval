# Online Prediction Report

**Test Query:** Q4_62_seed_500445891
**Timestamp:** 2025-12-13 03:53:56

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 2.73%

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
Node 6607 (Aggregate) - ROOT
  Node 6608 (Gather Merge)
    Node 6609 (Sort)
      Node 6610 (Aggregate)
        Node 6611 (Nested Loop)
          Node 6612 (Seq Scan) - LEAF
          Node 6613 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 2.31%
- Improvement: 0.42%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 6607 | Aggregate | 1046.62 | 1022.48 | 2.3% | operator |
| 6608 | Gather Merge | 1046.61 | 1112.87 | 6.3% | operator |
| 6609 | Sort | 1041.31 | 1061.19 | 1.9% | operator |
| 6610 | Aggregate | 1041.29 | 923.44 | 11.3% | operator |
| 6611 | Nested Loop | 1039.40 | 1106.39 | 6.4% | operator |
| 6612 | Seq Scan | 164.97 | 157.03 | 4.8% | operator |
| 6613 | Index Scan | 0.06 | 0.38 | 513.6% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 6612 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=17856
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=20
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0119
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=33394.0600
- **Output:** st=0.23, rt=157.03

### Step 2: Node 6613 (Index Scan) - LEAF

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
  - total_cost=2.3400
- **Output:** st=0.06, rt=0.38

### Step 3: Node 6611 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14561
  - nt1=17856
  - nt2=2
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=157.0311
  - rt2=0.3804
  - sel=0.4077
  - st1=0.2256
  - st2=0.0614
  - startup_cost=0.4300
  - total_cost=65497.8000
- **Output:** st=31.33, rt=1106.39

### Step 4: Node 6610 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=14561
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=1106.3928
  - rt2=0.0000
  - sel=0.0003
  - st1=31.3315
  - st2=0.0000
  - startup_cost=65570.6000
  - total_cost=65570.6500
- **Output:** st=912.31, rt=923.44

### Step 5: Node 6609 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=5
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=923.4406
  - rt2=0.0000
  - sel=1.0000
  - st1=912.3118
  - st2=0.0000
  - startup_cost=65570.7100
  - total_cost=65570.7200
- **Output:** st=1059.87, rt=1061.19

### Step 6: Node 6608 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15
  - nt1=5
  - nt2=0
  - parallel_workers=3
  - plan_width=24
  - reltuples=0.0000
  - rt1=1061.1876
  - rt2=0.0000
  - sel=3.0000
  - st1=1059.8747
  - st2=0.0000
  - startup_cost=66570.7500
  - total_cost=66572.5300
- **Output:** st=1109.63, rt=1112.87

### Step 7: Node 6607 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=15
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=1112.8736
  - rt2=0.0000
  - sel=0.3333
  - st1=1109.6304
  - st2=0.0000
  - startup_cost=66570.7500
  - total_cost=66572.6500
- **Output:** st=1025.29, rt=1022.48
