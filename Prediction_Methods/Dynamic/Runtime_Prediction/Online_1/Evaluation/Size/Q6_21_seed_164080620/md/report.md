# Online Prediction Report

**Test Query:** Q6_21_seed_164080620
**Timestamp:** 2025-12-21 15:58:30

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 18971 | Operator + Pattern Training |
| Training_Test | 4748 | Pattern Selection Eval |
| Training | 23719 | Final Model Training |
| Test | 600 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 19.48%

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
Node 10153 (Aggregate) [PATTERN: a5f39f08] - ROOT
  Node 10154 (Gather) [consumed]
    Node 10155 (Aggregate) [consumed]
      Node 10156 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | a5f39f08 | 10153 | 10154, 10155 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 10.25%
- Improvement: 9.22%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 10153 | Aggregate | 770.95 | 849.99 | 10.3% | pattern |
| 10156 | Seq Scan | 751.34 | 748.50 | 0.4% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 10156 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=22717
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=12
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0038
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=139605.4700
- **Output:** st=1.92, rt=748.50

### Step 2: Node 10153 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** a5f39f08 (Aggregate -> Gather -> Aggregate (Outer) (Outer))
- **Consumes:** Nodes 10154, 10155
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=1
  - Aggregate_Outer_nt1=22717
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=32
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0000
  - Aggregate_Outer_startup_cost=139719.0500
  - Aggregate_Outer_total_cost=139719.0700
  - Aggregate_np=0
  - Aggregate_nt=1
  - Aggregate_nt1=5
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=32
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=140719.5900
  - Aggregate_total_cost=140719.6000
  - Gather_Outer_np=0
  - Gather_Outer_nt=5
  - Gather_Outer_nt1=1
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=5
  - Gather_Outer_plan_width=32
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=5.0000
  - Gather_Outer_startup_cost=140719.0500
  - Gather_Outer_total_cost=140719.5700
- **Output:** st=844.38, rt=849.99
