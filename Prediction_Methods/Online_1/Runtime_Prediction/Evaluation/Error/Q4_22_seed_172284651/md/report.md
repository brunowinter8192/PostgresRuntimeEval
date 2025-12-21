# Online Prediction Report

**Test Query:** Q4_22_seed_172284651
**Timestamp:** 2025-12-21 21:28:30

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 3.26%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 96 | 4.7% | 4.4662 |
| f8231c4d | Aggregate -> Gather Merge -> Sort -> Agg... | 4 | 48 | 7.1% | 3.4083 |
| 260efc4f | Aggregate -> Gather Merge -> Sort -> Agg... | 5 | 24 | 4.3% | 1.0349 |
| 80bd802d | Aggregate -> Gather Merge -> Sort -> Agg... | 6 | 24 | 4.3% | 1.0349 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 96 | 7.6% | 7.3257 |
| 715d5c92 | Gather Merge -> Sort -> Aggregate (Outer... | 3 | 48 | 9.1% | 4.3530 |
| 1393818c | Gather Merge -> Sort -> Aggregate -> Nes... | 4 | 24 | 4.9% | 1.1790 |
| 6e6e9493 | Gather Merge -> Sort -> Aggregate -> Nes... | 5 | 24 | 4.9% | 1.1790 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| f86f2b1b | Sort -> Aggregate -> Nested Loop (Outer)... | 3 | 24 | 2.1% | 0.5091 |
| ab77776a | Sort -> Aggregate -> Nested Loop -> [Seq... | 4 | 24 | 2.1% | 0.5091 |
| 3b447875 | Aggregate -> Nested Loop (Outer) | 2 | 44 | 8.1% | 3.5717 |
| 3f1648ef | Aggregate -> Nested Loop -> [Seq Scan (O... | 3 | 24 | 12.7% | 3.0380 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 147.6% | 141.6847 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.92% |
| 1 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 2 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 3 | 1691f6f0 | 7.3257 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 4 | 29ee00db | 4.4662 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 5 | 715d5c92 | 4.3530 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 6 | 3b447875 | 3.5717 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 7 | f8231c4d | 3.4083 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 8 | 3f1648ef | 3.0380 | 0.0002% | REJECTED | 17.92% |
| 9 | 1393818c | 1.1790 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 10 | 6e6e9493 | 1.1790 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 11 | 260efc4f | 1.0349 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 12 | 80bd802d | 1.0349 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 13 | ab77776a | 0.5091 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 14 | f86f2b1b | 0.5091 | N/A | SKIPPED_LOW_ERROR | 17.92% |
## Query Tree

```
Node 6299 (Aggregate) - ROOT
  Node 6300 (Gather Merge)
    Node 6301 (Sort)
      Node 6302 (Aggregate)
        Node 6303 (Nested Loop)
          Node 6304 (Seq Scan) - LEAF
          Node 6305 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 2.83%
- Improvement: 0.42%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 6299 | Aggregate | 1052.31 | 1022.48 | 2.8% | operator |
| 6300 | Gather Merge | 1052.30 | 1112.87 | 5.8% | operator |
| 6301 | Sort | 1047.54 | 1061.19 | 1.3% | operator |
| 6302 | Aggregate | 1047.52 | 923.43 | 11.8% | operator |
| 6303 | Nested Loop | 1045.66 | 1106.40 | 5.8% | operator |
| 6304 | Seq Scan | 165.01 | 157.03 | 4.8% | operator |
| 6305 | Index Scan | 0.06 | 0.38 | 513.6% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 6304 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=17869
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

### Step 2: Node 6305 (Index Scan) - LEAF

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

### Step 3: Node 6303 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14572
  - nt1=17869
  - nt2=2
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=157.0309
  - rt2=0.3804
  - sel=0.4077
  - st1=0.2257
  - st2=0.0614
  - startup_cost=0.4300
  - total_cost=65507.8400
- **Output:** st=31.34, rt=1106.40

### Step 4: Node 6302 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=14572
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=1106.3994
  - rt2=0.0000
  - sel=0.0003
  - st1=31.3350
  - st2=0.0000
  - startup_cost=65580.7000
  - total_cost=65580.7500
- **Output:** st=912.30, rt=923.43

### Step 5: Node 6301 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=5
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=923.4321
  - rt2=0.0000
  - sel=1.0000
  - st1=912.3044
  - st2=0.0000
  - startup_cost=65580.8100
  - total_cost=65580.8200
- **Output:** st=1059.87, rt=1061.19

### Step 6: Node 6300 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15
  - nt1=5
  - nt2=0
  - parallel_workers=3
  - plan_width=24
  - reltuples=0.0000
  - rt1=1061.1879
  - rt2=0.0000
  - sel=3.0000
  - st1=1059.8750
  - st2=0.0000
  - startup_cost=66580.8500
  - total_cost=66582.6200
- **Output:** st=1109.63, rt=1112.87

### Step 7: Node 6299 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=15
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=1112.8723
  - rt2=0.0000
  - sel=0.3333
  - st1=1109.6290
  - st2=0.0000
  - startup_cost=66580.8500
  - total_cost=66582.7500
- **Output:** st=1025.28, rt=1022.48
