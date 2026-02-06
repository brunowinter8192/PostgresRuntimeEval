# Online Prediction Report

**Test Query:** Q6_118_seed_959871627
**Timestamp:** 2026-01-11 17:08:45

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 5.82%

## Phase C: Patterns in Query

- Total Patterns: 6

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 9.3% | 13.3894 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 96 | 8.0% | 7.7175 |
| 184f44de | Aggregate -> Seq Scan (Outer) | 2 | 48 | 8.4% | 4.0548 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 96 | 13.0% | 12.4695 |
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
| 2 | 184f44de | 4.0548 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 3 | a5f39f08 | 12.4695 | 1.7095% | ACCEPTED | 16.21% |
| 4 | 10e10cd4 | 2.5305 | N/A | REJECTED | 16.21% |
| 5 | dd3706ac | 3.4697 | 0.2258% | ACCEPTED | 15.99% |
## Query Tree

```
Node 9977 (Aggregate) [PATTERN: dd3706ac] - ROOT
  Node 9978 (Gather) [consumed]
    Node 9979 (Aggregate) [consumed]
      Node 9980 (Seq Scan) [consumed] - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | dd3706ac | 9977 | 9978, 9979, 9980 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 7.45%
- Improvement: -1.63%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 9977 | Aggregate | 854.97 | 791.26 | 7.5% | pattern |

## Prediction Chain (Bottom-Up)

### Step 1: Node 9977 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** dd3706ac (Aggregate -> Gather -> Aggregate -> Seq Scan (Outer) (Outer) (Outer))
- **Consumes:** Nodes 9978, 9979, 9980
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=1
  - Aggregate_Outer_nt1=22639
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=32
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0000
  - Aggregate_Outer_startup_cost=139718.6700
  - Aggregate_Outer_total_cost=139718.6800
  - Aggregate_np=0
  - Aggregate_nt=1
  - Aggregate_nt1=5
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=32
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=140719.2000
  - Aggregate_total_cost=140719.2100
  - Gather_Outer_np=0
  - Gather_Outer_nt=5
  - Gather_Outer_nt1=1
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=5
  - Gather_Outer_plan_width=32
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=5.0000
  - Gather_Outer_startup_cost=140718.6700
  - Gather_Outer_total_cost=140719.1800
  - SeqScan_Outer_np=112600
  - SeqScan_Outer_nt=22639
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=12
  - SeqScan_Outer_reltuples=6001215.0000
  - SeqScan_Outer_sel=0.0038
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=139605.4700
- **Output:** st=785.06, rt=791.26
