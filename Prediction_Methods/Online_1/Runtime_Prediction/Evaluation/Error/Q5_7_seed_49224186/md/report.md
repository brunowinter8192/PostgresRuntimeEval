# Online Prediction Report

**Test Query:** Q5_7_seed_49224186
**Timestamp:** 2026-01-01 20:26:27

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 2.67%

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
| 11 | 1d35fb97 | 26.4006 | 0.1163% | ACCEPTED | 17.81% |
| 12 | ec92bdaa | 20.2515 | N/A | REJECTED | 17.81% |
| 13 | 3e2d5a00 | 18.4265 | 0.0001% | ACCEPTED | 17.81% |
| 14 | c302739b | 18.3306 | N/A | REJECTED | 17.81% |
| 15 | e1d7e5b4 | 18.3306 | N/A | REJECTED | 17.81% |
| 16 | ddb1e0ca | 13.5374 | -5.4908% | REJECTED | 17.81% |
| 17 | 2724c080 | 7.7847 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 18 | 3cfa90d7 | 4.0055 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 19 | e0e3c3e1 | 3.3189 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 20 | 91d6e559 | 3.0313 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 21 | 46f37744 | 2.8145 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 22 | e6c1e0d8 | 2.8145 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 23 | 12e6457c | 2.7493 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 24 | bd9dfa7b | 2.5412 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 25 | 9d0e407c | 2.4738 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 26 | 460af52c | 2.1945 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 27 | 8a8c43c6 | 2.1945 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 28 | 3754655c | 2.1224 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 29 | 2422d111 | 1.5987 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 30 | 14a1f63a | 1.1936 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 31 | 1b84acf9 | 1.1936 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 32 | 39e55ae2 | 1.1936 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 33 | 6255ff62 | 1.1936 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 34 | 739b1b7e | 1.1936 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 35 | 843b7fef | 1.1936 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 36 | 8b7a3d08 | 1.1936 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 37 | ac1e65be | 1.1936 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 38 | f169a84a | 1.1936 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 39 | 0fa21834 | 1.1511 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 40 | 3a31b48f | 1.1511 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 41 | 421ce908 | 1.1511 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 42 | 4de97842 | 1.1511 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 43 | 7b82db07 | 1.1511 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 44 | 7d401e23 | 1.1511 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 45 | 8823d1e5 | 1.1511 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 46 | 9325c19d | 1.1511 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 47 | 94adff2c | 1.1511 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 48 | 3d4c3db9 | 1.1101 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 49 | 440e6274 | 1.1101 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 50 | 4db07220 | 1.1101 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 51 | 9ce781b0 | 1.1101 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 52 | a95bee4e | 1.1101 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 53 | f4603221 | 1.1101 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 54 | 0e38b2d0 | 0.4938 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 55 | 2dc34d1b | 0.4938 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 56 | 45767427 | 0.4938 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 57 | 5f022f0d | 0.4938 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 58 | 91ed3a4f | 0.4938 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 59 | d25d9b9f | 0.4938 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 60 | 255215ee | 0.4253 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 61 | 5a24af68 | 0.4253 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 62 | 627c5619 | 0.4253 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 63 | 6815cf8d | 0.4253 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 64 | 7014b260 | 0.4253 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 65 | 9b0e5572 | 0.4253 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 66 | b20b9f6a | 0.4253 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 67 | bf4763ca | 0.4253 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 68 | d21d6eb9 | 0.4253 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 69 | d959dddb | 0.4253 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 70 | de57e0e8 | 0.4253 | N/A | SKIPPED_LOW_ERROR | 17.81% |
## Query Tree

```
Node 9441 (Sort) [PATTERN: 1d35fb97] - ROOT
  Node 9442 (Aggregate) [consumed]
    Node 9443 (Gather Merge)
      Node 9444 (Aggregate)
        Node 9445 (Sort)
          Node 9446 (Hash Join) [PATTERN: 2e0f44ef]
            Node 9447 (Nested Loop) [consumed]
              Node 9448 (Hash Join) [PATTERN: 895c6e8c]
                Node 9449 (Seq Scan) [consumed] - LEAF
                Node 9450 (Hash) [consumed]
                  Node 9451 (Hash Join)
                    Node 9452 (Seq Scan) - LEAF
                    Node 9453 (Hash) [PATTERN: a54055ce]
                      Node 9454 (Hash Join) [consumed]
                        Node 9455 (Seq Scan) [consumed] - LEAF
                        Node 9456 (Hash) [consumed]
                          Node 9457 (Seq Scan) [consumed] - LEAF
              Node 9458 (Index Scan) - LEAF
            Node 9459 (Hash) [consumed]
              Node 9460 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Hash -> Hash Join -> [Seq Scan | a54055ce | 9453 | 9441, 9442, 9446, 9447, 9448, 9449, 9450, 9454, 9455, 9456, 9457, 9459 |
| Hash Join -> [Seq Scan (Outer) | 895c6e8c | 9448 | 9441, 9442, 9446, 9447, 9449, 9450, 9453, 9454, 9455, 9456, 9457, 9459 |
| Hash Join -> [Nested Loop (Out | 2e0f44ef | 9446 | 9441, 9442, 9447, 9448, 9449, 9450, 9453, 9454, 9455, 9456, 9457, 9459 |
| Sort -> Aggregate (Outer) | 1d35fb97 | 9441 | 9442, 9446, 9447, 9448, 9449, 9450, 9453, 9454, 9455, 9456, 9457, 9459 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 0.05%
- Improvement: 2.62%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 9441 | Sort | 1079.55 | 1080.14 | 0.1% | pattern |
| 9443 | Gather Merge | 1079.53 | 1124.36 | 4.2% | operator |
| 9444 | Aggregate | 1074.39 | 1019.70 | 5.1% | operator |
| 9445 | Sort | 1074.14 | 1073.11 | 0.1% | operator |
| 9446 | Hash Join | 1073.67 | 1080.38 | 0.6% | pattern |
| 9448 | Hash Join | 214.98 | 259.82 | 20.9% | pattern |
| 9458 | Index Scan | 0.07 | -0.03 | 134.0% | operator |
| 9460 | Seq Scan | 3.39 | 10.62 | 213.1% | operator |
| 9451 | Hash Join | 35.44 | 62.70 | 76.9% | operator |
| 9452 | Seq Scan | 34.01 | 24.87 | 26.9% | operator |
| 9453 | Hash | 0.07 | 0.14 | 100.3% | pattern |

## Prediction Chain (Bottom-Up)

### Step 1: Node 9452 (Seq Scan) - LEAF

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

### Step 2: Node 9453 (Hash) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** a54055ce (Hash -> Hash Join -> [Seq Scan (Outer), Hash -> Seq Scan (Outer) (Inner)] (Outer))
- **Consumes:** Nodes 9441, 9442, 9446, 9447, 9448, 9449, 9450, 9454, 9455, 9456, 9457, 9459
- **Input Features:**
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=5
  - HashJoin_Outer_nt1=25
  - HashJoin_Outer_nt2=1
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=108
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
  - Hash_plan_width=108
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
- **Output:** st=0.14, rt=0.14

### Step 3: Node 9451 (Hash Join)

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
  - rt2=0.1362
  - sel=0.0400
  - st1=0.2761
  - st2=0.1356
  - startup_cost=2.4600
  - total_cost=4586.8400
- **Output:** st=2.85, rt=62.70

### Step 4: Node 9448 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 895c6e8c (Hash Join -> [Seq Scan (Outer), Hash (Inner)])
- **Consumes:** Nodes 9441, 9442, 9446, 9447, 9449, 9450, 9453, 9454, 9455, 9456, 9457, 9459
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

### Step 5: Node 9458 (Index Scan) - LEAF

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

### Step 6: Node 9460 (Seq Scan) - LEAF

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

### Step 7: Node 9446 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 2e0f44ef (Hash Join -> [Nested Loop (Outer), Hash (Inner)])
- **Consumes:** Nodes 9441, 9442, 9447, 9448, 9449, 9450, 9453, 9454, 9455, 9456, 9457, 9459
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=2362
  - HashJoin_nt1=59037
  - HashJoin_nt2=10000
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=116
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0000
  - HashJoin_startup_cost=5216.5200
  - HashJoin_total_cost=56827.8200
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
  - NestedLoop_Outer_nt=59037
  - NestedLoop_Outer_nt1=14756
  - NestedLoop_Outer_nt2=5
  - NestedLoop_Outer_parallel_workers=0
  - NestedLoop_Outer_plan_width=128
  - NestedLoop_Outer_reltuples=0.0000
  - NestedLoop_Outer_sel=0.8002
  - NestedLoop_Outer_startup_cost=4743.5200
  - NestedLoop_Outer_total_cost=56044.8800
- **Output:** st=41.72, rt=1080.38

### Step 8: Node 9445 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2362
  - nt1=2362
  - nt2=0
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=1080.3751
  - rt2=0.0000
  - sel=1.0000
  - st1=41.7211
  - st2=0.0000
  - startup_cost=56960.1600
  - total_cost=56966.0700
- **Output:** st=1072.20, rt=1073.11

### Step 9: Node 9444 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=2362
  - nt2=0
  - parallel_workers=0
  - plan_width=136
  - reltuples=0.0000
  - rt1=1073.1123
  - rt2=0.0000
  - sel=0.0106
  - st1=1072.1969
  - st2=0.0000
  - startup_cost=56960.1600
  - total_cost=56990.0000
- **Output:** st=1017.73, rt=1019.70

### Step 10: Node 9443 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=75
  - nt1=25
  - nt2=0
  - parallel_workers=3
  - plan_width=136
  - reltuples=0.0000
  - rt1=1019.7046
  - rt2=0.0000
  - sel=3.0000
  - st1=1017.7313
  - st2=0.0000
  - startup_cost=57960.2000
  - total_cost=57998.8500
- **Output:** st=1121.35, rt=1124.36

### Step 11: Node 9441 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 1d35fb97 (Sort -> Aggregate (Outer))
- **Consumes:** Nodes 9442, 9446, 9447, 9448, 9449, 9450, 9453, 9454, 9455, 9456, 9457, 9459
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
