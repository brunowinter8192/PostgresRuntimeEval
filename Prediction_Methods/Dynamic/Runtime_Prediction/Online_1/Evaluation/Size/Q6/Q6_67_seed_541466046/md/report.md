# Online Prediction Report

**Test Query:** Q6_67_seed_541466046
**Timestamp:** 2025-12-21 16:00:26

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 18971 | Operator + Pattern Training |
| Training_Test | 4748 | Pattern Selection Eval |
| Training | 23719 | Final Model Training |
| Test | 600 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 13.63%

## Phase C: Patterns in Query

- Total Patterns: 6

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 150 | 8.6% | 12.9432 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 90 | 7.1% | 6.4015 |
| 184f44de | Aggregate -> Seq Scan (Outer) | 2 | 30 | 4.1% | 1.2375 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 90 | 13.0% | 11.6727 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 4fc84c77 | 12.9432 | N/A | SKIPPED_LOW_ERROR | 17.40% |
| 1 | 634cdbe2 | 6.4015 | N/A | SKIPPED_LOW_ERROR | 17.40% |
| 2 | 184f44de | 1.2375 | N/A | SKIPPED_LOW_ERROR | 17.40% |
| 3 | a5f39f08 | 11.6727 | 0.9884% | ACCEPTED | 16.42% |
## Query Tree

```
Node 10353 (Aggregate) [PATTERN: a5f39f08] - ROOT
  Node 10354 (Gather) [consumed]
    Node 10355 (Aggregate) [consumed]
      Node 10356 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | a5f39f08 | 10353 | 10354, 10355 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 4.87%
- Improvement: 8.76%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 10353 | Aggregate | 810.61 | 850.06 | 4.9% | pattern |
| 10356 | Seq Scan | 789.47 | 748.54 | 5.2% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 10356 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=23789
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=12
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0040
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=139605.4700
- **Output:** st=1.92, rt=748.54

### Step 2: Node 10353 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** a5f39f08 (Aggregate -> Gather -> Aggregate (Outer) (Outer))
- **Consumes:** Nodes 10354, 10355
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=1
  - Aggregate_Outer_nt1=23789
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=32
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0000
  - Aggregate_Outer_startup_cost=139724.4200
  - Aggregate_Outer_total_cost=139724.4300
  - Aggregate_np=0
  - Aggregate_nt=1
  - Aggregate_nt1=5
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=32
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=140724.9500
  - Aggregate_total_cost=140724.9600
  - Gather_Outer_np=0
  - Gather_Outer_nt=5
  - Gather_Outer_nt1=1
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=5
  - Gather_Outer_plan_width=32
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=5.0000
  - Gather_Outer_startup_cost=140724.4200
  - Gather_Outer_total_cost=140724.9300
- **Output:** st=844.45, rt=850.06
