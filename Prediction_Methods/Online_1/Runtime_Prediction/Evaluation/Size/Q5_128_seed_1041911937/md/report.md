# Online Prediction Report

**Test Query:** Q5_128_seed_1041911937
**Timestamp:** 2026-01-01 18:17:56

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
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 33781.0% | 113504.2307 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 172 | 3565.0% | 6131.8766 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 75.1% | 108.1438 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 140 | 4.5% | 6.2375 |
| 3e2d5a00 | Sort -> Hash Join (Outer) | 2 | 96 | 19.3% | 18.5586 |
| 46f37744 | Gather Merge -> Aggregate (Outer) | 2 | 48 | 5.9% | 2.8144 |
| 3754655c | Aggregate -> Sort (Outer) | 2 | 48 | 4.4% | 2.1302 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 168 | 44967.0% | 75544.5822 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 148 | 116.8% | 172.9284 |
| c0a8d3de | Hash -> Hash Join -> [Seq Scan (Outer), ... | 3 | 148 | 4130.8% | 6113.5159 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 116 | 3.5% | 4.0772 |
| 91d6e559 | Sort -> Hash Join -> [Nested Loop (Outer... | 3 | 72 | 5.4% | 3.8546 |
| 2422d111 | Hash Join -> [Nested Loop -> [Hash Join ... | 3 | 72 | 15.0% | 10.7757 |
| ddb1e0ca | Sort -> Aggregate -> Gather Merge (Outer... | 3 | 48 | 28.5% | 13.6847 |
| 8a8c43c6 | Aggregate -> Gather Merge -> Aggregate (... | 3 | 48 | 3.2% | 1.5375 |
| e6c1e0d8 | Gather Merge -> Aggregate -> Sort (Outer... | 3 | 48 | 5.9% | 2.8144 |
| 8823d1e5 | Aggregate -> Sort -> Hash Join (Outer) (... | 3 | 24 | 4.8% | 1.1588 |
| 37515ad8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 124 | 135.7% | 168.3286 |
| a54055ce | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 96 | 6342.9% | 6089.1983 |
| bd9dfa7b | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 92 | 3.7% | 3.3601 |
| 444761fb | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 52 | 46.8% | 24.3176 |
| 460af52c | Aggregate -> Gather Merge -> Aggregate -... | 4 | 48 | 3.2% | 1.5375 |
| 12e6457c | Sort -> Hash Join -> [Nested Loop -> [Ha... | 4 | 48 | 6.0% | 2.9009 |
| 4db07220 | Hash Join -> [Nested Loop -> [Hash Join ... | 4 | 48 | 12.3% | 5.9049 |
| 627c5619 | Sort -> Aggregate -> Gather Merge -> Agg... | 4 | 24 | 3.6% | 0.8575 |
| 39e55ae2 | Gather Merge -> Aggregate -> Sort -> Has... | 4 | 24 | 5.0% | 1.1935 |
| 94adff2c | Aggregate -> Sort -> Hash Join -> [Neste... | 4 | 24 | 4.8% | 1.1588 |
| 9d0e407c | Nested Loop -> [Hash Join -> [Seq Scan (... | 5 | 72 | 4.1% | 2.9587 |
| 545b5e57 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 72 | 212.7% | 153.1732 |
| ec92bdaa | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 52 | 29.1% | 15.1555 |
| 440e6274 | Hash Join -> [Nested Loop -> [Hash Join ... | 5 | 48 | 12.3% | 5.9049 |
| 314469b0 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 5 | 48 | 43.2% | 20.7410 |
| 7014b260 | Sort -> Aggregate -> Gather Merge -> Agg... | 5 | 24 | 3.6% | 0.8575 |
| c42cb45a | Aggregate -> Gather Merge -> Aggregate -... | 5 | 24 | 1.8% | 0.4402 |
| 14a1f63a | Gather Merge -> Aggregate -> Sort -> Has... | 5 | 24 | 5.0% | 1.1935 |
| 3a31b48f | Aggregate -> Sort -> Hash Join -> [Neste... | 5 | 24 | 4.8% | 1.1588 |
| 91ed3a4f | Sort -> Hash Join -> [Nested Loop -> [Ha... | 5 | 24 | 1.9% | 0.4506 |
| f4603221 | Hash Join -> [Nested Loop -> [Hash Join ... | 6 | 48 | 12.3% | 5.9049 |
| 5bfce159 | Nested Loop -> [Hash Join -> [Seq Scan (... | 6 | 48 | 4.4% | 2.1340 |
| e1d7e5b4 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 48 | 27.6% | 13.2381 |
| 54cb7f90 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 6 | 48 | 43.2% | 20.7410 |
| 6815cf8d | Sort -> Aggregate -> Gather Merge -> Agg... | 6 | 24 | 3.6% | 0.8575 |
| 729d307d | Aggregate -> Gather Merge -> Aggregate -... | 6 | 24 | 1.8% | 0.4402 |
| 843b7fef | Gather Merge -> Aggregate -> Sort -> Has... | 6 | 24 | 5.0% | 1.1935 |
| 0fa21834 | Aggregate -> Sort -> Hash Join -> [Neste... | 6 | 24 | 4.8% | 1.1588 |
| d25d9b9f | Sort -> Hash Join -> [Nested Loop -> [Ha... | 6 | 24 | 1.9% | 0.4506 |
| 3d4c3db9 | Hash Join -> [Nested Loop -> [Hash Join ... | 7 | 48 | 12.3% | 5.9049 |
| ef93d4fc | Nested Loop -> [Hash Join -> [Seq Scan (... | 7 | 48 | 4.4% | 2.1340 |
| c302739b | Hash Join -> [Seq Scan (Outer), Hash -> ... | 7 | 48 | 27.6% | 13.2381 |
| bf4763ca | Sort -> Aggregate -> Gather Merge -> Agg... | 7 | 24 | 3.6% | 0.8575 |
| 8757732f | Aggregate -> Gather Merge -> Aggregate -... | 7 | 24 | 1.8% | 0.4402 |
| 739b1b7e | Gather Merge -> Aggregate -> Sort -> Has... | 7 | 24 | 5.0% | 1.1935 |
| 4de97842 | Aggregate -> Sort -> Hash Join -> [Neste... | 7 | 24 | 4.8% | 1.1588 |
| 2dc34d1b | Sort -> Hash Join -> [Nested Loop -> [Ha... | 7 | 24 | 1.9% | 0.4506 |
| 9ce781b0 | Hash Join -> [Nested Loop -> [Hash Join ... | 8 | 48 | 12.3% | 5.9049 |
| 5ae97df8 | Nested Loop -> [Hash Join -> [Seq Scan (... | 8 | 48 | 4.4% | 2.1340 |
| 9b0e5572 | Sort -> Aggregate -> Gather Merge -> Agg... | 8 | 24 | 3.6% | 0.8575 |
| 00dd2f10 | Aggregate -> Gather Merge -> Aggregate -... | 8 | 24 | 1.8% | 0.4402 |
| f169a84a | Gather Merge -> Aggregate -> Sort -> Has... | 8 | 24 | 5.0% | 1.1935 |
| 421ce908 | Aggregate -> Sort -> Hash Join -> [Neste... | 8 | 24 | 4.8% | 1.1588 |
| 5f022f0d | Sort -> Hash Join -> [Nested Loop -> [Ha... | 8 | 24 | 1.9% | 0.4506 |
| a95bee4e | Hash Join -> [Nested Loop -> [Hash Join ... | 9 | 48 | 12.3% | 5.9049 |
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
| 0 | 895c6e8c | 75736.1626 | 0.0004% | ACCEPTED | 17.92% |
| 1 | 3aab37be | 94712.4752 | -0.0000% | REJECTED | 17.92% |
| 2 | 1d35fb97 | 26.4006 | 0.1163% | ACCEPTED | 17.81% |
| 3 | 7df893ad | 678.6757 | N/A | REJECTED | 17.81% |
| 4 | 2724c080 | 7.7852 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 5 | 2e0f44ef | 108.1433 | 0.0001% | ACCEPTED | 17.81% |
| 6 | 3cfa90d7 | 3.5091 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 7 | 3e2d5a00 | 18.3526 | N/A | REJECTED | 17.81% |
| 8 | 46f37744 | 2.8145 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 9 | 3754655c | 2.1224 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 10 | f4cb205a | 41652.9228 | 0.0005% | ACCEPTED | 17.81% |
| 11 | bb930825 | 188.3060 | N/A | REJECTED | 17.81% |
| 12 | e0e3c3e1 | 2.9552 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 13 | 91d6e559 | 3.6292 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 14 | 2422d111 | 1.5987 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 15 | ddb1e0ca | 13.5374 | -5.4908% | REJECTED | 17.81% |
| 16 | 8a8c43c6 | 2.1945 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 17 | e6c1e0d8 | 2.8145 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 18 | 8823d1e5 | 1.1511 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 19 | 37515ad8 | 180.6991 | N/A | REJECTED | 17.81% |
| 20 | bd9dfa7b | 1.7976 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 21 | 460af52c | 2.1945 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 22 | 12e6457c | 2.7493 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 23 | 4db07220 | 1.1101 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 24 | 627c5619 | 0.4253 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 25 | 39e55ae2 | 1.1936 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 26 | 94adff2c | 1.1511 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 27 | 545b5e57 | 159.7788 | N/A | REJECTED | 17.81% |
| 28 | ec92bdaa | 20.9203 | N/A | REJECTED | 17.81% |
| 29 | 440e6274 | 1.1101 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 30 | 7014b260 | 0.4253 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 31 | 14a1f63a | 1.1936 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 32 | 3a31b48f | 1.1511 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 33 | 91ed3a4f | 0.4938 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 34 | f4603221 | 1.1101 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 35 | e1d7e5b4 | 18.3306 | N/A | REJECTED | 17.81% |
| 36 | 6815cf8d | 0.4253 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 37 | 843b7fef | 1.1936 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 38 | 0fa21834 | 1.1511 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 39 | d25d9b9f | 0.4938 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 40 | 3d4c3db9 | 1.1101 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 41 | c302739b | 18.3306 | N/A | REJECTED | 17.81% |
| 42 | bf4763ca | 0.4253 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 43 | 739b1b7e | 1.1936 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 44 | 4de97842 | 1.1511 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 45 | 2dc34d1b | 0.4938 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 46 | 9ce781b0 | 1.1101 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 47 | 9b0e5572 | 0.4253 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 48 | f169a84a | 1.1936 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 49 | 421ce908 | 1.1511 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 50 | 5f022f0d | 0.4938 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 51 | a95bee4e | 1.1101 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 52 | 5a24af68 | 0.4253 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 53 | ac1e65be | 1.1936 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 54 | 9325c19d | 1.1511 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 55 | 0e38b2d0 | 0.4938 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 56 | b20b9f6a | 0.4253 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 57 | 6255ff62 | 1.1936 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 58 | 7b82db07 | 1.1511 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 59 | 45767427 | 0.4938 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 60 | d21d6eb9 | 0.4253 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 61 | 8b7a3d08 | 1.1936 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 62 | 7d401e23 | 1.1511 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 63 | 255215ee | 0.4253 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 64 | 1b84acf9 | 1.1936 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 65 | d959dddb | 0.4253 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 66 | de57e0e8 | 0.4253 | N/A | SKIPPED_LOW_ERROR | 17.81% |
## Query Tree

```
Node 7501 (Sort) [PATTERN: 1d35fb97] - ROOT
  Node 7502 (Aggregate) [consumed]
    Node 7503 (Gather Merge)
      Node 7504 (Aggregate)
        Node 7505 (Sort)
          Node 7506 (Hash Join) [PATTERN: 2e0f44ef]
            Node 7507 (Nested Loop) [consumed]
              Node 7508 (Hash Join) [PATTERN: 895c6e8c]
                Node 7509 (Seq Scan) [consumed] - LEAF
                Node 7510 (Hash) [consumed]
                  Node 7511 (Hash Join) [PATTERN: 895c6e8c]
                    Node 7512 (Seq Scan) [consumed] - LEAF
                    Node 7513 (Hash) [consumed]
                      Node 7514 (Hash Join) [PATTERN: f4cb205a]
                        Node 7515 (Seq Scan) [consumed] - LEAF
                        Node 7516 (Hash) [consumed]
                          Node 7517 (Seq Scan) [consumed] - LEAF
              Node 7518 (Index Scan) - LEAF
            Node 7519 (Hash) [consumed]
              Node 7520 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Hash Join -> [Seq Scan (Outer) | f4cb205a | 7514 | 7501, 7502, 7506, 7507, 7508, 7509, 7510, 7511, 7512, 7513, 7515, 7516, 7517, 7519 |
| Hash Join -> [Seq Scan (Outer) | 895c6e8c | 7508 | 7501, 7502, 7506, 7507, 7509, 7510, 7511, 7512, 7513, 7514, 7515, 7516, 7517, 7519 |
| Hash Join -> [Seq Scan (Outer) | 895c6e8c | 7511 | 7501, 7502, 7506, 7507, 7508, 7509, 7510, 7512, 7513, 7514, 7515, 7516, 7517, 7519 |
| Sort -> Aggregate (Outer) | 1d35fb97 | 7501 | 7502, 7506, 7507, 7508, 7509, 7510, 7511, 7512, 7513, 7514, 7515, 7516, 7517, 7519 |
| Hash Join -> [Nested Loop (Out | 2e0f44ef | 7506 | 7501, 7502, 7507, 7508, 7509, 7510, 7511, 7512, 7513, 7514, 7515, 7516, 7517, 7519 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 0.59%
- Improvement: 2.63%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 7501 | Sort | 1073.80 | 1080.12 | 0.6% | pattern |
| 7503 | Gather Merge | 1073.78 | 1124.38 | 4.7% | operator |
| 7504 | Aggregate | 1069.38 | 1019.75 | 4.6% | operator |
| 7505 | Sort | 1069.09 | 1073.09 | 0.4% | operator |
| 7506 | Hash Join | 1068.61 | 1080.14 | 1.1% | pattern |
| 7508 | Hash Join | 216.95 | 259.84 | 19.8% | pattern |
| 7518 | Index Scan | 0.07 | -0.03 | 133.9% | operator |
| 7520 | Seq Scan | 3.02 | 10.62 | 251.9% | operator |
| 7511 | Hash Join | 36.88 | 84.97 | 130.4% | pattern |
| 7514 | Hash Join | 0.18 | 11.62 | 6282.3% | pattern |

## Prediction Chain (Bottom-Up)

### Step 1: Node 7514 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** f4cb205a (Hash Join -> [Seq Scan (Outer), Hash -> Seq Scan (Outer) (Inner)])
- **Consumes:** Nodes 7501, 7502, 7506, 7507, 7508, 7509, 7510, 7511, 7512, 7513, 7515, 7516, 7517, 7519
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

### Step 2: Node 7511 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 895c6e8c (Hash Join -> [Seq Scan (Outer), Hash (Inner)])
- **Consumes:** Nodes 7501, 7502, 7506, 7507, 7508, 7509, 7510, 7512, 7513, 7514, 7515, 7516, 7517, 7519
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

### Step 3: Node 7508 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 895c6e8c (Hash Join -> [Seq Scan (Outer), Hash (Inner)])
- **Consumes:** Nodes 7501, 7502, 7506, 7507, 7509, 7510, 7511, 7512, 7513, 7514, 7515, 7516, 7517, 7519
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=14646
  - HashJoin_nt1=73231
  - HashJoin_nt2=12500
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=116
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0000
  - HashJoin_startup_cost=4743.0900
  - HashJoin_total_cost=38472.8000
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
  - SeqScan_Outer_nt=73231
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=8
  - SeqScan_Outer_reltuples=1500000.0000
  - SeqScan_Outer_sel=0.0488
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=33394.0600
- **Output:** st=36.18, rt=259.84

### Step 4: Node 7518 (Index Scan) - LEAF

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

### Step 5: Node 7520 (Seq Scan) - LEAF

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

### Step 6: Node 7506 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 2e0f44ef (Hash Join -> [Nested Loop (Outer), Hash (Inner)])
- **Consumes:** Nodes 7501, 7502, 7507, 7508, 7509, 7510, 7511, 7512, 7513, 7514, 7515, 7516, 7517, 7519
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=2344
  - HashJoin_nt1=58597
  - HashJoin_nt2=10000
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=116
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0000
  - HashJoin_startup_cost=5216.5200
  - HashJoin_total_cost=56760.4200
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
  - NestedLoop_Outer_nt=58597
  - NestedLoop_Outer_nt1=14646
  - NestedLoop_Outer_nt2=5
  - NestedLoop_Outer_parallel_workers=0
  - NestedLoop_Outer_plan_width=128
  - NestedLoop_Outer_reltuples=0.0000
  - NestedLoop_Outer_sel=0.8002
  - NestedLoop_Outer_startup_cost=4743.5200
  - NestedLoop_Outer_total_cost=55979.7800
- **Output:** st=41.66, rt=1080.14

### Step 7: Node 7505 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2344
  - nt1=2344
  - nt2=0
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=1080.1362
  - rt2=0.0000
  - sel=1.0000
  - st1=41.6608
  - st2=0.0000
  - startup_cost=56891.6200
  - total_cost=56897.4800
- **Output:** st=1072.18, rt=1073.09

### Step 8: Node 7504 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=2344
  - nt2=0
  - parallel_workers=0
  - plan_width=136
  - reltuples=0.0000
  - rt1=1073.0942
  - rt2=0.0000
  - sel=0.0107
  - st1=1072.1791
  - st2=0.0000
  - startup_cost=56891.6200
  - total_cost=56921.2300
- **Output:** st=1017.78, rt=1019.75

### Step 9: Node 7503 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=75
  - nt1=25
  - nt2=0
  - parallel_workers=3
  - plan_width=136
  - reltuples=0.0000
  - rt1=1019.7523
  - rt2=0.0000
  - sel=3.0000
  - st1=1017.7750
  - st2=0.0000
  - startup_cost=57891.6600
  - total_cost=57930.0800
- **Output:** st=1121.36, rt=1124.38

### Step 10: Node 7501 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 1d35fb97 (Sort -> Aggregate (Outer))
- **Consumes:** Nodes 7502, 7506, 7507, 7508, 7509, 7510, 7511, 7512, 7513, 7514, 7515, 7516, 7517, 7519
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
