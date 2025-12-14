# Online Prediction Report

**Test Query:** Q10_62_seed_500445891
**Timestamp:** 2025-12-13 01:05:11

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 68.00%

## Phase C: Patterns in Query

- Total Patterns: 29

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 113504.2307 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 141.6847 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 108.1438 |
| 2873b8c3 | Hash Join -> [Nested Loop -> [Seq Scan (... | 3 | 48 | 94.8003 |
| 7d4e78be | Hash Join -> [Hash Join (Outer), Hash (I... | 2 | 48 | 89.9904 |
| 30d6e09b | Hash Join -> [Hash Join -> [Nested Loop ... | 3 | 48 | 89.9904 |
| 7a51ce50 | Hash Join -> [Hash Join -> [Nested Loop ... | 4 | 48 | 89.9904 |
| e296a71f | Limit -> Sort (Outer) | 2 | 72 | 40.3755 |
| 7bcfec22 | Limit -> Sort -> Aggregate (Outer) (Oute... | 3 | 72 | 40.3755 |
| 25df29b5 | Limit -> Sort -> Aggregate -> Gather (Ou... | 4 | 48 | 33.4481 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 1 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.92% |
| 2 | 2e0f44ef | 108.1438 | 0.0001% | REJECTED | 17.92% |
| 3 | 2873b8c3 | 94.8003 | 0.0000% | REJECTED | 17.92% |
| 4 | 7d4e78be | 89.9904 | 0.0000% | REJECTED | 17.92% |
| 5 | 30d6e09b | 89.9904 | 0.0000% | REJECTED | 17.92% |
| 6 | 7a51ce50 | 89.9904 | 0.0000% | REJECTED | 17.92% |
| 7 | e296a71f | 40.3755 | 0.0412% | REJECTED | 17.92% |
| 8 | 7bcfec22 | 40.3755 | 0.0356% | REJECTED | 17.92% |
| 9 | 25df29b5 | 33.4481 | 9.8112% | ACCEPTED | 8.11% |
| 10 | 1d35fb97 | 33.3258 | 0.1176% | REJECTED | 8.11% |
| 11 | 4fc84c77 | 18.7042 | 0.7529% | ACCEPTED | 7.36% |
## Query Tree

```
Node 20774 (Limit) [PATTERN: 25df29b5] - ROOT
  Node 20775 (Sort) [consumed]
    Node 20776 (Aggregate) [consumed]
      Node 20777 (Gather) [consumed]
        Node 20778 (Hash Join)
          Node 20779 (Hash Join)
            Node 20780 (Nested Loop)
              Node 20781 (Seq Scan) - LEAF
              Node 20782 (Index Scan) - LEAF
            Node 20783 (Hash)
              Node 20784 (Seq Scan) - LEAF
          Node 20785 (Hash)
            Node 20786 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 25df29b5 | 20774 | 20775, 20776, 20777 |


## Phase E: Final Prediction

- Final MRE: 1.42%
- Improvement: 66.58%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 20774 | Limit | 1171.46 | 1154.80 | 1.4% | pattern |
| 20778 | Hash Join | 1116.31 | 1062.30 | 4.8% | operator |
| 20779 | Hash Join | 1113.36 | 1044.47 | 6.2% | operator |
| 20785 | Hash | 0.02 | 14.54 | 90773.2% | operator |
| 20780 | Nested Loop | 1068.29 | 1098.06 | 2.8% | operator |
| 20783 | Hash | 34.58 | 45.64 | 32.0% | operator |
| 20786 | Seq Scan | 0.01 | 7.19 | 59854.0% | operator |
| 20781 | Seq Scan | 159.83 | 162.03 | 1.4% | operator |
| 20782 | Index Scan | 0.06 | -0.02 | 129.0% | operator |
| 20784 | Seq Scan | 27.29 | 29.69 | 8.8% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 20781 (Seq Scan) - LEAF

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
- **Output:** st=0.15, rt=162.03

### Step 2: Node 20782 (Index Scan) - LEAF

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

### Step 3: Node 20784 (Seq Scan) - LEAF

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

### Step 4: Node 20780 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18183
  - nt1=18371
  - nt2=1
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=162.0285
  - rt2=-0.0183
  - sel=0.9898
  - st1=0.1548
  - st2=0.0563
  - startup_cost=0.4300
  - total_cost=75753.0800
- **Output:** st=8.45, rt=1098.06

### Step 5: Node 20783 (Hash)

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

### Step 6: Node 20786 (Seq Scan) - LEAF

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

### Step 7: Node 20779 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18183
  - nt1=18183
  - nt2=62500
  - parallel_workers=0
  - plan_width=160
  - reltuples=0.0000
  - rt1=1098.0573
  - rt2=45.6402
  - sel=0.0000
  - st1=8.4496
  - st2=45.6390
  - startup_cost=5006.6800
  - total_cost=80807.0600
- **Output:** st=34.86, rt=1044.47

### Step 8: Node 20785 (Hash)

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

### Step 9: Node 20778 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18183
  - nt1=18183
  - nt2=25
  - parallel_workers=0
  - plan_width=260
  - reltuples=0.0000
  - rt1=1044.4722
  - rt2=14.5397
  - sel=0.0400
  - st1=34.8570
  - st2=14.5393
  - startup_cost=5008.2400
  - total_cost=80864.4400
- **Output:** st=38.08, rt=1062.30

### Step 10: Node 20774 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 25df29b5 (Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer))
- **Consumes:** Nodes 20775, 20776, 20777
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
- **Output:** st=1153.97, rt=1154.80
