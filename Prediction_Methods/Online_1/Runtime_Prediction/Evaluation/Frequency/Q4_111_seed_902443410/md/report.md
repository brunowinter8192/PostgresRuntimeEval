# Online Prediction Report

**Test Query:** Q4_111_seed_902443410
**Timestamp:** 2026-01-11 18:36:04

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

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 96 | 7.6% | 7.3257 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 96 | 4.7% | 4.4662 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 147.6% | 141.6847 |
| 715d5c92 | Gather Merge -> Sort -> Aggregate (Outer... | 3 | 48 | 9.1% | 4.3530 |
| f8231c4d | Aggregate -> Gather Merge -> Sort -> Agg... | 4 | 48 | 7.1% | 3.4083 |
| 3b447875 | Aggregate -> Nested Loop (Outer) | 2 | 44 | 8.1% | 3.5717 |
| f86f2b1b | Sort -> Aggregate -> Nested Loop (Outer)... | 3 | 24 | 2.1% | 0.5091 |
| 1393818c | Gather Merge -> Sort -> Aggregate -> Nes... | 4 | 24 | 4.9% | 1.1790 |
| 3f1648ef | Aggregate -> Nested Loop -> [Seq Scan (O... | 3 | 24 | 12.7% | 3.0380 |
| 260efc4f | Aggregate -> Gather Merge -> Sort -> Agg... | 5 | 24 | 4.3% | 1.0349 |
| ab77776a | Sort -> Aggregate -> Nested Loop -> [Seq... | 4 | 24 | 2.1% | 0.5091 |
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
| 1 | 2724c080 | 19.6008 | 0.0346% | ACCEPTED | 17.77% |
| 2 | 1691f6f0 | 7.3257 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 3 | 29ee00db | 4.4662 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 4 | c53c4396 | 141.6847 | N/A | REJECTED | 17.77% |
| 5 | 715d5c92 | 4.3530 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 6 | f8231c4d | 3.4083 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 7 | 3b447875 | 3.5717 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 8 | f86f2b1b | 0.5091 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 9 | 1393818c | 1.1790 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 10 | 3f1648ef | 3.0380 | N/A | REJECTED | 17.77% |
| 11 | 260efc4f | 1.0349 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 12 | ab77776a | 0.5091 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 13 | 6e6e9493 | 1.1790 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 14 | 80bd802d | 1.0349 | N/A | SKIPPED_LOW_ERROR | 17.77% |
## Query Tree

```
Node 5935 (Aggregate) [PATTERN: 2724c080] - ROOT
  Node 5936 (Gather Merge) [consumed]
    Node 5937 (Sort) [PATTERN: 1d35fb97]
      Node 5938 (Aggregate) [consumed]
        Node 5939 (Nested Loop)
          Node 5940 (Seq Scan) - LEAF
          Node 5941 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Sort -> Aggregate (Outer) | 1d35fb97 | 5937 | 5935, 5936, 5938 |
| Aggregate -> Gather Merge (Out | 2724c080 | 5935 | 5936, 5937, 5938 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 2.06%
- Improvement: 1.67%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 5935 | Aggregate | 1057.16 | 1078.92 | 2.1% | pattern |
| 5937 | Sort | 1052.36 | 1055.51 | 0.3% | pattern |
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

### Step 4: Node 5937 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 1d35fb97 (Sort -> Aggregate (Outer))
- **Consumes:** Nodes 5935, 5936, 5938
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=5
  - Aggregate_Outer_nt1=15113
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=24
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0003
  - Aggregate_Outer_startup_cost=66113.1500
  - Aggregate_Outer_total_cost=66113.2000
  - Sort_np=0
  - Sort_nt=5
  - Sort_nt1=5
  - Sort_nt2=0
  - Sort_parallel_workers=0
  - Sort_plan_width=24
  - Sort_reltuples=0.0000
  - Sort_sel=1.0000
  - Sort_startup_cost=66113.2600
  - Sort_total_cost=66113.2700
- **Output:** st=1054.35, rt=1055.51

### Step 5: Node 5935 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 2724c080 (Aggregate -> Gather Merge (Outer))
- **Consumes:** Nodes 5936, 5937, 5938
- **Input Features:**
  - Aggregate_np=0
  - Aggregate_nt=5
  - Aggregate_nt1=15
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=24
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.3333
  - Aggregate_startup_cost=67113.3000
  - Aggregate_total_cost=67115.2000
  - GatherMerge_Outer_np=0
  - GatherMerge_Outer_nt=15
  - GatherMerge_Outer_nt1=5
  - GatherMerge_Outer_nt2=0
  - GatherMerge_Outer_parallel_workers=3
  - GatherMerge_Outer_plan_width=24
  - GatherMerge_Outer_reltuples=0.0000
  - GatherMerge_Outer_sel=3.0000
  - GatherMerge_Outer_startup_cost=67113.3000
  - GatherMerge_Outer_total_cost=67115.0700
- **Output:** st=1076.38, rt=1078.92
