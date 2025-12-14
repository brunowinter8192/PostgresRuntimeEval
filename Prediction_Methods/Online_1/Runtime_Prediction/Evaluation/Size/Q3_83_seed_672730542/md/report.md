# Online Prediction Report

**Test Query:** Q3_83_seed_672730542
**Timestamp:** 2025-12-13 02:42:55

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 68.41%

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
Node 5661 (Limit) [PATTERN: 25df29b5] - ROOT
  Node 5662 (Sort) [consumed]
    Node 5663 (Aggregate) [consumed]
      Node 5664 (Gather) [consumed]
        Node 5665 (Nested Loop)
          Node 5666 (Hash Join)
            Node 5667 (Seq Scan) - LEAF
            Node 5668 (Hash)
              Node 5669 (Seq Scan) - LEAF
          Node 5670 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 25df29b5 | 5661 | 5662, 5663, 5664 |


## Phase E: Final Prediction

- Final MRE: 0.50%
- Improvement: 67.90%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 5661 | Limit | 1189.91 | 1195.90 | 0.5% | pattern |
| 5665 | Nested Loop | 1152.40 | 1121.69 | 2.7% | operator |
| 5666 | Hash Join | 206.82 | 231.44 | 11.9% | operator |
| 5670 | Index Scan | 0.03 | -0.02 | 171.3% | operator |
| 5667 | Seq Scan | 153.52 | 162.21 | 5.7% | operator |
| 5668 | Hash | 30.71 | 17.51 | 43.0% | operator |
| 5669 | Seq Scan | 29.85 | 36.69 | 22.9% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 5669 (Seq Scan) - LEAF

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

### Step 2: Node 5667 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=233978
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=16
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1560
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=32184.3900
- **Output:** st=0.30, rt=162.21

### Step 3: Node 5668 (Hash)

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

### Step 4: Node 5666 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=46716
  - nt1=233978
  - nt2=12479
  - parallel_workers=0
  - plan_width=12
  - reltuples=0.0000
  - rt1=162.2137
  - rt2=17.5121
  - sel=0.0000
  - st1=0.2967
  - st2=17.5125
  - startup_cost=4537.2400
  - total_cost=37335.8400
- **Output:** st=29.07, rt=231.44

### Step 5: Node 5670 (Index Scan) - LEAF

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

### Step 6: Node 5665 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=101062
  - nt1=46716
  - nt2=3
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=231.4405
  - rt2=-0.0185
  - sel=0.7211
  - st1=29.0654
  - st2=0.0563
  - startup_cost=4537.6700
  - total_cost=72756.9000
- **Output:** st=30.16, rt=1121.69

### Step 7: Node 5661 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 25df29b5 (Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer))
- **Consumes:** Nodes 5662, 5663, 5664
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=313291
  - Aggregate_Outer_nt1=313291
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=44
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=109785.3700
  - Aggregate_Outer_total_cost=113701.5100
  - Gather_Outer_np=0
  - Gather_Outer_nt=313291
  - Gather_Outer_nt1=101062
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=24
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.1000
  - Gather_Outer_startup_cost=5537.6700
  - Gather_Outer_total_cost=105086.0000
  - Limit_np=0
  - Limit_nt=10
  - Limit_nt1=313291
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=44
  - Limit_reltuples=0.0000
  - Limit_sel=0.0000
  - Limit_startup_cost=120471.6100
  - Limit_total_cost=120471.6400
  - Sort_Outer_np=0
  - Sort_Outer_nt=313291
  - Sort_Outer_nt1=313291
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=44
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=120471.6100
  - Sort_Outer_total_cost=121254.8400
- **Output:** st=1194.01, rt=1195.90
