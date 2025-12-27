# Online Prediction Report

**Test Query:** Q8_94_seed_762974883
**Timestamp:** 2025-12-22 06:01:37

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 3.81%

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
| 0 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 1 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 2 | 7df893ad | 6131.8766 | -0.0000% | REJECTED | 17.92% |
| 3 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 4 | 2e0f44ef | 108.1438 | 0.0001% | REJECTED | 17.92% |
| 5 | 3cfa90d7 | 6.2375 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 6 | 1691f6f0 | 7.3257 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 7 | 3e2d5a00 | 18.5586 | 0.0007% | REJECTED | 17.92% |
| 8 | f4cb205a | 75544.5822 | 0.0006% | REJECTED | 17.92% |
| 9 | bb930825 | 172.9284 | -0.0000% | REJECTED | 17.92% |
| 10 | c0a8d3de | 6113.5159 | -0.0000% | REJECTED | 17.92% |
| 11 | e0e3c3e1 | 4.0772 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 12 | 29ee00db | 4.4662 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 13 | 91d6e559 | 3.8546 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 14 | 2422d111 | 10.7757 | 0.0001% | REJECTED | 17.92% |
| 15 | 98d4ff98 | 2.9727 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 16 | f62279eb | 2.1603 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 17 | 37515ad8 | 168.3286 | -0.0000% | REJECTED | 17.92% |
| 18 | a54055ce | 6089.1983 | -0.0000% | REJECTED | 17.92% |
| 19 | bd9dfa7b | 3.3601 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 20 | 444761fb | 24.3176 | -0.0000% | REJECTED | 17.92% |
| 21 | b149ff28 | 1.0579 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 22 | 3c6d8006 | 2.9727 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 23 | 12e6457c | 2.9009 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 24 | 4db07220 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 25 | c5dad784 | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 26 | c5a9eefd | 2.1603 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 27 | 9d0e407c | 2.9587 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 28 | 545b5e57 | 153.1732 | -0.0000% | REJECTED | 17.92% |
| 29 | ec92bdaa | 15.1555 | -0.0000% | REJECTED | 17.92% |
| 30 | 53f9aa07 | 1.0579 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 31 | 440e6274 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 32 | 314469b0 | 20.7410 | 0.0000% | REJECTED | 17.92% |
| 33 | db6a761f | 1.8886 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 34 | 58ed95a8 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 35 | 6981af52 | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 36 | 9b49df80 | 2.1603 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 37 | f4603221 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 38 | 5bfce159 | 2.1340 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 39 | e1d7e5b4 | 13.2381 | -0.0000% | REJECTED | 17.92% |
| 40 | 54cb7f90 | 20.7410 | 0.0000% | REJECTED | 17.92% |
| 41 | c9736a93 | 0.7651 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 42 | 839648da | 1.8886 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 43 | be705a2d | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 44 | b88a3db4 | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 45 | 45158dca | 2.1603 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 46 | 3d4c3db9 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 47 | ef93d4fc | 2.1340 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 48 | c302739b | 13.2381 | -0.0000% | REJECTED | 17.92% |
| 49 | 59f6581f | 0.7651 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 50 | d8d77761 | 1.8886 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 51 | 5d01b240 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 52 | 800ffecc | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 53 | 473ac852 | 2.1603 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 54 | 9ce781b0 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 55 | 5ae97df8 | 2.1340 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 56 | 7f3b31ff | 0.7651 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 57 | ef63c60f | 1.8886 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 58 | c7b8fb6d | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 59 | 9d50c2fc | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 60 | 959de0c2 | 2.1603 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 61 | a95bee4e | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 62 | cb7eed03 | 0.7651 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 63 | 82a8bdb2 | 1.8886 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 64 | 1d069442 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 65 | cee0b988 | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 66 | bf197fca | 2.1603 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 67 | b659e5bf | 0.7651 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 68 | e31c99cb | 1.8886 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 69 | d00b75d6 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 70 | 910f6702 | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 71 | 19fc9abd | 2.1603 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 72 | 96f339c9 | 0.7651 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 73 | 50ace808 | 1.8886 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 74 | 06857491 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 75 | fb7bcc0c | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 76 | 9b77a70e | 0.7651 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 77 | 860d9d3a | 1.8886 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 78 | 8febc667 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 79 | 264d1e57 | 0.7651 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 80 | ffc3be98 | 1.8886 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 81 | acd22c74 | 0.7651 | N/A | SKIPPED_LOW_ERROR | 17.92% |
## Query Tree

```
Node 16490 (Aggregate) - ROOT
  Node 16491 (Gather Merge)
    Node 16492 (Sort)
      Node 16493 (Hash Join)
        Node 16494 (Nested Loop)
          Node 16495 (Hash Join)
            Node 16496 (Nested Loop)
              Node 16497 (Hash Join)
                Node 16498 (Seq Scan) - LEAF
                Node 16499 (Hash)
                  Node 16500 (Hash Join)
                    Node 16501 (Seq Scan) - LEAF
                    Node 16502 (Hash)
                      Node 16503 (Hash Join)
                        Node 16504 (Seq Scan) - LEAF
                        Node 16505 (Hash)
                          Node 16506 (Seq Scan) - LEAF
              Node 16507 (Index Scan) - LEAF
            Node 16508 (Hash)
              Node 16509 (Seq Scan) - LEAF
          Node 16510 (Index Scan) - LEAF
        Node 16511 (Hash)
          Node 16512 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 3.00%
- Improvement: 0.80%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 16490 | Aggregate | 1233.58 | 1196.51 | 3.0% | operator |
| 16491 | Gather Merge | 1233.15 | 1123.89 | 8.9% | operator |
| 16492 | Sort | 1227.88 | 1087.88 | 11.4% | operator |
| 16493 | Hash Join | 1227.64 | 1055.46 | 14.0% | operator |
| 16494 | Nested Loop | 1227.33 | 1105.65 | 9.9% | operator |
| 16511 | Hash | 0.02 | 14.54 | 80676.2% | operator |
| 16495 | Hash Join | 1223.53 | 1027.31 | 16.0% | operator |
| 16510 | Index Scan | 0.01 | 0.05 | 753.5% | operator |
| 16512 | Seq Scan | 0.01 | 7.19 | 55242.1% | operator |
| 16496 | Nested Loop | 1178.38 | 1119.20 | 5.0% | operator |
| 16508 | Hash | 40.80 | 17.76 | 56.5% | operator |
| 16497 | Hash Join | 214.61 | 226.27 | 5.4% | operator |
| 16507 | Index Scan | 0.04 | 0.09 | 112.3% | operator |
| 16509 | Seq Scan | 40.74 | 44.49 | 9.2% | operator |
| 16498 | Seq Scan | 160.28 | 161.81 | 1.0% | operator |
| 16499 | Hash | 35.44 | 18.06 | 49.0% | operator |
| 16500 | Hash Join | 34.04 | 67.97 | 99.7% | operator |
| 16501 | Seq Scan | 32.63 | 24.87 | 23.8% | operator |
| 16502 | Hash | 0.09 | 17.93 | 20991.5% | operator |
| 16503 | Hash Join | 0.08 | 151.58 | 187040.0% | operator |
| 16504 | Seq Scan | 0.01 | 9.26 | 71135.6% | operator |
| 16505 | Hash | 0.06 | 16.01 | 26154.0% | operator |
| 16506 | Seq Scan | 0.06 | 21.39 | 37426.2% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 16506 (Seq Scan) - LEAF

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

### Step 2: Node 16504 (Seq Scan) - LEAF

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

### Step 3: Node 16505 (Hash)

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

### Step 4: Node 16503 (Hash Join)

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

### Step 5: Node 16501 (Seq Scan) - LEAF

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

### Step 6: Node 16502 (Hash)

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

### Step 7: Node 16500 (Hash Join)

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

### Step 8: Node 16498 (Seq Scan) - LEAF

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

### Step 9: Node 16499 (Hash)

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

### Step 10: Node 16497 (Hash Join)

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

### Step 11: Node 16507 (Index Scan) - LEAF

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

### Step 12: Node 16509 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=534
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0027
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=0.42, rt=44.49

### Step 13: Node 16496 (Nested Loop)

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

### Step 14: Node 16508 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=534
  - nt1=534
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=44.4932
  - rt2=0.0000
  - sel=1.0000
  - st1=0.4241
  - st2=0.0000
  - startup_cost=5169.6700
  - total_cost=5169.6700
- **Output:** st=17.77, rt=17.76

### Step 15: Node 16495 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=756
  - nt1=118013
  - nt2=534
  - parallel_workers=0
  - plan_width=20
  - reltuples=0.0000
  - rt1=1119.1991
  - rt2=17.7646
  - sel=0.0000
  - st1=37.2387
  - st2=17.7650
  - startup_cost=9919.8600
  - total_cost=70271.3400
- **Output:** st=77.18, rt=1027.31

### Step 16: Node 16510 (Index Scan) - LEAF

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

### Step 17: Node 16512 (Seq Scan) - LEAF

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

### Step 18: Node 16494 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=756
  - nt1=756
  - nt2=1
  - parallel_workers=0
  - plan_width=20
  - reltuples=0.0000
  - rt1=1027.3074
  - rt2=0.0512
  - sel=1.0000
  - st1=77.1779
  - st2=0.0060
  - startup_cost=9920.1500
  - total_cost=70500.0700
- **Output:** st=27.01, rt=1105.65

### Step 19: Node 16511 (Hash)

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

### Step 20: Node 16493 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=756
  - nt1=756
  - nt2=25
  - parallel_workers=0
  - plan_width=148
  - reltuples=0.0000
  - rt1=1105.6482
  - rt2=14.5397
  - sel=0.0400
  - st1=27.0073
  - st2=14.5393
  - startup_cost=9921.7100
  - total_cost=70505.8400
- **Output:** st=35.78, rt=1055.46

### Step 21: Node 16492 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=756
  - nt1=756
  - nt2=0
  - parallel_workers=0
  - plan_width=148
  - reltuples=0.0000
  - rt1=1055.4636
  - rt2=0.0000
  - sel=1.0000
  - st1=35.7799
  - st2=0.0000
  - startup_cost=70541.9800
  - total_cost=70543.8700
- **Output:** st=1086.92, rt=1087.88

### Step 22: Node 16491 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2343
  - nt1=756
  - nt2=0
  - parallel_workers=3
  - plan_width=148
  - reltuples=0.0000
  - rt1=1087.8781
  - rt2=0.0000
  - sel=3.0992
  - st1=1086.9201
  - st2=0.0000
  - startup_cost=71542.0200
  - total_cost=71819.2100
- **Output:** st=1120.81, rt=1123.89

### Step 23: Node 16490 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2343
  - nt1=2343
  - nt2=0
  - parallel_workers=0
  - plan_width=64
  - reltuples=0.0000
  - rt1=1123.8910
  - rt2=0.0000
  - sel=1.0000
  - st1=1120.8129
  - st2=0.0000
  - startup_cost=71542.0200
  - total_cost=71912.9300
- **Output:** st=1187.93, rt=1196.51
