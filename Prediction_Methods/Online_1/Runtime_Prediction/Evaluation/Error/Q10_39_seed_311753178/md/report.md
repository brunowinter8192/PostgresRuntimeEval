# Online Prediction Report

**Test Query:** Q10_39_seed_311753178
**Timestamp:** 2026-01-11 19:33:30

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 72.03%

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
| 12 | b3a45093 | 5.7725 | 0.4105% | ACCEPTED | 6.81% |
| 13 | 04a01b61 | 0.2016 | 0.0045% | ACCEPTED | 6.81% |
| 14 | 4cf43b83 | 0.1864 | -0.0000% | REJECTED | 6.81% |
| 15 | 843f0c9a | 0.1864 | -0.0000% | REJECTED | 6.81% |
| 16 | bef3a974 | 0.1864 | -0.0000% | REJECTED | 6.81% |
## Query Tree

```
Node 20436 (Limit) [PATTERN: 04a01b61] - ROOT
  Node 20437 (Sort) [consumed]
    Node 20438 (Aggregate) [consumed]
      Node 20439 (Gather) [consumed]
        Node 20440 (Hash Join) [consumed]
          Node 20441 (Hash Join) [PATTERN: 2873b8c3]
            Node 20442 (Nested Loop) [consumed]
              Node 20443 (Seq Scan) [consumed] - LEAF
              Node 20444 (Index Scan) [consumed] - LEAF
            Node 20445 (Hash) [consumed]
              Node 20446 (Seq Scan) [consumed] - LEAF
          Node 20447 (Hash)
            Node 20448 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 04a01b61 | 20436 | 20437, 20438, 20439, 20440, 20441, 20442, 20443, 20444, 20445, 20446 |
| Hash Join -> [Nested Loop -> [ | 2873b8c3 | 20441 | 20436, 20437, 20438, 20439, 20440, 20442, 20443, 20444, 20445, 20446 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 0.61%
- Improvement: 71.42%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 20436 | Limit | 1144.16 | 1151.14 | 0.6% | pattern |
| 20441 | Hash Join | 1091.48 | 725.01 | 33.6% | pattern |
| 20447 | Hash | 0.01 | 14.54 | 111744.0% | operator |
| 20448 | Seq Scan | 0.01 | 7.19 | 71844.7% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 20448 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=1
  - nt=25
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=25.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=1.2500
- **Output:** st=0.06, rt=7.19

### Step 2: Node 20441 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 2873b8c3 (Hash Join -> [Nested Loop -> [Seq Scan (Outer), Index Scan (Inner)] (Outer), Hash -> Seq Scan (Outer) (Inner)])
- **Consumes:** Nodes 20436, 20437, 20438, 20439, 20440, 20442, 20443, 20444, 20445, 20446
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=17761
  - HashJoin_nt1=17761
  - HashJoin_nt2=62500
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=160
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0000
  - HashJoin_startup_cost=5006.6800
  - HashJoin_total_cost=80406.2200
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
  - IndexScan_Inner_total_cost=2.3300
  - NestedLoop_Outer_np=0
  - NestedLoop_Outer_nt=17761
  - NestedLoop_Outer_nt1=17945
  - NestedLoop_Outer_nt2=1
  - NestedLoop_Outer_parallel_workers=0
  - NestedLoop_Outer_plan_width=16
  - NestedLoop_Outer_reltuples=0.0000
  - NestedLoop_Outer_sel=0.9897
  - NestedLoop_Outer_startup_cost=0.4300
  - NestedLoop_Outer_total_cost=75353.3500
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
- **Output:** st=36.96, rt=725.01

### Step 3: Node 20447 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=25
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=7.1945
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0613
  - st2=0.0000
  - startup_cost=1.2500
  - total_cost=1.2500
- **Output:** st=14.54, rt=14.54

### Step 4: Node 20436 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 04a01b61 (Limit -> Sort -> Aggregate -> Gather -> Hash Join (Outer) (Outer) (Outer) (Outer))
- **Consumes:** Nodes 20437, 20438, 20439, 20440, 20441, 20442, 20443, 20444, 20445, 20446
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=55059
  - Aggregate_Outer_nt1=55059
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=280
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=87656.4500
  - Aggregate_Outer_total_cost=88344.6800
  - Gather_Outer_np=0
  - Gather_Outer_nt=55059
  - Gather_Outer_nt1=17761
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=260
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.1000
  - Gather_Outer_startup_cost=6008.2400
  - Gather_Outer_total_cost=86968.2100
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=17761
  - HashJoin_Outer_nt1=17761
  - HashJoin_Outer_nt2=25
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=260
  - HashJoin_Outer_reltuples=0.0000
  - HashJoin_Outer_sel=0.0400
  - HashJoin_Outer_startup_cost=5008.2400
  - HashJoin_Outer_total_cost=80462.3100
  - Limit_np=0
  - Limit_nt=20
  - Limit_nt1=55059
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=280
  - Limit_reltuples=0.0000
  - Limit_sel=0.0004
  - Limit_startup_cost=89809.7800
  - Limit_total_cost=89809.8300
  - Sort_Outer_np=0
  - Sort_Outer_nt=55059
  - Sort_Outer_nt1=55059
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=280
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=89809.7800
  - Sort_Outer_total_cost=89947.4300
- **Output:** st=1150.37, rt=1151.14
