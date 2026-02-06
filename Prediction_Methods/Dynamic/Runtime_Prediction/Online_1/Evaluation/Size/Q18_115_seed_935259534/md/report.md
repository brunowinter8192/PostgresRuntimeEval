# Online Prediction Report

**Test Query:** Q18_115_seed_935259534
**Timestamp:** 2026-01-18 20:20:40

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17531 | Operator + Pattern Training |
| Training_Test | 4388 | Pattern Selection Eval |
| Training | 21919 | Final Model Training |
| Test | 2400 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 62.05%

## Phase C: Patterns in Query

- Total Patterns: 67

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 210 | 6.3% | 13.1538 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 180 | 3.2% | 5.8409 |
| 3e2d5a00 | Sort -> Hash Join (Outer) | 2 | 90 | 5.4% | 4.8997 |
| e296a71f | Limit -> Sort (Outer) | 2 | 60 | 1.3% | 0.7659 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 428 | 14583.3% | 62416.6571 |
| 7bcfec22 | Limit -> Sort -> Aggregate (Outer) (Oute... | 3 | 60 | 1.3% | 0.7659 |
| ddb1e0ca | Sort -> Aggregate -> Gather Merge (Outer... | 3 | 30 | 1.2% | 0.3706 |
| fd858367 | Limit -> Sort -> Aggregate -> Gather Mer... | 4 | 0 | - | - |
| 6ce7e974 | Limit -> Sort -> Aggregate -> Gather Mer... | 5 | 0 | - | - |
| 3f59a731 | Limit -> Sort -> Aggregate -> Gather Mer... | 6 | 0 | - | - |
| 0aa5463f | Limit -> Sort -> Aggregate -> Gather Mer... | 7 | 0 | - | - |
| f62c331d | Limit -> Sort -> Aggregate -> Gather Mer... | 8 | 0 | - | - |
| 530c0110 | Limit -> Sort -> Aggregate -> Gather Mer... | 9 | 0 | - | - |
| 3f0eb924 | Limit -> Sort -> Aggregate -> Gather Mer... | 10 | 0 | - | - |
| 267d3d4e | Limit -> Sort -> Aggregate -> Gather Mer... | 11 | 0 | - | - |
| f27bf3b8 | Limit -> Sort -> Aggregate -> Gather Mer... | 12 | 0 | - | - |
| 9609a2d3 | Sort -> Aggregate -> Gather Merge -> Inc... | 4 | 0 | - | - |
| 0591a930 | Sort -> Aggregate -> Gather Merge -> Inc... | 5 | 0 | - | - |
| 9aab693e | Sort -> Aggregate -> Gather Merge -> Inc... | 6 | 0 | - | - |
| 697afc49 | Sort -> Aggregate -> Gather Merge -> Inc... | 7 | 0 | - | - |
| 8b13b27f | Sort -> Aggregate -> Gather Merge -> Inc... | 8 | 0 | - | - |
| c4e52017 | Sort -> Aggregate -> Gather Merge -> Inc... | 9 | 0 | - | - |
| fd242865 | Sort -> Aggregate -> Gather Merge -> Inc... | 10 | 0 | - | - |
| e32c11b5 | Sort -> Aggregate -> Gather Merge -> Inc... | 11 | 0 | - | - |
| 20547233 | Aggregate -> Gather Merge -> Incremental... | 3 | 0 | - | - |
| 5a10b80e | Aggregate -> Gather Merge -> Incremental... | 4 | 0 | - | - |
| fe1d68e6 | Aggregate -> Gather Merge -> Incremental... | 5 | 0 | - | - |
| 3833e018 | Aggregate -> Gather Merge -> Incremental... | 6 | 0 | - | - |
| bf6e7b10 | Aggregate -> Gather Merge -> Incremental... | 7 | 0 | - | - |
| 249a576d | Aggregate -> Gather Merge -> Incremental... | 8 | 0 | - | - |
| 053642a5 | Aggregate -> Gather Merge -> Incremental... | 9 | 0 | - | - |
| f4f9ccef | Aggregate -> Gather Merge -> Incremental... | 10 | 0 | - | - |
| 44ca42df | Gather Merge -> Incremental Sort (Outer) | 2 | 0 | - | - |
| 9156106f | Gather Merge -> Incremental Sort -> Nest... | 3 | 0 | - | - |
| 77cc594c | Gather Merge -> Incremental Sort -> Nest... | 4 | 0 | - | - |
| 1f89191d | Gather Merge -> Incremental Sort -> Nest... | 5 | 0 | - | - |
| f632c59a | Gather Merge -> Incremental Sort -> Nest... | 6 | 0 | - | - |
| a7f0dd84 | Gather Merge -> Incremental Sort -> Nest... | 7 | 0 | - | - |
| 0564d0b3 | Gather Merge -> Incremental Sort -> Nest... | 8 | 0 | - | - |
| e2c63171 | Gather Merge -> Incremental Sort -> Nest... | 9 | 0 | - | - |
| 8a78742e | Incremental Sort -> Nested Loop (Outer) | 2 | 0 | - | - |
| 42f3ebc2 | Incremental Sort -> Nested Loop -> [Merg... | 3 | 0 | - | - |
| f7190cfe | Incremental Sort -> Nested Loop -> [Merg... | 4 | 0 | - | - |
| da27e563 | Incremental Sort -> Nested Loop -> [Merg... | 5 | 0 | - | - |
| ae2eedbb | Incremental Sort -> Nested Loop -> [Merg... | 6 | 0 | - | - |
| c66d3a14 | Incremental Sort -> Nested Loop -> [Merg... | 7 | 0 | - | - |
| b06f5887 | Incremental Sort -> Nested Loop -> [Merg... | 8 | 0 | - | - |
| 4b856d44 | Nested Loop -> [Merge Join (Outer), Inde... | 2 | 0 | - | - |
| b6901c4f | Nested Loop -> [Merge Join -> [Sort (Out... | 3 | 0 | - | - |
| 64890ff2 | Nested Loop -> [Merge Join -> [Sort -> H... | 4 | 0 | - | - |
| 757104e0 | Nested Loop -> [Merge Join -> [Sort -> H... | 5 | 0 | - | - |
| f97027ec | Nested Loop -> [Merge Join -> [Sort -> H... | 6 | 0 | - | - |
| d3e76c7b | Nested Loop -> [Merge Join -> [Sort -> H... | 7 | 0 | - | - |
| 56dc70e5 | Merge Join -> [Sort (Outer), Sort (Inner... | 2 | 0 | - | - |
| 7b9e50b6 | Merge Join -> [Sort -> Hash Join (Outer)... | 3 | 0 | - | - |
| cdf32396 | Merge Join -> [Sort -> Hash Join -> [Seq... | 4 | 0 | - | - |
| 21ad4177 | Merge Join -> [Sort -> Hash Join -> [Seq... | 5 | 0 | - | - |
| 5dab29bd | Merge Join -> [Sort -> Hash Join -> [Seq... | 6 | 0 | - | - |
| 108510a7 | Sort -> Hash Join -> [Seq Scan (Outer), ... | 3 | 0 | - | - |
| b947fceb | Sort -> Hash Join -> [Seq Scan (Outer), ... | 4 | 0 | - | - |
| da164244 | Sort -> Hash Join -> [Seq Scan (Outer), ... | 5 | 0 | - | - |
| fa8016c8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 0 | - | - |
| c50b85fa | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 0 | - | - |
| 3e579ee9 | Hash -> Aggregate (Outer) | 2 | 0 | - | - |
| 81649f1e | Hash -> Aggregate -> Index Scan (Outer) ... | 3 | 0 | - | - |
| a02337a9 | Aggregate -> Index Scan (Outer) | 2 | 0 | - | - |
| be4808de | Sort -> Seq Scan (Outer) | 2 | 0 | - | - |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 1d35fb97 | 13.1538 | N/A | SKIPPED_LOW_ERROR | 5.12% |
| 1 | 2724c080 | 5.8409 | N/A | SKIPPED_LOW_ERROR | 5.12% |
| 2 | 3e2d5a00 | 4.8997 | N/A | SKIPPED_LOW_ERROR | 5.12% |
| 3 | e296a71f | 0.7659 | N/A | SKIPPED_LOW_ERROR | 5.12% |
| 4 | 895c6e8c | 62416.6571 | 0.0028% | ACCEPTED | 5.11% |
| 5 | 7bcfec22 | 0.7659 | N/A | SKIPPED_LOW_ERROR | 5.11% |
| 6 | ddb1e0ca | 0.3706 | N/A | SKIPPED_LOW_ERROR | 5.11% |
## Query Tree

```
Node 29076 (Limit) - ROOT
  Node 29077 (Sort)
    Node 29078 (Aggregate)
      Node 29079 (Gather Merge)
        Node 29080 (Incremental Sort)
          Node 29081 (Nested Loop)
            Node 29082 (Merge Join)
              Node 29083 (Sort)
                Node 29084 (Hash Join) [PATTERN: 895c6e8c]
                  Node 29085 (Seq Scan) [consumed] - LEAF
                  Node 29086 (Hash) [consumed]
                    Node 29087 (Aggregate)
                      Node 29088 (Index Scan) - LEAF
              Node 29089 (Sort)
                Node 29090 (Seq Scan) - LEAF
            Node 29091 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Hash Join -> [Seq Scan (Outer) | 895c6e8c | 29084 | 29085, 29086 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 62.05%
- Improvement: -0.00%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 29076 | Limit | 3097.12 | 1175.21 | 62.1% | operator |
| 29077 | Sort | 2982.42 | 1127.81 | 62.2% | operator |
| 29078 | Aggregate | 2982.38 | 1073.15 | 64.0% | operator |
| 29079 | Gather Merge | 2982.35 | 1073.95 | 64.0% | operator |
| 29080 | Incremental Sort | 2944.53 | 0.00 | 100.0% | operator |
| 29081 | Nested Loop | 2944.47 | 1111.34 | 62.3% | operator |
| 29082 | Merge Join | 2944.42 | 0.00 | 100.0% | operator |
| 29091 | Index Scan | 0.02 | 0.05 | 114.9% | operator |
| 29083 | Sort | 2894.77 | 1095.58 | 62.2% | operator |
| 29089 | Sort | 63.19 | 1074.66 | 1600.7% | operator |
| 29084 | Hash Join | 2894.76 | 471.07 | 83.7% | pattern |
| 29090 | Seq Scan | 51.49 | 18.25 | 64.6% | operator |
| 29087 | Aggregate | 2670.24 | 1073.15 | 59.8% | operator |
| 29088 | Index Scan | 2157.90 | 0.00 | 100.0% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 29088 (Index Scan) - LEAF

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
- **Output:** st=0.00, rt=0.00

### Step 2: Node 29087 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=407734
  - nt1=6001215
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=0.0047
  - rt2=0.0000
  - sel=0.0679
  - st1=0.0007
  - st2=0.0000
  - startup_cost=0.4300
  - total_cost=274001.7700
- **Output:** st=1069.76, rt=1073.15

### Step 3: Node 29084 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 895c6e8c (Hash Join -> [Seq Scan (Outer), Hash (Inner)])
- **Consumes:** Nodes 29085, 29086
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
- **Output:** st=57.27, rt=471.07

### Step 4: Node 29090 (Seq Scan) - LEAF

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
- **Output:** st=1.32, rt=18.25

### Step 5: Node 29083 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=131527
  - nt1=131527
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=471.0721
  - rt2=0.0000
  - sel=1.0000
  - st1=57.2667
  - st2=0.0000
  - startup_cost=322526.4000
  - total_cost=322855.2200
- **Output:** st=1094.33, rt=1095.58

### Step 6: Node 29089 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=150000
  - nt1=150000
  - nt2=0
  - parallel_workers=0
  - plan_width=23
  - reltuples=0.0000
  - rt1=18.2462
  - rt2=0.0000
  - sel=1.0000
  - st1=1.3221
  - st2=0.0000
  - startup_cost=17995.9500
  - total_cost=18370.9500
- **Output:** st=1073.84, rt=1074.66

### Step 7: Node 29082 (Merge Join)

- **Source:** operator
- **Output:** st=0.00, rt=0.00

### Step 8: Node 29091 (Index Scan) - LEAF

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
- **Output:** st=0.04, rt=0.05

### Step 9: Node 29081 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=526215
  - nt1=131527
  - nt2=5
  - parallel_workers=0
  - plan_width=44
  - reltuples=0.0000
  - rt1=0.0000
  - rt2=0.0451
  - sel=0.8002
  - st1=0.0000
  - st2=0.0433
  - startup_cost=340522.8000
  - total_cost=430663.5800
- **Output:** st=72.40, rt=1111.34

### Step 10: Node 29080 (Incremental Sort)

- **Source:** operator
- **Output:** st=0.00, rt=0.00

### Step 11: Node 29079 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=1631266
  - nt1=526215
  - nt2=0
  - parallel_workers=3
  - plan_width=44
  - reltuples=0.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=3.1000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=341523.4700
  - total_cost=637679.1300
- **Output:** st=1069.75, rt=1073.95

### Step 12: Node 29078 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=1631266
  - nt1=1631266
  - nt2=0
  - parallel_workers=0
  - plan_width=71
  - reltuples=0.0000
  - rt1=1073.9540
  - rt2=0.0000
  - sel=1.0000
  - st1=1069.7474
  - st2=0.0000
  - startup_cost=341523.4700
  - total_cost=670304.4500
- **Output:** st=1069.76, rt=1073.15

### Step 13: Node 29077 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=1631266
  - nt1=1631266
  - nt2=0
  - parallel_workers=0
  - plan_width=71
  - reltuples=0.0000
  - rt1=1073.1534
  - rt2=0.0000
  - sel=1.0000
  - st1=1069.7560
  - st2=0.0000
  - startup_cost=732650.2600
  - total_cost=736728.4200
- **Output:** st=1126.40, rt=1127.81

### Step 14: Node 29076 (Limit) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=100
  - nt1=1631266
  - nt2=0
  - parallel_workers=0
  - plan_width=71
  - reltuples=0.0000
  - rt1=1127.8063
  - rt2=0.0000
  - sel=0.0001
  - st1=1126.3987
  - st2=0.0000
  - startup_cost=732650.2600
  - total_cost=732650.5100
- **Output:** st=1173.93, rt=1175.21
