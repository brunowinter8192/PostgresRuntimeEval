# Online Prediction Report

**Test Query:** Q6_59_seed_475833798
**Timestamp:** 2025-12-13 04:04:53

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 13.68%

## Phase C: Patterns in Query

- Total Patterns: 6

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 13.3894 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 96 | 7.7175 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 96 | 12.4695 |
| 184f44de | Aggregate -> Seq Scan (Outer) | 2 | 48 | 4.0548 |
| 10e10cd4 | Gather -> Aggregate -> Seq Scan (Outer) ... | 3 | 24 | 2.5305 |
| dd3706ac | Aggregate -> Gather -> Aggregate -> Seq ... | 4 | 24 | 3.4697 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 2 | a5f39f08 | 12.4695 | 1.7095% | ACCEPTED | 16.21% |
## Query Tree

```
Node 10317 (Aggregate) [PATTERN: a5f39f08] - ROOT
  Node 10318 (Gather) [consumed]
    Node 10319 (Aggregate) [consumed]
      Node 10320 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | a5f39f08 | 10317 | 10318, 10319 |


## Phase E: Final Prediction

- Final MRE: 4.31%
- Improvement: 9.37%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 10317 | Aggregate | 795.85 | 830.13 | 4.3% | pattern |
| 10320 | Seq Scan | 774.02 | 750.64 | 3.0% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 10320 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=23898
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
- **Output:** st=4.75, rt=750.64

### Step 2: Node 10317 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** a5f39f08 (Aggregate -> Gather -> Aggregate (Outer) (Outer))
- **Consumes:** Nodes 10318, 10319
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=1
  - Aggregate_Outer_nt1=23898
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=32
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0000
  - Aggregate_Outer_startup_cost=139724.9600
  - Aggregate_Outer_total_cost=139724.9700
  - Aggregate_np=0
  - Aggregate_nt=1
  - Aggregate_nt1=5
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=32
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=140725.5000
  - Aggregate_total_cost=140725.5100
  - Gather_Outer_np=0
  - Gather_Outer_nt=5
  - Gather_Outer_nt1=1
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=5
  - Gather_Outer_plan_width=32
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=5.0000
  - Gather_Outer_startup_cost=140724.9600
  - Gather_Outer_total_cost=140725.4700
- **Output:** st=824.72, rt=830.13
