# Online Prediction Report

**Test Query:** Q18_133_seed_1082932092
**Timestamp:** 2026-01-11 16:37:20

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

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| 3e2d5a00 | Sort -> Hash Join (Outer) | 2 | 96 | 19.3% | 18.5586 |
| e296a71f | Limit -> Sort (Outer) | 2 | 72 | 56.1% | 40.3755 |
| 3e579ee9 | Hash -> Aggregate (Outer) | 2 | 24 | 92.2% | 22.1283 |
| 44ca42df | Gather Merge -> Incremental Sort (Outer) | 2 | 24 | 54.5% | 13.0757 |
| 8a78742e | Incremental Sort -> Nested Loop (Outer) | 2 | 24 | 0.6% | 0.1344 |
| a02337a9 | Aggregate -> Index Scan (Outer) | 2 | 24 | 52.3% | 12.5548 |
| be4808de | Sort -> Seq Scan (Outer) | 2 | 24 | 1457.3% | 349.7507 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| 7bcfec22 | Limit -> Sort -> Aggregate (Outer) (Oute... | 3 | 72 | 56.1% | 40.3755 |
| ddb1e0ca | Sort -> Aggregate -> Gather Merge (Outer... | 3 | 48 | 28.5% | 13.6847 |
| 20547233 | Aggregate -> Gather Merge -> Incremental... | 3 | 24 | 56.7% | 13.5972 |
| 4b856d44 | Nested Loop -> [Merge Join (Outer), Inde... | 2 | 24 | 53.7% | 12.8846 |
| 56dc70e5 | Merge Join -> [Sort (Outer), Sort (Inner... | 2 | 24 | 0.6% | 0.1353 |
| 81649f1e | Hash -> Aggregate -> Index Scan (Outer) ... | 3 | 24 | 92.2% | 22.1283 |
| 9156106f | Gather Merge -> Incremental Sort -> Nest... | 3 | 24 | 54.5% | 13.0757 |
| 108510a7 | Sort -> Hash Join -> [Seq Scan (Outer), ... | 3 | 24 | 61.3% | 14.7039 |
| 42f3ebc2 | Incremental Sort -> Nested Loop -> [Merg... | 3 | 24 | 0.6% | 0.1344 |
| 5a10b80e | Aggregate -> Gather Merge -> Incremental... | 4 | 24 | 56.7% | 13.5972 |
| 9609a2d3 | Sort -> Aggregate -> Gather Merge -> Inc... | 4 | 24 | 53.4% | 12.8272 |
| fa8016c8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 24 | 73.6% | 17.6637 |
| fd858367 | Limit -> Sort -> Aggregate -> Gather Mer... | 4 | 24 | 28.9% | 6.9274 |
| 0591a930 | Sort -> Aggregate -> Gather Merge -> Inc... | 5 | 24 | 53.4% | 12.8272 |
| 6ce7e974 | Limit -> Sort -> Aggregate -> Gather Mer... | 5 | 24 | 28.9% | 6.9274 |
| 77cc594c | Gather Merge -> Incremental Sort -> Nest... | 4 | 24 | 54.5% | 13.0757 |
| 7b9e50b6 | Merge Join -> [Sort -> Hash Join (Outer)... | 3 | 24 | 0.6% | 0.1353 |
| b6901c4f | Nested Loop -> [Merge Join -> [Sort (Out... | 3 | 24 | 53.7% | 12.8846 |
| b947fceb | Sort -> Hash Join -> [Seq Scan (Outer), ... | 4 | 24 | 61.3% | 14.7039 |
| c50b85fa | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 24 | 73.6% | 17.6637 |
| 3f59a731 | Limit -> Sort -> Aggregate -> Gather Mer... | 6 | 24 | 28.9% | 6.9274 |
| da164244 | Sort -> Hash Join -> [Seq Scan (Outer), ... | 5 | 24 | 61.3% | 14.7039 |
| f7190cfe | Incremental Sort -> Nested Loop -> [Merg... | 4 | 24 | 0.6% | 0.1344 |
| fe1d68e6 | Aggregate -> Gather Merge -> Incremental... | 5 | 24 | 56.7% | 13.5972 |
| 1f89191d | Gather Merge -> Incremental Sort -> Nest... | 5 | 24 | 54.5% | 13.0757 |
| 64890ff2 | Nested Loop -> [Merge Join -> [Sort -> H... | 4 | 24 | 53.7% | 12.8846 |
| 9aab693e | Sort -> Aggregate -> Gather Merge -> Inc... | 6 | 24 | 53.4% | 12.8272 |
| cdf32396 | Merge Join -> [Sort -> Hash Join -> [Seq... | 4 | 24 | 0.6% | 0.1353 |
| 0aa5463f | Limit -> Sort -> Aggregate -> Gather Mer... | 7 | 24 | 28.9% | 6.9274 |
| 21ad4177 | Merge Join -> [Sort -> Hash Join -> [Seq... | 5 | 24 | 0.6% | 0.1353 |
| 3833e018 | Aggregate -> Gather Merge -> Incremental... | 6 | 24 | 56.7% | 13.5972 |
| da27e563 | Incremental Sort -> Nested Loop -> [Merg... | 5 | 24 | 0.6% | 0.1344 |
| 5dab29bd | Merge Join -> [Sort -> Hash Join -> [Seq... | 6 | 24 | 0.6% | 0.1353 |
| 697afc49 | Sort -> Aggregate -> Gather Merge -> Inc... | 7 | 24 | 53.4% | 12.8272 |
| 757104e0 | Nested Loop -> [Merge Join -> [Sort -> H... | 5 | 24 | 53.7% | 12.8846 |
| f632c59a | Gather Merge -> Incremental Sort -> Nest... | 6 | 24 | 54.5% | 13.0757 |
| ae2eedbb | Incremental Sort -> Nested Loop -> [Merg... | 6 | 24 | 0.6% | 0.1344 |
| bf6e7b10 | Aggregate -> Gather Merge -> Incremental... | 7 | 24 | 56.7% | 13.5972 |
| f62c331d | Limit -> Sort -> Aggregate -> Gather Mer... | 8 | 24 | 28.9% | 6.9274 |
| f97027ec | Nested Loop -> [Merge Join -> [Sort -> H... | 6 | 24 | 53.7% | 12.8846 |
| 8b13b27f | Sort -> Aggregate -> Gather Merge -> Inc... | 8 | 24 | 53.4% | 12.8272 |
| a7f0dd84 | Gather Merge -> Incremental Sort -> Nest... | 7 | 24 | 54.5% | 13.0757 |
| c66d3a14 | Incremental Sort -> Nested Loop -> [Merg... | 7 | 24 | 0.6% | 0.1344 |
| d3e76c7b | Nested Loop -> [Merge Join -> [Sort -> H... | 7 | 24 | 53.7% | 12.8846 |
| 0564d0b3 | Gather Merge -> Incremental Sort -> Nest... | 8 | 24 | 54.5% | 13.0757 |
| 249a576d | Aggregate -> Gather Merge -> Incremental... | 8 | 24 | 56.7% | 13.5972 |
| 530c0110 | Limit -> Sort -> Aggregate -> Gather Mer... | 9 | 24 | 28.9% | 6.9274 |
| b06f5887 | Incremental Sort -> Nested Loop -> [Merg... | 8 | 24 | 0.6% | 0.1344 |
| 053642a5 | Aggregate -> Gather Merge -> Incremental... | 9 | 24 | 56.7% | 13.5972 |
| c4e52017 | Sort -> Aggregate -> Gather Merge -> Inc... | 9 | 24 | 53.4% | 12.8272 |
| e2c63171 | Gather Merge -> Incremental Sort -> Nest... | 9 | 24 | 54.5% | 13.0757 |
| 3f0eb924 | Limit -> Sort -> Aggregate -> Gather Mer... | 10 | 24 | 28.9% | 6.9274 |
| f4f9ccef | Aggregate -> Gather Merge -> Incremental... | 10 | 24 | 56.7% | 13.5972 |
| fd242865 | Sort -> Aggregate -> Gather Merge -> Inc... | 10 | 24 | 53.4% | 12.8272 |
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
| 0 | 1d35fb97 | 26.4017 | 0.1167% | ACCEPTED | 17.81% |
| 1 | 2724c080 | 19.6008 | 0.0346% | ACCEPTED | 17.77% |
| 2 | 3e2d5a00 | 18.5586 | N/A | REJECTED | 17.77% |
| 3 | e296a71f | 40.3755 | N/A | REJECTED | 17.77% |
| 4 | 3e579ee9 | 22.1283 | N/A | REJECTED | 17.77% |
| 5 | 44ca42df | 13.0757 | N/A | REJECTED | 17.77% |
| 6 | 8a78742e | 0.1344 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 7 | a02337a9 | 12.5548 | N/A | REJECTED | 17.77% |
| 8 | be4808de | 349.7507 | N/A | REJECTED | 17.77% |
| 9 | 895c6e8c | 75736.1626 | 0.0001% | ACCEPTED | 17.77% |
| 10 | 7bcfec22 | 40.3755 | 0.0394% | ACCEPTED | 17.73% |
| 11 | ddb1e0ca | 13.6847 | -5.5461% | REJECTED | 17.73% |
| 12 | 20547233 | 13.5972 | N/A | REJECTED | 17.73% |
| 13 | 4b856d44 | 12.8846 | N/A | REJECTED | 17.73% |
| 14 | 56dc70e5 | 0.1353 | N/A | SKIPPED_LOW_ERROR | 17.73% |
| 15 | 81649f1e | 22.1283 | N/A | REJECTED | 17.73% |
| 16 | 9156106f | 13.0757 | N/A | REJECTED | 17.73% |
| 17 | 108510a7 | 14.7039 | N/A | REJECTED | 17.73% |
| 18 | 42f3ebc2 | 0.1344 | N/A | SKIPPED_LOW_ERROR | 17.73% |
| 19 | 5a10b80e | 13.5972 | -0.0716% | REJECTED | 17.73% |
| 20 | 9609a2d3 | 12.8272 | 0.0071% | ACCEPTED | 17.73% |
| 21 | fa8016c8 | 17.6637 | N/A | REJECTED | 17.73% |
| 22 | fd858367 | 6.9274 | N/A | REJECTED | 17.73% |
| 23 | 0591a930 | 12.8272 | N/A | REJECTED | 17.73% |
| 24 | 6ce7e974 | 6.9274 | 1.9440% | ACCEPTED | 15.78% |
| 25 | 77cc594c | 13.0757 | N/A | REJECTED | 15.78% |
| 26 | 7b9e50b6 | 0.1353 | N/A | SKIPPED_LOW_ERROR | 15.78% |
| 27 | b6901c4f | 12.8846 | N/A | REJECTED | 15.78% |
| 28 | b947fceb | 14.7039 | N/A | REJECTED | 15.78% |
| 29 | c50b85fa | 17.6637 | N/A | REJECTED | 15.78% |
| 30 | 3f59a731 | 6.9274 | N/A | REJECTED | 15.78% |
| 31 | da164244 | 14.7039 | N/A | REJECTED | 15.78% |
| 32 | f7190cfe | 0.1344 | N/A | SKIPPED_LOW_ERROR | 15.78% |
| 33 | fe1d68e6 | 13.5972 | N/A | REJECTED | 15.78% |
| 34 | 1f89191d | 13.0757 | N/A | REJECTED | 15.78% |
| 35 | 64890ff2 | 12.8846 | N/A | REJECTED | 15.78% |
| 36 | 9aab693e | 12.8272 | -1.9440% | REJECTED | 15.78% |
| 37 | cdf32396 | 0.1353 | N/A | SKIPPED_LOW_ERROR | 15.78% |
| 38 | 0aa5463f | 6.9274 | N/A | REJECTED | 15.78% |
| 39 | 21ad4177 | 0.1353 | N/A | SKIPPED_LOW_ERROR | 15.78% |
| 40 | 3833e018 | 13.5972 | -2.0226% | REJECTED | 15.78% |
| 41 | da27e563 | 0.1344 | N/A | SKIPPED_LOW_ERROR | 15.78% |
| 42 | 5dab29bd | 0.1353 | N/A | SKIPPED_LOW_ERROR | 15.78% |
| 43 | 697afc49 | 12.8272 | -1.9440% | REJECTED | 15.78% |
| 44 | 757104e0 | 12.8846 | N/A | REJECTED | 15.78% |
| 45 | f632c59a | 13.0757 | -1.9511% | REJECTED | 15.78% |
| 46 | ae2eedbb | 0.1344 | N/A | SKIPPED_LOW_ERROR | 15.78% |
| 47 | bf6e7b10 | 13.5972 | -2.0226% | REJECTED | 15.78% |
| 48 | f62c331d | 6.9274 | N/A | REJECTED | 15.78% |
| 49 | f97027ec | 12.8846 | N/A | REJECTED | 15.78% |
| 50 | 8b13b27f | 12.8272 | -1.9440% | REJECTED | 15.78% |
| 51 | a7f0dd84 | 13.0757 | -1.9511% | REJECTED | 15.78% |
| 52 | c66d3a14 | 0.1344 | N/A | SKIPPED_LOW_ERROR | 15.78% |
| 53 | d3e76c7b | 12.8846 | N/A | REJECTED | 15.78% |
| 54 | 0564d0b3 | 13.0757 | -1.9511% | REJECTED | 15.78% |
| 55 | 249a576d | 13.5972 | -2.0226% | REJECTED | 15.78% |
| 56 | 530c0110 | 6.9274 | N/A | REJECTED | 15.78% |
| 57 | b06f5887 | 0.1344 | N/A | SKIPPED_LOW_ERROR | 15.78% |
| 58 | 053642a5 | 13.5972 | -2.0226% | REJECTED | 15.78% |
| 59 | c4e52017 | 12.8272 | -1.9440% | REJECTED | 15.78% |
| 60 | e2c63171 | 13.0757 | -1.9511% | REJECTED | 15.78% |
| 61 | 3f0eb924 | 6.9274 | N/A | REJECTED | 15.78% |
| 62 | f4f9ccef | 13.5972 | -2.0226% | REJECTED | 15.78% |
| 63 | fd242865 | 12.8272 | -1.9440% | REJECTED | 15.78% |
| 64 | 267d3d4e | 6.9274 | N/A | REJECTED | 15.78% |
| 65 | e32c11b5 | 12.8272 | -1.9440% | REJECTED | 15.78% |
| 66 | f27bf3b8 | 6.9274 | N/A | REJECTED | 15.78% |
## Query Tree

```
Node 29396 (Limit) [PATTERN: 6ce7e974] - ROOT
  Node 29397 (Sort) [consumed]
    Node 29398 (Aggregate) [consumed]
      Node 29399 (Gather Merge) [consumed]
        Node 29400 (Incremental Sort) [consumed]
          Node 29401 (Nested Loop)
            Node 29402 (Merge Join)
              Node 29403 (Sort)
                Node 29404 (Hash Join) [PATTERN: 895c6e8c]
                  Node 29405 (Seq Scan) [consumed] - LEAF
                  Node 29406 (Hash) [consumed]
                    Node 29407 (Aggregate)
                      Node 29408 (Index Scan) - LEAF
              Node 29409 (Sort)
                Node 29410 (Seq Scan) - LEAF
            Node 29411 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 6ce7e974 | 29396 | 29397, 29398, 29399, 29400, 29404, 29405, 29406 |
| Hash Join -> [Seq Scan (Outer) | 895c6e8c | 29404 | 29396, 29397, 29398, 29399, 29400, 29405, 29406 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 0.33%
- Improvement: 28.36%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 29396 | Limit | 3040.06 | 3050.24 | 0.3% | pattern |
| 29401 | Nested Loop | 2893.59 | 1400.02 | 51.6% | operator |
| 29402 | Merge Join | 2893.55 | 2910.61 | 0.6% | operator |
| 29411 | Index Scan | 0.02 | 0.07 | 247.3% | operator |
| 29403 | Sort | 2841.99 | 1098.13 | 61.4% | operator |
| 29409 | Sort | 66.07 | 1014.60 | 1435.6% | operator |
| 29404 | Hash Join | 2841.97 | 688.83 | 75.8% | pattern |
| 29410 | Seq Scan | 54.21 | 25.47 | 53.0% | operator |
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

### Step 3: Node 29404 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 895c6e8c (Hash Join -> [Seq Scan (Outer), Hash (Inner)])
- **Consumes:** Nodes 29396, 29397, 29398, 29399, 29400, 29405, 29406
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

### Step 4: Node 29410 (Seq Scan) - LEAF

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

### Step 5: Node 29403 (Sort)

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

### Step 6: Node 29409 (Sort)

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

### Step 7: Node 29402 (Merge Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=131527
  - nt1=131527
  - nt2=150000
  - parallel_workers=0
  - plan_width=43
  - reltuples=0.0000
  - rt1=1098.1318
  - rt2=1014.6022
  - sel=0.0000
  - st1=1096.6068
  - st2=1014.2096
  - startup_cost=340522.3600
  - total_cost=343245.2400
- **Output:** st=2908.06, rt=2910.61

### Step 8: Node 29411 (Index Scan) - LEAF

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

### Step 9: Node 29401 (Nested Loop)

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

### Step 10: Node 29396 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 6ce7e974 (Limit -> Sort -> Aggregate -> Gather Merge -> Incremental Sort (Outer) (Outer) (Outer) (Outer))
- **Consumes:** Nodes 29397, 29398, 29399, 29400, 29404, 29405, 29406
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
