# Online Prediction Report

**Test Query:** Q3_96_seed_779382945
**Timestamp:** 2025-12-22 03:16:57

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 64.89%

## Phase C: Patterns in Query

- Total Patterns: 28

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 33781.0% | 113504.2307 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 168 | 44967.0% | 75544.5822 |
| 7bcfec22 | Limit -> Sort -> Aggregate (Outer) (Oute... | 3 | 72 | 56.1% | 40.3755 |
| e296a71f | Limit -> Sort (Outer) | 2 | 72 | 56.1% | 40.3755 |
| 25df29b5 | Limit -> Sort -> Aggregate -> Gather (Ou... | 4 | 48 | 69.7% | 33.4481 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 5eedbd1b | Limit -> Sort -> Aggregate -> Gather -> ... | 6 | 24 | 68.3% | 16.3813 |
| b68c8b96 | Limit -> Sort -> Aggregate -> Gather -> ... | 5 | 24 | 68.3% | 16.3813 |
| d64c42c6 | Limit -> Sort -> Aggregate -> Gather -> ... | 7 | 24 | 68.3% | 16.3813 |
| ea3737ca | Limit -> Sort -> Aggregate -> Gather -> ... | 8 | 24 | 68.3% | 16.3813 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 9.3% | 13.3894 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 140 | 4.5% | 6.2375 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 116 | 3.5% | 4.0772 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 72 | 4.0% | 2.9042 |
| 128ec77a | Sort -> Aggregate -> Gather -> Nested Lo... | 4 | 24 | 3.8% | 0.9012 |
| 64cd7a0c | Sort -> Aggregate -> Gather -> Nested Lo... | 6 | 24 | 3.8% | 0.9012 |
| ac6af82a | Sort -> Aggregate -> Gather -> Nested Lo... | 5 | 24 | 3.8% | 0.9012 |
| eb451e77 | Sort -> Aggregate -> Gather -> Nested Lo... | 7 | 24 | 3.8% | 0.9012 |
| 9d8bc76c | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 24 | 3.0% | 0.7171 |
| 3e93cf76 | Gather -> Nested Loop -> [Hash Join -> [... | 5 | 24 | 2.7% | 0.6475 |
| 694ae2c3 | Gather -> Nested Loop (Outer) | 2 | 24 | 2.7% | 0.6475 |
| 8d7fa5fd | Gather -> Nested Loop -> [Hash Join -> [... | 4 | 24 | 2.7% | 0.6475 |
| 925caafa | Gather -> Nested Loop -> [Hash Join (Out... | 3 | 24 | 2.7% | 0.6475 |
| 071a1ee5 | Aggregate -> Gather -> Nested Loop (Oute... | 3 | 24 | 1.2% | 0.2995 |
| 5a77e21f | Aggregate -> Gather -> Nested Loop -> [H... | 5 | 24 | 1.2% | 0.2995 |
| 7b066ef4 | Aggregate -> Gather -> Nested Loop -> [H... | 4 | 24 | 1.2% | 0.2995 |
| ff421d05 | Aggregate -> Gather -> Nested Loop -> [H... | 6 | 24 | 1.2% | 0.2995 |

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
Node 5801 (Limit) [PATTERN: 25df29b5] - ROOT
  Node 5802 (Sort) [consumed]
    Node 5803 (Aggregate) [consumed]
      Node 5804 (Gather) [consumed]
        Node 5805 (Nested Loop)
          Node 5806 (Hash Join)
            Node 5807 (Seq Scan) - LEAF
            Node 5808 (Hash)
              Node 5809 (Seq Scan) - LEAF
          Node 5810 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 25df29b5 | 5801 | 5802, 5803, 5804 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 1.59%
- Improvement: 63.30%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 5801 | Limit | 1215.29 | 1195.92 | 1.6% | pattern |
| 5805 | Nested Loop | 1178.49 | 1121.94 | 4.8% | operator |
| 5806 | Hash Join | 205.48 | 231.57 | 12.7% | operator |
| 5810 | Index Scan | 0.03 | -0.02 | 168.7% | operator |
| 5807 | Seq Scan | 155.75 | 162.26 | 4.2% | operator |
| 5808 | Hash | 26.86 | 17.51 | 34.8% | operator |
| 5809 | Seq Scan | 26.25 | 36.69 | 39.7% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 5809 (Seq Scan) - LEAF

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

### Step 2: Node 5807 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=234610
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=16
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1564
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=32184.3900
- **Output:** st=0.30, rt=162.26

### Step 3: Node 5808 (Hash)

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

### Step 4: Node 5806 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=46872
  - nt1=234610
  - nt2=12487
  - parallel_workers=0
  - plan_width=12
  - reltuples=0.0000
  - rt1=162.2561
  - rt2=17.5123
  - sel=0.0000
  - st1=0.2968
  - st2=17.5126
  - startup_cost=4537.3400
  - total_cost=37337.6000
- **Output:** st=29.09, rt=231.57

### Step 5: Node 5810 (Index Scan) - LEAF

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

### Step 6: Node 5805 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=101124
  - nt1=46872
  - nt2=3
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=231.5659
  - rt2=-0.0185
  - sel=0.7192
  - st1=29.0878
  - st2=0.0563
  - startup_cost=4537.7700
  - total_cost=72852.2300
- **Output:** st=30.39, rt=1121.94

### Step 7: Node 5801 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 25df29b5 (Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer))
- **Consumes:** Nodes 5802, 5803, 5804
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=313485
  - Aggregate_Outer_nt1=313485
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=44
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=109903.0100
  - Aggregate_Outer_total_cost=113821.5700
  - Gather_Outer_np=0
  - Gather_Outer_nt=313485
  - Gather_Outer_nt1=101124
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=24
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.1000
  - Gather_Outer_startup_cost=5537.7700
  - Gather_Outer_total_cost=105200.7300
  - Limit_np=0
  - Limit_nt=10
  - Limit_nt1=313485
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=44
  - Limit_reltuples=0.0000
  - Limit_sel=0.0000
  - Limit_startup_cost=120595.8700
  - Limit_total_cost=120595.9000
  - Sort_Outer_np=0
  - Sort_Outer_nt=313485
  - Sort_Outer_nt1=313485
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=44
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=120595.8700
  - Sort_Outer_total_cost=121379.5800
- **Output:** st=1194.02, rt=1195.92
