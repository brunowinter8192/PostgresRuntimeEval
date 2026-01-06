# Online Prediction Report

**Test Query:** Q7_141_seed_1148564340
**Timestamp:** 2026-01-01 18:26:32

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 1.18%

## Phase C: Patterns in Query

- Total Patterns: 44

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
| 98d4ff98 | Gather Merge -> Sort -> Hash Join (Outer... | 3 | 48 | 6.2% | 2.9727 |
| 1e7829bf | Hash Join -> [Nested Loop -> [Hash Join ... | 3 | 24 | 10.7% | 2.5679 |
| 37515ad8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 124 | 135.7% | 168.3286 |
| a54055ce | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 96 | 6342.9% | 6089.1983 |
| bd9dfa7b | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 92 | 3.7% | 3.3601 |
| b149ff28 | Aggregate -> Gather Merge -> Sort -> Has... | 4 | 48 | 2.2% | 1.0579 |
| 3c6d8006 | Gather Merge -> Sort -> Hash Join -> [Ne... | 4 | 48 | 6.2% | 2.9727 |
| 94a6aee0 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 4 | 24 | 4.0% | 0.9537 |
| 88cd04f5 | Hash Join -> [Nested Loop -> [Hash Join ... | 4 | 24 | 10.7% | 2.5679 |
| 9d0e407c | Nested Loop -> [Hash Join -> [Seq Scan (... | 5 | 72 | 4.1% | 2.9587 |
| 545b5e57 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 72 | 212.7% | 153.1732 |
| 53f9aa07 | Aggregate -> Gather Merge -> Sort -> Has... | 5 | 48 | 2.2% | 1.0579 |
| 814388b1 | Gather Merge -> Sort -> Hash Join -> [Ne... | 5 | 24 | 4.5% | 1.0842 |
| 6b43f5a7 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 5 | 24 | 4.0% | 0.9537 |
| 2dab5c22 | Hash Join -> [Nested Loop -> [Hash Join ... | 5 | 24 | 10.7% | 2.5679 |
| 27c3eea9 | Aggregate -> Gather Merge -> Sort -> Has... | 6 | 24 | 1.2% | 0.2928 |
| 34811571 | Gather Merge -> Sort -> Hash Join -> [Ne... | 6 | 24 | 4.5% | 1.0842 |
| cfb66570 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 6 | 24 | 4.0% | 0.9537 |
| 66a98304 | Hash Join -> [Nested Loop -> [Hash Join ... | 6 | 24 | 10.7% | 2.5679 |
| 68382c9c | Nested Loop -> [Hash Join -> [Seq Scan (... | 6 | 24 | 3.4% | 0.8246 |
| e8907654 | Aggregate -> Gather Merge -> Sort -> Has... | 7 | 24 | 1.2% | 0.2928 |
| 3d2df434 | Gather Merge -> Sort -> Hash Join -> [Ne... | 7 | 24 | 4.5% | 1.0842 |
| f5c4d937 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 7 | 24 | 4.0% | 0.9537 |
| 759d57a4 | Hash Join -> [Nested Loop -> [Hash Join ... | 7 | 24 | 10.7% | 2.5679 |
| c83209ef | Aggregate -> Gather Merge -> Sort -> Has... | 8 | 24 | 1.2% | 0.2928 |
| 991242c7 | Gather Merge -> Sort -> Hash Join -> [Ne... | 8 | 24 | 4.5% | 1.0842 |
| bdf0194d | Sort -> Hash Join -> [Nested Loop -> [Ha... | 8 | 24 | 4.0% | 0.9537 |
| 9d0b7ec3 | Aggregate -> Gather Merge -> Sort -> Has... | 9 | 24 | 1.2% | 0.2928 |
| 1ec32e3e | Gather Merge -> Sort -> Hash Join -> [Ne... | 9 | 24 | 4.5% | 1.0842 |
| e7dc2e6a | Aggregate -> Gather Merge -> Sort -> Has... | 10 | 24 | 1.2% | 0.2928 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 75736.1626 | 0.0004% | ACCEPTED | 17.92% |
| 1 | 3aab37be | 94712.4752 | -0.0000% | REJECTED | 17.92% |
| 2 | 7df893ad | 678.6757 | N/A | REJECTED | 17.92% |
| 3 | 2724c080 | 19.6008 | 0.0222% | ACCEPTED | 17.90% |
| 4 | 2e0f44ef | 108.1433 | -0.0000% | REJECTED | 17.90% |
| 5 | 3cfa90d7 | 6.2269 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 6 | 3e2d5a00 | 18.5791 | N/A | REJECTED | 17.90% |
| 7 | f4cb205a | 41652.9228 | 0.0005% | ACCEPTED | 17.90% |
| 8 | bb930825 | 188.3060 | -0.0000% | REJECTED | 17.90% |
| 9 | c0a8d3de | 540.8859 | 0.0000% | ACCEPTED | 17.90% |
| 10 | e0e3c3e1 | 4.0887 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 11 | 29ee00db | 4.4857 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 12 | 91d6e559 | 3.8554 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 13 | 1e7829bf | 2.5921 | N/A | REJECTED | 17.90% |
| 14 | 37515ad8 | 38.5998 | -0.0000% | REJECTED | 17.90% |
| 15 | a54055ce | 350.8449 | N/A | REJECTED | 17.90% |
| 16 | bd9dfa7b | 3.3586 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 17 | b149ff28 | 1.5277 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 18 | 94a6aee0 | 0.9545 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 19 | 88cd04f5 | 2.5921 | N/A | REJECTED | 17.90% |
| 20 | 9d0e407c | 2.9678 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 21 | 545b5e57 | 25.3429 | N/A | REJECTED | 17.90% |
| 22 | 53f9aa07 | 1.5277 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 23 | 6b43f5a7 | 0.9545 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 24 | 2dab5c22 | 2.5921 | N/A | REJECTED | 17.90% |
| 25 | 27c3eea9 | 0.4758 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 26 | cfb66570 | 0.9545 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 27 | 66a98304 | 2.5921 | N/A | REJECTED | 17.90% |
| 28 | 68382c9c | 0.8338 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 29 | e8907654 | 0.4758 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 30 | f5c4d937 | 0.9545 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 31 | 759d57a4 | 2.5921 | N/A | REJECTED | 17.90% |
| 32 | c83209ef | 0.4758 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 33 | bdf0194d | 0.9545 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 34 | 9d0b7ec3 | 0.4758 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 35 | e7dc2e6a | 0.4758 | N/A | SKIPPED_LOW_ERROR | 17.90% |
## Query Tree

```
Node 11311 (Aggregate) [PATTERN: 2724c080] - ROOT
  Node 11312 (Gather Merge) [consumed]
    Node 11313 (Sort)
      Node 11314 (Hash Join)
        Node 11315 (Nested Loop)
          Node 11316 (Hash Join) [PATTERN: 895c6e8c]
            Node 11317 (Seq Scan) [consumed] - LEAF
            Node 11318 (Hash) [consumed]
              Node 11319 (Hash Join) [PATTERN: f4cb205a]
                Node 11320 (Seq Scan) [consumed] - LEAF
                Node 11321 (Hash) [consumed]
                  Node 11322 (Seq Scan) [consumed] - LEAF
          Node 11323 (Index Scan) - LEAF
        Node 11324 (Hash)
          Node 11325 (Hash Join) [PATTERN: f4cb205a]
            Node 11326 (Seq Scan) [consumed] - LEAF
            Node 11327 (Hash) [consumed]
              Node 11328 (Seq Scan) [consumed] - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Hash Join -> [Seq Scan (Outer) | f4cb205a | 11319 | 11311, 11312, 11316, 11317, 11318, 11320, 11321, 11322, 11325, 11326, 11327, 11328 |
| Hash Join -> [Seq Scan (Outer) | f4cb205a | 11325 | 11311, 11312, 11316, 11317, 11318, 11319, 11320, 11321, 11322, 11326, 11327, 11328 |
| Hash Join -> [Seq Scan (Outer) | 895c6e8c | 11316 | 11311, 11312, 11317, 11318, 11319, 11320, 11321, 11322, 11325, 11326, 11327, 11328 |
| Aggregate -> Gather Merge (Out | 2724c080 | 11311 | 11312, 11316, 11317, 11318, 11319, 11320, 11321, 11322, 11325, 11326, 11327, 11328 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 1.73%
- Improvement: -0.55%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 11311 | Aggregate | 1208.55 | 1187.65 | 1.7% | pattern |
| 11313 | Sort | 1202.50 | 1149.81 | 4.4% | operator |
| 11314 | Hash Join | 1201.81 | 1129.06 | 6.1% | operator |
| 11315 | Nested Loop | 1194.40 | 1145.37 | 4.1% | operator |
| 11324 | Hash | 3.43 | 14.94 | 335.0% | operator |
| 11316 | Hash Join | 217.52 | 260.16 | 19.6% | pattern |
| 11323 | Index Scan | 0.03 | 0.09 | 163.5% | operator |
| 11325 | Hash Join | 3.39 | 21.24 | 527.0% | pattern |
| 11319 | Hash Join | 36.22 | 24.82 | 31.5% | pattern |

## Prediction Chain (Bottom-Up)

### Step 1: Node 11319 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** f4cb205a (Hash Join -> [Seq Scan (Outer), Hash -> Seq Scan (Outer) (Inner)])
- **Consumes:** Nodes 11311, 11312, 11316, 11317, 11318, 11320, 11321, 11322, 11325, 11326, 11327, 11328
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
- **Output:** st=0.24, rt=24.82

### Step 2: Node 11316 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 895c6e8c (Hash Join -> [Seq Scan (Outer), Hash (Inner)])
- **Consumes:** Nodes 11311, 11312, 11317, 11318, 11319, 11320, 11321, 11322, 11325, 11326, 11327, 11328
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
- **Output:** st=37.17, rt=260.16

### Step 3: Node 11323 (Index Scan) - LEAF

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
- **Output:** st=0.04, rt=0.09

### Step 4: Node 11325 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** f4cb205a (Hash Join -> [Seq Scan (Outer), Hash -> Seq Scan (Outer) (Inner)])
- **Consumes:** Nodes 11311, 11312, 11316, 11317, 11318, 11319, 11320, 11321, 11322, 11326, 11327, 11328
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
- **Output:** st=0.15, rt=21.24

### Step 5: Node 11315 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=47115
  - nt1=38710
  - nt2=1
  - parallel_workers=0
  - plan_width=124
  - reltuples=0.0000
  - rt1=260.1604
  - rt2=0.0870
  - sel=1.2171
  - st1=37.1684
  - st2=0.0386
  - startup_cost=4481.2100
  - total_cost=62578.9300
- **Output:** st=42.24, rt=1145.37

### Step 6: Node 11324 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=800
  - nt1=800
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=21.2363
  - rt2=0.0000
  - sel=1.0000
  - st1=0.1531
  - st2=0.0000
  - startup_cost=355.1000
  - total_cost=355.1000
- **Output:** st=14.94, rt=14.94

### Step 7: Node 11314 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=1961
  - nt1=47115
  - nt2=800
  - parallel_workers=0
  - plan_width=252
  - reltuples=0.0000
  - rt1=1145.3731
  - rt2=14.9388
  - sel=0.0001
  - st1=42.2433
  - st2=14.9384
  - startup_cost=4846.3100
  - total_cost=63200.9900
- **Output:** st=43.43, rt=1129.06

### Step 8: Node 11313 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=1961
  - nt1=1961
  - nt2=0
  - parallel_workers=0
  - plan_width=252
  - reltuples=0.0000
  - rt1=1129.0568
  - rt2=0.0000
  - sel=1.0000
  - st1=43.4258
  - st2=0.0000
  - startup_cost=63308.2300
  - total_cost=63313.1300
- **Output:** st=1149.22, rt=1149.81

### Step 9: Node 11311 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 2724c080 (Aggregate -> Gather Merge (Outer))
- **Consumes:** Nodes 11312, 11316, 11317, 11318, 11319, 11320, 11321, 11322, 11325, 11326, 11327, 11328
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
- **Output:** st=1184.05, rt=1187.65
