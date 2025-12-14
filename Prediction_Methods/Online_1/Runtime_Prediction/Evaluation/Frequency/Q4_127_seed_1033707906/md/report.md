# Online Prediction Report

**Test Query:** Q4_127_seed_1033707906
**Timestamp:** 2025-12-13 03:52:51

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 3.33%

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
Node 6054 (Aggregate) - ROOT
  Node 6055 (Gather Merge)
    Node 6056 (Sort)
      Node 6057 (Aggregate)
        Node 6058 (Nested Loop)
          Node 6059 (Seq Scan) - LEAF
          Node 6060 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 2.91%
- Improvement: 0.42%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 6054 | Aggregate | 1052.89 | 1022.21 | 2.9% | operator |
| 6055 | Gather Merge | 1052.88 | 1112.82 | 5.7% | operator |
| 6056 | Sort | 1048.20 | 1061.20 | 1.2% | operator |
| 6057 | Aggregate | 1048.18 | 923.10 | 11.9% | operator |
| 6058 | Nested Loop | 1046.21 | 1106.68 | 5.8% | operator |
| 6059 | Seq Scan | 163.28 | 157.02 | 3.8% | operator |
| 6060 | Index Scan | 0.06 | 0.38 | 513.6% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 6059 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=18371
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=20
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0122
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=33394.0600
- **Output:** st=0.23, rt=157.02

### Step 2: Node 6060 (Index Scan) - LEAF

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
  - total_cost=2.3000
- **Output:** st=0.06, rt=0.38

### Step 3: Node 6058 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14981
  - nt1=18371
  - nt2=2
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=157.0247
  - rt2=0.3804
  - sel=0.4077
  - st1=0.2260
  - st2=0.0614
  - startup_cost=0.4300
  - total_cost=65908.6900
- **Output:** st=31.50, rt=1106.68

### Step 4: Node 6057 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=14981
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=1106.6844
  - rt2=0.0000
  - sel=0.0003
  - st1=31.5021
  - st2=0.0000
  - startup_cost=65983.5900
  - total_cost=65983.6400
- **Output:** st=912.01, rt=923.10

### Step 5: Node 6056 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=5
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=923.0987
  - rt2=0.0000
  - sel=1.0000
  - st1=912.0115
  - st2=0.0000
  - startup_cost=65983.7000
  - total_cost=65983.7100
- **Output:** st=1059.89, rt=1061.20

### Step 6: Node 6055 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15
  - nt1=5
  - nt2=0
  - parallel_workers=3
  - plan_width=24
  - reltuples=0.0000
  - rt1=1061.2011
  - rt2=0.0000
  - sel=3.0000
  - st1=1059.8869
  - st2=0.0000
  - startup_cost=66983.7400
  - total_cost=66985.5200
- **Output:** st=1109.57, rt=1112.82

### Step 7: Node 6054 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=15
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=1112.8185
  - rt2=0.0000
  - sel=0.3333
  - st1=1109.5737
  - st2=0.0000
  - startup_cost=66983.7400
  - total_cost=66985.6400
- **Output:** st=1025.06, rt=1022.21
