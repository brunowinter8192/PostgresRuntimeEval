# Online Prediction Report

**Test Query:** Q14_74_seed_598894263
**Timestamp:** 2026-01-18 20:15:37

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 18611 | Operator + Pattern Training |
| Training_Test | 4658 | Pattern Selection Eval |
| Training | 23269 | Final Model Training |
| Test | 1050 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 7.22%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 390 | 34889.7% | 136069.6918 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 150 | 9.4% | 14.1138 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 90 | 8.1% | 7.3162 |
| 7524c54c | Aggregate -> Hash Join (Outer) | 2 | 68 | 7.3% | 4.9917 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 428 | 15940.0% | 68223.0970 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 90 | 14.3% | 12.8731 |
| 2e8f3f67 | Gather -> Aggregate -> Hash Join (Outer)... | 3 | 38 | 6.8% | 2.5782 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 180 | 37832.9% | 68099.2751 |
| 422ae017 | Aggregate -> Hash Join -> [Seq Scan (Out... | 3 | 68 | 7.3% | 4.9917 |
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
| 0 | 3aab37be | 136069.6918 | -0.0000% | REJECTED | 17.77% |
| 1 | 4fc84c77 | 14.1138 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 2 | 634cdbe2 | 7.3162 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 3 | 7524c54c | 4.9917 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 4 | 895c6e8c | 68223.0970 | 0.0008% | ACCEPTED | 17.77% |
| 5 | a5f39f08 | 12.8731 | 1.1258% | ACCEPTED | 16.65% |
| 6 | 2e8f3f67 | 2.5782 | N/A | SKIPPED_LOW_ERROR | 16.65% |
| 7 | f4cb205a | 68099.2751 | 0.0000% | ACCEPTED | 16.65% |
| 8 | 422ae017 | 4.9917 | N/A | SKIPPED_LOW_ERROR | 16.65% |
| 9 | efde8b38 | 4.3066 | 0.0565% | ACCEPTED | 16.59% |
| 10 | af27a52b | 2.5782 | N/A | SKIPPED_LOW_ERROR | 16.59% |
| 11 | 4e54d684 | 1.9769 | N/A | SKIPPED_LOW_ERROR | 16.59% |
| 12 | 310134da | 4.3066 | -0.0000% | REJECTED | 16.59% |
| 13 | 422b9b8c | 1.5081 | N/A | SKIPPED_LOW_ERROR | 16.59% |
| 14 | f8295d8b | 2.6548 | N/A | SKIPPED_LOW_ERROR | 16.59% |
## Query Tree

```
Node 27267 (Aggregate) [PATTERN: efde8b38] - ROOT
  Node 27268 (Gather) [consumed]
    Node 27269 (Aggregate) [consumed]
      Node 27270 (Hash Join) [consumed]
        Node 27271 (Seq Scan) - LEAF
        Node 27272 (Hash)
          Node 27273 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | efde8b38 | 27267 | 27268, 27269, 27270 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 0.22%
- Improvement: 7.00%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 27267 | Aggregate | 859.01 | 857.14 | 0.2% | pattern |
| 27271 | Seq Scan | 785.37 | 758.51 | 3.4% | operator |
| 27272 | Hash | 43.38 | 9.38 | 78.4% | operator |
| 27273 | Seq Scan | 37.76 | 12.70 | 66.4% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 27273 (Seq Scan) - LEAF

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

### Step 2: Node 27271 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=15802
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=16
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0026
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=130603.6400
- **Output:** st=6.82, rt=758.51

### Step 3: Node 27272 (Hash)

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

### Step 4: Node 27267 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** efde8b38 (Aggregate -> Gather -> Aggregate -> Hash Join (Outer) (Outer) (Outer))
- **Consumes:** Nodes 27268, 27269, 27270
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=1
  - Aggregate_Outer_nt1=15802
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=64
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0001
  - Aggregate_Outer_startup_cost=136924.6600
  - Aggregate_Outer_total_cost=136924.6700
  - Aggregate_np=0
  - Aggregate_nt=1
  - Aggregate_nt1=5
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=32
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=137925.2300
  - Aggregate_total_cost=137925.2400
  - Gather_Outer_np=0
  - Gather_Outer_nt=5
  - Gather_Outer_nt1=1
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=5
  - Gather_Outer_plan_width=64
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=5.0000
  - Gather_Outer_startup_cost=137924.6600
  - Gather_Outer_total_cost=137925.1700
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=15802
  - HashJoin_Outer_nt1=15802
  - HashJoin_Outer_nt2=83333
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=33
  - HashJoin_Outer_reltuples=0.0000
  - HashJoin_Outer_sel=0.0000
  - HashJoin_Outer_startup_cost=6003.0000
  - HashJoin_Outer_total_cost=136648.1200
- **Output:** st=850.78, rt=857.14
