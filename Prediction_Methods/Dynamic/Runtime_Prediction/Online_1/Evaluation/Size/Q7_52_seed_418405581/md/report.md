# Online Prediction Report

**Test Query:** Q7_52_seed_418405581
**Timestamp:** 2026-01-18 18:01:13

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17291 | Operator + Pattern Training |
| Training_Test | 4328 | Pattern Selection Eval |
| Training | 21619 | Final Model Training |
| Test | 2700 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 0.60%

## Phase C: Patterns in Query

- Total Patterns: 44

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 360 | 19515.5% | 70255.9551 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 180 | 12.9% | 23.1405 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 158 | 5421.3% | 8565.6070 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 90 | 9.2% | 8.2533 |
| 3e2d5a00 | Sort -> Hash Join (Outer) | 2 | 90 | 25.2% | 22.7018 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 368 | 27128.1% | 99831.3585 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 150 | 84.4% | 126.6606 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 142 | 4.1% | 5.7940 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 90 | 5.5% | 4.9483 |
| 98d4ff98 | Gather Merge -> Sort -> Hash Join (Outer... | 3 | 30 | 8.5% | 2.5384 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 158 | 165.4% | 261.3404 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 150 | 66363.9% | 99545.8479 |
| c0a8d3de | Hash -> Hash Join -> [Seq Scan (Outer), ... | 3 | 128 | 6674.5% | 8543.4003 |
| 91d6e559 | Sort -> Hash Join -> [Nested Loop (Outer... | 3 | 60 | 7.1% | 4.2435 |
| b149ff28 | Aggregate -> Gather Merge -> Sort -> Has... | 4 | 30 | 3.1% | 0.9427 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 112 | 2.4% | 2.7134 |
| a54055ce | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 60 | 14188.5% | 8513.0877 |
| 3c6d8006 | Gather Merge -> Sort -> Hash Join -> [Ne... | 4 | 30 | 8.5% | 2.5384 |
| 37515ad8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 128 | 201.0% | 257.3049 |
| bd9dfa7b | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 82 | 2.5% | 2.0349 |
| 53f9aa07 | Aggregate -> Gather Merge -> Sort -> Has... | 5 | 30 | 3.1% | 0.9427 |
| 545b5e57 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 60 | 383.7% | 230.2087 |
| 9d0e407c | Nested Loop -> [Hash Join -> [Seq Scan (... | 5 | 60 | 2.7% | 1.6049 |
| 27c3eea9 | Aggregate -> Gather Merge -> Sort -> Has... | 6 | 0 | - | - |
| e8907654 | Aggregate -> Gather Merge -> Sort -> Has... | 7 | 0 | - | - |
| c83209ef | Aggregate -> Gather Merge -> Sort -> Has... | 8 | 0 | - | - |
| 9d0b7ec3 | Aggregate -> Gather Merge -> Sort -> Has... | 9 | 0 | - | - |
| e7dc2e6a | Aggregate -> Gather Merge -> Sort -> Has... | 10 | 0 | - | - |
| 814388b1 | Gather Merge -> Sort -> Hash Join -> [Ne... | 5 | 0 | - | - |
| 34811571 | Gather Merge -> Sort -> Hash Join -> [Ne... | 6 | 0 | - | - |
| 3d2df434 | Gather Merge -> Sort -> Hash Join -> [Ne... | 7 | 0 | - | - |
| 991242c7 | Gather Merge -> Sort -> Hash Join -> [Ne... | 8 | 0 | - | - |
| 1ec32e3e | Gather Merge -> Sort -> Hash Join -> [Ne... | 9 | 0 | - | - |
| 94a6aee0 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 4 | 0 | - | - |
| 6b43f5a7 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 5 | 0 | - | - |
| cfb66570 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 6 | 0 | - | - |
| f5c4d937 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 7 | 0 | - | - |
| bdf0194d | Sort -> Hash Join -> [Nested Loop -> [Ha... | 8 | 0 | - | - |
| 1e7829bf | Hash Join -> [Nested Loop -> [Hash Join ... | 3 | 0 | - | - |
| 88cd04f5 | Hash Join -> [Nested Loop -> [Hash Join ... | 4 | 0 | - | - |
| 2dab5c22 | Hash Join -> [Nested Loop -> [Hash Join ... | 5 | 0 | - | - |
| 66a98304 | Hash Join -> [Nested Loop -> [Hash Join ... | 6 | 0 | - | - |
| 759d57a4 | Hash Join -> [Nested Loop -> [Hash Join ... | 7 | 0 | - | - |
| 68382c9c | Nested Loop -> [Hash Join -> [Seq Scan (... | 6 | 0 | - | - |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 3aab37be | 70255.9551 | -0.0000% | REJECTED | 18.09% |
| 1 | 2724c080 | 23.1405 | 0.0057% | ACCEPTED | 18.09% |
| 2 | 7df893ad | 8565.6070 | -0.0000% | REJECTED | 18.09% |
| 3 | 1691f6f0 | 8.2533 | N/A | SKIPPED_LOW_ERROR | 18.09% |
| 4 | 3e2d5a00 | 22.7018 | N/A | REJECTED | 18.09% |
| 5 | 895c6e8c | 99831.3585 | 0.0010% | ACCEPTED | 18.09% |
| 6 | 2e0f44ef | 126.6606 | -0.0000% | REJECTED | 18.09% |
| 7 | 3cfa90d7 | 5.7940 | N/A | SKIPPED_LOW_ERROR | 18.09% |
| 8 | 29ee00db | 4.9483 | N/A | SKIPPED_LOW_ERROR | 18.09% |
| 9 | 98d4ff98 | 2.5384 | N/A | SKIPPED_LOW_ERROR | 18.09% |
| 10 | bb930825 | 261.3404 | -0.0000% | REJECTED | 18.09% |
| 11 | f4cb205a | 99545.8479 | 0.0004% | ACCEPTED | 18.09% |
| 12 | c0a8d3de | 8543.4003 | 0.0000% | ACCEPTED | 18.09% |
| 13 | 91d6e559 | 4.2435 | N/A | SKIPPED_LOW_ERROR | 18.09% |
| 14 | b149ff28 | 0.9427 | N/A | SKIPPED_LOW_ERROR | 18.09% |
| 15 | e0e3c3e1 | 2.7134 | N/A | SKIPPED_LOW_ERROR | 18.09% |
| 16 | a54055ce | 8513.0877 | N/A | REJECTED | 18.09% |
| 17 | 3c6d8006 | 2.5384 | N/A | SKIPPED_LOW_ERROR | 18.09% |
| 18 | 37515ad8 | 257.3049 | -0.0000% | REJECTED | 18.09% |
| 19 | bd9dfa7b | 2.0349 | N/A | SKIPPED_LOW_ERROR | 18.09% |
| 20 | 53f9aa07 | 0.9427 | N/A | SKIPPED_LOW_ERROR | 18.09% |
| 21 | 545b5e57 | 230.2087 | N/A | REJECTED | 18.09% |
| 22 | 9d0e407c | 1.6049 | N/A | SKIPPED_LOW_ERROR | 18.09% |
## Query Tree

```
Node 12247 (Aggregate) [PATTERN: 2724c080] - ROOT
  Node 12248 (Gather Merge) [consumed]
    Node 12249 (Sort)
      Node 12250 (Hash Join)
        Node 12251 (Nested Loop)
          Node 12252 (Hash Join) [PATTERN: 895c6e8c]
            Node 12253 (Seq Scan) [consumed] - LEAF
            Node 12254 (Hash) [consumed]
              Node 12255 (Hash Join) [PATTERN: f4cb205a]
                Node 12256 (Seq Scan) [consumed] - LEAF
                Node 12257 (Hash) [consumed]
                  Node 12258 (Seq Scan) [consumed] - LEAF
          Node 12259 (Index Scan) - LEAF
        Node 12260 (Hash)
          Node 12261 (Hash Join) [PATTERN: f4cb205a]
            Node 12262 (Seq Scan) [consumed] - LEAF
            Node 12263 (Hash) [consumed]
              Node 12264 (Seq Scan) [consumed] - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Hash Join -> [Seq Scan (Outer) | f4cb205a | 12255 | 12247, 12248, 12252, 12253, 12254, 12256, 12257, 12258, 12261, 12262, 12263, 12264 |
| Hash Join -> [Seq Scan (Outer) | f4cb205a | 12261 | 12247, 12248, 12252, 12253, 12254, 12255, 12256, 12257, 12258, 12262, 12263, 12264 |
| Aggregate -> Gather Merge (Out | 2724c080 | 12247 | 12248, 12252, 12253, 12254, 12255, 12256, 12257, 12258, 12261, 12262, 12263, 12264 |
| Hash Join -> [Seq Scan (Outer) | 895c6e8c | 12252 | 12247, 12248, 12253, 12254, 12255, 12256, 12257, 12258, 12261, 12262, 12263, 12264 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 3.70%
- Improvement: -3.10%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 12247 | Aggregate | 1207.85 | 1163.13 | 3.7% | pattern |
| 12249 | Sort | 1200.79 | 1109.16 | 7.6% | operator |
| 12250 | Hash Join | 1200.16 | 843.11 | 29.8% | operator |
| 12251 | Nested Loop | 1193.98 | 1215.99 | 1.8% | operator |
| 12260 | Hash | 2.39 | 27.74 | 1062.3% | operator |
| 12252 | Hash Join | 213.95 | 304.89 | 42.5% | pattern |
| 12259 | Index Scan | 0.03 | 0.96 | 2817.7% | operator |
| 12261 | Hash Join | 2.32 | 429.36 | 18423.0% | pattern |
| 12255 | Hash Join | 37.49 | 429.38 | 1045.3% | pattern |

## Prediction Chain (Bottom-Up)

### Step 1: Node 12255 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** f4cb205a (Hash Join -> [Seq Scan (Outer), Hash -> Seq Scan (Outer) (Inner)])
- **Consumes:** Nodes 12247, 12248, 12252, 12253, 12254, 12256, 12257, 12258, 12261, 12262, 12263, 12264
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=5000
  - HashJoin_nt1=62500
  - HashJoin_nt2=2
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=108
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0400
  - HashJoin_startup_cost=1.4000
  - HashJoin_total_cost=4418.2700
  - Hash_Inner_np=0
  - Hash_Inner_nt=2
  - Hash_Inner_nt1=2
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=108
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=1.3800
  - Hash_Inner_total_cost=1.3800
  - SeqScan_Outer_np=1
  - SeqScan_Outer_nt=2
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=108
  - SeqScan_Outer_reltuples=25.0000
  - SeqScan_Outer_sel=0.0800
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=1.3800
- **Output:** st=37.62, rt=429.38

### Step 2: Node 12252 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 895c6e8c (Hash Join -> [Seq Scan (Outer), Hash (Inner)])
- **Consumes:** Nodes 12247, 12248, 12253, 12254, 12255, 12256, 12257, 12258, 12261, 12262, 12263, 12264
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=38710
  - HashJoin_nt1=483871
  - HashJoin_nt2=5000
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=108
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0000
  - HashJoin_startup_cost=4480.7700
  - HashJoin_total_cost=37431.2900
  - Hash_Inner_np=0
  - Hash_Inner_nt=5000
  - Hash_Inner_nt1=5000
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=108
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=4418.2700
  - Hash_Inner_total_cost=4418.2700
  - SeqScan_Outer_np=26136
  - SeqScan_Outer_nt=483871
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=8
  - SeqScan_Outer_reltuples=1500000.0000
  - SeqScan_Outer_sel=0.3226
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=30974.7100
- **Output:** st=39.64, rt=304.89

### Step 3: Node 12259 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=1
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
  - total_cost=0.6400
- **Output:** st=0.04, rt=0.96

### Step 4: Node 12261 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** f4cb205a (Hash Join -> [Seq Scan (Outer), Hash -> Seq Scan (Outer) (Inner)])
- **Consumes:** Nodes 12247, 12248, 12252, 12253, 12254, 12255, 12256, 12257, 12258, 12262, 12263, 12264
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=800
  - HashJoin_nt1=10000
  - HashJoin_nt2=2
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=108
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0400
  - HashJoin_startup_cost=1.4000
  - HashJoin_total_cost=355.1000
  - Hash_Inner_np=0
  - Hash_Inner_nt=2
  - Hash_Inner_nt1=2
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=108
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=1.3800
  - Hash_Inner_total_cost=1.3800
  - SeqScan_Outer_np=1
  - SeqScan_Outer_nt=2
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=108
  - SeqScan_Outer_reltuples=25.0000
  - SeqScan_Outer_sel=0.0800
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=1.3800
- **Output:** st=37.62, rt=429.36

### Step 5: Node 12251 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=47115
  - nt1=38710
  - nt2=1
  - parallel_workers=0
  - plan_width=124
  - reltuples=0.0000
  - rt1=304.8910
  - rt2=0.9629
  - sel=1.2171
  - st1=39.6385
  - st2=0.0394
  - startup_cost=4481.2100
  - total_cost=62578.9300
- **Output:** st=173.40, rt=1215.99

### Step 6: Node 12260 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=800
  - nt1=800
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=429.3628
  - rt2=0.0000
  - sel=1.0000
  - st1=37.6160
  - st2=0.0000
  - startup_cost=355.1000
  - total_cost=355.1000
- **Output:** st=27.74, rt=27.74

### Step 7: Node 12250 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=1961
  - nt1=47115
  - nt2=800
  - parallel_workers=0
  - plan_width=252
  - reltuples=0.0000
  - rt1=1215.9932
  - rt2=27.7432
  - sel=0.0001
  - st1=173.4013
  - st2=27.7423
  - startup_cost=4846.3100
  - total_cost=63200.9900
- **Output:** st=124.69, rt=843.11

### Step 8: Node 12249 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=1961
  - nt1=1961
  - nt2=0
  - parallel_workers=0
  - plan_width=252
  - reltuples=0.0000
  - rt1=843.1103
  - rt2=0.0000
  - sel=1.0000
  - st1=124.6885
  - st2=0.0000
  - startup_cost=63308.2300
  - total_cost=63313.1300
- **Output:** st=1107.66, rt=1109.16

### Step 9: Node 12247 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 2724c080 (Aggregate -> Gather Merge (Outer))
- **Consumes:** Nodes 12248, 12252, 12253, 12254, 12255, 12256, 12257, 12258, 12261, 12262, 12263, 12264
- **Input Features:**
  - Aggregate_np=0
  - Aggregate_nt=6078
  - Aggregate_nt1=6078
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=272
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=1.0000
  - Aggregate_startup_cost=64308.2700
  - Aggregate_total_cost=65209.6800
  - GatherMerge_Outer_np=0
  - GatherMerge_Outer_nt=6078
  - GatherMerge_Outer_nt1=1961
  - GatherMerge_Outer_nt2=0
  - GatherMerge_Outer_parallel_workers=3
  - GatherMerge_Outer_plan_width=252
  - GatherMerge_Outer_reltuples=0.0000
  - GatherMerge_Outer_sel=3.0994
  - GatherMerge_Outer_startup_cost=64308.2700
  - GatherMerge_Outer_total_cost=65027.3400
- **Output:** st=1159.54, rt=1163.13
