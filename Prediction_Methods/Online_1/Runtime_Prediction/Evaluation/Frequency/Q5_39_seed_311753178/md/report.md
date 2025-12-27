# Online Prediction Report

**Test Query:** Q5_39_seed_311753178
**Timestamp:** 2025-12-22 07:21:46

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 4.28%

## Phase C: Patterns in Query

- Total Patterns: 85

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 33781.0% | 113504.2307 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 172 | 3565.0% | 6131.8766 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 168 | 44967.0% | 75544.5822 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 148 | 116.8% | 172.9284 |
| c0a8d3de | Hash -> Hash Join -> [Seq Scan (Outer), ... | 3 | 148 | 4130.8% | 6113.5159 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 75.1% | 108.1438 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 140 | 4.5% | 6.2375 |
| 37515ad8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 124 | 135.7% | 168.3286 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 116 | 3.5% | 4.0772 |
| 3e2d5a00 | Sort -> Hash Join (Outer) | 2 | 96 | 19.3% | 18.5586 |
| a54055ce | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 96 | 6342.9% | 6089.1983 |
| bd9dfa7b | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 92 | 3.7% | 3.3601 |
| 91d6e559 | Sort -> Hash Join -> [Nested Loop (Outer... | 3 | 72 | 5.4% | 3.8546 |
| 2422d111 | Hash Join -> [Nested Loop -> [Hash Join ... | 3 | 72 | 15.0% | 10.7757 |
| 9d0e407c | Nested Loop -> [Hash Join -> [Seq Scan (... | 5 | 72 | 4.1% | 2.9587 |
| 545b5e57 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 72 | 212.7% | 153.1732 |
| 444761fb | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 52 | 46.8% | 24.3176 |
| ec92bdaa | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 52 | 29.1% | 15.1555 |
| 46f37744 | Gather Merge -> Aggregate (Outer) | 2 | 48 | 5.9% | 2.8144 |
| 3754655c | Aggregate -> Sort (Outer) | 2 | 48 | 4.4% | 2.1302 |
| ddb1e0ca | Sort -> Aggregate -> Gather Merge (Outer... | 3 | 48 | 28.5% | 13.6847 |
| 8a8c43c6 | Aggregate -> Gather Merge -> Aggregate (... | 3 | 48 | 3.2% | 1.5375 |
| e6c1e0d8 | Gather Merge -> Aggregate -> Sort (Outer... | 3 | 48 | 5.9% | 2.8144 |
| 460af52c | Aggregate -> Gather Merge -> Aggregate -... | 4 | 48 | 3.2% | 1.5375 |
| 12e6457c | Sort -> Hash Join -> [Nested Loop -> [Ha... | 4 | 48 | 6.0% | 2.9009 |
| 4db07220 | Hash Join -> [Nested Loop -> [Hash Join ... | 4 | 48 | 12.3% | 5.9049 |
| 440e6274 | Hash Join -> [Nested Loop -> [Hash Join ... | 5 | 48 | 12.3% | 5.9049 |
| 314469b0 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 5 | 48 | 43.2% | 20.7410 |
| f4603221 | Hash Join -> [Nested Loop -> [Hash Join ... | 6 | 48 | 12.3% | 5.9049 |
| 5bfce159 | Nested Loop -> [Hash Join -> [Seq Scan (... | 6 | 48 | 4.4% | 2.1340 |
| e1d7e5b4 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 48 | 27.6% | 13.2381 |
| 54cb7f90 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 6 | 48 | 43.2% | 20.7410 |
| 3d4c3db9 | Hash Join -> [Nested Loop -> [Hash Join ... | 7 | 48 | 12.3% | 5.9049 |
| ef93d4fc | Nested Loop -> [Hash Join -> [Seq Scan (... | 7 | 48 | 4.4% | 2.1340 |
| c302739b | Hash Join -> [Seq Scan (Outer), Hash -> ... | 7 | 48 | 27.6% | 13.2381 |
| 9ce781b0 | Hash Join -> [Nested Loop -> [Hash Join ... | 8 | 48 | 12.3% | 5.9049 |
| 5ae97df8 | Nested Loop -> [Hash Join -> [Seq Scan (... | 8 | 48 | 4.4% | 2.1340 |
| a95bee4e | Hash Join -> [Nested Loop -> [Hash Join ... | 9 | 48 | 12.3% | 5.9049 |
| 8823d1e5 | Aggregate -> Sort -> Hash Join (Outer) (... | 3 | 24 | 4.8% | 1.1588 |
| 627c5619 | Sort -> Aggregate -> Gather Merge -> Agg... | 4 | 24 | 3.6% | 0.8575 |
| 39e55ae2 | Gather Merge -> Aggregate -> Sort -> Has... | 4 | 24 | 5.0% | 1.1935 |
| 94adff2c | Aggregate -> Sort -> Hash Join -> [Neste... | 4 | 24 | 4.8% | 1.1588 |
| 7014b260 | Sort -> Aggregate -> Gather Merge -> Agg... | 5 | 24 | 3.6% | 0.8575 |
| c42cb45a | Aggregate -> Gather Merge -> Aggregate -... | 5 | 24 | 1.8% | 0.4402 |
| 14a1f63a | Gather Merge -> Aggregate -> Sort -> Has... | 5 | 24 | 5.0% | 1.1935 |
| 3a31b48f | Aggregate -> Sort -> Hash Join -> [Neste... | 5 | 24 | 4.8% | 1.1588 |
| 91ed3a4f | Sort -> Hash Join -> [Nested Loop -> [Ha... | 5 | 24 | 1.9% | 0.4506 |
| 6815cf8d | Sort -> Aggregate -> Gather Merge -> Agg... | 6 | 24 | 3.6% | 0.8575 |
| 729d307d | Aggregate -> Gather Merge -> Aggregate -... | 6 | 24 | 1.8% | 0.4402 |
| 843b7fef | Gather Merge -> Aggregate -> Sort -> Has... | 6 | 24 | 5.0% | 1.1935 |
| 0fa21834 | Aggregate -> Sort -> Hash Join -> [Neste... | 6 | 24 | 4.8% | 1.1588 |
| d25d9b9f | Sort -> Hash Join -> [Nested Loop -> [Ha... | 6 | 24 | 1.9% | 0.4506 |
| bf4763ca | Sort -> Aggregate -> Gather Merge -> Agg... | 7 | 24 | 3.6% | 0.8575 |
| 8757732f | Aggregate -> Gather Merge -> Aggregate -... | 7 | 24 | 1.8% | 0.4402 |
| 739b1b7e | Gather Merge -> Aggregate -> Sort -> Has... | 7 | 24 | 5.0% | 1.1935 |
| 4de97842 | Aggregate -> Sort -> Hash Join -> [Neste... | 7 | 24 | 4.8% | 1.1588 |
| 2dc34d1b | Sort -> Hash Join -> [Nested Loop -> [Ha... | 7 | 24 | 1.9% | 0.4506 |
| 9b0e5572 | Sort -> Aggregate -> Gather Merge -> Agg... | 8 | 24 | 3.6% | 0.8575 |
| 00dd2f10 | Aggregate -> Gather Merge -> Aggregate -... | 8 | 24 | 1.8% | 0.4402 |
| f169a84a | Gather Merge -> Aggregate -> Sort -> Has... | 8 | 24 | 5.0% | 1.1935 |
| 421ce908 | Aggregate -> Sort -> Hash Join -> [Neste... | 8 | 24 | 4.8% | 1.1588 |
| 5f022f0d | Sort -> Hash Join -> [Nested Loop -> [Ha... | 8 | 24 | 1.9% | 0.4506 |
| 5a24af68 | Sort -> Aggregate -> Gather Merge -> Agg... | 9 | 24 | 3.6% | 0.8575 |
| 45e3e43d | Aggregate -> Gather Merge -> Aggregate -... | 9 | 24 | 1.8% | 0.4402 |
| ac1e65be | Gather Merge -> Aggregate -> Sort -> Has... | 9 | 24 | 5.0% | 1.1935 |
| 9325c19d | Aggregate -> Sort -> Hash Join -> [Neste... | 9 | 24 | 4.8% | 1.1588 |
| 0e38b2d0 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 9 | 24 | 1.9% | 0.4506 |
| b20b9f6a | Sort -> Aggregate -> Gather Merge -> Agg... | 10 | 24 | 3.6% | 0.8575 |
| 96b20505 | Aggregate -> Gather Merge -> Aggregate -... | 10 | 24 | 1.8% | 0.4402 |
| 6255ff62 | Gather Merge -> Aggregate -> Sort -> Has... | 10 | 24 | 5.0% | 1.1935 |
| 7b82db07 | Aggregate -> Sort -> Hash Join -> [Neste... | 10 | 24 | 4.8% | 1.1588 |
| 45767427 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 10 | 24 | 1.9% | 0.4506 |
| d21d6eb9 | Sort -> Aggregate -> Gather Merge -> Agg... | 11 | 24 | 3.6% | 0.8575 |
| d0ca624d | Aggregate -> Gather Merge -> Aggregate -... | 11 | 24 | 1.8% | 0.4402 |
| 8b7a3d08 | Gather Merge -> Aggregate -> Sort -> Has... | 11 | 24 | 5.0% | 1.1935 |
| 7d401e23 | Aggregate -> Sort -> Hash Join -> [Neste... | 11 | 24 | 4.8% | 1.1588 |
| 255215ee | Sort -> Aggregate -> Gather Merge -> Agg... | 12 | 24 | 3.6% | 0.8575 |
| b7143fa7 | Aggregate -> Gather Merge -> Aggregate -... | 12 | 24 | 1.8% | 0.4402 |
| 1b84acf9 | Gather Merge -> Aggregate -> Sort -> Has... | 12 | 24 | 5.0% | 1.1935 |
| d959dddb | Sort -> Aggregate -> Gather Merge -> Agg... | 13 | 24 | 3.6% | 0.8575 |
| 2b345df9 | Aggregate -> Gather Merge -> Aggregate -... | 13 | 24 | 1.8% | 0.4402 |
| de57e0e8 | Sort -> Aggregate -> Gather Merge -> Agg... | 14 | 24 | 3.6% | 0.8575 |

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
| 4 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 5 | f4cb205a | 75544.5822 | 0.0006% | REJECTED | 17.92% |
| 6 | bb930825 | 172.9284 | -0.0000% | REJECTED | 17.92% |
| 7 | c0a8d3de | 6113.5159 | -0.0000% | REJECTED | 17.92% |
| 8 | 2e0f44ef | 108.1438 | 0.0001% | REJECTED | 17.92% |
| 9 | 3cfa90d7 | 6.2375 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 10 | 37515ad8 | 168.3286 | -0.0000% | REJECTED | 17.92% |
| 11 | e0e3c3e1 | 4.0772 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 12 | 3e2d5a00 | 18.5586 | 0.0007% | REJECTED | 17.92% |
| 13 | a54055ce | 6089.1983 | -0.0000% | REJECTED | 17.92% |
| 14 | bd9dfa7b | 3.3601 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 15 | 91d6e559 | 3.8546 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 16 | 2422d111 | 10.7757 | 0.0001% | REJECTED | 17.92% |
| 17 | 9d0e407c | 2.9587 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 18 | 545b5e57 | 153.1732 | -0.0000% | REJECTED | 17.92% |
| 19 | 444761fb | 24.3176 | -0.0000% | REJECTED | 17.92% |
| 20 | ec92bdaa | 15.1555 | -0.0000% | REJECTED | 17.92% |
| 21 | 46f37744 | 2.8144 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 22 | 3754655c | 2.1302 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 23 | ddb1e0ca | 13.6847 | -5.3651% | REJECTED | 17.92% |
| 24 | 8a8c43c6 | 1.5375 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 25 | e6c1e0d8 | 2.8144 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 26 | 460af52c | 1.5375 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 27 | 12e6457c | 2.9009 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 28 | 4db07220 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 29 | 440e6274 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 30 | 314469b0 | 20.7410 | 0.0000% | REJECTED | 17.92% |
| 31 | f4603221 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 32 | 5bfce159 | 2.1340 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 33 | e1d7e5b4 | 13.2381 | -0.0000% | REJECTED | 17.92% |
| 34 | 54cb7f90 | 20.7410 | 0.0000% | REJECTED | 17.92% |
| 35 | 3d4c3db9 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 36 | ef93d4fc | 2.1340 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 37 | c302739b | 13.2381 | -0.0000% | REJECTED | 17.92% |
| 38 | 9ce781b0 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 39 | 5ae97df8 | 2.1340 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 40 | a95bee4e | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 41 | 8823d1e5 | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 42 | 627c5619 | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 43 | 39e55ae2 | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 44 | 94adff2c | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 45 | 7014b260 | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 46 | c42cb45a | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 47 | 14a1f63a | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 48 | 3a31b48f | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 49 | 91ed3a4f | 0.4506 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 50 | 6815cf8d | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 51 | 729d307d | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 52 | 843b7fef | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 53 | 0fa21834 | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 54 | d25d9b9f | 0.4506 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 55 | bf4763ca | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 56 | 8757732f | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 57 | 739b1b7e | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 58 | 4de97842 | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 59 | 2dc34d1b | 0.4506 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 60 | 9b0e5572 | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 61 | 00dd2f10 | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 62 | f169a84a | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 63 | 421ce908 | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 64 | 5f022f0d | 0.4506 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 65 | 5a24af68 | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 66 | 45e3e43d | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 67 | ac1e65be | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 68 | 9325c19d | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 69 | 0e38b2d0 | 0.4506 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 70 | b20b9f6a | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 71 | 96b20505 | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 72 | 6255ff62 | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 73 | 7b82db07 | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 74 | 45767427 | 0.4506 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 75 | d21d6eb9 | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 76 | d0ca624d | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 77 | 8b7a3d08 | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 78 | 7d401e23 | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 79 | 255215ee | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 80 | b7143fa7 | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 81 | 1b84acf9 | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 82 | d959dddb | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 83 | 2b345df9 | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 84 | de57e0e8 | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.92% |
## Query Tree

```
Node 8541 (Sort) - ROOT
  Node 8542 (Aggregate)
    Node 8543 (Gather Merge)
      Node 8544 (Aggregate)
        Node 8545 (Sort)
          Node 8546 (Hash Join)
            Node 8547 (Nested Loop)
              Node 8548 (Hash Join)
                Node 8549 (Seq Scan) - LEAF
                Node 8550 (Hash)
                  Node 8551 (Hash Join)
                    Node 8552 (Seq Scan) - LEAF
                    Node 8553 (Hash)
                      Node 8554 (Hash Join)
                        Node 8555 (Seq Scan) - LEAF
                        Node 8556 (Hash)
                          Node 8557 (Seq Scan) - LEAF
              Node 8558 (Index Scan) - LEAF
            Node 8559 (Hash)
              Node 8560 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 3.89%
- Improvement: 0.39%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 8541 | Sort | 1062.91 | 1104.24 | 3.9% | operator |
| 8542 | Aggregate | 1062.89 | 1057.87 | 0.5% | operator |
| 8543 | Gather Merge | 1062.89 | 1124.35 | 5.8% | operator |
| 8544 | Aggregate | 1058.07 | 1019.89 | 3.6% | operator |
| 8545 | Sort | 1057.83 | 1074.66 | 1.6% | operator |
| 8546 | Hash Join | 1057.33 | 1107.14 | 4.7% | operator |
| 8547 | Nested Loop | 1045.42 | 1102.69 | 5.5% | operator |
| 8559 | Hash | 3.73 | 14.79 | 296.5% | operator |
| 8548 | Hash Join | 217.29 | 234.18 | 7.8% | operator |
| 8558 | Index Scan | 0.07 | -0.03 | 134.4% | operator |
| 8560 | Seq Scan | 3.22 | 10.62 | 230.1% | operator |
| 8549 | Seq Scan | 165.20 | 161.95 | 2.0% | operator |
| 8550 | Hash | 39.32 | 21.31 | 45.8% | operator |
| 8551 | Hash Join | 38.61 | 62.87 | 62.8% | operator |
| 8552 | Seq Scan | 37.10 | 24.87 | 33.0% | operator |
| 8553 | Hash | 0.17 | 16.80 | 10079.7% | operator |
| 8554 | Hash Join | 0.16 | 142.84 | 88075.3% | operator |
| 8555 | Seq Scan | 0.01 | 10.49 | 116508.1% | operator |
| 8556 | Hash | 0.15 | 16.01 | 10794.5% | operator |
| 8557 | Seq Scan | 0.14 | 21.39 | 14754.1% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 8557 (Seq Scan) - LEAF

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

### Step 2: Node 8555 (Seq Scan) - LEAF

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

### Step 3: Node 8556 (Hash)

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

### Step 4: Node 8554 (Hash Join)

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

### Step 5: Node 8552 (Seq Scan) - LEAF

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

### Step 6: Node 8553 (Hash)

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

### Step 7: Node 8551 (Hash Join)

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

### Step 8: Node 8549 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=74418
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0496
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=33394.0600
- **Output:** st=0.18, rt=161.95

### Step 9: Node 8550 (Hash)

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

### Step 10: Node 8548 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14884
  - nt1=74418
  - nt2=12500
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=161.9546
  - rt2=21.3137
  - sel=0.0000
  - st1=0.1790
  - st2=21.3132
  - startup_cost=4743.0900
  - total_cost=38478.2400
- **Output:** st=24.76, rt=234.18

### Step 11: Node 8558 (Index Scan) - LEAF

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
  - total_cost=1.1400
- **Output:** st=0.07, rt=-0.03

### Step 12: Node 8560 (Seq Scan) - LEAF

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

### Step 13: Node 8547 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=59546
  - nt1=14884
  - nt2=5
  - parallel_workers=0
  - plan_width=128
  - reltuples=0.0000
  - rt1=234.1837
  - rt2=-0.0251
  - sel=0.8001
  - st1=24.7647
  - st2=0.0674
  - startup_cost=4743.5200
  - total_cost=56121.2800
- **Output:** st=42.63, rt=1102.69

### Step 14: Node 8559 (Hash)

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

### Step 15: Node 8546 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2382
  - nt1=59546
  - nt2=10000
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=1102.6872
  - rt2=14.7884
  - sel=0.0000
  - st1=42.6265
  - st2=14.7887
  - startup_cost=5216.5200
  - total_cost=56906.9000
- **Output:** st=49.51, rt=1107.14

### Step 16: Node 8545 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2382
  - nt1=2382
  - nt2=0
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=1107.1381
  - rt2=0.0000
  - sel=1.0000
  - st1=49.5074
  - st2=0.0000
  - startup_cost=57040.5100
  - total_cost=57046.4600
- **Output:** st=1073.74, rt=1074.66

### Step 17: Node 8544 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=2382
  - nt2=0
  - parallel_workers=0
  - plan_width=136
  - reltuples=0.0000
  - rt1=1074.6625
  - rt2=0.0000
  - sel=0.0105
  - st1=1073.7395
  - st2=0.0000
  - startup_cost=57040.5100
  - total_cost=57070.5900
- **Output:** st=1017.87, rt=1019.89

### Step 18: Node 8543 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=75
  - nt1=25
  - nt2=0
  - parallel_workers=3
  - plan_width=136
  - reltuples=0.0000
  - rt1=1019.8930
  - rt2=0.0000
  - sel=3.0000
  - st1=1017.8677
  - st2=0.0000
  - startup_cost=58040.5500
  - total_cost=58079.4500
- **Output:** st=1121.33, rt=1124.35

### Step 19: Node 8542 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=75
  - nt2=0
  - parallel_workers=0
  - plan_width=136
  - reltuples=0.0000
  - rt1=1124.3522
  - rt2=0.0000
  - sel=0.3333
  - st1=1121.3337
  - st2=0.0000
  - startup_cost=58040.5500
  - total_cost=58080.3200
- **Output:** st=1074.31, rt=1057.87

### Step 20: Node 8541 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=25
  - nt2=0
  - parallel_workers=0
  - plan_width=136
  - reltuples=0.0000
  - rt1=1057.8672
  - rt2=0.0000
  - sel=1.0000
  - st1=1074.3091
  - st2=0.0000
  - startup_cost=58080.9000
  - total_cost=58080.9600
- **Output:** st=1102.40, rt=1104.24
