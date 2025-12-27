# Online Prediction Report

**Test Query:** Q19_111_seed_902443410
**Timestamp:** 2025-12-22 07:01:51

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 3.28%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 33781.0% | 113504.2307 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 168 | 44967.0% | 75544.5822 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 9.3% | 13.3894 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 96 | 8.0% | 7.7175 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 96 | 13.0% | 12.4695 |
| 7524c54c | Aggregate -> Hash Join (Outer) | 2 | 76 | 6.9% | 5.2190 |
| 422ae017 | Aggregate -> Hash Join -> [Seq Scan (Out... | 3 | 76 | 6.9% | 5.2190 |
| 2e8f3f67 | Gather -> Aggregate -> Hash Join (Outer)... | 3 | 52 | 6.8% | 3.5252 |
| efde8b38 | Aggregate -> Gather -> Aggregate -> Hash... | 4 | 52 | 10.3% | 5.3353 |
| af27a52b | Gather -> Aggregate -> Hash Join -> [Seq... | 4 | 52 | 6.8% | 3.5252 |
| 310134da | Aggregate -> Gather -> Aggregate -> Hash... | 5 | 52 | 10.3% | 5.3353 |
| 4e54d684 | Aggregate -> Hash Join -> [Seq Scan (Out... | 4 | 48 | 7.1% | 3.3909 |
| 422b9b8c | Gather -> Aggregate -> Hash Join -> [Seq... | 5 | 48 | 6.0% | 2.8904 |
| f8295d8b | Aggregate -> Gather -> Aggregate -> Hash... | 6 | 48 | 9.3% | 4.4470 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 1 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 2 | f4cb205a | 75544.5822 | 0.0006% | REJECTED | 17.92% |
| 3 | 4fc84c77 | 13.3894 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 4 | 634cdbe2 | 7.7175 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 5 | a5f39f08 | 12.4695 | 1.7095% | ACCEPTED | 16.21% |
| 6 | 7524c54c | 3.0007 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 7 | 422ae017 | 3.0007 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 8 | efde8b38 | 1.7942 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 9 | 310134da | 1.7942 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 10 | f8295d8b | 1.0024 | N/A | SKIPPED_LOW_ERROR | 16.21% |
## Query Tree

```
Node 31304 (Aggregate) [PATTERN: a5f39f08] - ROOT
  Node 31305 (Gather) [consumed]
    Node 31306 (Aggregate) [consumed]
      Node 31307 (Hash Join)
        Node 31308 (Seq Scan) - LEAF
        Node 31309 (Hash)
          Node 31310 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | a5f39f08 | 31304 | 31305, 31306 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 4.50%
- Improvement: -1.22%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 31304 | Aggregate | 873.83 | 834.50 | 4.5% | pattern |
| 31307 | Hash Join | 854.69 | 782.38 | 8.5% | operator |
| 31308 | Seq Scan | 804.20 | 750.07 | 6.7% | operator |
| 31309 | Hash | 47.85 | 12.06 | 74.8% | operator |
| 31310 | Seq Scan | 47.70 | 31.60 | 33.7% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 31310 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=202
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

### Step 2: Node 31308 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=22504
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=21
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0037
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=148607.2900
- **Output:** st=2.79, rt=750.07

### Step 3: Node 31309 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=202
  - nt1=202
  - nt2=0
  - parallel_workers=0
  - plan_width=30
  - reltuples=0.0000
  - rt1=31.6024
  - rt2=0.0000
  - sel=1.0000
  - st1=2.6639
  - st2=0.0000
  - startup_cost=7669.6700
  - total_cost=7669.6700
- **Output:** st=12.06, rt=12.06

### Step 4: Node 31307 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=23
  - nt1=22504
  - nt2=202
  - parallel_workers=0
  - plan_width=12
  - reltuples=0.0000
  - rt1=750.0675
  - rt2=12.0554
  - sel=0.0000
  - st1=2.7883
  - st2=12.0557
  - startup_cost=7672.1900
  - total_cost=156338.5500
- **Output:** st=77.19, rt=782.38

### Step 5: Node 31304 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** a5f39f08 (Aggregate -> Gather -> Aggregate (Outer) (Outer))
- **Consumes:** Nodes 31305, 31306
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=1
  - Aggregate_Outer_nt1=23
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=32
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0435
  - Aggregate_Outer_startup_cost=156338.7300
  - Aggregate_Outer_total_cost=156338.7400
  - Aggregate_np=0
  - Aggregate_nt=1
  - Aggregate_nt1=5
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=32
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=157339.2700
  - Aggregate_total_cost=157339.2800
  - Gather_Outer_np=0
  - Gather_Outer_nt=5
  - Gather_Outer_nt1=1
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=5
  - Gather_Outer_plan_width=32
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=5.0000
  - Gather_Outer_startup_cost=157338.7300
  - Gather_Outer_total_cost=157339.2400
- **Output:** st=829.19, rt=834.50
