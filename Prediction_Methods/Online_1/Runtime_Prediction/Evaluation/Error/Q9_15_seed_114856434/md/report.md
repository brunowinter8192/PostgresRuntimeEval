# Online Prediction Report

**Test Query:** Q9_15_seed_114856434
**Timestamp:** 2026-01-11 21:03:28

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 4.13%

## Phase C: Patterns in Query

- Total Patterns: 56

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 33781.0% | 113504.2307 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 172 | 3565.0% | 6131.8766 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 148 | 116.8% | 172.9284 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 147.6% | 141.6847 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 75.1% | 108.1438 |
| 2873b8c3 | Hash Join -> [Nested Loop -> [Seq Scan (... | 3 | 48 | 197.5% | 94.8003 |
| 30d6e09b | Hash Join -> [Hash Join -> [Nested Loop ... | 3 | 48 | 187.5% | 89.9904 |
| 7a51ce50 | Hash Join -> [Hash Join -> [Nested Loop ... | 4 | 48 | 187.5% | 89.9904 |
| 7d4e78be | Hash Join -> [Hash Join (Outer), Hash (I... | 2 | 48 | 187.5% | 89.9904 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 1a17c7f7 | Hash -> Hash Join -> [Hash Join (Outer),... | 3 | 24 | 76.5% | 18.3606 |
| 702e1a46 | Hash -> Hash Join -> [Hash Join -> [Nest... | 5 | 24 | 76.5% | 18.3606 |
| fee45978 | Hash -> Hash Join -> [Hash Join -> [Nest... | 4 | 24 | 76.5% | 18.3606 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 9.3% | 13.3894 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 96 | 13.0% | 12.4695 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 96 | 8.0% | 7.7175 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 140 | 4.5% | 6.2375 |
| 49ae7e42 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 24 | 19.2% | 4.5998 |
| e941d0ad | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 24 | 19.2% | 4.5998 |
| ed7f2e45 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 24 | 19.2% | 4.5998 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 116 | 3.5% | 4.0772 |
| 0405d50f | Aggregate -> Gather -> Aggregate -> Nest... | 4 | 20 | 18.3% | 3.6645 |
| 1c7aa67e | Aggregate -> Gather -> Aggregate -> Nest... | 10 | 20 | 18.3% | 3.6645 |
| 366e9db5 | Aggregate -> Gather -> Aggregate -> Nest... | 7 | 20 | 18.3% | 3.6645 |
| 51640d13 | Aggregate -> Gather -> Aggregate -> Nest... | 6 | 20 | 18.3% | 3.6645 |
| 6e1ec341 | Aggregate -> Gather -> Aggregate -> Nest... | 5 | 20 | 18.3% | 3.6645 |
| 88dc07c3 | Aggregate -> Gather -> Aggregate -> Nest... | 8 | 20 | 18.3% | 3.6645 |
| c94fcfda | Aggregate -> Gather -> Aggregate -> Nest... | 9 | 20 | 18.3% | 3.6645 |
| 3b447875 | Aggregate -> Nested Loop (Outer) | 2 | 44 | 8.1% | 3.5717 |
| bd9dfa7b | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 92 | 3.7% | 3.3601 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 72 | 4.0% | 2.9042 |
| 3ac23d41 | Gather -> Aggregate -> Nested Loop (Oute... | 3 | 20 | 8.3% | 1.6618 |
| 43da7031 | Gather -> Aggregate -> Nested Loop -> [H... | 4 | 20 | 8.3% | 1.6618 |
| 6ac77a36 | Gather -> Aggregate -> Nested Loop -> [H... | 6 | 20 | 8.3% | 1.6618 |
| 75cf2f59 | Gather -> Aggregate -> Nested Loop -> [H... | 8 | 20 | 8.3% | 1.6618 |
| a4e25603 | Gather -> Aggregate -> Nested Loop -> [H... | 5 | 20 | 8.3% | 1.6618 |
| d60fddc6 | Gather -> Aggregate -> Nested Loop -> [H... | 7 | 20 | 8.3% | 1.6618 |
| f17356e6 | Gather -> Aggregate -> Nested Loop -> [H... | 9 | 20 | 8.3% | 1.6618 |
| 6e659102 | Sort -> Aggregate -> Gather -> Aggregate... | 4 | 24 | 6.2% | 1.4968 |
| 4d81a89d | Sort -> Aggregate -> Gather -> Aggregate... | 9 | 20 | 5.2% | 1.0450 |
| 76ab422a | Sort -> Aggregate -> Gather -> Aggregate... | 10 | 20 | 5.2% | 1.0450 |
| 9e770981 | Sort -> Aggregate -> Gather -> Aggregate... | 7 | 20 | 5.2% | 1.0450 |
| a70c5941 | Sort -> Aggregate -> Gather -> Aggregate... | 5 | 20 | 5.2% | 1.0450 |
| d8d0a254 | Sort -> Aggregate -> Gather -> Aggregate... | 8 | 20 | 5.2% | 1.0450 |
| e9a32a5c | Sort -> Aggregate -> Gather -> Aggregate... | 6 | 20 | 5.2% | 1.0450 |
| f1e59da5 | Sort -> Aggregate -> Gather -> Aggregate... | 11 | 20 | 5.2% | 1.0450 |
| 2af8b806 | Aggregate -> Nested Loop -> [Hash Join -... | 7 | 20 | 2.7% | 0.5337 |
| 4251e9b4 | Aggregate -> Nested Loop -> [Hash Join (... | 3 | 20 | 2.7% | 0.5337 |
| 5305e2e5 | Aggregate -> Nested Loop -> [Hash Join -... | 8 | 20 | 2.7% | 0.5337 |
| 69ec2c4a | Aggregate -> Nested Loop -> [Hash Join -... | 4 | 20 | 2.7% | 0.5337 |
| 6b2db56d | Aggregate -> Nested Loop -> [Hash Join -... | 5 | 20 | 2.7% | 0.5337 |
| 7378d2b2 | Aggregate -> Nested Loop -> [Hash Join -... | 6 | 20 | 2.7% | 0.5337 |
| 3dbdd75b | Nested Loop -> [Hash Join -> [Seq Scan (... | 6 | 20 | 2.0% | 0.4014 |
| 7b7172dc | Nested Loop -> [Hash Join -> [Seq Scan (... | 5 | 20 | 2.0% | 0.4014 |
| dc9f4b49 | Nested Loop -> [Hash Join -> [Seq Scan (... | 7 | 20 | 2.0% | 0.4014 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 1 | 895c6e8c | 75736.1626 | 0.0004% | ACCEPTED | 17.92% |
| 2 | 7df893ad | 678.6757 | N/A | REJECTED | 17.92% |
| 3 | bb930825 | 188.3060 | -0.0000% | REJECTED | 17.92% |
| 4 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.92% |
| 5 | 2e0f44ef | 108.1433 | 0.0001% | ACCEPTED | 17.92% |
| 6 | 2873b8c3 | 121.6368 | 0.0000% | ACCEPTED | 17.92% |
| 7 | 30d6e09b | 42.9691 | N/A | REJECTED | 17.92% |
| 8 | 7a51ce50 | 42.9691 | 0.0000% | ACCEPTED | 17.92% |
| 9 | 7d4e78be | 59.2266 | N/A | REJECTED | 17.92% |
| 10 | 1d35fb97 | 26.4006 | 0.1163% | ACCEPTED | 17.81% |
| 11 | 4fc84c77 | 15.8328 | 0.6911% | ACCEPTED | 17.12% |
| 12 | 634cdbe2 | 9.1880 | N/A | REJECTED | 17.12% |
| 13 | 49ae7e42 | 7.6069 | N/A | REJECTED | 17.12% |
| 14 | e941d0ad | 7.6069 | N/A | REJECTED | 17.12% |
| 15 | ed7f2e45 | 7.6069 | N/A | REJECTED | 17.12% |
| 16 | a5f39f08 | 7.4593 | 1.1455% | ACCEPTED | 15.97% |
| 17 | 3cfa90d7 | 3.5091 | N/A | REJECTED | 15.97% |
| 18 | e0e3c3e1 | 2.9076 | -0.0000% | REJECTED | 15.97% |
| 19 | 0405d50f | 2.3736 | 0.0562% | ACCEPTED | 15.91% |
| 20 | b3a45093 | 1.6608 | -0.0009% | REJECTED | 15.91% |
| 21 | 6e659102 | 1.2037 | 0.0543% | ACCEPTED | 15.86% |
| 22 | 4d81a89d | 0.7585 | 0.1535% | ACCEPTED | 15.71% |
| 23 | 76ab422a | 0.2426 | 0.0000% | ACCEPTED | 15.71% |
| 24 | 9e770981 | 0.2426 | N/A | REJECTED | 15.71% |
| 25 | a70c5941 | 0.2426 | N/A | REJECTED | 15.71% |
| 26 | d8d0a254 | 0.2426 | N/A | REJECTED | 15.71% |
| 27 | e9a32a5c | 0.2426 | N/A | REJECTED | 15.71% |
| 28 | f1e59da5 | 0.2426 | N/A | REJECTED | 15.71% |
## Query Tree

```
Node 17665 (Sort) [PATTERN: 76ab422a] - ROOT
  Node 17666 (Aggregate) [consumed]
    Node 17667 (Gather) [consumed]
      Node 17668 (Aggregate) [consumed]
        Node 17669 (Nested Loop) [consumed]
          Node 17670 (Hash Join) [consumed]
            Node 17671 (Seq Scan) [consumed] - LEAF
            Node 17672 (Hash) [consumed]
              Node 17673 (Hash Join) [consumed]
                Node 17674 (Hash Join) [consumed]
                  Node 17675 (Nested Loop) [consumed]
                    Node 17676 (Seq Scan) - LEAF
                    Node 17677 (Index Scan) - LEAF
                  Node 17678 (Hash) [consumed]
                    Node 17679 (Seq Scan) - LEAF
                Node 17680 (Hash) [consumed]
                  Node 17681 (Seq Scan) [consumed] - LEAF
          Node 17682 (Index Scan) [consumed] - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Sort -> Aggregate -> Gather -> | 76ab422a | 17665 | 17666, 17667, 17668, 17669, 17670, 17671, 17672, 17673, 17674, 17675, 17678, 17680, 17681, 17682 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 0.71%
- Improvement: 3.41%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 17665 | Sort | 1186.48 | 1194.95 | 0.7% | pattern |
| 17676 | Seq Scan | 20.92 | 42.80 | 104.6% | operator |
| 17677 | Index Scan | 0.07 | 0.12 | 58.9% | operator |
| 17679 | Seq Scan | 3.26 | 10.62 | 226.0% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 17676 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=4843
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0242
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=0.41, rt=42.80

### Step 2: Node 17677 (Index Scan) - LEAF

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
  - total_cost=1.8900
- **Output:** st=0.07, rt=0.12

### Step 3: Node 17679 (Seq Scan) - LEAF

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

### Step 4: Node 17665 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 76ab422a (Sort -> Aggregate -> Gather -> Aggregate -> Nested Loop -> [Hash Join -> [Seq Scan (Outer), Hash -> Hash Join -> [Hash Join -> [Nested Loop (Outer), Hash (Inner)] (Outer), Hash -> Seq Scan (Outer) (Inner)] (Outer) (Inner)] (Outer), Index Scan (Inner)] (Outer) (Outer) (Outer) (Outer))
- **Consumes:** Nodes 17666, 17667, 17668, 17669, 17670, 17671, 17672, 17673, 17674, 17675, 17678, 17680, 17681, 17682
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=60150
  - Aggregate_Outer_nt1=69752
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=168
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.8623
  - Aggregate_Outer_startup_cost=181816.3900
  - Aggregate_Outer_total_cost=182718.6400
  - Gather_Outer_np=0
  - Gather_Outer_nt=300750
  - Gather_Outer_nt1=60150
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=5
  - Gather_Outer_plan_width=168
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=5.0000
  - Gather_Outer_startup_cost=182816.3900
  - Gather_Outer_total_cost=213793.6400
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=19372
  - HashJoin_Outer_nt1=19372
  - HashJoin_Outer_nt2=10000
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=26
  - HashJoin_Outer_reltuples=0.0000
  - HashJoin_Outer_sel=0.0001
  - HashJoin_Outer_startup_cost=448.4300
  - HashJoin_Outer_total_cost=15038.9400
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
  - IndexScan_Inner_np=26136
  - IndexScan_Inner_nt=1
  - IndexScan_Inner_nt1=0
  - IndexScan_Inner_nt2=0
  - IndexScan_Inner_parallel_workers=0
  - IndexScan_Inner_plan_width=8
  - IndexScan_Inner_reltuples=1500000.0000
  - IndexScan_Inner_sel=0.0000
  - IndexScan_Inner_startup_cost=0.4300
  - IndexScan_Inner_total_cost=0.4500
  - NestedLoop_Outer_np=0
  - NestedLoop_Outer_nt=19372
  - NestedLoop_Outer_nt1=4843
  - NestedLoop_Outer_nt2=4
  - NestedLoop_Outer_parallel_workers=0
  - NestedLoop_Outer_plan_width=18
  - NestedLoop_Outer_reltuples=0.0000
  - NestedLoop_Outer_sel=1.0000
  - NestedLoop_Outer_startup_cost=0.4200
  - NestedLoop_Outer_total_cost=14540.0600
  - SeqScan_Outer_np=1
  - SeqScan_Outer_nt=25
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=108
  - SeqScan_Outer_reltuples=25.0000
  - SeqScan_Outer_sel=1.0000
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=1.2500
  - Sort_np=0
  - Sort_nt=60150
  - Sort_nt1=60150
  - Sort_nt2=0
  - Sort_parallel_workers=0
  - Sort_plan_width=168
  - Sort_reltuples=0.0000
  - Sort_sel=1.0000
  - Sort_startup_cost=222478.1800
  - Sort_total_cost=222628.5500
- **Output:** st=1189.34, rt=1194.95
