# Online Prediction Report

**Test Query:** Q6_33_seed_262528992
**Timestamp:** 2026-01-11 20:35:02

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 14.57%

## Phase C: Patterns in Query

- Total Patterns: 6

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 9.3% | 13.3894 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 96 | 13.0% | 12.4695 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 96 | 8.0% | 7.7175 |
| 184f44de | Aggregate -> Seq Scan (Outer) | 2 | 48 | 8.4% | 4.0548 |
| dd3706ac | Aggregate -> Gather -> Aggregate -> Seq ... | 4 | 24 | 14.5% | 3.4697 |
| 10e10cd4 | Gather -> Aggregate -> Seq Scan (Outer) ... | 3 | 24 | 10.5% | 2.5305 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 4fc84c77 | 13.3894 | 0.7530% | ACCEPTED | 17.17% |
| 1 | a5f39f08 | 7.4789 | 0.9566% | ACCEPTED | 16.21% |
| 2 | 184f44de | 2.3138 | 0.0000% | ACCEPTED | 16.21% |
| 3 | dd3706ac | 1.2748 | 0.2258% | ACCEPTED | 15.99% |
## Query Tree

```
Node 10205 (Aggregate) [PATTERN: dd3706ac] - ROOT
  Node 10206 (Gather) [consumed]
    Node 10207 (Aggregate) [consumed]
      Node 10208 (Seq Scan) [consumed] - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | dd3706ac | 10205 | 10206, 10207, 10208 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 0.21%
- Improvement: 14.37%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 10205 | Aggregate | 789.63 | 791.27 | 0.2% | pattern |

## Prediction Chain (Bottom-Up)

### Step 1: Node 10205 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** dd3706ac (Aggregate -> Gather -> Aggregate -> Seq Scan (Outer) (Outer) (Outer))
- **Consumes:** Nodes 10206, 10207, 10208
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=1
  - Aggregate_Outer_nt1=23718
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=32
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0000
  - Aggregate_Outer_startup_cost=139724.0600
  - Aggregate_Outer_total_cost=139724.0700
  - Aggregate_np=0
  - Aggregate_nt=1
  - Aggregate_nt1=5
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=32
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=140724.6000
  - Aggregate_total_cost=140724.6100
  - Gather_Outer_np=0
  - Gather_Outer_nt=5
  - Gather_Outer_nt1=1
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=5
  - Gather_Outer_plan_width=32
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=5.0000
  - Gather_Outer_startup_cost=140724.0600
  - Gather_Outer_total_cost=140724.5700
  - SeqScan_Outer_np=112600
  - SeqScan_Outer_nt=23718
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=12
  - SeqScan_Outer_reltuples=6001215.0000
  - SeqScan_Outer_sel=0.0040
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=139605.4700
- **Output:** st=785.06, rt=791.27
