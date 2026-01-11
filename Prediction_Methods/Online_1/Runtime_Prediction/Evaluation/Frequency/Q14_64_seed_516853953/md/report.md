# Online Prediction Report

**Test Query:** Q14_64_seed_516853953
**Timestamp:** 2026-01-11 18:07:38

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 14.47%

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
| 0 | 895c6e8c | 75736.1626 | 0.0004% | ACCEPTED | 17.92% |
| 1 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 2 | f4cb205a | 75544.5822 | 0.0005% | ACCEPTED | 17.92% |
| 3 | 4fc84c77 | 13.3894 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 4 | 634cdbe2 | 7.7175 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 5 | a5f39f08 | 12.4695 | 1.7089% | ACCEPTED | 16.21% |
| 6 | 7524c54c | 5.2190 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 7 | 422ae017 | 5.2190 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 8 | 2e8f3f67 | 3.5252 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 9 | efde8b38 | 5.3353 | 0.0189% | ACCEPTED | 16.20% |
| 10 | af27a52b | 3.5252 | N/A | SKIPPED_LOW_ERROR | 16.20% |
| 11 | 310134da | 5.3353 | 0.0002% | ACCEPTED | 16.20% |
| 12 | 4e54d684 | 3.3909 | N/A | SKIPPED_LOW_ERROR | 16.20% |
| 13 | 422b9b8c | 2.8904 | N/A | SKIPPED_LOW_ERROR | 16.20% |
| 14 | f8295d8b | 4.4470 | N/A | SKIPPED_LOW_ERROR | 16.20% |
## Query Tree

```
Node 27190 (Aggregate) [PATTERN: 310134da] - ROOT
  Node 27191 (Gather) [consumed]
    Node 27192 (Aggregate) [consumed]
      Node 27193 (Hash Join) [consumed]
        Node 27194 (Seq Scan) [consumed] - LEAF
        Node 27195 (Hash) [consumed]
          Node 27196 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | 310134da | 27190 | 27191, 27192, 27193, 27194, 27195 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 4.42%
- Improvement: 10.06%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 27190 | Aggregate | 791.02 | 825.95 | 4.4% | pattern |
| 27196 | Seq Scan | 37.62 | 16.56 | 56.0% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 27196 (Seq Scan) - LEAF

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

### Step 2: Node 27190 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 310134da (Aggregate -> Gather -> Aggregate -> Hash Join -> [Seq Scan (Outer), Hash (Inner)] (Outer) (Outer) (Outer))
- **Consumes:** Nodes 27191, 27192, 27193, 27194, 27195
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=1
  - Aggregate_Outer_nt1=15778
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=64
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0001
  - Aggregate_Outer_startup_cost=136924.1800
  - Aggregate_Outer_total_cost=136924.1900
  - Aggregate_np=0
  - Aggregate_nt=1
  - Aggregate_nt1=5
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=32
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=137924.7400
  - Aggregate_total_cost=137924.7600
  - Gather_Outer_np=0
  - Gather_Outer_nt=5
  - Gather_Outer_nt1=1
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=5
  - Gather_Outer_plan_width=64
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=5.0000
  - Gather_Outer_startup_cost=137924.1800
  - Gather_Outer_total_cost=137924.6900
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=15778
  - HashJoin_Outer_nt1=15778
  - HashJoin_Outer_nt2=83333
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=33
  - HashJoin_Outer_reltuples=0.0000
  - HashJoin_Outer_sel=0.0000
  - HashJoin_Outer_startup_cost=6003.0000
  - HashJoin_Outer_total_cost=136648.0600
  - Hash_Inner_np=0
  - Hash_Inner_nt=83333
  - Hash_Inner_nt1=83333
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=25
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=4961.3300
  - Hash_Inner_total_cost=4961.3300
  - SeqScan_Outer_np=112600
  - SeqScan_Outer_nt=15778
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=16
  - SeqScan_Outer_reltuples=6001215.0000
  - SeqScan_Outer_sel=0.0026
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=130603.6400
- **Output:** st=820.07, rt=825.95
