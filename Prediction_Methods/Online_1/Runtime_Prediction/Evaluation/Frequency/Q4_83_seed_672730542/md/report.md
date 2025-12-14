# Online Prediction Report

**Test Query:** Q4_83_seed_672730542
**Timestamp:** 2025-12-13 03:53:56

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 4.17%

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
Node 6768 (Aggregate) - ROOT
  Node 6769 (Gather Merge)
    Node 6770 (Sort)
      Node 6771 (Aggregate)
        Node 6772 (Nested Loop)
          Node 6773 (Seq Scan) - LEAF
          Node 6774 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 3.75%
- Improvement: 0.41%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 6768 | Aggregate | 1061.99 | 1022.16 | 3.8% | operator |
| 6769 | Gather Merge | 1061.98 | 1112.81 | 4.8% | operator |
| 6770 | Sort | 1055.88 | 1061.20 | 0.5% | operator |
| 6771 | Aggregate | 1055.86 | 923.04 | 12.6% | operator |
| 6772 | Nested Loop | 1053.84 | 1106.74 | 5.0% | operator |
| 6773 | Seq Scan | 163.65 | 157.02 | 4.1% | operator |
| 6774 | Index Scan | 0.06 | 0.38 | 513.6% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 6773 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=18465
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

### Step 2: Node 6774 (Index Scan) - LEAF

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

### Step 3: Node 6772 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15058
  - nt1=18465
  - nt2=2
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=157.0235
  - rt2=0.3804
  - sel=0.4077
  - st1=0.2261
  - st2=0.0614
  - startup_cost=0.4300
  - total_cost=65983.1200
- **Output:** st=31.53, rt=1106.74

### Step 4: Node 6771 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=15058
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=1106.7378
  - rt2=0.0000
  - sel=0.0003
  - st1=31.5334
  - st2=0.0000
  - startup_cost=66058.4100
  - total_cost=66058.4600
- **Output:** st=911.96, rt=923.04

### Step 5: Node 6770 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=5
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=923.0369
  - rt2=0.0000
  - sel=1.0000
  - st1=911.9572
  - st2=0.0000
  - startup_cost=66058.5200
  - total_cost=66058.5300
- **Output:** st=1059.89, rt=1061.20

### Step 6: Node 6769 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15
  - nt1=5
  - nt2=0
  - parallel_workers=3
  - plan_width=24
  - reltuples=0.0000
  - rt1=1061.2036
  - rt2=0.0000
  - sel=3.0000
  - st1=1059.8891
  - st2=0.0000
  - startup_cost=67058.5600
  - total_cost=67060.3300
- **Output:** st=1109.56, rt=1112.81

### Step 7: Node 6768 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=15
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=1112.8086
  - rt2=0.0000
  - sel=0.3333
  - st1=1109.5635
  - st2=0.0000
  - startup_cost=67058.5600
  - total_cost=67060.4600
- **Output:** st=1025.01, rt=1022.16
