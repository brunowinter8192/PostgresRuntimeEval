# Online Prediction Report

**Test Query:** Q3_64_seed_516853953
**Timestamp:** 2025-12-13 03:51:39

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 65.72%

## Phase C: Patterns in Query

- Total Patterns: 28

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 75736.1626 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 113504.2307 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 26.4017 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 168 | 75544.5822 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 13.3894 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 140 | 6.2375 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 116 | 4.0772 |
| e296a71f | Limit -> Sort (Outer) | 2 | 72 | 40.3755 |
| 7bcfec22 | Limit -> Sort -> Aggregate (Outer) (Oute... | 3 | 72 | 40.3755 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 72 | 2.9042 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 1 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 2 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 3 | f4cb205a | 75544.5822 | 0.0006% | REJECTED | 17.92% |
| 7 | e296a71f | 40.3755 | 0.0412% | REJECTED | 17.92% |
| 8 | 7bcfec22 | 40.3755 | 0.0356% | REJECTED | 17.92% |
| 10 | 25df29b5 | 33.4481 | 9.8112% | ACCEPTED | 8.11% |
## Query Tree

```
Node 5451 (Limit) [PATTERN: 25df29b5] - ROOT
  Node 5452 (Sort) [consumed]
    Node 5453 (Aggregate) [consumed]
      Node 5454 (Gather) [consumed]
        Node 5455 (Nested Loop)
          Node 5456 (Hash Join)
            Node 5457 (Seq Scan) - LEAF
            Node 5458 (Hash)
              Node 5459 (Seq Scan) - LEAF
          Node 5460 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 25df29b5 | 5451 | 5452, 5453, 5454 |


## Phase E: Final Prediction

- Final MRE: 1.10%
- Improvement: 64.62%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 5451 | Limit | 1209.32 | 1196.06 | 1.1% | pattern |
| 5455 | Nested Loop | 1172.25 | 1122.92 | 4.2% | operator |
| 5456 | Hash Join | 210.94 | 231.85 | 9.9% | operator |
| 5460 | Index Scan | 0.03 | -0.02 | 171.3% | operator |
| 5457 | Seq Scan | 155.95 | 162.34 | 4.1% | operator |
| 5458 | Hash | 28.63 | 17.51 | 38.8% | operator |
| 5459 | Seq Scan | 27.87 | 36.65 | 31.5% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 5459 (Seq Scan) - LEAF

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

### Step 2: Node 5457 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=235905
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=16
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1573
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=32184.3900
- **Output:** st=0.30, rt=162.34

### Step 3: Node 5458 (Hash)

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

### Step 4: Node 5456 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=47478
  - nt1=235905
  - nt2=12579
  - parallel_workers=0
  - plan_width=12
  - reltuples=0.0000
  - rt1=162.3435
  - rt2=17.5136
  - sel=0.0000
  - st1=0.2969
  - st2=17.5140
  - startup_cost=4538.4900
  - total_cost=37342.1500
- **Output:** st=29.12, rt=231.85

### Step 5: Node 5460 (Index Scan) - LEAF

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

### Step 6: Node 5455 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=101971
  - nt1=47478
  - nt2=3
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=231.8503
  - rt2=-0.0185
  - sel=0.7159
  - st1=29.1231
  - st2=0.0563
  - startup_cost=4538.9200
  - total_cost=73265.0500
- **Output:** st=31.25, rt=1122.92

### Step 7: Node 5451 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 25df29b5 (Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer))
- **Consumes:** Nodes 5452, 5453, 5454
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=316111
  - Aggregate_Outer_nt1=316111
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=44
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=110617.8200
  - Aggregate_Outer_total_cost=114569.2100
  - Gather_Outer_np=0
  - Gather_Outer_nt=316111
  - Gather_Outer_nt1=101971
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=24
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.1000
  - Gather_Outer_startup_cost=5538.9200
  - Gather_Outer_total_cost=105876.1500
  - Limit_np=0
  - Limit_nt=10
  - Limit_nt1=316111
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=44
  - Limit_reltuples=0.0000
  - Limit_sel=0.0000
  - Limit_startup_cost=121400.2500
  - Limit_total_cost=121400.2800
  - Sort_Outer_np=0
  - Sort_Outer_nt=316111
  - Sort_Outer_nt1=316111
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=44
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=121400.2500
  - Sort_Outer_total_cost=122190.5300
- **Output:** st=1194.16, rt=1196.06
