# Online Prediction Report

**Test Query:** Q3_15_seed_114856434
**Timestamp:** 2025-12-13 02:41:43

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 63.85%

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
Node 4911 (Limit) [PATTERN: 25df29b5] - ROOT
  Node 4912 (Sort) [consumed]
    Node 4913 (Aggregate) [consumed]
      Node 4914 (Gather) [consumed]
        Node 4915 (Nested Loop)
          Node 4916 (Hash Join)
            Node 4917 (Seq Scan) - LEAF
            Node 4918 (Hash)
              Node 4919 (Seq Scan) - LEAF
          Node 4920 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 25df29b5 | 4911 | 4912, 4913, 4914 |


## Phase E: Final Prediction

- Final MRE: 2.21%
- Improvement: 61.64%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 4911 | Limit | 1223.05 | 1196.02 | 2.2% | pattern |
| 4915 | Nested Loop | 1187.84 | 1121.63 | 5.6% | operator |
| 4916 | Hash Join | 210.32 | 231.08 | 9.9% | operator |
| 4920 | Index Scan | 0.03 | -0.02 | 168.7% | operator |
| 4917 | Seq Scan | 158.90 | 162.08 | 2.0% | operator |
| 4918 | Hash | 28.71 | 17.51 | 39.0% | operator |
| 4919 | Seq Scan | 28.13 | 36.65 | 30.3% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 4919 (Seq Scan) - LEAF

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

### Step 2: Node 4917 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=231924
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=16
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1546
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=32184.3900
- **Output:** st=0.30, rt=162.08

### Step 3: Node 4918 (Hash)

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

### Step 4: Node 4916 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=46677
  - nt1=231924
  - nt2=12579
  - parallel_workers=0
  - plan_width=12
  - reltuples=0.0000
  - rt1=162.0770
  - rt2=17.5136
  - sel=0.0000
  - st1=0.2963
  - st2=17.5140
  - startup_cost=4538.4900
  - total_cost=37331.7000
- **Output:** st=28.97, rt=231.08

### Step 5: Node 4920 (Index Scan) - LEAF

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

### Step 6: Node 4915 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=101761
  - nt1=46677
  - nt2=3
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=231.0796
  - rt2=-0.0185
  - sel=0.7267
  - st1=28.9749
  - st2=0.0563
  - startup_cost=4538.9200
  - total_cost=72804.1000
- **Output:** st=30.09, rt=1121.63

### Step 7: Node 4911 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 25df29b5 (Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer))
- **Consumes:** Nodes 4912, 4913, 4914
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=315460
  - Aggregate_Outer_nt1=315460
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=44
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=110082.0000
  - Aggregate_Outer_total_cost=114025.2500
  - Gather_Outer_np=0
  - Gather_Outer_nt=315460
  - Gather_Outer_nt1=101761
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=24
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.1000
  - Gather_Outer_startup_cost=5538.9200
  - Gather_Outer_total_cost=105350.1000
  - Limit_np=0
  - Limit_nt=10
  - Limit_nt1=315460
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=44
  - Limit_reltuples=0.0000
  - Limit_sel=0.0000
  - Limit_startup_cost=120842.2200
  - Limit_total_cost=120842.2500
  - Sort_Outer_np=0
  - Sort_Outer_nt=315460
  - Sort_Outer_nt1=315460
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=44
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=120842.2200
  - Sort_Outer_total_cost=121630.8700
- **Output:** st=1194.12, rt=1196.02
