# Online Prediction Report

**Test Query:** Q9_117_seed_951667596
**Timestamp:** 2025-12-22 08:01:56

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 3.02%

## Phase C: Patterns in Query

- Total Patterns: 56

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 33781.0% | 113504.2307 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 172 | 3565.0% | 6131.8766 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 148 | 116.8% | 172.9284 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 9.3% | 13.3894 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 75.1% | 108.1438 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 140 | 4.5% | 6.2375 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 116 | 3.5% | 4.0772 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 96 | 8.0% | 7.7175 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 147.6% | 141.6847 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 96 | 13.0% | 12.4695 |
| bd9dfa7b | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 92 | 3.7% | 3.3601 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 72 | 4.0% | 2.9042 |
| 7d4e78be | Hash Join -> [Hash Join (Outer), Hash (I... | 2 | 48 | 187.5% | 89.9904 |
| 30d6e09b | Hash Join -> [Hash Join -> [Nested Loop ... | 3 | 48 | 187.5% | 89.9904 |
| 2873b8c3 | Hash Join -> [Nested Loop -> [Seq Scan (... | 3 | 48 | 197.5% | 94.8003 |
| 7a51ce50 | Hash Join -> [Hash Join -> [Nested Loop ... | 4 | 48 | 187.5% | 89.9904 |
| 3b447875 | Aggregate -> Nested Loop (Outer) | 2 | 44 | 8.1% | 3.5717 |
| 1a17c7f7 | Hash -> Hash Join -> [Hash Join (Outer),... | 3 | 24 | 76.5% | 18.3606 |
| 6e659102 | Sort -> Aggregate -> Gather -> Aggregate... | 4 | 24 | 6.2% | 1.4968 |
| e941d0ad | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 24 | 19.2% | 4.5998 |
| fee45978 | Hash -> Hash Join -> [Hash Join -> [Nest... | 4 | 24 | 76.5% | 18.3606 |
| 49ae7e42 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 24 | 19.2% | 4.5998 |
| 702e1a46 | Hash -> Hash Join -> [Hash Join -> [Nest... | 5 | 24 | 76.5% | 18.3606 |
| ed7f2e45 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 24 | 19.2% | 4.5998 |
| 3ac23d41 | Gather -> Aggregate -> Nested Loop (Oute... | 3 | 20 | 8.3% | 1.6618 |
| 4251e9b4 | Aggregate -> Nested Loop -> [Hash Join (... | 3 | 20 | 2.7% | 0.5337 |
| 0405d50f | Aggregate -> Gather -> Aggregate -> Nest... | 4 | 20 | 18.3% | 3.6645 |
| 43da7031 | Gather -> Aggregate -> Nested Loop -> [H... | 4 | 20 | 8.3% | 1.6618 |
| 69ec2c4a | Aggregate -> Nested Loop -> [Hash Join -... | 4 | 20 | 2.7% | 0.5337 |
| a70c5941 | Sort -> Aggregate -> Gather -> Aggregate... | 5 | 20 | 5.2% | 1.0450 |
| 6e1ec341 | Aggregate -> Gather -> Aggregate -> Nest... | 5 | 20 | 18.3% | 3.6645 |
| a4e25603 | Gather -> Aggregate -> Nested Loop -> [H... | 5 | 20 | 8.3% | 1.6618 |
| 6b2db56d | Aggregate -> Nested Loop -> [Hash Join -... | 5 | 20 | 2.7% | 0.5337 |
| 7b7172dc | Nested Loop -> [Hash Join -> [Seq Scan (... | 5 | 20 | 2.0% | 0.4014 |
| e9a32a5c | Sort -> Aggregate -> Gather -> Aggregate... | 6 | 20 | 5.2% | 1.0450 |
| 51640d13 | Aggregate -> Gather -> Aggregate -> Nest... | 6 | 20 | 18.3% | 3.6645 |
| 6ac77a36 | Gather -> Aggregate -> Nested Loop -> [H... | 6 | 20 | 8.3% | 1.6618 |
| 7378d2b2 | Aggregate -> Nested Loop -> [Hash Join -... | 6 | 20 | 2.7% | 0.5337 |
| 3dbdd75b | Nested Loop -> [Hash Join -> [Seq Scan (... | 6 | 20 | 2.0% | 0.4014 |
| 9e770981 | Sort -> Aggregate -> Gather -> Aggregate... | 7 | 20 | 5.2% | 1.0450 |
| 366e9db5 | Aggregate -> Gather -> Aggregate -> Nest... | 7 | 20 | 18.3% | 3.6645 |
| d60fddc6 | Gather -> Aggregate -> Nested Loop -> [H... | 7 | 20 | 8.3% | 1.6618 |
| 2af8b806 | Aggregate -> Nested Loop -> [Hash Join -... | 7 | 20 | 2.7% | 0.5337 |
| dc9f4b49 | Nested Loop -> [Hash Join -> [Seq Scan (... | 7 | 20 | 2.0% | 0.4014 |
| d8d0a254 | Sort -> Aggregate -> Gather -> Aggregate... | 8 | 20 | 5.2% | 1.0450 |
| 88dc07c3 | Aggregate -> Gather -> Aggregate -> Nest... | 8 | 20 | 18.3% | 3.6645 |
| 75cf2f59 | Gather -> Aggregate -> Nested Loop -> [H... | 8 | 20 | 8.3% | 1.6618 |
| 5305e2e5 | Aggregate -> Nested Loop -> [Hash Join -... | 8 | 20 | 2.7% | 0.5337 |
| 4d81a89d | Sort -> Aggregate -> Gather -> Aggregate... | 9 | 20 | 5.2% | 1.0450 |
| c94fcfda | Aggregate -> Gather -> Aggregate -> Nest... | 9 | 20 | 18.3% | 3.6645 |
| f17356e6 | Gather -> Aggregate -> Nested Loop -> [H... | 9 | 20 | 8.3% | 1.6618 |
| 76ab422a | Sort -> Aggregate -> Gather -> Aggregate... | 10 | 20 | 5.2% | 1.0450 |
| 1c7aa67e | Aggregate -> Gather -> Aggregate -> Nest... | 10 | 20 | 18.3% | 3.6645 |
| f1e59da5 | Sort -> Aggregate -> Gather -> Aggregate... | 11 | 20 | 5.2% | 1.0450 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 1 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 2 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 3 | 7df893ad | 6131.8766 | -0.0000% | REJECTED | 17.92% |
| 4 | bb930825 | 172.9284 | -0.0000% | REJECTED | 17.92% |
| 5 | 4fc84c77 | 13.3894 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 6 | 2e0f44ef | 108.1438 | 0.0001% | REJECTED | 17.92% |
| 7 | 3cfa90d7 | 6.2375 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 8 | e0e3c3e1 | 4.0772 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 9 | 634cdbe2 | 7.7175 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 10 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.92% |
| 11 | a5f39f08 | 12.4695 | 1.7095% | ACCEPTED | 16.21% |
| 12 | bd9dfa7b | 3.3601 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 13 | b3a45093 | 2.7998 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 14 | 7d4e78be | 89.9904 | 0.0000% | REJECTED | 16.21% |
| 15 | 30d6e09b | 89.9904 | 0.0000% | REJECTED | 16.21% |
| 16 | 2873b8c3 | 94.8003 | 0.0000% | REJECTED | 16.21% |
| 17 | 7a51ce50 | 89.9904 | 0.0000% | REJECTED | 16.21% |
| 18 | 3b447875 | 5.5697 | 0.0002% | REJECTED | 16.21% |
| 19 | 1a17c7f7 | 18.3606 | N/A | REJECTED | 16.21% |
| 20 | 6e659102 | 1.3924 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 21 | e941d0ad | 4.5998 | N/A | REJECTED | 16.21% |
| 22 | fee45978 | 18.3606 | N/A | REJECTED | 16.21% |
| 23 | 49ae7e42 | 4.5998 | N/A | REJECTED | 16.21% |
| 24 | 702e1a46 | 18.3606 | N/A | REJECTED | 16.21% |
| 25 | ed7f2e45 | 4.5998 | N/A | REJECTED | 16.21% |
| 26 | 0405d50f | 2.3736 | 0.0562% | REJECTED | 16.21% |
| 27 | a70c5941 | 0.9472 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 28 | 6e1ec341 | 2.3736 | 0.0562% | REJECTED | 16.21% |
| 29 | 7b7172dc | 0.4014 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 30 | e9a32a5c | 0.9472 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 31 | 51640d13 | 2.3736 | 0.0562% | REJECTED | 16.21% |
| 32 | 3dbdd75b | 0.4014 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 33 | 9e770981 | 0.9472 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 34 | 366e9db5 | 2.3736 | 0.0562% | REJECTED | 16.21% |
| 35 | dc9f4b49 | 0.4014 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 36 | d8d0a254 | 0.9472 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 37 | 88dc07c3 | 2.3736 | 0.0562% | REJECTED | 16.21% |
| 38 | 4d81a89d | 0.9472 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 39 | c94fcfda | 2.3736 | 0.0562% | REJECTED | 16.21% |
| 40 | 76ab422a | 0.9472 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 41 | 1c7aa67e | 2.3736 | 0.0562% | REJECTED | 16.21% |
| 42 | f1e59da5 | 0.9472 | N/A | SKIPPED_LOW_ERROR | 16.21% |
## Query Tree

```
Node 16978 (Sort) - ROOT
  Node 16979 (Aggregate) [PATTERN: a5f39f08]
    Node 16980 (Gather) [consumed]
      Node 16981 (Aggregate) [consumed]
        Node 16982 (Nested Loop)
          Node 16983 (Hash Join)
            Node 16984 (Seq Scan) - LEAF
            Node 16985 (Hash)
              Node 16986 (Hash Join)
                Node 16987 (Hash Join)
                  Node 16988 (Nested Loop)
                    Node 16989 (Seq Scan) - LEAF
                    Node 16990 (Index Scan) - LEAF
                  Node 16991 (Hash)
                    Node 16992 (Seq Scan) - LEAF
                Node 16993 (Hash)
                  Node 16994 (Seq Scan) - LEAF
          Node 16995 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | a5f39f08 | 16979 | 16980, 16981 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 1.82%
- Improvement: 1.20%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 16978 | Sort | 1172.38 | 1151.06 | 1.8% | operator |
| 16979 | Aggregate | 1172.23 | 1114.29 | 4.9% | pattern |
| 16982 | Nested Loop | 1126.56 | 1180.24 | 4.8% | operator |
| 16983 | Hash Join | 951.17 | 831.48 | 12.6% | operator |
| 16995 | Index Scan | 0.00 | -0.04 | 1512.7% | operator |
| 16984 | Seq Scan | 669.56 | 565.06 | 15.6% | operator |
| 16985 | Hash | 186.38 | 52.07 | 72.1% | operator |
| 16986 | Hash Join | 184.32 | 911.29 | 394.4% | operator |
| 16987 | Hash Join | 170.82 | 850.93 | 398.1% | operator |
| 16993 | Hash | 12.72 | 14.54 | 14.3% | operator |
| 16988 | Nested Loop | 165.04 | 1066.32 | 546.1% | operator |
| 16991 | Hash | 3.56 | 14.79 | 314.8% | operator |
| 16994 | Seq Scan | 12.71 | 7.19 | 43.4% | operator |
| 16989 | Seq Scan | 21.07 | 42.93 | 103.8% | operator |
| 16990 | Index Scan | 0.08 | 0.12 | 50.9% | operator |
| 16992 | Seq Scan | 2.98 | 10.62 | 255.7% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 16989 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=4509
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0225
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=0.41, rt=42.93

### Step 2: Node 16990 (Index Scan) - LEAF

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
  - total_cost=1.9700
- **Output:** st=0.07, rt=0.12

### Step 3: Node 16992 (Seq Scan) - LEAF

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
- **Output:** st=0.04, rt=10.62

### Step 4: Node 16988 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18037
  - nt1=4509
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=42.9274
  - rt2=0.1192
  - sel=1.0001
  - st1=0.4112
  - st2=0.0716
  - startup_cost=0.4200
  - total_cost=14242.4200
- **Output:** st=3.72, rt=1066.32

### Step 5: Node 16991 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=10000
  - nt1=10000
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=0.0000
  - rt1=10.6168
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0355
  - st2=0.0000
  - startup_cost=323.0000
  - total_cost=323.0000
- **Output:** st=14.79, rt=14.79

### Step 6: Node 16994 (Seq Scan) - LEAF

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
- **Output:** st=0.06, rt=7.19

### Step 7: Node 16987 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18037
  - nt1=18037
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1066.3163
  - rt2=14.7884
  - sel=0.0001
  - st1=3.7194
  - st2=14.7887
  - startup_cost=448.4300
  - total_cost=14737.7900
- **Output:** st=52.36, rt=850.93

### Step 8: Node 16993 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=25
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=7.1945
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0613
  - st2=0.0000
  - startup_cost=1.2500
  - total_cost=1.2500
- **Output:** st=14.54, rt=14.54

### Step 9: Node 16986 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18037
  - nt1=18037
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=850.9332
  - rt2=14.5397
  - sel=0.0400
  - st1=52.3619
  - st2=14.5393
  - startup_cost=449.9900
  - total_cost=14794.7200
- **Output:** st=40.34, rt=911.29

### Step 10: Node 16984 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=1200243
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=29
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.2000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=124602.4300
- **Output:** st=1.00, rt=565.06

### Step 11: Node 16985 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18037
  - nt1=18037
  - nt2=0
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=911.2867
  - rt2=0.0000
  - sel=1.0000
  - st1=40.3411
  - st2=0.0000
  - startup_cost=14794.7200
  - total_cost=14794.7200
- **Output:** st=52.07, rt=52.07

### Step 12: Node 16983 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=64945
  - nt1=1200243
  - nt2=18037
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=565.0624
  - rt2=52.0739
  - sel=0.0000
  - st1=0.9985
  - st2=52.0732
  - startup_cost=15065.2800
  - total_cost=148669.6400
- **Output:** st=168.65, rt=831.48

### Step 13: Node 16995 (Index Scan) - LEAF

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
- **Output:** st=0.00, rt=-0.04

### Step 14: Node 16982 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=64945
  - nt1=64945
  - nt2=1
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=831.4806
  - rt2=-0.0424
  - sel=1.0000
  - st1=168.6463
  - st2=0.0037
  - startup_cost=15065.7100
  - total_cost=178092.6500
- **Output:** st=127.78, rt=1180.24

### Step 15: Node 16979 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** a5f39f08 (Aggregate -> Gather -> Aggregate (Outer) (Outer))
- **Consumes:** Nodes 16980, 16981
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=60150
  - Aggregate_Outer_nt1=64945
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=168
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.9262
  - Aggregate_Outer_startup_cost=179229.1900
  - Aggregate_Outer_total_cost=180131.4400
  - Aggregate_np=0
  - Aggregate_nt=60150
  - Aggregate_nt1=300750
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=168
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=214213.9400
  - Aggregate_total_cost=215116.1900
  - Gather_Outer_np=0
  - Gather_Outer_nt=300750
  - Gather_Outer_nt1=60150
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=5
  - Gather_Outer_plan_width=168
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=5.0000
  - Gather_Outer_startup_cost=180229.1900
  - Gather_Outer_total_cost=211206.4400
- **Output:** st=1108.81, rt=1114.29

### Step 16: Node 16978 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=60150
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=1114.2885
  - rt2=0.0000
  - sel=1.0000
  - st1=1108.8147
  - st2=0.0000
  - startup_cost=219890.9800
  - total_cost=220041.3600
- **Output:** st=1148.58, rt=1151.06
