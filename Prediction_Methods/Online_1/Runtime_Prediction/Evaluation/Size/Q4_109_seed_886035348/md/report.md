# Online Prediction Report

**Test Query:** Q4_109_seed_886035348
**Timestamp:** 2025-12-13 02:44:06

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 3.64%

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
Node 5914 (Aggregate) - ROOT
  Node 5915 (Gather Merge)
    Node 5916 (Sort)
      Node 5917 (Aggregate)
        Node 5918 (Nested Loop)
          Node 5919 (Seq Scan) - LEAF
          Node 5920 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 3.22%
- Improvement: 0.42%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 5914 | Aggregate | 1056.09 | 1022.06 | 3.2% | operator |
| 5915 | Gather Merge | 1056.09 | 1112.79 | 5.4% | operator |
| 5916 | Sort | 1050.06 | 1061.21 | 1.1% | operator |
| 5917 | Aggregate | 1050.04 | 922.91 | 12.1% | operator |
| 5918 | Nested Loop | 1048.08 | 1106.85 | 5.6% | operator |
| 5919 | Seq Scan | 162.25 | 157.02 | 3.2% | operator |
| 5920 | Index Scan | 0.06 | 0.38 | 513.6% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 5919 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=18655
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

### Step 2: Node 5920 (Index Scan) - LEAF

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
  - total_cost=2.2700
- **Output:** st=0.06, rt=0.38

### Step 3: Node 5918 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15213
  - nt1=18655
  - nt2=2
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=157.0211
  - rt2=0.3804
  - sel=0.4077
  - st1=0.2262
  - st2=0.0614
  - startup_cost=0.4300
  - total_cost=66134.2800
- **Output:** st=31.60, rt=1106.85

### Step 4: Node 5917 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=15213
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=1106.8468
  - rt2=0.0000
  - sel=0.0003
  - st1=31.5981
  - st2=0.0000
  - startup_cost=66210.3400
  - total_cost=66210.3900
- **Output:** st=911.85, rt=922.91

### Step 5: Node 5916 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=5
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=922.9117
  - rt2=0.0000
  - sel=1.0000
  - st1=911.8471
  - st2=0.0000
  - startup_cost=66210.4500
  - total_cost=66210.4600
- **Output:** st=1059.89, rt=1061.21

### Step 6: Node 5915 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15
  - nt1=5
  - nt2=0
  - parallel_workers=3
  - plan_width=24
  - reltuples=0.0000
  - rt1=1061.2086
  - rt2=0.0000
  - sel=3.0000
  - st1=1059.8937
  - st2=0.0000
  - startup_cost=67210.4900
  - total_cost=67212.2600
- **Output:** st=1109.54, rt=1112.79

### Step 7: Node 5914 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=15
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=1112.7884
  - rt2=0.0000
  - sel=0.3333
  - st1=1109.5427
  - st2=0.0000
  - startup_cost=67210.4900
  - total_cost=67212.3900
- **Output:** st=1024.93, rt=1022.06
