# Online Prediction Report

**Test Query:** Q3_8_seed_57428217
**Timestamp:** 2025-12-21 14:50:24

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 18251 | Operator + Pattern Training |
| Training_Test | 4568 | Pattern Selection Eval |
| Training | 22819 | Final Model Training |
| Test | 1500 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 69.26%

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
Node 5731 (Limit) [PATTERN: 25df29b5] - ROOT
  Node 5732 (Sort) [consumed]
    Node 5733 (Aggregate) [consumed]
      Node 5734 (Gather) [consumed]
        Node 5735 (Nested Loop)
          Node 5736 (Hash Join)
            Node 5737 (Seq Scan) - LEAF
            Node 5738 (Hash)
              Node 5739 (Seq Scan) - LEAF
          Node 5740 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 25df29b5 | 5731 | 5732, 5733, 5734 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 5.37%
- Improvement: 63.89%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 5731 | Limit | 1216.54 | 1151.18 | 5.4% | pattern |
| 5735 | Nested Loop | 1178.70 | 1193.13 | 1.2% | operator |
| 5736 | Hash Join | 210.83 | 230.73 | 9.4% | operator |
| 5740 | Index Scan | 0.03 | -0.52 | 2092.6% | operator |
| 5737 | Seq Scan | 157.53 | 163.36 | 3.7% | operator |
| 5738 | Hash | 30.52 | 17.75 | 41.8% | operator |
| 5739 | Seq Scan | 29.81 | 38.54 | 29.3% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 5739 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=3600
  - nt=12559
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=150000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0837
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=4381.2500
- **Output:** st=0.26, rt=38.54

### Step 2: Node 5737 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=234768
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=16
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1565
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=32184.3900
- **Output:** st=0.29, rt=163.36

### Step 3: Node 5738 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=12559
  - nt1=12559
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=38.5374
  - rt2=0.0000
  - sel=1.0000
  - st1=0.2622
  - st2=0.0000
  - startup_cost=4381.2500
  - total_cost=4381.2500
- **Output:** st=17.74, rt=17.75

### Step 4: Node 5736 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=47176
  - nt1=234768
  - nt2=12559
  - parallel_workers=0
  - plan_width=12
  - reltuples=0.0000
  - rt1=163.3622
  - rt2=17.7453
  - sel=0.0000
  - st1=0.2914
  - st2=17.7448
  - startup_cost=4538.2400
  - total_cost=37338.9100
- **Output:** st=27.18, rt=230.73

### Step 5: Node 5740 (Index Scan) - LEAF

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

### Step 6: Node 5735 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=101622
  - nt1=47176
  - nt2=3
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=230.7338
  - rt2=-0.5181
  - sel=0.7180
  - st1=27.1815
  - st2=0.0584
  - startup_cost=4538.6700
  - total_cost=73077.6900
- **Output:** st=121.81, rt=1193.13

### Step 7: Node 5731 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 25df29b5 (Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer))
- **Consumes:** Nodes 5732, 5733, 5734
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=315027
  - Aggregate_Outer_nt1=315027
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=44
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=110305.7900
  - Aggregate_Outer_total_cost=114243.6300
  - Gather_Outer_np=0
  - Gather_Outer_nt=315027
  - Gather_Outer_nt1=101622
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=24
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.1000
  - Gather_Outer_startup_cost=5538.6700
  - Gather_Outer_total_cost=105580.3900
  - Limit_np=0
  - Limit_nt=10
  - Limit_nt1=315027
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=44
  - Limit_reltuples=0.0000
  - Limit_sel=0.0000
  - Limit_startup_cost=121051.2500
  - Limit_total_cost=121051.2800
  - Sort_Outer_np=0
  - Sort_Outer_nt=315027
  - Sort_Outer_nt1=315027
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=44
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=121051.2500
  - Sort_Outer_total_cost=121838.8200
- **Output:** st=1150.42, rt=1151.18
