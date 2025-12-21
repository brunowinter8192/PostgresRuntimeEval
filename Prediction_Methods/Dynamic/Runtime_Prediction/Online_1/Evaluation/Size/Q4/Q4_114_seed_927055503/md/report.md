# Online Prediction Report

**Test Query:** Q4_114_seed_927055503
**Timestamp:** 2025-12-21 14:54:43

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 18611 | Operator + Pattern Training |
| Training_Test | 4658 | Pattern Selection Eval |
| Training | 23269 | Final Model Training |
| Test | 1050 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 2.84%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 210 | 15.3% | 32.1945 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 180 | 12.7% | 22.7741 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 90 | 8.6% | 7.7136 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 90 | 191.2% | 172.0722 |
| 3b447875 | Aggregate -> Nested Loop (Outer) | 2 | 22 | 2.4% | 0.5216 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 90 | 5.0% | 4.4553 |
| 715d5c92 | Gather Merge -> Sort -> Aggregate (Outer... | 3 | 30 | 12.8% | 3.8426 |
| f8231c4d | Aggregate -> Gather Merge -> Sort -> Agg... | 4 | 30 | 10.7% | 3.1984 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 1d35fb97 | 32.1945 | 0.0571% | REJECTED | 17.76% |
| 1 | 2724c080 | 22.7741 | -0.1352% | REJECTED | 17.76% |
| 2 | 1691f6f0 | 7.7136 | N/A | SKIPPED_LOW_ERROR | 17.76% |
| 3 | c53c4396 | 172.0722 | -0.0001% | REJECTED | 17.76% |
| 4 | 3b447875 | 0.5216 | N/A | SKIPPED_LOW_ERROR | 17.76% |
| 5 | 29ee00db | 4.4553 | N/A | SKIPPED_LOW_ERROR | 17.76% |
| 6 | 715d5c92 | 3.8426 | 0.1370% | REJECTED | 17.76% |
| 7 | f8231c4d | 3.1984 | 0.6323% | ACCEPTED | 17.13% |
## Query Tree

```
Node 5956 (Aggregate) [PATTERN: f8231c4d] - ROOT
  Node 5957 (Gather Merge) [consumed]
    Node 5958 (Sort) [consumed]
      Node 5959 (Aggregate) [consumed]
        Node 5960 (Nested Loop)
          Node 5961 (Seq Scan) - LEAF
          Node 5962 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather Merge -> S | f8231c4d | 5956 | 5957, 5958, 5959 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 8.05%
- Improvement: -5.21%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 5956 | Aggregate | 1035.56 | 952.19 | 8.1% | pattern |
| 5960 | Nested Loop | 1029.52 | 1255.45 | 21.9% | operator |
| 5961 | Seq Scan | 162.09 | 154.66 | 4.6% | operator |
| 5962 | Index Scan | 0.06 | 11.10 | 18103.9% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 5961 (Seq Scan) - LEAF

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
- **Output:** st=0.94, rt=154.66

### Step 2: Node 5962 (Index Scan) - LEAF

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
- **Output:** st=-0.00, rt=11.10

### Step 3: Node 5960 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15028
  - nt1=18429
  - nt2=2
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=154.6622
  - rt2=11.1044
  - sel=0.4077
  - st1=0.9382
  - st2=-0.0035
  - startup_cost=0.4300
  - total_cost=65954.5700
- **Output:** st=199.80, rt=1255.45

### Step 4: Node 5956 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** f8231c4d (Aggregate -> Gather Merge -> Sort -> Aggregate (Outer) (Outer) (Outer))
- **Consumes:** Nodes 5957, 5958, 5959
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=5
  - Aggregate_Outer_nt1=15028
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=24
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0003
  - Aggregate_Outer_startup_cost=66029.7100
  - Aggregate_Outer_total_cost=66029.7600
  - Aggregate_np=0
  - Aggregate_nt=5
  - Aggregate_nt1=15
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=24
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.3333
  - Aggregate_startup_cost=67029.8600
  - Aggregate_total_cost=67031.7600
  - GatherMerge_Outer_np=0
  - GatherMerge_Outer_nt=15
  - GatherMerge_Outer_nt1=5
  - GatherMerge_Outer_nt2=0
  - GatherMerge_Outer_parallel_workers=3
  - GatherMerge_Outer_plan_width=24
  - GatherMerge_Outer_reltuples=0.0000
  - GatherMerge_Outer_sel=3.0000
  - GatherMerge_Outer_startup_cost=67029.8600
  - GatherMerge_Outer_total_cost=67031.6300
  - Sort_Outer_np=0
  - Sort_Outer_nt=5
  - Sort_Outer_nt1=5
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=24
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=66029.8200
  - Sort_Outer_total_cost=66029.8300
- **Output:** st=946.37, rt=952.19
