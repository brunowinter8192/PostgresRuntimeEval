# Online Prediction Report

**Test Query:** Q10_94_seed_762974883
**Timestamp:** 2025-12-13 02:24:40

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 74.09%

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
| 7d4e78be | Hash Join -> [Hash Join (Outer), Hash (I... | 2 | 48 | 89.9904 |
| 5437ac31 | Gather -> Hash Join (Outer) | 2 | 24 | 0.9438 |
| 7bcfec22 | Limit -> Sort -> Aggregate (Outer) (Oute... | 3 | 72 | 40.3755 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 72 | 2.9042 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 1 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 3 | 2e0f44ef | 108.1438 | 0.0001% | REJECTED | 17.92% |
| 4 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.92% |
| 5 | e296a71f | 40.3755 | 0.0412% | REJECTED | 17.92% |
| 6 | 7d4e78be | 89.9904 | 0.0000% | REJECTED | 17.92% |
| 8 | 7bcfec22 | 40.3755 | 0.0356% | REJECTED | 17.92% |
| 10 | 30d6e09b | 89.9904 | 0.0000% | REJECTED | 17.92% |
| 11 | 2873b8c3 | 94.8003 | 0.0000% | REJECTED | 17.92% |
| 14 | 25df29b5 | 33.4481 | 9.8112% | ACCEPTED | 8.11% |
| 15 | 7a51ce50 | 89.9904 | -0.0000% | REJECTED | 8.11% |
## Query Tree

```
Node 21229 (Limit) [PATTERN: 25df29b5] - ROOT
  Node 21230 (Sort) [consumed]
    Node 21231 (Aggregate) [consumed]
      Node 21232 (Gather) [consumed]
        Node 21233 (Hash Join)
          Node 21234 (Hash Join)
            Node 21235 (Nested Loop)
              Node 21236 (Seq Scan) - LEAF
              Node 21237 (Index Scan) - LEAF
            Node 21238 (Hash)
              Node 21239 (Seq Scan) - LEAF
          Node 21240 (Hash)
            Node 21241 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 25df29b5 | 21229 | 21230, 21231, 21232 |


## Phase E: Final Prediction

- Final MRE: 2.14%
- Improvement: 71.94%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 21229 | Limit | 1130.55 | 1154.78 | 2.1% | pattern |
| 21233 | Hash Join | 1081.28 | 1062.22 | 1.8% | operator |
| 21234 | Hash Join | 1076.81 | 1044.34 | 3.0% | operator |
| 21240 | Hash | 0.02 | 14.54 | 90773.2% | operator |
| 21235 | Nested Loop | 1033.54 | 1098.03 | 6.2% | operator |
| 21238 | Hash | 32.84 | 45.64 | 39.0% | operator |
| 21241 | Seq Scan | 0.01 | 7.19 | 65304.3% | operator |
| 21236 | Seq Scan | 159.12 | 162.03 | 1.8% | operator |
| 21237 | Index Scan | 0.06 | -0.02 | 130.0% | operator |
| 21239 | Seq Scan | 26.79 | 29.69 | 10.8% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 21236 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=18317
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

### Step 2: Node 21237 (Index Scan) - LEAF

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

### Step 3: Node 21239 (Seq Scan) - LEAF

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

### Step 4: Node 21235 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18130
  - nt1=18317
  - nt2=1
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=162.0291
  - rt2=-0.0183
  - sel=0.9898
  - st1=0.1548
  - st2=0.0563
  - startup_cost=0.4300
  - total_cost=75701.8300
- **Output:** st=8.43, rt=1098.03

### Step 5: Node 21238 (Hash)

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

### Step 6: Node 21241 (Seq Scan) - LEAF

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

### Step 7: Node 21234 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18130
  - nt1=18130
  - nt2=62500
  - parallel_workers=0
  - plan_width=160
  - reltuples=0.0000
  - rt1=1098.0251
  - rt2=45.6402
  - sel=0.0000
  - st1=8.4285
  - st2=45.6390
  - startup_cost=5006.6800
  - total_cost=80755.6700
- **Output:** st=34.85, rt=1044.34

### Step 8: Node 21240 (Hash)

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

### Step 9: Node 21233 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18130
  - nt1=18130
  - nt2=25
  - parallel_workers=0
  - plan_width=260
  - reltuples=0.0000
  - rt1=1044.3405
  - rt2=14.5397
  - sel=0.0400
  - st1=34.8537
  - st2=14.5393
  - startup_cost=5008.2400
  - total_cost=80812.8900
- **Output:** st=38.07, rt=1062.22

### Step 10: Node 21229 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 25df29b5 (Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer))
- **Consumes:** Nodes 21230, 21231, 21232
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=56202
  - Aggregate_Outer_nt1=56202
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=280
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=88135.6200
  - Aggregate_Outer_total_cost=88838.1400
  - Gather_Outer_np=0
  - Gather_Outer_nt=56202
  - Gather_Outer_nt1=18130
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=260
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.0999
  - Gather_Outer_startup_cost=6008.2400
  - Gather_Outer_total_cost=87433.0900
  - Limit_np=0
  - Limit_nt=20
  - Limit_nt1=56202
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=280
  - Limit_reltuples=0.0000
  - Limit_sel=0.0004
  - Limit_startup_cost=90333.6600
  - Limit_total_cost=90333.7100
  - Sort_Outer_np=0
  - Sort_Outer_nt=56202
  - Sort_Outer_nt1=56202
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=280
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=90333.6600
  - Sort_Outer_total_cost=90474.1600
- **Output:** st=1153.95, rt=1154.78
