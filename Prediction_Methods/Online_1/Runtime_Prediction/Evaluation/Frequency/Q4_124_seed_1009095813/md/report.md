# Online Prediction Report

**Test Query:** Q4_124_seed_1009095813
**Timestamp:** 2025-12-13 03:52:51

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 3.37%

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
Node 6033 (Aggregate) - ROOT
  Node 6034 (Gather Merge)
    Node 6035 (Sort)
      Node 6036 (Aggregate)
        Node 6037 (Nested Loop)
          Node 6038 (Seq Scan) - LEAF
          Node 6039 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 2.95%
- Improvement: 0.42%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 6033 | Aggregate | 1053.25 | 1022.15 | 3.0% | operator |
| 6034 | Gather Merge | 1053.24 | 1112.81 | 5.7% | operator |
| 6035 | Sort | 1048.73 | 1061.20 | 1.2% | operator |
| 6036 | Aggregate | 1048.71 | 923.03 | 12.0% | operator |
| 6037 | Nested Loop | 1046.86 | 1106.75 | 5.7% | operator |
| 6038 | Seq Scan | 165.13 | 157.02 | 4.9% | operator |
| 6039 | Index Scan | 0.06 | 0.38 | 523.7% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 6038 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=18478
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=20
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0123
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=33394.0600
- **Output:** st=0.23, rt=157.02

### Step 2: Node 6039 (Index Scan) - LEAF

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
  - total_cost=2.2900
- **Output:** st=0.06, rt=0.38

### Step 3: Node 6037 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15068
  - nt1=18478
  - nt2=2
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=157.0233
  - rt2=0.3804
  - sel=0.4077
  - st1=0.2261
  - st2=0.0614
  - startup_cost=0.4300
  - total_cost=65993.2000
- **Output:** st=31.54, rt=1106.75

### Step 4: Node 6036 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=15068
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=1106.7459
  - rt2=0.0000
  - sel=0.0003
  - st1=31.5385
  - st2=0.0000
  - startup_cost=66068.5400
  - total_cost=66068.5900
- **Output:** st=911.95, rt=923.03

### Step 5: Node 6035 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=5
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=923.0287
  - rt2=0.0000
  - sel=1.0000
  - st1=911.9499
  - st2=0.0000
  - startup_cost=66068.6500
  - total_cost=66068.6600
- **Output:** st=1059.89, rt=1061.20

### Step 6: Node 6034 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15
  - nt1=5
  - nt2=0
  - parallel_workers=3
  - plan_width=24
  - reltuples=0.0000
  - rt1=1061.2039
  - rt2=0.0000
  - sel=3.0000
  - st1=1059.8894
  - st2=0.0000
  - startup_cost=67068.6900
  - total_cost=67070.4600
- **Output:** st=1109.56, rt=1112.81

### Step 7: Node 6033 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=15
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=1112.8072
  - rt2=0.0000
  - sel=0.3333
  - st1=1109.5621
  - st2=0.0000
  - startup_cost=67068.6900
  - total_cost=67070.5900
- **Output:** st=1025.01, rt=1022.15
