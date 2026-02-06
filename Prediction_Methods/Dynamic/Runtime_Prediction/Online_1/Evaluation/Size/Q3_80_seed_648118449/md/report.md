# Online Prediction Report

**Test Query:** Q3_80_seed_648118449
**Timestamp:** 2026-01-18 16:24:27

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 18251 | Operator + Pattern Training |
| Training_Test | 4568 | Pattern Selection Eval |
| Training | 22819 | Final Model Training |
| Test | 1500 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 72.87%

## Phase C: Patterns in Query

- Total Patterns: 28

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 390 | 37912.5% | 147858.8421 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 210 | 14.6% | 30.5802 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 150 | 10.9% | 16.4241 |
| e296a71f | Limit -> Sort (Outer) | 2 | 60 | 51.1% | 30.6535 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 428 | 15868.7% | 67917.8254 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 142 | 6.2% | 8.8335 |
| 7bcfec22 | Limit -> Sort -> Aggregate (Outer) (Oute... | 3 | 60 | 51.1% | 30.6535 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 60 | 4.7% | 2.8082 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 180 | 37658.5% | 67785.3072 |
| 25df29b5 | Limit -> Sort -> Aggregate -> Gather (Ou... | 4 | 30 | 73.6% | 22.0884 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 112 | 5.4% | 6.0355 |
| b68c8b96 | Limit -> Sort -> Aggregate -> Gather -> ... | 5 | 0 | - | - |
| 5eedbd1b | Limit -> Sort -> Aggregate -> Gather -> ... | 6 | 0 | - | - |
| d64c42c6 | Limit -> Sort -> Aggregate -> Gather -> ... | 7 | 0 | - | - |
| ea3737ca | Limit -> Sort -> Aggregate -> Gather -> ... | 8 | 0 | - | - |
| 128ec77a | Sort -> Aggregate -> Gather -> Nested Lo... | 4 | 0 | - | - |
| ac6af82a | Sort -> Aggregate -> Gather -> Nested Lo... | 5 | 0 | - | - |
| 64cd7a0c | Sort -> Aggregate -> Gather -> Nested Lo... | 6 | 0 | - | - |
| eb451e77 | Sort -> Aggregate -> Gather -> Nested Lo... | 7 | 0 | - | - |
| 071a1ee5 | Aggregate -> Gather -> Nested Loop (Oute... | 3 | 0 | - | - |
| 7b066ef4 | Aggregate -> Gather -> Nested Loop -> [H... | 4 | 0 | - | - |
| 5a77e21f | Aggregate -> Gather -> Nested Loop -> [H... | 5 | 0 | - | - |
| ff421d05 | Aggregate -> Gather -> Nested Loop -> [H... | 6 | 0 | - | - |
| 694ae2c3 | Gather -> Nested Loop (Outer) | 2 | 0 | - | - |
| 925caafa | Gather -> Nested Loop -> [Hash Join (Out... | 3 | 0 | - | - |
| 8d7fa5fd | Gather -> Nested Loop -> [Hash Join -> [... | 4 | 0 | - | - |
| 3e93cf76 | Gather -> Nested Loop -> [Hash Join -> [... | 5 | 0 | - | - |
| 9d8bc76c | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 0 | - | - |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 3aab37be | 147858.8421 | -0.0000% | REJECTED | 14.04% |
| 1 | 1d35fb97 | 30.5802 | -0.1018% | REJECTED | 14.04% |
| 2 | 4fc84c77 | 16.4241 | 1.9434% | ACCEPTED | 12.10% |
| 3 | e296a71f | 30.6535 | 0.0612% | ACCEPTED | 12.04% |
| 4 | 895c6e8c | 67917.8254 | 0.0004% | ACCEPTED | 12.04% |
| 5 | 3cfa90d7 | 8.8335 | N/A | SKIPPED_LOW_ERROR | 12.04% |
| 6 | 7bcfec22 | 30.6535 | -0.0142% | REJECTED | 12.04% |
| 7 | b3a45093 | 2.8082 | N/A | SKIPPED_LOW_ERROR | 12.04% |
| 8 | f4cb205a | 67785.3072 | -0.0000% | REJECTED | 12.04% |
| 9 | 25df29b5 | 22.0884 | 5.5764% | ACCEPTED | 6.46% |
| 10 | e0e3c3e1 | 6.0355 | N/A | SKIPPED_LOW_ERROR | 6.46% |
## Query Tree

```
Node 5631 (Limit) [PATTERN: 25df29b5] - ROOT
  Node 5632 (Sort) [consumed]
    Node 5633 (Aggregate) [consumed]
      Node 5634 (Gather) [consumed]
        Node 5635 (Nested Loop)
          Node 5636 (Hash Join) [PATTERN: 895c6e8c]
            Node 5637 (Seq Scan) [consumed] - LEAF
            Node 5638 (Hash) [consumed]
              Node 5639 (Seq Scan) - LEAF
          Node 5640 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 25df29b5 | 5631 | 5632, 5633, 5634, 5636, 5637, 5638 |
| Hash Join -> [Seq Scan (Outer) | 895c6e8c | 5636 | 5631, 5632, 5633, 5634, 5637, 5638 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 3.35%
- Improvement: 69.52%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 5631 | Limit | 1191.02 | 1151.18 | 3.3% | pattern |
| 5635 | Nested Loop | 1154.86 | 1192.88 | 3.3% | operator |
| 5636 | Hash Join | 210.24 | 242.44 | 15.3% | pattern |
| 5640 | Index Scan | 0.03 | -0.52 | 2092.6% | operator |
| 5639 | Seq Scan | 26.40 | 38.60 | 46.2% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 5639 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=3600
  - nt=12397
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=150000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0826
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=4381.2500
- **Output:** st=0.26, rt=38.60

### Step 2: Node 5636 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 895c6e8c (Hash Join -> [Seq Scan (Outer), Hash (Inner)])
- **Consumes:** Nodes 5631, 5632, 5633, 5634, 5637, 5638
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=46659
  - HashJoin_nt1=235242
  - HashJoin_nt2=12397
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=12
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0000
  - HashJoin_startup_cost=4536.2100
  - HashJoin_total_cost=37338.1300
  - Hash_Inner_np=0
  - Hash_Inner_nt=12397
  - Hash_Inner_nt1=12397
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=4
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=4381.2500
  - Hash_Inner_total_cost=4381.2500
  - SeqScan_Outer_np=26136
  - SeqScan_Outer_nt=235242
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=16
  - SeqScan_Outer_reltuples=1500000.0000
  - SeqScan_Outer_sel=0.1568
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=32184.3900
- **Output:** st=29.74, rt=242.44

### Step 3: Node 5640 (Index Scan) - LEAF

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
- **Output:** st=0.06, rt=-0.52

### Step 4: Node 5635 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=100390
  - nt1=46659
  - nt2=3
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=242.4408
  - rt2=-0.5181
  - sel=0.7172
  - st1=29.7355
  - st2=0.0584
  - startup_cost=4536.6400
  - total_cost=72666.9100
- **Output:** st=121.66, rt=1192.88

### Step 5: Node 5631 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 25df29b5 (Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer))
- **Consumes:** Nodes 5632, 5633, 5634, 5636, 5637, 5638
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=311210
  - Aggregate_Outer_nt1=311210
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=44
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=109456.0600
  - Aggregate_Outer_total_cost=113346.1900
  - Gather_Outer_np=0
  - Gather_Outer_nt=311210
  - Gather_Outer_nt1=100390
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=24
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.1000
  - Gather_Outer_startup_cost=5536.6400
  - Gather_Outer_total_cost=104787.9100
  - Limit_np=0
  - Limit_nt=10
  - Limit_nt1=311210
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=44
  - Limit_reltuples=0.0000
  - Limit_sel=0.0000
  - Limit_startup_cost=120071.3300
  - Limit_total_cost=120071.3500
  - Sort_Outer_np=0
  - Sort_Outer_nt=311210
  - Sort_Outer_nt1=311210
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=44
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=120071.3300
  - Sort_Outer_total_cost=120849.3500
- **Output:** st=1150.42, rt=1151.18
