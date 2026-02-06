# Online Prediction Report

**Test Query:** Q5_124_seed_1009095813
**Timestamp:** 2026-01-11 20:16:52

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
| 17 | 2724c080 | 7.7847 | 0.0345% | ACCEPTED | 17.77% |
| 18 | 3cfa90d7 | 4.0055 | N/A | REJECTED | 17.77% |
| 19 | e0e3c3e1 | 3.3189 | N/A | REJECTED | 17.77% |
| 20 | 91d6e559 | 3.0313 | N/A | REJECTED | 17.77% |
| 21 | 12e6457c | 2.7493 | N/A | REJECTED | 17.77% |
| 22 | bd9dfa7b | 2.5412 | N/A | REJECTED | 17.77% |
| 23 | 9d0e407c | 2.4738 | N/A | REJECTED | 17.77% |
| 24 | 46f37744 | 2.3873 | N/A | REJECTED | 17.77% |
| 25 | e6c1e0d8 | 2.3873 | -0.1094% | REJECTED | 17.77% |
| 26 | 3754655c | 2.1224 | N/A | REJECTED | 17.77% |
| 27 | 460af52c | 1.9179 | 0.0894% | ACCEPTED | 17.68% |
| 28 | 2422d111 | 1.5987 | N/A | REJECTED | 17.68% |
| 29 | 3d4c3db9 | 1.1101 | N/A | REJECTED | 17.68% |
| 30 | 440e6274 | 1.1101 | N/A | REJECTED | 17.68% |
| 31 | 4db07220 | 1.1101 | N/A | REJECTED | 17.68% |
| 32 | 9ce781b0 | 1.1101 | N/A | REJECTED | 17.68% |
| 33 | a95bee4e | 1.1101 | N/A | REJECTED | 17.68% |
| 34 | f4603221 | 1.1101 | N/A | REJECTED | 17.68% |
| 35 | 255215ee | 0.8621 | 0.1600% | ACCEPTED | 17.52% |
| 36 | 8a8c43c6 | 0.4436 | N/A | REJECTED | 17.52% |
| 37 | 5a24af68 | 0.3246 | N/A | REJECTED | 17.52% |
| 38 | 627c5619 | 0.3246 | N/A | REJECTED | 17.52% |
| 39 | 6815cf8d | 0.3246 | N/A | REJECTED | 17.52% |
| 40 | 7014b260 | 0.3246 | N/A | REJECTED | 17.52% |
| 41 | 9b0e5572 | 0.3246 | N/A | REJECTED | 17.52% |
| 42 | b20b9f6a | 0.3246 | N/A | REJECTED | 17.52% |
| 43 | bf4763ca | 0.3246 | N/A | REJECTED | 17.52% |
| 44 | d21d6eb9 | 0.3246 | N/A | REJECTED | 17.52% |
| 45 | d959dddb | 0.3246 | N/A | REJECTED | 17.52% |
| 46 | de57e0e8 | 0.3246 | N/A | REJECTED | 17.52% |
## Query Tree

```
Node 7421 (Sort) [PATTERN: 255215ee] - ROOT
  Node 7422 (Aggregate) [consumed]
    Node 7423 (Gather Merge) [consumed]
      Node 7424 (Aggregate) [consumed]
        Node 7425 (Sort) [consumed]
          Node 7426 (Hash Join) [consumed]
            Node 7427 (Nested Loop) [consumed]
              Node 7428 (Hash Join) [consumed]
                Node 7429 (Seq Scan) [consumed] - LEAF
                Node 7430 (Hash) [consumed]
                  Node 7431 (Hash Join) [consumed]
                    Node 7432 (Seq Scan) [consumed] - LEAF
                    Node 7433 (Hash) [consumed]
                      Node 7434 (Hash Join) [consumed]
                        Node 7435 (Seq Scan) - LEAF
                        Node 7436 (Hash)
                          Node 7437 (Seq Scan) - LEAF
              Node 7438 (Index Scan) [consumed] - LEAF
            Node 7439 (Hash) [consumed]
              Node 7440 (Seq Scan) [consumed] - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Sort -> Aggregate -> Gather Me | 255215ee | 7421 | 7422, 7423, 7424, 7425, 7426, 7427, 7428, 7429, 7430, 7431, 7432, 7433, 7434, 7438, 7439, 7440 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 2.45%
- Improvement: 3.63%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 7421 | Sort | 1044.84 | 1070.44 | 2.5% | pattern |
| 7435 | Seq Scan | 0.01 | 10.49 | 131084.1% | operator |
| 7436 | Hash | 0.14 | 16.01 | 11675.7% | operator |
| 7437 | Seq Scan | 0.13 | 21.39 | 16228.2% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 7437 (Seq Scan) - LEAF

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

### Step 2: Node 7435 (Seq Scan) - LEAF

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

### Step 3: Node 7436 (Hash)

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

### Step 4: Node 7421 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 255215ee (Sort -> Aggregate -> Gather Merge -> Aggregate -> Sort -> Hash Join -> [Nested Loop -> [Hash Join -> [Seq Scan (Outer), Hash -> Hash Join -> [Seq Scan (Outer), Hash -> Hash Join (Outer) (Inner)] (Outer) (Inner)] (Outer), Index Scan (Inner)] (Outer), Hash -> Seq Scan (Outer) (Inner)] (Outer) (Outer) (Outer) (Outer) (Outer))
- **Consumes:** Nodes 7422, 7423, 7424, 7425, 7426, 7427, 7428, 7429, 7430, 7431, 7432, 7433, 7434, 7438, 7439, 7440
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=25
  - Aggregate_Outer_nt1=2344
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=136
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0107
  - Aggregate_Outer_startup_cost=56891.6200
  - Aggregate_Outer_total_cost=56921.2300
  - GatherMerge_Outer_np=0
  - GatherMerge_Outer_nt=75
  - GatherMerge_Outer_nt1=25
  - GatherMerge_Outer_nt2=0
  - GatherMerge_Outer_parallel_workers=3
  - GatherMerge_Outer_plan_width=136
  - GatherMerge_Outer_reltuples=0.0000
  - GatherMerge_Outer_sel=3.0000
  - GatherMerge_Outer_startup_cost=57891.6600
  - GatherMerge_Outer_total_cost=57930.0800
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
  - Hash_Inner_nt=12500
  - Hash_Inner_nt1=12500
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=116
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=4586.8400
  - Hash_Inner_total_cost=4586.8400
  - IndexScan_Inner_np=112600
  - IndexScan_Inner_nt=5
  - IndexScan_Inner_nt1=0
  - IndexScan_Inner_nt2=0
  - IndexScan_Inner_parallel_workers=0
  - IndexScan_Inner_plan_width=20
  - IndexScan_Inner_reltuples=6001215.0000
  - IndexScan_Inner_sel=0.0000
  - IndexScan_Inner_startup_cost=0.4300
  - IndexScan_Inner_total_cost=1.1500
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
  - SeqScan_Outer_np=223
  - SeqScan_Outer_nt=10000
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=8
  - SeqScan_Outer_reltuples=10000.0000
  - SeqScan_Outer_sel=1.0000
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=323.0000
  - Sort_Outer_np=0
  - Sort_Outer_nt=2344
  - Sort_Outer_nt1=2344
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=116
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=56891.6200
  - Sort_Outer_total_cost=56897.4800
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
- **Output:** st=1068.79, rt=1070.44
