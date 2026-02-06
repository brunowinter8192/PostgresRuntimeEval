# Online Prediction Report

**Test Query:** Q5_64_seed_516853953
**Timestamp:** 2026-01-11 18:42:00

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 5.36%

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
| 545b5e57 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 72 | 212.7% | 153.1732 |
| 9d0e407c | Nested Loop -> [Hash Join -> [Seq Scan (... | 5 | 72 | 4.1% | 2.9587 |
| 444761fb | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 52 | 46.8% | 24.3176 |
| ec92bdaa | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 52 | 29.1% | 15.1555 |
| 3754655c | Aggregate -> Sort (Outer) | 2 | 48 | 4.4% | 2.1302 |
| 46f37744 | Gather Merge -> Aggregate (Outer) | 2 | 48 | 5.9% | 2.8144 |
| 8a8c43c6 | Aggregate -> Gather Merge -> Aggregate (... | 3 | 48 | 3.2% | 1.5375 |
| ddb1e0ca | Sort -> Aggregate -> Gather Merge (Outer... | 3 | 48 | 28.5% | 13.6847 |
| e6c1e0d8 | Gather Merge -> Aggregate -> Sort (Outer... | 3 | 48 | 5.9% | 2.8144 |
| 460af52c | Aggregate -> Gather Merge -> Aggregate -... | 4 | 48 | 3.2% | 1.5375 |
| 12e6457c | Sort -> Hash Join -> [Nested Loop -> [Ha... | 4 | 48 | 6.0% | 2.9009 |
| 314469b0 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 5 | 48 | 43.2% | 20.7410 |
| 4db07220 | Hash Join -> [Nested Loop -> [Hash Join ... | 4 | 48 | 12.3% | 5.9049 |
| 54cb7f90 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 6 | 48 | 43.2% | 20.7410 |
| 440e6274 | Hash Join -> [Nested Loop -> [Hash Join ... | 5 | 48 | 12.3% | 5.9049 |
| 5bfce159 | Nested Loop -> [Hash Join -> [Seq Scan (... | 6 | 48 | 4.4% | 2.1340 |
| e1d7e5b4 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 48 | 27.6% | 13.2381 |
| c302739b | Hash Join -> [Seq Scan (Outer), Hash -> ... | 7 | 48 | 27.6% | 13.2381 |
| ef93d4fc | Nested Loop -> [Hash Join -> [Seq Scan (... | 7 | 48 | 4.4% | 2.1340 |
| f4603221 | Hash Join -> [Nested Loop -> [Hash Join ... | 6 | 48 | 12.3% | 5.9049 |
| 3d4c3db9 | Hash Join -> [Nested Loop -> [Hash Join ... | 7 | 48 | 12.3% | 5.9049 |
| 5ae97df8 | Nested Loop -> [Hash Join -> [Seq Scan (... | 8 | 48 | 4.4% | 2.1340 |
| 9ce781b0 | Hash Join -> [Nested Loop -> [Hash Join ... | 8 | 48 | 12.3% | 5.9049 |
| a95bee4e | Hash Join -> [Nested Loop -> [Hash Join ... | 9 | 48 | 12.3% | 5.9049 |
| 8823d1e5 | Aggregate -> Sort -> Hash Join (Outer) (... | 3 | 24 | 4.8% | 1.1588 |
| 39e55ae2 | Gather Merge -> Aggregate -> Sort -> Has... | 4 | 24 | 5.0% | 1.1935 |
| 627c5619 | Sort -> Aggregate -> Gather Merge -> Agg... | 4 | 24 | 3.6% | 0.8575 |
| 7014b260 | Sort -> Aggregate -> Gather Merge -> Agg... | 5 | 24 | 3.6% | 0.8575 |
| 94adff2c | Aggregate -> Sort -> Hash Join -> [Neste... | 4 | 24 | 4.8% | 1.1588 |
| c42cb45a | Aggregate -> Gather Merge -> Aggregate -... | 5 | 24 | 1.8% | 0.4402 |
| 14a1f63a | Gather Merge -> Aggregate -> Sort -> Has... | 5 | 24 | 5.0% | 1.1935 |
| 6815cf8d | Sort -> Aggregate -> Gather Merge -> Agg... | 6 | 24 | 3.6% | 0.8575 |
| 729d307d | Aggregate -> Gather Merge -> Aggregate -... | 6 | 24 | 1.8% | 0.4402 |
| 3a31b48f | Aggregate -> Sort -> Hash Join -> [Neste... | 5 | 24 | 4.8% | 1.1588 |
| bf4763ca | Sort -> Aggregate -> Gather Merge -> Agg... | 7 | 24 | 3.6% | 0.8575 |
| 843b7fef | Gather Merge -> Aggregate -> Sort -> Has... | 6 | 24 | 5.0% | 1.1935 |
| 91ed3a4f | Sort -> Hash Join -> [Nested Loop -> [Ha... | 5 | 24 | 1.9% | 0.4506 |
| 0fa21834 | Aggregate -> Sort -> Hash Join -> [Neste... | 6 | 24 | 4.8% | 1.1588 |
| 8757732f | Aggregate -> Gather Merge -> Aggregate -... | 7 | 24 | 1.8% | 0.4402 |
| d25d9b9f | Sort -> Hash Join -> [Nested Loop -> [Ha... | 6 | 24 | 1.9% | 0.4506 |
| 4de97842 | Aggregate -> Sort -> Hash Join -> [Neste... | 7 | 24 | 4.8% | 1.1588 |
| 739b1b7e | Gather Merge -> Aggregate -> Sort -> Has... | 7 | 24 | 5.0% | 1.1935 |
| 9b0e5572 | Sort -> Aggregate -> Gather Merge -> Agg... | 8 | 24 | 3.6% | 0.8575 |
| 00dd2f10 | Aggregate -> Gather Merge -> Aggregate -... | 8 | 24 | 1.8% | 0.4402 |
| 2dc34d1b | Sort -> Hash Join -> [Nested Loop -> [Ha... | 7 | 24 | 1.9% | 0.4506 |
| f169a84a | Gather Merge -> Aggregate -> Sort -> Has... | 8 | 24 | 5.0% | 1.1935 |
| 421ce908 | Aggregate -> Sort -> Hash Join -> [Neste... | 8 | 24 | 4.8% | 1.1588 |
| 45e3e43d | Aggregate -> Gather Merge -> Aggregate -... | 9 | 24 | 1.8% | 0.4402 |
| 5a24af68 | Sort -> Aggregate -> Gather Merge -> Agg... | 9 | 24 | 3.6% | 0.8575 |
| 5f022f0d | Sort -> Hash Join -> [Nested Loop -> [Ha... | 8 | 24 | 1.9% | 0.4506 |
| 9325c19d | Aggregate -> Sort -> Hash Join -> [Neste... | 9 | 24 | 4.8% | 1.1588 |
| ac1e65be | Gather Merge -> Aggregate -> Sort -> Has... | 9 | 24 | 5.0% | 1.1935 |
| b20b9f6a | Sort -> Aggregate -> Gather Merge -> Agg... | 10 | 24 | 3.6% | 0.8575 |
| 0e38b2d0 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 9 | 24 | 1.9% | 0.4506 |
| 6255ff62 | Gather Merge -> Aggregate -> Sort -> Has... | 10 | 24 | 5.0% | 1.1935 |
| 96b20505 | Aggregate -> Gather Merge -> Aggregate -... | 10 | 24 | 1.8% | 0.4402 |
| 45767427 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 10 | 24 | 1.9% | 0.4506 |
| 7b82db07 | Aggregate -> Sort -> Hash Join -> [Neste... | 10 | 24 | 4.8% | 1.1588 |
| d0ca624d | Aggregate -> Gather Merge -> Aggregate -... | 11 | 24 | 1.8% | 0.4402 |
| d21d6eb9 | Sort -> Aggregate -> Gather Merge -> Agg... | 11 | 24 | 3.6% | 0.8575 |
| 255215ee | Sort -> Aggregate -> Gather Merge -> Agg... | 12 | 24 | 3.6% | 0.8575 |
| 7d401e23 | Aggregate -> Sort -> Hash Join -> [Neste... | 11 | 24 | 4.8% | 1.1588 |
| 8b7a3d08 | Gather Merge -> Aggregate -> Sort -> Has... | 11 | 24 | 5.0% | 1.1935 |
| 1b84acf9 | Gather Merge -> Aggregate -> Sort -> Has... | 12 | 24 | 5.0% | 1.1935 |
| b7143fa7 | Aggregate -> Gather Merge -> Aggregate -... | 12 | 24 | 1.8% | 0.4402 |
| 2b345df9 | Aggregate -> Gather Merge -> Aggregate -... | 13 | 24 | 1.8% | 0.4402 |
| d959dddb | Sort -> Aggregate -> Gather Merge -> Agg... | 13 | 24 | 3.6% | 0.8575 |
| de57e0e8 | Sort -> Aggregate -> Gather Merge -> Agg... | 14 | 24 | 3.6% | 0.8575 |

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
| 4 | 2724c080 | 19.6008 | 0.0346% | ACCEPTED | 17.77% |
| 5 | f4cb205a | 75544.5822 | 0.0005% | ACCEPTED | 17.77% |
| 6 | bb930825 | 172.9284 | N/A | REJECTED | 17.77% |
| 7 | c0a8d3de | 6113.5159 | N/A | REJECTED | 17.77% |
| 8 | 2e0f44ef | 108.1438 | N/A | REJECTED | 17.77% |
| 9 | 3cfa90d7 | 6.2375 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 10 | 37515ad8 | 168.3286 | N/A | REJECTED | 17.77% |
| 11 | e0e3c3e1 | 4.0772 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 12 | 3e2d5a00 | 18.5586 | N/A | REJECTED | 17.77% |
| 13 | a54055ce | 6089.1983 | N/A | REJECTED | 17.77% |
| 14 | bd9dfa7b | 3.3601 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 15 | 91d6e559 | 3.8546 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 16 | 2422d111 | 10.7757 | N/A | REJECTED | 17.77% |
| 17 | 545b5e57 | 153.1732 | N/A | REJECTED | 17.77% |
| 18 | 9d0e407c | 2.9587 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 19 | 444761fb | 24.3176 | N/A | REJECTED | 17.77% |
| 20 | ec92bdaa | 15.1555 | N/A | REJECTED | 17.77% |
| 21 | 3754655c | 2.1302 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 22 | 46f37744 | 2.8144 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 23 | 8a8c43c6 | 1.5375 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 24 | ddb1e0ca | 13.6847 | -5.4908% | REJECTED | 17.77% |
| 25 | e6c1e0d8 | 2.8144 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 26 | 460af52c | 1.5375 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 27 | 12e6457c | 2.9009 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 28 | 314469b0 | 20.7410 | N/A | REJECTED | 17.77% |
| 29 | 4db07220 | 5.9049 | N/A | REJECTED | 17.77% |
| 30 | 54cb7f90 | 20.7410 | N/A | REJECTED | 17.77% |
| 31 | 440e6274 | 5.9049 | N/A | REJECTED | 17.77% |
| 32 | 5bfce159 | 2.1340 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 33 | e1d7e5b4 | 13.2381 | N/A | REJECTED | 17.77% |
| 34 | c302739b | 13.2381 | N/A | REJECTED | 17.77% |
| 35 | ef93d4fc | 2.1340 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 36 | f4603221 | 5.9049 | N/A | REJECTED | 17.77% |
| 37 | 3d4c3db9 | 5.9049 | N/A | REJECTED | 17.77% |
| 38 | 5ae97df8 | 2.1340 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 39 | 9ce781b0 | 5.9049 | N/A | REJECTED | 17.77% |
| 40 | a95bee4e | 5.9049 | N/A | REJECTED | 17.77% |
| 41 | 8823d1e5 | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 42 | 39e55ae2 | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 43 | 627c5619 | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 44 | 7014b260 | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 45 | 94adff2c | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 46 | c42cb45a | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 47 | 14a1f63a | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 48 | 6815cf8d | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 49 | 729d307d | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 50 | 3a31b48f | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 51 | bf4763ca | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 52 | 843b7fef | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 53 | 91ed3a4f | 0.4506 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 54 | 0fa21834 | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 55 | 8757732f | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 56 | d25d9b9f | 0.4506 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 57 | 4de97842 | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 58 | 739b1b7e | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 59 | 9b0e5572 | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 60 | 00dd2f10 | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 61 | 2dc34d1b | 0.4506 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 62 | f169a84a | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 63 | 421ce908 | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 64 | 45e3e43d | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 65 | 5a24af68 | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 66 | 5f022f0d | 0.4506 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 67 | 9325c19d | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 68 | ac1e65be | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 69 | b20b9f6a | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 70 | 0e38b2d0 | 0.4506 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 71 | 6255ff62 | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 72 | 96b20505 | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 73 | 45767427 | 0.4506 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 74 | 7b82db07 | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 75 | d0ca624d | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 76 | d21d6eb9 | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 77 | 255215ee | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 78 | 7d401e23 | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 79 | 8b7a3d08 | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 80 | 1b84acf9 | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 81 | b7143fa7 | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 82 | 2b345df9 | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 83 | d959dddb | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 84 | de57e0e8 | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.77% |
## Query Tree

```
Node 9101 (Sort) [PATTERN: 1d35fb97] - ROOT
  Node 9102 (Aggregate) [consumed]
    Node 9103 (Gather Merge)
      Node 9104 (Aggregate)
        Node 9105 (Sort)
          Node 9106 (Hash Join)
            Node 9107 (Nested Loop)
              Node 9108 (Hash Join) [PATTERN: 895c6e8c]
                Node 9109 (Seq Scan) [consumed] - LEAF
                Node 9110 (Hash) [consumed]
                  Node 9111 (Hash Join) [PATTERN: 895c6e8c]
                    Node 9112 (Seq Scan) [consumed] - LEAF
                    Node 9113 (Hash) [consumed]
                      Node 9114 (Hash Join) [PATTERN: f4cb205a]
                        Node 9115 (Seq Scan) [consumed] - LEAF
                        Node 9116 (Hash) [consumed]
                          Node 9117 (Seq Scan) [consumed] - LEAF
              Node 9118 (Index Scan) - LEAF
            Node 9119 (Hash)
              Node 9120 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Hash Join -> [Seq Scan (Outer) | f4cb205a | 9114 | 9101, 9102, 9108, 9109, 9110, 9111, 9112, 9113, 9115, 9116, 9117 |
| Hash Join -> [Seq Scan (Outer) | 895c6e8c | 9108 | 9101, 9102, 9109, 9110, 9111, 9112, 9113, 9114, 9115, 9116, 9117 |
| Hash Join -> [Seq Scan (Outer) | 895c6e8c | 9111 | 9101, 9102, 9108, 9109, 9110, 9112, 9113, 9114, 9115, 9116, 9117 |
| Sort -> Aggregate (Outer) | 1d35fb97 | 9101 | 9102, 9108, 9109, 9110, 9111, 9112, 9113, 9114, 9115, 9116, 9117 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 2.67%
- Improvement: 2.69%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 9101 | Sort | 1052.03 | 1080.14 | 2.7% | pattern |
| 9103 | Gather Merge | 1052.01 | 1124.37 | 6.9% | operator |
| 9104 | Aggregate | 1047.15 | 1019.96 | 2.6% | operator |
| 9105 | Sort | 1046.89 | 1074.68 | 2.7% | operator |
| 9106 | Hash Join | 1046.23 | 1107.60 | 5.9% | operator |
| 9107 | Nested Loop | 1034.62 | 1102.78 | 6.6% | operator |
| 9119 | Hash | 3.60 | 14.79 | 310.7% | operator |
| 9108 | Hash Join | 218.76 | 259.82 | 18.8% | pattern |
| 9118 | Index Scan | 0.07 | -0.03 | 134.9% | operator |
| 9120 | Seq Scan | 3.08 | 10.62 | 245.1% | operator |
| 9111 | Hash Join | 35.91 | 84.97 | 136.6% | pattern |
| 9114 | Hash Join | 0.07 | 11.62 | 16494.1% | pattern |

## Prediction Chain (Bottom-Up)

### Step 1: Node 9114 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** f4cb205a (Hash Join -> [Seq Scan (Outer), Hash -> Seq Scan (Outer) (Inner)])
- **Consumes:** Nodes 9101, 9102, 9108, 9109, 9110, 9111, 9112, 9113, 9115, 9116, 9117
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=5
  - HashJoin_nt1=25
  - HashJoin_nt2=1
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=108
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.2000
  - HashJoin_startup_cost=1.0700
  - HashJoin_total_cost=2.4000
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
- **Output:** st=0.12, rt=11.62

### Step 2: Node 9111 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 895c6e8c (Hash Join -> [Seq Scan (Outer), Hash (Inner)])
- **Consumes:** Nodes 9101, 9102, 9108, 9109, 9110, 9112, 9113, 9114, 9115, 9116, 9117
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=12500
  - HashJoin_nt1=62500
  - HashJoin_nt2=5
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=116
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0400
  - HashJoin_startup_cost=2.4600
  - HashJoin_total_cost=4586.8400
  - Hash_Inner_np=0
  - Hash_Inner_nt=5
  - Hash_Inner_nt1=5
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=108
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=2.4000
  - Hash_Inner_total_cost=2.4000
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
- **Output:** st=1.05, rt=84.97

### Step 3: Node 9108 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 895c6e8c (Hash Join -> [Seq Scan (Outer), Hash (Inner)])
- **Consumes:** Nodes 9101, 9102, 9109, 9110, 9111, 9112, 9113, 9114, 9115, 9116, 9117
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=14756
  - HashJoin_nt1=73782
  - HashJoin_nt2=12500
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=116
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0000
  - HashJoin_startup_cost=4743.0900
  - HashJoin_total_cost=38475.3200
  - Hash_Inner_np=0
  - Hash_Inner_nt=12500
  - Hash_Inner_nt1=12500
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=116
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=4586.8400
  - Hash_Inner_total_cost=4586.8400
  - SeqScan_Outer_np=26136
  - SeqScan_Outer_nt=73782
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=8
  - SeqScan_Outer_reltuples=1500000.0000
  - SeqScan_Outer_sel=0.0492
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=33394.0600
- **Output:** st=36.18, rt=259.82

### Step 4: Node 9118 (Index Scan) - LEAF

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

### Step 5: Node 9120 (Seq Scan) - LEAF

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

### Step 6: Node 9107 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=59037
  - nt1=14756
  - nt2=5
  - parallel_workers=0
  - plan_width=128
  - reltuples=0.0000
  - rt1=259.8240
  - rt2=-0.0251
  - sel=0.8002
  - st1=36.1815
  - st2=0.0674
  - startup_cost=4743.5200
  - total_cost=56044.8800
- **Output:** st=42.89, rt=1102.78

### Step 7: Node 9119 (Hash)

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

### Step 8: Node 9106 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2362
  - nt1=59037
  - nt2=10000
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=1102.7838
  - rt2=14.7884
  - sel=0.0000
  - st1=42.8948
  - st2=14.7887
  - startup_cost=5216.5200
  - total_cost=56827.8200
- **Output:** st=49.64, rt=1107.60

### Step 9: Node 9105 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2362
  - nt1=2362
  - nt2=0
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=1107.5991
  - rt2=0.0000
  - sel=1.0000
  - st1=49.6424
  - st2=0.0000
  - startup_cost=56960.1600
  - total_cost=56966.0700
- **Output:** st=1073.76, rt=1074.68

### Step 10: Node 9104 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=2362
  - nt2=0
  - parallel_workers=0
  - plan_width=136
  - reltuples=0.0000
  - rt1=1074.6840
  - rt2=0.0000
  - sel=0.0106
  - st1=1073.7612
  - st2=0.0000
  - startup_cost=56960.1600
  - total_cost=56990.0000
- **Output:** st=1017.92, rt=1019.96

### Step 11: Node 9103 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=75
  - nt1=25
  - nt2=0
  - parallel_workers=3
  - plan_width=136
  - reltuples=0.0000
  - rt1=1019.9556
  - rt2=0.0000
  - sel=3.0000
  - st1=1017.9236
  - st2=0.0000
  - startup_cost=57960.2000
  - total_cost=57998.8500
- **Output:** st=1121.35, rt=1124.37

### Step 12: Node 9101 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 1d35fb97 (Sort -> Aggregate (Outer))
- **Consumes:** Nodes 9102, 9108, 9109, 9110, 9111, 9112, 9113, 9114, 9115, 9116, 9117
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=25
  - Aggregate_Outer_nt1=75
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=136
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.3333
  - Aggregate_Outer_startup_cost=57960.2000
  - Aggregate_Outer_total_cost=57999.7300
  - Sort_np=0
  - Sort_nt=25
  - Sort_nt1=25
  - Sort_nt2=0
  - Sort_parallel_workers=0
  - Sort_plan_width=136
  - Sort_reltuples=0.0000
  - Sort_sel=1.0000
  - Sort_startup_cost=58000.3100
  - Sort_total_cost=58000.3700
- **Output:** st=1078.45, rt=1080.14
