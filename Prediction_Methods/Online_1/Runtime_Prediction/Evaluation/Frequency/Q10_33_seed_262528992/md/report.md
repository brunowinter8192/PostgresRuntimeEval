# Online Prediction Report

**Test Query:** Q10_33_seed_262528992
**Timestamp:** 2025-12-13 03:31:42

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 72.79%

## Phase C: Patterns in Query

- Total Patterns: 29

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 113504.2307 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 26.4017 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 13.3894 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 108.1438 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 141.6847 |
| e296a71f | Limit -> Sort (Outer) | 2 | 72 | 40.3755 |
| 7bcfec22 | Limit -> Sort -> Aggregate (Outer) (Oute... | 3 | 72 | 40.3755 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 72 | 2.9042 |
| 7d4e78be | Hash Join -> [Hash Join (Outer), Hash (I... | 2 | 48 | 89.9904 |
| 30d6e09b | Hash Join -> [Hash Join -> [Nested Loop ... | 3 | 48 | 89.9904 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 1 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 3 | 2e0f44ef | 108.1438 | 0.0001% | REJECTED | 17.92% |
| 4 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.92% |
| 5 | e296a71f | 40.3755 | 0.0412% | REJECTED | 17.92% |
| 6 | 7bcfec22 | 40.3755 | 0.0356% | REJECTED | 17.92% |
| 8 | 7d4e78be | 89.9904 | 0.0000% | REJECTED | 17.92% |
| 9 | 30d6e09b | 89.9904 | 0.0000% | REJECTED | 17.92% |
| 10 | 2873b8c3 | 94.8003 | 0.0000% | REJECTED | 17.92% |
| 11 | 25df29b5 | 33.4481 | 9.8112% | ACCEPTED | 8.11% |
| 12 | 7a51ce50 | 89.9904 | -0.0000% | REJECTED | 8.11% |
## Query Tree

```
Node 20358 (Limit) [PATTERN: 25df29b5] - ROOT
  Node 20359 (Sort) [consumed]
    Node 20360 (Aggregate) [consumed]
      Node 20361 (Gather) [consumed]
        Node 20362 (Hash Join)
          Node 20363 (Hash Join)
            Node 20364 (Nested Loop)
              Node 20365 (Seq Scan) - LEAF
              Node 20366 (Index Scan) - LEAF
            Node 20367 (Hash)
              Node 20368 (Seq Scan) - LEAF
          Node 20369 (Hash)
            Node 20370 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 25df29b5 | 20358 | 20359, 20360, 20361 |


## Phase E: Final Prediction

- Final MRE: 1.37%
- Improvement: 71.42%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 20358 | Limit | 1139.07 | 1154.71 | 1.4% | pattern |
| 20362 | Hash Join | 1083.94 | 1061.88 | 2.0% | operator |
| 20363 | Hash Join | 1080.90 | 1043.77 | 3.4% | operator |
| 20369 | Hash | 0.01 | 14.54 | 111744.0% | operator |
| 20364 | Nested Loop | 1034.87 | 1097.89 | 6.1% | operator |
| 20367 | Hash | 33.16 | 45.64 | 37.6% | operator |
| 20370 | Seq Scan | 0.01 | 7.19 | 79838.6% | operator |
| 20365 | Seq Scan | 160.11 | 162.03 | 1.2% | operator |
| 20366 | Index Scan | 0.06 | -0.02 | 129.5% | operator |
| 20368 | Seq Scan | 25.17 | 29.69 | 17.9% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 20365 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=18086
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0121
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=33394.0600
- **Output:** st=0.15, rt=162.03

### Step 2: Node 20366 (Index Scan) - LEAF

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
  - total_cost=2.3200
- **Output:** st=0.06, rt=-0.02

### Step 3: Node 20368 (Seq Scan) - LEAF

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

### Step 4: Node 20364 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=17901
  - nt1=18086
  - nt2=1
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=162.0316
  - rt2=-0.0183
  - sel=0.9898
  - st1=0.1547
  - st2=0.0563
  - startup_cost=0.4300
  - total_cost=75485.0300
- **Output:** st=8.34, rt=1097.89

### Step 5: Node 20367 (Hash)

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

### Step 6: Node 20370 (Seq Scan) - LEAF

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

### Step 7: Node 20363 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=17901
  - nt1=17901
  - nt2=62500
  - parallel_workers=0
  - plan_width=160
  - reltuples=0.0000
  - rt1=1097.8852
  - rt2=45.6402
  - sel=0.0000
  - st1=8.3375
  - st2=45.6390
  - startup_cost=5006.6800
  - total_cost=80538.2700
- **Output:** st=34.84, rt=1043.77

### Step 8: Node 20369 (Hash)

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

### Step 9: Node 20362 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=17901
  - nt1=17901
  - nt2=25
  - parallel_workers=0
  - plan_width=260
  - reltuples=0.0000
  - rt1=1043.7741
  - rt2=14.5397
  - sel=0.0400
  - st1=34.8401
  - st2=14.5393
  - startup_cost=5008.2400
  - total_cost=80594.7900
- **Output:** st=38.04, rt=1061.88

### Step 10: Node 20358 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 25df29b5 (Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer))
- **Consumes:** Nodes 20359, 20360, 20361
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=55493
  - Aggregate_Outer_nt1=55493
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=280
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=87837.7600
  - Aggregate_Outer_total_cost=88531.4200
  - Gather_Outer_np=0
  - Gather_Outer_nt=55493
  - Gather_Outer_nt1=17901
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=260
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.1000
  - Gather_Outer_startup_cost=6008.2400
  - Gather_Outer_total_cost=87144.0900
  - Limit_np=0
  - Limit_nt=20
  - Limit_nt1=55493
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=280
  - Limit_reltuples=0.0000
  - Limit_sel=0.0004
  - Limit_startup_cost=90008.0700
  - Limit_total_cost=90008.1200
  - Sort_Outer_np=0
  - Sort_Outer_nt=55493
  - Sort_Outer_nt1=55493
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=280
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=90008.0700
  - Sort_Outer_total_cost=90146.8000
- **Output:** st=1153.88, rt=1154.71
