# Online Prediction Report

**Test Query:** Q14_26_seed_205100775
**Timestamp:** 2026-01-11 19:46:16

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 11.52%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 33781.0% | 113504.2307 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 168 | 44967.0% | 75544.5822 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 9.3% | 13.3894 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 96 | 13.0% | 12.4695 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 96 | 8.0% | 7.7175 |
| 310134da | Aggregate -> Gather -> Aggregate -> Hash... | 5 | 52 | 10.3% | 5.3353 |
| efde8b38 | Aggregate -> Gather -> Aggregate -> Hash... | 4 | 52 | 10.3% | 5.3353 |
| 422ae017 | Aggregate -> Hash Join -> [Seq Scan (Out... | 3 | 76 | 6.9% | 5.2190 |
| 7524c54c | Aggregate -> Hash Join (Outer) | 2 | 76 | 6.9% | 5.2190 |
| f8295d8b | Aggregate -> Gather -> Aggregate -> Hash... | 6 | 48 | 9.3% | 4.4470 |
| 2e8f3f67 | Gather -> Aggregate -> Hash Join (Outer)... | 3 | 52 | 6.8% | 3.5252 |
| af27a52b | Gather -> Aggregate -> Hash Join -> [Seq... | 4 | 52 | 6.8% | 3.5252 |
| 4e54d684 | Aggregate -> Hash Join -> [Seq Scan (Out... | 4 | 48 | 7.1% | 3.3909 |
| 422b9b8c | Gather -> Aggregate -> Hash Join -> [Seq... | 5 | 48 | 6.0% | 2.8904 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 1 | 895c6e8c | 75736.1626 | 0.0004% | ACCEPTED | 17.92% |
| 2 | f4cb205a | 41652.9228 | 0.0005% | ACCEPTED | 17.92% |
| 3 | 4fc84c77 | 13.3874 | 0.7524% | ACCEPTED | 17.17% |
| 4 | a5f39f08 | 7.4789 | 0.9566% | ACCEPTED | 16.21% |
| 5 | 422ae017 | 2.5808 | 0.0024% | ACCEPTED | 16.21% |
| 6 | 310134da | 1.7942 | 0.0191% | ACCEPTED | 16.19% |
| 7 | efde8b38 | 2.2456 | N/A | REJECTED | 16.19% |
| 8 | 7524c54c | 1.6899 | N/A | REJECTED | 16.19% |
| 9 | f8295d8b | 0.8975 | 0.0064% | ACCEPTED | 16.19% |
## Query Tree

```
Node 26896 (Aggregate) [PATTERN: f8295d8b] - ROOT
  Node 26897 (Gather) [consumed]
    Node 26898 (Aggregate) [consumed]
      Node 26899 (Hash Join) [consumed]
        Node 26900 (Seq Scan) [consumed] - LEAF
        Node 26901 (Hash) [consumed]
          Node 26902 (Seq Scan) [consumed] - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | f8295d8b | 26896 | 26897, 26898, 26899, 26900, 26901, 26902 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 1.33%
- Improvement: 10.20%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 26896 | Aggregate | 811.96 | 822.73 | 1.3% | pattern |

## Prediction Chain (Bottom-Up)

### Step 1: Node 26896 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** f8295d8b (Aggregate -> Gather -> Aggregate -> Hash Join -> [Seq Scan (Outer), Hash -> Seq Scan (Outer) (Inner)] (Outer) (Outer) (Outer))
- **Consumes:** Nodes 26897, 26898, 26899, 26900, 26901, 26902
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=1
  - Aggregate_Outer_nt1=15122
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=64
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0001
  - Aggregate_Outer_startup_cost=136910.9800
  - Aggregate_Outer_total_cost=136910.9900
  - Aggregate_np=0
  - Aggregate_nt=1
  - Aggregate_nt1=5
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=32
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=137911.5400
  - Aggregate_total_cost=137911.5600
  - Gather_Outer_np=0
  - Gather_Outer_nt=5
  - Gather_Outer_nt1=1
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=5
  - Gather_Outer_plan_width=64
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=5.0000
  - Gather_Outer_startup_cost=137910.9800
  - Gather_Outer_total_cost=137911.4900
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=15122
  - HashJoin_Outer_nt1=15122
  - HashJoin_Outer_nt2=83333
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=33
  - HashJoin_Outer_reltuples=0.0000
  - HashJoin_Outer_sel=0.0000
  - HashJoin_Outer_startup_cost=6003.0000
  - HashJoin_Outer_total_cost=136646.3400
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
  - SeqScan_Outer_np=4128
  - SeqScan_Outer_nt=83333
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=25
  - SeqScan_Outer_reltuples=200000.0000
  - SeqScan_Outer_sel=0.4167
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=4961.3300
- **Output:** st=816.84, rt=822.73
