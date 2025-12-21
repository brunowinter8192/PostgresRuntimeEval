# Online Prediction Report

**Test Query:** Q3_133_seed_1082932092
**Timestamp:** 2025-12-21 21:24:17

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 70.41%

## Phase C: Patterns in Query

- Total Patterns: 28

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| e296a71f | Limit -> Sort (Outer) | 2 | 72 | 56.1% | 40.3755 |
| 7bcfec22 | Limit -> Sort -> Aggregate (Outer) (Oute... | 3 | 72 | 56.1% | 40.3755 |
| 25df29b5 | Limit -> Sort -> Aggregate -> Gather (Ou... | 4 | 48 | 69.7% | 33.4481 |
| b68c8b96 | Limit -> Sort -> Aggregate -> Gather -> ... | 5 | 24 | 68.3% | 16.3813 |
| 5eedbd1b | Limit -> Sort -> Aggregate -> Gather -> ... | 6 | 24 | 68.3% | 16.3813 |
| d64c42c6 | Limit -> Sort -> Aggregate -> Gather -> ... | 7 | 24 | 68.3% | 16.3813 |
| ea3737ca | Limit -> Sort -> Aggregate -> Gather -> ... | 8 | 24 | 68.3% | 16.3813 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 72 | 4.0% | 2.9042 |
| 128ec77a | Sort -> Aggregate -> Gather -> Nested Lo... | 4 | 24 | 3.8% | 0.9012 |
| ac6af82a | Sort -> Aggregate -> Gather -> Nested Lo... | 5 | 24 | 3.8% | 0.9012 |
| 64cd7a0c | Sort -> Aggregate -> Gather -> Nested Lo... | 6 | 24 | 3.8% | 0.9012 |
| eb451e77 | Sort -> Aggregate -> Gather -> Nested Lo... | 7 | 24 | 3.8% | 0.9012 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 9.3% | 13.3894 |
| 071a1ee5 | Aggregate -> Gather -> Nested Loop (Oute... | 3 | 24 | 1.2% | 0.2995 |
| 7b066ef4 | Aggregate -> Gather -> Nested Loop -> [H... | 4 | 24 | 1.2% | 0.2995 |
| 5a77e21f | Aggregate -> Gather -> Nested Loop -> [H... | 5 | 24 | 1.2% | 0.2995 |
| ff421d05 | Aggregate -> Gather -> Nested Loop -> [H... | 6 | 24 | 1.2% | 0.2995 |
| 694ae2c3 | Gather -> Nested Loop (Outer) | 2 | 24 | 2.7% | 0.6475 |
| 925caafa | Gather -> Nested Loop -> [Hash Join (Out... | 3 | 24 | 2.7% | 0.6475 |
| 8d7fa5fd | Gather -> Nested Loop -> [Hash Join -> [... | 4 | 24 | 2.7% | 0.6475 |
| 3e93cf76 | Gather -> Nested Loop -> [Hash Join -> [... | 5 | 24 | 2.7% | 0.6475 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 140 | 4.5% | 6.2375 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 116 | 3.5% | 4.0772 |
| 9d8bc76c | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 24 | 3.0% | 0.7171 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 168 | 44967.0% | 75544.5822 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 33781.0% | 113504.2307 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 1 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 2 | f4cb205a | 75544.5822 | 0.0006% | REJECTED | 17.92% |
| 3 | 7bcfec22 | 40.3755 | 0.0356% | REJECTED | 17.92% |
| 4 | e296a71f | 40.3755 | 0.0412% | REJECTED | 17.92% |
| 5 | 25df29b5 | 33.4481 | 9.8112% | ACCEPTED | 8.11% |
| 6 | 1d35fb97 | 33.3258 | 0.1176% | REJECTED | 8.11% |
| 7 | 4fc84c77 | 18.7042 | 0.7529% | ACCEPTED | 7.36% |
| 8 | 3cfa90d7 | 6.2375 | N/A | SKIPPED_LOW_ERROR | 7.36% |
| 9 | e0e3c3e1 | 4.0772 | N/A | SKIPPED_LOW_ERROR | 7.36% |
| 10 | b3a45093 | 3.8683 | N/A | SKIPPED_LOW_ERROR | 7.36% |
| 11 | 9d8bc76c | 0.7171 | N/A | SKIPPED_LOW_ERROR | 7.36% |
| 12 | 5eedbd1b | 0.2810 | N/A | SKIPPED_LOW_ERROR | 7.36% |
| 13 | b68c8b96 | 0.2810 | N/A | SKIPPED_LOW_ERROR | 7.36% |
| 14 | d64c42c6 | 0.2810 | N/A | SKIPPED_LOW_ERROR | 7.36% |
| 15 | ea3737ca | 0.2810 | N/A | SKIPPED_LOW_ERROR | 7.36% |
## Query Tree

```
Node 4711 (Limit) [PATTERN: 25df29b5] - ROOT
  Node 4712 (Sort) [consumed]
    Node 4713 (Aggregate) [consumed]
      Node 4714 (Gather) [consumed]
        Node 4715 (Nested Loop)
          Node 4716 (Hash Join)
            Node 4717 (Seq Scan) - LEAF
            Node 4718 (Hash)
              Node 4719 (Seq Scan) - LEAF
          Node 4720 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 25df29b5 | 4711 | 4712, 4713, 4714 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 1.70%
- Improvement: 68.71%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 4711 | Limit | 1175.92 | 1195.93 | 1.7% | pattern |
| 4715 | Nested Loop | 1138.83 | 1122.80 | 1.4% | operator |
| 4716 | Hash Join | 208.61 | 232.11 | 11.3% | operator |
| 4720 | Index Scan | 0.03 | -0.02 | 174.1% | operator |
| 4717 | Seq Scan | 156.25 | 162.45 | 4.0% | operator |
| 4718 | Hash | 28.68 | 17.51 | 38.9% | operator |
| 4719 | Seq Scan | 27.95 | 36.69 | 31.3% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 4719 (Seq Scan) - LEAF

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

### Step 2: Node 4717 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=237422
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=16
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1583
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=32184.3900
- **Output:** st=0.30, rt=162.45

### Step 3: Node 4718 (Hash)

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

### Step 4: Node 4716 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=47404
  - nt1=237422
  - nt2=12479
  - parallel_workers=0
  - plan_width=12
  - reltuples=0.0000
  - rt1=162.4467
  - rt2=17.5121
  - sel=0.0000
  - st1=0.2972
  - st2=17.5125
  - startup_cost=4537.2400
  - total_cost=37344.8800
- **Output:** st=29.19, rt=232.11

### Step 5: Node 4720 (Index Scan) - LEAF

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

### Step 6: Node 4715 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=101139
  - nt1=47404
  - nt2=3
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=232.1144
  - rt2=-0.0185
  - sel=0.7112
  - st1=29.1948
  - st2=0.0563
  - startup_cost=4537.6700
  - total_cost=73153.0100
- **Output:** st=31.16, rt=1122.80

### Step 7: Node 4711 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 25df29b5 (Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer))
- **Consumes:** Nodes 4712, 4713, 4714
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=313530
  - Aggregate_Outer_nt1=313530
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=44
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=110208.9600
  - Aggregate_Outer_total_cost=114128.0800
  - Gather_Outer_np=0
  - Gather_Outer_nt=313530
  - Gather_Outer_nt1=101139
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=24
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.1000
  - Gather_Outer_startup_cost=5537.6700
  - Gather_Outer_total_cost=105506.0100
  - Limit_np=0
  - Limit_nt=10
  - Limit_nt1=313530
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=44
  - Limit_reltuples=0.0000
  - Limit_sel=0.0000
  - Limit_startup_cost=120903.3500
  - Limit_total_cost=120903.3800
  - Sort_Outer_np=0
  - Sort_Outer_nt=313530
  - Sort_Outer_nt1=313530
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=44
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=120903.3500
  - Sort_Outer_total_cost=121687.1800
- **Output:** st=1194.03, rt=1195.93
