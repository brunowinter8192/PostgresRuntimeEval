# Online Prediction Report

**Test Query:** Q9_26_seed_205100775
**Timestamp:** 2026-01-11 19:13:31

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 9.68%

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
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 96 | 13.0% | 12.4695 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 147.6% | 141.6847 |
| bd9dfa7b | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 92 | 3.7% | 3.3601 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 72 | 4.0% | 2.9042 |
| 7d4e78be | Hash Join -> [Hash Join (Outer), Hash (I... | 2 | 48 | 187.5% | 89.9904 |
| 2873b8c3 | Hash Join -> [Nested Loop -> [Seq Scan (... | 3 | 48 | 197.5% | 94.8003 |
| 30d6e09b | Hash Join -> [Hash Join -> [Nested Loop ... | 3 | 48 | 187.5% | 89.9904 |
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
| 0405d50f | Aggregate -> Gather -> Aggregate -> Nest... | 4 | 20 | 18.3% | 3.6645 |
| 4251e9b4 | Aggregate -> Nested Loop -> [Hash Join (... | 3 | 20 | 2.7% | 0.5337 |
| 43da7031 | Gather -> Aggregate -> Nested Loop -> [H... | 4 | 20 | 8.3% | 1.6618 |
| a70c5941 | Sort -> Aggregate -> Gather -> Aggregate... | 5 | 20 | 5.2% | 1.0450 |
| 69ec2c4a | Aggregate -> Nested Loop -> [Hash Join -... | 4 | 20 | 2.7% | 0.5337 |
| 6e1ec341 | Aggregate -> Gather -> Aggregate -> Nest... | 5 | 20 | 18.3% | 3.6645 |
| 6b2db56d | Aggregate -> Nested Loop -> [Hash Join -... | 5 | 20 | 2.7% | 0.5337 |
| a4e25603 | Gather -> Aggregate -> Nested Loop -> [H... | 5 | 20 | 8.3% | 1.6618 |
| e9a32a5c | Sort -> Aggregate -> Gather -> Aggregate... | 6 | 20 | 5.2% | 1.0450 |
| 51640d13 | Aggregate -> Gather -> Aggregate -> Nest... | 6 | 20 | 18.3% | 3.6645 |
| 6ac77a36 | Gather -> Aggregate -> Nested Loop -> [H... | 6 | 20 | 8.3% | 1.6618 |
| 7b7172dc | Nested Loop -> [Hash Join -> [Seq Scan (... | 5 | 20 | 2.0% | 0.4014 |
| 366e9db5 | Aggregate -> Gather -> Aggregate -> Nest... | 7 | 20 | 18.3% | 3.6645 |
| 7378d2b2 | Aggregate -> Nested Loop -> [Hash Join -... | 6 | 20 | 2.7% | 0.5337 |
| 9e770981 | Sort -> Aggregate -> Gather -> Aggregate... | 7 | 20 | 5.2% | 1.0450 |
| d60fddc6 | Gather -> Aggregate -> Nested Loop -> [H... | 7 | 20 | 8.3% | 1.6618 |
| d8d0a254 | Sort -> Aggregate -> Gather -> Aggregate... | 8 | 20 | 5.2% | 1.0450 |
| 3dbdd75b | Nested Loop -> [Hash Join -> [Seq Scan (... | 6 | 20 | 2.0% | 0.4014 |
| 88dc07c3 | Aggregate -> Gather -> Aggregate -> Nest... | 8 | 20 | 18.3% | 3.6645 |
| 2af8b806 | Aggregate -> Nested Loop -> [Hash Join -... | 7 | 20 | 2.7% | 0.5337 |
| 4d81a89d | Sort -> Aggregate -> Gather -> Aggregate... | 9 | 20 | 5.2% | 1.0450 |
| 75cf2f59 | Gather -> Aggregate -> Nested Loop -> [H... | 8 | 20 | 8.3% | 1.6618 |
| c94fcfda | Aggregate -> Gather -> Aggregate -> Nest... | 9 | 20 | 18.3% | 3.6645 |
| dc9f4b49 | Nested Loop -> [Hash Join -> [Seq Scan (... | 7 | 20 | 2.0% | 0.4014 |
| 5305e2e5 | Aggregate -> Nested Loop -> [Hash Join -... | 8 | 20 | 2.7% | 0.5337 |
| 76ab422a | Sort -> Aggregate -> Gather -> Aggregate... | 10 | 20 | 5.2% | 1.0450 |
| f17356e6 | Gather -> Aggregate -> Nested Loop -> [H... | 9 | 20 | 8.3% | 1.6618 |
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
| 1 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 2 | 1d35fb97 | 26.4017 | 0.1163% | ACCEPTED | 17.81% |
| 3 | 7df893ad | 6131.8766 | N/A | REJECTED | 17.81% |
| 4 | bb930825 | 172.9284 | -0.0000% | REJECTED | 17.81% |
| 5 | 4fc84c77 | 13.3894 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 6 | 2e0f44ef | 108.1438 | 0.0001% | ACCEPTED | 17.81% |
| 7 | 3cfa90d7 | 6.2375 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 8 | e0e3c3e1 | 4.0772 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 9 | 634cdbe2 | 7.7175 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 10 | a5f39f08 | 12.4695 | 1.8366% | ACCEPTED | 15.97% |
| 11 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 15.97% |
| 12 | bd9dfa7b | 3.3601 | N/A | SKIPPED_LOW_ERROR | 15.97% |
| 13 | b3a45093 | 2.9042 | N/A | SKIPPED_LOW_ERROR | 15.97% |
| 14 | 7d4e78be | 89.9904 | N/A | REJECTED | 15.97% |
| 15 | 2873b8c3 | 94.8003 | N/A | REJECTED | 15.97% |
| 16 | 30d6e09b | 89.9904 | N/A | REJECTED | 15.97% |
| 17 | 7a51ce50 | 89.9904 | N/A | REJECTED | 15.97% |
| 18 | 3b447875 | 3.5717 | N/A | SKIPPED_LOW_ERROR | 15.97% |
| 19 | 1a17c7f7 | 18.3606 | N/A | REJECTED | 15.97% |
| 20 | 6e659102 | 1.4968 | N/A | SKIPPED_LOW_ERROR | 15.97% |
| 21 | e941d0ad | 4.5998 | N/A | REJECTED | 15.97% |
| 22 | fee45978 | 18.3606 | N/A | REJECTED | 15.97% |
| 23 | 49ae7e42 | 4.5998 | N/A | REJECTED | 15.97% |
| 24 | 702e1a46 | 18.3606 | N/A | REJECTED | 15.97% |
| 25 | ed7f2e45 | 4.5998 | N/A | REJECTED | 15.97% |
| 26 | 3ac23d41 | 1.6618 | N/A | SKIPPED_LOW_ERROR | 15.97% |
| 27 | 0405d50f | 3.6645 | 0.0562% | ACCEPTED | 15.91% |
| 28 | 4251e9b4 | 0.5337 | N/A | SKIPPED_LOW_ERROR | 15.91% |
| 29 | 43da7031 | 1.6618 | N/A | SKIPPED_LOW_ERROR | 15.91% |
| 30 | a70c5941 | 1.0450 | N/A | SKIPPED_LOW_ERROR | 15.91% |
| 31 | 69ec2c4a | 0.5337 | N/A | SKIPPED_LOW_ERROR | 15.91% |
| 32 | 6e1ec341 | 3.6645 | -0.0000% | REJECTED | 15.91% |
| 33 | 6b2db56d | 0.5337 | N/A | SKIPPED_LOW_ERROR | 15.91% |
| 34 | a4e25603 | 1.6618 | N/A | SKIPPED_LOW_ERROR | 15.91% |
| 35 | e9a32a5c | 1.0450 | N/A | SKIPPED_LOW_ERROR | 15.91% |
| 36 | 51640d13 | 3.6645 | -0.0000% | REJECTED | 15.91% |
| 37 | 6ac77a36 | 1.6618 | N/A | SKIPPED_LOW_ERROR | 15.91% |
| 38 | 7b7172dc | 0.4014 | N/A | SKIPPED_LOW_ERROR | 15.91% |
| 39 | 366e9db5 | 3.6645 | -0.0000% | REJECTED | 15.91% |
| 40 | 7378d2b2 | 0.5337 | N/A | SKIPPED_LOW_ERROR | 15.91% |
| 41 | 9e770981 | 1.0450 | N/A | SKIPPED_LOW_ERROR | 15.91% |
| 42 | d60fddc6 | 1.6618 | N/A | SKIPPED_LOW_ERROR | 15.91% |
| 43 | d8d0a254 | 1.0450 | N/A | SKIPPED_LOW_ERROR | 15.91% |
| 44 | 3dbdd75b | 0.4014 | N/A | SKIPPED_LOW_ERROR | 15.91% |
| 45 | 88dc07c3 | 3.6645 | -0.0000% | REJECTED | 15.91% |
| 46 | 2af8b806 | 0.5337 | N/A | SKIPPED_LOW_ERROR | 15.91% |
| 47 | 4d81a89d | 1.0450 | N/A | SKIPPED_LOW_ERROR | 15.91% |
| 48 | 75cf2f59 | 1.6618 | N/A | SKIPPED_LOW_ERROR | 15.91% |
| 49 | c94fcfda | 3.6645 | -0.0000% | REJECTED | 15.91% |
| 50 | dc9f4b49 | 0.4014 | N/A | SKIPPED_LOW_ERROR | 15.91% |
| 51 | 5305e2e5 | 0.5337 | N/A | SKIPPED_LOW_ERROR | 15.91% |
| 52 | 76ab422a | 1.0450 | N/A | SKIPPED_LOW_ERROR | 15.91% |
| 53 | f17356e6 | 1.6618 | N/A | SKIPPED_LOW_ERROR | 15.91% |
| 54 | 1c7aa67e | 3.6645 | -0.0000% | REJECTED | 15.91% |
| 55 | f1e59da5 | 1.0450 | N/A | SKIPPED_LOW_ERROR | 15.91% |
## Query Tree

```
Node 17883 (Sort) - ROOT
  Node 17884 (Aggregate) [PATTERN: 0405d50f]
    Node 17885 (Gather) [consumed]
      Node 17886 (Aggregate) [consumed]
        Node 17887 (Nested Loop) [consumed]
          Node 17888 (Hash Join) [PATTERN: 895c6e8c]
            Node 17889 (Seq Scan) [consumed] - LEAF
            Node 17890 (Hash) [consumed]
              Node 17891 (Hash Join)
                Node 17892 (Hash Join) [PATTERN: 2e0f44ef]
                  Node 17893 (Nested Loop) [consumed]
                    Node 17894 (Seq Scan) - LEAF
                    Node 17895 (Index Scan) - LEAF
                  Node 17896 (Hash) [consumed]
                    Node 17897 (Seq Scan) - LEAF
                Node 17898 (Hash)
                  Node 17899 (Seq Scan) - LEAF
          Node 17900 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | 0405d50f | 17884 | 17885, 17886, 17887, 17888, 17889, 17890, 17892, 17893, 17896 |
| Hash Join -> [Seq Scan (Outer) | 895c6e8c | 17888 | 17884, 17885, 17886, 17887, 17889, 17890, 17892, 17893, 17896 |
| Hash Join -> [Nested Loop (Out | 2e0f44ef | 17892 | 17884, 17885, 17886, 17887, 17888, 17889, 17890, 17893, 17896 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 7.90%
- Improvement: 1.78%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 17883 | Sort | 1259.70 | 1160.18 | 7.9% | operator |
| 17884 | Aggregate | 1259.57 | 1194.84 | 5.1% | pattern |
| 17888 | Hash Join | 1043.47 | 734.36 | 29.6% | pattern |
| 17900 | Index Scan | 0.00 | -0.04 | 1512.7% | operator |
| 17891 | Hash Join | 188.01 | 820.76 | 336.6% | operator |
| 17892 | Hash Join | 174.33 | 981.04 | 462.7% | pattern |
| 17898 | Hash | 13.05 | 14.54 | 11.4% | operator |
| 17899 | Seq Scan | 13.04 | 7.19 | 44.8% | operator |
| 17894 | Seq Scan | 19.85 | 42.74 | 115.3% | operator |
| 17895 | Index Scan | 0.08 | 0.12 | 47.1% | operator |
| 17897 | Seq Scan | 4.91 | 10.62 | 116.1% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 17894 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=5010
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0250
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=0.41, rt=42.74

### Step 2: Node 17895 (Index Scan) - LEAF

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
  - total_cost=1.8600
- **Output:** st=0.07, rt=0.12

### Step 3: Node 17897 (Seq Scan) - LEAF

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

### Step 4: Node 17899 (Seq Scan) - LEAF

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

### Step 5: Node 17892 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 2e0f44ef (Hash Join -> [Nested Loop (Outer), Hash (Inner)])
- **Consumes:** Nodes 17884, 17885, 17886, 17887, 17888, 17889, 17890, 17893, 17896
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=20040
  - HashJoin_nt1=20040
  - HashJoin_nt2=10000
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=26
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0001
  - HashJoin_startup_cost=448.4300
  - HashJoin_total_cost=15187.9200
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
  - NestedLoop_Outer_nt=20040
  - NestedLoop_Outer_nt1=5010
  - NestedLoop_Outer_nt2=4
  - NestedLoop_Outer_parallel_workers=0
  - NestedLoop_Outer_plan_width=18
  - NestedLoop_Outer_reltuples=0.0000
  - NestedLoop_Outer_sel=1.0000
  - NestedLoop_Outer_startup_cost=0.4200
  - NestedLoop_Outer_total_cost=14687.3000
- **Output:** st=5.38, rt=981.04

### Step 6: Node 17898 (Hash)

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

### Step 7: Node 17891 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=20040
  - nt1=20040
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=981.0376
  - rt2=14.5397
  - sel=0.0400
  - st1=5.3840
  - st2=14.5393
  - startup_cost=449.9900
  - total_cost=15251.0100
- **Output:** st=26.52, rt=820.76

### Step 8: Node 17888 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 895c6e8c (Hash Join -> [Seq Scan (Outer), Hash (Inner)])
- **Consumes:** Nodes 17884, 17885, 17886, 17887, 17889, 17890, 17892, 17893, 17896
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=72159
  - HashJoin_nt1=1200243
  - HashJoin_nt2=20040
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=131
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0000
  - HashJoin_startup_cost=15551.6100
  - HashJoin_total_cost=149155.9800
  - Hash_Inner_np=0
  - Hash_Inner_nt=20040
  - Hash_Inner_nt1=20040
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=126
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=15251.0100
  - Hash_Inner_total_cost=15251.0100
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
- **Output:** st=176.13, rt=734.36

### Step 9: Node 17900 (Index Scan) - LEAF

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

### Step 10: Node 17884 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 0405d50f (Aggregate -> Gather -> Aggregate -> Nested Loop (Outer) (Outer) (Outer))
- **Consumes:** Nodes 17885, 17886, 17887, 17888, 17889, 17890, 17892, 17893, 17896
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=60150
  - Aggregate_Outer_nt1=72159
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=168
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.8336
  - Aggregate_Outer_startup_cost=183110.0500
  - Aggregate_Outer_total_cost=184012.3000
  - Aggregate_np=0
  - Aggregate_nt=60150
  - Aggregate_nt1=300750
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=168
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=218094.8000
  - Aggregate_total_cost=218997.0500
  - Gather_Outer_np=0
  - Gather_Outer_nt=300750
  - Gather_Outer_nt1=60150
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=5
  - Gather_Outer_plan_width=168
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=5.0000
  - Gather_Outer_startup_cost=184110.0500
  - Gather_Outer_total_cost=215087.3000
  - NestedLoop_Outer_np=0
  - NestedLoop_Outer_nt=72159
  - NestedLoop_Outer_nt1=72159
  - NestedLoop_Outer_nt2=1
  - NestedLoop_Outer_parallel_workers=0
  - NestedLoop_Outer_plan_width=159
  - NestedLoop_Outer_reltuples=0.0000
  - NestedLoop_Outer_sel=1.0000
  - NestedLoop_Outer_startup_cost=15552.0400
  - NestedLoop_Outer_total_cost=181847.2600
- **Output:** st=1188.78, rt=1194.84

### Step 11: Node 17883 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=60150
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=1194.8356
  - rt2=0.0000
  - sel=1.0000
  - st1=1188.7827
  - st2=0.0000
  - startup_cost=223771.8400
  - total_cost=223922.2100
- **Output:** st=1157.62, rt=1160.18
