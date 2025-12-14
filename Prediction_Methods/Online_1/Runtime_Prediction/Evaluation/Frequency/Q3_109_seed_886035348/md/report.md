# Online Prediction Report

**Test Query:** Q3_109_seed_886035348
**Timestamp:** 2025-12-13 03:50:27

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 66.32%

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
Node 4441 (Limit) [PATTERN: 25df29b5] - ROOT
  Node 4442 (Sort) [consumed]
    Node 4443 (Aggregate) [consumed]
      Node 4444 (Gather) [consumed]
        Node 4445 (Nested Loop)
          Node 4446 (Hash Join)
            Node 4447 (Seq Scan) - LEAF
            Node 4448 (Hash)
              Node 4449 (Seq Scan) - LEAF
          Node 4450 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 25df29b5 | 4441 | 4442, 4443, 4444 |


## Phase E: Final Prediction

- Final MRE: 0.74%
- Improvement: 65.57%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 4441 | Limit | 1204.95 | 1196.02 | 0.7% | pattern |
| 4445 | Nested Loop | 1169.65 | 1122.58 | 4.0% | operator |
| 4446 | Hash Join | 211.27 | 231.71 | 9.7% | operator |
| 4450 | Index Scan | 0.03 | -0.02 | 171.3% | operator |
| 4447 | Seq Scan | 155.86 | 162.30 | 4.1% | operator |
| 4448 | Hash | 29.51 | 17.51 | 40.6% | operator |
| 4449 | Seq Scan | 28.62 | 36.66 | 28.1% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 4449 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=3600
  - nt=12559
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=150000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0837
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=4381.2500
- **Output:** st=0.35, rt=36.66

### Step 2: Node 4447 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=235242
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=16
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1568
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=32184.3900
- **Output:** st=0.30, rt=162.30

### Step 3: Node 4448 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=12559
  - nt1=12559
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=36.6574
  - rt2=0.0000
  - sel=1.0000
  - st1=0.3533
  - st2=0.0000
  - startup_cost=4381.2500
  - total_cost=4381.2500
- **Output:** st=17.51, rt=17.51

### Step 4: Node 4446 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=47271
  - nt1=235242
  - nt2=12559
  - parallel_workers=0
  - plan_width=12
  - reltuples=0.0000
  - rt1=162.2987
  - rt2=17.5133
  - sel=0.0000
  - st1=0.2968
  - st2=17.5137
  - startup_cost=4538.2400
  - total_cost=37340.1600
- **Output:** st=29.10, rt=231.71

### Step 5: Node 4450 (Index Scan) - LEAF

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

### Step 6: Node 4445 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=101706
  - nt1=47271
  - nt2=3
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=231.7138
  - rt2=-0.0185
  - sel=0.7172
  - st1=29.1011
  - st2=0.0563
  - startup_cost=4538.6700
  - total_cost=73132.3300
- **Output:** st=30.95, rt=1122.58

### Step 7: Node 4441 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 25df29b5 (Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer))
- **Consumes:** Nodes 4442, 4443, 4444
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=315289
  - Aggregate_Outer_nt1=315289
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=44
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=110390.5600
  - Aggregate_Outer_total_cost=114331.6700
  - Gather_Outer_np=0
  - Gather_Outer_nt=315289
  - Gather_Outer_nt1=101706
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=24
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.1000
  - Gather_Outer_startup_cost=5538.6700
  - Gather_Outer_total_cost=105661.2300
  - Limit_np=0
  - Limit_nt=10
  - Limit_nt1=315289
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=44
  - Limit_reltuples=0.0000
  - Limit_sel=0.0000
  - Limit_startup_cost=121144.9600
  - Limit_total_cost=121144.9800
  - Sort_Outer_np=0
  - Sort_Outer_nt=315289
  - Sort_Outer_nt1=315289
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=44
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=121144.9600
  - Sort_Outer_total_cost=121933.1800
- **Output:** st=1194.12, rt=1196.02
