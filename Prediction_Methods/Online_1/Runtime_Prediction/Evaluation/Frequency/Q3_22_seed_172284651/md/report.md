# Online Prediction Report

**Test Query:** Q3_22_seed_172284651
**Timestamp:** 2026-01-11 18:31:58

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
| 128ec77a | Sort -> Aggregate -> Gather -> Nested Lo... | 4 | 24 | 3.8% | 0.9012 |
| 925caafa | Gather -> Nested Loop -> [Hash Join (Out... | 3 | 24 | 2.7% | 0.6475 |
| 7b066ef4 | Aggregate -> Gather -> Nested Loop -> [H... | 4 | 24 | 1.2% | 0.2995 |
| b68c8b96 | Limit -> Sort -> Aggregate -> Gather -> ... | 5 | 24 | 68.3% | 16.3813 |
| 8d7fa5fd | Gather -> Nested Loop -> [Hash Join -> [... | 4 | 24 | 2.7% | 0.6475 |
| 9d8bc76c | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 24 | 3.0% | 0.7171 |
| ac6af82a | Sort -> Aggregate -> Gather -> Nested Lo... | 5 | 24 | 3.8% | 0.9012 |
| 3e93cf76 | Gather -> Nested Loop -> [Hash Join -> [... | 5 | 24 | 2.7% | 0.6475 |
| 5a77e21f | Aggregate -> Gather -> Nested Loop -> [H... | 5 | 24 | 1.2% | 0.2995 |
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
| 0 | 895c6e8c | 75736.1626 | 0.0004% | ACCEPTED | 17.92% |
| 1 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 2 | 1d35fb97 | 26.4017 | 0.1163% | ACCEPTED | 17.81% |
| 3 | f4cb205a | 75544.5822 | 0.0005% | ACCEPTED | 17.81% |
| 4 | 4fc84c77 | 13.3894 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 5 | 3cfa90d7 | 6.2375 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 6 | e0e3c3e1 | 4.0772 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 7 | e296a71f | 40.3755 | N/A | REJECTED | 17.81% |
| 8 | 7bcfec22 | 40.3755 | 0.0394% | ACCEPTED | 17.77% |
| 9 | b3a45093 | 2.9042 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 10 | 25df29b5 | 33.4481 | 9.8522% | ACCEPTED | 7.92% |
| 11 | 694ae2c3 | 0.6475 | N/A | SKIPPED_LOW_ERROR | 7.92% |
| 12 | 071a1ee5 | 0.2995 | N/A | SKIPPED_LOW_ERROR | 7.92% |
| 13 | 128ec77a | 0.9012 | N/A | SKIPPED_LOW_ERROR | 7.92% |
| 14 | 925caafa | 0.6475 | N/A | SKIPPED_LOW_ERROR | 7.92% |
| 15 | 7b066ef4 | 0.2995 | N/A | SKIPPED_LOW_ERROR | 7.92% |
| 16 | b68c8b96 | 16.3813 | -0.0154% | REJECTED | 7.92% |
| 17 | 8d7fa5fd | 0.6475 | N/A | SKIPPED_LOW_ERROR | 7.92% |
| 18 | 9d8bc76c | 0.7171 | N/A | SKIPPED_LOW_ERROR | 7.92% |
| 19 | ac6af82a | 0.9012 | N/A | SKIPPED_LOW_ERROR | 7.92% |
| 20 | 3e93cf76 | 0.6475 | N/A | SKIPPED_LOW_ERROR | 7.92% |
| 21 | 5a77e21f | 0.2995 | N/A | SKIPPED_LOW_ERROR | 7.92% |
| 22 | 5eedbd1b | 16.3813 | -0.0154% | REJECTED | 7.92% |
| 23 | 64cd7a0c | 0.9012 | N/A | SKIPPED_LOW_ERROR | 7.92% |
| 24 | ff421d05 | 0.2995 | N/A | SKIPPED_LOW_ERROR | 7.92% |
| 25 | d64c42c6 | 16.3813 | -0.0154% | REJECTED | 7.92% |
| 26 | eb451e77 | 0.9012 | N/A | SKIPPED_LOW_ERROR | 7.92% |
| 27 | ea3737ca | 16.3813 | -0.0154% | REJECTED | 7.92% |
## Query Tree

```
Node 4991 (Limit) [PATTERN: 25df29b5] - ROOT
  Node 4992 (Sort) [consumed]
    Node 4993 (Aggregate) [consumed]
      Node 4994 (Gather) [consumed]
        Node 4995 (Nested Loop)
          Node 4996 (Hash Join) [PATTERN: f4cb205a]
            Node 4997 (Seq Scan) [consumed] - LEAF
            Node 4998 (Hash) [consumed]
              Node 4999 (Seq Scan) [consumed] - LEAF
          Node 5000 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 25df29b5 | 4991 | 4992, 4993, 4994, 4996, 4997, 4998, 4999 |
| Hash Join -> [Seq Scan (Outer) | f4cb205a | 4996 | 4991, 4992, 4993, 4994, 4997, 4998, 4999 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 1.81%
- Improvement: 62.72%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 4991 | Limit | 1217.96 | 1195.90 | 1.8% | pattern |
| 4995 | Nested Loop | 1182.42 | 1121.89 | 5.1% | operator |
| 4996 | Hash Join | 210.34 | 219.19 | 4.2% | pattern |
| 5000 | Index Scan | 0.03 | -0.02 | 168.7% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 4996 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** f4cb205a (Hash Join -> [Seq Scan (Outer), Hash -> Seq Scan (Outer) (Inner)])
- **Consumes:** Nodes 4991, 4992, 4993, 4994, 4997, 4998, 4999
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=46921
  - HashJoin_nt1=235005
  - HashJoin_nt2=12479
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=12
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0000
  - HashJoin_startup_cost=4537.2400
  - HashJoin_total_cost=37338.5300
  - Hash_Inner_np=0
  - Hash_Inner_nt=12479
  - Hash_Inner_nt1=12479
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=4
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=4381.2500
  - Hash_Inner_total_cost=4381.2500
  - SeqScan_Outer_np=3600
  - SeqScan_Outer_nt=12479
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=4
  - SeqScan_Outer_reltuples=150000.0000
  - SeqScan_Outer_sel=0.0832
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=4381.2500
- **Output:** st=30.33, rt=219.19

### Step 2: Node 5000 (Index Scan) - LEAF

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

### Step 3: Node 4995 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=101013
  - nt1=46921
  - nt2=3
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=219.1871
  - rt2=-0.0185
  - sel=0.7176
  - st1=30.3267
  - st2=0.0563
  - startup_cost=4537.6700
  - total_cost=72874.9000
- **Output:** st=30.25, rt=1121.89

### Step 4: Node 4991 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 25df29b5 (Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer))
- **Consumes:** Nodes 4992, 4993, 4994, 4996, 4997, 4998, 4999
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
