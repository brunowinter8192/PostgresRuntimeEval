# Online Prediction Report

**Test Query:** Q10_71_seed_574282170
**Timestamp:** 2026-01-01 18:55:47

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 70.27%

## Phase C: Patterns in Query

- Total Patterns: 29

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 33781.0% | 113504.2307 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 9.3% | 13.3894 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 75.1% | 108.1438 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 147.6% | 141.6847 |
| e296a71f | Limit -> Sort (Outer) | 2 | 72 | 56.1% | 40.3755 |
| 7bcfec22 | Limit -> Sort -> Aggregate (Outer) (Oute... | 3 | 72 | 56.1% | 40.3755 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 72 | 4.0% | 2.9042 |
| 7d4e78be | Hash Join -> [Hash Join (Outer), Hash (I... | 2 | 48 | 187.5% | 89.9904 |
| 30d6e09b | Hash Join -> [Hash Join -> [Nested Loop ... | 3 | 48 | 187.5% | 89.9904 |
| 2873b8c3 | Hash Join -> [Nested Loop -> [Seq Scan (... | 3 | 48 | 197.5% | 94.8003 |
| 25df29b5 | Limit -> Sort -> Aggregate -> Gather (Ou... | 4 | 48 | 69.7% | 33.4481 |
| 7a51ce50 | Hash Join -> [Hash Join -> [Nested Loop ... | 4 | 48 | 187.5% | 89.9904 |
| 5437ac31 | Gather -> Hash Join (Outer) | 2 | 24 | 3.9% | 0.9438 |
| 284f5967 | Aggregate -> Gather -> Hash Join (Outer)... | 3 | 24 | 2.6% | 0.6204 |
| f4d53e95 | Gather -> Hash Join -> [Hash Join (Outer... | 3 | 24 | 3.9% | 0.9438 |
| 6abf8d66 | Sort -> Aggregate -> Gather -> Hash Join... | 4 | 24 | 2.1% | 0.5062 |
| 183d8335 | Aggregate -> Gather -> Hash Join -> [Has... | 4 | 24 | 2.6% | 0.6204 |
| dd59eb74 | Gather -> Hash Join -> [Hash Join -> [Ne... | 4 | 24 | 3.9% | 0.9438 |
| 04a01b61 | Limit -> Sort -> Aggregate -> Gather -> ... | 5 | 24 | 71.1% | 17.0668 |
| 41017f66 | Sort -> Aggregate -> Gather -> Hash Join... | 5 | 24 | 2.1% | 0.5062 |
| 95d67a9e | Aggregate -> Gather -> Hash Join -> [Has... | 5 | 24 | 2.6% | 0.6204 |
| c9d5d7a8 | Gather -> Hash Join -> [Hash Join -> [Ne... | 5 | 24 | 3.9% | 0.9438 |
| 4cf43b83 | Limit -> Sort -> Aggregate -> Gather -> ... | 6 | 24 | 71.1% | 17.0668 |
| 313b221c | Sort -> Aggregate -> Gather -> Hash Join... | 6 | 24 | 2.1% | 0.5062 |
| b8f6401f | Aggregate -> Gather -> Hash Join -> [Has... | 6 | 24 | 2.6% | 0.6204 |
| 843f0c9a | Limit -> Sort -> Aggregate -> Gather -> ... | 7 | 24 | 71.1% | 17.0668 |
| 449d0c12 | Sort -> Aggregate -> Gather -> Hash Join... | 7 | 24 | 2.1% | 0.5062 |
| bef3a974 | Limit -> Sort -> Aggregate -> Gather -> ... | 8 | 24 | 71.1% | 17.0668 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 1 | 1d35fb97 | 26.4017 | 0.1167% | ACCEPTED | 17.81% |
| 2 | 4fc84c77 | 15.8334 | 0.6912% | ACCEPTED | 17.12% |
| 3 | 2e0f44ef | 108.1438 | 0.0001% | ACCEPTED | 17.12% |
| 4 | c53c4396 | 8.0758 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 5 | e296a71f | 40.3884 | N/A | REJECTED | 17.12% |
| 6 | 7bcfec22 | 40.3884 | 0.0394% | ACCEPTED | 17.08% |
| 7 | b3a45093 | 5.7725 | N/A | SKIPPED_LOW_ERROR | 17.08% |
| 8 | 7d4e78be | 83.6779 | N/A | REJECTED | 17.08% |
| 9 | 30d6e09b | 83.6779 | N/A | REJECTED | 17.08% |
| 10 | 2873b8c3 | 121.6368 | N/A | REJECTED | 17.08% |
| 11 | 25df29b5 | 33.5860 | 9.8522% | ACCEPTED | 7.22% |
| 12 | 7a51ce50 | 83.6779 | N/A | REJECTED | 7.22% |
| 13 | 04a01b61 | 0.2016 | N/A | SKIPPED_LOW_ERROR | 7.22% |
| 14 | 4cf43b83 | 0.2016 | N/A | SKIPPED_LOW_ERROR | 7.22% |
| 15 | 843f0c9a | 0.2016 | N/A | SKIPPED_LOW_ERROR | 7.22% |
| 16 | bef3a974 | 0.2016 | N/A | SKIPPED_LOW_ERROR | 7.22% |
## Query Tree

```
Node 20904 (Limit) [PATTERN: 25df29b5] - ROOT
  Node 20905 (Sort) [consumed]
    Node 20906 (Aggregate) [consumed]
      Node 20907 (Gather) [consumed]
        Node 20908 (Hash Join)
          Node 20909 (Hash Join) [PATTERN: 2e0f44ef]
            Node 20910 (Nested Loop) [consumed]
              Node 20911 (Seq Scan) - LEAF
              Node 20912 (Index Scan) - LEAF
            Node 20913 (Hash) [consumed]
              Node 20914 (Seq Scan) - LEAF
          Node 20915 (Hash)
            Node 20916 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 25df29b5 | 20904 | 20905, 20906, 20907, 20909, 20910, 20913 |
| Hash Join -> [Nested Loop (Out | 2e0f44ef | 20909 | 20904, 20905, 20906, 20907, 20910, 20913 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 0.09%
- Improvement: 70.18%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 20904 | Limit | 1155.84 | 1154.80 | 0.1% | pattern |
| 20908 | Hash Join | 1106.30 | 1087.34 | 1.7% | operator |
| 20909 | Hash Join | 1103.41 | 1101.74 | 0.2% | pattern |
| 20915 | Hash | 0.01 | 14.54 | 96831.4% | operator |
| 20916 | Seq Scan | 0.01 | 7.19 | 65304.3% | operator |
| 20911 | Seq Scan | 166.99 | 162.03 | 3.0% | operator |
| 20912 | Index Scan | 0.06 | -0.02 | 129.5% | operator |
| 20914 | Seq Scan | 27.06 | 29.69 | 9.7% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 20911 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=18372
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
- **Output:** st=0.15, rt=162.03

### Step 2: Node 20912 (Index Scan) - LEAF

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
- **Output:** st=0.06, rt=-0.02

### Step 3: Node 20914 (Seq Scan) - LEAF

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
- **Output:** st=0.06, rt=29.69

### Step 4: Node 20916 (Seq Scan) - LEAF

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

### Step 5: Node 20909 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 2e0f44ef (Hash Join -> [Nested Loop (Outer), Hash (Inner)])
- **Consumes:** Nodes 20904, 20905, 20906, 20907, 20910, 20913
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=18184
  - HashJoin_nt1=18184
  - HashJoin_nt2=62500
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=160
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0000
  - HashJoin_startup_cost=5006.6800
  - HashJoin_total_cost=80807.8600
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
  - NestedLoop_Outer_nt=18184
  - NestedLoop_Outer_nt1=18372
  - NestedLoop_Outer_nt2=1
  - NestedLoop_Outer_parallel_workers=0
  - NestedLoop_Outer_plan_width=16
  - NestedLoop_Outer_reltuples=0.0000
  - NestedLoop_Outer_sel=0.9898
  - NestedLoop_Outer_startup_cost=0.4300
  - NestedLoop_Outer_total_cost=75753.8800
- **Output:** st=37.52, rt=1101.74

### Step 6: Node 20915 (Hash)

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

### Step 7: Node 20908 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18184
  - nt1=18184
  - nt2=25
  - parallel_workers=0
  - plan_width=260
  - reltuples=0.0000
  - rt1=1101.7371
  - rt2=14.5397
  - sel=0.0400
  - st1=37.5164
  - st2=14.5393
  - startup_cost=5008.2400
  - total_cost=80865.2500
- **Output:** st=39.30, rt=1087.34

### Step 8: Node 20904 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 25df29b5 (Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer))
- **Consumes:** Nodes 20905, 20906, 20907, 20909, 20910, 20913
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=56369
  - Aggregate_Outer_nt1=56369
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=280
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=88206.7600
  - Aggregate_Outer_total_cost=88911.3700
  - Gather_Outer_np=0
  - Gather_Outer_nt=56369
  - Gather_Outer_nt1=18184
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=260
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.0999
  - Gather_Outer_startup_cost=6008.2400
  - Gather_Outer_total_cost=87502.1500
  - Limit_np=0
  - Limit_nt=20
  - Limit_nt1=56369
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=280
  - Limit_reltuples=0.0000
  - Limit_sel=0.0004
  - Limit_startup_cost=90411.3300
  - Limit_total_cost=90411.3800
  - Sort_Outer_np=0
  - Sort_Outer_nt=56369
  - Sort_Outer_nt1=56369
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=280
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=90411.3300
  - Sort_Outer_total_cost=90552.2500
- **Output:** st=1153.97, rt=1154.80
