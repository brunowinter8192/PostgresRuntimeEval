# Online Prediction Report

**Test Query:** Q8_127_seed_1033707906
**Timestamp:** 2026-01-11 20:50:43

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 3.86%

## Phase C: Patterns in Query

- Total Patterns: 82

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 33781.0% | 113504.2307 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 168 | 44967.0% | 75544.5822 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 172 | 3565.0% | 6131.8766 |
| c0a8d3de | Hash -> Hash Join -> [Seq Scan (Outer), ... | 3 | 148 | 4130.8% | 6113.5159 |
| a54055ce | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 96 | 6342.9% | 6089.1983 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 148 | 116.8% | 172.9284 |
| 37515ad8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 124 | 135.7% | 168.3286 |
| 545b5e57 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 72 | 212.7% | 153.1732 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 75.1% | 108.1438 |
| 444761fb | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 52 | 46.8% | 24.3176 |
| 314469b0 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 5 | 48 | 43.2% | 20.7410 |
| 54cb7f90 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 6 | 48 | 43.2% | 20.7410 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| 3e2d5a00 | Sort -> Hash Join (Outer) | 2 | 96 | 19.3% | 18.5586 |
| ec92bdaa | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 52 | 29.1% | 15.1555 |
| c302739b | Hash Join -> [Seq Scan (Outer), Hash -> ... | 7 | 48 | 27.6% | 13.2381 |
| e1d7e5b4 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 48 | 27.6% | 13.2381 |
| 2422d111 | Hash Join -> [Nested Loop -> [Hash Join ... | 3 | 72 | 15.0% | 10.7757 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 96 | 7.6% | 7.3257 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 140 | 4.5% | 6.2375 |
| 3d4c3db9 | Hash Join -> [Nested Loop -> [Hash Join ... | 7 | 48 | 12.3% | 5.9049 |
| 440e6274 | Hash Join -> [Nested Loop -> [Hash Join ... | 5 | 48 | 12.3% | 5.9049 |
| 4db07220 | Hash Join -> [Nested Loop -> [Hash Join ... | 4 | 48 | 12.3% | 5.9049 |
| 9ce781b0 | Hash Join -> [Nested Loop -> [Hash Join ... | 8 | 48 | 12.3% | 5.9049 |
| a95bee4e | Hash Join -> [Nested Loop -> [Hash Join ... | 9 | 48 | 12.3% | 5.9049 |
| f4603221 | Hash Join -> [Nested Loop -> [Hash Join ... | 6 | 48 | 12.3% | 5.9049 |
| 6981af52 | Hash Join -> [Nested Loop -> [Hash Join ... | 5 | 24 | 20.3% | 4.8707 |
| 800ffecc | Hash Join -> [Nested Loop -> [Hash Join ... | 7 | 24 | 20.3% | 4.8707 |
| 910f6702 | Hash Join -> [Nested Loop -> [Hash Join ... | 10 | 24 | 20.3% | 4.8707 |
| 9d50c2fc | Hash Join -> [Nested Loop -> [Hash Join ... | 8 | 24 | 20.3% | 4.8707 |
| b88a3db4 | Hash Join -> [Nested Loop -> [Hash Join ... | 6 | 24 | 20.3% | 4.8707 |
| c5dad784 | Hash Join -> [Nested Loop -> [Hash Join ... | 4 | 24 | 20.3% | 4.8707 |
| cee0b988 | Hash Join -> [Nested Loop -> [Hash Join ... | 9 | 24 | 20.3% | 4.8707 |
| fb7bcc0c | Hash Join -> [Nested Loop -> [Hash Join ... | 11 | 24 | 20.3% | 4.8707 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 96 | 4.7% | 4.4662 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 116 | 3.5% | 4.0772 |
| 91d6e559 | Sort -> Hash Join -> [Nested Loop (Outer... | 3 | 72 | 5.4% | 3.8546 |
| bd9dfa7b | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 92 | 3.7% | 3.3601 |
| 3c6d8006 | Gather Merge -> Sort -> Hash Join -> [Ne... | 4 | 48 | 6.2% | 2.9727 |
| 98d4ff98 | Gather Merge -> Sort -> Hash Join (Outer... | 3 | 48 | 6.2% | 2.9727 |
| 9d0e407c | Nested Loop -> [Hash Join -> [Seq Scan (... | 5 | 72 | 4.1% | 2.9587 |
| 12e6457c | Sort -> Hash Join -> [Nested Loop -> [Ha... | 4 | 48 | 6.0% | 2.9009 |
| 06857491 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 11 | 24 | 10.2% | 2.4503 |
| 1d069442 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 9 | 24 | 10.2% | 2.4503 |
| 58ed95a8 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 5 | 24 | 10.2% | 2.4503 |
| 5d01b240 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 7 | 24 | 10.2% | 2.4503 |
| 8febc667 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 12 | 24 | 10.2% | 2.4503 |
| be705a2d | Sort -> Hash Join -> [Nested Loop -> [Ha... | 6 | 24 | 10.2% | 2.4503 |
| c7b8fb6d | Sort -> Hash Join -> [Nested Loop -> [Ha... | 8 | 24 | 10.2% | 2.4503 |
| d00b75d6 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 10 | 24 | 10.2% | 2.4503 |
| 19fc9abd | Nested Loop -> [Hash Join -> [Nested Loo... | 10 | 24 | 9.0% | 2.1603 |
| 45158dca | Nested Loop -> [Hash Join -> [Nested Loo... | 6 | 24 | 9.0% | 2.1603 |
| 473ac852 | Nested Loop -> [Hash Join -> [Nested Loo... | 7 | 24 | 9.0% | 2.1603 |
| 959de0c2 | Nested Loop -> [Hash Join -> [Nested Loo... | 8 | 24 | 9.0% | 2.1603 |
| 9b49df80 | Nested Loop -> [Hash Join -> [Nested Loo... | 5 | 24 | 9.0% | 2.1603 |
| bf197fca | Nested Loop -> [Hash Join -> [Nested Loo... | 9 | 24 | 9.0% | 2.1603 |
| c5a9eefd | Nested Loop -> [Hash Join -> [Nested Loo... | 4 | 24 | 9.0% | 2.1603 |
| f62279eb | Nested Loop -> [Hash Join -> [Nested Loo... | 3 | 24 | 9.0% | 2.1603 |
| 5ae97df8 | Nested Loop -> [Hash Join -> [Seq Scan (... | 8 | 48 | 4.4% | 2.1340 |
| 5bfce159 | Nested Loop -> [Hash Join -> [Seq Scan (... | 6 | 48 | 4.4% | 2.1340 |
| ef93d4fc | Nested Loop -> [Hash Join -> [Seq Scan (... | 7 | 48 | 4.4% | 2.1340 |
| 50ace808 | Gather Merge -> Sort -> Hash Join -> [Ne... | 11 | 24 | 7.9% | 1.8886 |
| 82a8bdb2 | Gather Merge -> Sort -> Hash Join -> [Ne... | 9 | 24 | 7.9% | 1.8886 |
| 839648da | Gather Merge -> Sort -> Hash Join -> [Ne... | 6 | 24 | 7.9% | 1.8886 |
| 860d9d3a | Gather Merge -> Sort -> Hash Join -> [Ne... | 12 | 24 | 7.9% | 1.8886 |
| d8d77761 | Gather Merge -> Sort -> Hash Join -> [Ne... | 7 | 24 | 7.9% | 1.8886 |
| db6a761f | Gather Merge -> Sort -> Hash Join -> [Ne... | 5 | 24 | 7.9% | 1.8886 |
| e31c99cb | Gather Merge -> Sort -> Hash Join -> [Ne... | 10 | 24 | 7.9% | 1.8886 |
| ef63c60f | Gather Merge -> Sort -> Hash Join -> [Ne... | 8 | 24 | 7.9% | 1.8886 |
| ffc3be98 | Gather Merge -> Sort -> Hash Join -> [Ne... | 13 | 24 | 7.9% | 1.8886 |
| 53f9aa07 | Aggregate -> Gather Merge -> Sort -> Has... | 5 | 48 | 2.2% | 1.0579 |
| b149ff28 | Aggregate -> Gather Merge -> Sort -> Has... | 4 | 48 | 2.2% | 1.0579 |
| 264d1e57 | Aggregate -> Gather Merge -> Sort -> Has... | 13 | 24 | 3.2% | 0.7651 |
| 59f6581f | Aggregate -> Gather Merge -> Sort -> Has... | 7 | 24 | 3.2% | 0.7651 |
| 7f3b31ff | Aggregate -> Gather Merge -> Sort -> Has... | 8 | 24 | 3.2% | 0.7651 |
| 96f339c9 | Aggregate -> Gather Merge -> Sort -> Has... | 11 | 24 | 3.2% | 0.7651 |
| 9b77a70e | Aggregate -> Gather Merge -> Sort -> Has... | 12 | 24 | 3.2% | 0.7651 |
| acd22c74 | Aggregate -> Gather Merge -> Sort -> Has... | 14 | 24 | 3.2% | 0.7651 |
| b659e5bf | Aggregate -> Gather Merge -> Sort -> Has... | 10 | 24 | 3.2% | 0.7651 |
| c9736a93 | Aggregate -> Gather Merge -> Sort -> Has... | 6 | 24 | 3.2% | 0.7651 |
| cb7eed03 | Aggregate -> Gather Merge -> Sort -> Has... | 9 | 24 | 3.2% | 0.7651 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 1 | 895c6e8c | 75736.1626 | 0.0004% | ACCEPTED | 17.92% |
| 2 | f4cb205a | 41652.9228 | 0.0005% | ACCEPTED | 17.92% |
| 3 | 7df893ad | 628.5971 | N/A | REJECTED | 17.92% |
| 4 | c0a8d3de | 540.8859 | 0.0000% | ACCEPTED | 17.92% |
| 5 | a54055ce | 350.8449 | 0.0000% | ACCEPTED | 17.92% |
| 6 | bb930825 | 184.4803 | -0.0000% | REJECTED | 17.92% |
| 7 | 37515ad8 | 173.2469 | -0.0000% | REJECTED | 17.92% |
| 8 | 545b5e57 | 152.9942 | -0.0000% | REJECTED | 17.92% |
| 9 | 2e0f44ef | 108.1203 | 0.0001% | ACCEPTED | 17.92% |
| 10 | 444761fb | 50.2829 | 0.0000% | ACCEPTED | 17.92% |
| 11 | ec92bdaa | 20.2515 | -0.0000% | REJECTED | 17.92% |
| 12 | 2724c080 | 19.6006 | 0.0222% | ACCEPTED | 17.90% |
| 13 | 3e2d5a00 | 18.4265 | N/A | REJECTED | 17.90% |
| 14 | c302739b | 18.3306 | N/A | REJECTED | 17.90% |
| 15 | e1d7e5b4 | 18.3306 | N/A | REJECTED | 17.90% |
| 16 | 29ee00db | 4.4857 | 0.2706% | ACCEPTED | 17.63% |
| 17 | 3cfa90d7 | 4.0055 | N/A | REJECTED | 17.63% |
| 18 | e0e3c3e1 | 3.3189 | 0.0000% | ACCEPTED | 17.63% |
| 19 | 2422d111 | 6.3844 | N/A | REJECTED | 17.63% |
| 20 | 3d4c3db9 | 5.8958 | N/A | REJECTED | 17.63% |
| 21 | 440e6274 | 5.8958 | N/A | REJECTED | 17.63% |
| 22 | 4db07220 | 5.8958 | N/A | REJECTED | 17.63% |
| 23 | 9ce781b0 | 5.8958 | N/A | REJECTED | 17.63% |
| 24 | a95bee4e | 5.8958 | N/A | REJECTED | 17.63% |
| 25 | f4603221 | 5.8958 | N/A | REJECTED | 17.63% |
| 26 | bd9dfa7b | 2.5603 | 0.0000% | ACCEPTED | 17.63% |
| 27 | 9d0e407c | 2.4353 | N/A | REJECTED | 17.63% |
| 28 | 5ae97df8 | 1.6108 | N/A | REJECTED | 17.63% |
| 29 | 5bfce159 | 1.6108 | N/A | REJECTED | 17.63% |
| 30 | ef93d4fc | 1.6108 | N/A | REJECTED | 17.63% |
| 31 | 53f9aa07 | 1.3983 | 0.2414% | ACCEPTED | 17.39% |
| 32 | 91d6e559 | 1.3357 | N/A | REJECTED | 17.39% |
| 33 | 12e6457c | 0.8905 | N/A | REJECTED | 17.39% |
| 34 | b149ff28 | 0.5871 | N/A | REJECTED | 17.39% |
| 35 | 264d1e57 | 0.3097 | -0.0002% | REJECTED | 17.39% |
| 36 | 59f6581f | 0.3097 | -0.0002% | REJECTED | 17.39% |
| 37 | 7f3b31ff | 0.3097 | -0.0002% | REJECTED | 17.39% |
| 38 | 96f339c9 | 0.3097 | -0.0002% | REJECTED | 17.39% |
| 39 | 9b77a70e | 0.3097 | -0.0002% | REJECTED | 17.39% |
| 40 | acd22c74 | 0.3097 | -0.0002% | REJECTED | 17.39% |
| 41 | b659e5bf | 0.3097 | -0.0002% | REJECTED | 17.39% |
| 42 | c9736a93 | 0.3097 | -0.0002% | REJECTED | 17.39% |
| 43 | cb7eed03 | 0.3097 | -0.0002% | REJECTED | 17.39% |
## Query Tree

```
Node 13868 (Aggregate) [PATTERN: 53f9aa07] - ROOT
  Node 13869 (Gather Merge) [consumed]
    Node 13870 (Sort) [consumed]
      Node 13871 (Hash Join) [consumed]
        Node 13872 (Nested Loop) [consumed]
          Node 13873 (Hash Join)
            Node 13874 (Nested Loop) [PATTERN: bd9dfa7b]
              Node 13875 (Hash Join) [consumed]
                Node 13876 (Seq Scan) [consumed] - LEAF
                Node 13877 (Hash) [consumed]
                  Node 13878 (Hash Join) [consumed]
                    Node 13879 (Seq Scan) - LEAF
                    Node 13880 (Hash) [PATTERN: a54055ce]
                      Node 13881 (Hash Join) [consumed]
                        Node 13882 (Seq Scan) [consumed] - LEAF
                        Node 13883 (Hash) [consumed]
                          Node 13884 (Seq Scan) [consumed] - LEAF
              Node 13885 (Index Scan) [consumed] - LEAF
            Node 13886 (Hash)
              Node 13887 (Seq Scan) - LEAF
          Node 13888 (Index Scan) - LEAF
        Node 13889 (Hash) [consumed]
          Node 13890 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather Merge -> S | 53f9aa07 | 13868 | 13869, 13870, 13871, 13872, 13874, 13875, 13876, 13877, 13878, 13880, 13881, 13882, 13883, 13884, 13885, 13889 |
| Hash -> Hash Join -> [Seq Scan | a54055ce | 13880 | 13868, 13869, 13870, 13871, 13872, 13874, 13875, 13876, 13877, 13878, 13881, 13882, 13883, 13884, 13885, 13889 |
| Nested Loop -> [Hash Join -> [ | bd9dfa7b | 13874 | 13868, 13869, 13870, 13871, 13872, 13875, 13876, 13877, 13878, 13880, 13881, 13882, 13883, 13884, 13885, 13889 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 0.10%
- Improvement: 3.76%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 13868 | Aggregate | 1219.25 | 1220.42 | 0.1% | pattern |
| 13873 | Hash Join | 1209.13 | 1042.87 | 13.7% | operator |
| 13888 | Index Scan | 0.01 | 0.05 | 753.5% | operator |
| 13890 | Seq Scan | 0.01 | 7.19 | 71844.7% | operator |
| 13874 | Nested Loop | 1161.85 | 1155.06 | 0.6% | pattern |
| 13886 | Hash | 42.78 | 17.76 | 58.5% | operator |
| 13887 | Seq Scan | 42.72 | 44.47 | 4.1% | operator |
| 13879 | Seq Scan | 35.11 | 24.87 | 29.1% | operator |
| 13880 | Hash | 0.24 | 0.20 | 19.3% | pattern |

## Prediction Chain (Bottom-Up)

### Step 1: Node 13879 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=3600
  - nt=62500
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=150000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.4167
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=4225.0000
- **Output:** st=0.28, rt=24.87

### Step 2: Node 13880 (Hash) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** a54055ce (Hash -> Hash Join -> [Seq Scan (Outer), Hash -> Seq Scan (Outer) (Inner)] (Outer))
- **Consumes:** Nodes 13868, 13869, 13870, 13871, 13872, 13874, 13875, 13876, 13877, 13878, 13881, 13882, 13883, 13884, 13885, 13889
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
  - Hash_Inner_nt=1
  - Hash_Inner_nt1=1
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=4
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=1.0600
  - Hash_Inner_total_cost=1.0600
  - Hash_np=0
  - Hash_nt=5
  - Hash_nt1=5
  - Hash_nt2=0
  - Hash_parallel_workers=0
  - Hash_plan_width=4
  - Hash_reltuples=0.0000
  - Hash_sel=1.0000
  - Hash_startup_cost=2.4000
  - Hash_total_cost=2.4000
  - SeqScan_Outer_np=1
  - SeqScan_Outer_nt=1
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=4
  - SeqScan_Outer_reltuples=5.0000
  - SeqScan_Outer_sel=0.2000
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=1.0600
- **Output:** st=0.19, rt=0.20

### Step 3: Node 13887 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=590
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0029
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=0.42, rt=44.47

### Step 4: Node 13874 (Nested Loop) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** bd9dfa7b (Nested Loop -> [Hash Join -> [Seq Scan (Outer), Hash -> Hash Join (Outer) (Inner)] (Outer), Index Scan (Inner)])
- **Consumes:** Nodes 13868, 13869, 13870, 13871, 13872, 13875, 13876, 13877, 13878, 13880, 13881, 13882, 13883, 13884, 13885, 13889
- **Input Features:**
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=12500
  - HashJoin_Outer_nt1=62500
  - HashJoin_Outer_nt2=5
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=4
  - HashJoin_Outer_reltuples=0.0000
  - HashJoin_Outer_sel=0.0400
  - HashJoin_Outer_startup_cost=2.4600
  - HashJoin_Outer_total_cost=4586.8400
  - Hash_Inner_np=0
  - Hash_Inner_nt=12500
  - Hash_Inner_nt1=12500
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=4
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=4586.8400
  - Hash_Inner_total_cost=4586.8400
  - IndexScan_Inner_np=112600
  - IndexScan_Inner_nt=5
  - IndexScan_Inner_nt1=0
  - IndexScan_Inner_nt2=0
  - IndexScan_Inner_parallel_workers=0
  - IndexScan_Inner_plan_width=24
  - IndexScan_Inner_reltuples=6001215.0000
  - IndexScan_Inner_sel=0.0000
  - IndexScan_Inner_startup_cost=0.4300
  - IndexScan_Inner_total_cost=0.8300
  - NestedLoop_np=0
  - NestedLoop_nt=118013
  - NestedLoop_nt1=29497
  - NestedLoop_nt2=5
  - NestedLoop_parallel_workers=0
  - NestedLoop_plan_width=24
  - NestedLoop_reltuples=0.0000
  - NestedLoop_sel=0.8002
  - NestedLoop_startup_cost=4743.5200
  - NestedLoop_total_cost=64785.2000
  - SeqScan_Outer_np=26136
  - SeqScan_Outer_nt=147487
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=12
  - SeqScan_Outer_reltuples=1500000.0000
  - SeqScan_Outer_sel=0.0983
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=33394.0600
- **Output:** st=37.64, rt=1155.06

### Step 5: Node 13886 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=590
  - nt1=590
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=44.4702
  - rt2=0.0000
  - sel=1.0000
  - st1=0.4239
  - st2=0.0000
  - startup_cost=5169.6700
  - total_cost=5169.6700
- **Output:** st=17.76, rt=17.76

### Step 6: Node 13873 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=836
  - nt1=118013
  - nt2=590
  - parallel_workers=0
  - plan_width=20
  - reltuples=0.0000
  - rt1=1155.0575
  - rt2=17.7639
  - sel=0.0000
  - st1=37.6418
  - st2=17.7644
  - startup_cost=9920.5600
  - total_cost=70272.0400
- **Output:** st=78.66, rt=1042.87

### Step 7: Node 13888 (Index Scan) - LEAF

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
- **Output:** st=0.01, rt=0.05

### Step 8: Node 13890 (Seq Scan) - LEAF

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

### Step 9: Node 13868 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 53f9aa07 (Aggregate -> Gather Merge -> Sort -> Hash Join -> [Nested Loop (Outer), Hash (Inner)] (Outer) (Outer) (Outer))
- **Consumes:** Nodes 13869, 13870, 13871, 13872, 13874, 13875, 13876, 13877, 13878, 13880, 13881, 13882, 13883, 13884, 13885, 13889
- **Input Features:**
  - Aggregate_np=0
  - Aggregate_nt=2406
  - Aggregate_nt1=2592
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=64
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.9282
  - Aggregate_startup_cost=71571.8000
  - Aggregate_total_cost=71978.4100
  - GatherMerge_Outer_np=0
  - GatherMerge_Outer_nt=2592
  - GatherMerge_Outer_nt1=836
  - GatherMerge_Outer_nt2=0
  - GatherMerge_Outer_parallel_workers=3
  - GatherMerge_Outer_plan_width=148
  - GatherMerge_Outer_reltuples=0.0000
  - GatherMerge_Outer_sel=3.1005
  - GatherMerge_Outer_startup_cost=71571.8000
  - GatherMerge_Outer_total_cost=71878.4500
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=836
  - HashJoin_Outer_nt1=836
  - HashJoin_Outer_nt2=25
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=148
  - HashJoin_Outer_reltuples=0.0000
  - HashJoin_Outer_sel=0.0400
  - HashJoin_Outer_startup_cost=9922.4100
  - HashJoin_Outer_total_cost=70531.1800
  - Hash_Inner_np=0
  - Hash_Inner_nt=25
  - Hash_Inner_nt1=25
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=108
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=1.2500
  - Hash_Inner_total_cost=1.2500
  - NestedLoop_Outer_np=0
  - NestedLoop_Outer_nt=836
  - NestedLoop_Outer_nt1=836
  - NestedLoop_Outer_nt2=1
  - NestedLoop_Outer_parallel_workers=0
  - NestedLoop_Outer_plan_width=20
  - NestedLoop_Outer_reltuples=0.0000
  - NestedLoop_Outer_sel=1.0000
  - NestedLoop_Outer_startup_cost=9920.8500
  - NestedLoop_Outer_total_cost=70524.9700
  - Sort_Outer_np=0
  - Sort_Outer_nt=836
  - Sort_Outer_nt1=836
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=148
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=70571.7600
  - Sort_Outer_total_cost=70573.8500
- **Output:** st=1219.05, rt=1220.42
