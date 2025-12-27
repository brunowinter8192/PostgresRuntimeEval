# Online Prediction Report

**Test Query:** Q4_117_seed_951667596
**Timestamp:** 2025-12-22 07:09:41

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 1.97%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 96 | 7.6% | 7.3257 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 147.6% | 141.6847 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 96 | 4.7% | 4.4662 |
| 715d5c92 | Gather Merge -> Sort -> Aggregate (Outer... | 3 | 48 | 9.1% | 4.3530 |
| f8231c4d | Aggregate -> Gather Merge -> Sort -> Agg... | 4 | 48 | 7.1% | 3.4083 |
| 3b447875 | Aggregate -> Nested Loop (Outer) | 2 | 44 | 8.1% | 3.5717 |
| f86f2b1b | Sort -> Aggregate -> Nested Loop (Outer)... | 3 | 24 | 2.1% | 0.5091 |
| 3f1648ef | Aggregate -> Nested Loop -> [Seq Scan (O... | 3 | 24 | 12.7% | 3.0380 |
| 1393818c | Gather Merge -> Sort -> Aggregate -> Nes... | 4 | 24 | 4.9% | 1.1790 |
| ab77776a | Sort -> Aggregate -> Nested Loop -> [Seq... | 4 | 24 | 2.1% | 0.5091 |
| 260efc4f | Aggregate -> Gather Merge -> Sort -> Agg... | 5 | 24 | 4.3% | 1.0349 |
| 6e6e9493 | Gather Merge -> Sort -> Aggregate -> Nes... | 5 | 24 | 4.9% | 1.1790 |
| 80bd802d | Aggregate -> Gather Merge -> Sort -> Agg... | 6 | 24 | 4.3% | 1.0349 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 1 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 2 | 1691f6f0 | 7.3257 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 3 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.92% |
| 4 | 29ee00db | 4.4662 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 5 | 715d5c92 | 4.3530 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 6 | f8231c4d | 3.4083 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 7 | 3b447875 | 3.5717 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 8 | f86f2b1b | 0.5091 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 9 | 3f1648ef | 3.0380 | 0.0002% | REJECTED | 17.92% |
| 10 | 1393818c | 1.1790 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 11 | ab77776a | 0.5091 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 12 | 260efc4f | 1.0349 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 13 | 6e6e9493 | 1.1790 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 14 | 80bd802d | 1.0349 | N/A | SKIPPED_LOW_ERROR | 17.92% |
## Query Tree

```
Node 5977 (Aggregate) - ROOT
  Node 5978 (Gather Merge)
    Node 5979 (Sort)
      Node 5980 (Aggregate)
        Node 5981 (Nested Loop)
          Node 5982 (Seq Scan) - LEAF
          Node 5983 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 1.54%
- Improvement: 0.43%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 5977 | Aggregate | 1038.30 | 1022.32 | 1.5% | operator |
| 5978 | Gather Merge | 1038.30 | 1112.84 | 7.2% | operator |
| 5979 | Sort | 1033.53 | 1061.20 | 2.7% | operator |
| 5980 | Aggregate | 1033.51 | 923.23 | 10.7% | operator |
| 5981 | Nested Loop | 1031.53 | 1106.57 | 7.3% | operator |
| 5982 | Seq Scan | 161.74 | 157.03 | 2.9% | operator |
| 5983 | Index Scan | 0.06 | 0.38 | 523.7% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 5982 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=18165
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=20
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0121
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=33394.0600
- **Output:** st=0.23, rt=157.03

### Step 2: Node 5983 (Index Scan) - LEAF

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
  - total_cost=2.3100
- **Output:** st=0.06, rt=0.38

### Step 3: Node 5981 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14813
  - nt1=18165
  - nt2=2
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=157.0272
  - rt2=0.3804
  - sel=0.4077
  - st1=0.2259
  - st2=0.0614
  - startup_cost=0.4300
  - total_cost=65744.9100
- **Output:** st=31.43, rt=1106.57

### Step 4: Node 5980 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=14813
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=1106.5670
  - rt2=0.0000
  - sel=0.0003
  - st1=31.4329
  - st2=0.0000
  - startup_cost=65818.9700
  - total_cost=65819.0200
- **Output:** st=912.13, rt=923.23

### Step 5: Node 5979 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=5
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=923.2347
  - rt2=0.0000
  - sel=1.0000
  - st1=912.1310
  - st2=0.0000
  - startup_cost=65819.0800
  - total_cost=65819.0900
- **Output:** st=1059.88, rt=1061.20

### Step 6: Node 5978 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15
  - nt1=5
  - nt2=0
  - parallel_workers=3
  - plan_width=24
  - reltuples=0.0000
  - rt1=1061.1957
  - rt2=0.0000
  - sel=3.0000
  - st1=1059.8820
  - st2=0.0000
  - startup_cost=66819.1200
  - total_cost=66820.8900
- **Output:** st=1109.60, rt=1112.84

### Step 7: Node 5977 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=15
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=1112.8405
  - rt2=0.0000
  - sel=0.3333
  - st1=1109.5963
  - st2=0.0000
  - startup_cost=66819.1200
  - total_cost=66821.0200
- **Output:** st=1025.15, rt=1022.32
