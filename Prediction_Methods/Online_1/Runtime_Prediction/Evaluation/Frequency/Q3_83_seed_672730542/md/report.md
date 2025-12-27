# Online Prediction Report

**Test Query:** Q3_83_seed_672730542
**Timestamp:** 2025-12-22 07:08:45

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

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 33781.0% | 113504.2307 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 168 | 44967.0% | 75544.5822 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 9.3% | 13.3894 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 140 | 4.5% | 6.2375 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 116 | 3.5% | 4.0772 |
| e296a71f | Limit -> Sort (Outer) | 2 | 72 | 56.1% | 40.3755 |
| 7bcfec22 | Limit -> Sort -> Aggregate (Outer) (Oute... | 3 | 72 | 56.1% | 40.3755 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 72 | 4.0% | 2.9042 |
| 25df29b5 | Limit -> Sort -> Aggregate -> Gather (Ou... | 4 | 48 | 69.7% | 33.4481 |
| 694ae2c3 | Gather -> Nested Loop (Outer) | 2 | 24 | 2.7% | 0.6475 |
| 071a1ee5 | Aggregate -> Gather -> Nested Loop (Oute... | 3 | 24 | 1.2% | 0.2995 |
| 925caafa | Gather -> Nested Loop -> [Hash Join (Out... | 3 | 24 | 2.7% | 0.6475 |
| 128ec77a | Sort -> Aggregate -> Gather -> Nested Lo... | 4 | 24 | 3.8% | 0.9012 |
| 7b066ef4 | Aggregate -> Gather -> Nested Loop -> [H... | 4 | 24 | 1.2% | 0.2995 |
| 8d7fa5fd | Gather -> Nested Loop -> [Hash Join -> [... | 4 | 24 | 2.7% | 0.6475 |
| 9d8bc76c | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 24 | 3.0% | 0.7171 |
| b68c8b96 | Limit -> Sort -> Aggregate -> Gather -> ... | 5 | 24 | 68.3% | 16.3813 |
| ac6af82a | Sort -> Aggregate -> Gather -> Nested Lo... | 5 | 24 | 3.8% | 0.9012 |
| 5a77e21f | Aggregate -> Gather -> Nested Loop -> [H... | 5 | 24 | 1.2% | 0.2995 |
| 3e93cf76 | Gather -> Nested Loop -> [Hash Join -> [... | 5 | 24 | 2.7% | 0.6475 |
| 5eedbd1b | Limit -> Sort -> Aggregate -> Gather -> ... | 6 | 24 | 68.3% | 16.3813 |
| 64cd7a0c | Sort -> Aggregate -> Gather -> Nested Lo... | 6 | 24 | 3.8% | 0.9012 |
| ff421d05 | Aggregate -> Gather -> Nested Loop -> [H... | 6 | 24 | 1.2% | 0.2995 |
| d64c42c6 | Limit -> Sort -> Aggregate -> Gather -> ... | 7 | 24 | 68.3% | 16.3813 |
| eb451e77 | Sort -> Aggregate -> Gather -> Nested Lo... | 7 | 24 | 3.8% | 0.9012 |
| ea3737ca | Limit -> Sort -> Aggregate -> Gather -> ... | 8 | 24 | 68.3% | 16.3813 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 1 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 2 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 3 | f4cb205a | 75544.5822 | 0.0006% | REJECTED | 17.92% |
| 4 | 4fc84c77 | 13.3894 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 5 | 3cfa90d7 | 6.2375 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 6 | e0e3c3e1 | 4.0772 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 7 | e296a71f | 40.3755 | 0.0412% | REJECTED | 17.92% |
| 8 | 7bcfec22 | 40.3755 | 0.0356% | REJECTED | 17.92% |
| 9 | b3a45093 | 2.9042 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 10 | 25df29b5 | 33.4481 | 9.8112% | ACCEPTED | 8.11% |
| 11 | 9d8bc76c | 0.7171 | N/A | SKIPPED_LOW_ERROR | 8.11% |
| 12 | b68c8b96 | 0.2810 | N/A | SKIPPED_LOW_ERROR | 8.11% |
| 13 | 5eedbd1b | 0.2810 | N/A | SKIPPED_LOW_ERROR | 8.11% |
| 14 | d64c42c6 | 0.2810 | N/A | SKIPPED_LOW_ERROR | 8.11% |
| 15 | ea3737ca | 0.2810 | N/A | SKIPPED_LOW_ERROR | 8.11% |
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


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

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
