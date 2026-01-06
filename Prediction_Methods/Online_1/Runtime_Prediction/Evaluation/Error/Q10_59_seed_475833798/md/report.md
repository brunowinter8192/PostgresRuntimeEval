# Online Prediction Report

**Test Query:** Q10_59_seed_475833798
**Timestamp:** 2026-01-01 19:57:45

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 72.40%

## Phase C: Patterns in Query

- Total Patterns: 29

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 33781.0% | 113504.2307 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 147.6% | 141.6847 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 75.1% | 108.1438 |
| 2873b8c3 | Hash Join -> [Nested Loop -> [Seq Scan (... | 3 | 48 | 197.5% | 94.8003 |
| 30d6e09b | Hash Join -> [Hash Join -> [Nested Loop ... | 3 | 48 | 187.5% | 89.9904 |
| 7a51ce50 | Hash Join -> [Hash Join -> [Nested Loop ... | 4 | 48 | 187.5% | 89.9904 |
| 7d4e78be | Hash Join -> [Hash Join (Outer), Hash (I... | 2 | 48 | 187.5% | 89.9904 |
| 7bcfec22 | Limit -> Sort -> Aggregate (Outer) (Oute... | 3 | 72 | 56.1% | 40.3755 |
| e296a71f | Limit -> Sort (Outer) | 2 | 72 | 56.1% | 40.3755 |
| 25df29b5 | Limit -> Sort -> Aggregate -> Gather (Ou... | 4 | 48 | 69.7% | 33.4481 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 04a01b61 | Limit -> Sort -> Aggregate -> Gather -> ... | 5 | 24 | 71.1% | 17.0668 |
| 4cf43b83 | Limit -> Sort -> Aggregate -> Gather -> ... | 6 | 24 | 71.1% | 17.0668 |
| 843f0c9a | Limit -> Sort -> Aggregate -> Gather -> ... | 7 | 24 | 71.1% | 17.0668 |
| bef3a974 | Limit -> Sort -> Aggregate -> Gather -> ... | 8 | 24 | 71.1% | 17.0668 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 9.3% | 13.3894 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 72 | 4.0% | 2.9042 |
| 5437ac31 | Gather -> Hash Join (Outer) | 2 | 24 | 3.9% | 0.9438 |
| c9d5d7a8 | Gather -> Hash Join -> [Hash Join -> [Ne... | 5 | 24 | 3.9% | 0.9438 |
| dd59eb74 | Gather -> Hash Join -> [Hash Join -> [Ne... | 4 | 24 | 3.9% | 0.9438 |
| f4d53e95 | Gather -> Hash Join -> [Hash Join (Outer... | 3 | 24 | 3.9% | 0.9438 |
| 183d8335 | Aggregate -> Gather -> Hash Join -> [Has... | 4 | 24 | 2.6% | 0.6204 |
| 284f5967 | Aggregate -> Gather -> Hash Join (Outer)... | 3 | 24 | 2.6% | 0.6204 |
| 95d67a9e | Aggregate -> Gather -> Hash Join -> [Has... | 5 | 24 | 2.6% | 0.6204 |
| b8f6401f | Aggregate -> Gather -> Hash Join -> [Has... | 6 | 24 | 2.6% | 0.6204 |
| 313b221c | Sort -> Aggregate -> Gather -> Hash Join... | 6 | 24 | 2.1% | 0.5062 |
| 41017f66 | Sort -> Aggregate -> Gather -> Hash Join... | 5 | 24 | 2.1% | 0.5062 |
| 449d0c12 | Sort -> Aggregate -> Gather -> Hash Join... | 7 | 24 | 2.1% | 0.5062 |
| 6abf8d66 | Sort -> Aggregate -> Gather -> Hash Join... | 4 | 24 | 2.1% | 0.5062 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 1 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.92% |
| 2 | 2e0f44ef | 108.1438 | 0.0001% | ACCEPTED | 17.92% |
| 3 | 2873b8c3 | 121.6368 | 0.0000% | ACCEPTED | 17.92% |
| 4 | 30d6e09b | 42.9691 | N/A | REJECTED | 17.92% |
| 5 | 7a51ce50 | 42.9691 | 0.0000% | ACCEPTED | 17.92% |
| 6 | 7d4e78be | 59.2266 | N/A | REJECTED | 17.92% |
| 7 | 7bcfec22 | 40.3755 | 0.0356% | ACCEPTED | 17.89% |
| 8 | e296a71f | 40.2560 | N/A | REJECTED | 17.89% |
| 9 | 25df29b5 | 33.5860 | 9.8522% | ACCEPTED | 8.04% |
| 10 | 1d35fb97 | 19.4675 | 0.1205% | ACCEPTED | 7.92% |
| 11 | 4fc84c77 | 15.8334 | 0.6912% | ACCEPTED | 7.22% |
| 12 | b3a45093 | 5.7725 | N/A | SKIPPED_LOW_ERROR | 7.22% |
| 13 | 04a01b61 | 0.2016 | N/A | SKIPPED_LOW_ERROR | 7.22% |
| 14 | 4cf43b83 | 0.2016 | N/A | SKIPPED_LOW_ERROR | 7.22% |
| 15 | 843f0c9a | 0.2016 | N/A | SKIPPED_LOW_ERROR | 7.22% |
| 16 | bef3a974 | 0.2016 | N/A | SKIPPED_LOW_ERROR | 7.22% |
## Query Tree

```
Node 20722 (Limit) [PATTERN: 25df29b5] - ROOT
  Node 20723 (Sort) [consumed]
    Node 20724 (Aggregate) [consumed]
      Node 20725 (Gather) [consumed]
        Node 20726 (Hash Join) [PATTERN: 7a51ce50]
          Node 20727 (Hash Join) [consumed]
            Node 20728 (Nested Loop) [consumed]
              Node 20729 (Seq Scan) [consumed] - LEAF
              Node 20730 (Index Scan) [consumed] - LEAF
            Node 20731 (Hash) [consumed]
              Node 20732 (Seq Scan) [consumed] - LEAF
          Node 20733 (Hash) [consumed]
            Node 20734 (Seq Scan) [consumed] - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Hash Join -> [Hash Join -> [Ne | 7a51ce50 | 20726 | 20722, 20723, 20724, 20725, 20727, 20728, 20729, 20730, 20731, 20732, 20733, 20734 |
| Limit -> Sort -> Aggregate ->  | 25df29b5 | 20722 | 20723, 20724, 20725, 20726, 20727, 20728, 20729, 20730, 20731, 20732, 20733, 20734 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 1.16%
- Improvement: 71.24%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 20722 | Limit | 1141.61 | 1154.80 | 1.2% | pattern |
| 20726 | Hash Join | 1096.19 | 730.67 | 33.3% | pattern |

## Prediction Chain (Bottom-Up)

### Step 1: Node 20726 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 7a51ce50 (Hash Join -> [Hash Join -> [Nested Loop -> [Seq Scan (Outer), Index Scan (Inner)] (Outer), Hash -> Seq Scan (Outer) (Inner)] (Outer), Hash -> Seq Scan (Outer) (Inner)])
- **Consumes:** Nodes 20722, 20723, 20724, 20725, 20727, 20728, 20729, 20730, 20731, 20732, 20733, 20734
- **Input Features:**
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=18186
  - HashJoin_Outer_nt1=18186
  - HashJoin_Outer_nt2=62500
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=160
  - HashJoin_Outer_reltuples=0.0000
  - HashJoin_Outer_sel=0.0000
  - HashJoin_Outer_startup_cost=5006.6800
  - HashJoin_Outer_total_cost=80809.5000
  - HashJoin_np=0
  - HashJoin_nt=18186
  - HashJoin_nt1=18186
  - HashJoin_nt2=25
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=260
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0400
  - HashJoin_startup_cost=5008.2400
  - HashJoin_total_cost=80866.8900
  - Hash_Inner_np=0
  - Hash_Inner_nt=62500
  - Hash_Inner_nt1=62500
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=148
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=4225.0000
  - Hash_Inner_total_cost=4225.0000
  - IndexScan_Inner_np=112600
  - IndexScan_Inner_nt=1
  - IndexScan_Inner_nt1=0
  - IndexScan_Inner_nt2=0
  - IndexScan_Inner_parallel_workers=0
  - IndexScan_Inner_plan_width=16
  - IndexScan_Inner_reltuples=6001215.0000
  - IndexScan_Inner_sel=0.0000
  - IndexScan_Inner_startup_cost=0.4300
  - IndexScan_Inner_total_cost=2.3000
  - NestedLoop_Outer_np=0
  - NestedLoop_Outer_nt=18186
  - NestedLoop_Outer_nt1=18374
  - NestedLoop_Outer_nt2=1
  - NestedLoop_Outer_parallel_workers=0
  - NestedLoop_Outer_plan_width=16
  - NestedLoop_Outer_reltuples=0.0000
  - NestedLoop_Outer_sel=0.9898
  - NestedLoop_Outer_startup_cost=0.4300
  - NestedLoop_Outer_total_cost=75755.5100
  - SeqScan_Outer_np=3600
  - SeqScan_Outer_nt=62500
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=148
  - SeqScan_Outer_reltuples=150000.0000
  - SeqScan_Outer_sel=0.4167
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=4225.0000
- **Output:** st=37.23, rt=730.67

### Step 2: Node 20722 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 25df29b5 (Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer))
- **Consumes:** Nodes 20723, 20724, 20725, 20726, 20727, 20728, 20729, 20730, 20731, 20732, 20733, 20734
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=56376
  - Aggregate_Outer_nt1=56376
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=280
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=88209.1900
  - Aggregate_Outer_total_cost=88913.8900
  - Gather_Outer_np=0
  - Gather_Outer_nt=56376
  - Gather_Outer_nt1=18186
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=260
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.1000
  - Gather_Outer_startup_cost=6008.2400
  - Gather_Outer_total_cost=87504.4900
  - Limit_np=0
  - Limit_nt=20
  - Limit_nt1=56376
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=280
  - Limit_reltuples=0.0000
  - Limit_sel=0.0004
  - Limit_startup_cost=90414.0300
  - Limit_total_cost=90414.0800
  - Sort_Outer_np=0
  - Sort_Outer_nt=56376
  - Sort_Outer_nt1=56376
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=280
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=90414.0300
  - Sort_Outer_total_cost=90554.9700
- **Output:** st=1153.97, rt=1154.80
