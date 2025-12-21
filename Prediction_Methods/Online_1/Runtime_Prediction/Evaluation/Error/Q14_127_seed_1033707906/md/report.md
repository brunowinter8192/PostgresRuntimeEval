# Online Prediction Report

**Test Query:** Q14_127_seed_1033707906
**Timestamp:** 2025-12-21 21:02:25

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 5.02%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 9.3% | 13.3894 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 96 | 13.0% | 12.4695 |
| efde8b38 | Aggregate -> Gather -> Aggregate -> Hash... | 4 | 52 | 10.3% | 5.3353 |
| 310134da | Aggregate -> Gather -> Aggregate -> Hash... | 5 | 52 | 10.3% | 5.3353 |
| f8295d8b | Aggregate -> Gather -> Aggregate -> Hash... | 6 | 48 | 9.3% | 4.4470 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 96 | 8.0% | 7.7175 |
| 2e8f3f67 | Gather -> Aggregate -> Hash Join (Outer)... | 3 | 52 | 6.8% | 3.5252 |
| af27a52b | Gather -> Aggregate -> Hash Join -> [Seq... | 4 | 52 | 6.8% | 3.5252 |
| 422b9b8c | Gather -> Aggregate -> Hash Join -> [Seq... | 5 | 48 | 6.0% | 2.8904 |
| 7524c54c | Aggregate -> Hash Join (Outer) | 2 | 76 | 6.9% | 5.2190 |
| 422ae017 | Aggregate -> Hash Join -> [Seq Scan (Out... | 3 | 76 | 6.9% | 5.2190 |
| 4e54d684 | Aggregate -> Hash Join -> [Seq Scan (Out... | 4 | 48 | 7.1% | 3.3909 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 168 | 44967.0% | 75544.5822 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 33781.0% | 113504.2307 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 1 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 2 | f4cb205a | 75544.5822 | 0.0006% | REJECTED | 17.92% |
| 3 | 4fc84c77 | 13.3894 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 4 | a5f39f08 | 12.4695 | 1.7095% | ACCEPTED | 16.21% |
| 5 | 422ae017 | 3.0007 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 6 | 7524c54c | 3.0007 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 7 | 310134da | 1.7942 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 8 | efde8b38 | 1.7942 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 9 | f8295d8b | 1.0024 | N/A | SKIPPED_LOW_ERROR | 16.21% |
## Query Tree

```
Node 26623 (Aggregate) [PATTERN: a5f39f08] - ROOT
  Node 26624 (Gather) [consumed]
    Node 26625 (Aggregate) [consumed]
      Node 26626 (Hash Join)
        Node 26627 (Seq Scan) - LEAF
        Node 26628 (Hash)
          Node 26629 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | a5f39f08 | 26623 | 26624, 26625 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 3.19%
- Improvement: 1.83%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 26623 | Aggregate | 862.25 | 834.74 | 3.2% | pattern |
| 26626 | Hash Join | 840.00 | 788.28 | 6.2% | operator |
| 26627 | Seq Scan | 788.28 | 747.94 | 5.1% | operator |
| 26628 | Hash | 44.22 | 21.25 | 51.9% | operator |
| 26629 | Seq Scan | 40.09 | 16.56 | 58.7% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 26629 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=83333
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=25
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.4167
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=4961.3300
- **Output:** st=2.10, rt=16.56

### Step 2: Node 26627 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=16281
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=16
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0027
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=130603.6400
- **Output:** st=3.47, rt=747.94

### Step 3: Node 26628 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=83333
  - nt1=83333
  - nt2=0
  - parallel_workers=0
  - plan_width=25
  - reltuples=0.0000
  - rt1=16.5598
  - rt2=0.0000
  - sel=1.0000
  - st1=2.1005
  - st2=0.0000
  - startup_cost=4961.3300
  - total_cost=4961.3300
- **Output:** st=21.25, rt=21.25

### Step 4: Node 26626 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=16281
  - nt1=16281
  - nt2=83333
  - parallel_workers=0
  - plan_width=33
  - reltuples=0.0000
  - rt1=747.9381
  - rt2=21.2487
  - sel=0.0000
  - st1=3.4690
  - st2=21.2480
  - startup_cost=6003.0000
  - total_cost=136649.3800
- **Output:** st=49.33, rt=788.28

### Step 5: Node 26623 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** a5f39f08 (Aggregate -> Gather -> Aggregate (Outer) (Outer))
- **Consumes:** Nodes 26624, 26625
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=1
  - Aggregate_Outer_nt1=16281
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=64
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0001
  - Aggregate_Outer_startup_cost=136934.3000
  - Aggregate_Outer_total_cost=136934.3100
  - Aggregate_np=0
  - Aggregate_nt=1
  - Aggregate_nt1=5
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=32
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=137934.8700
  - Aggregate_total_cost=137934.8800
  - Gather_Outer_np=0
  - Gather_Outer_nt=5
  - Gather_Outer_nt1=1
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=5
  - Gather_Outer_plan_width=64
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=5.0000
  - Gather_Outer_startup_cost=137934.3000
  - Gather_Outer_total_cost=137934.8100
- **Output:** st=829.19, rt=834.74
