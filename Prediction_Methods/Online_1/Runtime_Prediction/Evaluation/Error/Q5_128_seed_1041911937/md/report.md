# Online Prediction Report

**Test Query:** Q5_128_seed_1041911937
**Timestamp:** 2025-12-22 03:23:59

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 3.22%

## Phase C: Patterns in Query

- Total Patterns: 85

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
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 444761fb | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 52 | 46.8% | 24.3176 |
| 314469b0 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 5 | 48 | 43.2% | 20.7410 |
| 54cb7f90 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 6 | 48 | 43.2% | 20.7410 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| 3e2d5a00 | Sort -> Hash Join (Outer) | 2 | 96 | 19.3% | 18.5586 |
| ec92bdaa | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 52 | 29.1% | 15.1555 |
| ddb1e0ca | Sort -> Aggregate -> Gather Merge (Outer... | 3 | 48 | 28.5% | 13.6847 |
| c302739b | Hash Join -> [Seq Scan (Outer), Hash -> ... | 7 | 48 | 27.6% | 13.2381 |
| e1d7e5b4 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 48 | 27.6% | 13.2381 |
| 2422d111 | Hash Join -> [Nested Loop -> [Hash Join ... | 3 | 72 | 15.0% | 10.7757 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 140 | 4.5% | 6.2375 |
| 3d4c3db9 | Hash Join -> [Nested Loop -> [Hash Join ... | 7 | 48 | 12.3% | 5.9049 |
| 440e6274 | Hash Join -> [Nested Loop -> [Hash Join ... | 5 | 48 | 12.3% | 5.9049 |
| 4db07220 | Hash Join -> [Nested Loop -> [Hash Join ... | 4 | 48 | 12.3% | 5.9049 |
| 9ce781b0 | Hash Join -> [Nested Loop -> [Hash Join ... | 8 | 48 | 12.3% | 5.9049 |
| a95bee4e | Hash Join -> [Nested Loop -> [Hash Join ... | 9 | 48 | 12.3% | 5.9049 |
| f4603221 | Hash Join -> [Nested Loop -> [Hash Join ... | 6 | 48 | 12.3% | 5.9049 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 116 | 3.5% | 4.0772 |
| 91d6e559 | Sort -> Hash Join -> [Nested Loop (Outer... | 3 | 72 | 5.4% | 3.8546 |
| bd9dfa7b | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 92 | 3.7% | 3.3601 |
| 9d0e407c | Nested Loop -> [Hash Join -> [Seq Scan (... | 5 | 72 | 4.1% | 2.9587 |
| 12e6457c | Sort -> Hash Join -> [Nested Loop -> [Ha... | 4 | 48 | 6.0% | 2.9009 |
| 46f37744 | Gather Merge -> Aggregate (Outer) | 2 | 48 | 5.9% | 2.8144 |
| e6c1e0d8 | Gather Merge -> Aggregate -> Sort (Outer... | 3 | 48 | 5.9% | 2.8144 |
| 5ae97df8 | Nested Loop -> [Hash Join -> [Seq Scan (... | 8 | 48 | 4.4% | 2.1340 |
| 5bfce159 | Nested Loop -> [Hash Join -> [Seq Scan (... | 6 | 48 | 4.4% | 2.1340 |
| ef93d4fc | Nested Loop -> [Hash Join -> [Seq Scan (... | 7 | 48 | 4.4% | 2.1340 |
| 3754655c | Aggregate -> Sort (Outer) | 2 | 48 | 4.4% | 2.1302 |
| 460af52c | Aggregate -> Gather Merge -> Aggregate -... | 4 | 48 | 3.2% | 1.5375 |
| 8a8c43c6 | Aggregate -> Gather Merge -> Aggregate (... | 3 | 48 | 3.2% | 1.5375 |
| 14a1f63a | Gather Merge -> Aggregate -> Sort -> Has... | 5 | 24 | 5.0% | 1.1935 |
| 1b84acf9 | Gather Merge -> Aggregate -> Sort -> Has... | 12 | 24 | 5.0% | 1.1935 |
| 39e55ae2 | Gather Merge -> Aggregate -> Sort -> Has... | 4 | 24 | 5.0% | 1.1935 |
| 6255ff62 | Gather Merge -> Aggregate -> Sort -> Has... | 10 | 24 | 5.0% | 1.1935 |
| 739b1b7e | Gather Merge -> Aggregate -> Sort -> Has... | 7 | 24 | 5.0% | 1.1935 |
| 843b7fef | Gather Merge -> Aggregate -> Sort -> Has... | 6 | 24 | 5.0% | 1.1935 |
| 8b7a3d08 | Gather Merge -> Aggregate -> Sort -> Has... | 11 | 24 | 5.0% | 1.1935 |
| ac1e65be | Gather Merge -> Aggregate -> Sort -> Has... | 9 | 24 | 5.0% | 1.1935 |
| f169a84a | Gather Merge -> Aggregate -> Sort -> Has... | 8 | 24 | 5.0% | 1.1935 |
| 0fa21834 | Aggregate -> Sort -> Hash Join -> [Neste... | 6 | 24 | 4.8% | 1.1588 |
| 3a31b48f | Aggregate -> Sort -> Hash Join -> [Neste... | 5 | 24 | 4.8% | 1.1588 |
| 421ce908 | Aggregate -> Sort -> Hash Join -> [Neste... | 8 | 24 | 4.8% | 1.1588 |
| 4de97842 | Aggregate -> Sort -> Hash Join -> [Neste... | 7 | 24 | 4.8% | 1.1588 |
| 7b82db07 | Aggregate -> Sort -> Hash Join -> [Neste... | 10 | 24 | 4.8% | 1.1588 |
| 7d401e23 | Aggregate -> Sort -> Hash Join -> [Neste... | 11 | 24 | 4.8% | 1.1588 |
| 8823d1e5 | Aggregate -> Sort -> Hash Join (Outer) (... | 3 | 24 | 4.8% | 1.1588 |
| 9325c19d | Aggregate -> Sort -> Hash Join -> [Neste... | 9 | 24 | 4.8% | 1.1588 |
| 94adff2c | Aggregate -> Sort -> Hash Join -> [Neste... | 4 | 24 | 4.8% | 1.1588 |
| 255215ee | Sort -> Aggregate -> Gather Merge -> Agg... | 12 | 24 | 3.6% | 0.8575 |
| 5a24af68 | Sort -> Aggregate -> Gather Merge -> Agg... | 9 | 24 | 3.6% | 0.8575 |
| 627c5619 | Sort -> Aggregate -> Gather Merge -> Agg... | 4 | 24 | 3.6% | 0.8575 |
| 6815cf8d | Sort -> Aggregate -> Gather Merge -> Agg... | 6 | 24 | 3.6% | 0.8575 |
| 7014b260 | Sort -> Aggregate -> Gather Merge -> Agg... | 5 | 24 | 3.6% | 0.8575 |
| 9b0e5572 | Sort -> Aggregate -> Gather Merge -> Agg... | 8 | 24 | 3.6% | 0.8575 |
| b20b9f6a | Sort -> Aggregate -> Gather Merge -> Agg... | 10 | 24 | 3.6% | 0.8575 |
| bf4763ca | Sort -> Aggregate -> Gather Merge -> Agg... | 7 | 24 | 3.6% | 0.8575 |
| d21d6eb9 | Sort -> Aggregate -> Gather Merge -> Agg... | 11 | 24 | 3.6% | 0.8575 |
| d959dddb | Sort -> Aggregate -> Gather Merge -> Agg... | 13 | 24 | 3.6% | 0.8575 |
| de57e0e8 | Sort -> Aggregate -> Gather Merge -> Agg... | 14 | 24 | 3.6% | 0.8575 |
| 0e38b2d0 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 9 | 24 | 1.9% | 0.4506 |
| 2dc34d1b | Sort -> Hash Join -> [Nested Loop -> [Ha... | 7 | 24 | 1.9% | 0.4506 |
| 45767427 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 10 | 24 | 1.9% | 0.4506 |
| 5f022f0d | Sort -> Hash Join -> [Nested Loop -> [Ha... | 8 | 24 | 1.9% | 0.4506 |
| 91ed3a4f | Sort -> Hash Join -> [Nested Loop -> [Ha... | 5 | 24 | 1.9% | 0.4506 |
| d25d9b9f | Sort -> Hash Join -> [Nested Loop -> [Ha... | 6 | 24 | 1.9% | 0.4506 |
| 00dd2f10 | Aggregate -> Gather Merge -> Aggregate -... | 8 | 24 | 1.8% | 0.4402 |
| 2b345df9 | Aggregate -> Gather Merge -> Aggregate -... | 13 | 24 | 1.8% | 0.4402 |
| 45e3e43d | Aggregate -> Gather Merge -> Aggregate -... | 9 | 24 | 1.8% | 0.4402 |
| 729d307d | Aggregate -> Gather Merge -> Aggregate -... | 6 | 24 | 1.8% | 0.4402 |
| 8757732f | Aggregate -> Gather Merge -> Aggregate -... | 7 | 24 | 1.8% | 0.4402 |
| 96b20505 | Aggregate -> Gather Merge -> Aggregate -... | 10 | 24 | 1.8% | 0.4402 |
| b7143fa7 | Aggregate -> Gather Merge -> Aggregate -... | 12 | 24 | 1.8% | 0.4402 |
| c42cb45a | Aggregate -> Gather Merge -> Aggregate -... | 5 | 24 | 1.8% | 0.4402 |
| d0ca624d | Aggregate -> Gather Merge -> Aggregate -... | 11 | 24 | 1.8% | 0.4402 |

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
| 10 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 11 | 444761fb | 24.3176 | -0.0000% | REJECTED | 17.92% |
| 12 | 314469b0 | 20.7410 | 0.0000% | REJECTED | 17.92% |
| 13 | 54cb7f90 | 20.7410 | 0.0000% | REJECTED | 17.92% |
| 14 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 15 | 3e2d5a00 | 18.5586 | 0.0007% | REJECTED | 17.92% |
| 16 | ec92bdaa | 15.1555 | -0.0000% | REJECTED | 17.92% |
| 17 | ddb1e0ca | 13.6847 | -5.3651% | REJECTED | 17.92% |
| 18 | c302739b | 13.2381 | -0.0000% | REJECTED | 17.92% |
| 19 | e1d7e5b4 | 13.2381 | -0.0000% | REJECTED | 17.92% |
| 20 | 2422d111 | 10.7757 | 0.0001% | REJECTED | 17.92% |
| 21 | 3cfa90d7 | 6.2375 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 22 | 3d4c3db9 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 23 | 440e6274 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 24 | 4db07220 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 25 | 9ce781b0 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 26 | a95bee4e | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 27 | f4603221 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 28 | e0e3c3e1 | 4.0772 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 29 | 91d6e559 | 3.8546 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 30 | bd9dfa7b | 3.3601 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 31 | 9d0e407c | 2.9587 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 32 | 12e6457c | 2.9009 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 33 | 46f37744 | 2.8144 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 34 | e6c1e0d8 | 2.8144 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 35 | 5ae97df8 | 2.1340 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 36 | 5bfce159 | 2.1340 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 37 | ef93d4fc | 2.1340 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 38 | 3754655c | 2.1302 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 39 | 460af52c | 1.5375 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 40 | 8a8c43c6 | 1.5375 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 41 | 14a1f63a | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 42 | 1b84acf9 | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 43 | 39e55ae2 | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 44 | 6255ff62 | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 45 | 739b1b7e | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 46 | 843b7fef | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 47 | 8b7a3d08 | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 48 | ac1e65be | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 49 | f169a84a | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 50 | 0fa21834 | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 51 | 3a31b48f | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 52 | 421ce908 | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 53 | 4de97842 | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 54 | 7b82db07 | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 55 | 7d401e23 | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 56 | 8823d1e5 | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 57 | 9325c19d | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 58 | 94adff2c | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 59 | 255215ee | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 60 | 5a24af68 | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 61 | 627c5619 | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 62 | 6815cf8d | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 63 | 7014b260 | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 64 | 9b0e5572 | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 65 | b20b9f6a | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 66 | bf4763ca | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 67 | d21d6eb9 | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 68 | d959dddb | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 69 | de57e0e8 | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 70 | 0e38b2d0 | 0.4506 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 71 | 2dc34d1b | 0.4506 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 72 | 45767427 | 0.4506 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 73 | 5f022f0d | 0.4506 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 74 | 91ed3a4f | 0.4506 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 75 | d25d9b9f | 0.4506 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 76 | 00dd2f10 | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 77 | 2b345df9 | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 78 | 45e3e43d | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 79 | 729d307d | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 80 | 8757732f | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 81 | 96b20505 | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 82 | b7143fa7 | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 83 | c42cb45a | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 84 | d0ca624d | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.92% |
## Query Tree

```
Node 7501 (Sort) - ROOT
  Node 7502 (Aggregate)
    Node 7503 (Gather Merge)
      Node 7504 (Aggregate)
        Node 7505 (Sort)
          Node 7506 (Hash Join)
            Node 7507 (Nested Loop)
              Node 7508 (Hash Join)
                Node 7509 (Seq Scan) - LEAF
                Node 7510 (Hash)
                  Node 7511 (Hash Join)
                    Node 7512 (Seq Scan) - LEAF
                    Node 7513 (Hash)
                      Node 7514 (Hash Join)
                        Node 7515 (Seq Scan) - LEAF
                        Node 7516 (Hash)
                          Node 7517 (Seq Scan) - LEAF
              Node 7518 (Index Scan) - LEAF
            Node 7519 (Hash)
              Node 7520 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 2.83%
- Improvement: 0.39%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 7501 | Sort | 1073.80 | 1104.24 | 2.8% | operator |
| 7502 | Aggregate | 1073.79 | 1057.96 | 1.5% | operator |
| 7503 | Gather Merge | 1073.78 | 1124.38 | 4.7% | operator |
| 7504 | Aggregate | 1069.38 | 1020.00 | 4.6% | operator |
| 7505 | Sort | 1069.09 | 1074.63 | 0.5% | operator |
| 7506 | Hash Join | 1068.61 | 1106.69 | 3.6% | operator |
| 7507 | Nested Loop | 1057.17 | 1102.47 | 4.3% | operator |
| 7519 | Hash | 3.56 | 14.79 | 315.5% | operator |
| 7508 | Hash Join | 216.95 | 234.19 | 7.9% | operator |
| 7518 | Index Scan | 0.07 | -0.03 | 133.9% | operator |
| 7520 | Seq Scan | 3.02 | 10.62 | 251.9% | operator |
| 7509 | Seq Scan | 166.82 | 161.95 | 2.9% | operator |
| 7510 | Hash | 37.59 | 21.31 | 43.3% | operator |
| 7511 | Hash Join | 36.88 | 62.87 | 70.5% | operator |
| 7512 | Seq Scan | 35.28 | 24.87 | 29.5% | operator |
| 7513 | Hash | 0.18 | 16.80 | 8979.2% | operator |
| 7514 | Hash Join | 0.18 | 142.84 | 78385.7% | operator |
| 7515 | Seq Scan | 0.12 | 10.49 | 8573.3% | operator |
| 7516 | Hash | 0.05 | 16.01 | 29557.2% | operator |
| 7517 | Seq Scan | 0.05 | 21.39 | 41034.5% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 7517 (Seq Scan) - LEAF

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

### Step 2: Node 7515 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=1
  - nt=25
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=112
  - reltuples=25.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=1.2500
- **Output:** st=-0.02, rt=10.49

### Step 3: Node 7516 (Hash)

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

### Step 4: Node 7514 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=25
  - nt2=1
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=10.4947
  - rt2=16.0149
  - sel=0.2000
  - st1=-0.0152
  - st2=16.0154
  - startup_cost=1.0700
  - total_cost=2.4000
- **Output:** st=1.92, rt=142.84

### Step 5: Node 7512 (Seq Scan) - LEAF

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

### Step 6: Node 7513 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=5
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=142.8439
  - rt2=0.0000
  - sel=1.0000
  - st1=1.9164
  - st2=0.0000
  - startup_cost=2.4000
  - total_cost=2.4000
- **Output:** st=16.80, rt=16.80

### Step 7: Node 7511 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=12500
  - nt1=62500
  - nt2=5
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=24.8735
  - rt2=16.7965
  - sel=0.0400
  - st1=0.2761
  - st2=16.7962
  - startup_cost=2.4600
  - total_cost=4586.8400
- **Output:** st=3.04, rt=62.87

### Step 8: Node 7509 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=73231
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0488
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=33394.0600
- **Output:** st=0.18, rt=161.95

### Step 9: Node 7510 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=12500
  - nt1=12500
  - nt2=0
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=62.8708
  - rt2=0.0000
  - sel=1.0000
  - st1=3.0413
  - st2=0.0000
  - startup_cost=4586.8400
  - total_cost=4586.8400
- **Output:** st=21.31, rt=21.31

### Step 10: Node 7508 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14646
  - nt1=73231
  - nt2=12500
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=161.9450
  - rt2=21.3137
  - sel=0.0000
  - st1=0.1786
  - st2=21.3132
  - startup_cost=4743.0900
  - total_cost=38472.8000
- **Output:** st=24.77, rt=234.19

### Step 11: Node 7518 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=5
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=20
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.4300
  - total_cost=1.1500
- **Output:** st=0.07, rt=-0.03

### Step 12: Node 7520 (Seq Scan) - LEAF

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

### Step 13: Node 7507 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=58597
  - nt1=14646
  - nt2=5
  - parallel_workers=0
  - plan_width=128
  - reltuples=0.0000
  - rt1=234.1852
  - rt2=-0.0251
  - sel=0.8002
  - st1=24.7650
  - st2=0.0674
  - startup_cost=4743.5200
  - total_cost=55979.7800
- **Output:** st=42.51, rt=1102.47

### Step 14: Node 7519 (Hash)

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

### Step 15: Node 7506 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2344
  - nt1=58597
  - nt2=10000
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=1102.4654
  - rt2=14.7884
  - sel=0.0000
  - st1=42.5052
  - st2=14.7887
  - startup_cost=5216.5200
  - total_cost=56760.4200
- **Output:** st=49.38, rt=1106.69

### Step 16: Node 7505 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2344
  - nt1=2344
  - nt2=0
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=1106.6853
  - rt2=0.0000
  - sel=1.0000
  - st1=49.3846
  - st2=0.0000
  - startup_cost=56891.6200
  - total_cost=56897.4800
- **Output:** st=1073.70, rt=1074.63

### Step 17: Node 7504 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=2344
  - nt2=0
  - parallel_workers=0
  - plan_width=136
  - reltuples=0.0000
  - rt1=1074.6262
  - rt2=0.0000
  - sel=0.0107
  - st1=1073.7039
  - st2=0.0000
  - startup_cost=56891.6200
  - total_cost=56921.2300
- **Output:** st=1017.96, rt=1020.00

### Step 18: Node 7503 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=75
  - nt1=25
  - nt2=0
  - parallel_workers=3
  - plan_width=136
  - reltuples=0.0000
  - rt1=1019.9969
  - rt2=0.0000
  - sel=3.0000
  - st1=1017.9625
  - st2=0.0000
  - startup_cost=57891.6600
  - total_cost=57930.0800
- **Output:** st=1121.36, rt=1124.38

### Step 19: Node 7502 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=75
  - nt2=0
  - parallel_workers=0
  - plan_width=136
  - reltuples=0.0000
  - rt1=1124.3803
  - rt2=0.0000
  - sel=0.3333
  - st1=1121.3623
  - st2=0.0000
  - startup_cost=57891.6600
  - total_cost=57930.9600
- **Output:** st=1074.38, rt=1057.96

### Step 20: Node 7501 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=25
  - nt2=0
  - parallel_workers=0
  - plan_width=136
  - reltuples=0.0000
  - rt1=1057.9622
  - rt2=0.0000
  - sel=1.0000
  - st1=1074.3766
  - st2=0.0000
  - startup_cost=57931.5400
  - total_cost=57931.6000
- **Output:** st=1102.40, rt=1104.24
