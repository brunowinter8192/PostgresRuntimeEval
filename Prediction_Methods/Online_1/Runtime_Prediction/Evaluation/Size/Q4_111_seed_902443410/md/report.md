# Online Prediction Report

**Test Query:** Q4_111_seed_902443410
**Timestamp:** 2025-12-13 02:44:06

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 3.73%

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
Node 5935 (Aggregate) - ROOT
  Node 5936 (Gather Merge)
    Node 5937 (Sort)
      Node 5938 (Aggregate)
        Node 5939 (Nested Loop)
          Node 5940 (Seq Scan) - LEAF
          Node 5941 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 3.31%
- Improvement: 0.42%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 5935 | Aggregate | 1057.16 | 1022.12 | 3.3% | operator |
| 5936 | Gather Merge | 1057.15 | 1112.80 | 5.3% | operator |
| 5937 | Sort | 1052.36 | 1061.21 | 0.8% | operator |
| 5938 | Aggregate | 1052.35 | 922.99 | 12.3% | operator |
| 5939 | Nested Loop | 1050.37 | 1106.78 | 5.4% | operator |
| 5940 | Seq Scan | 165.67 | 157.02 | 5.2% | operator |
| 5941 | Index Scan | 0.06 | 0.38 | 513.6% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 5940 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=18533
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=20
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0124
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=33394.0600
- **Output:** st=0.23, rt=157.02

### Step 2: Node 5941 (Index Scan) - LEAF

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
  - total_cost=2.2800
- **Output:** st=0.06, rt=0.38

### Step 3: Node 5939 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15113
  - nt1=18533
  - nt2=2
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=157.0227
  - rt2=0.3804
  - sel=0.4077
  - st1=0.2261
  - st2=0.0614
  - startup_cost=0.4300
  - total_cost=66037.5800
- **Output:** st=31.56, rt=1106.78

### Step 4: Node 5938 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=15113
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=1106.7771
  - rt2=0.0000
  - sel=0.0003
  - st1=31.5569
  - st2=0.0000
  - startup_cost=66113.1500
  - total_cost=66113.2000
- **Output:** st=911.92, rt=922.99

### Step 5: Node 5937 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=5
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=922.9918
  - rt2=0.0000
  - sel=1.0000
  - st1=911.9175
  - st2=0.0000
  - startup_cost=66113.2600
  - total_cost=66113.2700
- **Output:** st=1059.89, rt=1061.21

### Step 6: Node 5936 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15
  - nt1=5
  - nt2=0
  - parallel_workers=3
  - plan_width=24
  - reltuples=0.0000
  - rt1=1061.2054
  - rt2=0.0000
  - sel=3.0000
  - st1=1059.8908
  - st2=0.0000
  - startup_cost=67113.3000
  - total_cost=67115.0700
- **Output:** st=1109.56, rt=1112.80

### Step 7: Node 5935 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=15
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=1112.8013
  - rt2=0.0000
  - sel=0.3333
  - st1=1109.5560
  - st2=0.0000
  - startup_cost=67113.3000
  - total_cost=67115.2000
- **Output:** st=1024.98, rt=1022.12
