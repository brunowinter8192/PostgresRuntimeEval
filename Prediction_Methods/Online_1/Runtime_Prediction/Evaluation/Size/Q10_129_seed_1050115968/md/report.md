# Online Prediction Report

**Test Query:** Q10_129_seed_1050115968
**Timestamp:** 2025-12-22 04:37:37

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 72.84%

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
| 7d4e78be | Hash Join -> [Hash Join (Outer), Hash (I... | 2 | 48 | 187.5% | 89.9904 |
| 5437ac31 | Gather -> Hash Join (Outer) | 2 | 24 | 3.9% | 0.9438 |
| 7bcfec22 | Limit -> Sort -> Aggregate (Outer) (Oute... | 3 | 72 | 56.1% | 40.3755 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 72 | 4.0% | 2.9042 |
| 30d6e09b | Hash Join -> [Hash Join -> [Nested Loop ... | 3 | 48 | 187.5% | 89.9904 |
| 2873b8c3 | Hash Join -> [Nested Loop -> [Seq Scan (... | 3 | 48 | 197.5% | 94.8003 |
| 284f5967 | Aggregate -> Gather -> Hash Join (Outer)... | 3 | 24 | 2.6% | 0.6204 |
| f4d53e95 | Gather -> Hash Join -> [Hash Join (Outer... | 3 | 24 | 3.9% | 0.9438 |
| 25df29b5 | Limit -> Sort -> Aggregate -> Gather (Ou... | 4 | 48 | 69.7% | 33.4481 |
| 7a51ce50 | Hash Join -> [Hash Join -> [Nested Loop ... | 4 | 48 | 187.5% | 89.9904 |
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
| 1 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 2 | 4fc84c77 | 13.3894 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 3 | 2e0f44ef | 108.1438 | 0.0001% | REJECTED | 17.92% |
| 4 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.92% |
| 5 | e296a71f | 40.3755 | 0.0412% | REJECTED | 17.92% |
| 6 | 7d4e78be | 89.9904 | 0.0000% | REJECTED | 17.92% |
| 7 | 5437ac31 | 0.9438 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 8 | 7bcfec22 | 40.3755 | 0.0356% | REJECTED | 17.92% |
| 9 | b3a45093 | 2.9042 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 10 | 30d6e09b | 89.9904 | 0.0000% | REJECTED | 17.92% |
| 11 | 2873b8c3 | 94.8003 | 0.0000% | REJECTED | 17.92% |
| 12 | 284f5967 | 0.6204 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 13 | f4d53e95 | 0.9438 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 14 | 25df29b5 | 33.4481 | 9.8112% | ACCEPTED | 8.11% |
| 15 | 7a51ce50 | 89.9904 | -0.0000% | REJECTED | 8.11% |
| 16 | 04a01b61 | 0.2016 | N/A | SKIPPED_LOW_ERROR | 8.11% |
| 17 | 4cf43b83 | 0.2016 | N/A | SKIPPED_LOW_ERROR | 8.11% |
| 18 | 843f0c9a | 0.2016 | N/A | SKIPPED_LOW_ERROR | 8.11% |
| 19 | bef3a974 | 0.2016 | N/A | SKIPPED_LOW_ERROR | 8.11% |
## Query Tree

```
Node 19773 (Limit) [PATTERN: 25df29b5] - ROOT
  Node 19774 (Sort) [consumed]
    Node 19775 (Aggregate) [consumed]
      Node 19776 (Gather) [consumed]
        Node 19777 (Hash Join)
          Node 19778 (Hash Join)
            Node 19779 (Nested Loop)
              Node 19780 (Seq Scan) - LEAF
              Node 19781 (Index Scan) - LEAF
            Node 19782 (Hash)
              Node 19783 (Seq Scan) - LEAF
          Node 19784 (Hash)
            Node 19785 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 25df29b5 | 19773 | 19774, 19775, 19776 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 1.42%
- Improvement: 71.42%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 19773 | Limit | 1138.65 | 1154.81 | 1.4% | pattern |
| 19777 | Hash Join | 1090.15 | 1062.37 | 2.5% | operator |
| 19778 | Hash Join | 1087.25 | 1044.59 | 3.9% | operator |
| 19784 | Hash | 0.01 | 14.54 | 103755.1% | operator |
| 19779 | Nested Loop | 1045.48 | 1098.09 | 5.0% | operator |
| 19782 | Hash | 31.29 | 45.64 | 45.9% | operator |
| 19785 | Seq Scan | 0.01 | 7.19 | 71844.7% | operator |
| 19780 | Seq Scan | 160.15 | 162.03 | 1.2% | operator |
| 19781 | Index Scan | 0.06 | -0.02 | 129.5% | operator |
| 19783 | Seq Scan | 23.43 | 29.69 | 26.7% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 19780 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=18419
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

### Step 2: Node 19781 (Index Scan) - LEAF

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

### Step 3: Node 19783 (Seq Scan) - LEAF

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

### Step 4: Node 19779 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18231
  - nt1=18419
  - nt2=1
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=162.0280
  - rt2=-0.0183
  - sel=0.9898
  - st1=0.1549
  - st2=0.0563
  - startup_cost=0.4300
  - total_cost=75797.4000
- **Output:** st=8.47, rt=1098.09

### Step 5: Node 19782 (Hash)

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

### Step 6: Node 19785 (Seq Scan) - LEAF

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

### Step 7: Node 19778 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18231
  - nt1=18231
  - nt2=62500
  - parallel_workers=0
  - plan_width=160
  - reltuples=0.0000
  - rt1=1098.0871
  - rt2=45.6402
  - sel=0.0000
  - st1=8.4691
  - st2=45.6390
  - startup_cost=5006.6800
  - total_cost=80851.5100
- **Output:** st=34.86, rt=1044.59

### Step 8: Node 19784 (Hash)

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

### Step 9: Node 19777 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18231
  - nt1=18231
  - nt2=25
  - parallel_workers=0
  - plan_width=260
  - reltuples=0.0000
  - rt1=1044.5920
  - rt2=14.5397
  - sel=0.0400
  - st1=34.8596
  - st2=14.5393
  - startup_cost=5008.2400
  - total_cost=80909.0400
- **Output:** st=38.09, rt=1062.37

### Step 10: Node 19773 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 25df29b5 (Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer))
- **Consumes:** Nodes 19774, 19775, 19776
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=56515
  - Aggregate_Outer_nt1=56515
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=280
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=88266.9800
  - Aggregate_Outer_total_cost=88973.4100
  - Gather_Outer_np=0
  - Gather_Outer_nt=56515
  - Gather_Outer_nt1=18231
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=260
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.0999
  - Gather_Outer_startup_cost=6008.2400
  - Gather_Outer_total_cost=87560.5400
  - Limit_np=0
  - Limit_nt=20
  - Limit_nt1=56515
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=280
  - Limit_reltuples=0.0000
  - Limit_sel=0.0004
  - Limit_startup_cost=90477.2600
  - Limit_total_cost=90477.3100
  - Sort_Outer_np=0
  - Sort_Outer_nt=56515
  - Sort_Outer_nt1=56515
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=280
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=90477.2600
  - Sort_Outer_total_cost=90618.5400
- **Output:** st=1153.98, rt=1154.81
