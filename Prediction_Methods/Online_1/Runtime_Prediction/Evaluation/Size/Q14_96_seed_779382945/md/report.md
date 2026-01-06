# Online Prediction Report

**Test Query:** Q14_96_seed_779382945
**Timestamp:** 2026-01-01 18:02:20

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 7.20%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 33781.0% | 113504.2307 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 9.3% | 13.3894 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 96 | 8.0% | 7.7175 |
| 7524c54c | Aggregate -> Hash Join (Outer) | 2 | 76 | 6.9% | 5.2190 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 168 | 44967.0% | 75544.5822 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 96 | 13.0% | 12.4695 |
| 422ae017 | Aggregate -> Hash Join -> [Seq Scan (Out... | 3 | 76 | 6.9% | 5.2190 |
| 2e8f3f67 | Gather -> Aggregate -> Hash Join (Outer)... | 3 | 52 | 6.8% | 3.5252 |
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
| 0 | 895c6e8c | 75736.1626 | 0.0004% | ACCEPTED | 17.92% |
| 1 | 3aab37be | 94712.4752 | -0.0000% | REJECTED | 17.92% |
| 2 | 4fc84c77 | 13.3892 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 3 | 634cdbe2 | 7.7155 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 4 | 7524c54c | 5.0128 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 5 | f4cb205a | 41652.9228 | 0.0005% | ACCEPTED | 17.92% |
| 6 | a5f39f08 | 12.4675 | 1.7089% | ACCEPTED | 16.21% |
| 7 | 422ae017 | 2.5808 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 8 | efde8b38 | 1.7942 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 9 | 310134da | 1.7942 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 10 | f8295d8b | 1.0024 | N/A | SKIPPED_LOW_ERROR | 16.21% |
## Query Tree

```
Node 27435 (Aggregate) [PATTERN: a5f39f08] - ROOT
  Node 27436 (Gather) [consumed]
    Node 27437 (Aggregate) [consumed]
      Node 27438 (Hash Join) [PATTERN: f4cb205a]
        Node 27439 (Seq Scan) [consumed] - LEAF
        Node 27440 (Hash) [consumed]
          Node 27441 (Seq Scan) [consumed] - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Hash Join -> [Seq Scan (Outer) | f4cb205a | 27438 | 27435, 27436, 27437, 27439, 27440, 27441 |
| Aggregate -> Gather -> Aggrega | a5f39f08 | 27435 | 27436, 27437, 27438, 27439, 27440, 27441 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 1.18%
- Improvement: 6.01%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 27435 | Aggregate | 844.73 | 834.73 | 1.2% | pattern |
| 27438 | Hash Join | 822.67 | 397.08 | 51.7% | pattern |

## Prediction Chain (Bottom-Up)

### Step 1: Node 27438 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** f4cb205a (Hash Join -> [Seq Scan (Outer), Hash -> Seq Scan (Outer) (Inner)])
- **Consumes:** Nodes 27435, 27436, 27437, 27439, 27440, 27441
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=15395
  - HashJoin_nt1=15395
  - HashJoin_nt2=83333
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=33
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0000
  - HashJoin_startup_cost=6003.0000
  - HashJoin_total_cost=136647.0500
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
- **Output:** st=44.60, rt=397.08

### Step 2: Node 27435 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** a5f39f08 (Aggregate -> Gather -> Aggregate (Outer) (Outer))
- **Consumes:** Nodes 27436, 27437, 27438, 27439, 27440, 27441
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=1
  - Aggregate_Outer_nt1=15395
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=64
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0001
  - Aggregate_Outer_startup_cost=136916.4700
  - Aggregate_Outer_total_cost=136916.4800
  - Aggregate_np=0
  - Aggregate_nt=1
  - Aggregate_nt1=5
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=32
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=137917.0400
  - Aggregate_total_cost=137917.0500
  - Gather_Outer_np=0
  - Gather_Outer_nt=5
  - Gather_Outer_nt1=1
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=5
  - Gather_Outer_plan_width=64
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=5.0000
  - Gather_Outer_startup_cost=137916.4700
  - Gather_Outer_total_cost=137916.9800
- **Output:** st=829.18, rt=834.73
