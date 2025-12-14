# Online Prediction Report

**Test Query:** Q10_150_seed_1231235959
**Timestamp:** 2025-12-13 02:21:17

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 69.29%

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
Node 20085 (Limit) [PATTERN: 25df29b5] - ROOT
  Node 20086 (Sort) [consumed]
    Node 20087 (Aggregate) [consumed]
      Node 20088 (Gather) [consumed]
        Node 20089 (Hash Join)
          Node 20090 (Hash Join)
            Node 20091 (Nested Loop)
              Node 20092 (Seq Scan) - LEAF
              Node 20093 (Index Scan) - LEAF
            Node 20094 (Hash)
              Node 20095 (Seq Scan) - LEAF
          Node 20096 (Hash)
            Node 20097 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 25df29b5 | 20085 | 20086, 20087, 20088 |


## Phase E: Final Prediction

- Final MRE: 0.68%
- Improvement: 68.61%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 20085 | Limit | 1162.61 | 1154.73 | 0.7% | pattern |
| 20089 | Hash Join | 1105.02 | 1061.97 | 3.9% | operator |
| 20090 | Hash Join | 1102.09 | 1043.93 | 5.3% | operator |
| 20096 | Hash | 0.01 | 14.54 | 96831.4% | operator |
| 20091 | Nested Loop | 1051.62 | 1097.92 | 4.4% | operator |
| 20094 | Hash | 38.12 | 45.64 | 19.7% | operator |
| 20097 | Seq Scan | 0.01 | 7.19 | 71844.7% | operator |
| 20092 | Seq Scan | 162.82 | 162.03 | 0.5% | operator |
| 20093 | Index Scan | 0.06 | -0.02 | 129.5% | operator |
| 20095 | Seq Scan | 28.24 | 29.69 | 5.1% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 20092 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=18150
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

### Step 2: Node 20093 (Index Scan) - LEAF

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

### Step 3: Node 20095 (Seq Scan) - LEAF

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

### Step 4: Node 20091 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=17964
  - nt1=18150
  - nt2=1
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=162.0309
  - rt2=-0.0183
  - sel=0.9898
  - st1=0.1547
  - st2=0.0563
  - startup_cost=0.4300
  - total_cost=75546.0800
- **Output:** st=8.36, rt=1097.92

### Step 5: Node 20094 (Hash)

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

### Step 6: Node 20097 (Seq Scan) - LEAF

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

### Step 7: Node 20090 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=17964
  - nt1=17964
  - nt2=62500
  - parallel_workers=0
  - plan_width=160
  - reltuples=0.0000
  - rt1=1097.9234
  - rt2=45.6402
  - sel=0.0000
  - st1=8.3623
  - st2=45.6390
  - startup_cost=5006.6800
  - total_cost=80599.4900
- **Output:** st=34.84, rt=1043.93

### Step 8: Node 20096 (Hash)

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

### Step 9: Node 20089 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=17964
  - nt1=17964
  - nt2=25
  - parallel_workers=0
  - plan_width=260
  - reltuples=0.0000
  - rt1=1043.9301
  - rt2=14.5397
  - sel=0.0400
  - st1=34.8441
  - st2=14.5393
  - startup_cost=5008.2400
  - total_cost=80656.2100
- **Output:** st=38.05, rt=1061.97

### Step 10: Node 20085 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 25df29b5 (Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer))
- **Consumes:** Nodes 20086, 20087, 20088
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=55687
  - Aggregate_Outer_nt1=55687
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=280
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=87920.9900
  - Aggregate_Outer_total_cost=88617.0800
  - Gather_Outer_np=0
  - Gather_Outer_nt=55687
  - Gather_Outer_nt1=17964
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=260
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.0999
  - Gather_Outer_startup_cost=6008.2400
  - Gather_Outer_total_cost=87224.9100
  - Limit_np=0
  - Limit_nt=20
  - Limit_nt1=55687
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=280
  - Limit_reltuples=0.0000
  - Limit_sel=0.0004
  - Limit_startup_cost=90098.8900
  - Limit_total_cost=90098.9400
  - Sort_Outer_np=0
  - Sort_Outer_nt=55687
  - Sort_Outer_nt1=55687
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=280
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=90098.8900
  - Sort_Outer_total_cost=90238.1100
- **Output:** st=1153.90, rt=1154.73
