# Online Prediction Report

**Test Query:** Q18_27_seed_213304806
**Timestamp:** 2025-12-22 06:52:52

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 28.78%

## Phase C: Patterns in Query

- Total Patterns: 67

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| 3e2d5a00 | Sort -> Hash Join (Outer) | 2 | 96 | 19.3% | 18.5586 |
| e296a71f | Limit -> Sort (Outer) | 2 | 72 | 56.1% | 40.3755 |
| 7bcfec22 | Limit -> Sort -> Aggregate (Outer) (Oute... | 3 | 72 | 56.1% | 40.3755 |
| ddb1e0ca | Sort -> Aggregate -> Gather Merge (Outer... | 3 | 48 | 28.5% | 13.6847 |
| 44ca42df | Gather Merge -> Incremental Sort (Outer) | 2 | 24 | 54.5% | 13.0757 |
| 8a78742e | Incremental Sort -> Nested Loop (Outer) | 2 | 24 | 0.6% | 0.1344 |
| 4b856d44 | Nested Loop -> [Merge Join (Outer), Inde... | 2 | 24 | 53.7% | 12.8846 |
| 56dc70e5 | Merge Join -> [Sort (Outer), Sort (Inner... | 2 | 24 | 0.6% | 0.1353 |
| 3e579ee9 | Hash -> Aggregate (Outer) | 2 | 24 | 92.2% | 22.1283 |
| a02337a9 | Aggregate -> Index Scan (Outer) | 2 | 24 | 52.3% | 12.5548 |
| be4808de | Sort -> Seq Scan (Outer) | 2 | 24 | 1457.3% | 349.7507 |
| 20547233 | Aggregate -> Gather Merge -> Incremental... | 3 | 24 | 56.7% | 13.5972 |
| 9156106f | Gather Merge -> Incremental Sort -> Nest... | 3 | 24 | 54.5% | 13.0757 |
| 42f3ebc2 | Incremental Sort -> Nested Loop -> [Merg... | 3 | 24 | 0.6% | 0.1344 |
| b6901c4f | Nested Loop -> [Merge Join -> [Sort (Out... | 3 | 24 | 53.7% | 12.8846 |
| 7b9e50b6 | Merge Join -> [Sort -> Hash Join (Outer)... | 3 | 24 | 0.6% | 0.1353 |
| 108510a7 | Sort -> Hash Join -> [Seq Scan (Outer), ... | 3 | 24 | 61.3% | 14.7039 |
| fa8016c8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 24 | 73.6% | 17.6637 |
| 81649f1e | Hash -> Aggregate -> Index Scan (Outer) ... | 3 | 24 | 92.2% | 22.1283 |
| fd858367 | Limit -> Sort -> Aggregate -> Gather Mer... | 4 | 24 | 28.9% | 6.9274 |
| 9609a2d3 | Sort -> Aggregate -> Gather Merge -> Inc... | 4 | 24 | 53.4% | 12.8272 |
| 5a10b80e | Aggregate -> Gather Merge -> Incremental... | 4 | 24 | 56.7% | 13.5972 |
| 77cc594c | Gather Merge -> Incremental Sort -> Nest... | 4 | 24 | 54.5% | 13.0757 |
| f7190cfe | Incremental Sort -> Nested Loop -> [Merg... | 4 | 24 | 0.6% | 0.1344 |
| 64890ff2 | Nested Loop -> [Merge Join -> [Sort -> H... | 4 | 24 | 53.7% | 12.8846 |
| cdf32396 | Merge Join -> [Sort -> Hash Join -> [Seq... | 4 | 24 | 0.6% | 0.1353 |
| b947fceb | Sort -> Hash Join -> [Seq Scan (Outer), ... | 4 | 24 | 61.3% | 14.7039 |
| c50b85fa | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 24 | 73.6% | 17.6637 |
| 6ce7e974 | Limit -> Sort -> Aggregate -> Gather Mer... | 5 | 24 | 28.9% | 6.9274 |
| 0591a930 | Sort -> Aggregate -> Gather Merge -> Inc... | 5 | 24 | 53.4% | 12.8272 |
| fe1d68e6 | Aggregate -> Gather Merge -> Incremental... | 5 | 24 | 56.7% | 13.5972 |
| 1f89191d | Gather Merge -> Incremental Sort -> Nest... | 5 | 24 | 54.5% | 13.0757 |
| da27e563 | Incremental Sort -> Nested Loop -> [Merg... | 5 | 24 | 0.6% | 0.1344 |
| 757104e0 | Nested Loop -> [Merge Join -> [Sort -> H... | 5 | 24 | 53.7% | 12.8846 |
| 21ad4177 | Merge Join -> [Sort -> Hash Join -> [Seq... | 5 | 24 | 0.6% | 0.1353 |
| da164244 | Sort -> Hash Join -> [Seq Scan (Outer), ... | 5 | 24 | 61.3% | 14.7039 |
| 3f59a731 | Limit -> Sort -> Aggregate -> Gather Mer... | 6 | 24 | 28.9% | 6.9274 |
| 9aab693e | Sort -> Aggregate -> Gather Merge -> Inc... | 6 | 24 | 53.4% | 12.8272 |
| 3833e018 | Aggregate -> Gather Merge -> Incremental... | 6 | 24 | 56.7% | 13.5972 |
| f632c59a | Gather Merge -> Incremental Sort -> Nest... | 6 | 24 | 54.5% | 13.0757 |
| ae2eedbb | Incremental Sort -> Nested Loop -> [Merg... | 6 | 24 | 0.6% | 0.1344 |
| f97027ec | Nested Loop -> [Merge Join -> [Sort -> H... | 6 | 24 | 53.7% | 12.8846 |
| 5dab29bd | Merge Join -> [Sort -> Hash Join -> [Seq... | 6 | 24 | 0.6% | 0.1353 |
| 0aa5463f | Limit -> Sort -> Aggregate -> Gather Mer... | 7 | 24 | 28.9% | 6.9274 |
| 697afc49 | Sort -> Aggregate -> Gather Merge -> Inc... | 7 | 24 | 53.4% | 12.8272 |
| bf6e7b10 | Aggregate -> Gather Merge -> Incremental... | 7 | 24 | 56.7% | 13.5972 |
| a7f0dd84 | Gather Merge -> Incremental Sort -> Nest... | 7 | 24 | 54.5% | 13.0757 |
| c66d3a14 | Incremental Sort -> Nested Loop -> [Merg... | 7 | 24 | 0.6% | 0.1344 |
| d3e76c7b | Nested Loop -> [Merge Join -> [Sort -> H... | 7 | 24 | 53.7% | 12.8846 |
| f62c331d | Limit -> Sort -> Aggregate -> Gather Mer... | 8 | 24 | 28.9% | 6.9274 |
| 8b13b27f | Sort -> Aggregate -> Gather Merge -> Inc... | 8 | 24 | 53.4% | 12.8272 |
| 249a576d | Aggregate -> Gather Merge -> Incremental... | 8 | 24 | 56.7% | 13.5972 |
| 0564d0b3 | Gather Merge -> Incremental Sort -> Nest... | 8 | 24 | 54.5% | 13.0757 |
| b06f5887 | Incremental Sort -> Nested Loop -> [Merg... | 8 | 24 | 0.6% | 0.1344 |
| 530c0110 | Limit -> Sort -> Aggregate -> Gather Mer... | 9 | 24 | 28.9% | 6.9274 |
| c4e52017 | Sort -> Aggregate -> Gather Merge -> Inc... | 9 | 24 | 53.4% | 12.8272 |
| 053642a5 | Aggregate -> Gather Merge -> Incremental... | 9 | 24 | 56.7% | 13.5972 |
| e2c63171 | Gather Merge -> Incremental Sort -> Nest... | 9 | 24 | 54.5% | 13.0757 |
| 3f0eb924 | Limit -> Sort -> Aggregate -> Gather Mer... | 10 | 24 | 28.9% | 6.9274 |
| fd242865 | Sort -> Aggregate -> Gather Merge -> Inc... | 10 | 24 | 53.4% | 12.8272 |
| f4f9ccef | Aggregate -> Gather Merge -> Incremental... | 10 | 24 | 56.7% | 13.5972 |
| 267d3d4e | Limit -> Sort -> Aggregate -> Gather Mer... | 11 | 24 | 28.9% | 6.9274 |
| e32c11b5 | Sort -> Aggregate -> Gather Merge -> Inc... | 11 | 24 | 53.4% | 12.8272 |
| f27bf3b8 | Limit -> Sort -> Aggregate -> Gather Mer... | 12 | 24 | 28.9% | 6.9274 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 1 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 2 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 3 | 3e2d5a00 | 18.5586 | 0.0007% | REJECTED | 17.92% |
| 4 | e296a71f | 40.3755 | 0.0412% | REJECTED | 17.92% |
| 5 | 7bcfec22 | 40.3755 | 0.0356% | REJECTED | 17.92% |
| 6 | ddb1e0ca | 13.6847 | -5.3651% | REJECTED | 17.92% |
| 7 | 44ca42df | 13.0757 | 0.0003% | REJECTED | 17.92% |
| 8 | 8a78742e | 0.1344 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 9 | 4b856d44 | 12.8846 | 0.0000% | REJECTED | 17.92% |
| 10 | 56dc70e5 | 0.1353 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 11 | 3e579ee9 | 22.1283 | N/A | REJECTED | 17.92% |
| 12 | a02337a9 | 12.5548 | N/A | REJECTED | 17.92% |
| 13 | be4808de | 349.7507 | N/A | REJECTED | 17.92% |
| 14 | 20547233 | 13.5972 | 0.0050% | REJECTED | 17.92% |
| 15 | 9156106f | 13.0757 | 0.0003% | REJECTED | 17.92% |
| 16 | 42f3ebc2 | 0.1344 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 17 | b6901c4f | 12.8846 | 0.0000% | REJECTED | 17.92% |
| 18 | 7b9e50b6 | 0.1353 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 19 | 108510a7 | 14.7039 | N/A | REJECTED | 17.92% |
| 20 | fa8016c8 | 17.6637 | N/A | REJECTED | 17.92% |
| 21 | 81649f1e | 22.1283 | N/A | REJECTED | 17.92% |
| 22 | fd858367 | 6.9274 | 2.0277% | ACCEPTED | 15.90% |
| 23 | f7190cfe | 0.1344 | N/A | SKIPPED_LOW_ERROR | 15.90% |
| 24 | 64890ff2 | 12.8846 | N/A | REJECTED | 15.90% |
| 25 | cdf32396 | 0.1353 | N/A | SKIPPED_LOW_ERROR | 15.90% |
| 26 | b947fceb | 14.7039 | N/A | REJECTED | 15.90% |
| 27 | c50b85fa | 17.6637 | N/A | REJECTED | 15.90% |
| 28 | 6ce7e974 | 0.1143 | N/A | SKIPPED_LOW_ERROR | 15.90% |
| 29 | da27e563 | 0.1344 | N/A | SKIPPED_LOW_ERROR | 15.90% |
| 30 | 757104e0 | 12.8846 | N/A | REJECTED | 15.90% |
| 31 | 21ad4177 | 0.1353 | N/A | SKIPPED_LOW_ERROR | 15.90% |
| 32 | da164244 | 14.7039 | N/A | REJECTED | 15.90% |
| 33 | 3f59a731 | 0.1143 | N/A | SKIPPED_LOW_ERROR | 15.90% |
| 34 | ae2eedbb | 0.1344 | N/A | SKIPPED_LOW_ERROR | 15.90% |
| 35 | f97027ec | 12.8846 | N/A | REJECTED | 15.90% |
| 36 | 5dab29bd | 0.1353 | N/A | SKIPPED_LOW_ERROR | 15.90% |
| 37 | 0aa5463f | 0.1143 | N/A | SKIPPED_LOW_ERROR | 15.90% |
| 38 | c66d3a14 | 0.1344 | N/A | SKIPPED_LOW_ERROR | 15.90% |
| 39 | d3e76c7b | 12.8846 | N/A | REJECTED | 15.90% |
| 40 | f62c331d | 0.1143 | N/A | SKIPPED_LOW_ERROR | 15.90% |
| 41 | b06f5887 | 0.1344 | N/A | SKIPPED_LOW_ERROR | 15.90% |
| 42 | 530c0110 | 0.1143 | N/A | SKIPPED_LOW_ERROR | 15.90% |
| 43 | 3f0eb924 | 0.1143 | N/A | SKIPPED_LOW_ERROR | 15.90% |
| 44 | 267d3d4e | 0.1143 | N/A | SKIPPED_LOW_ERROR | 15.90% |
| 45 | f27bf3b8 | 0.1143 | N/A | SKIPPED_LOW_ERROR | 15.90% |
## Query Tree

```
Node 29924 (Limit) [PATTERN: fd858367] - ROOT
  Node 29925 (Sort) [consumed]
    Node 29926 (Aggregate) [consumed]
      Node 29927 (Gather Merge) [consumed]
        Node 29928 (Incremental Sort)
          Node 29929 (Nested Loop)
            Node 29930 (Merge Join)
              Node 29931 (Sort)
                Node 29932 (Hash Join)
                  Node 29933 (Seq Scan) - LEAF
                  Node 29934 (Hash)
                    Node 29935 (Aggregate)
                      Node 29936 (Index Scan) - LEAF
              Node 29937 (Sort)
                Node 29938 (Seq Scan) - LEAF
            Node 29939 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | fd858367 | 29924 | 29925, 29926, 29927 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 0.21%
- Improvement: 28.57%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 29924 | Limit | 3043.82 | 3050.24 | 0.2% | pattern |
| 29928 | Incremental Sort | 2911.65 | 2910.23 | 0.0% | operator |
| 29929 | Nested Loop | 2911.59 | 1400.02 | 51.9% | operator |
| 29930 | Merge Join | 2911.53 | 2910.61 | 0.0% | operator |
| 29939 | Index Scan | 0.02 | 0.07 | 199.9% | operator |
| 29931 | Sort | 2838.57 | 1098.75 | 61.3% | operator |
| 29937 | Sort | 68.58 | 1014.60 | 1379.3% | operator |
| 29932 | Hash Join | 2838.56 | 773.67 | 72.7% | operator |
| 29938 | Seq Scan | 55.06 | 25.47 | 53.7% | operator |
| 29933 | Seq Scan | 185.11 | 187.11 | 1.1% | operator |
| 29934 | Hash | 2622.85 | 255.35 | 90.3% | operator |
| 29935 | Aggregate | 2622.79 | 1300.21 | 50.4% | operator |
| 29936 | Index Scan | 2118.58 | 219.99 | 89.6% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 29936 (Index Scan) - LEAF

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

### Step 2: Node 29935 (Aggregate)

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

### Step 3: Node 29933 (Seq Scan) - LEAF

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

### Step 4: Node 29934 (Hash)

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

### Step 5: Node 29932 (Hash Join)

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

### Step 6: Node 29938 (Seq Scan) - LEAF

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

### Step 7: Node 29931 (Sort)

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

### Step 8: Node 29937 (Sort)

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

### Step 9: Node 29930 (Merge Join)

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

### Step 10: Node 29939 (Index Scan) - LEAF

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

### Step 11: Node 29929 (Nested Loop)

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

### Step 12: Node 29928 (Incremental Sort)

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

### Step 13: Node 29924 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** fd858367 (Limit -> Sort -> Aggregate -> Gather Merge (Outer) (Outer) (Outer))
- **Consumes:** Nodes 29925, 29926, 29927
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
