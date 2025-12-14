# Online Prediction Report

**Test Query:** Q4_39_seed_311753178
**Timestamp:** 2025-12-13 02:45:11

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 3.32%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 26.4017 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 19.6008 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 96 | 7.3257 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 141.6847 |
| 3b447875 | Aggregate -> Nested Loop (Outer) | 2 | 44 | 3.5717 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 96 | 4.4662 |
| 715d5c92 | Gather Merge -> Sort -> Aggregate (Outer... | 3 | 48 | 4.3530 |
| f86f2b1b | Sort -> Aggregate -> Nested Loop (Outer)... | 3 | 24 | 0.5091 |
| 3f1648ef | Aggregate -> Nested Loop -> [Seq Scan (O... | 3 | 24 | 3.0380 |
| f8231c4d | Aggregate -> Gather Merge -> Sort -> Agg... | 4 | 48 | 3.4083 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 1 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 3 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.92% |
| 8 | 3f1648ef | 3.0380 | 0.0002% | REJECTED | 17.92% |
## Query Tree

```
Node 6425 (Aggregate) - ROOT
  Node 6426 (Gather Merge)
    Node 6427 (Sort)
      Node 6428 (Aggregate)
        Node 6429 (Nested Loop)
          Node 6430 (Seq Scan) - LEAF
          Node 6431 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 2.89%
- Improvement: 0.42%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 6425 | Aggregate | 1052.97 | 1022.50 | 2.9% | operator |
| 6426 | Gather Merge | 1052.97 | 1112.88 | 5.7% | operator |
| 6427 | Sort | 1048.71 | 1061.19 | 1.2% | operator |
| 6428 | Aggregate | 1048.70 | 923.46 | 11.9% | operator |
| 6429 | Nested Loop | 1046.81 | 1106.37 | 5.7% | operator |
| 6430 | Seq Scan | 160.65 | 157.03 | 2.3% | operator |
| 6431 | Index Scan | 0.06 | 0.38 | 513.6% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 6430 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=17822
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

### Step 2: Node 6431 (Index Scan) - LEAF

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

### Step 3: Node 6429 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14533
  - nt1=17822
  - nt2=2
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=157.0315
  - rt2=0.3804
  - sel=0.4077
  - st1=0.2256
  - st2=0.0614
  - startup_cost=0.4300
  - total_cost=65470.4400
- **Output:** st=31.32, rt=1106.37

### Step 4: Node 6428 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=14533
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=1106.3740
  - rt2=0.0000
  - sel=0.0003
  - st1=31.3207
  - st2=0.0000
  - startup_cost=65543.1100
  - total_cost=65543.1600
- **Output:** st=912.33, rt=923.46

### Step 5: Node 6427 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=5
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=923.4634
  - rt2=0.0000
  - sel=1.0000
  - st1=912.3318
  - st2=0.0000
  - startup_cost=65543.2100
  - total_cost=65543.2300
- **Output:** st=1059.87, rt=1061.19

### Step 6: Node 6426 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15
  - nt1=5
  - nt2=0
  - parallel_workers=3
  - plan_width=24
  - reltuples=0.0000
  - rt1=1061.1867
  - rt2=0.0000
  - sel=3.0000
  - st1=1059.8739
  - st2=0.0000
  - startup_cost=66543.2500
  - total_cost=66545.0300
- **Output:** st=1109.63, rt=1112.88

### Step 7: Node 6425 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=15
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=1112.8773
  - rt2=0.0000
  - sel=0.3333
  - st1=1109.6341
  - st2=0.0000
  - startup_cost=66543.2500
  - total_cost=66545.1500
- **Output:** st=1025.30, rt=1022.50
