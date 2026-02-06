# Online Prediction Report

**Test Query:** Q9_5_seed_32816124
**Timestamp:** 2026-01-18 19:09:22

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17280 | Operator + Pattern Training |
| Training_Test | 4320 | Pattern Selection Eval |
| Training | 21600 | Final Model Training |
| Test | 2719 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 6.81%

## Phase C: Patterns in Query

- Total Patterns: 56

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 360 | 40658.7% | 146371.3776 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 210 | 14.4% | 30.2509 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 180 | 4284.6% | 7712.2590 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 150 | 5.7% | 8.5422 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 90 | 3.4% | 3.0966 |
| 3b447875 | Aggregate -> Nested Loop (Outer) | 2 | 30 | 10.6% | 3.1651 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 420 | 12818.3% | 53836.8732 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 150 | 9.7% | 14.5467 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 150 | 4.6% | 6.8991 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 90 | 8.1% | 7.2489 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 90 | 11.3% | 10.1670 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 60 | 3.5% | 2.1270 |
| 7d4e78be | Hash Join -> [Hash Join (Outer), Hash (I... | 2 | 30 | 5.5% | 1.6532 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 150 | 79.2% | 118.8648 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 120 | 3.5% | 4.1629 |
| bd9dfa7b | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 90 | 3.8% | 3.3937 |
| 2873b8c3 | Hash Join -> [Nested Loop -> [Seq Scan (... | 3 | 30 | 3.4% | 1.0295 |
| 30d6e09b | Hash Join -> [Hash Join -> [Nested Loop ... | 3 | 30 | 5.5% | 1.6532 |
| 7a51ce50 | Hash Join -> [Hash Join -> [Nested Loop ... | 4 | 30 | 5.5% | 1.6532 |
| 6e659102 | Sort -> Aggregate -> Gather -> Aggregate... | 4 | 0 | - | - |
| a70c5941 | Sort -> Aggregate -> Gather -> Aggregate... | 5 | 0 | - | - |
| e9a32a5c | Sort -> Aggregate -> Gather -> Aggregate... | 6 | 0 | - | - |
| 9e770981 | Sort -> Aggregate -> Gather -> Aggregate... | 7 | 0 | - | - |
| d8d0a254 | Sort -> Aggregate -> Gather -> Aggregate... | 8 | 0 | - | - |
| 4d81a89d | Sort -> Aggregate -> Gather -> Aggregate... | 9 | 0 | - | - |
| 76ab422a | Sort -> Aggregate -> Gather -> Aggregate... | 10 | 0 | - | - |
| f1e59da5 | Sort -> Aggregate -> Gather -> Aggregate... | 11 | 0 | - | - |
| 0405d50f | Aggregate -> Gather -> Aggregate -> Nest... | 4 | 0 | - | - |
| 6e1ec341 | Aggregate -> Gather -> Aggregate -> Nest... | 5 | 0 | - | - |
| 51640d13 | Aggregate -> Gather -> Aggregate -> Nest... | 6 | 0 | - | - |
| 366e9db5 | Aggregate -> Gather -> Aggregate -> Nest... | 7 | 0 | - | - |
| 88dc07c3 | Aggregate -> Gather -> Aggregate -> Nest... | 8 | 0 | - | - |
| c94fcfda | Aggregate -> Gather -> Aggregate -> Nest... | 9 | 0 | - | - |
| 1c7aa67e | Aggregate -> Gather -> Aggregate -> Nest... | 10 | 0 | - | - |
| 3ac23d41 | Gather -> Aggregate -> Nested Loop (Oute... | 3 | 0 | - | - |
| 43da7031 | Gather -> Aggregate -> Nested Loop -> [H... | 4 | 0 | - | - |
| a4e25603 | Gather -> Aggregate -> Nested Loop -> [H... | 5 | 0 | - | - |
| 6ac77a36 | Gather -> Aggregate -> Nested Loop -> [H... | 6 | 0 | - | - |
| d60fddc6 | Gather -> Aggregate -> Nested Loop -> [H... | 7 | 0 | - | - |
| 75cf2f59 | Gather -> Aggregate -> Nested Loop -> [H... | 8 | 0 | - | - |
| f17356e6 | Gather -> Aggregate -> Nested Loop -> [H... | 9 | 0 | - | - |
| 4251e9b4 | Aggregate -> Nested Loop -> [Hash Join (... | 3 | 0 | - | - |
| 69ec2c4a | Aggregate -> Nested Loop -> [Hash Join -... | 4 | 0 | - | - |
| 6b2db56d | Aggregate -> Nested Loop -> [Hash Join -... | 5 | 0 | - | - |
| 7378d2b2 | Aggregate -> Nested Loop -> [Hash Join -... | 6 | 0 | - | - |
| 2af8b806 | Aggregate -> Nested Loop -> [Hash Join -... | 7 | 0 | - | - |
| 5305e2e5 | Aggregate -> Nested Loop -> [Hash Join -... | 8 | 0 | - | - |
| 7b7172dc | Nested Loop -> [Hash Join -> [Seq Scan (... | 5 | 0 | - | - |
| 3dbdd75b | Nested Loop -> [Hash Join -> [Seq Scan (... | 6 | 0 | - | - |
| dc9f4b49 | Nested Loop -> [Hash Join -> [Seq Scan (... | 7 | 0 | - | - |
| e941d0ad | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 0 | - | - |
| 49ae7e42 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 0 | - | - |
| ed7f2e45 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 0 | - | - |
| 1a17c7f7 | Hash -> Hash Join -> [Hash Join (Outer),... | 3 | 0 | - | - |
| fee45978 | Hash -> Hash Join -> [Hash Join -> [Nest... | 4 | 0 | - | - |
| 702e1a46 | Hash -> Hash Join -> [Hash Join -> [Nest... | 5 | 0 | - | - |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 3aab37be | 146371.3776 | -0.0000% | REJECTED | 17.17% |
| 1 | 1d35fb97 | 30.2509 | 0.2650% | ACCEPTED | 16.90% |
| 2 | 7df893ad | 7712.2590 | -0.0000% | REJECTED | 16.90% |
| 3 | 4fc84c77 | 8.5422 | N/A | SKIPPED_LOW_ERROR | 16.90% |
| 4 | 634cdbe2 | 3.0966 | N/A | SKIPPED_LOW_ERROR | 16.90% |
| 5 | 3b447875 | 3.1651 | N/A | REJECTED | 16.90% |
| 6 | 895c6e8c | 53836.8732 | 0.0002% | ACCEPTED | 16.90% |
| 7 | 2e0f44ef | 14.5467 | N/A | SKIPPED_LOW_ERROR | 16.90% |
| 8 | 3cfa90d7 | 6.8991 | N/A | SKIPPED_LOW_ERROR | 16.90% |
| 9 | a5f39f08 | 7.2489 | N/A | SKIPPED_LOW_ERROR | 16.90% |
| 10 | c53c4396 | 10.1670 | -0.0000% | REJECTED | 16.90% |
| 11 | b3a45093 | 2.1270 | N/A | SKIPPED_LOW_ERROR | 16.90% |
| 12 | 7d4e78be | 1.6532 | N/A | SKIPPED_LOW_ERROR | 16.90% |
| 13 | bb930825 | 118.8648 | 0.0000% | ACCEPTED | 16.90% |
| 14 | e0e3c3e1 | 4.1629 | N/A | SKIPPED_LOW_ERROR | 16.90% |
| 15 | bd9dfa7b | 3.3937 | N/A | SKIPPED_LOW_ERROR | 16.90% |
| 16 | 2873b8c3 | 1.0295 | N/A | SKIPPED_LOW_ERROR | 16.90% |
| 17 | 30d6e09b | 1.6532 | N/A | SKIPPED_LOW_ERROR | 16.90% |
| 18 | 7a51ce50 | 1.6532 | N/A | SKIPPED_LOW_ERROR | 16.90% |
## Query Tree

```
Node 18552 (Sort) [PATTERN: 1d35fb97] - ROOT
  Node 18553 (Aggregate) [consumed]
    Node 18554 (Gather)
      Node 18555 (Aggregate)
        Node 18556 (Nested Loop)
          Node 18557 (Hash Join) [PATTERN: bb930825]
            Node 18558 (Seq Scan) [consumed] - LEAF
            Node 18559 (Hash) [consumed]
              Node 18560 (Hash Join) [consumed]
                Node 18561 (Hash Join)
                  Node 18562 (Nested Loop)
                    Node 18563 (Seq Scan) - LEAF
                    Node 18564 (Index Scan) - LEAF
                  Node 18565 (Hash)
                    Node 18566 (Seq Scan) - LEAF
                Node 18567 (Hash)
                  Node 18568 (Seq Scan) - LEAF
          Node 18569 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Hash Join -> [Seq Scan (Outer) | bb930825 | 18557 | 18552, 18553, 18558, 18559, 18560 |
| Sort -> Aggregate (Outer) | 1d35fb97 | 18552 | 18553, 18557, 18558, 18559, 18560 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 12.78%
- Improvement: -5.97%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 18552 | Sort | 1201.85 | 1048.20 | 12.8% | pattern |
| 18554 | Gather | 1200.96 | 945.99 | 21.2% | operator |
| 18555 | Aggregate | 1178.58 | 1141.78 | 3.1% | operator |
| 18556 | Nested Loop | 1155.12 | 1252.17 | 8.4% | operator |
| 18557 | Hash Join | 986.96 | 134.80 | 86.3% | pattern |
| 18569 | Index Scan | 0.00 | -5.54 | 184812.7% | operator |
| 18561 | Hash Join | 162.95 | 837.36 | 413.9% | operator |
| 18567 | Hash | 13.23 | 14.95 | 13.0% | operator |
| 18562 | Nested Loop | 156.28 | 1251.76 | 701.0% | operator |
| 18565 | Hash | 4.41 | 15.94 | 261.6% | operator |
| 18568 | Seq Scan | 13.22 | 2.94 | 77.8% | operator |
| 18563 | Seq Scan | 19.71 | 44.58 | 126.2% | operator |
| 18564 | Index Scan | 0.08 | -1.39 | 1926.9% | operator |
| 18566 | Seq Scan | 3.86 | 9.45 | 144.5% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 18563 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=3507
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0175
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=1.85, rt=44.58

### Step 2: Node 18564 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=17560
  - nt=4
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=14
  - reltuples=800000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.4200
  - total_cost=2.2600
- **Output:** st=0.01, rt=-1.39

### Step 3: Node 18566 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=223
  - nt=10000
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=10000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=323.0000
- **Output:** st=0.04, rt=9.45

### Step 4: Node 18562 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14028
  - nt1=3507
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=44.5799
  - rt2=-1.3884
  - sel=1.0000
  - st1=1.8531
  - st2=0.0113
  - startup_cost=0.4200
  - total_cost=13249.9400
- **Output:** st=153.57, rt=1251.76

### Step 5: Node 18565 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=10000
  - nt1=10000
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=0.0000
  - rt1=9.4454
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0398
  - st2=0.0000
  - startup_cost=323.0000
  - total_cost=323.0000
- **Output:** st=15.94, rt=15.94

### Step 6: Node 18568 (Seq Scan) - LEAF

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
- **Output:** st=0.05, rt=2.94

### Step 7: Node 18561 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14028
  - nt1=14028
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1251.7614
  - rt2=15.9407
  - sel=0.0001
  - st1=153.5749
  - st2=15.9407
  - startup_cost=448.4300
  - total_cost=13734.7800
- **Output:** st=121.41, rt=837.36

### Step 8: Node 18567 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=25
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=2.9371
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0513
  - st2=0.0000
  - startup_cost=1.2500
  - total_cost=1.2500
- **Output:** st=14.95, rt=14.95

### Step 9: Node 18557 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** bb930825 (Hash Join -> [Seq Scan (Outer), Hash -> Hash Join (Outer) (Inner)])
- **Consumes:** Nodes 18552, 18553, 18558, 18559, 18560
- **Input Features:**
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=14028
  - HashJoin_Outer_nt1=14028
  - HashJoin_Outer_nt2=25
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=126
  - HashJoin_Outer_reltuples=0.0000
  - HashJoin_Outer_sel=0.0400
  - HashJoin_Outer_startup_cost=449.9900
  - HashJoin_Outer_total_cost=13779.4100
  - HashJoin_np=0
  - HashJoin_nt=50512
  - HashJoin_nt1=1200243
  - HashJoin_nt2=14028
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=131
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0000
  - HashJoin_startup_cost=13989.8300
  - HashJoin_total_cost=147594.1600
  - Hash_Inner_np=0
  - Hash_Inner_nt=14028
  - Hash_Inner_nt1=14028
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=126
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=13779.4100
  - Hash_Inner_total_cost=13779.4100
  - SeqScan_Outer_np=112600
  - SeqScan_Outer_nt=1200243
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=29
  - SeqScan_Outer_reltuples=6001215.0000
  - SeqScan_Outer_sel=0.2000
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=124602.4300
- **Output:** st=20.53, rt=134.80

### Step 10: Node 18569 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=1
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.4300
  - total_cost=0.4500
- **Output:** st=0.00, rt=-5.54

### Step 11: Node 18556 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=50512
  - nt1=50512
  - nt2=1
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=134.7957
  - rt2=-5.5414
  - sel=1.0000
  - st1=20.5277
  - st2=0.0041
  - startup_cost=13990.2500
  - total_cost=170478.3700
- **Output:** st=154.10, rt=1252.17

### Step 12: Node 18555 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=50512
  - nt1=50512
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=1252.1681
  - rt2=0.0000
  - sel=1.0000
  - st1=154.1042
  - st2=0.0000
  - startup_cost=171362.3300
  - total_cost=172120.0100
- **Output:** st=1130.22, rt=1141.78

### Step 13: Node 18554 (Gather)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=252560
  - nt1=50512
  - nt2=0
  - parallel_workers=5
  - plan_width=168
  - reltuples=0.0000
  - rt1=1141.7826
  - rt2=0.0000
  - sel=5.0000
  - st1=1130.2242
  - st2=0.0000
  - startup_cost=172362.3300
  - total_cost=198376.0100
- **Output:** st=497.52, rt=945.99

### Step 14: Node 18552 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 1d35fb97 (Sort -> Aggregate (Outer))
- **Consumes:** Nodes 18553, 18557, 18558, 18559, 18560
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=60150
  - Aggregate_Outer_nt1=252560
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=168
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.2382
  - Aggregate_Outer_startup_cost=200901.6100
  - Aggregate_Outer_total_cost=201803.8600
  - Sort_np=0
  - Sort_nt=60150
  - Sort_nt1=60150
  - Sort_nt2=0
  - Sort_parallel_workers=0
  - Sort_plan_width=168
  - Sort_reltuples=0.0000
  - Sort_sel=1.0000
  - Sort_startup_cost=206578.6500
  - Sort_total_cost=206729.0300
- **Output:** st=1047.34, rt=1048.20
