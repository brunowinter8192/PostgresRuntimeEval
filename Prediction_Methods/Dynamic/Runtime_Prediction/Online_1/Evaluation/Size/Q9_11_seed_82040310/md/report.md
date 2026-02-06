# Online Prediction Report

**Test Query:** Q9_11_seed_82040310
**Timestamp:** 2026-01-18 18:57:30

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17280 | Operator + Pattern Training |
| Training_Test | 4320 | Pattern Selection Eval |
| Training | 21600 | Final Model Training |
| Test | 2719 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 6.70%

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
Node 17032 (Sort) [PATTERN: 1d35fb97] - ROOT
  Node 17033 (Aggregate) [consumed]
    Node 17034 (Gather)
      Node 17035 (Aggregate)
        Node 17036 (Nested Loop)
          Node 17037 (Hash Join) [PATTERN: bb930825]
            Node 17038 (Seq Scan) [consumed] - LEAF
            Node 17039 (Hash) [consumed]
              Node 17040 (Hash Join) [consumed]
                Node 17041 (Hash Join)
                  Node 17042 (Nested Loop)
                    Node 17043 (Seq Scan) - LEAF
                    Node 17044 (Index Scan) - LEAF
                  Node 17045 (Hash)
                    Node 17046 (Seq Scan) - LEAF
                Node 17047 (Hash)
                  Node 17048 (Seq Scan) - LEAF
          Node 17049 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Hash Join -> [Seq Scan (Outer) | bb930825 | 17037 | 17032, 17033, 17038, 17039, 17040 |
| Sort -> Aggregate (Outer) | 1d35fb97 | 17032 | 17033, 17037, 17038, 17039, 17040 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 12.81%
- Improvement: -6.10%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 17032 | Sort | 1200.82 | 1047.04 | 12.8% | pattern |
| 17034 | Gather | 1199.61 | 950.92 | 20.7% | operator |
| 17035 | Aggregate | 1180.11 | 1141.61 | 3.3% | operator |
| 17036 | Nested Loop | 1155.48 | 1252.17 | 8.4% | operator |
| 17037 | Hash Join | 976.83 | 134.80 | 86.2% | pattern |
| 17049 | Index Scan | 0.00 | -5.54 | 184812.7% | operator |
| 17041 | Hash Join | 161.45 | 837.40 | 418.7% | operator |
| 17047 | Hash | 12.78 | 14.95 | 17.0% | operator |
| 17042 | Nested Loop | 154.36 | 1251.76 | 710.9% | operator |
| 17045 | Hash | 4.75 | 15.94 | 235.7% | operator |
| 17048 | Seq Scan | 12.76 | 2.94 | 77.0% | operator |
| 17043 | Seq Scan | 19.00 | 44.51 | 134.2% | operator |
| 17044 | Index Scan | 0.07 | -1.39 | 2002.0% | operator |
| 17046 | Seq Scan | 4.21 | 9.45 | 124.6% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 17043 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=3674
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0184
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=1.85, rt=44.51

### Step 2: Node 17044 (Index Scan) - LEAF

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
  - total_cost=2.2200
- **Output:** st=0.01, rt=-1.39

### Step 3: Node 17046 (Seq Scan) - LEAF

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

### Step 4: Node 17042 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14697
  - nt1=3674
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=44.5102
  - rt2=-1.3884
  - sel=1.0001
  - st1=1.8465
  - st2=0.0113
  - startup_cost=0.4200
  - total_cost=13480.1200
- **Output:** st=153.58, rt=1251.76

### Step 5: Node 17045 (Hash)

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

### Step 6: Node 17048 (Seq Scan) - LEAF

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

### Step 7: Node 17041 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14697
  - nt1=14697
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1251.7619
  - rt2=15.9407
  - sel=0.0001
  - st1=153.5750
  - st2=15.9407
  - startup_cost=448.4300
  - total_cost=13966.7100
- **Output:** st=121.42, rt=837.40

### Step 8: Node 17047 (Hash)

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

### Step 9: Node 17037 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** bb930825 (Hash Join -> [Seq Scan (Outer), Hash -> Hash Join (Outer) (Inner)])
- **Consumes:** Nodes 17032, 17033, 17038, 17039, 17040
- **Input Features:**
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=14697
  - HashJoin_Outer_nt1=14697
  - HashJoin_Outer_nt2=25
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=126
  - HashJoin_Outer_reltuples=0.0000
  - HashJoin_Outer_sel=0.0400
  - HashJoin_Outer_startup_cost=449.9900
  - HashJoin_Outer_total_cost=14013.3900
  - HashJoin_np=0
  - HashJoin_nt=52919
  - HashJoin_nt1=1200243
  - HashJoin_nt2=14697
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=131
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0000
  - HashJoin_startup_cost=14233.8500
  - HashJoin_total_cost=147838.1900
  - Hash_Inner_np=0
  - Hash_Inner_nt=14697
  - Hash_Inner_nt1=14697
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=126
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=14013.3900
  - Hash_Inner_total_cost=14013.3900
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

### Step 10: Node 17049 (Index Scan) - LEAF

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

### Step 11: Node 17036 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=52919
  - nt1=52919
  - nt2=1
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=134.7957
  - rt2=-5.5414
  - sel=1.0000
  - st1=20.5277
  - st2=0.0041
  - startup_cost=14234.2700
  - total_cost=171812.8800
- **Output:** st=154.10, rt=1252.17

### Step 12: Node 17035 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=52919
  - nt1=52919
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=1252.1681
  - rt2=0.0000
  - sel=1.0000
  - st1=154.1042
  - st2=0.0000
  - startup_cost=172738.9600
  - total_cost=173532.7500
- **Output:** st=1129.59, rt=1141.61

### Step 13: Node 17034 (Gather)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=264595
  - nt1=52919
  - nt2=0
  - parallel_workers=5
  - plan_width=168
  - reltuples=0.0000
  - rt1=1141.6129
  - rt2=0.0000
  - sel=5.0000
  - st1=1129.5927
  - st2=0.0000
  - startup_cost=173738.9600
  - total_cost=200992.2500
- **Output:** st=490.67, rt=950.92

### Step 14: Node 17032 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 1d35fb97 (Sort -> Aggregate (Outer))
- **Consumes:** Nodes 17033, 17037, 17038, 17039, 17040
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=60150
  - Aggregate_Outer_nt1=264595
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=168
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.2273
  - Aggregate_Outer_startup_cost=203638.2000
  - Aggregate_Outer_total_cost=204540.4500
  - Sort_np=0
  - Sort_nt=60150
  - Sort_nt1=60150
  - Sort_nt2=0
  - Sort_parallel_workers=0
  - Sort_plan_width=168
  - Sort_reltuples=0.0000
  - Sort_sel=1.0000
  - Sort_startup_cost=209315.2400
  - Sort_total_cost=209465.6100
- **Output:** st=1046.20, rt=1047.04
