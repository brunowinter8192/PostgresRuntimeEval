# Online Prediction Report

**Test Query:** Q4_30_seed_237916899
**Timestamp:** 2026-01-01 18:17:25

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 3.27%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 96 | 7.6% | 7.3257 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 147.6% | 141.6847 |
| 3b447875 | Aggregate -> Nested Loop (Outer) | 2 | 44 | 8.1% | 3.5717 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 96 | 4.7% | 4.4662 |
| 715d5c92 | Gather Merge -> Sort -> Aggregate (Outer... | 3 | 48 | 9.1% | 4.3530 |
| f86f2b1b | Sort -> Aggregate -> Nested Loop (Outer)... | 3 | 24 | 2.1% | 0.5091 |
| 3f1648ef | Aggregate -> Nested Loop -> [Seq Scan (O... | 3 | 24 | 12.7% | 3.0380 |
| f8231c4d | Aggregate -> Gather Merge -> Sort -> Agg... | 4 | 48 | 7.1% | 3.4083 |
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
| 0 | 1d35fb97 | 26.4017 | 0.1167% | ACCEPTED | 17.81% |
| 1 | 2724c080 | 7.7852 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 2 | 1691f6f0 | 7.2969 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 3 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.81% |
| 4 | 3b447875 | 1.1741 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 5 | 29ee00db | 4.4636 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 6 | 715d5c92 | 4.3242 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 7 | f86f2b1b | 0.3988 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 8 | f8231c4d | 3.4058 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 9 | 1393818c | 1.1761 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 10 | ab77776a | 0.3988 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 11 | 260efc4f | 1.0354 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 12 | 6e6e9493 | 1.1761 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 13 | 80bd802d | 1.0354 | N/A | SKIPPED_LOW_ERROR | 17.81% |
## Query Tree

```
Node 6362 (Aggregate) - ROOT
  Node 6363 (Gather Merge)
    Node 6364 (Sort) [PATTERN: 1d35fb97]
      Node 6365 (Aggregate) [consumed]
        Node 6366 (Nested Loop)
          Node 6367 (Seq Scan) - LEAF
          Node 6368 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Sort -> Aggregate (Outer) | 1d35fb97 | 6364 | 6365 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 2.86%
- Improvement: 0.42%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 6362 | Aggregate | 1052.29 | 1022.24 | 2.9% | operator |
| 6363 | Gather Merge | 1052.29 | 1112.73 | 5.7% | operator |
| 6364 | Sort | 1047.65 | 1055.48 | 0.7% | pattern |
| 6366 | Nested Loop | 1045.48 | 1106.64 | 5.8% | operator |
| 6367 | Seq Scan | 163.38 | 157.03 | 3.9% | operator |
| 6368 | Index Scan | 0.06 | 0.38 | 503.9% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 6367 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=18286
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
- **Output:** st=0.23, rt=157.03

### Step 2: Node 6368 (Index Scan) - LEAF

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

### Step 3: Node 6366 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14912
  - nt1=18286
  - nt2=2
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=157.0257
  - rt2=0.3804
  - sel=0.4077
  - st1=0.2260
  - st2=0.0614
  - startup_cost=0.4300
  - total_cost=65841.2000
- **Output:** st=31.47, rt=1106.64

### Step 4: Node 6364 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 1d35fb97 (Sort -> Aggregate (Outer))
- **Consumes:** Nodes 6365
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=5
  - Aggregate_Outer_nt1=14912
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=24
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0003
  - Aggregate_Outer_startup_cost=65915.7600
  - Aggregate_Outer_total_cost=65915.8100
  - Sort_np=0
  - Sort_nt=5
  - Sort_nt1=5
  - Sort_nt2=0
  - Sort_parallel_workers=0
  - Sort_plan_width=24
  - Sort_reltuples=0.0000
  - Sort_sel=1.0000
  - Sort_startup_cost=65915.8700
  - Sort_total_cost=65915.8800
- **Output:** st=1054.32, rt=1055.48

### Step 5: Node 6363 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15
  - nt1=5
  - nt2=0
  - parallel_workers=3
  - plan_width=24
  - reltuples=0.0000
  - rt1=1055.4797
  - rt2=0.0000
  - sel=3.0000
  - st1=1054.3169
  - st2=0.0000
  - startup_cost=66915.9100
  - total_cost=66917.6800
- **Output:** st=1109.49, rt=1112.73

### Step 6: Node 6362 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=15
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=1112.7314
  - rt2=0.0000
  - sel=0.3333
  - st1=1109.4865
  - st2=0.0000
  - startup_cost=66915.9100
  - total_cost=66917.8100
- **Output:** st=1025.08, rt=1022.24
