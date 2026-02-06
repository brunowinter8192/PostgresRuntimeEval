# Online Prediction Report

**Test Query:** Q10_3_seed_16408062
**Timestamp:** 2026-01-18 19:32:11

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17891 | Operator + Pattern Training |
| Training_Test | 4478 | Pattern Selection Eval |
| Training | 22369 | Final Model Training |
| Test | 1950 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 83.41%

## Phase C: Patterns in Query

- Total Patterns: 29

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 360 | 34236.0% | 123249.7776 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 210 | 15.2% | 31.9214 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 150 | 10.6% | 15.8901 |
| e296a71f | Limit -> Sort (Outer) | 2 | 60 | 48.4% | 29.0440 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 150 | 87.4% | 131.1122 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 90 | 195.4% | 175.8467 |
| 7bcfec22 | Limit -> Sort -> Aggregate (Outer) (Oute... | 3 | 60 | 48.4% | 29.0440 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 60 | 5.3% | 3.1940 |
| 7d4e78be | Hash Join -> [Hash Join (Outer), Hash (I... | 2 | 30 | 375.5% | 112.6472 |
| 25df29b5 | Limit -> Sort -> Aggregate -> Gather (Ou... | 4 | 30 | 68.7% | 20.6018 |
| 2873b8c3 | Hash Join -> [Nested Loop -> [Seq Scan (... | 3 | 30 | 391.6% | 117.4853 |
| 30d6e09b | Hash Join -> [Hash Join -> [Nested Loop ... | 3 | 30 | 375.5% | 112.6472 |
| 7a51ce50 | Hash Join -> [Hash Join -> [Nested Loop ... | 4 | 30 | 375.5% | 112.6472 |
| 04a01b61 | Limit -> Sort -> Aggregate -> Gather -> ... | 5 | 0 | - | - |
| 4cf43b83 | Limit -> Sort -> Aggregate -> Gather -> ... | 6 | 0 | - | - |
| 843f0c9a | Limit -> Sort -> Aggregate -> Gather -> ... | 7 | 0 | - | - |
| bef3a974 | Limit -> Sort -> Aggregate -> Gather -> ... | 8 | 0 | - | - |
| 6abf8d66 | Sort -> Aggregate -> Gather -> Hash Join... | 4 | 0 | - | - |
| 41017f66 | Sort -> Aggregate -> Gather -> Hash Join... | 5 | 0 | - | - |
| 313b221c | Sort -> Aggregate -> Gather -> Hash Join... | 6 | 0 | - | - |
| 449d0c12 | Sort -> Aggregate -> Gather -> Hash Join... | 7 | 0 | - | - |
| 284f5967 | Aggregate -> Gather -> Hash Join (Outer)... | 3 | 0 | - | - |
| 183d8335 | Aggregate -> Gather -> Hash Join -> [Has... | 4 | 0 | - | - |
| 95d67a9e | Aggregate -> Gather -> Hash Join -> [Has... | 5 | 0 | - | - |
| b8f6401f | Aggregate -> Gather -> Hash Join -> [Has... | 6 | 0 | - | - |
| 5437ac31 | Gather -> Hash Join (Outer) | 2 | 0 | - | - |
| f4d53e95 | Gather -> Hash Join -> [Hash Join (Outer... | 3 | 0 | - | - |
| dd59eb74 | Gather -> Hash Join -> [Hash Join -> [Ne... | 4 | 0 | - | - |
| c9d5d7a8 | Gather -> Hash Join -> [Hash Join -> [Ne... | 5 | 0 | - | - |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 3aab37be | 123249.7776 | -0.0000% | REJECTED | 13.80% |
| 1 | 1d35fb97 | 31.9214 | 0.0688% | ACCEPTED | 13.73% |
| 2 | 4fc84c77 | 15.8901 | 1.7948% | ACCEPTED | 11.94% |
| 3 | e296a71f | 29.0440 | N/A | REJECTED | 11.94% |
| 4 | 2e0f44ef | 131.1122 | 0.0001% | ACCEPTED | 11.94% |
| 5 | c53c4396 | 175.8467 | -0.0001% | REJECTED | 11.94% |
| 6 | 7bcfec22 | 29.0440 | 0.0384% | ACCEPTED | 11.90% |
| 7 | b3a45093 | 3.1940 | N/A | SKIPPED_LOW_ERROR | 11.90% |
| 8 | 7d4e78be | 112.6472 | N/A | REJECTED | 11.90% |
| 9 | 25df29b5 | 20.6018 | 5.1969% | ACCEPTED | 6.70% |
| 10 | 2873b8c3 | 117.4853 | N/A | REJECTED | 6.70% |
| 11 | 30d6e09b | 112.6472 | N/A | REJECTED | 6.70% |
| 12 | 7a51ce50 | 112.6472 | N/A | REJECTED | 6.70% |
## Query Tree

```
Node 20449 (Limit) [PATTERN: 25df29b5] - ROOT
  Node 20450 (Sort) [consumed]
    Node 20451 (Aggregate) [consumed]
      Node 20452 (Gather) [consumed]
        Node 20453 (Hash Join)
          Node 20454 (Hash Join) [PATTERN: 2e0f44ef]
            Node 20455 (Nested Loop) [consumed]
              Node 20456 (Seq Scan) - LEAF
              Node 20457 (Index Scan) - LEAF
            Node 20458 (Hash) [consumed]
              Node 20459 (Seq Scan) - LEAF
          Node 20460 (Hash)
            Node 20461 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 25df29b5 | 20449 | 20450, 20451, 20452, 20454, 20455, 20458 |
| Hash Join -> [Nested Loop (Out | 2e0f44ef | 20454 | 20449, 20450, 20451, 20452, 20455, 20458 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 3.59%
- Improvement: 79.82%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 20449 | Limit | 1157.94 | 1199.47 | 3.6% | pattern |
| 20453 | Hash Join | 1109.59 | 1095.55 | 1.3% | operator |
| 20454 | Hash Join | 1106.68 | 1120.19 | 1.2% | pattern |
| 20460 | Hash | 0.02 | 15.71 | 98092.3% | operator |
| 20461 | Seq Scan | 0.01 | 6.98 | 58055.9% | operator |
| 20456 | Seq Scan | 163.48 | 159.74 | 2.3% | operator |
| 20457 | Index Scan | 0.06 | -0.52 | 922.6% | operator |
| 20459 | Seq Scan | 27.05 | 26.64 | 1.5% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 20456 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=18371
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0122
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=33394.0600
- **Output:** st=-0.55, rt=159.74

### Step 2: Node 20457 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=1
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=16
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.4300
  - total_cost=2.3000
- **Output:** st=0.03, rt=-0.52

### Step 3: Node 20459 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=3600
  - nt=62500
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=148
  - reltuples=150000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.4167
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=4225.0000
- **Output:** st=-10.03, rt=26.64

### Step 4: Node 20461 (Seq Scan) - LEAF

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
- **Output:** st=0.44, rt=6.98

### Step 5: Node 20454 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 2e0f44ef (Hash Join -> [Nested Loop (Outer), Hash (Inner)])
- **Consumes:** Nodes 20449, 20450, 20451, 20452, 20455, 20458
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=18183
  - HashJoin_nt1=18183
  - HashJoin_nt2=62500
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=160
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0000
  - HashJoin_startup_cost=5006.6800
  - HashJoin_total_cost=80807.0600
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
  - NestedLoop_Outer_np=0
  - NestedLoop_Outer_nt=18183
  - NestedLoop_Outer_nt1=18371
  - NestedLoop_Outer_nt2=1
  - NestedLoop_Outer_parallel_workers=0
  - NestedLoop_Outer_plan_width=16
  - NestedLoop_Outer_reltuples=0.0000
  - NestedLoop_Outer_sel=0.9898
  - NestedLoop_Outer_startup_cost=0.4300
  - NestedLoop_Outer_total_cost=75753.0800
- **Output:** st=51.86, rt=1120.19

### Step 6: Node 20460 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=25
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=6.9787
  - rt2=0.0000
  - sel=1.0000
  - st1=0.4364
  - st2=0.0000
  - startup_cost=1.2500
  - total_cost=1.2500
- **Output:** st=15.71, rt=15.71

### Step 7: Node 20453 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18183
  - nt1=18183
  - nt2=25
  - parallel_workers=0
  - plan_width=260
  - reltuples=0.0000
  - rt1=1120.1863
  - rt2=15.7108
  - sel=0.0400
  - st1=51.8597
  - st2=15.7100
  - startup_cost=5008.2400
  - total_cost=80864.4400
- **Output:** st=54.21, rt=1095.55

### Step 8: Node 20449 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 25df29b5 (Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer))
- **Consumes:** Nodes 20450, 20451, 20452, 20454, 20455, 20458
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=56366
  - Aggregate_Outer_nt1=56366
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=280
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=88205.6200
  - Aggregate_Outer_total_cost=88910.1900
  - Gather_Outer_np=0
  - Gather_Outer_nt=56366
  - Gather_Outer_nt1=18183
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=260
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.0999
  - Gather_Outer_startup_cost=6008.2400
  - Gather_Outer_total_cost=87501.0400
  - Limit_np=0
  - Limit_nt=20
  - Limit_nt1=56366
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=280
  - Limit_reltuples=0.0000
  - Limit_sel=0.0004
  - Limit_startup_cost=90410.0700
  - Limit_total_cost=90410.1200
  - Sort_Outer_np=0
  - Sort_Outer_nt=56366
  - Sort_Outer_nt1=56366
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=280
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=90410.0700
  - Sort_Outer_total_cost=90550.9900
- **Output:** st=1197.42, rt=1199.47
