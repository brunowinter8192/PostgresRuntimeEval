# Online Prediction Report

**Test Query:** Q4_64_seed_516853953
**Timestamp:** 2026-01-01 19:18:54

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 4.05%

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
| 0 | 1d35fb97 | 26.4017 | 0.1167% | ACCEPTED | 17.81% |
| 1 | 2724c080 | 7.7852 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 2 | 1691f6f0 | 7.2969 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 3 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.81% |
| 4 | 29ee00db | 4.4636 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 5 | 715d5c92 | 4.3242 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 6 | f8231c4d | 3.4058 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 7 | 3b447875 | 1.1741 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 8 | f86f2b1b | 0.3988 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 9 | 1393818c | 1.1761 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 10 | ab77776a | 0.3988 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 11 | 260efc4f | 1.0354 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 12 | 6e6e9493 | 1.1761 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 13 | 80bd802d | 1.0354 | N/A | SKIPPED_LOW_ERROR | 17.81% |
## Query Tree

```
Node 6621 (Aggregate) - ROOT
  Node 6622 (Gather Merge)
    Node 6623 (Sort) [PATTERN: 1d35fb97]
      Node 6624 (Aggregate) [consumed]
        Node 6625 (Nested Loop)
          Node 6626 (Seq Scan) - LEAF
          Node 6627 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Sort -> Aggregate (Outer) | 1d35fb97 | 6623 | 6624 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 3.64%
- Improvement: 0.41%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 6621 | Aggregate | 1060.67 | 1022.11 | 3.6% | operator |
| 6622 | Gather Merge | 1060.66 | 1112.71 | 4.9% | operator |
| 6623 | Sort | 1055.71 | 1055.51 | 0.0% | pattern |
| 6625 | Nested Loop | 1053.74 | 1106.77 | 5.0% | operator |
| 6626 | Seq Scan | 165.23 | 157.02 | 5.0% | operator |
| 6627 | Index Scan | 0.06 | 0.38 | 513.6% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 6626 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=18529
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

### Step 2: Node 6627 (Index Scan) - LEAF

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

### Step 3: Node 6625 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15110
  - nt1=18529
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
  - total_cost=66034.3500
- **Output:** st=31.56, rt=1106.77

### Step 4: Node 6623 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 1d35fb97 (Sort -> Aggregate (Outer))
- **Consumes:** Nodes 6624
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=5
  - Aggregate_Outer_nt1=15110
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=24
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0003
  - Aggregate_Outer_startup_cost=66109.9000
  - Aggregate_Outer_total_cost=66109.9500
  - Sort_np=0
  - Sort_nt=5
  - Sort_nt1=5
  - Sort_nt2=0
  - Sort_parallel_workers=0
  - Sort_plan_width=24
  - Sort_reltuples=0.0000
  - Sort_sel=1.0000
  - Sort_startup_cost=66110.0100
  - Sort_total_cost=66110.0200
- **Output:** st=1054.35, rt=1055.51

### Step 5: Node 6622 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15
  - nt1=5
  - nt2=0
  - parallel_workers=3
  - plan_width=24
  - reltuples=0.0000
  - rt1=1055.5089
  - rt2=0.0000
  - sel=3.0000
  - st1=1054.3461
  - st2=0.0000
  - startup_cost=67110.0500
  - total_cost=67111.8300
- **Output:** st=1109.46, rt=1112.71

### Step 6: Node 6621 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=15
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=1112.7059
  - rt2=0.0000
  - sel=0.3333
  - st1=1109.4603
  - st2=0.0000
  - startup_cost=67110.0500
  - total_cost=67111.9500
- **Output:** st=1024.97, rt=1022.11
