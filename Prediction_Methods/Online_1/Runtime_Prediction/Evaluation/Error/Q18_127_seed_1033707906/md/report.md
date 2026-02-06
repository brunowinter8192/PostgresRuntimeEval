# Online Prediction Report

**Test Query:** Q18_127_seed_1033707906
**Timestamp:** 2026-01-11 19:52:40

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 29.27%

## Phase C: Patterns in Query

- Total Patterns: 67

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| be4808de | Sort -> Seq Scan (Outer) | 2 | 24 | 1457.3% | 349.7507 |
| 7bcfec22 | Limit -> Sort -> Aggregate (Outer) (Oute... | 3 | 72 | 56.1% | 40.3755 |
| e296a71f | Limit -> Sort (Outer) | 2 | 72 | 56.1% | 40.3755 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 3e579ee9 | Hash -> Aggregate (Outer) | 2 | 24 | 92.2% | 22.1283 |
| 81649f1e | Hash -> Aggregate -> Index Scan (Outer) ... | 3 | 24 | 92.2% | 22.1283 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| 3e2d5a00 | Sort -> Hash Join (Outer) | 2 | 96 | 19.3% | 18.5586 |
| c50b85fa | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 24 | 73.6% | 17.6637 |
| fa8016c8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 24 | 73.6% | 17.6637 |
| 108510a7 | Sort -> Hash Join -> [Seq Scan (Outer), ... | 3 | 24 | 61.3% | 14.7039 |
| b947fceb | Sort -> Hash Join -> [Seq Scan (Outer), ... | 4 | 24 | 61.3% | 14.7039 |
| da164244 | Sort -> Hash Join -> [Seq Scan (Outer), ... | 5 | 24 | 61.3% | 14.7039 |
| ddb1e0ca | Sort -> Aggregate -> Gather Merge (Outer... | 3 | 48 | 28.5% | 13.6847 |
| 053642a5 | Aggregate -> Gather Merge -> Incremental... | 9 | 24 | 56.7% | 13.5972 |
| 20547233 | Aggregate -> Gather Merge -> Incremental... | 3 | 24 | 56.7% | 13.5972 |
| 249a576d | Aggregate -> Gather Merge -> Incremental... | 8 | 24 | 56.7% | 13.5972 |
| 3833e018 | Aggregate -> Gather Merge -> Incremental... | 6 | 24 | 56.7% | 13.5972 |
| 5a10b80e | Aggregate -> Gather Merge -> Incremental... | 4 | 24 | 56.7% | 13.5972 |
| bf6e7b10 | Aggregate -> Gather Merge -> Incremental... | 7 | 24 | 56.7% | 13.5972 |
| f4f9ccef | Aggregate -> Gather Merge -> Incremental... | 10 | 24 | 56.7% | 13.5972 |
| fe1d68e6 | Aggregate -> Gather Merge -> Incremental... | 5 | 24 | 56.7% | 13.5972 |
| 0564d0b3 | Gather Merge -> Incremental Sort -> Nest... | 8 | 24 | 54.5% | 13.0757 |
| 1f89191d | Gather Merge -> Incremental Sort -> Nest... | 5 | 24 | 54.5% | 13.0757 |
| 44ca42df | Gather Merge -> Incremental Sort (Outer) | 2 | 24 | 54.5% | 13.0757 |
| 77cc594c | Gather Merge -> Incremental Sort -> Nest... | 4 | 24 | 54.5% | 13.0757 |
| 9156106f | Gather Merge -> Incremental Sort -> Nest... | 3 | 24 | 54.5% | 13.0757 |
| a7f0dd84 | Gather Merge -> Incremental Sort -> Nest... | 7 | 24 | 54.5% | 13.0757 |
| e2c63171 | Gather Merge -> Incremental Sort -> Nest... | 9 | 24 | 54.5% | 13.0757 |
| f632c59a | Gather Merge -> Incremental Sort -> Nest... | 6 | 24 | 54.5% | 13.0757 |
| 4b856d44 | Nested Loop -> [Merge Join (Outer), Inde... | 2 | 24 | 53.7% | 12.8846 |
| 64890ff2 | Nested Loop -> [Merge Join -> [Sort -> H... | 4 | 24 | 53.7% | 12.8846 |
| 757104e0 | Nested Loop -> [Merge Join -> [Sort -> H... | 5 | 24 | 53.7% | 12.8846 |
| b6901c4f | Nested Loop -> [Merge Join -> [Sort (Out... | 3 | 24 | 53.7% | 12.8846 |
| d3e76c7b | Nested Loop -> [Merge Join -> [Sort -> H... | 7 | 24 | 53.7% | 12.8846 |
| f97027ec | Nested Loop -> [Merge Join -> [Sort -> H... | 6 | 24 | 53.7% | 12.8846 |
| 0591a930 | Sort -> Aggregate -> Gather Merge -> Inc... | 5 | 24 | 53.4% | 12.8272 |
| 697afc49 | Sort -> Aggregate -> Gather Merge -> Inc... | 7 | 24 | 53.4% | 12.8272 |
| 8b13b27f | Sort -> Aggregate -> Gather Merge -> Inc... | 8 | 24 | 53.4% | 12.8272 |
| 9609a2d3 | Sort -> Aggregate -> Gather Merge -> Inc... | 4 | 24 | 53.4% | 12.8272 |
| 9aab693e | Sort -> Aggregate -> Gather Merge -> Inc... | 6 | 24 | 53.4% | 12.8272 |
| c4e52017 | Sort -> Aggregate -> Gather Merge -> Inc... | 9 | 24 | 53.4% | 12.8272 |
| e32c11b5 | Sort -> Aggregate -> Gather Merge -> Inc... | 11 | 24 | 53.4% | 12.8272 |
| fd242865 | Sort -> Aggregate -> Gather Merge -> Inc... | 10 | 24 | 53.4% | 12.8272 |
| a02337a9 | Aggregate -> Index Scan (Outer) | 2 | 24 | 52.3% | 12.5548 |
| 0aa5463f | Limit -> Sort -> Aggregate -> Gather Mer... | 7 | 24 | 28.9% | 6.9274 |
| 267d3d4e | Limit -> Sort -> Aggregate -> Gather Mer... | 11 | 24 | 28.9% | 6.9274 |
| 3f0eb924 | Limit -> Sort -> Aggregate -> Gather Mer... | 10 | 24 | 28.9% | 6.9274 |
| 3f59a731 | Limit -> Sort -> Aggregate -> Gather Mer... | 6 | 24 | 28.9% | 6.9274 |
| 530c0110 | Limit -> Sort -> Aggregate -> Gather Mer... | 9 | 24 | 28.9% | 6.9274 |
| 6ce7e974 | Limit -> Sort -> Aggregate -> Gather Mer... | 5 | 24 | 28.9% | 6.9274 |
| f27bf3b8 | Limit -> Sort -> Aggregate -> Gather Mer... | 12 | 24 | 28.9% | 6.9274 |
| f62c331d | Limit -> Sort -> Aggregate -> Gather Mer... | 8 | 24 | 28.9% | 6.9274 |
| fd858367 | Limit -> Sort -> Aggregate -> Gather Mer... | 4 | 24 | 28.9% | 6.9274 |
| 21ad4177 | Merge Join -> [Sort -> Hash Join -> [Seq... | 5 | 24 | 0.6% | 0.1353 |
| 56dc70e5 | Merge Join -> [Sort (Outer), Sort (Inner... | 2 | 24 | 0.6% | 0.1353 |
| 5dab29bd | Merge Join -> [Sort -> Hash Join -> [Seq... | 6 | 24 | 0.6% | 0.1353 |
| 7b9e50b6 | Merge Join -> [Sort -> Hash Join (Outer)... | 3 | 24 | 0.6% | 0.1353 |
| cdf32396 | Merge Join -> [Sort -> Hash Join -> [Seq... | 4 | 24 | 0.6% | 0.1353 |
| 42f3ebc2 | Incremental Sort -> Nested Loop -> [Merg... | 3 | 24 | 0.6% | 0.1344 |
| 8a78742e | Incremental Sort -> Nested Loop (Outer) | 2 | 24 | 0.6% | 0.1344 |
| ae2eedbb | Incremental Sort -> Nested Loop -> [Merg... | 6 | 24 | 0.6% | 0.1344 |
| b06f5887 | Incremental Sort -> Nested Loop -> [Merg... | 8 | 24 | 0.6% | 0.1344 |
| c66d3a14 | Incremental Sort -> Nested Loop -> [Merg... | 7 | 24 | 0.6% | 0.1344 |
| da27e563 | Incremental Sort -> Nested Loop -> [Merg... | 5 | 24 | 0.6% | 0.1344 |
| f7190cfe | Incremental Sort -> Nested Loop -> [Merg... | 4 | 24 | 0.6% | 0.1344 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 75736.1626 | 0.0004% | ACCEPTED | 17.92% |
| 1 | be4808de | 349.7507 | N/A | REJECTED | 17.92% |
| 2 | 7bcfec22 | 40.3755 | 0.0356% | ACCEPTED | 17.89% |
| 3 | e296a71f | 40.2560 | N/A | REJECTED | 17.89% |
| 4 | 1d35fb97 | 19.4657 | 0.1202% | ACCEPTED | 17.77% |
| 5 | c50b85fa | 18.6818 | N/A | REJECTED | 17.77% |
| 6 | fa8016c8 | 18.6818 | N/A | REJECTED | 17.77% |
| 7 | 3e2d5a00 | 18.5791 | 0.0008% | ACCEPTED | 17.77% |
| 8 | 108510a7 | 14.7234 | N/A | REJECTED | 17.77% |
| 9 | b947fceb | 14.7234 | N/A | REJECTED | 17.77% |
| 10 | da164244 | 14.7234 | N/A | REJECTED | 17.77% |
| 11 | 0564d0b3 | 13.0757 | N/A | REJECTED | 17.77% |
| 12 | 1f89191d | 13.0757 | N/A | REJECTED | 17.77% |
| 13 | 44ca42df | 13.0757 | N/A | REJECTED | 17.77% |
| 14 | 77cc594c | 13.0757 | N/A | REJECTED | 17.77% |
| 15 | 9156106f | 13.0757 | N/A | REJECTED | 17.77% |
| 16 | a7f0dd84 | 13.0757 | N/A | REJECTED | 17.77% |
| 17 | e2c63171 | 13.0757 | N/A | REJECTED | 17.77% |
| 18 | f632c59a | 13.0757 | N/A | REJECTED | 17.77% |
| 19 | 4b856d44 | 12.8846 | N/A | REJECTED | 17.77% |
| 20 | 64890ff2 | 12.8846 | N/A | REJECTED | 17.77% |
| 21 | 757104e0 | 12.8846 | N/A | REJECTED | 17.77% |
| 22 | b6901c4f | 12.8846 | N/A | REJECTED | 17.77% |
| 23 | d3e76c7b | 12.8846 | N/A | REJECTED | 17.77% |
| 24 | f97027ec | 12.8846 | N/A | REJECTED | 17.77% |
| 25 | a02337a9 | 12.5548 | N/A | REJECTED | 17.77% |
| 26 | 2724c080 | 7.7817 | 0.0338% | ACCEPTED | 17.73% |
| 27 | 0aa5463f | 6.6700 | 1.9511% | ACCEPTED | 15.78% |
| 28 | ddb1e0ca | 0.8507 | -5.5461% | REJECTED | 15.78% |
| 29 | 267d3d4e | 0.1143 | N/A | REJECTED | 15.78% |
| 30 | 3f0eb924 | 0.1143 | N/A | REJECTED | 15.78% |
| 31 | 3f59a731 | 0.1143 | N/A | REJECTED | 15.78% |
| 32 | 530c0110 | 0.1143 | N/A | REJECTED | 15.78% |
| 33 | 6ce7e974 | 0.1143 | N/A | REJECTED | 15.78% |
| 34 | f27bf3b8 | 0.1143 | N/A | REJECTED | 15.78% |
| 35 | f62c331d | 0.1143 | N/A | REJECTED | 15.78% |
| 36 | fd858367 | 0.1143 | N/A | REJECTED | 15.78% |
## Query Tree

```
Node 29284 (Limit) [PATTERN: 0aa5463f] - ROOT
  Node 29285 (Sort) [consumed]
    Node 29286 (Aggregate) [consumed]
      Node 29287 (Gather Merge) [consumed]
        Node 29288 (Incremental Sort) [consumed]
          Node 29289 (Nested Loop) [consumed]
            Node 29290 (Merge Join) [consumed]
              Node 29291 (Sort)
                Node 29292 (Hash Join) [PATTERN: 895c6e8c]
                  Node 29293 (Seq Scan) [consumed] - LEAF
                  Node 29294 (Hash) [consumed]
                    Node 29295 (Aggregate)
                      Node 29296 (Index Scan) - LEAF
              Node 29297 (Sort)
                Node 29298 (Seq Scan) - LEAF
            Node 29299 (Index Scan) [consumed] - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 0aa5463f | 29284 | 29285, 29286, 29287, 29288, 29289, 29290, 29292, 29293, 29294, 29299 |
| Hash Join -> [Seq Scan (Outer) | 895c6e8c | 29292 | 29284, 29285, 29286, 29287, 29288, 29289, 29290, 29293, 29294, 29299 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 0.48%
- Improvement: 28.79%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 29284 | Limit | 3064.92 | 3050.24 | 0.5% | pattern |
| 29291 | Sort | 2862.89 | 1098.13 | 61.6% | operator |
| 29297 | Sort | 64.22 | 1014.60 | 1480.0% | operator |
| 29292 | Hash Join | 2862.88 | 688.83 | 75.9% | pattern |
| 29298 | Seq Scan | 52.73 | 25.47 | 51.7% | operator |
| 29295 | Aggregate | 2628.93 | 1300.21 | 50.5% | operator |
| 29296 | Index Scan | 2130.98 | 219.99 | 89.7% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 29296 (Index Scan) - LEAF

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

### Step 2: Node 29295 (Aggregate)

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

### Step 3: Node 29292 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 895c6e8c (Hash Join -> [Seq Scan (Outer), Hash (Inner)])
- **Consumes:** Nodes 29284, 29285, 29286, 29287, 29288, 29289, 29290, 29293, 29294, 29299
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=131527
  - HashJoin_nt1=483871
  - HashJoin_nt2=407734
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=24
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0000
  - HashJoin_startup_cost=279098.4400
  - HashJoin_total_cost=311343.3100
  - Hash_Inner_np=0
  - Hash_Inner_nt=407734
  - Hash_Inner_nt1=407734
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=4
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=274001.7700
  - Hash_Inner_total_cost=274001.7700
  - SeqScan_Outer_np=26136
  - SeqScan_Outer_nt=483871
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=20
  - SeqScan_Outer_reltuples=1500000.0000
  - SeqScan_Outer_sel=0.3226
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=30974.7100
- **Output:** st=276.92, rt=688.83

### Step 4: Node 29298 (Seq Scan) - LEAF

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

### Step 5: Node 29291 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=131527
  - nt1=131527
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=688.8337
  - rt2=0.0000
  - sel=1.0000
  - st1=276.9250
  - st2=0.0000
  - startup_cost=322526.4000
  - total_cost=322855.2200
- **Output:** st=1096.61, rt=1098.13

### Step 6: Node 29297 (Sort)

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

### Step 7: Node 29284 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 0aa5463f (Limit -> Sort -> Aggregate -> Gather Merge -> Incremental Sort -> Nested Loop -> [Merge Join (Outer), Index Scan (Inner)] (Outer) (Outer) (Outer) (Outer) (Outer))
- **Consumes:** Nodes 29285, 29286, 29287, 29288, 29289, 29290, 29292, 29293, 29294, 29299
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
  - IncrementalSort_Outer_np=0
  - IncrementalSort_Outer_nt=526215
  - IncrementalSort_Outer_nt1=526215
  - IncrementalSort_Outer_nt2=0
  - IncrementalSort_Outer_parallel_workers=0
  - IncrementalSort_Outer_plan_width=44
  - IncrementalSort_Outer_reltuples=0.0000
  - IncrementalSort_Outer_sel=1.0000
  - IncrementalSort_Outer_startup_cost=340523.4300
  - IncrementalSort_Outer_total_cost=445005.3300
  - IndexScan_Inner_np=112600
  - IndexScan_Inner_nt=5
  - IndexScan_Inner_nt1=0
  - IndexScan_Inner_nt2=0
  - IndexScan_Inner_parallel_workers=0
  - IndexScan_Inner_plan_width=9
  - IndexScan_Inner_reltuples=6001215.0000
  - IndexScan_Inner_sel=0.0000
  - IndexScan_Inner_startup_cost=0.4300
  - IndexScan_Inner_total_cost=0.6100
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
  - MergeJoin_Outer_np=0
  - MergeJoin_Outer_nt=131527
  - MergeJoin_Outer_nt1=131527
  - MergeJoin_Outer_nt2=150000
  - MergeJoin_Outer_parallel_workers=0
  - MergeJoin_Outer_plan_width=43
  - MergeJoin_Outer_reltuples=0.0000
  - MergeJoin_Outer_sel=0.0000
  - MergeJoin_Outer_startup_cost=340522.3600
  - MergeJoin_Outer_total_cost=343245.2400
  - NestedLoop_Outer_np=0
  - NestedLoop_Outer_nt=526215
  - NestedLoop_Outer_nt1=131527
  - NestedLoop_Outer_nt2=5
  - NestedLoop_Outer_parallel_workers=0
  - NestedLoop_Outer_plan_width=44
  - NestedLoop_Outer_reltuples=0.0000
  - NestedLoop_Outer_sel=0.8002
  - NestedLoop_Outer_startup_cost=340522.8000
  - NestedLoop_Outer_total_cost=430663.5800
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
