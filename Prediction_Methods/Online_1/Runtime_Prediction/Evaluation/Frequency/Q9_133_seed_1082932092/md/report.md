# Online Prediction Report

**Test Query:** Q9_133_seed_1082932092
**Timestamp:** 2026-01-01 19:46:51

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 4.21%

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
| 0 | 895c6e8c | 75736.1626 | 0.0004% | ACCEPTED | 17.92% |
| 1 | 3aab37be | 94712.4752 | -0.0000% | REJECTED | 17.92% |
| 2 | 1d35fb97 | 26.4006 | 0.1163% | ACCEPTED | 17.81% |
| 3 | 7df893ad | 678.6757 | N/A | REJECTED | 17.81% |
| 4 | bb930825 | 188.3060 | -0.0000% | REJECTED | 17.81% |
| 5 | 4fc84c77 | 15.8328 | 0.6911% | ACCEPTED | 17.12% |
| 6 | 2e0f44ef | 108.1433 | 0.0001% | ACCEPTED | 17.12% |
| 7 | 3cfa90d7 | 3.5091 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 8 | e0e3c3e1 | 2.9076 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 9 | 634cdbe2 | 9.1880 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 10 | c53c4396 | 8.0758 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 11 | a5f39f08 | 7.4593 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 12 | bd9dfa7b | 1.7976 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 13 | b3a45093 | 2.3813 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 14 | 7d4e78be | 83.6779 | N/A | REJECTED | 17.12% |
| 15 | 30d6e09b | 83.6779 | N/A | REJECTED | 17.12% |
| 16 | 2873b8c3 | 121.6368 | N/A | REJECTED | 17.12% |
| 17 | 7a51ce50 | 83.6779 | N/A | REJECTED | 17.12% |
| 18 | 3b447875 | 1.1760 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 19 | 6e659102 | 1.9242 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 20 | e941d0ad | 7.6069 | N/A | REJECTED | 17.12% |
| 21 | 49ae7e42 | 7.6069 | N/A | REJECTED | 17.12% |
| 22 | ed7f2e45 | 7.6069 | N/A | REJECTED | 17.12% |
| 23 | 3ac23d41 | 1.6618 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 24 | 4251e9b4 | 0.5345 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 25 | 43da7031 | 1.6618 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 26 | 69ec2c4a | 0.5345 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 27 | a70c5941 | 1.4275 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 28 | a4e25603 | 1.6618 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 29 | 6b2db56d | 0.5345 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 30 | 7b7172dc | 0.3908 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 31 | e9a32a5c | 1.4275 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 32 | 6ac77a36 | 1.6618 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 33 | 7378d2b2 | 0.5345 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 34 | 3dbdd75b | 0.3908 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 35 | 9e770981 | 1.4275 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 36 | d60fddc6 | 1.6618 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 37 | 2af8b806 | 0.5345 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 38 | dc9f4b49 | 0.3908 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 39 | d8d0a254 | 1.4275 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 40 | 75cf2f59 | 1.6618 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 41 | 5305e2e5 | 0.5345 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 42 | 4d81a89d | 1.4275 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 43 | f17356e6 | 1.6618 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 44 | 76ab422a | 1.4275 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 45 | f1e59da5 | 1.4275 | N/A | SKIPPED_LOW_ERROR | 17.12% |
## Query Tree

```
Node 17303 (Sort) [PATTERN: 1d35fb97] - ROOT
  Node 17304 (Aggregate) [consumed]
    Node 17305 (Gather)
      Node 17306 (Aggregate)
        Node 17307 (Nested Loop)
          Node 17308 (Hash Join) [PATTERN: 895c6e8c]
            Node 17309 (Seq Scan) [consumed] - LEAF
            Node 17310 (Hash) [consumed]
              Node 17311 (Hash Join)
                Node 17312 (Hash Join) [PATTERN: 2e0f44ef]
                  Node 17313 (Nested Loop) [consumed]
                    Node 17314 (Seq Scan) - LEAF
                    Node 17315 (Index Scan) - LEAF
                  Node 17316 (Hash) [consumed]
                    Node 17317 (Seq Scan) - LEAF
                Node 17318 (Hash)
                  Node 17319 (Seq Scan) - LEAF
          Node 17320 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Hash Join -> [Seq Scan (Outer) | 895c6e8c | 17308 | 17303, 17304, 17309, 17310, 17312, 17313, 17316 |
| Sort -> Aggregate (Outer) | 1d35fb97 | 17303 | 17304, 17308, 17309, 17310, 17312, 17313, 17316 |
| Hash Join -> [Nested Loop (Out | 2e0f44ef | 17312 | 17303, 17304, 17308, 17309, 17310, 17313, 17316 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 5.91%
- Improvement: -1.70%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 17303 | Sort | 1188.08 | 1117.86 | 5.9% | pattern |
| 17305 | Gather | 1187.28 | 1134.99 | 4.4% | operator |
| 17306 | Aggregate | 1166.96 | 1119.74 | 4.0% | operator |
| 17307 | Nested Loop | 1142.22 | 1186.22 | 3.9% | operator |
| 17308 | Hash Join | 968.30 | 734.53 | 24.1% | pattern |
| 17320 | Index Scan | 0.00 | -0.04 | 1512.7% | operator |
| 17311 | Hash Join | 169.66 | 820.89 | 383.8% | operator |
| 17312 | Hash Join | 156.10 | 981.07 | 528.5% | pattern |
| 17318 | Hash | 12.92 | 14.54 | 12.5% | operator |
| 17319 | Seq Scan | 12.91 | 7.19 | 44.3% | operator |
| 17314 | Seq Scan | 20.11 | 42.68 | 112.2% | operator |
| 17315 | Index Scan | 0.07 | 0.12 | 67.8% | operator |
| 17317 | Seq Scan | 3.58 | 10.62 | 196.1% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 17314 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=5177
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0259
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=0.41, rt=42.68

### Step 2: Node 17315 (Index Scan) - LEAF

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
  - total_cost=1.8300
- **Output:** st=0.07, rt=0.12

### Step 3: Node 17317 (Seq Scan) - LEAF

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

### Step 4: Node 17319 (Seq Scan) - LEAF

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

### Step 5: Node 17312 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 2e0f44ef (Hash Join -> [Nested Loop (Outer), Hash (Inner)])
- **Consumes:** Nodes 17303, 17304, 17308, 17309, 17310, 17313, 17316
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=20708
  - HashJoin_nt1=20708
  - HashJoin_nt2=10000
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=26
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0001
  - HashJoin_startup_cost=448.4300
  - HashJoin_total_cost=15335.6200
  - Hash_Inner_np=0
  - Hash_Inner_nt=10000
  - Hash_Inner_nt1=10000
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=8
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=323.0000
  - Hash_Inner_total_cost=323.0000
  - NestedLoop_Outer_np=0
  - NestedLoop_Outer_nt=20708
  - NestedLoop_Outer_nt1=5177
  - NestedLoop_Outer_nt2=4
  - NestedLoop_Outer_parallel_workers=0
  - NestedLoop_Outer_plan_width=18
  - NestedLoop_Outer_reltuples=0.0000
  - NestedLoop_Outer_sel=1.0000
  - NestedLoop_Outer_startup_cost=0.4200
  - NestedLoop_Outer_total_cost=14833.2400
- **Output:** st=5.37, rt=981.07

### Step 6: Node 17318 (Hash)

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

### Step 7: Node 17311 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=20708
  - nt1=20708
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=981.0723
  - rt2=14.5397
  - sel=0.0400
  - st1=5.3671
  - st2=14.5393
  - startup_cost=449.9900
  - total_cost=15400.7600
- **Output:** st=26.55, rt=820.89

### Step 8: Node 17308 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 895c6e8c (Hash Join -> [Seq Scan (Outer), Hash (Inner)])
- **Consumes:** Nodes 17303, 17304, 17309, 17310, 17312, 17313, 17316
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=74565
  - HashJoin_nt1=1200243
  - HashJoin_nt2=20708
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=131
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0000
  - HashJoin_startup_cost=15711.3800
  - HashJoin_total_cost=149315.7500
  - Hash_Inner_np=0
  - Hash_Inner_nt=20708
  - Hash_Inner_nt1=20708
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=126
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=15400.7600
  - Hash_Inner_total_cost=15400.7600
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
- **Output:** st=176.10, rt=734.53

### Step 9: Node 17320 (Index Scan) - LEAF

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

### Step 10: Node 17307 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=74565
  - nt1=74565
  - nt2=1
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=734.5299
  - rt2=-0.0424
  - sel=1.0000
  - st1=176.1002
  - st2=0.0037
  - startup_cost=15711.8000
  - total_cost=183097.0600
- **Output:** st=136.78, rt=1186.22

### Step 11: Node 17306 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=74565
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=1186.2211
  - rt2=0.0000
  - sel=0.8067
  - st1=136.7819
  - st2=0.0000
  - startup_cost=184401.9400
  - total_cost=185304.1900
- **Output:** st=1121.00, rt=1119.74

### Step 12: Node 17305 (Gather)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=300750
  - nt1=60150
  - nt2=0
  - parallel_workers=5
  - plan_width=168
  - reltuples=0.0000
  - rt1=1119.7399
  - rt2=0.0000
  - sel=5.0000
  - st1=1120.9979
  - st2=0.0000
  - startup_cost=185401.9400
  - total_cost=216379.1900
- **Output:** st=579.92, rt=1134.99

### Step 13: Node 17303 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 1d35fb97 (Sort -> Aggregate (Outer))
- **Consumes:** Nodes 17304, 17308, 17309, 17310, 17312, 17313, 17316
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=60150
  - Aggregate_Outer_nt1=300750
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=168
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.2000
  - Aggregate_Outer_startup_cost=219386.6900
  - Aggregate_Outer_total_cost=220288.9400
  - Sort_np=0
  - Sort_nt=60150
  - Sort_nt1=60150
  - Sort_nt2=0
  - Sort_parallel_workers=0
  - Sort_plan_width=168
  - Sort_reltuples=0.0000
  - Sort_sel=1.0000
  - Sort_startup_cost=225063.7300
  - Sort_total_cost=225214.1100
- **Output:** st=1116.38, rt=1117.86
