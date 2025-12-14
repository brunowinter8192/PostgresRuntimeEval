# Online Prediction Report

**Test Query:** Q19_124_seed_1009095813
**Timestamp:** 2025-12-13 03:48:53

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 6.40%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 75736.1626 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 113504.2307 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 168 | 75544.5822 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 13.3894 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 96 | 7.7175 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 96 | 12.4695 |
| 7524c54c | Aggregate -> Hash Join (Outer) | 2 | 76 | 5.2190 |
| 422ae017 | Aggregate -> Hash Join -> [Seq Scan (Out... | 3 | 76 | 5.2190 |
| 2e8f3f67 | Gather -> Aggregate -> Hash Join (Outer)... | 3 | 52 | 3.5252 |
| efde8b38 | Aggregate -> Gather -> Aggregate -> Hash... | 4 | 52 | 5.3353 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 1 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 2 | f4cb205a | 75544.5822 | 0.0006% | REJECTED | 17.92% |
| 5 | a5f39f08 | 12.4695 | 1.7095% | ACCEPTED | 16.21% |
## Query Tree

```
Node 31402 (Aggregate) [PATTERN: a5f39f08] - ROOT
  Node 31403 (Gather) [consumed]
    Node 31404 (Aggregate) [consumed]
      Node 31405 (Hash Join)
        Node 31406 (Seq Scan) - LEAF
        Node 31407 (Hash)
          Node 31408 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | a5f39f08 | 31402 | 31403, 31404 |


## Phase E: Final Prediction

- Final MRE: 1.62%
- Improvement: 4.78%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 31402 | Aggregate | 848.21 | 834.50 | 1.6% | pattern |
| 31405 | Hash Join | 829.09 | 782.38 | 5.6% | operator |
| 31406 | Seq Scan | 775.85 | 750.07 | 3.3% | operator |
| 31407 | Hash | 50.59 | 12.06 | 76.2% | operator |
| 31408 | Seq Scan | 50.46 | 31.60 | 37.4% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 31408 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=203
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=30
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0010
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=7669.6700
- **Output:** st=2.66, rt=31.60

### Step 2: Node 31406 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=22543
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=21
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0038
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=148607.2900
- **Output:** st=2.79, rt=750.07

### Step 3: Node 31407 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=203
  - nt1=203
  - nt2=0
  - parallel_workers=0
  - plan_width=30
  - reltuples=0.0000
  - rt1=31.6020
  - rt2=0.0000
  - sel=1.0000
  - st1=2.6639
  - st2=0.0000
  - startup_cost=7669.6700
  - total_cost=7669.6700
- **Output:** st=12.06, rt=12.06

### Step 4: Node 31405 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=23
  - nt1=22543
  - nt2=203
  - parallel_workers=0
  - plan_width=12
  - reltuples=0.0000
  - rt1=750.0690
  - rt2=12.0554
  - sel=0.0000
  - st1=2.7884
  - st2=12.0557
  - startup_cost=7672.2000
  - total_cost=156338.6700
- **Output:** st=77.20, rt=782.38

### Step 5: Node 31402 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** a5f39f08 (Aggregate -> Gather -> Aggregate (Outer) (Outer))
- **Consumes:** Nodes 31403, 31404
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=1
  - Aggregate_Outer_nt1=23
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=32
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0435
  - Aggregate_Outer_startup_cost=156338.8400
  - Aggregate_Outer_total_cost=156338.8500
  - Aggregate_np=0
  - Aggregate_nt=1
  - Aggregate_nt1=5
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=32
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=157339.3800
  - Aggregate_total_cost=157339.3900
  - Gather_Outer_np=0
  - Gather_Outer_nt=5
  - Gather_Outer_nt1=1
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=5
  - Gather_Outer_plan_width=32
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=5.0000
  - Gather_Outer_startup_cost=157338.8400
  - Gather_Outer_total_cost=157339.3500
- **Output:** st=829.19, rt=834.50
