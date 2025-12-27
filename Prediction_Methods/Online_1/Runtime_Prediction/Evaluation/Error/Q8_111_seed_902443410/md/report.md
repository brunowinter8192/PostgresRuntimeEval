# Online Prediction Report

**Test Query:** Q8_111_seed_902443410
**Timestamp:** 2025-12-22 03:47:35

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 4.64%

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
| 1 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 2 | f4cb205a | 75544.5822 | 0.0006% | REJECTED | 17.92% |
| 3 | 7df893ad | 6131.8766 | -0.0000% | REJECTED | 17.92% |
| 4 | c0a8d3de | 6113.5159 | -0.0000% | REJECTED | 17.92% |
| 5 | a54055ce | 6089.1983 | -0.0000% | REJECTED | 17.92% |
| 6 | bb930825 | 172.9284 | -0.0000% | REJECTED | 17.92% |
| 7 | 37515ad8 | 168.3286 | -0.0000% | REJECTED | 17.92% |
| 8 | 545b5e57 | 153.1732 | -0.0000% | REJECTED | 17.92% |
| 9 | 2e0f44ef | 108.1438 | 0.0001% | REJECTED | 17.92% |
| 10 | 444761fb | 24.3176 | -0.0000% | REJECTED | 17.92% |
| 11 | 314469b0 | 20.7410 | 0.0000% | REJECTED | 17.92% |
| 12 | 54cb7f90 | 20.7410 | 0.0000% | REJECTED | 17.92% |
| 13 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 14 | 3e2d5a00 | 18.5586 | 0.0007% | REJECTED | 17.92% |
| 15 | ec92bdaa | 15.1555 | -0.0000% | REJECTED | 17.92% |
| 16 | c302739b | 13.2381 | -0.0000% | REJECTED | 17.92% |
| 17 | e1d7e5b4 | 13.2381 | -0.0000% | REJECTED | 17.92% |
| 18 | 2422d111 | 10.7757 | 0.0001% | REJECTED | 17.92% |
| 19 | 1691f6f0 | 7.3257 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 20 | 3cfa90d7 | 6.2375 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 21 | 3d4c3db9 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 22 | 440e6274 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 23 | 4db07220 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 24 | 9ce781b0 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 25 | a95bee4e | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 26 | f4603221 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 27 | 6981af52 | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 28 | 800ffecc | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 29 | 910f6702 | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 30 | 9d50c2fc | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 31 | b88a3db4 | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 32 | c5dad784 | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 33 | cee0b988 | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 34 | fb7bcc0c | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 35 | 29ee00db | 4.4662 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 36 | e0e3c3e1 | 4.0772 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 37 | 91d6e559 | 3.8546 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 38 | bd9dfa7b | 3.3601 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 39 | 3c6d8006 | 2.9727 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 40 | 98d4ff98 | 2.9727 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 41 | 9d0e407c | 2.9587 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 42 | 12e6457c | 2.9009 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 43 | 06857491 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 44 | 1d069442 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 45 | 58ed95a8 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 46 | 5d01b240 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 47 | 8febc667 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 48 | be705a2d | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 49 | c7b8fb6d | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 50 | d00b75d6 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 51 | 19fc9abd | 2.1603 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 52 | 45158dca | 2.1603 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 53 | 473ac852 | 2.1603 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 54 | 959de0c2 | 2.1603 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 55 | 9b49df80 | 2.1603 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 56 | bf197fca | 2.1603 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 57 | c5a9eefd | 2.1603 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 58 | f62279eb | 2.1603 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 59 | 5ae97df8 | 2.1340 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 60 | 5bfce159 | 2.1340 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 61 | ef93d4fc | 2.1340 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 62 | 50ace808 | 1.8886 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 63 | 82a8bdb2 | 1.8886 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 64 | 839648da | 1.8886 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 65 | 860d9d3a | 1.8886 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 66 | d8d77761 | 1.8886 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 67 | db6a761f | 1.8886 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 68 | e31c99cb | 1.8886 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 69 | ef63c60f | 1.8886 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 70 | ffc3be98 | 1.8886 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 71 | 53f9aa07 | 1.0579 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 72 | b149ff28 | 1.0579 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 73 | 264d1e57 | 0.7651 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 74 | 59f6581f | 0.7651 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 75 | 7f3b31ff | 0.7651 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 76 | 96f339c9 | 0.7651 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 77 | 9b77a70e | 0.7651 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 78 | acd22c74 | 0.7651 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 79 | b659e5bf | 0.7651 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 80 | c9736a93 | 0.7651 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 81 | cb7eed03 | 0.7651 | N/A | SKIPPED_LOW_ERROR | 17.92% |
## Query Tree

```
Node 13477 (Aggregate) - ROOT
  Node 13478 (Gather Merge)
    Node 13479 (Sort)
      Node 13480 (Hash Join)
        Node 13481 (Nested Loop)
          Node 13482 (Hash Join)
            Node 13483 (Nested Loop)
              Node 13484 (Hash Join)
                Node 13485 (Seq Scan) - LEAF
                Node 13486 (Hash)
                  Node 13487 (Hash Join)
                    Node 13488 (Seq Scan) - LEAF
                    Node 13489 (Hash)
                      Node 13490 (Hash Join)
                        Node 13491 (Seq Scan) - LEAF
                        Node 13492 (Hash)
                          Node 13493 (Seq Scan) - LEAF
              Node 13494 (Index Scan) - LEAF
            Node 13495 (Hash)
              Node 13496 (Seq Scan) - LEAF
          Node 13497 (Index Scan) - LEAF
        Node 13498 (Hash)
          Node 13499 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 3.87%
- Improvement: 0.78%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 13477 | Aggregate | 1241.46 | 1193.46 | 3.9% | operator |
| 13478 | Gather Merge | 1240.96 | 1123.89 | 9.4% | operator |
| 13479 | Sort | 1235.17 | 1087.88 | 11.9% | operator |
| 13480 | Hash Join | 1234.88 | 1055.47 | 14.5% | operator |
| 13481 | Nested Loop | 1234.56 | 1105.66 | 10.4% | operator |
| 13498 | Hash | 0.02 | 14.54 | 90773.2% | operator |
| 13482 | Hash Join | 1229.76 | 1027.31 | 16.5% | operator |
| 13497 | Index Scan | 0.01 | 0.05 | 631.6% | operator |
| 13499 | Seq Scan | 0.01 | 7.19 | 59854.0% | operator |
| 13483 | Nested Loop | 1185.22 | 1119.20 | 5.6% | operator |
| 13495 | Hash | 39.74 | 17.76 | 55.3% | operator |
| 13484 | Hash Join | 213.78 | 226.27 | 5.8% | operator |
| 13494 | Index Scan | 0.04 | 0.09 | 107.2% | operator |
| 13496 | Seq Scan | 39.50 | 44.48 | 12.6% | operator |
| 13485 | Seq Scan | 158.82 | 161.81 | 1.9% | operator |
| 13486 | Hash | 36.05 | 18.06 | 49.9% | operator |
| 13487 | Hash Join | 34.38 | 67.97 | 97.7% | operator |
| 13488 | Seq Scan | 33.04 | 24.87 | 24.7% | operator |
| 13489 | Hash | 0.09 | 17.93 | 19177.2% | operator |
| 13490 | Hash Join | 0.09 | 151.58 | 168326.0% | operator |
| 13491 | Seq Scan | 0.01 | 9.26 | 115657.9% | operator |
| 13492 | Hash | 0.08 | 16.01 | 20972.3% | operator |
| 13493 | Seq Scan | 0.07 | 21.39 | 29201.3% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 13493 (Seq Scan) - LEAF

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

### Step 2: Node 13491 (Seq Scan) - LEAF

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

### Step 3: Node 13492 (Hash)

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

### Step 4: Node 13490 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=25
  - nt2=1
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=9.2606
  - rt2=16.0149
  - sel=0.2000
  - st1=0.0596
  - st2=16.0154
  - startup_cost=1.0700
  - total_cost=2.4000
- **Output:** st=1.98, rt=151.58

### Step 5: Node 13488 (Seq Scan) - LEAF

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

### Step 6: Node 13489 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=5
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=151.5834
  - rt2=0.0000
  - sel=1.0000
  - st1=1.9819
  - st2=0.0000
  - startup_cost=2.4000
  - total_cost=2.4000
- **Output:** st=17.93, rt=17.93

### Step 7: Node 13487 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=12500
  - nt1=62500
  - nt2=5
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=24.8735
  - rt2=17.9278
  - sel=0.0400
  - st1=0.2761
  - st2=17.9282
  - startup_cost=2.4600
  - total_cost=4586.8400
- **Output:** st=2.26, rt=67.97

### Step 8: Node 13485 (Seq Scan) - LEAF

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

### Step 9: Node 13486 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=12500
  - nt1=12500
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=67.9686
  - rt2=0.0000
  - sel=1.0000
  - st1=2.2615
  - st2=0.0000
  - startup_cost=4586.8400
  - total_cost=4586.8400
- **Output:** st=18.06, rt=18.06

### Step 10: Node 13484 (Hash Join)

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
  - rt2=18.0614
  - sel=0.0000
  - st1=0.2615
  - st2=18.0617
  - startup_cost=4743.0900
  - total_cost=38813.1400
- **Output:** st=27.70, rt=226.27

### Step 11: Node 13494 (Index Scan) - LEAF

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

### Step 12: Node 13496 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=556
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0028
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=0.42, rt=44.48

### Step 13: Node 13483 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=118013
  - nt1=29497
  - nt2=5
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=226.2726
  - rt2=0.0870
  - sel=0.8002
  - st1=27.7005
  - st2=0.0386
  - startup_cost=4743.5200
  - total_cost=64785.2000
- **Output:** st=37.24, rt=1119.20

### Step 14: Node 13495 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=556
  - nt1=556
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=44.4841
  - rt2=0.0000
  - sel=1.0000
  - st1=0.4240
  - st2=0.0000
  - startup_cost=5169.6700
  - total_cost=5169.6700
- **Output:** st=17.76, rt=17.76

### Step 15: Node 13482 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=788
  - nt1=118013
  - nt2=556
  - parallel_workers=0
  - plan_width=20
  - reltuples=0.0000
  - rt1=1119.1991
  - rt2=17.7643
  - sel=0.0000
  - st1=37.2387
  - st2=17.7648
  - startup_cost=9920.1400
  - total_cost=70271.6200
- **Output:** st=77.17, rt=1027.31

### Step 16: Node 13497 (Index Scan) - LEAF

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

### Step 17: Node 13499 (Seq Scan) - LEAF

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

### Step 18: Node 13481 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=788
  - nt1=788
  - nt2=1
  - parallel_workers=0
  - plan_width=20
  - reltuples=0.0000
  - rt1=1027.3121
  - rt2=0.0512
  - sel=1.0000
  - st1=77.1733
  - st2=0.0060
  - startup_cost=9920.4200
  - total_cost=70510.0200
- **Output:** st=27.01, rt=1105.66

### Step 19: Node 13498 (Hash)

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

### Step 20: Node 13480 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=788
  - nt1=788
  - nt2=25
  - parallel_workers=0
  - plan_width=148
  - reltuples=0.0000
  - rt1=1105.6554
  - rt2=14.5397
  - sel=0.0400
  - st1=27.0063
  - st2=14.5393
  - startup_cost=9921.9900
  - total_cost=70515.9800
- **Output:** st=35.78, rt=1055.47

### Step 21: Node 13479 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=788
  - nt1=788
  - nt2=0
  - parallel_workers=0
  - plan_width=148
  - reltuples=0.0000
  - rt1=1055.4733
  - rt2=0.0000
  - sel=1.0000
  - st1=35.7818
  - st2=0.0000
  - startup_cost=70553.8900
  - total_cost=70555.8600
- **Output:** st=1086.92, rt=1087.88

### Step 22: Node 13478 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2442
  - nt1=788
  - nt2=0
  - parallel_workers=3
  - plan_width=148
  - reltuples=0.0000
  - rt1=1087.8805
  - rt2=0.0000
  - sel=3.0990
  - st1=1086.9225
  - st2=0.0000
  - startup_cost=71553.9300
  - total_cost=71842.8400
- **Output:** st=1120.82, rt=1123.89

### Step 23: Node 13477 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2406
  - nt1=2442
  - nt2=0
  - parallel_workers=0
  - plan_width=64
  - reltuples=0.0000
  - rt1=1123.8943
  - rt2=0.0000
  - sel=0.9853
  - st1=1120.8162
  - st2=0.0000
  - startup_cost=71553.9300
  - total_cost=71939.8000
- **Output:** st=1186.19, rt=1193.46
