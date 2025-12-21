# Online Prediction Report

**Test Query:** Q19_134_seed_1091136123
**Timestamp:** 2025-12-21 18:33:15

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 18611 | Operator + Pattern Training |
| Training_Test | 4658 | Pattern Selection Eval |
| Training | 23269 | Final Model Training |
| Test | 1050 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 8.24%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 428 | 15281.2% | 65403.5311 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 390 | 34243.4% | 133549.2647 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 150 | 10.0% | 14.9536 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 90 | 8.5% | 7.6786 |
| 7524c54c | Aggregate -> Hash Join (Outer) | 2 | 68 | 8.2% | 5.5861 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 180 | 36271.5% | 65288.7854 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 90 | 15.3% | 13.7321 |
| 422ae017 | Aggregate -> Hash Join -> [Seq Scan (Out... | 3 | 68 | 8.2% | 5.5861 |
| 2e8f3f67 | Gather -> Aggregate -> Hash Join (Outer)... | 3 | 38 | 8.3% | 3.1568 |
| efde8b38 | Aggregate -> Gather -> Aggregate -> Hash... | 4 | 38 | 13.5% | 5.1439 |
| af27a52b | Gather -> Aggregate -> Hash Join -> [Seq... | 4 | 38 | 8.3% | 3.1568 |
| 4e54d684 | Aggregate -> Hash Join -> [Seq Scan (Out... | 4 | 30 | 8.8% | 2.6438 |
| 310134da | Aggregate -> Gather -> Aggregate -> Hash... | 5 | 38 | 13.5% | 5.1439 |
| 422b9b8c | Gather -> Aggregate -> Hash Join -> [Seq... | 5 | 30 | 6.7% | 2.0083 |
| f8295d8b | Aggregate -> Gather -> Aggregate -> Hash... | 6 | 30 | 11.6% | 3.4855 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 65403.5311 | 0.0009% | REJECTED | 17.94% |
| 1 | 3aab37be | 133549.2647 | -0.0000% | REJECTED | 17.94% |
| 2 | 4fc84c77 | 14.9536 | N/A | SKIPPED_LOW_ERROR | 17.94% |
| 3 | 634cdbe2 | 7.6786 | N/A | SKIPPED_LOW_ERROR | 17.94% |
| 4 | 7524c54c | 5.5861 | N/A | SKIPPED_LOW_ERROR | 17.94% |
| 5 | f4cb205a | 65288.7854 | 0.0006% | REJECTED | 17.94% |
| 6 | a5f39f08 | 13.7321 | 1.3112% | ACCEPTED | 16.63% |
| 7 | 422ae017 | 2.9139 | N/A | SKIPPED_LOW_ERROR | 16.63% |
| 8 | efde8b38 | 2.3729 | N/A | SKIPPED_LOW_ERROR | 16.63% |
| 9 | 310134da | 2.3729 | N/A | SKIPPED_LOW_ERROR | 16.63% |
| 10 | f8295d8b | 1.1997 | N/A | SKIPPED_LOW_ERROR | 16.63% |
## Query Tree

```
Node 31479 (Aggregate) [PATTERN: a5f39f08] - ROOT
  Node 31480 (Gather) [consumed]
    Node 31481 (Aggregate) [consumed]
      Node 31482 (Hash Join)
        Node 31483 (Seq Scan) - LEAF
        Node 31484 (Hash)
          Node 31485 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | a5f39f08 | 31479 | 31480, 31481 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 2.23%
- Improvement: 6.00%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 31479 | Aggregate | 850.18 | 831.20 | 2.2% | pattern |
| 31482 | Hash Join | 831.07 | 766.06 | 7.8% | operator |
| 31483 | Seq Scan | 780.76 | 743.46 | 4.8% | operator |
| 31484 | Hash | 48.46 | 8.29 | 82.9% | operator |
| 31485 | Seq Scan | 48.29 | 23.76 | 50.8% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 31485 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=201
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
- **Output:** st=1.13, rt=23.76

### Step 2: Node 31483 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=22512
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
- **Output:** st=7.83, rt=743.46

### Step 3: Node 31484 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=201
  - nt1=201
  - nt2=0
  - parallel_workers=0
  - plan_width=30
  - reltuples=0.0000
  - rt1=23.7631
  - rt2=0.0000
  - sel=1.0000
  - st1=1.1346
  - st2=0.0000
  - startup_cost=7669.6700
  - total_cost=7669.6700
- **Output:** st=8.28, rt=8.29

### Step 4: Node 31482 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=23
  - nt1=22512
  - nt2=201
  - parallel_workers=0
  - plan_width=12
  - reltuples=0.0000
  - rt1=743.4585
  - rt2=8.2852
  - sel=0.0000
  - st1=7.8284
  - st2=8.2846
  - startup_cost=7672.1800
  - total_cost=156338.5600
- **Output:** st=60.26, rt=766.06

### Step 5: Node 31479 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** a5f39f08 (Aggregate -> Gather -> Aggregate (Outer) (Outer))
- **Consumes:** Nodes 31480, 31481
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=1
  - Aggregate_Outer_nt1=23
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=32
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0435
  - Aggregate_Outer_startup_cost=156338.7400
  - Aggregate_Outer_total_cost=156338.7500
  - Aggregate_np=0
  - Aggregate_nt=1
  - Aggregate_nt1=5
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=32
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=157339.2800
  - Aggregate_total_cost=157339.2900
  - Gather_Outer_np=0
  - Gather_Outer_nt=5
  - Gather_Outer_nt1=1
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=5
  - Gather_Outer_plan_width=32
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=5.0000
  - Gather_Outer_startup_cost=157338.7400
  - Gather_Outer_total_cost=157339.2500
- **Output:** st=825.73, rt=831.20
