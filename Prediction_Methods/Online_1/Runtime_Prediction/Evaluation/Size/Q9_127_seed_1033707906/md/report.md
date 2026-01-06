# Online Prediction Report

**Test Query:** Q9_127_seed_1033707906
**Timestamp:** 2026-01-01 18:45:14

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 4.68%

## Phase C: Patterns in Query

- Total Patterns: 56

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 33781.0% | 113504.2307 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 172 | 3565.0% | 6131.8766 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 9.3% | 13.3894 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 75.1% | 108.1438 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 140 | 4.5% | 6.2375 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 96 | 8.0% | 7.7175 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 147.6% | 141.6847 |
| 7d4e78be | Hash Join -> [Hash Join (Outer), Hash (I... | 2 | 48 | 187.5% | 89.9904 |
| 3b447875 | Aggregate -> Nested Loop (Outer) | 2 | 44 | 8.1% | 3.5717 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 148 | 116.8% | 172.9284 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 116 | 3.5% | 4.0772 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 96 | 13.0% | 12.4695 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 72 | 4.0% | 2.9042 |
| 30d6e09b | Hash Join -> [Hash Join -> [Nested Loop ... | 3 | 48 | 187.5% | 89.9904 |
| 2873b8c3 | Hash Join -> [Nested Loop -> [Seq Scan (... | 3 | 48 | 197.5% | 94.8003 |
| 1a17c7f7 | Hash -> Hash Join -> [Hash Join (Outer),... | 3 | 24 | 76.5% | 18.3606 |
| 3ac23d41 | Gather -> Aggregate -> Nested Loop (Oute... | 3 | 20 | 8.3% | 1.6618 |
| 4251e9b4 | Aggregate -> Nested Loop -> [Hash Join (... | 3 | 20 | 2.7% | 0.5337 |
| bd9dfa7b | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 92 | 3.7% | 3.3601 |
| 7a51ce50 | Hash Join -> [Hash Join -> [Nested Loop ... | 4 | 48 | 187.5% | 89.9904 |
| 6e659102 | Sort -> Aggregate -> Gather -> Aggregate... | 4 | 24 | 6.2% | 1.4968 |
| e941d0ad | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 24 | 19.2% | 4.5998 |
| fee45978 | Hash -> Hash Join -> [Hash Join -> [Nest... | 4 | 24 | 76.5% | 18.3606 |
| 0405d50f | Aggregate -> Gather -> Aggregate -> Nest... | 4 | 20 | 18.3% | 3.6645 |
| 43da7031 | Gather -> Aggregate -> Nested Loop -> [H... | 4 | 20 | 8.3% | 1.6618 |
| 69ec2c4a | Aggregate -> Nested Loop -> [Hash Join -... | 4 | 20 | 2.7% | 0.5337 |
| 49ae7e42 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 24 | 19.2% | 4.5998 |
| 702e1a46 | Hash -> Hash Join -> [Hash Join -> [Nest... | 5 | 24 | 76.5% | 18.3606 |
| a70c5941 | Sort -> Aggregate -> Gather -> Aggregate... | 5 | 20 | 5.2% | 1.0450 |
| 6e1ec341 | Aggregate -> Gather -> Aggregate -> Nest... | 5 | 20 | 18.3% | 3.6645 |
| a4e25603 | Gather -> Aggregate -> Nested Loop -> [H... | 5 | 20 | 8.3% | 1.6618 |
| 6b2db56d | Aggregate -> Nested Loop -> [Hash Join -... | 5 | 20 | 2.7% | 0.5337 |
| 7b7172dc | Nested Loop -> [Hash Join -> [Seq Scan (... | 5 | 20 | 2.0% | 0.4014 |
| ed7f2e45 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 24 | 19.2% | 4.5998 |
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
| 4 | 4fc84c77 | 15.8328 | 0.6911% | ACCEPTED | 17.12% |
| 5 | 2e0f44ef | 108.1433 | 0.0001% | ACCEPTED | 17.12% |
| 6 | 3cfa90d7 | 3.5091 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 7 | 634cdbe2 | 9.1880 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 8 | c53c4396 | 8.0758 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 9 | 7d4e78be | 83.6779 | N/A | REJECTED | 17.12% |
| 10 | 3b447875 | 1.1760 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 11 | bb930825 | 188.3060 | N/A | REJECTED | 17.12% |
| 12 | e0e3c3e1 | 2.9076 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 13 | a5f39f08 | 7.4593 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 14 | b3a45093 | 2.3813 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 15 | 30d6e09b | 83.6779 | N/A | REJECTED | 17.12% |
| 16 | 2873b8c3 | 121.6368 | N/A | REJECTED | 17.12% |
| 17 | 3ac23d41 | 1.6618 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 18 | 4251e9b4 | 0.5345 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 19 | bd9dfa7b | 1.7976 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 20 | 7a51ce50 | 83.6779 | N/A | REJECTED | 17.12% |
| 21 | 6e659102 | 1.9242 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 22 | e941d0ad | 7.6069 | N/A | REJECTED | 17.12% |
| 23 | 43da7031 | 1.6618 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 24 | 69ec2c4a | 0.5345 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 25 | 49ae7e42 | 7.6069 | N/A | REJECTED | 17.12% |
| 26 | a70c5941 | 1.4275 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 27 | a4e25603 | 1.6618 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 28 | 6b2db56d | 0.5345 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 29 | 7b7172dc | 0.3908 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 30 | ed7f2e45 | 7.6069 | N/A | REJECTED | 17.12% |
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
Node 17176 (Sort) [PATTERN: 1d35fb97] - ROOT
  Node 17177 (Aggregate) [consumed]
    Node 17178 (Gather)
      Node 17179 (Aggregate)
        Node 17180 (Nested Loop)
          Node 17181 (Hash Join) [PATTERN: 895c6e8c]
            Node 17182 (Seq Scan) [consumed] - LEAF
            Node 17183 (Hash) [consumed]
              Node 17184 (Hash Join)
                Node 17185 (Hash Join) [PATTERN: 2e0f44ef]
                  Node 17186 (Nested Loop) [consumed]
                    Node 17187 (Seq Scan) - LEAF
                    Node 17188 (Index Scan) - LEAF
                  Node 17189 (Hash) [consumed]
                    Node 17190 (Seq Scan) - LEAF
                Node 17191 (Hash)
                  Node 17192 (Seq Scan) - LEAF
          Node 17193 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Hash Join -> [Seq Scan (Outer) | 895c6e8c | 17181 | 17176, 17177, 17182, 17183, 17185, 17186, 17189 |
| Sort -> Aggregate (Outer) | 1d35fb97 | 17176 | 17177, 17181, 17182, 17183, 17185, 17186, 17189 |
| Hash Join -> [Nested Loop (Out | 2e0f44ef | 17185 | 17176, 17177, 17181, 17182, 17183, 17186, 17189 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 6.46%
- Improvement: -1.78%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 17176 | Sort | 1192.85 | 1115.82 | 6.5% | pattern |
| 17178 | Gather | 1191.96 | 1135.98 | 4.7% | operator |
| 17179 | Aggregate | 1172.01 | 1152.73 | 1.6% | operator |
| 17180 | Nested Loop | 1147.12 | 1179.58 | 2.8% | operator |
| 17181 | Hash Join | 969.26 | 733.84 | 24.3% | pattern |
| 17193 | Index Scan | 0.00 | -0.04 | 1512.7% | operator |
| 17184 | Hash Join | 180.36 | 820.92 | 355.2% | operator |
| 17185 | Hash Join | 166.90 | 981.22 | 487.9% | pattern |
| 17191 | Hash | 12.83 | 14.54 | 13.3% | operator |
| 17192 | Seq Scan | 12.82 | 7.19 | 43.9% | operator |
| 17187 | Seq Scan | 22.30 | 42.93 | 92.5% | operator |
| 17188 | Index Scan | 0.08 | 0.12 | 56.8% | operator |
| 17190 | Seq Scan | 3.71 | 10.62 | 186.1% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 17187 (Seq Scan) - LEAF

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

### Step 2: Node 17188 (Index Scan) - LEAF

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

### Step 3: Node 17190 (Seq Scan) - LEAF

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

### Step 4: Node 17192 (Seq Scan) - LEAF

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

### Step 5: Node 17185 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 2e0f44ef (Hash Join -> [Nested Loop (Outer), Hash (Inner)])
- **Consumes:** Nodes 17176, 17177, 17181, 17182, 17183, 17186, 17189
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=18037
  - HashJoin_nt1=18037
  - HashJoin_nt2=10000
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=26
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0001
  - HashJoin_startup_cost=448.4300
  - HashJoin_total_cost=14737.7900
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
  - NestedLoop_Outer_nt=18037
  - NestedLoop_Outer_nt1=4509
  - NestedLoop_Outer_nt2=4
  - NestedLoop_Outer_parallel_workers=0
  - NestedLoop_Outer_plan_width=18
  - NestedLoop_Outer_reltuples=0.0000
  - NestedLoop_Outer_sel=1.0001
  - NestedLoop_Outer_startup_cost=0.4200
  - NestedLoop_Outer_total_cost=14242.4200
- **Output:** st=5.52, rt=981.22

### Step 6: Node 17191 (Hash)

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

### Step 7: Node 17184 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18037
  - nt1=18037
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=981.2208
  - rt2=14.5397
  - sel=0.0400
  - st1=5.5229
  - st2=14.5393
  - startup_cost=449.9900
  - total_cost=14794.7200
- **Output:** st=26.43, rt=820.92

### Step 8: Node 17181 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 895c6e8c (Hash Join -> [Seq Scan (Outer), Hash (Inner)])
- **Consumes:** Nodes 17176, 17177, 17182, 17183, 17185, 17186, 17189
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=64945
  - HashJoin_nt1=1200243
  - HashJoin_nt2=18037
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=131
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0000
  - HashJoin_startup_cost=15065.2800
  - HashJoin_total_cost=148669.6400
  - Hash_Inner_np=0
  - Hash_Inner_nt=18037
  - Hash_Inner_nt1=18037
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=126
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=14794.7200
  - Hash_Inner_total_cost=14794.7200
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
- **Output:** st=176.20, rt=733.84

### Step 9: Node 17193 (Index Scan) - LEAF

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

### Step 10: Node 17180 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=64945
  - nt1=64945
  - nt2=1
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=733.8356
  - rt2=-0.0424
  - sel=1.0000
  - st1=176.1990
  - st2=0.0037
  - startup_cost=15065.7100
  - total_cost=178092.6500
- **Output:** st=125.31, rt=1179.58

### Step 11: Node 17179 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=64945
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=1179.5778
  - rt2=0.0000
  - sel=0.9262
  - st1=125.3064
  - st2=0.0000
  - startup_cost=179229.1900
  - total_cost=180131.4400
- **Output:** st=1147.23, rt=1152.73

### Step 12: Node 17178 (Gather)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=300750
  - nt1=60150
  - nt2=0
  - parallel_workers=5
  - plan_width=168
  - reltuples=0.0000
  - rt1=1152.7268
  - rt2=0.0000
  - sel=5.0000
  - st1=1147.2270
  - st2=0.0000
  - startup_cost=180229.1900
  - total_cost=211206.4400
- **Output:** st=578.56, rt=1135.98

### Step 13: Node 17176 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 1d35fb97 (Sort -> Aggregate (Outer))
- **Consumes:** Nodes 17177, 17181, 17182, 17183, 17185, 17186, 17189
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=60150
  - Aggregate_Outer_nt1=300750
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=168
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.2000
  - Aggregate_Outer_startup_cost=214213.9400
  - Aggregate_Outer_total_cost=215116.1900
  - Sort_np=0
  - Sort_nt=60150
  - Sort_nt1=60150
  - Sort_nt2=0
  - Sort_parallel_workers=0
  - Sort_plan_width=168
  - Sort_reltuples=0.0000
  - Sort_sel=1.0000
  - Sort_startup_cost=219890.9800
  - Sort_total_cost=220041.3600
- **Output:** st=1114.32, rt=1115.82
