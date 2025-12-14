# Online Prediction Report

**Test Query:** Q3_7_seed_49224186
**Timestamp:** 2025-12-13 02:42:54

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 66.62%

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
Node 5621 (Limit) [PATTERN: 25df29b5] - ROOT
  Node 5622 (Sort) [consumed]
    Node 5623 (Aggregate) [consumed]
      Node 5624 (Gather) [consumed]
        Node 5625 (Nested Loop)
          Node 5626 (Hash Join)
            Node 5627 (Seq Scan) - LEAF
            Node 5628 (Hash)
              Node 5629 (Seq Scan) - LEAF
          Node 5630 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 25df29b5 | 5621 | 5622, 5623, 5624 |


## Phase E: Final Prediction

- Final MRE: 0.56%
- Improvement: 66.06%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 5621 | Limit | 1202.66 | 1195.92 | 0.6% | pattern |
| 5625 | Nested Loop | 1164.81 | 1122.15 | 3.7% | operator |
| 5626 | Hash Join | 207.74 | 231.69 | 11.5% | operator |
| 5630 | Index Scan | 0.03 | -0.02 | 171.3% | operator |
| 5627 | Seq Scan | 154.07 | 162.30 | 5.3% | operator |
| 5628 | Hash | 30.77 | 17.51 | 43.1% | operator |
| 5629 | Seq Scan | 29.93 | 36.69 | 22.6% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 5629 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=3600
  - nt=12487
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

### Step 2: Node 5627 (Seq Scan) - LEAF

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

### Step 3: Node 5628 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=12487
  - nt1=12487
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=36.6859
  - rt2=0.0000
  - sel=1.0000
  - st1=0.3539
  - st2=0.0000
  - startup_cost=4381.2500
  - total_cost=4381.2500
- **Output:** st=17.51, rt=17.51

### Step 4: Node 5626 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=46998
  - nt1=235242
  - nt2=12487
  - parallel_workers=0
  - plan_width=12
  - reltuples=0.0000
  - rt1=162.2987
  - rt2=17.5123
  - sel=0.0000
  - st1=0.2968
  - st2=17.5126
  - startup_cost=4537.3400
  - total_cost=37339.2600
- **Output:** st=29.11, rt=231.69

### Step 5: Node 5630 (Index Scan) - LEAF

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

### Step 6: Node 5625 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=101119
  - nt1=46998
  - nt2=3
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=231.6890
  - rt2=-0.0185
  - sel=0.7172
  - st1=29.1115
  - st2=0.0563
  - startup_cost=4537.7700
  - total_cost=72924.7200
- **Output:** st=30.57, rt=1122.15

### Step 7: Node 5621 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 25df29b5 (Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer))
- **Consumes:** Nodes 5622, 5623, 5624
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=313469
  - Aggregate_Outer_nt1=313469
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=44
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=109973.6500
  - Aggregate_Outer_total_cost=113892.0200
  - Gather_Outer_np=0
  - Gather_Outer_nt=313469
  - Gather_Outer_nt1=101119
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=24
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.1000
  - Gather_Outer_startup_cost=5537.7700
  - Gather_Outer_total_cost=105271.6200
  - Limit_np=0
  - Limit_nt=10
  - Limit_nt1=313469
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=44
  - Limit_reltuples=0.0000
  - Limit_sel=0.0000
  - Limit_startup_cost=120665.9700
  - Limit_total_cost=120665.9900
  - Sort_Outer_np=0
  - Sort_Outer_nt=313469
  - Sort_Outer_nt1=313469
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=44
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=120665.9700
  - Sort_Outer_total_cost=121449.6400
- **Output:** st=1194.02, rt=1195.92
