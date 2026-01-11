# Online Prediction Report

**Test Query:** Q10_80_seed_648118449
**Timestamp:** 2026-01-11 17:55:25

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 69.79%

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
| 25df29b5 | Limit -> Sort -> Aggregate -> Gather (Ou... | 4 | 48 | 69.7% | 33.4481 |
| 2873b8c3 | Hash Join -> [Nested Loop -> [Seq Scan (... | 3 | 48 | 197.5% | 94.8003 |
| 30d6e09b | Hash Join -> [Hash Join -> [Nested Loop ... | 3 | 48 | 187.5% | 89.9904 |
| 7a51ce50 | Hash Join -> [Hash Join -> [Nested Loop ... | 4 | 48 | 187.5% | 89.9904 |
| 5437ac31 | Gather -> Hash Join (Outer) | 2 | 24 | 3.9% | 0.9438 |
| 284f5967 | Aggregate -> Gather -> Hash Join (Outer)... | 3 | 24 | 2.6% | 0.6204 |
| 6abf8d66 | Sort -> Aggregate -> Gather -> Hash Join... | 4 | 24 | 2.1% | 0.5062 |
| f4d53e95 | Gather -> Hash Join -> [Hash Join (Outer... | 3 | 24 | 3.9% | 0.9438 |
| 04a01b61 | Limit -> Sort -> Aggregate -> Gather -> ... | 5 | 24 | 71.1% | 17.0668 |
| 183d8335 | Aggregate -> Gather -> Hash Join -> [Has... | 4 | 24 | 2.6% | 0.6204 |
| 41017f66 | Sort -> Aggregate -> Gather -> Hash Join... | 5 | 24 | 2.1% | 0.5062 |
| 4cf43b83 | Limit -> Sort -> Aggregate -> Gather -> ... | 6 | 24 | 71.1% | 17.0668 |
| dd59eb74 | Gather -> Hash Join -> [Hash Join -> [Ne... | 4 | 24 | 3.9% | 0.9438 |
| 95d67a9e | Aggregate -> Gather -> Hash Join -> [Has... | 5 | 24 | 2.6% | 0.6204 |
| 313b221c | Sort -> Aggregate -> Gather -> Hash Join... | 6 | 24 | 2.1% | 0.5062 |
| 843f0c9a | Limit -> Sort -> Aggregate -> Gather -> ... | 7 | 24 | 71.1% | 17.0668 |
| c9d5d7a8 | Gather -> Hash Join -> [Hash Join -> [Ne... | 5 | 24 | 3.9% | 0.9438 |
| b8f6401f | Aggregate -> Gather -> Hash Join -> [Has... | 6 | 24 | 2.6% | 0.6204 |
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
| 2 | 4fc84c77 | 13.3894 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 3 | 2e0f44ef | 108.1438 | 0.0001% | ACCEPTED | 17.81% |
| 4 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.81% |
| 5 | e296a71f | 40.3755 | N/A | REJECTED | 17.81% |
| 6 | 7bcfec22 | 40.3755 | 0.0394% | ACCEPTED | 17.77% |
| 7 | b3a45093 | 2.9042 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 8 | 7d4e78be | 89.9904 | N/A | REJECTED | 17.77% |
| 9 | 25df29b5 | 33.4481 | 9.8522% | ACCEPTED | 7.92% |
| 10 | 2873b8c3 | 94.8003 | N/A | REJECTED | 7.92% |
| 11 | 30d6e09b | 89.9904 | N/A | REJECTED | 7.92% |
| 12 | 7a51ce50 | 89.9904 | N/A | REJECTED | 7.92% |
| 13 | 5437ac31 | 0.9438 | N/A | SKIPPED_LOW_ERROR | 7.92% |
| 14 | 284f5967 | 0.6204 | N/A | SKIPPED_LOW_ERROR | 7.92% |
| 15 | 6abf8d66 | 0.5062 | N/A | SKIPPED_LOW_ERROR | 7.92% |
| 16 | f4d53e95 | 0.9438 | N/A | SKIPPED_LOW_ERROR | 7.92% |
| 17 | 04a01b61 | 17.0668 | 0.0045% | ACCEPTED | 7.91% |
| 18 | 183d8335 | 0.6204 | N/A | SKIPPED_LOW_ERROR | 7.91% |
| 19 | 41017f66 | 0.5062 | N/A | SKIPPED_LOW_ERROR | 7.91% |
| 20 | 4cf43b83 | 17.0668 | -0.0000% | REJECTED | 7.91% |
| 21 | dd59eb74 | 0.9438 | N/A | SKIPPED_LOW_ERROR | 7.91% |
| 22 | 95d67a9e | 0.6204 | N/A | SKIPPED_LOW_ERROR | 7.91% |
| 23 | 313b221c | 0.5062 | N/A | SKIPPED_LOW_ERROR | 7.91% |
| 24 | 843f0c9a | 17.0668 | -0.0000% | REJECTED | 7.91% |
| 25 | c9d5d7a8 | 0.9438 | N/A | SKIPPED_LOW_ERROR | 7.91% |
| 26 | b8f6401f | 0.6204 | N/A | SKIPPED_LOW_ERROR | 7.91% |
| 27 | 449d0c12 | 0.5062 | N/A | SKIPPED_LOW_ERROR | 7.91% |
| 28 | bef3a974 | 17.0668 | -0.0000% | REJECTED | 7.91% |
## Query Tree

```
Node 21034 (Limit) [PATTERN: 04a01b61] - ROOT
  Node 21035 (Sort) [consumed]
    Node 21036 (Aggregate) [consumed]
      Node 21037 (Gather) [consumed]
        Node 21038 (Hash Join) [consumed]
          Node 21039 (Hash Join) [PATTERN: 2e0f44ef]
            Node 21040 (Nested Loop) [consumed]
              Node 21041 (Seq Scan) - LEAF
              Node 21042 (Index Scan) - LEAF
            Node 21043 (Hash) [consumed]
              Node 21044 (Seq Scan) - LEAF
          Node 21045 (Hash)
            Node 21046 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 04a01b61 | 21034 | 21035, 21036, 21037, 21038, 21039, 21040, 21043 |
| Hash Join -> [Nested Loop (Out | 2e0f44ef | 21039 | 21034, 21035, 21036, 21037, 21038, 21040, 21043 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 0.69%
- Improvement: 69.10%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 21034 | Limit | 1159.14 | 1151.16 | 0.7% | pattern |
| 21039 | Hash Join | 1106.91 | 1101.75 | 0.5% | pattern |
| 21045 | Hash | 0.02 | 14.54 | 80676.2% | operator |
| 21046 | Seq Scan | 0.01 | 7.19 | 59854.0% | operator |
| 21041 | Seq Scan | 161.40 | 162.03 | 0.4% | operator |
| 21042 | Index Scan | 0.06 | -0.02 | 129.0% | operator |
| 21044 | Seq Scan | 28.78 | 29.69 | 3.2% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 21041 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=18429
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0123
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=33394.0600
- **Output:** st=0.15, rt=162.03

### Step 2: Node 21042 (Index Scan) - LEAF

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
  - total_cost=2.2900
- **Output:** st=0.06, rt=-0.02

### Step 3: Node 21044 (Seq Scan) - LEAF

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

### Step 4: Node 21046 (Seq Scan) - LEAF

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

### Step 5: Node 21039 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 2e0f44ef (Hash Join -> [Nested Loop (Outer), Hash (Inner)])
- **Consumes:** Nodes 21034, 21035, 21036, 21037, 21038, 21040, 21043
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=18240
  - HashJoin_nt1=18240
  - HashJoin_nt2=62500
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=160
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0000
  - HashJoin_startup_cost=5006.6800
  - HashJoin_total_cost=80861.3200
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
  - NestedLoop_Outer_nt=18240
  - NestedLoop_Outer_nt1=18429
  - NestedLoop_Outer_nt2=1
  - NestedLoop_Outer_parallel_workers=0
  - NestedLoop_Outer_plan_width=16
  - NestedLoop_Outer_reltuples=0.0000
  - NestedLoop_Outer_sel=0.9897
  - NestedLoop_Outer_startup_cost=0.4300
  - NestedLoop_Outer_total_cost=75807.1900
- **Output:** st=37.52, rt=1101.75

### Step 6: Node 21045 (Hash)

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

### Step 7: Node 21034 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 04a01b61 (Limit -> Sort -> Aggregate -> Gather -> Hash Join (Outer) (Outer) (Outer) (Outer))
- **Consumes:** Nodes 21035, 21036, 21037, 21038, 21039, 21040, 21043
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=56544
  - Aggregate_Outer_nt1=56544
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=280
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=88280.0800
  - Aggregate_Outer_total_cost=88986.8800
  - Gather_Outer_np=0
  - Gather_Outer_nt=56544
  - Gather_Outer_nt1=18240
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=260
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.1000
  - Gather_Outer_startup_cost=6008.2400
  - Gather_Outer_total_cost=87573.2800
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=18240
  - HashJoin_Outer_nt1=18240
  - HashJoin_Outer_nt2=25
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=260
  - HashJoin_Outer_reltuples=0.0000
  - HashJoin_Outer_sel=0.0400
  - HashJoin_Outer_startup_cost=5008.2400
  - HashJoin_Outer_total_cost=80918.8800
  - Limit_np=0
  - Limit_nt=20
  - Limit_nt1=56544
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=280
  - Limit_reltuples=0.0000
  - Limit_sel=0.0004
  - Limit_startup_cost=90491.5000
  - Limit_total_cost=90491.5500
  - Sort_Outer_np=0
  - Sort_Outer_nt=56544
  - Sort_Outer_nt1=56544
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=280
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=90491.5000
  - Sort_Outer_total_cost=90632.8600
- **Output:** st=1150.40, rt=1151.16
