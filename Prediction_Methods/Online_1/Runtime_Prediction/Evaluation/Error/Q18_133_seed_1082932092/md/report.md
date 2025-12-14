# Online Prediction Report

**Test Query:** Q18_133_seed_1082932092
**Timestamp:** 2025-12-13 01:17:41

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 28.70%

## Phase C: Patterns in Query

- Total Patterns: 67

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 75736.1626 |
| be4808de | Sort -> Seq Scan (Outer) | 2 | 24 | 349.7507 |
| e296a71f | Limit -> Sort (Outer) | 2 | 72 | 40.3755 |
| 7bcfec22 | Limit -> Sort -> Aggregate (Outer) (Oute... | 3 | 72 | 40.3755 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 26.4017 |
| 3e579ee9 | Hash -> Aggregate (Outer) | 2 | 24 | 22.1283 |
| 81649f1e | Hash -> Aggregate -> Index Scan (Outer) ... | 3 | 24 | 22.1283 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 19.6008 |
| 3e2d5a00 | Sort -> Hash Join (Outer) | 2 | 96 | 18.5586 |
| fa8016c8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 24 | 17.6637 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 1 | be4808de | 349.7507 | N/A | REJECTED | 17.92% |
| 2 | e296a71f | 40.3755 | 0.0412% | REJECTED | 17.92% |
| 3 | 7bcfec22 | 40.3755 | 0.0356% | REJECTED | 17.92% |
| 4 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 5 | 3e579ee9 | 22.1283 | N/A | REJECTED | 17.92% |
| 6 | 81649f1e | 22.1283 | N/A | REJECTED | 17.92% |
| 7 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 8 | 3e2d5a00 | 18.5586 | 0.0007% | REJECTED | 17.92% |
| 9 | fa8016c8 | 17.6637 | N/A | REJECTED | 17.92% |
| 10 | c50b85fa | 17.6637 | N/A | REJECTED | 17.92% |
| 11 | 108510a7 | 14.7039 | N/A | REJECTED | 17.92% |
| 12 | b947fceb | 14.7039 | N/A | REJECTED | 17.92% |
| 13 | da164244 | 14.7039 | N/A | REJECTED | 17.92% |
| 14 | ddb1e0ca | 13.6847 | -5.3651% | REJECTED | 17.92% |
| 15 | 20547233 | 13.5972 | 0.0050% | REJECTED | 17.92% |
| 16 | 5a10b80e | 13.5972 | 0.0050% | REJECTED | 17.92% |
| 17 | fe1d68e6 | 13.5972 | 0.0050% | REJECTED | 17.92% |
| 18 | 3833e018 | 13.5972 | 0.0050% | REJECTED | 17.92% |
| 19 | bf6e7b10 | 13.5972 | 0.0050% | REJECTED | 17.92% |
| 20 | 249a576d | 13.5972 | 0.0050% | REJECTED | 17.92% |
| 21 | 053642a5 | 13.5972 | 0.0050% | REJECTED | 17.92% |
| 22 | f4f9ccef | 13.5972 | 0.0050% | REJECTED | 17.92% |
| 23 | 44ca42df | 13.0757 | 0.0003% | REJECTED | 17.92% |
| 24 | 9156106f | 13.0757 | 0.0003% | REJECTED | 17.92% |
| 25 | 77cc594c | 13.0757 | 0.0003% | REJECTED | 17.92% |
| 26 | 1f89191d | 13.0757 | 0.0003% | REJECTED | 17.92% |
| 27 | f632c59a | 13.0757 | 0.0003% | REJECTED | 17.92% |
| 28 | a7f0dd84 | 13.0757 | 0.0003% | REJECTED | 17.92% |
| 29 | 0564d0b3 | 13.0757 | 0.0003% | REJECTED | 17.92% |
| 30 | e2c63171 | 13.0757 | 0.0003% | REJECTED | 17.92% |
| 31 | 4b856d44 | 12.8846 | 0.0000% | REJECTED | 17.92% |
| 32 | b6901c4f | 12.8846 | 0.0000% | REJECTED | 17.92% |
| 33 | 64890ff2 | 12.8846 | 0.0000% | REJECTED | 17.92% |
| 34 | 757104e0 | 12.8846 | 0.0000% | REJECTED | 17.92% |
| 35 | f97027ec | 12.8846 | 0.0000% | REJECTED | 17.92% |
| 36 | d3e76c7b | 12.8846 | 0.0000% | REJECTED | 17.92% |
| 37 | 9609a2d3 | 12.8272 | 0.0837% | REJECTED | 17.92% |
| 38 | 0591a930 | 12.8272 | 0.0837% | REJECTED | 17.92% |
| 39 | 9aab693e | 12.8272 | 0.0837% | REJECTED | 17.92% |
| 40 | 697afc49 | 12.8272 | 0.0837% | REJECTED | 17.92% |
| 41 | 8b13b27f | 12.8272 | 0.0837% | REJECTED | 17.92% |
| 42 | c4e52017 | 12.8272 | 0.0837% | REJECTED | 17.92% |
| 43 | fd242865 | 12.8272 | 0.0837% | REJECTED | 17.92% |
| 44 | e32c11b5 | 12.8272 | 0.0837% | REJECTED | 17.92% |
| 45 | a02337a9 | 12.5548 | N/A | REJECTED | 17.92% |
| 46 | fd858367 | 6.9274 | 2.0277% | ACCEPTED | 15.90% |
## Query Tree

```
Node 29396 (Limit) [PATTERN: fd858367] - ROOT
  Node 29397 (Sort) [consumed]
    Node 29398 (Aggregate) [consumed]
      Node 29399 (Gather Merge) [consumed]
        Node 29400 (Incremental Sort)
          Node 29401 (Nested Loop)
            Node 29402 (Merge Join)
              Node 29403 (Sort)
                Node 29404 (Hash Join)
                  Node 29405 (Seq Scan) - LEAF
                  Node 29406 (Hash)
                    Node 29407 (Aggregate)
                      Node 29408 (Index Scan) - LEAF
              Node 29409 (Sort)
                Node 29410 (Seq Scan) - LEAF
            Node 29411 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | fd858367 | 29396 | 29397, 29398, 29399 |


## Phase E: Final Prediction

- Final MRE: 0.33%
- Improvement: 28.36%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 29396 | Limit | 3040.06 | 3050.24 | 0.3% | pattern |
| 29400 | Incremental Sort | 2893.64 | 2910.23 | 0.6% | operator |
| 29401 | Nested Loop | 2893.59 | 1400.02 | 51.6% | operator |
| 29402 | Merge Join | 2893.55 | 2910.61 | 0.6% | operator |
| 29411 | Index Scan | 0.02 | 0.07 | 247.3% | operator |
| 29403 | Sort | 2841.99 | 1098.75 | 61.3% | operator |
| 29409 | Sort | 66.07 | 1014.60 | 1435.6% | operator |
| 29404 | Hash Join | 2841.97 | 773.67 | 72.8% | operator |
| 29410 | Seq Scan | 54.21 | 25.47 | 53.0% | operator |
| 29405 | Seq Scan | 194.19 | 187.11 | 3.6% | operator |
| 29406 | Hash | 2618.98 | 255.35 | 90.3% | operator |
| 29407 | Aggregate | 2618.92 | 1300.21 | 50.4% | operator |
| 29408 | Index Scan | 2155.20 | 219.99 | 89.8% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 29408 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=6001215
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=9
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.4300
  - total_cost=225647.6600
- **Output:** st=0.08, rt=219.99

### Step 2: Node 29407 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=407734
  - nt1=6001215
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=219.9901
  - rt2=0.0000
  - sel=0.0679
  - st1=0.0784
  - st2=0.0000
  - startup_cost=0.4300
  - total_cost=274001.7700
- **Output:** st=946.74, rt=1300.21

### Step 3: Node 29405 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=483871
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=20
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.3226
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=30974.7100
- **Output:** st=0.27, rt=187.11

### Step 4: Node 29406 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=407734
  - nt1=407734
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=1300.2142
  - rt2=0.0000
  - sel=1.0000
  - st1=946.7421
  - st2=0.0000
  - startup_cost=274001.7700
  - total_cost=274001.7700
- **Output:** st=255.35, rt=255.35

### Step 5: Node 29404 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=131527
  - nt1=483871
  - nt2=407734
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=187.1100
  - rt2=255.3479
  - sel=0.0000
  - st1=0.2723
  - st2=255.3471
  - startup_cost=279098.4400
  - total_cost=311343.3100
- **Output:** st=142.64, rt=773.67

### Step 6: Node 29410 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=3600
  - nt=150000
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=23
  - reltuples=150000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5100.0000
- **Output:** st=0.10, rt=25.47

### Step 7: Node 29403 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=131527
  - nt1=131527
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=773.6746
  - rt2=0.0000
  - sel=1.0000
  - st1=142.6372
  - st2=0.0000
  - startup_cost=322526.4000
  - total_cost=322855.2200
- **Output:** st=1097.31, rt=1098.75

### Step 8: Node 29409 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=150000
  - nt1=150000
  - nt2=0
  - parallel_workers=0
  - plan_width=23
  - reltuples=0.0000
  - rt1=25.4706
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0956
  - st2=0.0000
  - startup_cost=17995.9500
  - total_cost=18370.9500
- **Output:** st=1014.21, rt=1014.60

### Step 9: Node 29402 (Merge Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=131527
  - nt1=131527
  - nt2=150000
  - parallel_workers=0
  - plan_width=43
  - reltuples=0.0000
  - rt1=1098.7472
  - rt2=1014.6022
  - sel=0.0000
  - st1=1097.3073
  - st2=1014.2096
  - startup_cost=340522.3600
  - total_cost=343245.2400
- **Output:** st=2908.06, rt=2910.61

### Step 10: Node 29411 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=5
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=9
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.4300
  - total_cost=0.6100
- **Output:** st=0.02, rt=0.07

### Step 11: Node 29401 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=526215
  - nt1=131527
  - nt2=5
  - parallel_workers=0
  - plan_width=44
  - reltuples=0.0000
  - rt1=2910.6084
  - rt2=0.0660
  - sel=0.8002
  - st1=2908.0578
  - st2=0.0236
  - startup_cost=340522.8000
  - total_cost=430663.5800
- **Output:** st=339.08, rt=1400.02

### Step 12: Node 29400 (Incremental Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=526215
  - nt1=526215
  - nt2=0
  - parallel_workers=0
  - plan_width=44
  - reltuples=0.0000
  - rt1=1400.0160
  - rt2=0.0000
  - sel=1.0000
  - st1=339.0813
  - st2=0.0000
  - startup_cost=340523.4300
  - total_cost=445005.3300
- **Output:** st=2910.23, rt=2910.23

### Step 13: Node 29396 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** fd858367 (Limit -> Sort -> Aggregate -> Gather Merge (Outer) (Outer) (Outer))
- **Consumes:** Nodes 29397, 29398, 29399
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=1631266
  - Aggregate_Outer_nt1=1631266
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=71
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=341523.4700
  - Aggregate_Outer_total_cost=670304.4500
  - GatherMerge_Outer_np=0
  - GatherMerge_Outer_nt=1631266
  - GatherMerge_Outer_nt1=526215
  - GatherMerge_Outer_nt2=0
  - GatherMerge_Outer_parallel_workers=3
  - GatherMerge_Outer_plan_width=44
  - GatherMerge_Outer_reltuples=0.0000
  - GatherMerge_Outer_sel=3.1000
  - GatherMerge_Outer_startup_cost=341523.4700
  - GatherMerge_Outer_total_cost=637679.1300
  - Limit_np=0
  - Limit_nt=100
  - Limit_nt1=1631266
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=71
  - Limit_reltuples=0.0000
  - Limit_sel=0.0001
  - Limit_startup_cost=732650.2600
  - Limit_total_cost=732650.5100
  - Sort_Outer_np=0
  - Sort_Outer_nt=1631266
  - Sort_Outer_nt1=1631266
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=71
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=732650.2600
  - Sort_Outer_total_cost=736728.4200
- **Output:** st=3043.08, rt=3050.24
