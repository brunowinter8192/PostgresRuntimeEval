# Online Prediction Report

**Test Query:** Q7_129_seed_1050115968
**Timestamp:** 2026-01-11 20:39:55

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 0.99%

## Phase C: Patterns in Query

- Total Patterns: 44

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
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| 3e2d5a00 | Sort -> Hash Join (Outer) | 2 | 96 | 19.3% | 18.5586 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 96 | 7.6% | 7.3257 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 140 | 4.5% | 6.2375 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 96 | 4.7% | 4.4662 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 116 | 3.5% | 4.0772 |
| 91d6e559 | Sort -> Hash Join -> [Nested Loop (Outer... | 3 | 72 | 5.4% | 3.8546 |
| bd9dfa7b | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 92 | 3.7% | 3.3601 |
| 3c6d8006 | Gather Merge -> Sort -> Hash Join -> [Ne... | 4 | 48 | 6.2% | 2.9727 |
| 98d4ff98 | Gather Merge -> Sort -> Hash Join (Outer... | 3 | 48 | 6.2% | 2.9727 |
| 9d0e407c | Nested Loop -> [Hash Join -> [Seq Scan (... | 5 | 72 | 4.1% | 2.9587 |
| 1e7829bf | Hash Join -> [Nested Loop -> [Hash Join ... | 3 | 24 | 10.7% | 2.5679 |
| 2dab5c22 | Hash Join -> [Nested Loop -> [Hash Join ... | 5 | 24 | 10.7% | 2.5679 |
| 66a98304 | Hash Join -> [Nested Loop -> [Hash Join ... | 6 | 24 | 10.7% | 2.5679 |
| 759d57a4 | Hash Join -> [Nested Loop -> [Hash Join ... | 7 | 24 | 10.7% | 2.5679 |
| 88cd04f5 | Hash Join -> [Nested Loop -> [Hash Join ... | 4 | 24 | 10.7% | 2.5679 |
| 1ec32e3e | Gather Merge -> Sort -> Hash Join -> [Ne... | 9 | 24 | 4.5% | 1.0842 |
| 34811571 | Gather Merge -> Sort -> Hash Join -> [Ne... | 6 | 24 | 4.5% | 1.0842 |
| 3d2df434 | Gather Merge -> Sort -> Hash Join -> [Ne... | 7 | 24 | 4.5% | 1.0842 |
| 814388b1 | Gather Merge -> Sort -> Hash Join -> [Ne... | 5 | 24 | 4.5% | 1.0842 |
| 991242c7 | Gather Merge -> Sort -> Hash Join -> [Ne... | 8 | 24 | 4.5% | 1.0842 |
| 53f9aa07 | Aggregate -> Gather Merge -> Sort -> Has... | 5 | 48 | 2.2% | 1.0579 |
| b149ff28 | Aggregate -> Gather Merge -> Sort -> Has... | 4 | 48 | 2.2% | 1.0579 |
| 6b43f5a7 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 5 | 24 | 4.0% | 0.9537 |
| 94a6aee0 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 4 | 24 | 4.0% | 0.9537 |
| bdf0194d | Sort -> Hash Join -> [Nested Loop -> [Ha... | 8 | 24 | 4.0% | 0.9537 |
| cfb66570 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 6 | 24 | 4.0% | 0.9537 |
| f5c4d937 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 7 | 24 | 4.0% | 0.9537 |
| 68382c9c | Nested Loop -> [Hash Join -> [Seq Scan (... | 6 | 24 | 3.4% | 0.8246 |
| 27c3eea9 | Aggregate -> Gather Merge -> Sort -> Has... | 6 | 24 | 1.2% | 0.2928 |
| 9d0b7ec3 | Aggregate -> Gather Merge -> Sort -> Has... | 9 | 24 | 1.2% | 0.2928 |
| c83209ef | Aggregate -> Gather Merge -> Sort -> Has... | 8 | 24 | 1.2% | 0.2928 |
| e7dc2e6a | Aggregate -> Gather Merge -> Sort -> Has... | 10 | 24 | 1.2% | 0.2928 |
| e8907654 | Aggregate -> Gather Merge -> Sort -> Has... | 7 | 24 | 1.2% | 0.2928 |

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
| 10 | 2724c080 | 19.6006 | 0.0222% | ACCEPTED | 17.90% |
| 11 | 3e2d5a00 | 18.4265 | N/A | REJECTED | 17.90% |
| 12 | 29ee00db | 4.4857 | 0.2706% | ACCEPTED | 17.63% |
| 13 | 3cfa90d7 | 4.0055 | N/A | REJECTED | 17.63% |
| 14 | e0e3c3e1 | 3.3189 | 0.0000% | ACCEPTED | 17.63% |
| 15 | 1e7829bf | 2.5690 | N/A | REJECTED | 17.63% |
| 16 | 2dab5c22 | 2.5690 | N/A | REJECTED | 17.63% |
| 17 | 66a98304 | 2.5690 | N/A | REJECTED | 17.63% |
| 18 | 759d57a4 | 2.5690 | N/A | REJECTED | 17.63% |
| 19 | 88cd04f5 | 2.5690 | N/A | REJECTED | 17.63% |
| 20 | bd9dfa7b | 2.5603 | 0.0000% | ACCEPTED | 17.63% |
| 21 | 9d0e407c | 2.4353 | N/A | REJECTED | 17.63% |
| 22 | 53f9aa07 | 1.3983 | 0.2414% | ACCEPTED | 17.39% |
| 23 | 91d6e559 | 1.3357 | N/A | REJECTED | 17.39% |
| 24 | b149ff28 | 0.5871 | N/A | REJECTED | 17.39% |
| 25 | 27c3eea9 | 0.2775 | 0.0001% | ACCEPTED | 17.39% |
| 26 | 9d0b7ec3 | 0.2770 | N/A | REJECTED | 17.39% |
| 27 | c83209ef | 0.2770 | N/A | REJECTED | 17.39% |
| 28 | e7dc2e6a | 0.2770 | N/A | REJECTED | 17.39% |
| 29 | e8907654 | 0.2770 | N/A | REJECTED | 17.39% |
## Query Tree

```
Node 11059 (Aggregate) [PATTERN: 27c3eea9] - ROOT
  Node 11060 (Gather Merge) [consumed]
    Node 11061 (Sort) [consumed]
      Node 11062 (Hash Join) [consumed]
        Node 11063 (Nested Loop) [consumed]
          Node 11064 (Hash Join) [consumed]
            Node 11065 (Seq Scan) - LEAF
            Node 11066 (Hash) [PATTERN: a54055ce]
              Node 11067 (Hash Join) [consumed]
                Node 11068 (Seq Scan) [consumed] - LEAF
                Node 11069 (Hash) [consumed]
                  Node 11070 (Seq Scan) [consumed] - LEAF
          Node 11071 (Index Scan) [consumed] - LEAF
        Node 11072 (Hash) [consumed]
          Node 11073 (Hash Join) [consumed]
            Node 11074 (Seq Scan) - LEAF
            Node 11075 (Hash)
              Node 11076 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather Merge -> S | 27c3eea9 | 11059 | 11060, 11061, 11062, 11063, 11064, 11066, 11067, 11068, 11069, 11070, 11071, 11072, 11073 |
| Hash -> Hash Join -> [Seq Scan | a54055ce | 11066 | 11059, 11060, 11061, 11062, 11063, 11064, 11067, 11068, 11069, 11070, 11071, 11072, 11073 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 1.55%
- Improvement: -0.56%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 11059 | Aggregate | 1182.61 | 1200.90 | 1.5% | pattern |
| 11065 | Seq Scan | 151.45 | 192.19 | 26.9% | operator |
| 11066 | Hash | 37.01 | 35.59 | 3.8% | pattern |
| 11074 | Seq Scan | 1.85 | 10.62 | 474.8% | operator |
| 11075 | Hash | 0.01 | 14.54 | 111724.3% | operator |
| 11076 | Seq Scan | 0.01 | 7.20 | 65317.7% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 11076 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=1
  - nt=2
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=25.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0800
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=1.3800
- **Output:** st=0.06, rt=7.20

### Step 2: Node 11065 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=483871
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.3226
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=30974.7100
- **Output:** st=0.17, rt=192.19

### Step 3: Node 11066 (Hash) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** a54055ce (Hash -> Hash Join -> [Seq Scan (Outer), Hash -> Seq Scan (Outer) (Inner)] (Outer))
- **Consumes:** Nodes 11059, 11060, 11061, 11062, 11063, 11064, 11067, 11068, 11069, 11070, 11071, 11072, 11073
- **Input Features:**
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=5000
  - HashJoin_Outer_nt1=62500
  - HashJoin_Outer_nt2=2
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=108
  - HashJoin_Outer_reltuples=0.0000
  - HashJoin_Outer_sel=0.0400
  - HashJoin_Outer_startup_cost=1.4000
  - HashJoin_Outer_total_cost=4418.2700
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
  - Hash_np=0
  - Hash_nt=5000
  - Hash_nt1=5000
  - Hash_nt2=0
  - Hash_parallel_workers=0
  - Hash_plan_width=108
  - Hash_reltuples=0.0000
  - Hash_sel=1.0000
  - Hash_startup_cost=4418.2700
  - Hash_total_cost=4418.2700
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
- **Output:** st=35.59, rt=35.59

### Step 4: Node 11074 (Seq Scan) - LEAF

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

### Step 5: Node 11075 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2
  - nt1=2
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=7.1959
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0575
  - st2=0.0000
  - startup_cost=1.3800
  - total_cost=1.3800
- **Output:** st=14.54, rt=14.54

### Step 6: Node 11059 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 27c3eea9 (Aggregate -> Gather Merge -> Sort -> Hash Join -> [Nested Loop -> [Hash Join (Outer), Index Scan (Inner)] (Outer), Hash -> Hash Join (Outer) (Inner)] (Outer) (Outer) (Outer))
- **Consumes:** Nodes 11060, 11061, 11062, 11063, 11064, 11066, 11067, 11068, 11069, 11070, 11071, 11072, 11073
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
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=800
  - HashJoin_Outer_nt1=10000
  - HashJoin_Outer_nt2=2
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=108
  - HashJoin_Outer_reltuples=0.0000
  - HashJoin_Outer_sel=0.0400
  - HashJoin_Outer_startup_cost=1.4000
  - HashJoin_Outer_total_cost=355.1000
  - Hash_Inner_np=0
  - Hash_Inner_nt=800
  - Hash_Inner_nt1=800
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=108
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=355.1000
  - Hash_Inner_total_cost=355.1000
  - IndexScan_Inner_np=112600
  - IndexScan_Inner_nt=1
  - IndexScan_Inner_nt1=0
  - IndexScan_Inner_nt2=0
  - IndexScan_Inner_parallel_workers=0
  - IndexScan_Inner_plan_width=24
  - IndexScan_Inner_reltuples=6001215.0000
  - IndexScan_Inner_sel=0.0000
  - IndexScan_Inner_startup_cost=0.4300
  - IndexScan_Inner_total_cost=0.6400
  - NestedLoop_Outer_np=0
  - NestedLoop_Outer_nt=47115
  - NestedLoop_Outer_nt1=38710
  - NestedLoop_Outer_nt2=1
  - NestedLoop_Outer_parallel_workers=0
  - NestedLoop_Outer_plan_width=124
  - NestedLoop_Outer_reltuples=0.0000
  - NestedLoop_Outer_sel=1.2171
  - NestedLoop_Outer_startup_cost=4481.2100
  - NestedLoop_Outer_total_cost=62578.9300
  - Sort_Outer_np=0
  - Sort_Outer_nt=1961
  - Sort_Outer_nt1=1961
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=252
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=63308.2300
  - Sort_Outer_total_cost=63313.1300
- **Output:** st=1196.63, rt=1200.90
