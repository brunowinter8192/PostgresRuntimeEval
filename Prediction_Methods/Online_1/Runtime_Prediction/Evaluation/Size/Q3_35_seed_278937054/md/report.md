# Online Prediction Report

**Test Query:** Q3_35_seed_278937054
**Timestamp:** 2025-12-13 02:42:54

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 63.91%

## Phase C: Patterns in Query

- Total Patterns: 28

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 75736.1626 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 113504.2307 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 26.4017 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 13.3894 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 140 | 6.2375 |
| e296a71f | Limit -> Sort (Outer) | 2 | 72 | 40.3755 |
| 694ae2c3 | Gather -> Nested Loop (Outer) | 2 | 24 | 0.6475 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 168 | 75544.5822 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 116 | 4.0772 |
| 7bcfec22 | Limit -> Sort -> Aggregate (Outer) (Oute... | 3 | 72 | 40.3755 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 1 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 2 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 5 | e296a71f | 40.3755 | 0.0412% | REJECTED | 17.92% |
| 7 | f4cb205a | 75544.5822 | 0.0006% | REJECTED | 17.92% |
| 9 | 7bcfec22 | 40.3755 | 0.0356% | REJECTED | 17.92% |
| 13 | 25df29b5 | 33.4481 | 9.8112% | ACCEPTED | 8.11% |
## Query Tree

```
Node 5131 (Limit) [PATTERN: 25df29b5] - ROOT
  Node 5132 (Sort) [consumed]
    Node 5133 (Aggregate) [consumed]
      Node 5134 (Gather) [consumed]
        Node 5135 (Nested Loop)
          Node 5136 (Hash Join)
            Node 5137 (Seq Scan) - LEAF
            Node 5138 (Hash)
              Node 5139 (Seq Scan) - LEAF
          Node 5140 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 25df29b5 | 5131 | 5132, 5133, 5134 |


## Phase E: Final Prediction

- Final MRE: 2.17%
- Improvement: 61.74%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 5131 | Limit | 1222.63 | 1196.06 | 2.2% | pattern |
| 5135 | Nested Loop | 1187.22 | 1122.86 | 5.4% | operator |
| 5136 | Hash Join | 210.88 | 231.81 | 9.9% | operator |
| 5140 | Index Scan | 0.03 | -0.02 | 168.7% | operator |
| 5137 | Seq Scan | 159.18 | 162.33 | 2.0% | operator |
| 5138 | Hash | 28.93 | 17.51 | 39.5% | operator |
| 5139 | Seq Scan | 28.34 | 36.65 | 29.3% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 5139 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=3600
  - nt=12579
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=150000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0839
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=4381.2500
- **Output:** st=0.35, rt=36.65

### Step 2: Node 5137 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=235716
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=16
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1571
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=32184.3900
- **Output:** st=0.30, rt=162.33

### Step 3: Node 5138 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=12579
  - nt1=12579
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=36.6494
  - rt2=0.0000
  - sel=1.0000
  - st1=0.3532
  - st2=0.0000
  - startup_cost=4381.2500
  - total_cost=4381.2500
- **Output:** st=17.51, rt=17.51

### Step 4: Node 5136 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=47440
  - nt1=235716
  - nt2=12579
  - parallel_workers=0
  - plan_width=12
  - reltuples=0.0000
  - rt1=162.3307
  - rt2=17.5136
  - sel=0.0000
  - st1=0.2969
  - st2=17.5140
  - startup_cost=4538.4900
  - total_cost=37341.6500
- **Output:** st=29.12, rt=231.81

### Step 5: Node 5140 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=3
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
  - total_cost=0.7300
- **Output:** st=0.06, rt=-0.02

### Step 6: Node 5135 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=101950
  - nt1=47440
  - nt2=3
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=231.8133
  - rt2=-0.0185
  - sel=0.7163
  - st1=29.1160
  - st2=0.0563
  - startup_cost=4538.9200
  - total_cost=73243.2000
- **Output:** st=31.20, rt=1122.86

### Step 7: Node 5131 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 25df29b5 (Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer))
- **Consumes:** Nodes 5132, 5133, 5134
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=316044
  - Aggregate_Outer_nt1=316044
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=44
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=110588.2600
  - Aggregate_Outer_total_cost=114538.8100
  - Gather_Outer_np=0
  - Gather_Outer_nt=316044
  - Gather_Outer_nt1=101950
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=24
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.1000
  - Gather_Outer_startup_cost=5538.9200
  - Gather_Outer_total_cost=105847.6000
  - Limit_np=0
  - Limit_nt=10
  - Limit_nt1=316044
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=44
  - Limit_reltuples=0.0000
  - Limit_sel=0.0000
  - Limit_startup_cost=121368.4100
  - Limit_total_cost=121368.4400
  - Sort_Outer_np=0
  - Sort_Outer_nt=316044
  - Sort_Outer_nt1=316044
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=44
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=121368.4100
  - Sort_Outer_total_cost=122158.5200
- **Output:** st=1194.16, rt=1196.06
