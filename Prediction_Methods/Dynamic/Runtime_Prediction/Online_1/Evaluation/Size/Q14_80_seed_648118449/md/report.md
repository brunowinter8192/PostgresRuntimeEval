# Online Prediction Report

**Test Query:** Q14_80_seed_648118449
**Timestamp:** 2025-12-21 18:21:51

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 18611 | Operator + Pattern Training |
| Training_Test | 4658 | Pattern Selection Eval |
| Training | 23269 | Final Model Training |
| Test | 1050 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 13.02%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 428 | 15940.0% | 68223.0970 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 390 | 34889.7% | 136069.6918 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 150 | 9.4% | 14.1138 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 90 | 8.1% | 7.3162 |
| 7524c54c | Aggregate -> Hash Join (Outer) | 2 | 68 | 7.3% | 4.9917 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 180 | 37832.9% | 68099.2751 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 90 | 14.3% | 12.8731 |
| 422ae017 | Aggregate -> Hash Join -> [Seq Scan (Out... | 3 | 68 | 7.3% | 4.9917 |
| 2e8f3f67 | Gather -> Aggregate -> Hash Join (Outer)... | 3 | 38 | 6.8% | 2.5782 |
| efde8b38 | Aggregate -> Gather -> Aggregate -> Hash... | 4 | 38 | 11.3% | 4.3066 |
| af27a52b | Gather -> Aggregate -> Hash Join -> [Seq... | 4 | 38 | 6.8% | 2.5782 |
| 4e54d684 | Aggregate -> Hash Join -> [Seq Scan (Out... | 4 | 30 | 6.6% | 1.9769 |
| 310134da | Aggregate -> Gather -> Aggregate -> Hash... | 5 | 38 | 11.3% | 4.3066 |
| 422b9b8c | Gather -> Aggregate -> Hash Join -> [Seq... | 5 | 30 | 5.0% | 1.5081 |
| f8295d8b | Aggregate -> Gather -> Aggregate -> Hash... | 6 | 30 | 8.8% | 2.6548 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 68223.0970 | 0.0008% | REJECTED | 17.77% |
| 1 | 3aab37be | 136069.6918 | -0.0000% | REJECTED | 17.77% |
| 2 | 4fc84c77 | 14.1138 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 3 | 634cdbe2 | 7.3162 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 4 | 7524c54c | 4.9917 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 5 | f4cb205a | 68099.2751 | 0.0005% | REJECTED | 17.77% |
| 6 | a5f39f08 | 12.8731 | 1.1261% | ACCEPTED | 16.65% |
| 7 | 422ae017 | 3.1212 | N/A | SKIPPED_LOW_ERROR | 16.65% |
| 8 | efde8b38 | 1.9396 | N/A | SKIPPED_LOW_ERROR | 16.65% |
| 9 | 310134da | 1.9396 | N/A | SKIPPED_LOW_ERROR | 16.65% |
| 10 | f8295d8b | 0.7951 | N/A | SKIPPED_LOW_ERROR | 16.65% |
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


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 4.10%
- Improvement: 8.92%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 27316 | Aggregate | 814.96 | 848.37 | 4.1% | pattern |
| 27319 | Hash Join | 791.32 | 807.65 | 2.1% | operator |
| 27320 | Seq Scan | 740.97 | 758.49 | 2.4% | operator |
| 27321 | Hash | 42.13 | 9.38 | 77.7% | operator |
| 27322 | Seq Scan | 36.41 | 12.70 | 65.1% | operator |

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
- **Output:** st=1.22, rt=12.70

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
- **Output:** st=6.82, rt=758.49

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
  - rt1=12.7039
  - rt2=0.0000
  - sel=1.0000
  - st1=1.2208
  - st2=0.0000
  - startup_cost=4961.3300
  - total_cost=4961.3300
- **Output:** st=9.38, rt=9.38

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
  - rt1=758.4892
  - rt2=9.3794
  - sel=0.0000
  - st1=6.8174
  - st2=9.3784
  - startup_cost=6003.0000
  - total_cost=136646.7400
- **Output:** st=78.57, rt=807.65

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
- **Output:** st=842.87, rt=848.37
