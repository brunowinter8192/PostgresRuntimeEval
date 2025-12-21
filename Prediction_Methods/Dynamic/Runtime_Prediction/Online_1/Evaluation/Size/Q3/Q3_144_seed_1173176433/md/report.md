# Online Prediction Report

**Test Query:** Q3_144_seed_1173176433
**Timestamp:** 2025-12-21 14:39:50

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 18251 | Operator + Pattern Training |
| Training_Test | 4568 | Pattern Selection Eval |
| Training | 22819 | Final Model Training |
| Test | 1500 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 72.35%

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
Node 4831 (Limit) [PATTERN: 25df29b5] - ROOT
  Node 4832 (Sort) [consumed]
    Node 4833 (Aggregate) [consumed]
      Node 4834 (Gather) [consumed]
        Node 4835 (Nested Loop)
          Node 4836 (Hash Join)
            Node 4837 (Seq Scan) - LEAF
            Node 4838 (Hash)
              Node 4839 (Seq Scan) - LEAF
          Node 4840 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 25df29b5 | 4831 | 4832, 4833, 4834 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 3.65%
- Improvement: 68.70%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 4831 | Limit | 1194.74 | 1151.18 | 3.6% | pattern |
| 4835 | Nested Loop | 1153.88 | 1192.93 | 3.4% | operator |
| 4836 | Hash Join | 205.64 | 230.36 | 12.0% | operator |
| 4840 | Index Scan | 0.03 | -0.52 | 2092.6% | operator |
| 4837 | Seq Scan | 156.03 | 163.23 | 4.6% | operator |
| 4838 | Hash | 27.34 | 17.75 | 35.1% | operator |
| 4839 | Seq Scan | 26.68 | 38.53 | 44.4% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 4839 (Seq Scan) - LEAF

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
- **Output:** st=0.26, rt=38.53

### Step 2: Node 4837 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=232872
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=16
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1552
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=32184.3900
- **Output:** st=0.29, rt=163.23

### Step 3: Node 4838 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=12579
  - nt1=12579
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=38.5293
  - rt2=0.0000
  - sel=1.0000
  - st1=0.2620
  - st2=0.0000
  - startup_cost=4381.2500
  - total_cost=4381.2500
- **Output:** st=17.74, rt=17.75

### Step 4: Node 4836 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=46868
  - nt1=232872
  - nt2=12579
  - parallel_workers=0
  - plan_width=12
  - reltuples=0.0000
  - rt1=163.2299
  - rt2=17.7450
  - sel=0.0000
  - st1=0.2910
  - st2=17.7445
  - startup_cost=4538.4900
  - total_cost=37334.1900
- **Output:** st=27.12, rt=230.36

### Step 5: Node 4840 (Index Scan) - LEAF

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

### Step 6: Node 4835 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=101801
  - nt1=46868
  - nt2=3
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=230.3631
  - rt2=-0.5181
  - sel=0.7240
  - st1=27.1188
  - st2=0.0584
  - startup_cost=4538.9200
  - total_cost=72914.0600
- **Output:** st=121.61, rt=1192.93

### Step 7: Node 4831 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 25df29b5 (Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer))
- **Consumes:** Nodes 4832, 4833, 4834
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=315584
  - Aggregate_Outer_nt1=315584
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=44
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=110206.2200
  - Aggregate_Outer_total_cost=114151.0200
  - Gather_Outer_np=0
  - Gather_Outer_nt=315584
  - Gather_Outer_nt1=101801
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=24
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.1000
  - Gather_Outer_startup_cost=5538.9200
  - Gather_Outer_total_cost=105472.4600
  - Limit_np=0
  - Limit_nt=10
  - Limit_nt1=315584
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=44
  - Limit_reltuples=0.0000
  - Limit_sel=0.0000
  - Limit_startup_cost=120970.6800
  - Limit_total_cost=120970.7000
  - Sort_Outer_np=0
  - Sort_Outer_nt=315584
  - Sort_Outer_nt1=315584
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=44
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=120970.6800
  - Sort_Outer_total_cost=121759.6400
- **Output:** st=1150.42, rt=1151.18
