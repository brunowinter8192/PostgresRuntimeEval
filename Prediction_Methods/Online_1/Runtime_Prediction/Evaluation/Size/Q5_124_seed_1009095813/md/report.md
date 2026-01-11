# Online Prediction Report

**Test Query:** Q5_124_seed_1009095813
**Timestamp:** 2026-01-11 17:01:12

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 6.08%

## Phase C: Patterns in Query

- Total Patterns: 85

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 33781.0% | 113504.2307 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 172 | 3565.0% | 6131.8766 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| 3e2d5a00 | Sort -> Hash Join (Outer) | 2 | 96 | 19.3% | 18.5586 |
| 3754655c | Aggregate -> Sort (Outer) | 2 | 48 | 4.4% | 2.1302 |
| 46f37744 | Gather Merge -> Aggregate (Outer) | 2 | 48 | 5.9% | 2.8144 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 75.1% | 108.1438 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 140 | 4.5% | 6.2375 |
| 8a8c43c6 | Aggregate -> Gather Merge -> Aggregate (... | 3 | 48 | 3.2% | 1.5375 |
| ddb1e0ca | Sort -> Aggregate -> Gather Merge (Outer... | 3 | 48 | 28.5% | 13.6847 |
| e6c1e0d8 | Gather Merge -> Aggregate -> Sort (Outer... | 3 | 48 | 5.9% | 2.8144 |
| 8823d1e5 | Aggregate -> Sort -> Hash Join (Outer) (... | 3 | 24 | 4.8% | 1.1588 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 168 | 44967.0% | 75544.5822 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 148 | 116.8% | 172.9284 |
| c0a8d3de | Hash -> Hash Join -> [Seq Scan (Outer), ... | 3 | 148 | 4130.8% | 6113.5159 |
| 91d6e559 | Sort -> Hash Join -> [Nested Loop (Outer... | 3 | 72 | 5.4% | 3.8546 |
| 460af52c | Aggregate -> Gather Merge -> Aggregate -... | 4 | 48 | 3.2% | 1.5375 |
| 39e55ae2 | Gather Merge -> Aggregate -> Sort -> Has... | 4 | 24 | 5.0% | 1.1935 |
| 627c5619 | Sort -> Aggregate -> Gather Merge -> Agg... | 4 | 24 | 3.6% | 0.8575 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 116 | 3.5% | 4.0772 |
| a54055ce | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 96 | 6342.9% | 6089.1983 |
| 444761fb | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 52 | 46.8% | 24.3176 |
| 7014b260 | Sort -> Aggregate -> Gather Merge -> Agg... | 5 | 24 | 3.6% | 0.8575 |
| 94adff2c | Aggregate -> Sort -> Hash Join -> [Neste... | 4 | 24 | 4.8% | 1.1588 |
| c42cb45a | Aggregate -> Gather Merge -> Aggregate -... | 5 | 24 | 1.8% | 0.4402 |
| 37515ad8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 124 | 135.7% | 168.3286 |
| bd9dfa7b | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 92 | 3.7% | 3.3601 |
| 2422d111 | Hash Join -> [Nested Loop -> [Hash Join ... | 3 | 72 | 15.0% | 10.7757 |
| 14a1f63a | Gather Merge -> Aggregate -> Sort -> Has... | 5 | 24 | 5.0% | 1.1935 |
| 6815cf8d | Sort -> Aggregate -> Gather Merge -> Agg... | 6 | 24 | 3.6% | 0.8575 |
| 545b5e57 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 72 | 212.7% | 153.1732 |
| ec92bdaa | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 52 | 29.1% | 15.1555 |
| 12e6457c | Sort -> Hash Join -> [Nested Loop -> [Ha... | 4 | 48 | 6.0% | 2.9009 |
| 314469b0 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 5 | 48 | 43.2% | 20.7410 |
| 729d307d | Aggregate -> Gather Merge -> Aggregate -... | 6 | 24 | 1.8% | 0.4402 |
| 9d0e407c | Nested Loop -> [Hash Join -> [Seq Scan (... | 5 | 72 | 4.1% | 2.9587 |
| 4db07220 | Hash Join -> [Nested Loop -> [Hash Join ... | 4 | 48 | 12.3% | 5.9049 |
| 54cb7f90 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 6 | 48 | 43.2% | 20.7410 |
| 3a31b48f | Aggregate -> Sort -> Hash Join -> [Neste... | 5 | 24 | 4.8% | 1.1588 |
| bf4763ca | Sort -> Aggregate -> Gather Merge -> Agg... | 7 | 24 | 3.6% | 0.8575 |
| 440e6274 | Hash Join -> [Nested Loop -> [Hash Join ... | 5 | 48 | 12.3% | 5.9049 |
| 5bfce159 | Nested Loop -> [Hash Join -> [Seq Scan (... | 6 | 48 | 4.4% | 2.1340 |
| e1d7e5b4 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 48 | 27.6% | 13.2381 |
| 843b7fef | Gather Merge -> Aggregate -> Sort -> Has... | 6 | 24 | 5.0% | 1.1935 |
| 91ed3a4f | Sort -> Hash Join -> [Nested Loop -> [Ha... | 5 | 24 | 1.9% | 0.4506 |
| c302739b | Hash Join -> [Seq Scan (Outer), Hash -> ... | 7 | 48 | 27.6% | 13.2381 |
| 0fa21834 | Aggregate -> Sort -> Hash Join -> [Neste... | 6 | 24 | 4.8% | 1.1588 |
| 8757732f | Aggregate -> Gather Merge -> Aggregate -... | 7 | 24 | 1.8% | 0.4402 |
| d25d9b9f | Sort -> Hash Join -> [Nested Loop -> [Ha... | 6 | 24 | 1.9% | 0.4506 |
| ef93d4fc | Nested Loop -> [Hash Join -> [Seq Scan (... | 7 | 48 | 4.4% | 2.1340 |
| f4603221 | Hash Join -> [Nested Loop -> [Hash Join ... | 6 | 48 | 12.3% | 5.9049 |
| 4de97842 | Aggregate -> Sort -> Hash Join -> [Neste... | 7 | 24 | 4.8% | 1.1588 |
| 739b1b7e | Gather Merge -> Aggregate -> Sort -> Has... | 7 | 24 | 5.0% | 1.1935 |
| 9b0e5572 | Sort -> Aggregate -> Gather Merge -> Agg... | 8 | 24 | 3.6% | 0.8575 |
| 3d4c3db9 | Hash Join -> [Nested Loop -> [Hash Join ... | 7 | 48 | 12.3% | 5.9049 |
| 5ae97df8 | Nested Loop -> [Hash Join -> [Seq Scan (... | 8 | 48 | 4.4% | 2.1340 |
| 00dd2f10 | Aggregate -> Gather Merge -> Aggregate -... | 8 | 24 | 1.8% | 0.4402 |
| 2dc34d1b | Sort -> Hash Join -> [Nested Loop -> [Ha... | 7 | 24 | 1.9% | 0.4506 |
| f169a84a | Gather Merge -> Aggregate -> Sort -> Has... | 8 | 24 | 5.0% | 1.1935 |
| 421ce908 | Aggregate -> Sort -> Hash Join -> [Neste... | 8 | 24 | 4.8% | 1.1588 |
| 45e3e43d | Aggregate -> Gather Merge -> Aggregate -... | 9 | 24 | 1.8% | 0.4402 |
| 5a24af68 | Sort -> Aggregate -> Gather Merge -> Agg... | 9 | 24 | 3.6% | 0.8575 |
| 5f022f0d | Sort -> Hash Join -> [Nested Loop -> [Ha... | 8 | 24 | 1.9% | 0.4506 |
| 9ce781b0 | Hash Join -> [Nested Loop -> [Hash Join ... | 8 | 48 | 12.3% | 5.9049 |
| 9325c19d | Aggregate -> Sort -> Hash Join -> [Neste... | 9 | 24 | 4.8% | 1.1588 |
| ac1e65be | Gather Merge -> Aggregate -> Sort -> Has... | 9 | 24 | 5.0% | 1.1935 |
| b20b9f6a | Sort -> Aggregate -> Gather Merge -> Agg... | 10 | 24 | 3.6% | 0.8575 |
| a95bee4e | Hash Join -> [Nested Loop -> [Hash Join ... | 9 | 48 | 12.3% | 5.9049 |
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
| 0 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 1 | 1d35fb97 | 26.4017 | 0.1167% | ACCEPTED | 17.81% |
| 2 | 7df893ad | 6131.8766 | 0.0000% | ACCEPTED | 17.81% |
| 3 | 2724c080 | 19.6008 | 0.0346% | ACCEPTED | 17.77% |
| 4 | 3e2d5a00 | 18.5586 | N/A | REJECTED | 17.77% |
| 5 | 3754655c | 2.1302 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 6 | 46f37744 | 2.8144 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 7 | 895c6e8c | 75736.1626 | 0.0001% | ACCEPTED | 17.77% |
| 8 | 2e0f44ef | 108.1438 | N/A | REJECTED | 17.77% |
| 9 | 3cfa90d7 | 6.2375 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 10 | 8a8c43c6 | 1.5375 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 11 | ddb1e0ca | 13.6847 | -5.4908% | REJECTED | 17.77% |
| 12 | e6c1e0d8 | 2.8144 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 13 | 8823d1e5 | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 14 | f4cb205a | 75544.5822 | 0.0005% | ACCEPTED | 17.77% |
| 15 | bb930825 | 172.9284 | N/A | REJECTED | 17.77% |
| 16 | c0a8d3de | 6113.5159 | N/A | REJECTED | 17.77% |
| 17 | 91d6e559 | 3.8546 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 18 | 460af52c | 1.5375 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 19 | 39e55ae2 | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 20 | 627c5619 | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 21 | e0e3c3e1 | 4.0772 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 22 | a54055ce | 6089.1983 | N/A | REJECTED | 17.77% |
| 23 | 444761fb | 24.3176 | N/A | REJECTED | 17.77% |
| 24 | 7014b260 | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 25 | 94adff2c | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 26 | c42cb45a | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 27 | 37515ad8 | 168.3286 | N/A | REJECTED | 17.77% |
| 28 | bd9dfa7b | 3.3601 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 29 | 2422d111 | 10.7757 | N/A | REJECTED | 17.77% |
| 30 | 14a1f63a | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 31 | 6815cf8d | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 32 | 545b5e57 | 153.1732 | N/A | REJECTED | 17.77% |
| 33 | ec92bdaa | 15.1555 | N/A | REJECTED | 17.77% |
| 34 | 12e6457c | 2.9009 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 35 | 314469b0 | 20.7410 | N/A | REJECTED | 17.77% |
| 36 | 729d307d | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 37 | 9d0e407c | 2.9587 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 38 | 4db07220 | 5.9049 | N/A | REJECTED | 17.77% |
| 39 | 54cb7f90 | 20.7410 | N/A | REJECTED | 17.77% |
| 40 | 3a31b48f | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 41 | bf4763ca | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 42 | 440e6274 | 5.9049 | N/A | REJECTED | 17.77% |
| 43 | 5bfce159 | 2.1340 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 44 | e1d7e5b4 | 13.2381 | N/A | REJECTED | 17.77% |
| 45 | 843b7fef | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 46 | 91ed3a4f | 0.4506 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 47 | c302739b | 13.2381 | N/A | REJECTED | 17.77% |
| 48 | 0fa21834 | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 49 | 8757732f | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 50 | d25d9b9f | 0.4506 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 51 | ef93d4fc | 2.1340 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 52 | f4603221 | 5.9049 | N/A | REJECTED | 17.77% |
| 53 | 4de97842 | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 54 | 739b1b7e | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 55 | 9b0e5572 | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 56 | 3d4c3db9 | 5.9049 | N/A | REJECTED | 17.77% |
| 57 | 5ae97df8 | 2.1340 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 58 | 00dd2f10 | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 59 | 2dc34d1b | 0.4506 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 60 | f169a84a | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 61 | 421ce908 | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 62 | 45e3e43d | 0.4402 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 63 | 5a24af68 | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 64 | 5f022f0d | 0.4506 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 65 | 9ce781b0 | 5.9049 | N/A | REJECTED | 17.77% |
| 66 | 9325c19d | 1.1588 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 67 | ac1e65be | 1.1935 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 68 | b20b9f6a | 0.8575 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 69 | a95bee4e | 5.9049 | N/A | REJECTED | 17.77% |
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
Node 7421 (Sort) [PATTERN: 1d35fb97] - ROOT
  Node 7422 (Aggregate) [consumed]
    Node 7423 (Gather Merge)
      Node 7424 (Aggregate)
        Node 7425 (Sort)
          Node 7426 (Hash Join)
            Node 7427 (Nested Loop)
              Node 7428 (Hash Join)
                Node 7429 (Seq Scan) - LEAF
                Node 7430 (Hash) [PATTERN: 7df893ad]
                  Node 7431 (Hash Join) [consumed]
                    Node 7432 (Seq Scan) - LEAF
                    Node 7433 (Hash)
                      Node 7434 (Hash Join) [PATTERN: f4cb205a]
                        Node 7435 (Seq Scan) [consumed] - LEAF
                        Node 7436 (Hash) [consumed]
                          Node 7437 (Seq Scan) [consumed] - LEAF
              Node 7438 (Index Scan) - LEAF
            Node 7439 (Hash)
              Node 7440 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Hash Join -> [Seq Scan (Outer) | f4cb205a | 7434 | 7421, 7422, 7430, 7431, 7435, 7436, 7437 |
| Sort -> Aggregate (Outer) | 1d35fb97 | 7421 | 7422, 7430, 7431, 7434, 7435, 7436, 7437 |
| Hash -> Hash Join (Outer) | 7df893ad | 7430 | 7421, 7422, 7431, 7434, 7435, 7436, 7437 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 3.38%
- Improvement: 2.71%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 7421 | Sort | 1044.84 | 1080.12 | 3.4% | pattern |
| 7423 | Gather Merge | 1044.82 | 1124.38 | 7.6% | operator |
| 7424 | Aggregate | 1040.07 | 1020.00 | 1.9% | operator |
| 7425 | Sort | 1039.82 | 1074.63 | 3.3% | operator |
| 7426 | Hash Join | 1039.36 | 1106.70 | 6.5% | operator |
| 7427 | Nested Loop | 1028.03 | 1102.47 | 7.2% | operator |
| 7439 | Hash | 3.35 | 14.79 | 341.1% | operator |
| 7428 | Hash Join | 209.59 | 234.53 | 11.9% | operator |
| 7438 | Index Scan | 0.07 | -0.03 | 134.9% | operator |
| 7440 | Seq Scan | 2.82 | 10.62 | 276.1% | operator |
| 7429 | Seq Scan | 165.24 | 161.95 | 2.0% | operator |
| 7430 | Hash | 31.61 | 39.26 | 24.2% | pattern |
| 7432 | Seq Scan | 29.26 | 24.87 | 15.0% | operator |
| 7433 | Hash | 0.15 | 14.60 | 9383.0% | operator |
| 7434 | Hash Join | 0.15 | 11.62 | 7592.6% | pattern |

## Prediction Chain (Bottom-Up)

### Step 1: Node 7434 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** f4cb205a (Hash Join -> [Seq Scan (Outer), Hash -> Seq Scan (Outer) (Inner)])
- **Consumes:** Nodes 7421, 7422, 7430, 7431, 7435, 7436, 7437
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

### Step 2: Node 7432 (Seq Scan) - LEAF

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

### Step 3: Node 7433 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=5
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=11.6159
  - rt2=0.0000
  - sel=1.0000
  - st1=0.1239
  - st2=0.0000
  - startup_cost=2.4000
  - total_cost=2.4000
- **Output:** st=14.60, rt=14.60

### Step 4: Node 7429 (Seq Scan) - LEAF

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

### Step 5: Node 7430 (Hash) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 7df893ad (Hash -> Hash Join (Outer))
- **Consumes:** Nodes 7421, 7422, 7431, 7434, 7435, 7436, 7437
- **Input Features:**
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=12500
  - HashJoin_Outer_nt1=62500
  - HashJoin_Outer_nt2=5
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=116
  - HashJoin_Outer_reltuples=0.0000
  - HashJoin_Outer_sel=0.0400
  - HashJoin_Outer_startup_cost=2.4600
  - HashJoin_Outer_total_cost=4586.8400
  - Hash_np=0
  - Hash_nt=12500
  - Hash_nt1=12500
  - Hash_nt2=0
  - Hash_parallel_workers=0
  - Hash_plan_width=116
  - Hash_reltuples=0.0000
  - Hash_sel=1.0000
  - Hash_startup_cost=4586.8400
  - Hash_total_cost=4586.8400
- **Output:** st=39.26, rt=39.26

### Step 6: Node 7428 (Hash Join)

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
  - rt2=39.2568
  - sel=0.0000
  - st1=0.1786
  - st2=39.2558
  - startup_cost=4743.0900
  - total_cost=38472.8000
- **Output:** st=25.02, rt=234.53

### Step 7: Node 7438 (Index Scan) - LEAF

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

### Step 8: Node 7440 (Seq Scan) - LEAF

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

### Step 9: Node 7427 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=58597
  - nt1=14646
  - nt2=5
  - parallel_workers=0
  - plan_width=128
  - reltuples=0.0000
  - rt1=234.5310
  - rt2=-0.0251
  - sel=0.8002
  - st1=25.0227
  - st2=0.0674
  - startup_cost=4743.5200
  - total_cost=55979.7800
- **Output:** st=42.51, rt=1102.47

### Step 10: Node 7439 (Hash)

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

### Step 11: Node 7426 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2344
  - nt1=58597
  - nt2=10000
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=1102.4684
  - rt2=14.7884
  - sel=0.0000
  - st1=42.5100
  - st2=14.7887
  - startup_cost=5216.5200
  - total_cost=56760.4200
- **Output:** st=49.39, rt=1106.70

### Step 12: Node 7425 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2344
  - nt1=2344
  - nt2=0
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=1106.6955
  - rt2=0.0000
  - sel=1.0000
  - st1=49.3874
  - st2=0.0000
  - startup_cost=56891.6200
  - total_cost=56897.4800
- **Output:** st=1073.70, rt=1074.63

### Step 13: Node 7424 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=2344
  - nt2=0
  - parallel_workers=0
  - plan_width=136
  - reltuples=0.0000
  - rt1=1074.6268
  - rt2=0.0000
  - sel=0.0107
  - st1=1073.7045
  - st2=0.0000
  - startup_cost=56891.6200
  - total_cost=56921.2300
- **Output:** st=1017.96, rt=1020.00

### Step 14: Node 7423 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=75
  - nt1=25
  - nt2=0
  - parallel_workers=3
  - plan_width=136
  - reltuples=0.0000
  - rt1=1019.9970
  - rt2=0.0000
  - sel=3.0000
  - st1=1017.9626
  - st2=0.0000
  - startup_cost=57891.6600
  - total_cost=57930.0800
- **Output:** st=1121.36, rt=1124.38

### Step 15: Node 7421 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 1d35fb97 (Sort -> Aggregate (Outer))
- **Consumes:** Nodes 7422, 7430, 7431, 7434, 7435, 7436, 7437
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=25
  - Aggregate_Outer_nt1=75
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=136
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.3333
  - Aggregate_Outer_startup_cost=57891.6600
  - Aggregate_Outer_total_cost=57930.9600
  - Sort_np=0
  - Sort_nt=25
  - Sort_nt1=25
  - Sort_nt2=0
  - Sort_parallel_workers=0
  - Sort_plan_width=136
  - Sort_reltuples=0.0000
  - Sort_sel=1.0000
  - Sort_startup_cost=57931.5400
  - Sort_total_cost=57931.6000
- **Output:** st=1078.44, rt=1080.12
