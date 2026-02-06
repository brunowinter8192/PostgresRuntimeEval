# Online Prediction Report

**Test Query:** Q8_1_seed_0101000000
**Timestamp:** 2026-01-18 18:10:36

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 16691 | Operator + Pattern Training |
| Training_Test | 4178 | Pattern Selection Eval |
| Training | 20869 | Final Model Training |
| Test | 3450 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 4.56%

## Phase C: Patterns in Query

- Total Patterns: 82

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 330 | 31979.6% | 105532.5343 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 180 | 12.9% | 23.2084 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 158 | 3454.0% | 5457.3989 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 90 | 6.8% | 6.0954 |
| 3e2d5a00 | Sort -> Hash Join (Outer) | 2 | 90 | 23.4% | 21.0975 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 368 | 24023.0% | 88404.7276 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 120 | 122.9% | 147.4435 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 112 | 3.0% | 3.3617 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 90 | 5.1% | 4.6238 |
| 98d4ff98 | Gather Merge -> Sort -> Hash Join (Outer... | 3 | 30 | 5.9% | 1.7696 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 180 | 49034.6% | 88262.2269 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 128 | 92.4% | 118.3091 |
| c0a8d3de | Hash -> Hash Join -> [Seq Scan (Outer), ... | 3 | 128 | 4246.5% | 5435.4562 |
| 91d6e559 | Sort -> Hash Join -> [Nested Loop (Outer... | 3 | 60 | 4.3% | 2.5954 |
| b149ff28 | Aggregate -> Gather Merge -> Sort -> Has... | 4 | 30 | 1.3% | 0.3955 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 112 | 3.0% | 3.3617 |
| a54055ce | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 90 | 6018.4% | 5416.5582 |
| 444761fb | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 38 | 49.7% | 18.8979 |
| 3c6d8006 | Gather Merge -> Sort -> Hash Join -> [Ne... | 4 | 30 | 5.9% | 1.7696 |
| 37515ad8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 98 | 115.9% | 113.5563 |
| bd9dfa7b | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 82 | 3.2% | 2.6341 |
| 2422d111 | Hash Join -> [Nested Loop -> [Hash Join ... | 3 | 30 | 16.6% | 4.9895 |
| 53f9aa07 | Aggregate -> Gather Merge -> Sort -> Has... | 5 | 30 | 1.3% | 0.3955 |
| 545b5e57 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 60 | 173.7% | 104.2271 |
| ec92bdaa | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 38 | 24.6% | 9.3291 |
| 12e6457c | Sort -> Hash Join -> [Nested Loop -> [Ha... | 4 | 30 | 2.1% | 0.6430 |
| 314469b0 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 5 | 30 | 39.7% | 11.9093 |
| 9d0e407c | Nested Loop -> [Hash Join -> [Seq Scan (... | 5 | 60 | 3.3% | 1.9789 |
| 4db07220 | Hash Join -> [Nested Loop -> [Hash Join ... | 4 | 30 | 16.6% | 4.9895 |
| 54cb7f90 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 6 | 30 | 39.7% | 11.9093 |
| 440e6274 | Hash Join -> [Nested Loop -> [Hash Join ... | 5 | 30 | 16.6% | 4.9895 |
| 5bfce159 | Nested Loop -> [Hash Join -> [Seq Scan (... | 6 | 30 | 5.2% | 1.5619 |
| e1d7e5b4 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 30 | 18.5% | 5.5387 |
| c302739b | Hash Join -> [Seq Scan (Outer), Hash -> ... | 7 | 30 | 18.5% | 5.5387 |
| ef93d4fc | Nested Loop -> [Hash Join -> [Seq Scan (... | 7 | 30 | 5.2% | 1.5619 |
| f4603221 | Hash Join -> [Nested Loop -> [Hash Join ... | 6 | 30 | 16.6% | 4.9895 |
| 3d4c3db9 | Hash Join -> [Nested Loop -> [Hash Join ... | 7 | 30 | 16.6% | 4.9895 |
| 5ae97df8 | Nested Loop -> [Hash Join -> [Seq Scan (... | 8 | 30 | 5.2% | 1.5619 |
| 9ce781b0 | Hash Join -> [Nested Loop -> [Hash Join ... | 8 | 30 | 16.6% | 4.9895 |
| a95bee4e | Hash Join -> [Nested Loop -> [Hash Join ... | 9 | 30 | 16.6% | 4.9895 |
| c9736a93 | Aggregate -> Gather Merge -> Sort -> Has... | 6 | 0 | - | - |
| 59f6581f | Aggregate -> Gather Merge -> Sort -> Has... | 7 | 0 | - | - |
| 7f3b31ff | Aggregate -> Gather Merge -> Sort -> Has... | 8 | 0 | - | - |
| cb7eed03 | Aggregate -> Gather Merge -> Sort -> Has... | 9 | 0 | - | - |
| b659e5bf | Aggregate -> Gather Merge -> Sort -> Has... | 10 | 0 | - | - |
| 96f339c9 | Aggregate -> Gather Merge -> Sort -> Has... | 11 | 0 | - | - |
| 9b77a70e | Aggregate -> Gather Merge -> Sort -> Has... | 12 | 0 | - | - |
| 264d1e57 | Aggregate -> Gather Merge -> Sort -> Has... | 13 | 0 | - | - |
| acd22c74 | Aggregate -> Gather Merge -> Sort -> Has... | 14 | 0 | - | - |
| db6a761f | Gather Merge -> Sort -> Hash Join -> [Ne... | 5 | 0 | - | - |
| 839648da | Gather Merge -> Sort -> Hash Join -> [Ne... | 6 | 0 | - | - |
| d8d77761 | Gather Merge -> Sort -> Hash Join -> [Ne... | 7 | 0 | - | - |
| ef63c60f | Gather Merge -> Sort -> Hash Join -> [Ne... | 8 | 0 | - | - |
| 82a8bdb2 | Gather Merge -> Sort -> Hash Join -> [Ne... | 9 | 0 | - | - |
| e31c99cb | Gather Merge -> Sort -> Hash Join -> [Ne... | 10 | 0 | - | - |
| 50ace808 | Gather Merge -> Sort -> Hash Join -> [Ne... | 11 | 0 | - | - |
| 860d9d3a | Gather Merge -> Sort -> Hash Join -> [Ne... | 12 | 0 | - | - |
| ffc3be98 | Gather Merge -> Sort -> Hash Join -> [Ne... | 13 | 0 | - | - |
| 58ed95a8 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 5 | 0 | - | - |
| be705a2d | Sort -> Hash Join -> [Nested Loop -> [Ha... | 6 | 0 | - | - |
| 5d01b240 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 7 | 0 | - | - |
| c7b8fb6d | Sort -> Hash Join -> [Nested Loop -> [Ha... | 8 | 0 | - | - |
| 1d069442 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 9 | 0 | - | - |
| d00b75d6 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 10 | 0 | - | - |
| 06857491 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 11 | 0 | - | - |
| 8febc667 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 12 | 0 | - | - |
| c5dad784 | Hash Join -> [Nested Loop -> [Hash Join ... | 4 | 0 | - | - |
| 6981af52 | Hash Join -> [Nested Loop -> [Hash Join ... | 5 | 0 | - | - |
| b88a3db4 | Hash Join -> [Nested Loop -> [Hash Join ... | 6 | 0 | - | - |
| 800ffecc | Hash Join -> [Nested Loop -> [Hash Join ... | 7 | 0 | - | - |
| 9d50c2fc | Hash Join -> [Nested Loop -> [Hash Join ... | 8 | 0 | - | - |
| cee0b988 | Hash Join -> [Nested Loop -> [Hash Join ... | 9 | 0 | - | - |
| 910f6702 | Hash Join -> [Nested Loop -> [Hash Join ... | 10 | 0 | - | - |
| fb7bcc0c | Hash Join -> [Nested Loop -> [Hash Join ... | 11 | 0 | - | - |
| f62279eb | Nested Loop -> [Hash Join -> [Nested Loo... | 3 | 0 | - | - |
| c5a9eefd | Nested Loop -> [Hash Join -> [Nested Loo... | 4 | 0 | - | - |
| 9b49df80 | Nested Loop -> [Hash Join -> [Nested Loo... | 5 | 0 | - | - |
| 45158dca | Nested Loop -> [Hash Join -> [Nested Loo... | 6 | 0 | - | - |
| 473ac852 | Nested Loop -> [Hash Join -> [Nested Loo... | 7 | 0 | - | - |
| 959de0c2 | Nested Loop -> [Hash Join -> [Nested Loo... | 8 | 0 | - | - |
| bf197fca | Nested Loop -> [Hash Join -> [Nested Loo... | 9 | 0 | - | - |
| 19fc9abd | Nested Loop -> [Hash Join -> [Nested Loo... | 10 | 0 | - | - |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 3aab37be | 105532.5343 | -0.0000% | REJECTED | 17.99% |
| 1 | 2724c080 | 23.2084 | 0.4114% | ACCEPTED | 17.58% |
| 2 | 7df893ad | 5457.3989 | -0.0000% | REJECTED | 17.58% |
| 3 | 1691f6f0 | 6.0954 | N/A | SKIPPED_LOW_ERROR | 17.58% |
| 4 | 3e2d5a00 | 21.0975 | N/A | REJECTED | 17.58% |
| 5 | 895c6e8c | 88404.7276 | 0.0009% | ACCEPTED | 17.58% |
| 6 | 2e0f44ef | 147.4435 | -0.0000% | REJECTED | 17.58% |
| 7 | 3cfa90d7 | 3.3617 | N/A | SKIPPED_LOW_ERROR | 17.58% |
| 8 | 29ee00db | 4.6238 | N/A | SKIPPED_LOW_ERROR | 17.58% |
| 9 | 98d4ff98 | 1.7696 | N/A | SKIPPED_LOW_ERROR | 17.58% |
| 10 | f4cb205a | 88262.2269 | 0.0005% | ACCEPTED | 17.58% |
| 11 | bb930825 | 118.3091 | -0.0000% | REJECTED | 17.58% |
| 12 | c0a8d3de | 5435.4562 | 0.0000% | ACCEPTED | 17.58% |
| 13 | 91d6e559 | 2.5954 | N/A | SKIPPED_LOW_ERROR | 17.58% |
| 14 | b149ff28 | 0.3955 | N/A | SKIPPED_LOW_ERROR | 17.58% |
| 15 | e0e3c3e1 | 3.3617 | N/A | SKIPPED_LOW_ERROR | 17.58% |
| 16 | a54055ce | 5416.5582 | N/A | REJECTED | 17.58% |
| 17 | 444761fb | 18.8979 | 0.0000% | ACCEPTED | 17.58% |
| 18 | 3c6d8006 | 1.7696 | N/A | SKIPPED_LOW_ERROR | 17.58% |
| 19 | 37515ad8 | 113.5563 | N/A | REJECTED | 17.58% |
| 20 | bd9dfa7b | 2.6341 | N/A | SKIPPED_LOW_ERROR | 17.58% |
| 21 | 2422d111 | 4.9895 | N/A | REJECTED | 17.58% |
| 22 | 53f9aa07 | 0.3955 | N/A | SKIPPED_LOW_ERROR | 17.58% |
| 23 | 545b5e57 | 104.2271 | N/A | REJECTED | 17.58% |
| 24 | ec92bdaa | 9.3291 | -0.0000% | REJECTED | 17.58% |
| 25 | 12e6457c | 0.6430 | N/A | SKIPPED_LOW_ERROR | 17.58% |
| 26 | 314469b0 | 11.9093 | N/A | REJECTED | 17.58% |
| 27 | 9d0e407c | 1.9789 | N/A | SKIPPED_LOW_ERROR | 17.58% |
| 28 | 4db07220 | 4.9895 | N/A | REJECTED | 17.58% |
| 29 | 54cb7f90 | 11.9093 | N/A | REJECTED | 17.58% |
| 30 | 440e6274 | 4.9895 | N/A | REJECTED | 17.58% |
| 31 | 5bfce159 | 1.5619 | N/A | SKIPPED_LOW_ERROR | 17.58% |
| 32 | e1d7e5b4 | 5.5387 | N/A | REJECTED | 17.58% |
| 33 | c302739b | 5.5387 | N/A | REJECTED | 17.58% |
| 34 | ef93d4fc | 1.5619 | N/A | SKIPPED_LOW_ERROR | 17.58% |
| 35 | f4603221 | 4.9895 | N/A | REJECTED | 17.58% |
| 36 | 3d4c3db9 | 4.9895 | N/A | REJECTED | 17.58% |
| 37 | 5ae97df8 | 1.5619 | N/A | SKIPPED_LOW_ERROR | 17.58% |
| 38 | 9ce781b0 | 4.9895 | N/A | REJECTED | 17.58% |
| 39 | a95bee4e | 4.9895 | N/A | REJECTED | 17.58% |
## Query Tree

```
Node 14604 (Aggregate) [PATTERN: 2724c080] - ROOT
  Node 14605 (Gather Merge) [consumed]
    Node 14606 (Sort)
      Node 14607 (Hash Join)
        Node 14608 (Nested Loop)
          Node 14609 (Hash Join)
            Node 14610 (Nested Loop)
              Node 14611 (Hash Join)
                Node 14612 (Seq Scan) - LEAF
                Node 14613 (Hash) [PATTERN: 444761fb]
                  Node 14614 (Hash Join) [consumed]
                    Node 14615 (Seq Scan) [consumed] - LEAF
                    Node 14616 (Hash) [consumed]
                      Node 14617 (Hash Join) [consumed]
                        Node 14618 (Seq Scan) - LEAF
                        Node 14619 (Hash)
                          Node 14620 (Seq Scan) - LEAF
              Node 14621 (Index Scan) - LEAF
            Node 14622 (Hash)
              Node 14623 (Seq Scan) - LEAF
          Node 14624 (Index Scan) - LEAF
        Node 14625 (Hash)
          Node 14626 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Hash -> Hash Join -> [Seq Scan | 444761fb | 14613 | 14604, 14605, 14614, 14615, 14616, 14617 |
| Aggregate -> Gather Merge (Out | 2724c080 | 14604 | 14605, 14613, 14614, 14615, 14616, 14617 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 8.11%
- Improvement: -3.56%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 14604 | Aggregate | 1233.79 | 1133.68 | 8.1% | pattern |
| 14606 | Sort | 1226.43 | 1046.21 | 14.7% | operator |
| 14607 | Hash Join | 1226.21 | 785.61 | 35.9% | operator |
| 14608 | Nested Loop | 1225.91 | 1198.29 | 2.3% | operator |
| 14625 | Hash | 0.01 | 13.72 | 105469.9% | operator |
| 14609 | Hash Join | 1222.21 | 785.60 | 35.7% | operator |
| 14624 | Index Scan | 0.01 | 12.42 | 206958.1% | operator |
| 14626 | Seq Scan | 0.01 | 6.51 | 72255.1% | operator |
| 14610 | Nested Loop | 1178.14 | 1198.29 | 1.7% | operator |
| 14622 | Hash | 39.41 | 19.97 | 49.3% | operator |
| 14611 | Hash Join | 214.13 | 251.67 | 17.5% | operator |
| 14621 | Index Scan | 0.04 | 2.88 | 6759.2% | operator |
| 14623 | Seq Scan | 39.30 | 48.89 | 24.4% | operator |
| 14612 | Seq Scan | 159.62 | 159.67 | 0.0% | operator |
| 14613 | Hash | 36.58 | 43.51 | 19.0% | pattern |
| 14618 | Seq Scan | 0.01 | 12.22 | 93938.0% | operator |
| 14619 | Hash | 0.17 | 18.14 | 10700.1% | operator |
| 14620 | Seq Scan | 0.17 | 23.36 | 14058.9% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 14620 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=1
  - nt=1
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=5.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.2000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=1.0600
- **Output:** st=0.26, rt=23.36

### Step 2: Node 14618 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=1
  - nt=25
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=25.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=1.2500
- **Output:** st=0.05, rt=12.22

### Step 3: Node 14619 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=1
  - nt1=1
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=23.3622
  - rt2=0.0000
  - sel=1.0000
  - st1=0.2635
  - st2=0.0000
  - startup_cost=1.0600
  - total_cost=1.0600
- **Output:** st=18.14, rt=18.14

### Step 4: Node 14612 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=147487
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=12
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0983
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=33394.0600
- **Output:** st=0.26, rt=159.67

### Step 5: Node 14613 (Hash) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 444761fb (Hash -> Hash Join -> [Seq Scan (Outer), Hash -> Hash Join (Outer) (Inner)] (Outer))
- **Consumes:** Nodes 14604, 14605, 14614, 14615, 14616, 14617
- **Input Features:**
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=5
  - HashJoin_Outer_nt1=25
  - HashJoin_Outer_nt2=1
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=4
  - HashJoin_Outer_reltuples=0.0000
  - HashJoin_Outer_sel=0.2000
  - HashJoin_Outer_startup_cost=1.0700
  - HashJoin_Outer_total_cost=2.4000
  - Hash_Inner_np=0
  - Hash_Inner_nt=5
  - Hash_Inner_nt1=5
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=4
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=2.4000
  - Hash_Inner_total_cost=2.4000
  - Hash_np=0
  - Hash_nt=12500
  - Hash_nt1=12500
  - Hash_nt2=0
  - Hash_parallel_workers=0
  - Hash_plan_width=4
  - Hash_reltuples=0.0000
  - Hash_sel=1.0000
  - Hash_startup_cost=4586.8400
  - Hash_total_cost=4586.8400
  - SeqScan_Outer_np=3600
  - SeqScan_Outer_nt=62500
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=8
  - SeqScan_Outer_reltuples=150000.0000
  - SeqScan_Outer_sel=0.4167
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=4225.0000
- **Output:** st=43.51, rt=43.51

### Step 6: Node 14611 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=29497
  - nt1=147487
  - nt2=12500
  - parallel_workers=0
  - plan_width=8
  - reltuples=0.0000
  - rt1=159.6655
  - rt2=43.5132
  - sel=0.0000
  - st1=0.2557
  - st2=43.5117
  - startup_cost=4743.0900
  - total_cost=38813.1400
- **Output:** st=26.38, rt=251.67

### Step 7: Node 14621 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=5
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.4300
  - total_cost=0.8300
- **Output:** st=0.03, rt=2.88

### Step 8: Node 14623 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=517
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0026
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=1.66, rt=48.89

### Step 9: Node 14610 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=118013
  - nt1=29497
  - nt2=5
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=251.6685
  - rt2=2.8809
  - sel=0.8002
  - st1=26.3825
  - st2=0.0327
  - startup_cost=4743.5200
  - total_cost=64785.2000
- **Output:** st=186.04, rt=1198.29

### Step 10: Node 14622 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=517
  - nt1=517
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=48.8913
  - rt2=0.0000
  - sel=1.0000
  - st1=1.6598
  - st2=0.0000
  - startup_cost=5169.6700
  - total_cost=5169.6700
- **Output:** st=19.97, rt=19.97

### Step 11: Node 14609 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=732
  - nt1=118013
  - nt2=517
  - parallel_workers=0
  - plan_width=20
  - reltuples=0.0000
  - rt1=1198.2891
  - rt2=19.9730
  - sel=0.0000
  - st1=186.0414
  - st2=19.9731
  - startup_cost=9919.6500
  - total_cost=70271.1300
- **Output:** st=113.62, rt=785.60

### Step 12: Node 14624 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=223
  - nt=1
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=10000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0001
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.2900
  - total_cost=0.3000
- **Output:** st=0.16, rt=12.42

### Step 13: Node 14626 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=1
  - nt=25
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=25.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=1.2500
- **Output:** st=0.16, rt=6.51

### Step 14: Node 14608 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=732
  - nt1=732
  - nt2=1
  - parallel_workers=0
  - plan_width=20
  - reltuples=0.0000
  - rt1=785.6048
  - rt2=12.4235
  - sel=1.0000
  - st1=113.6216
  - st2=0.1628
  - startup_cost=9919.9400
  - total_cost=70492.5900
- **Output:** st=186.04, rt=1198.29

### Step 15: Node 14625 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=25
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=6.5120
  - rt2=0.0000
  - sel=1.0000
  - st1=0.1624
  - st2=0.0000
  - startup_cost=1.2500
  - total_cost=1.2500
- **Output:** st=13.72, rt=13.72

### Step 16: Node 14607 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=732
  - nt1=732
  - nt2=25
  - parallel_workers=0
  - plan_width=148
  - reltuples=0.0000
  - rt1=1198.2891
  - rt2=13.7241
  - sel=0.0400
  - st1=186.0414
  - st2=13.7224
  - startup_cost=9921.5000
  - total_cost=70498.2300
- **Output:** st=113.62, rt=785.61

### Step 17: Node 14606 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=732
  - nt1=732
  - nt2=0
  - parallel_workers=0
  - plan_width=148
  - reltuples=0.0000
  - rt1=785.6126
  - rt2=0.0000
  - sel=1.0000
  - st1=113.6207
  - st2=0.0000
  - startup_cost=70533.0600
  - total_cost=70534.8900
- **Output:** st=1044.94, rt=1046.21

### Step 18: Node 14604 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 2724c080 (Aggregate -> Gather Merge (Outer))
- **Consumes:** Nodes 14605, 14613, 14614, 14615, 14616, 14617
- **Input Features:**
  - Aggregate_np=0
  - Aggregate_nt=2268
  - Aggregate_nt1=2268
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=64
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=1.0000
  - Aggregate_startup_cost=71533.1000
  - Aggregate_total_cost=71892.1400
  - GatherMerge_Outer_np=0
  - GatherMerge_Outer_nt=2268
  - GatherMerge_Outer_nt1=732
  - GatherMerge_Outer_nt2=0
  - GatherMerge_Outer_parallel_workers=3
  - GatherMerge_Outer_plan_width=148
  - GatherMerge_Outer_reltuples=0.0000
  - GatherMerge_Outer_sel=3.0984
  - GatherMerge_Outer_startup_cost=71533.1000
  - GatherMerge_Outer_total_cost=71801.4200
- **Output:** st=1130.69, rt=1133.68
