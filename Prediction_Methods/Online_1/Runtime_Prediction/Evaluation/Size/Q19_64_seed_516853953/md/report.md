# Online Prediction Report

**Test Query:** Q19_64_seed_516853953
**Timestamp:** 2026-01-11 16:53:21

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 7.35%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 33781.0% | 113504.2307 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 9.3% | 13.3894 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 96 | 8.0% | 7.7175 |
| 7524c54c | Aggregate -> Hash Join (Outer) | 2 | 76 | 6.9% | 5.2190 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 96 | 13.0% | 12.4695 |
| 2e8f3f67 | Gather -> Aggregate -> Hash Join (Outer)... | 3 | 52 | 6.8% | 3.5252 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 168 | 44967.0% | 75544.5822 |
| 422ae017 | Aggregate -> Hash Join -> [Seq Scan (Out... | 3 | 76 | 6.9% | 5.2190 |
| efde8b38 | Aggregate -> Gather -> Aggregate -> Hash... | 4 | 52 | 10.3% | 5.3353 |
| af27a52b | Gather -> Aggregate -> Hash Join -> [Seq... | 4 | 52 | 6.8% | 3.5252 |
| 4e54d684 | Aggregate -> Hash Join -> [Seq Scan (Out... | 4 | 48 | 7.1% | 3.3909 |
| 310134da | Aggregate -> Gather -> Aggregate -> Hash... | 5 | 52 | 10.3% | 5.3353 |
| 422b9b8c | Gather -> Aggregate -> Hash Join -> [Seq... | 5 | 48 | 6.0% | 2.8904 |
| f8295d8b | Aggregate -> Gather -> Aggregate -> Hash... | 6 | 48 | 9.3% | 4.4470 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 1 | 4fc84c77 | 13.3894 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 2 | 634cdbe2 | 7.7175 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 3 | 7524c54c | 5.2190 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 4 | 895c6e8c | 75736.1626 | 0.0004% | ACCEPTED | 17.92% |
| 5 | a5f39f08 | 12.4695 | 1.7094% | ACCEPTED | 16.21% |
| 6 | 2e8f3f67 | 3.5252 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 7 | f4cb205a | 75544.5822 | 0.0000% | ACCEPTED | 16.21% |
| 8 | 422ae017 | 5.2190 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 9 | efde8b38 | 5.3353 | 0.0189% | ACCEPTED | 16.20% |
| 10 | af27a52b | 3.5252 | N/A | SKIPPED_LOW_ERROR | 16.20% |
| 11 | 4e54d684 | 3.3909 | N/A | SKIPPED_LOW_ERROR | 16.20% |
| 12 | 310134da | 5.3353 | 0.0002% | ACCEPTED | 16.20% |
| 13 | 422b9b8c | 2.8904 | N/A | SKIPPED_LOW_ERROR | 16.20% |
| 14 | f8295d8b | 4.4470 | N/A | SKIPPED_LOW_ERROR | 16.20% |
## Query Tree

```
Node 31990 (Aggregate) [PATTERN: 310134da] - ROOT
  Node 31991 (Gather) [consumed]
    Node 31992 (Aggregate) [consumed]
      Node 31993 (Hash Join) [consumed]
        Node 31994 (Seq Scan) [consumed] - LEAF
        Node 31995 (Hash) [consumed]
          Node 31996 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | 310134da | 31990 | 31991, 31992, 31993, 31994, 31995 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 0.06%
- Improvement: 7.28%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 31990 | Aggregate | 840.70 | 841.24 | 0.1% | pattern |
| 31996 | Seq Scan | 45.43 | 31.60 | 30.4% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 31996 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=200
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

### Step 2: Node 31990 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 310134da (Aggregate -> Gather -> Aggregate -> Hash Join -> [Seq Scan (Outer), Hash (Inner)] (Outer) (Outer) (Outer))
- **Consumes:** Nodes 31991, 31992, 31993, 31994, 31995
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=1
  - Aggregate_Outer_nt1=23
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=32
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0435
  - Aggregate_Outer_startup_cost=156338.6700
  - Aggregate_Outer_total_cost=156338.6800
  - Aggregate_np=0
  - Aggregate_nt=1
  - Aggregate_nt1=5
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=32
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=157339.2100
  - Aggregate_total_cost=157339.2200
  - Gather_Outer_np=0
  - Gather_Outer_nt=5
  - Gather_Outer_nt1=1
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=5
  - Gather_Outer_plan_width=32
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=5.0000
  - Gather_Outer_startup_cost=157338.6700
  - Gather_Outer_total_cost=157339.1800
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=23
  - HashJoin_Outer_nt1=22492
  - HashJoin_Outer_nt2=200
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=12
  - HashJoin_Outer_reltuples=0.0000
  - HashJoin_Outer_sel=0.0000
  - HashJoin_Outer_startup_cost=7672.1700
  - HashJoin_Outer_total_cost=156338.5000
  - Hash_Inner_np=0
  - Hash_Inner_nt=200
  - Hash_Inner_nt1=200
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=30
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=7669.6700
  - Hash_Inner_total_cost=7669.6700
  - SeqScan_Outer_np=112600
  - SeqScan_Outer_nt=22492
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=21
  - SeqScan_Outer_reltuples=6001215.0000
  - SeqScan_Outer_sel=0.0037
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=148607.2900
- **Output:** st=835.99, rt=841.24
