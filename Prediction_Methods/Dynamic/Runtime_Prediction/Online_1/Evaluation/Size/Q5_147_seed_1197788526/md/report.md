# Online Prediction Report

**Test Query:** Q5_147_seed_1197788526
**Timestamp:** 2026-01-18 16:58:16

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17051 | Operator + Pattern Training |
| Training_Test | 4268 | Pattern Selection Eval |
| Training | 21319 | Final Model Training |
| Test | 3000 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 1.95%

## Phase C: Patterns in Query

- Total Patterns: 85

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 360 | 40138.8% | 144499.6064 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 210 | 15.1% | 31.8055 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 180 | 12.6% | 22.6523 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 158 | 2790.8% | 4409.3994 |
| 3e2d5a00 | Sort -> Hash Join (Outer) | 2 | 90 | 25.8% | 23.2555 |
| 3754655c | Aggregate -> Sort (Outer) | 2 | 30 | 4.1% | 1.2175 |
| 46f37744 | Gather Merge -> Aggregate (Outer) | 2 | 30 | 7.7% | 2.3145 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 368 | 15859.1% | 58361.5143 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 150 | 87.2% | 130.7419 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 142 | 4.2% | 5.9004 |
| 8a8c43c6 | Aggregate -> Gather Merge -> Aggregate (... | 3 | 30 | 4.2% | 1.2555 |
| ddb1e0ca | Sort -> Aggregate -> Gather Merge (Outer... | 3 | 30 | 51.7% | 15.5228 |
| e6c1e0d8 | Gather Merge -> Aggregate -> Sort (Outer... | 3 | 30 | 7.7% | 2.3145 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 180 | 32329.9% | 58193.8858 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 128 | 112.3% | 143.7620 |
| c0a8d3de | Hash -> Hash Join -> [Seq Scan (Outer), ... | 3 | 128 | 3427.7% | 4387.4701 |
| 91d6e559 | Sort -> Hash Join -> [Nested Loop (Outer... | 3 | 60 | 8.0% | 4.7942 |
| 460af52c | Aggregate -> Gather Merge -> Aggregate -... | 4 | 30 | 4.2% | 1.2555 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 112 | 2.8% | 3.0826 |
| a54055ce | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 90 | 4855.4% | 4369.8323 |
| 444761fb | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 38 | 46.4% | 17.6378 |
| 37515ad8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 98 | 142.5% | 139.6620 |
| bd9dfa7b | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 82 | 3.0% | 2.4909 |
| 2422d111 | Hash Join -> [Nested Loop -> [Hash Join ... | 3 | 60 | 16.0% | 9.5977 |
| 545b5e57 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 60 | 213.5% | 128.0948 |
| ec92bdaa | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 38 | 30.4% | 11.5672 |
| 12e6457c | Sort -> Hash Join -> [Nested Loop -> [Ha... | 4 | 30 | 11.3% | 3.3821 |
| 314469b0 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 5 | 30 | 35.5% | 10.6486 |
| 9d0e407c | Nested Loop -> [Hash Join -> [Seq Scan (... | 5 | 60 | 3.0% | 1.7738 |
| 4db07220 | Hash Join -> [Nested Loop -> [Hash Join ... | 4 | 30 | 17.3% | 5.2041 |
| 54cb7f90 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 6 | 30 | 35.5% | 10.6486 |
| 440e6274 | Hash Join -> [Nested Loop -> [Hash Join ... | 5 | 30 | 17.3% | 5.2041 |
| 5bfce159 | Nested Loop -> [Hash Join -> [Seq Scan (... | 6 | 30 | 2.8% | 0.8258 |
| e1d7e5b4 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 30 | 26.7% | 8.0206 |
| c302739b | Hash Join -> [Seq Scan (Outer), Hash -> ... | 7 | 30 | 26.7% | 8.0206 |
| ef93d4fc | Nested Loop -> [Hash Join -> [Seq Scan (... | 7 | 30 | 2.8% | 0.8258 |
| f4603221 | Hash Join -> [Nested Loop -> [Hash Join ... | 6 | 30 | 17.3% | 5.2041 |
| 3d4c3db9 | Hash Join -> [Nested Loop -> [Hash Join ... | 7 | 30 | 17.3% | 5.2041 |
| 5ae97df8 | Nested Loop -> [Hash Join -> [Seq Scan (... | 8 | 30 | 2.8% | 0.8258 |
| 9ce781b0 | Hash Join -> [Nested Loop -> [Hash Join ... | 8 | 30 | 17.3% | 5.2041 |
| a95bee4e | Hash Join -> [Nested Loop -> [Hash Join ... | 9 | 30 | 17.3% | 5.2041 |
| 627c5619 | Sort -> Aggregate -> Gather Merge -> Agg... | 4 | 0 | - | - |
| 7014b260 | Sort -> Aggregate -> Gather Merge -> Agg... | 5 | 0 | - | - |
| 6815cf8d | Sort -> Aggregate -> Gather Merge -> Agg... | 6 | 0 | - | - |
| bf4763ca | Sort -> Aggregate -> Gather Merge -> Agg... | 7 | 0 | - | - |
| 9b0e5572 | Sort -> Aggregate -> Gather Merge -> Agg... | 8 | 0 | - | - |
| 5a24af68 | Sort -> Aggregate -> Gather Merge -> Agg... | 9 | 0 | - | - |
| b20b9f6a | Sort -> Aggregate -> Gather Merge -> Agg... | 10 | 0 | - | - |
| d21d6eb9 | Sort -> Aggregate -> Gather Merge -> Agg... | 11 | 0 | - | - |
| 255215ee | Sort -> Aggregate -> Gather Merge -> Agg... | 12 | 0 | - | - |
| d959dddb | Sort -> Aggregate -> Gather Merge -> Agg... | 13 | 0 | - | - |
| de57e0e8 | Sort -> Aggregate -> Gather Merge -> Agg... | 14 | 0 | - | - |
| c42cb45a | Aggregate -> Gather Merge -> Aggregate -... | 5 | 0 | - | - |
| 729d307d | Aggregate -> Gather Merge -> Aggregate -... | 6 | 0 | - | - |
| 8757732f | Aggregate -> Gather Merge -> Aggregate -... | 7 | 0 | - | - |
| 00dd2f10 | Aggregate -> Gather Merge -> Aggregate -... | 8 | 0 | - | - |
| 45e3e43d | Aggregate -> Gather Merge -> Aggregate -... | 9 | 0 | - | - |
| 96b20505 | Aggregate -> Gather Merge -> Aggregate -... | 10 | 0 | - | - |
| d0ca624d | Aggregate -> Gather Merge -> Aggregate -... | 11 | 0 | - | - |
| b7143fa7 | Aggregate -> Gather Merge -> Aggregate -... | 12 | 0 | - | - |
| 2b345df9 | Aggregate -> Gather Merge -> Aggregate -... | 13 | 0 | - | - |
| 39e55ae2 | Gather Merge -> Aggregate -> Sort -> Has... | 4 | 0 | - | - |
| 14a1f63a | Gather Merge -> Aggregate -> Sort -> Has... | 5 | 0 | - | - |
| 843b7fef | Gather Merge -> Aggregate -> Sort -> Has... | 6 | 0 | - | - |
| 739b1b7e | Gather Merge -> Aggregate -> Sort -> Has... | 7 | 0 | - | - |
| f169a84a | Gather Merge -> Aggregate -> Sort -> Has... | 8 | 0 | - | - |
| ac1e65be | Gather Merge -> Aggregate -> Sort -> Has... | 9 | 0 | - | - |
| 6255ff62 | Gather Merge -> Aggregate -> Sort -> Has... | 10 | 0 | - | - |
| 8b7a3d08 | Gather Merge -> Aggregate -> Sort -> Has... | 11 | 0 | - | - |
| 1b84acf9 | Gather Merge -> Aggregate -> Sort -> Has... | 12 | 0 | - | - |
| 8823d1e5 | Aggregate -> Sort -> Hash Join (Outer) (... | 3 | 0 | - | - |
| 94adff2c | Aggregate -> Sort -> Hash Join -> [Neste... | 4 | 0 | - | - |
| 3a31b48f | Aggregate -> Sort -> Hash Join -> [Neste... | 5 | 0 | - | - |
| 0fa21834 | Aggregate -> Sort -> Hash Join -> [Neste... | 6 | 0 | - | - |
| 4de97842 | Aggregate -> Sort -> Hash Join -> [Neste... | 7 | 0 | - | - |
| 421ce908 | Aggregate -> Sort -> Hash Join -> [Neste... | 8 | 0 | - | - |
| 9325c19d | Aggregate -> Sort -> Hash Join -> [Neste... | 9 | 0 | - | - |
| 7b82db07 | Aggregate -> Sort -> Hash Join -> [Neste... | 10 | 0 | - | - |
| 7d401e23 | Aggregate -> Sort -> Hash Join -> [Neste... | 11 | 0 | - | - |
| 91ed3a4f | Sort -> Hash Join -> [Nested Loop -> [Ha... | 5 | 0 | - | - |
| d25d9b9f | Sort -> Hash Join -> [Nested Loop -> [Ha... | 6 | 0 | - | - |
| 2dc34d1b | Sort -> Hash Join -> [Nested Loop -> [Ha... | 7 | 0 | - | - |
| 5f022f0d | Sort -> Hash Join -> [Nested Loop -> [Ha... | 8 | 0 | - | - |
| 0e38b2d0 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 9 | 0 | - | - |
| 45767427 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 10 | 0 | - | - |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 3aab37be | 144499.6064 | -0.0000% | REJECTED | 18.02% |
| 1 | 1d35fb97 | 31.8055 | -0.0106% | REJECTED | 18.02% |
| 2 | 2724c080 | 22.6523 | -0.3132% | REJECTED | 18.02% |
| 3 | 7df893ad | 4409.3994 | -0.0000% | REJECTED | 18.02% |
| 4 | 3e2d5a00 | 23.2555 | 0.0090% | ACCEPTED | 18.01% |
| 5 | 3754655c | 1.2175 | N/A | SKIPPED_LOW_ERROR | 18.01% |
| 6 | 46f37744 | 2.3145 | N/A | SKIPPED_LOW_ERROR | 18.01% |
| 7 | 895c6e8c | 58361.5143 | 0.0007% | ACCEPTED | 18.01% |
| 8 | 2e0f44ef | 130.7419 | 0.0000% | ACCEPTED | 18.01% |
| 9 | 3cfa90d7 | 5.9004 | N/A | SKIPPED_LOW_ERROR | 18.01% |
| 10 | 8a8c43c6 | 1.2555 | N/A | SKIPPED_LOW_ERROR | 18.01% |
| 11 | ddb1e0ca | 15.5228 | 0.1072% | ACCEPTED | 17.90% |
| 12 | e6c1e0d8 | 2.3145 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 13 | f4cb205a | 58193.8858 | 0.0004% | ACCEPTED | 17.90% |
| 14 | bb930825 | 143.7620 | -0.0000% | REJECTED | 17.90% |
| 15 | c0a8d3de | 4387.4701 | 0.0000% | ACCEPTED | 17.90% |
| 16 | 91d6e559 | 4.7942 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 17 | 460af52c | 1.2555 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 18 | e0e3c3e1 | 3.0826 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 19 | a54055ce | 4369.8323 | N/A | REJECTED | 17.90% |
| 20 | 444761fb | 17.6378 | 0.0000% | ACCEPTED | 17.90% |
| 21 | 37515ad8 | 139.6620 | N/A | REJECTED | 17.90% |
| 22 | bd9dfa7b | 2.4909 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 23 | 2422d111 | 9.5977 | -0.0081% | REJECTED | 17.90% |
| 24 | 545b5e57 | 128.0948 | N/A | REJECTED | 17.90% |
| 25 | ec92bdaa | 11.5672 | -0.0000% | REJECTED | 17.90% |
| 26 | 12e6457c | 3.3821 | -0.0071% | REJECTED | 17.90% |
| 27 | 314469b0 | 10.6486 | N/A | REJECTED | 17.90% |
| 28 | 9d0e407c | 1.7738 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 29 | 4db07220 | 5.2041 | N/A | REJECTED | 17.90% |
| 30 | 54cb7f90 | 10.6486 | N/A | REJECTED | 17.90% |
| 31 | 440e6274 | 5.2041 | N/A | REJECTED | 17.90% |
| 32 | 5bfce159 | 0.8258 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 33 | e1d7e5b4 | 8.0206 | N/A | REJECTED | 17.90% |
| 34 | c302739b | 8.0206 | N/A | REJECTED | 17.90% |
| 35 | ef93d4fc | 0.8258 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 36 | f4603221 | 5.2041 | N/A | REJECTED | 17.90% |
| 37 | 3d4c3db9 | 5.2041 | N/A | REJECTED | 17.90% |
| 38 | 5ae97df8 | 0.8258 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 39 | 9ce781b0 | 5.2041 | N/A | REJECTED | 17.90% |
| 40 | a95bee4e | 5.2041 | N/A | REJECTED | 17.90% |
## Query Tree

```
Node 7921 (Sort) [PATTERN: ddb1e0ca] - ROOT
  Node 7922 (Aggregate) [consumed]
    Node 7923 (Gather Merge) [consumed]
      Node 7924 (Aggregate)
        Node 7925 (Sort) [PATTERN: 3e2d5a00]
          Node 7926 (Hash Join) [consumed]
            Node 7927 (Nested Loop)
              Node 7928 (Hash Join)
                Node 7929 (Seq Scan) - LEAF
                Node 7930 (Hash) [PATTERN: 444761fb]
                  Node 7931 (Hash Join) [consumed]
                    Node 7932 (Seq Scan) [consumed] - LEAF
                    Node 7933 (Hash) [consumed]
                      Node 7934 (Hash Join) [consumed]
                        Node 7935 (Seq Scan) - LEAF
                        Node 7936 (Hash)
                          Node 7937 (Seq Scan) - LEAF
              Node 7938 (Index Scan) - LEAF
            Node 7939 (Hash)
              Node 7940 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Hash -> Hash Join -> [Seq Scan | 444761fb | 7930 | 7921, 7922, 7923, 7925, 7926, 7931, 7932, 7933, 7934 |
| Sort -> Aggregate -> Gather Me | ddb1e0ca | 7921 | 7922, 7923, 7925, 7926, 7930, 7931, 7932, 7933, 7934 |
| Sort -> Hash Join (Outer) | 3e2d5a00 | 7925 | 7921, 7922, 7923, 7926, 7930, 7931, 7932, 7933, 7934 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 171.50%
- Improvement: -169.55%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 7921 | Sort | 1080.82 | 2934.42 | 171.5% | pattern |
| 7924 | Aggregate | 1075.63 | 1128.79 | 4.9% | operator |
| 7925 | Sort | 1075.38 | 1835.90 | 70.7% | pattern |
| 7927 | Nested Loop | 1061.23 | 1188.37 | 12.0% | operator |
| 7939 | Hash | 5.57 | 18.67 | 235.4% | operator |
| 7928 | Hash Join | 215.22 | 253.07 | 17.6% | operator |
| 7938 | Index Scan | 0.07 | -0.22 | 397.3% | operator |
| 7940 | Seq Scan | 5.04 | 12.36 | 145.2% | operator |
| 7929 | Seq Scan | 167.52 | 159.81 | 4.6% | operator |
| 7930 | Hash | 33.54 | 46.85 | 39.7% | pattern |
| 7935 | Seq Scan | 0.01 | 11.81 | 131103.0% | operator |
| 7936 | Hash | 0.05 | 21.05 | 44694.1% | operator |
| 7937 | Seq Scan | 0.04 | 22.93 | 52021.2% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 7937 (Seq Scan) - LEAF

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
- **Output:** st=0.17, rt=22.93

### Step 2: Node 7935 (Seq Scan) - LEAF

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
- **Output:** st=-0.03, rt=11.81

### Step 3: Node 7936 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=1
  - nt1=1
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=22.9333
  - rt2=0.0000
  - sel=1.0000
  - st1=0.1690
  - st2=0.0000
  - startup_cost=1.0600
  - total_cost=1.0600
- **Output:** st=21.05, rt=21.05

### Step 4: Node 7929 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=73059
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0487
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=33394.0600
- **Output:** st=0.14, rt=159.81

### Step 5: Node 7930 (Hash) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 444761fb (Hash -> Hash Join -> [Seq Scan (Outer), Hash -> Hash Join (Outer) (Inner)] (Outer))
- **Consumes:** Nodes 7921, 7922, 7923, 7925, 7926, 7931, 7932, 7933, 7934
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
  - Hash_Inner_nt=5
  - Hash_Inner_nt1=5
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=108
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=2.4000
  - Hash_Inner_total_cost=2.4000
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
- **Output:** st=46.85, rt=46.85

### Step 6: Node 7928 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14612
  - nt1=73059
  - nt2=12500
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=159.8089
  - rt2=46.8498
  - sel=0.0000
  - st1=0.1438
  - st2=46.8488
  - startup_cost=4743.0900
  - total_cost=38472.0100
- **Output:** st=17.17, rt=253.07

### Step 7: Node 7938 (Index Scan) - LEAF

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
- **Output:** st=0.04, rt=-0.22

### Step 8: Node 7940 (Seq Scan) - LEAF

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
- **Output:** st=0.03, rt=12.36

### Step 9: Node 7927 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=58459
  - nt1=14612
  - nt2=5
  - parallel_workers=0
  - plan_width=128
  - reltuples=0.0000
  - rt1=253.0723
  - rt2=-0.2200
  - sel=0.8002
  - st1=17.1704
  - st2=0.0370
  - startup_cost=4743.5200
  - total_cost=55959.8900
- **Output:** st=100.23, rt=1188.37

### Step 10: Node 7939 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=10000
  - nt1=10000
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=0.0000
  - rt1=12.3595
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0320
  - st2=0.0000
  - startup_cost=323.0000
  - total_cost=323.0000
- **Output:** st=18.67, rt=18.67

### Step 11: Node 7925 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 3e2d5a00 (Sort -> Hash Join (Outer))
- **Consumes:** Nodes 7921, 7922, 7923, 7926, 7930, 7931, 7932, 7933, 7934
- **Input Features:**
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=2338
  - HashJoin_Outer_nt1=58459
  - HashJoin_Outer_nt2=10000
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=116
  - HashJoin_Outer_reltuples=0.0000
  - HashJoin_Outer_sel=0.0000
  - HashJoin_Outer_startup_cost=5216.5200
  - HashJoin_Outer_total_cost=56739.8000
  - Sort_np=0
  - Sort_nt=2338
  - Sort_nt1=2338
  - Sort_nt2=0
  - Sort_parallel_workers=0
  - Sort_plan_width=116
  - Sort_reltuples=0.0000
  - Sort_sel=1.0000
  - Sort_startup_cost=56870.6200
  - Sort_total_cost=56876.4700
- **Output:** st=1835.88, rt=1835.90

### Step 12: Node 7924 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=2338
  - nt2=0
  - parallel_workers=0
  - plan_width=136
  - reltuples=0.0000
  - rt1=1835.8975
  - rt2=0.0000
  - sel=0.0107
  - st1=1835.8834
  - st2=0.0000
  - startup_cost=56870.6200
  - total_cost=56900.1600
- **Output:** st=1065.16, rt=1128.79

### Step 13: Node 7921 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** ddb1e0ca (Sort -> Aggregate -> Gather Merge (Outer) (Outer))
- **Consumes:** Nodes 7922, 7923, 7925, 7926, 7930, 7931, 7932, 7933, 7934
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=25
  - Aggregate_Outer_nt1=75
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=136
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.3333
  - Aggregate_Outer_startup_cost=57870.6600
  - Aggregate_Outer_total_cost=57909.8900
  - GatherMerge_Outer_np=0
  - GatherMerge_Outer_nt=75
  - GatherMerge_Outer_nt1=25
  - GatherMerge_Outer_nt2=0
  - GatherMerge_Outer_parallel_workers=3
  - GatherMerge_Outer_plan_width=136
  - GatherMerge_Outer_reltuples=0.0000
  - GatherMerge_Outer_sel=3.0000
  - GatherMerge_Outer_startup_cost=57870.6600
  - GatherMerge_Outer_total_cost=57909.0100
  - Sort_np=0
  - Sort_nt=25
  - Sort_nt1=25
  - Sort_nt2=0
  - Sort_parallel_workers=0
  - Sort_plan_width=136
  - Sort_reltuples=0.0000
  - Sort_sel=1.0000
  - Sort_startup_cost=57910.4700
  - Sort_total_cost=57910.5300
- **Output:** st=2927.00, rt=2934.42
