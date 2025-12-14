# Online Prediction Report

**Test Query:** Q3_129_seed_1050115968
**Timestamp:** 2025-12-13 03:50:27

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 54.10%

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
Node 4661 (Limit) [PATTERN: 25df29b5] - ROOT
  Node 4662 (Sort) [consumed]
    Node 4663 (Aggregate) [consumed]
      Node 4664 (Gather) [consumed]
        Node 4665 (Nested Loop)
          Node 4666 (Hash Join)
            Node 4667 (Seq Scan) - LEAF
            Node 4668 (Hash)
              Node 4669 (Seq Scan) - LEAF
          Node 4670 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 25df29b5 | 4661 | 4662, 4663, 4664 |


## Phase E: Final Prediction

- Final MRE: 8.03%
- Improvement: 46.07%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 4661 | Limit | 1300.46 | 1196.00 | 8.0% | pattern |
| 4665 | Nested Loop | 1265.16 | 1121.90 | 11.3% | operator |
| 4666 | Hash Join | 226.36 | 231.30 | 2.2% | operator |
| 4670 | Index Scan | 0.03 | -0.02 | 166.2% | operator |
| 4667 | Seq Scan | 171.89 | 162.16 | 5.7% | operator |
| 4668 | Hash | 31.18 | 17.51 | 43.8% | operator |
| 4669 | Seq Scan | 30.48 | 36.66 | 20.3% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 4669 (Seq Scan) - LEAF

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

### Step 2: Node 4667 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=233109
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=16
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1554
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=32184.3900
- **Output:** st=0.30, rt=162.16

### Step 3: Node 4668 (Hash)

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

### Step 4: Node 4666 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=46842
  - nt1=233109
  - nt2=12559
  - parallel_workers=0
  - plan_width=12
  - reltuples=0.0000
  - rt1=162.1557
  - rt2=17.5133
  - sel=0.0000
  - st1=0.2965
  - st2=17.5137
  - startup_cost=4538.2400
  - total_cost=37334.5600
- **Output:** st=29.02, rt=231.30

### Step 5: Node 4670 (Index Scan) - LEAF

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

### Step 6: Node 4665 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=101656
  - nt1=46842
  - nt2=3
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=231.3002
  - rt2=-0.0185
  - sel=0.7234
  - st1=29.0216
  - st2=0.0563
  - startup_cost=4538.6700
  - total_cost=72885.3400
- **Output:** st=30.33, rt=1121.90

### Step 7: Node 4661 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 25df29b5 (Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer))
- **Consumes:** Nodes 4662, 4663, 4664
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=315135
  - Aggregate_Outer_nt1=315135
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=44
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=110125.8600
  - Aggregate_Outer_total_cost=114065.0500
  - Gather_Outer_np=0
  - Gather_Outer_nt=315135
  - Gather_Outer_nt1=101656
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=24
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.1000
  - Gather_Outer_startup_cost=5538.6700
  - Gather_Outer_total_cost=105398.8400
  - Limit_np=0
  - Limit_nt=10
  - Limit_nt1=315135
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=44
  - Limit_reltuples=0.0000
  - Limit_sel=0.0000
  - Limit_startup_cost=120875.0000
  - Limit_total_cost=120875.0300
  - Sort_Outer_np=0
  - Sort_Outer_nt=315135
  - Sort_Outer_nt1=315135
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=44
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=120875.0000
  - Sort_Outer_total_cost=121662.8400
- **Output:** st=1194.10, rt=1196.00
