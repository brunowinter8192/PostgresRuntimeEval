# Online Prediction Report

**Test Query:** Q3_101_seed_820403100
**Timestamp:** 2025-12-21 14:34:45

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 18251 | Operator + Pattern Training |
| Training_Test | 4568 | Pattern Selection Eval |
| Training | 22819 | Final Model Training |
| Test | 1500 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 73.75%

## Phase C: Patterns in Query

- Total Patterns: 28

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 428 | 15868.7% | 67917.8254 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 390 | 37912.5% | 147858.8421 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 210 | 14.6% | 30.5802 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 150 | 10.9% | 16.4241 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 142 | 6.2% | 8.8335 |
| e296a71f | Limit -> Sort (Outer) | 2 | 60 | 51.1% | 30.6535 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 180 | 37658.5% | 67785.3072 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 112 | 5.4% | 6.0355 |
| 7bcfec22 | Limit -> Sort -> Aggregate (Outer) (Oute... | 3 | 60 | 51.1% | 30.6535 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 60 | 4.7% | 2.8082 |
| 25df29b5 | Limit -> Sort -> Aggregate -> Gather (Ou... | 4 | 30 | 73.6% | 22.0884 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 67917.8254 | 0.0006% | REJECTED | 14.04% |
| 1 | 3aab37be | 147858.8421 | -0.0000% | REJECTED | 14.04% |
| 2 | 1d35fb97 | 30.5802 | -0.1018% | REJECTED | 14.04% |
| 3 | 4fc84c77 | 16.4241 | 1.9434% | ACCEPTED | 12.10% |
| 4 | 3cfa90d7 | 8.8335 | N/A | SKIPPED_LOW_ERROR | 12.10% |
| 5 | e296a71f | 30.6530 | 0.0612% | REJECTED | 12.10% |
| 6 | f4cb205a | 67785.3072 | -0.0000% | REJECTED | 12.10% |
| 7 | e0e3c3e1 | 6.0355 | N/A | SKIPPED_LOW_ERROR | 12.10% |
| 8 | 7bcfec22 | 30.6530 | 0.0470% | REJECTED | 12.10% |
| 9 | b3a45093 | 2.4097 | N/A | SKIPPED_LOW_ERROR | 12.10% |
| 10 | 25df29b5 | 22.0879 | 5.5781% | ACCEPTED | 6.52% |
## Query Tree

```
Node 4361 (Limit) [PATTERN: 25df29b5] - ROOT
  Node 4362 (Sort) [consumed]
    Node 4363 (Aggregate) [consumed]
      Node 4364 (Gather) [consumed]
        Node 4365 (Nested Loop)
          Node 4366 (Hash Join)
            Node 4367 (Seq Scan) - LEAF
            Node 4368 (Hash)
              Node 4369 (Seq Scan) - LEAF
          Node 4370 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 25df29b5 | 4361 | 4362, 4363, 4364 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 2.85%
- Improvement: 70.90%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 4361 | Limit | 1184.97 | 1151.18 | 2.9% | pattern |
| 4365 | Nested Loop | 1149.55 | 1192.44 | 3.7% | operator |
| 4366 | Hash Join | 208.87 | 230.23 | 10.2% | operator |
| 4370 | Index Scan | 0.03 | -0.52 | 2092.6% | operator |
| 4367 | Seq Scan | 157.01 | 163.20 | 3.9% | operator |
| 4368 | Hash | 29.21 | 17.75 | 39.2% | operator |
| 4369 | Seq Scan | 28.61 | 38.60 | 34.9% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 4369 (Seq Scan) - LEAF

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

### Step 2: Node 4367 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=232493
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=16
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1550
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=32184.3900
- **Output:** st=0.29, rt=163.20

### Step 3: Node 4368 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=12397
  - nt1=12397
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=38.6032
  - rt2=0.0000
  - sel=1.0000
  - st1=0.2638
  - st2=0.0000
  - startup_cost=4381.2500
  - total_cost=4381.2500
- **Output:** st=17.75, rt=17.75

### Step 4: Node 4366 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=46114
  - nt1=232493
  - nt2=12397
  - parallel_workers=0
  - plan_width=12
  - reltuples=0.0000
  - rt1=163.2037
  - rt2=17.7478
  - sel=0.0000
  - st1=0.2910
  - st2=17.7473
  - startup_cost=4536.2100
  - total_cost=37330.9200
- **Output:** st=27.14, rt=230.23

### Step 5: Node 4370 (Index Scan) - LEAF

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

### Step 6: Node 4365 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=100323
  - nt1=46114
  - nt2=3
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=230.2284
  - rt2=-0.5181
  - sel=0.7252
  - st1=27.1400
  - st2=0.0584
  - startup_cost=4536.6400
  - total_cost=72353.1900
- **Output:** st=121.17, rt=1192.44

### Step 7: Node 4361 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 25df29b5 (Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer))
- **Consumes:** Nodes 4362, 4363, 4364
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=311001
  - Aggregate_Outer_nt1=311001
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=44
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=109118.3000
  - Aggregate_Outer_total_cost=113005.8100
  - Gather_Outer_np=0
  - Gather_Outer_nt=311001
  - Gather_Outer_nt1=100323
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=24
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.1000
  - Gather_Outer_startup_cost=5536.6400
  - Gather_Outer_total_cost=104453.2900
  - Limit_np=0
  - Limit_nt=10
  - Limit_nt1=311001
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=44
  - Limit_reltuples=0.0000
  - Limit_sel=0.0000
  - Limit_startup_cost=119726.4300
  - Limit_total_cost=119726.4600
  - Sort_Outer_np=0
  - Sort_Outer_nt=311001
  - Sort_Outer_nt1=311001
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=44
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=119726.4300
  - Sort_Outer_total_cost=120503.9400
- **Output:** st=1150.42, rt=1151.18
