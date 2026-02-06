# Online Prediction Report

**Test Query:** Q19_24_seed_188692713
**Timestamp:** 2026-01-18 20:32:50

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 18611 | Operator + Pattern Training |
| Training_Test | 4658 | Pattern Selection Eval |
| Training | 23269 | Final Model Training |
| Test | 1050 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 8.09%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 390 | 34243.4% | 133549.2647 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 150 | 10.0% | 14.9536 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 90 | 8.5% | 7.6786 |
| 7524c54c | Aggregate -> Hash Join (Outer) | 2 | 68 | 8.2% | 5.5861 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 428 | 15281.2% | 65403.5311 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 90 | 15.3% | 13.7321 |
| 2e8f3f67 | Gather -> Aggregate -> Hash Join (Outer)... | 3 | 38 | 8.3% | 3.1568 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 180 | 36271.5% | 65288.7854 |
| 422ae017 | Aggregate -> Hash Join -> [Seq Scan (Out... | 3 | 68 | 8.2% | 5.5861 |
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
| 0 | 3aab37be | 133549.2647 | -0.0000% | REJECTED | 17.94% |
| 1 | 4fc84c77 | 14.9536 | N/A | SKIPPED_LOW_ERROR | 17.94% |
| 2 | 634cdbe2 | 7.6786 | N/A | SKIPPED_LOW_ERROR | 17.94% |
| 3 | 7524c54c | 5.5861 | N/A | SKIPPED_LOW_ERROR | 17.94% |
| 4 | 895c6e8c | 65403.5311 | 0.0009% | ACCEPTED | 17.94% |
| 5 | a5f39f08 | 13.7321 | 1.3108% | ACCEPTED | 16.63% |
| 6 | 2e8f3f67 | 3.1568 | N/A | SKIPPED_LOW_ERROR | 16.63% |
| 7 | f4cb205a | 65288.7854 | 0.0000% | ACCEPTED | 16.63% |
| 8 | 422ae017 | 5.5861 | N/A | SKIPPED_LOW_ERROR | 16.63% |
| 9 | efde8b38 | 5.1439 | 0.1577% | ACCEPTED | 16.47% |
| 10 | af27a52b | 3.1568 | N/A | SKIPPED_LOW_ERROR | 16.47% |
| 11 | 4e54d684 | 2.6438 | N/A | SKIPPED_LOW_ERROR | 16.47% |
| 12 | 310134da | 5.1439 | -0.0002% | REJECTED | 16.47% |
| 13 | 422b9b8c | 2.0083 | N/A | SKIPPED_LOW_ERROR | 16.47% |
| 14 | f8295d8b | 3.4855 | -0.0022% | REJECTED | 16.47% |
## Query Tree

```
Node 31682 (Aggregate) [PATTERN: efde8b38] - ROOT
  Node 31683 (Gather) [consumed]
    Node 31684 (Aggregate) [consumed]
      Node 31685 (Hash Join) [consumed]
        Node 31686 (Seq Scan) - LEAF
        Node 31687 (Hash)
          Node 31688 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | efde8b38 | 31682 | 31683, 31684, 31685 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 2.59%
- Improvement: 5.49%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 31682 | Aggregate | 851.36 | 829.29 | 2.6% | pattern |
| 31686 | Seq Scan | 777.68 | 743.46 | 4.4% | operator |
| 31687 | Hash | 52.30 | 8.29 | 84.2% | operator |
| 31688 | Seq Scan | 52.22 | 23.76 | 54.5% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 31688 (Seq Scan) - LEAF

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

### Step 2: Node 31686 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=22495
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
- **Output:** st=7.83, rt=743.46

### Step 3: Node 31687 (Hash)

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

### Step 4: Node 31682 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** efde8b38 (Aggregate -> Gather -> Aggregate -> Hash Join (Outer) (Outer) (Outer))
- **Consumes:** Nodes 31683, 31684, 31685
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=1
  - Aggregate_Outer_nt1=23
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=32
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0435
  - Aggregate_Outer_startup_cost=156338.6900
  - Aggregate_Outer_total_cost=156338.7000
  - Aggregate_np=0
  - Aggregate_nt=1
  - Aggregate_nt1=5
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=32
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=157339.2300
  - Aggregate_total_cost=157339.2400
  - Gather_Outer_np=0
  - Gather_Outer_nt=5
  - Gather_Outer_nt1=1
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=5
  - Gather_Outer_plan_width=32
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=5.0000
  - Gather_Outer_startup_cost=157338.6900
  - Gather_Outer_total_cost=157339.2000
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=23
  - HashJoin_Outer_nt1=22495
  - HashJoin_Outer_nt2=201
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=12
  - HashJoin_Outer_reltuples=0.0000
  - HashJoin_Outer_sel=0.0000
  - HashJoin_Outer_startup_cost=7672.1800
  - HashJoin_Outer_total_cost=156338.5200
- **Output:** st=824.24, rt=829.29
