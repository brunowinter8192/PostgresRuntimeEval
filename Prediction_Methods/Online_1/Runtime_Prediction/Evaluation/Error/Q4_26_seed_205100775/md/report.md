# Online Prediction Report

**Test Query:** Q4_26_seed_205100775
**Timestamp:** 2025-12-22 03:19:12

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 4.77%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 147.6% | 141.6847 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 96 | 7.6% | 7.3257 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 96 | 4.7% | 4.4662 |
| 715d5c92 | Gather Merge -> Sort -> Aggregate (Outer... | 3 | 48 | 9.1% | 4.3530 |
| 3b447875 | Aggregate -> Nested Loop (Outer) | 2 | 44 | 8.1% | 3.5717 |
| f8231c4d | Aggregate -> Gather Merge -> Sort -> Agg... | 4 | 48 | 7.1% | 3.4083 |
| 3f1648ef | Aggregate -> Nested Loop -> [Seq Scan (O... | 3 | 24 | 12.7% | 3.0380 |
| 1393818c | Gather Merge -> Sort -> Aggregate -> Nes... | 4 | 24 | 4.9% | 1.1790 |
| 6e6e9493 | Gather Merge -> Sort -> Aggregate -> Nes... | 5 | 24 | 4.9% | 1.1790 |
| 260efc4f | Aggregate -> Gather Merge -> Sort -> Agg... | 5 | 24 | 4.3% | 1.0349 |
| 80bd802d | Aggregate -> Gather Merge -> Sort -> Agg... | 6 | 24 | 4.3% | 1.0349 |
| ab77776a | Sort -> Aggregate -> Nested Loop -> [Seq... | 4 | 24 | 2.1% | 0.5091 |
| f86f2b1b | Sort -> Aggregate -> Nested Loop (Outer)... | 3 | 24 | 2.1% | 0.5091 |

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
Node 6327 (Aggregate) - ROOT
  Node 6328 (Gather Merge)
    Node 6329 (Sort)
      Node 6330 (Aggregate)
        Node 6331 (Nested Loop)
          Node 6332 (Seq Scan) - LEAF
          Node 6333 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 4.36%
- Improvement: 0.41%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 6327 | Aggregate | 1068.77 | 1022.18 | 4.4% | operator |
| 6328 | Gather Merge | 1068.76 | 1112.81 | 4.1% | operator |
| 6329 | Sort | 1064.46 | 1061.20 | 0.3% | operator |
| 6330 | Aggregate | 1064.44 | 923.06 | 13.3% | operator |
| 6331 | Nested Loop | 1062.33 | 1106.72 | 4.2% | operator |
| 6332 | Seq Scan | 164.44 | 157.02 | 4.5% | operator |
| 6333 | Index Scan | 0.06 | 0.38 | 503.9% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 6332 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=18429
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

### Step 2: Node 6333 (Index Scan) - LEAF

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

### Step 3: Node 6331 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15028
  - nt1=18429
  - nt2=2
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=157.0239
  - rt2=0.3804
  - sel=0.4077
  - st1=0.2261
  - st2=0.0614
  - startup_cost=0.4300
  - total_cost=65954.5700
- **Output:** st=31.52, rt=1106.72

### Step 4: Node 6330 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=15028
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=1106.7178
  - rt2=0.0000
  - sel=0.0003
  - st1=31.5218
  - st2=0.0000
  - startup_cost=66029.7100
  - total_cost=66029.7600
- **Output:** st=911.98, rt=923.06

### Step 5: Node 6329 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=5
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=923.0607
  - rt2=0.0000
  - sel=1.0000
  - st1=911.9781
  - st2=0.0000
  - startup_cost=66029.8200
  - total_cost=66029.8300
- **Output:** st=1059.89, rt=1061.20

### Step 6: Node 6328 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15
  - nt1=5
  - nt2=0
  - parallel_workers=3
  - plan_width=24
  - reltuples=0.0000
  - rt1=1061.2026
  - rt2=0.0000
  - sel=3.0000
  - st1=1059.8883
  - st2=0.0000
  - startup_cost=67029.8600
  - total_cost=67031.6300
- **Output:** st=1109.57, rt=1112.81

### Step 7: Node 6327 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=15
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=1112.8124
  - rt2=0.0000
  - sel=0.3333
  - st1=1109.5674
  - st2=0.0000
  - startup_cost=67029.8600
  - total_cost=67031.7600
- **Output:** st=1025.03, rt=1022.18
