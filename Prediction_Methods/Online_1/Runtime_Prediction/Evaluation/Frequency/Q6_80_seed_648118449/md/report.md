# Online Prediction Report

**Test Query:** Q6_80_seed_648118449
**Timestamp:** 2026-01-01 19:26:10

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 19.55%

## Phase C: Patterns in Query

- Total Patterns: 6

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 9.3% | 13.3894 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 96 | 8.0% | 7.7175 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 96 | 13.0% | 12.4695 |
| 184f44de | Aggregate -> Seq Scan (Outer) | 2 | 48 | 8.4% | 4.0548 |
| 10e10cd4 | Gather -> Aggregate -> Seq Scan (Outer) ... | 3 | 24 | 10.5% | 2.5305 |
| dd3706ac | Aggregate -> Gather -> Aggregate -> Seq ... | 4 | 24 | 14.5% | 3.4697 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 4fc84c77 | 13.3894 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 1 | 634cdbe2 | 7.7175 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 2 | a5f39f08 | 12.4695 | 1.7095% | ACCEPTED | 16.21% |
| 3 | 184f44de | 2.3138 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 4 | dd3706ac | 1.2748 | N/A | SKIPPED_LOW_ERROR | 16.21% |
## Query Tree

```
Node 10413 (Aggregate) [PATTERN: a5f39f08] - ROOT
  Node 10414 (Gather) [consumed]
    Node 10415 (Aggregate) [consumed]
      Node 10416 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | a5f39f08 | 10413 | 10414, 10415 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 9.70%
- Improvement: 9.86%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 10413 | Aggregate | 756.75 | 830.13 | 9.7% | pattern |
| 10416 | Seq Scan | 731.52 | 750.63 | 2.6% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 10416 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=23625
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=12
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0039
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=139605.4700
- **Output:** st=4.75, rt=750.63

### Step 2: Node 10413 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** a5f39f08 (Aggregate -> Gather -> Aggregate (Outer) (Outer))
- **Consumes:** Nodes 10414, 10415
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=1
  - Aggregate_Outer_nt1=23625
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=32
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0000
  - Aggregate_Outer_startup_cost=139723.6000
  - Aggregate_Outer_total_cost=139723.6100
  - Aggregate_np=0
  - Aggregate_nt=1
  - Aggregate_nt1=5
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=32
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=140724.1300
  - Aggregate_total_cost=140724.1400
  - Gather_Outer_np=0
  - Gather_Outer_nt=5
  - Gather_Outer_nt1=1
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=5
  - Gather_Outer_plan_width=32
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=5.0000
  - Gather_Outer_startup_cost=140723.6000
  - Gather_Outer_total_cost=140724.1100
- **Output:** st=824.71, rt=830.13
