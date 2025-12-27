# Online Prediction Report

**Test Query:** Q10_127_seed_1033707906
**Timestamp:** 2025-12-22 02:27:20

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 73.41%

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
| 2 | 2e0f44ef | 108.1438 | 0.0001% | REJECTED | 17.92% |
| 3 | 2873b8c3 | 94.8003 | 0.0000% | REJECTED | 17.92% |
| 4 | 30d6e09b | 89.9904 | 0.0000% | REJECTED | 17.92% |
| 5 | 7a51ce50 | 89.9904 | 0.0000% | REJECTED | 17.92% |
| 6 | 7d4e78be | 89.9904 | 0.0000% | REJECTED | 17.92% |
| 7 | 7bcfec22 | 40.3755 | 0.0356% | REJECTED | 17.92% |
| 8 | e296a71f | 40.3755 | 0.0412% | REJECTED | 17.92% |
| 9 | 25df29b5 | 33.4481 | 9.8112% | ACCEPTED | 8.11% |
| 10 | 1d35fb97 | 33.3258 | 0.1176% | REJECTED | 8.11% |
| 11 | 4fc84c77 | 18.7042 | 0.7529% | ACCEPTED | 7.36% |
| 12 | b3a45093 | 3.8683 | N/A | SKIPPED_LOW_ERROR | 7.36% |
| 13 | 04a01b61 | 0.2016 | N/A | SKIPPED_LOW_ERROR | 7.36% |
| 14 | 4cf43b83 | 0.2016 | N/A | SKIPPED_LOW_ERROR | 7.36% |
| 15 | 843f0c9a | 0.2016 | N/A | SKIPPED_LOW_ERROR | 7.36% |
| 16 | bef3a974 | 0.2016 | N/A | SKIPPED_LOW_ERROR | 7.36% |
## Query Tree

```
Node 19747 (Limit) [PATTERN: 25df29b5] - ROOT
  Node 19748 (Sort) [consumed]
    Node 19749 (Aggregate) [consumed]
      Node 19750 (Gather) [consumed]
        Node 19751 (Hash Join)
          Node 19752 (Hash Join)
            Node 19753 (Nested Loop)
              Node 19754 (Seq Scan) - LEAF
              Node 19755 (Index Scan) - LEAF
            Node 19756 (Hash)
              Node 19757 (Seq Scan) - LEAF
          Node 19758 (Hash)
            Node 19759 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 25df29b5 | 19747 | 19748, 19749, 19750 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 1.74%
- Improvement: 71.67%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 19747 | Limit | 1134.97 | 1154.75 | 1.7% | pattern |
| 19751 | Hash Join | 1074.09 | 1062.09 | 1.1% | operator |
| 19752 | Hash Join | 1071.18 | 1044.12 | 2.5% | operator |
| 19758 | Hash | 0.02 | 14.54 | 80676.2% | operator |
| 19753 | Nested Loop | 1024.32 | 1097.97 | 7.2% | operator |
| 19756 | Hash | 36.53 | 45.64 | 24.9% | operator |
| 19759 | Seq Scan | 0.01 | 7.19 | 55242.1% | operator |
| 19754 | Seq Scan | 159.63 | 162.03 | 1.5% | operator |
| 19755 | Index Scan | 0.06 | -0.02 | 130.0% | operator |
| 19757 | Seq Scan | 29.41 | 29.69 | 0.9% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 19754 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=18230
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

### Step 2: Node 19755 (Index Scan) - LEAF

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
  - total_cost=2.3100
- **Output:** st=0.06, rt=-0.02

### Step 3: Node 19757 (Seq Scan) - LEAF

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

### Step 4: Node 19753 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18043
  - nt1=18230
  - nt2=1
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=162.0300
  - rt2=-0.0183
  - sel=0.9897
  - st1=0.1548
  - st2=0.0563
  - startup_cost=0.4300
  - total_cost=75621.2200
- **Output:** st=8.39, rt=1097.97

### Step 5: Node 19756 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=62500
  - nt1=62500
  - nt2=0
  - parallel_workers=0
  - plan_width=148
  - reltuples=0.0000
  - rt1=29.6885
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0565
  - st2=0.0000
  - startup_cost=4225.0000
  - total_cost=4225.0000
- **Output:** st=45.64, rt=45.64

### Step 6: Node 19759 (Seq Scan) - LEAF

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

### Step 7: Node 19752 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18043
  - nt1=18043
  - nt2=62500
  - parallel_workers=0
  - plan_width=160
  - reltuples=0.0000
  - rt1=1097.9714
  - rt2=45.6402
  - sel=0.0000
  - st1=8.3935
  - st2=45.6390
  - startup_cost=5006.6800
  - total_cost=80674.8300
- **Output:** st=34.85, rt=1044.12

### Step 8: Node 19758 (Hash)

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

### Step 9: Node 19751 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18043
  - nt1=18043
  - nt2=25
  - parallel_workers=0
  - plan_width=260
  - reltuples=0.0000
  - rt1=1044.1248
  - rt2=14.5397
  - sel=0.0400
  - st1=34.8488
  - st2=14.5393
  - startup_cost=5008.2400
  - total_cost=80731.7900
- **Output:** st=38.06, rt=1062.09

### Step 10: Node 19747 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 25df29b5 (Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer))
- **Consumes:** Nodes 19748, 19749, 19750
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=55933
  - Aggregate_Outer_nt1=55933
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=280
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=88024.2500
  - Aggregate_Outer_total_cost=88723.4100
  - Gather_Outer_np=0
  - Gather_Outer_nt=55933
  - Gather_Outer_nt1=18043
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=260
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.1000
  - Gather_Outer_startup_cost=6008.2400
  - Gather_Outer_total_cost=87325.0900
  - Limit_np=0
  - Limit_nt=20
  - Limit_nt1=55933
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=280
  - Limit_reltuples=0.0000
  - Limit_sel=0.0004
  - Limit_startup_cost=90211.7700
  - Limit_total_cost=90211.8200
  - Sort_Outer_np=0
  - Sort_Outer_nt=55933
  - Sort_Outer_nt1=55933
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=280
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=90211.7700
  - Sort_Outer_total_cost=90351.6000
- **Output:** st=1153.92, rt=1154.75
