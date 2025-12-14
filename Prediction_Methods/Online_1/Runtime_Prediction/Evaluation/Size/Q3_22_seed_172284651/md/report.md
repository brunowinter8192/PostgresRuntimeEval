# Online Prediction Report

**Test Query:** Q3_22_seed_172284651
**Timestamp:** 2025-12-13 02:41:43

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 64.53%

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
Node 4991 (Limit) [PATTERN: 25df29b5] - ROOT
  Node 4992 (Sort) [consumed]
    Node 4993 (Aggregate) [consumed]
      Node 4994 (Gather) [consumed]
        Node 4995 (Nested Loop)
          Node 4996 (Hash Join)
            Node 4997 (Seq Scan) - LEAF
            Node 4998 (Hash)
              Node 4999 (Seq Scan) - LEAF
          Node 5000 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 25df29b5 | 4991 | 4992, 4993, 4994 |


## Phase E: Final Prediction

- Final MRE: 1.81%
- Improvement: 62.72%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 4991 | Limit | 1217.96 | 1195.90 | 1.8% | pattern |
| 4995 | Nested Loop | 1182.42 | 1122.02 | 5.1% | operator |
| 4996 | Hash Join | 210.34 | 231.64 | 10.1% | operator |
| 5000 | Index Scan | 0.03 | -0.02 | 168.7% | operator |
| 4997 | Seq Scan | 158.88 | 162.28 | 2.1% | operator |
| 4998 | Hash | 29.27 | 17.51 | 40.2% | operator |
| 4999 | Seq Scan | 28.44 | 36.69 | 29.0% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 4999 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=3600
  - nt=12479
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=150000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0832
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=4381.2500
- **Output:** st=0.35, rt=36.69

### Step 2: Node 4997 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=235005
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=16
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1567
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=32184.3900
- **Output:** st=0.30, rt=162.28

### Step 3: Node 4998 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=12479
  - nt1=12479
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=36.6891
  - rt2=0.0000
  - sel=1.0000
  - st1=0.3540
  - st2=0.0000
  - startup_cost=4381.2500
  - total_cost=4381.2500
- **Output:** st=17.51, rt=17.51

### Step 4: Node 4996 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=46921
  - nt1=235005
  - nt2=12479
  - parallel_workers=0
  - plan_width=12
  - reltuples=0.0000
  - rt1=162.2827
  - rt2=17.5121
  - sel=0.0000
  - st1=0.2968
  - st2=17.5125
  - startup_cost=4537.2400
  - total_cost=37338.5300
- **Output:** st=29.10, rt=231.64

### Step 5: Node 5000 (Index Scan) - LEAF

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

### Step 6: Node 4995 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=101013
  - nt1=46921
  - nt2=3
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=231.6400
  - rt2=-0.0185
  - sel=0.7176
  - st1=29.1037
  - st2=0.0563
  - startup_cost=4537.6700
  - total_cost=72874.9000
- **Output:** st=30.46, rt=1122.02

### Step 7: Node 4991 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 25df29b5 (Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer))
- **Consumes:** Nodes 4992, 4993, 4994
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=313140
  - Aggregate_Outer_nt1=313140
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=44
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=109886.0000
  - Aggregate_Outer_total_cost=113800.2500
  - Gather_Outer_np=0
  - Gather_Outer_nt=313140
  - Gather_Outer_nt1=101013
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=24
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.1000
  - Gather_Outer_startup_cost=5537.6700
  - Gather_Outer_total_cost=105188.9000
  - Limit_np=0
  - Limit_nt=10
  - Limit_nt1=313140
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=44
  - Limit_reltuples=0.0000
  - Limit_sel=0.0000
  - Limit_startup_cost=120567.0900
  - Limit_total_cost=120567.1200
  - Sort_Outer_np=0
  - Sort_Outer_nt=313140
  - Sort_Outer_nt1=313140
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=44
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=120567.0900
  - Sort_Outer_total_cost=121349.9400
- **Output:** st=1194.00, rt=1195.90
