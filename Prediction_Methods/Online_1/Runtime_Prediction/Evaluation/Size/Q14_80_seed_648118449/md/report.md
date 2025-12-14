# Online Prediction Report

**Test Query:** Q14_80_seed_648118449
**Timestamp:** 2025-12-13 02:29:39

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 11.11%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 75736.1626 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 113504.2307 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 13.3894 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 96 | 7.7175 |
| 7524c54c | Aggregate -> Hash Join (Outer) | 2 | 76 | 5.2190 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 168 | 75544.5822 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 96 | 12.4695 |
| 422ae017 | Aggregate -> Hash Join -> [Seq Scan (Out... | 3 | 76 | 5.2190 |
| 2e8f3f67 | Gather -> Aggregate -> Hash Join (Outer)... | 3 | 52 | 3.5252 |
| efde8b38 | Aggregate -> Gather -> Aggregate -> Hash... | 4 | 52 | 5.3353 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 1 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 5 | f4cb205a | 75544.5822 | 0.0006% | REJECTED | 17.92% |
| 6 | a5f39f08 | 12.4695 | 1.7095% | ACCEPTED | 16.21% |
## Query Tree

```
Node 27316 (Aggregate) [PATTERN: a5f39f08] - ROOT
  Node 27317 (Gather) [consumed]
    Node 27318 (Aggregate) [consumed]
      Node 27319 (Hash Join)
        Node 27320 (Seq Scan) - LEAF
        Node 27321 (Hash)
          Node 27322 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | a5f39f08 | 27316 | 27317, 27318 |


## Phase E: Final Prediction

- Final MRE: 2.43%
- Improvement: 8.69%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 27316 | Aggregate | 814.96 | 834.73 | 2.4% | pattern |
| 27319 | Hash Join | 791.32 | 788.24 | 0.4% | operator |
| 27320 | Seq Scan | 740.97 | 747.90 | 0.9% | operator |
| 27321 | Hash | 42.13 | 21.25 | 49.6% | operator |
| 27322 | Seq Scan | 36.41 | 16.56 | 54.5% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 27322 (Seq Scan) - LEAF

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

### Step 2: Node 27320 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=15275
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=16
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0025
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=130603.6400
- **Output:** st=3.47, rt=747.90

### Step 3: Node 27321 (Hash)

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

### Step 4: Node 27319 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15275
  - nt1=15275
  - nt2=83333
  - parallel_workers=0
  - plan_width=33
  - reltuples=0.0000
  - rt1=747.8963
  - rt2=21.2487
  - sel=0.0000
  - st1=3.4663
  - st2=21.2480
  - startup_cost=6003.0000
  - total_cost=136646.7400
- **Output:** st=49.30, rt=788.24

### Step 5: Node 27316 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** a5f39f08 (Aggregate -> Gather -> Aggregate (Outer) (Outer))
- **Consumes:** Nodes 27317, 27318
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=1
  - Aggregate_Outer_nt1=15275
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=64
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0001
  - Aggregate_Outer_startup_cost=136914.0600
  - Aggregate_Outer_total_cost=136914.0700
  - Aggregate_np=0
  - Aggregate_nt=1
  - Aggregate_nt1=5
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=32
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=137914.6200
  - Aggregate_total_cost=137914.6400
  - Gather_Outer_np=0
  - Gather_Outer_nt=5
  - Gather_Outer_nt1=1
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=5
  - Gather_Outer_plan_width=64
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=5.0000
  - Gather_Outer_startup_cost=137914.0600
  - Gather_Outer_total_cost=137914.5700
- **Output:** st=829.18, rt=834.73
