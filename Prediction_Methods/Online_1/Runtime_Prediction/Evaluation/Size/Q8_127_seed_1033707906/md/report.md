# Online Prediction Report

**Test Query:** Q8_127_seed_1033707906
**Timestamp:** 2026-01-01 18:34:13

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
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 33781.0% | 113504.2307 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 172 | 3565.0% | 6131.8766 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 75.1% | 108.1438 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 140 | 4.5% | 6.2375 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 96 | 7.6% | 7.3257 |
| 3e2d5a00 | Sort -> Hash Join (Outer) | 2 | 96 | 19.3% | 18.5586 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 168 | 44967.0% | 75544.5822 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 148 | 116.8% | 172.9284 |
| c0a8d3de | Hash -> Hash Join -> [Seq Scan (Outer), ... | 3 | 148 | 4130.8% | 6113.5159 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 116 | 3.5% | 4.0772 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 96 | 4.7% | 4.4662 |
| 91d6e559 | Sort -> Hash Join -> [Nested Loop (Outer... | 3 | 72 | 5.4% | 3.8546 |
| 2422d111 | Hash Join -> [Nested Loop -> [Hash Join ... | 3 | 72 | 15.0% | 10.7757 |
| 98d4ff98 | Gather Merge -> Sort -> Hash Join (Outer... | 3 | 48 | 6.2% | 2.9727 |
| f62279eb | Nested Loop -> [Hash Join -> [Nested Loo... | 3 | 24 | 9.0% | 2.1603 |
| 37515ad8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 124 | 135.7% | 168.3286 |
| a54055ce | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 96 | 6342.9% | 6089.1983 |
| bd9dfa7b | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 92 | 3.7% | 3.3601 |
| 444761fb | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 52 | 46.8% | 24.3176 |
| b149ff28 | Aggregate -> Gather Merge -> Sort -> Has... | 4 | 48 | 2.2% | 1.0579 |
| 3c6d8006 | Gather Merge -> Sort -> Hash Join -> [Ne... | 4 | 48 | 6.2% | 2.9727 |
| 12e6457c | Sort -> Hash Join -> [Nested Loop -> [Ha... | 4 | 48 | 6.0% | 2.9009 |
| 4db07220 | Hash Join -> [Nested Loop -> [Hash Join ... | 4 | 48 | 12.3% | 5.9049 |
| c5dad784 | Hash Join -> [Nested Loop -> [Hash Join ... | 4 | 24 | 20.3% | 4.8707 |
| c5a9eefd | Nested Loop -> [Hash Join -> [Nested Loo... | 4 | 24 | 9.0% | 2.1603 |
| 9d0e407c | Nested Loop -> [Hash Join -> [Seq Scan (... | 5 | 72 | 4.1% | 2.9587 |
| 545b5e57 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 72 | 212.7% | 153.1732 |
| ec92bdaa | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 52 | 29.1% | 15.1555 |
| 53f9aa07 | Aggregate -> Gather Merge -> Sort -> Has... | 5 | 48 | 2.2% | 1.0579 |
| 440e6274 | Hash Join -> [Nested Loop -> [Hash Join ... | 5 | 48 | 12.3% | 5.9049 |
| 314469b0 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 5 | 48 | 43.2% | 20.7410 |
| db6a761f | Gather Merge -> Sort -> Hash Join -> [Ne... | 5 | 24 | 7.9% | 1.8886 |
| 58ed95a8 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 5 | 24 | 10.2% | 2.4503 |
| 6981af52 | Hash Join -> [Nested Loop -> [Hash Join ... | 5 | 24 | 20.3% | 4.8707 |
| 9b49df80 | Nested Loop -> [Hash Join -> [Nested Loo... | 5 | 24 | 9.0% | 2.1603 |
| f4603221 | Hash Join -> [Nested Loop -> [Hash Join ... | 6 | 48 | 12.3% | 5.9049 |
| 5bfce159 | Nested Loop -> [Hash Join -> [Seq Scan (... | 6 | 48 | 4.4% | 2.1340 |
| e1d7e5b4 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 48 | 27.6% | 13.2381 |
| 54cb7f90 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 6 | 48 | 43.2% | 20.7410 |
| c9736a93 | Aggregate -> Gather Merge -> Sort -> Has... | 6 | 24 | 3.2% | 0.7651 |
| 839648da | Gather Merge -> Sort -> Hash Join -> [Ne... | 6 | 24 | 7.9% | 1.8886 |
| be705a2d | Sort -> Hash Join -> [Nested Loop -> [Ha... | 6 | 24 | 10.2% | 2.4503 |
| b88a3db4 | Hash Join -> [Nested Loop -> [Hash Join ... | 6 | 24 | 20.3% | 4.8707 |
| 45158dca | Nested Loop -> [Hash Join -> [Nested Loo... | 6 | 24 | 9.0% | 2.1603 |
| 3d4c3db9 | Hash Join -> [Nested Loop -> [Hash Join ... | 7 | 48 | 12.3% | 5.9049 |
| ef93d4fc | Nested Loop -> [Hash Join -> [Seq Scan (... | 7 | 48 | 4.4% | 2.1340 |
| c302739b | Hash Join -> [Seq Scan (Outer), Hash -> ... | 7 | 48 | 27.6% | 13.2381 |
| 59f6581f | Aggregate -> Gather Merge -> Sort -> Has... | 7 | 24 | 3.2% | 0.7651 |
| d8d77761 | Gather Merge -> Sort -> Hash Join -> [Ne... | 7 | 24 | 7.9% | 1.8886 |
| 5d01b240 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 7 | 24 | 10.2% | 2.4503 |
| 800ffecc | Hash Join -> [Nested Loop -> [Hash Join ... | 7 | 24 | 20.3% | 4.8707 |
| 473ac852 | Nested Loop -> [Hash Join -> [Nested Loo... | 7 | 24 | 9.0% | 2.1603 |
| 9ce781b0 | Hash Join -> [Nested Loop -> [Hash Join ... | 8 | 48 | 12.3% | 5.9049 |
| 5ae97df8 | Nested Loop -> [Hash Join -> [Seq Scan (... | 8 | 48 | 4.4% | 2.1340 |
| 7f3b31ff | Aggregate -> Gather Merge -> Sort -> Has... | 8 | 24 | 3.2% | 0.7651 |
| ef63c60f | Gather Merge -> Sort -> Hash Join -> [Ne... | 8 | 24 | 7.9% | 1.8886 |
| c7b8fb6d | Sort -> Hash Join -> [Nested Loop -> [Ha... | 8 | 24 | 10.2% | 2.4503 |
| 9d50c2fc | Hash Join -> [Nested Loop -> [Hash Join ... | 8 | 24 | 20.3% | 4.8707 |
| 959de0c2 | Nested Loop -> [Hash Join -> [Nested Loo... | 8 | 24 | 9.0% | 2.1603 |
| a95bee4e | Hash Join -> [Nested Loop -> [Hash Join ... | 9 | 48 | 12.3% | 5.9049 |
| cb7eed03 | Aggregate -> Gather Merge -> Sort -> Has... | 9 | 24 | 3.2% | 0.7651 |
| 82a8bdb2 | Gather Merge -> Sort -> Hash Join -> [Ne... | 9 | 24 | 7.9% | 1.8886 |
| 1d069442 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 9 | 24 | 10.2% | 2.4503 |
| cee0b988 | Hash Join -> [Nested Loop -> [Hash Join ... | 9 | 24 | 20.3% | 4.8707 |
| bf197fca | Nested Loop -> [Hash Join -> [Nested Loo... | 9 | 24 | 9.0% | 2.1603 |
| b659e5bf | Aggregate -> Gather Merge -> Sort -> Has... | 10 | 24 | 3.2% | 0.7651 |
| e31c99cb | Gather Merge -> Sort -> Hash Join -> [Ne... | 10 | 24 | 7.9% | 1.8886 |
| d00b75d6 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 10 | 24 | 10.2% | 2.4503 |
| 910f6702 | Hash Join -> [Nested Loop -> [Hash Join ... | 10 | 24 | 20.3% | 4.8707 |
| 19fc9abd | Nested Loop -> [Hash Join -> [Nested Loo... | 10 | 24 | 9.0% | 2.1603 |
| 96f339c9 | Aggregate -> Gather Merge -> Sort -> Has... | 11 | 24 | 3.2% | 0.7651 |
| 50ace808 | Gather Merge -> Sort -> Hash Join -> [Ne... | 11 | 24 | 7.9% | 1.8886 |
| 06857491 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 11 | 24 | 10.2% | 2.4503 |
| fb7bcc0c | Hash Join -> [Nested Loop -> [Hash Join ... | 11 | 24 | 20.3% | 4.8707 |
| 9b77a70e | Aggregate -> Gather Merge -> Sort -> Has... | 12 | 24 | 3.2% | 0.7651 |
| 860d9d3a | Gather Merge -> Sort -> Hash Join -> [Ne... | 12 | 24 | 7.9% | 1.8886 |
| 8febc667 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 12 | 24 | 10.2% | 2.4503 |
| 264d1e57 | Aggregate -> Gather Merge -> Sort -> Has... | 13 | 24 | 3.2% | 0.7651 |
| ffc3be98 | Gather Merge -> Sort -> Hash Join -> [Ne... | 13 | 24 | 7.9% | 1.8886 |
| acd22c74 | Aggregate -> Gather Merge -> Sort -> Has... | 14 | 24 | 3.2% | 0.7651 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 75736.1626 | 0.0004% | ACCEPTED | 17.92% |
| 1 | 3aab37be | 94712.4752 | -0.0000% | REJECTED | 17.92% |
| 2 | 7df893ad | 678.6757 | N/A | REJECTED | 17.92% |
| 3 | 2724c080 | 19.6008 | 0.0222% | ACCEPTED | 17.90% |
| 4 | 2e0f44ef | 108.1433 | -0.0000% | REJECTED | 17.90% |
| 5 | 3cfa90d7 | 6.2269 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 6 | 3e2d5a00 | 18.5791 | N/A | REJECTED | 17.90% |
| 7 | f4cb205a | 41652.9228 | 0.0005% | ACCEPTED | 17.90% |
| 8 | bb930825 | 188.3060 | -0.0000% | REJECTED | 17.90% |
| 9 | c0a8d3de | 540.8859 | 0.0000% | ACCEPTED | 17.90% |
| 10 | e0e3c3e1 | 4.0887 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 11 | 29ee00db | 4.4857 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 12 | 91d6e559 | 3.8554 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 13 | 2422d111 | 10.7754 | N/A | REJECTED | 17.90% |
| 14 | f62279eb | 2.1603 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 15 | 37515ad8 | 38.5998 | -0.0000% | REJECTED | 17.90% |
| 16 | a54055ce | 350.8449 | N/A | REJECTED | 17.90% |
| 17 | bd9dfa7b | 3.3586 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 18 | 444761fb | 6.7516 | 0.0000% | ACCEPTED | 17.90% |
| 19 | b149ff28 | 1.5277 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 20 | 12e6457c | 2.9009 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 21 | 4db07220 | 5.9046 | N/A | REJECTED | 17.90% |
| 22 | c5dad784 | 4.8707 | N/A | REJECTED | 17.90% |
| 23 | c5a9eefd | 2.1603 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 24 | 9d0e407c | 2.9678 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 25 | 545b5e57 | 25.3429 | N/A | REJECTED | 17.90% |
| 26 | ec92bdaa | 15.2124 | -0.0000% | REJECTED | 17.90% |
| 27 | 53f9aa07 | 1.5277 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 28 | 440e6274 | 5.9046 | N/A | REJECTED | 17.90% |
| 29 | 314469b0 | 2.9309 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 30 | 58ed95a8 | 2.4503 | N/A | REJECTED | 17.90% |
| 31 | 6981af52 | 4.8707 | N/A | REJECTED | 17.90% |
| 32 | 9b49df80 | 2.1603 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 33 | f4603221 | 5.9046 | N/A | REJECTED | 17.90% |
| 34 | 5bfce159 | 2.1340 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 35 | e1d7e5b4 | 13.2915 | N/A | REJECTED | 17.90% |
| 36 | 54cb7f90 | 2.9309 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 37 | c9736a93 | 1.0519 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 38 | be705a2d | 2.4503 | N/A | REJECTED | 17.90% |
| 39 | b88a3db4 | 4.8707 | N/A | REJECTED | 17.90% |
| 40 | 45158dca | 2.1603 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 41 | 3d4c3db9 | 5.9046 | N/A | REJECTED | 17.90% |
| 42 | ef93d4fc | 2.1340 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 43 | c302739b | 13.2915 | N/A | REJECTED | 17.90% |
| 44 | 59f6581f | 1.0519 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 45 | 5d01b240 | 2.4503 | N/A | REJECTED | 17.90% |
| 46 | 800ffecc | 4.8707 | N/A | REJECTED | 17.90% |
| 47 | 473ac852 | 2.1603 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 48 | 9ce781b0 | 5.9046 | N/A | REJECTED | 17.90% |
| 49 | 5ae97df8 | 2.1340 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 50 | 7f3b31ff | 1.0519 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 51 | c7b8fb6d | 2.4503 | N/A | REJECTED | 17.90% |
| 52 | 9d50c2fc | 4.8707 | N/A | REJECTED | 17.90% |
| 53 | 959de0c2 | 2.1603 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 54 | a95bee4e | 5.9046 | N/A | REJECTED | 17.90% |
| 55 | cb7eed03 | 1.0519 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 56 | 1d069442 | 2.4503 | N/A | REJECTED | 17.90% |
| 57 | cee0b988 | 4.8707 | N/A | REJECTED | 17.90% |
| 58 | bf197fca | 2.1603 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 59 | b659e5bf | 1.0519 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 60 | d00b75d6 | 2.4503 | N/A | REJECTED | 17.90% |
| 61 | 910f6702 | 4.8707 | N/A | REJECTED | 17.90% |
| 62 | 19fc9abd | 2.1603 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 63 | 96f339c9 | 1.0519 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 64 | 06857491 | 2.4503 | N/A | REJECTED | 17.90% |
| 65 | fb7bcc0c | 4.8707 | N/A | REJECTED | 17.90% |
| 66 | 9b77a70e | 1.0519 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 67 | 8febc667 | 2.4503 | N/A | REJECTED | 17.90% |
| 68 | 264d1e57 | 1.0519 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 69 | acd22c74 | 1.0519 | N/A | SKIPPED_LOW_ERROR | 17.90% |
## Query Tree

```
Node 13868 (Aggregate) [PATTERN: 2724c080] - ROOT
  Node 13869 (Gather Merge) [consumed]
    Node 13870 (Sort)
      Node 13871 (Hash Join)
        Node 13872 (Nested Loop)
          Node 13873 (Hash Join)
            Node 13874 (Nested Loop)
              Node 13875 (Hash Join)
                Node 13876 (Seq Scan) - LEAF
                Node 13877 (Hash) [PATTERN: 444761fb]
                  Node 13878 (Hash Join) [consumed]
                    Node 13879 (Seq Scan) [consumed] - LEAF
                    Node 13880 (Hash) [consumed]
                      Node 13881 (Hash Join) [consumed]
                        Node 13882 (Seq Scan) - LEAF
                        Node 13883 (Hash)
                          Node 13884 (Seq Scan) - LEAF
              Node 13885 (Index Scan) - LEAF
            Node 13886 (Hash)
              Node 13887 (Seq Scan) - LEAF
          Node 13888 (Index Scan) - LEAF
        Node 13889 (Hash)
          Node 13890 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Hash -> Hash Join -> [Seq Scan | 444761fb | 13877 | 13868, 13869, 13878, 13879, 13880, 13881 |
| Aggregate -> Gather Merge (Out | 2724c080 | 13868 | 13869, 13877, 13878, 13879, 13880, 13881 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 4.04%
- Improvement: -0.19%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 13868 | Aggregate | 1219.25 | 1169.94 | 4.0% | pattern |
| 13870 | Sort | 1213.65 | 1087.88 | 10.4% | operator |
| 13871 | Hash Join | 1213.40 | 1055.49 | 13.0% | operator |
| 13872 | Nested Loop | 1213.08 | 1105.67 | 8.9% | operator |
| 13889 | Hash | 0.01 | 14.54 | 111744.0% | operator |
| 13873 | Hash Join | 1209.13 | 1027.33 | 15.0% | operator |
| 13888 | Index Scan | 0.01 | 0.05 | 753.5% | operator |
| 13890 | Seq Scan | 0.01 | 7.19 | 71844.7% | operator |
| 13874 | Nested Loop | 1161.85 | 1119.20 | 3.7% | operator |
| 13886 | Hash | 42.78 | 17.76 | 58.5% | operator |
| 13875 | Hash Join | 215.80 | 226.59 | 5.0% | operator |
| 13885 | Index Scan | 0.04 | 0.09 | 112.3% | operator |
| 13887 | Seq Scan | 42.72 | 44.47 | 4.1% | operator |
| 13876 | Seq Scan | 158.89 | 161.81 | 1.8% | operator |
| 13877 | Hash | 37.38 | 36.08 | 3.5% | pattern |
| 13882 | Seq Scan | 0.01 | 9.26 | 84087.6% | operator |
| 13883 | Hash | 0.22 | 16.01 | 7246.3% | operator |
| 13884 | Seq Scan | 0.21 | 21.39 | 9942.2% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 13884 (Seq Scan) - LEAF

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
- **Output:** st=0.12, rt=21.39

### Step 2: Node 13882 (Seq Scan) - LEAF

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
- **Output:** st=0.06, rt=9.26

### Step 3: Node 13883 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=1
  - nt1=1
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=21.3899
  - rt2=0.0000
  - sel=1.0000
  - st1=0.1185
  - st2=0.0000
  - startup_cost=1.0600
  - total_cost=1.0600
- **Output:** st=16.02, rt=16.01

### Step 4: Node 13876 (Seq Scan) - LEAF

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
- **Output:** st=0.26, rt=161.81

### Step 5: Node 13877 (Hash) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 444761fb (Hash -> Hash Join -> [Seq Scan (Outer), Hash -> Hash Join (Outer) (Inner)] (Outer))
- **Consumes:** Nodes 13868, 13869, 13878, 13879, 13880, 13881
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
- **Output:** st=36.08, rt=36.08

### Step 6: Node 13875 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=29497
  - nt1=147487
  - nt2=12500
  - parallel_workers=0
  - plan_width=8
  - reltuples=0.0000
  - rt1=161.8115
  - rt2=36.0810
  - sel=0.0000
  - st1=0.2615
  - st2=36.0800
  - startup_cost=4743.0900
  - total_cost=38813.1400
- **Output:** st=27.94, rt=226.59

### Step 7: Node 13885 (Index Scan) - LEAF

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
- **Output:** st=0.04, rt=0.09

### Step 8: Node 13887 (Seq Scan) - LEAF

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

### Step 9: Node 13874 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=118013
  - nt1=29497
  - nt2=5
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=226.5947
  - rt2=0.0870
  - sel=0.8002
  - st1=27.9426
  - st2=0.0386
  - startup_cost=4743.5200
  - total_cost=64785.2000
- **Output:** st=37.24, rt=1119.20

### Step 10: Node 13886 (Hash)

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

### Step 11: Node 13873 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=836
  - nt1=118013
  - nt2=590
  - parallel_workers=0
  - plan_width=20
  - reltuples=0.0000
  - rt1=1119.2033
  - rt2=17.7639
  - sel=0.0000
  - st1=37.2434
  - st2=17.7644
  - startup_cost=9920.5600
  - total_cost=70272.0400
- **Output:** st=77.17, rt=1027.33

### Step 12: Node 13888 (Index Scan) - LEAF

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

### Step 13: Node 13890 (Seq Scan) - LEAF

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

### Step 14: Node 13872 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=836
  - nt1=836
  - nt2=1
  - parallel_workers=0
  - plan_width=20
  - reltuples=0.0000
  - rt1=1027.3305
  - rt2=0.0512
  - sel=1.0000
  - st1=77.1685
  - st2=0.0060
  - startup_cost=9920.8500
  - total_cost=70524.9700
- **Output:** st=27.01, rt=1105.67

### Step 15: Node 13889 (Hash)

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

### Step 16: Node 13871 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=836
  - nt1=836
  - nt2=25
  - parallel_workers=0
  - plan_width=148
  - reltuples=0.0000
  - rt1=1105.6666
  - rt2=14.5397
  - sel=0.0400
  - st1=27.0053
  - st2=14.5393
  - startup_cost=9922.4100
  - total_cost=70531.1800
- **Output:** st=35.78, rt=1055.49

### Step 17: Node 13870 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=836
  - nt1=836
  - nt2=0
  - parallel_workers=0
  - plan_width=148
  - reltuples=0.0000
  - rt1=1055.4897
  - rt2=0.0000
  - sel=1.0000
  - st1=35.7849
  - st2=0.0000
  - startup_cost=70571.7600
  - total_cost=70573.8500
- **Output:** st=1086.93, rt=1087.88

### Step 18: Node 13868 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 2724c080 (Aggregate -> Gather Merge (Outer))
- **Consumes:** Nodes 13869, 13877, 13878, 13879, 13880, 13881
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
- **Output:** st=1167.47, rt=1169.94
