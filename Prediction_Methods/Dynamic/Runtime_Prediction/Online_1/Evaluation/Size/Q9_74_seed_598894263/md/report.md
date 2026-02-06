# Online Prediction Report

**Test Query:** Q9_74_seed_598894263
**Timestamp:** 2026-01-18 19:13:01

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17280 | Operator + Pattern Training |
| Training_Test | 4320 | Pattern Selection Eval |
| Training | 21600 | Final Model Training |
| Test | 2719 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 10.72%

## Phase C: Patterns in Query

- Total Patterns: 64

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 360 | 40658.7% | 146371.3776 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 210 | 14.4% | 30.2509 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 180 | 4284.6% | 7712.2590 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 150 | 5.7% | 8.5422 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 90 | 3.4% | 3.0966 |
| 7524c54c | Aggregate -> Hash Join (Outer) | 2 | 90 | 4.5% | 4.0342 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 420 | 12818.3% | 53836.8732 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 150 | 9.7% | 14.5467 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 90 | 8.1% | 7.2489 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 90 | 11.3% | 10.1670 |
| 2e8f3f67 | Gather -> Aggregate -> Hash Join (Outer)... | 3 | 60 | 2.1% | 1.2456 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 60 | 3.5% | 2.1270 |
| 7d4e78be | Hash Join -> [Hash Join (Outer), Hash (I... | 2 | 30 | 5.5% | 1.6532 |
| c0a8d3de | Hash -> Hash Join -> [Seq Scan (Outer), ... | 3 | 180 | 4284.6% | 7712.2590 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 150 | 79.2% | 118.8648 |
| 422ae017 | Aggregate -> Hash Join -> [Seq Scan (Out... | 3 | 90 | 4.5% | 4.0342 |
| efde8b38 | Aggregate -> Gather -> Aggregate -> Hash... | 4 | 60 | 6.0% | 3.6123 |
| 444761fb | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 60 | 46.6% | 27.9372 |
| af27a52b | Gather -> Aggregate -> Hash Join -> [Seq... | 4 | 60 | 2.1% | 1.2456 |
| 37515ad8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 150 | 79.2% | 118.8648 |
| 310134da | Aggregate -> Gather -> Aggregate -> Hash... | 5 | 60 | 6.0% | 3.6123 |
| 2873b8c3 | Hash Join -> [Nested Loop -> [Seq Scan (... | 3 | 30 | 3.4% | 1.0295 |
| 30d6e09b | Hash Join -> [Hash Join -> [Nested Loop ... | 3 | 30 | 5.5% | 1.6532 |
| ec92bdaa | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 60 | 17.5% | 10.5165 |
| 7a51ce50 | Hash Join -> [Hash Join -> [Nested Loop ... | 4 | 30 | 5.5% | 1.6532 |
| 6e659102 | Sort -> Aggregate -> Gather -> Aggregate... | 4 | 0 | - | - |
| 8951754f | Sort -> Aggregate -> Gather -> Aggregate... | 5 | 0 | - | - |
| e92539ee | Sort -> Aggregate -> Gather -> Aggregate... | 6 | 0 | - | - |
| fa5db8b6 | Sort -> Aggregate -> Gather -> Aggregate... | 7 | 0 | - | - |
| 57d290cd | Sort -> Aggregate -> Gather -> Aggregate... | 8 | 0 | - | - |
| 6e9566a0 | Sort -> Aggregate -> Gather -> Aggregate... | 9 | 0 | - | - |
| 5968661e | Sort -> Aggregate -> Gather -> Aggregate... | 10 | 0 | - | - |
| a2a9b057 | Sort -> Aggregate -> Gather -> Aggregate... | 11 | 0 | - | - |
| ceeb5cca | Sort -> Aggregate -> Gather -> Aggregate... | 12 | 0 | - | - |
| d0331b81 | Aggregate -> Gather -> Aggregate -> Hash... | 6 | 0 | - | - |
| 2bac8e6e | Aggregate -> Gather -> Aggregate -> Hash... | 7 | 0 | - | - |
| 8259bae3 | Aggregate -> Gather -> Aggregate -> Hash... | 8 | 0 | - | - |
| 4021e47f | Aggregate -> Gather -> Aggregate -> Hash... | 9 | 0 | - | - |
| 45a78037 | Aggregate -> Gather -> Aggregate -> Hash... | 10 | 0 | - | - |
| c65a77da | Aggregate -> Gather -> Aggregate -> Hash... | 11 | 0 | - | - |
| 10ed8951 | Gather -> Aggregate -> Hash Join -> [Seq... | 5 | 0 | - | - |
| 4ecd02f7 | Gather -> Aggregate -> Hash Join -> [Seq... | 6 | 0 | - | - |
| 2eaabdb6 | Gather -> Aggregate -> Hash Join -> [Seq... | 7 | 0 | - | - |
| eb55f880 | Gather -> Aggregate -> Hash Join -> [Seq... | 8 | 0 | - | - |
| 9627c015 | Gather -> Aggregate -> Hash Join -> [Seq... | 9 | 0 | - | - |
| ec6765c4 | Gather -> Aggregate -> Hash Join -> [Seq... | 10 | 0 | - | - |
| 7542faeb | Aggregate -> Hash Join -> [Seq Scan (Out... | 4 | 0 | - | - |
| 5891ae15 | Aggregate -> Hash Join -> [Seq Scan (Out... | 5 | 0 | - | - |
| c57cb4bb | Aggregate -> Hash Join -> [Seq Scan (Out... | 6 | 0 | - | - |
| 6b3fb960 | Aggregate -> Hash Join -> [Seq Scan (Out... | 7 | 0 | - | - |
| d3455a22 | Aggregate -> Hash Join -> [Seq Scan (Out... | 8 | 0 | - | - |
| 800ae9e1 | Aggregate -> Hash Join -> [Seq Scan (Out... | 9 | 0 | - | - |
| 9adbbadc | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 0 | - | - |
| 9a16eb41 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 7 | 0 | - | - |
| f01db5fe | Hash Join -> [Seq Scan (Outer), Hash -> ... | 8 | 0 | - | - |
| 06fbc794 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 5 | 0 | - | - |
| 59d2ec49 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 6 | 0 | - | - |
| d8ffcf0c | Hash -> Hash Join -> [Seq Scan (Outer), ... | 7 | 0 | - | - |
| e941d0ad | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 0 | - | - |
| 49ae7e42 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 0 | - | - |
| ed7f2e45 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 0 | - | - |
| 1a17c7f7 | Hash -> Hash Join -> [Hash Join (Outer),... | 3 | 0 | - | - |
| fee45978 | Hash -> Hash Join -> [Hash Join -> [Nest... | 4 | 0 | - | - |
| 702e1a46 | Hash -> Hash Join -> [Hash Join -> [Nest... | 5 | 0 | - | - |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 3aab37be | 146371.3776 | -0.0000% | REJECTED | 17.17% |
| 1 | 1d35fb97 | 30.2509 | 0.2650% | ACCEPTED | 16.90% |
| 2 | 7df893ad | 7712.2590 | -0.0000% | REJECTED | 16.90% |
| 3 | 4fc84c77 | 8.5422 | N/A | SKIPPED_LOW_ERROR | 16.90% |
| 4 | 634cdbe2 | 3.0966 | N/A | SKIPPED_LOW_ERROR | 16.90% |
| 5 | 7524c54c | 4.0342 | N/A | SKIPPED_LOW_ERROR | 16.90% |
| 6 | 895c6e8c | 53836.8732 | 0.0002% | ACCEPTED | 16.90% |
| 7 | 2e0f44ef | 14.5467 | N/A | SKIPPED_LOW_ERROR | 16.90% |
| 8 | a5f39f08 | 7.2489 | N/A | SKIPPED_LOW_ERROR | 16.90% |
| 9 | c53c4396 | 10.1670 | -0.0000% | REJECTED | 16.90% |
| 10 | 2e8f3f67 | 1.2456 | N/A | SKIPPED_LOW_ERROR | 16.90% |
| 11 | b3a45093 | 2.1270 | N/A | SKIPPED_LOW_ERROR | 16.90% |
| 12 | 7d4e78be | 1.6532 | N/A | SKIPPED_LOW_ERROR | 16.90% |
| 13 | c0a8d3de | 7712.2590 | 0.0000% | ACCEPTED | 16.90% |
| 14 | bb930825 | 118.8648 | N/A | REJECTED | 16.90% |
| 15 | 422ae017 | 4.0342 | N/A | SKIPPED_LOW_ERROR | 16.90% |
| 16 | efde8b38 | 3.6123 | N/A | SKIPPED_LOW_ERROR | 16.90% |
| 17 | 444761fb | 27.9372 | 0.0000% | ACCEPTED | 16.90% |
| 18 | af27a52b | 1.2456 | N/A | SKIPPED_LOW_ERROR | 16.90% |
| 19 | 37515ad8 | 118.8648 | -0.0000% | REJECTED | 16.90% |
| 20 | 310134da | 3.6123 | N/A | SKIPPED_LOW_ERROR | 16.90% |
| 21 | 2873b8c3 | 1.0295 | N/A | SKIPPED_LOW_ERROR | 16.90% |
| 22 | 30d6e09b | 1.6532 | N/A | SKIPPED_LOW_ERROR | 16.90% |
| 23 | ec92bdaa | 10.5165 | -0.0000% | REJECTED | 16.90% |
| 24 | 7a51ce50 | 1.6532 | N/A | SKIPPED_LOW_ERROR | 16.90% |
## Query Tree

```
Node 18843 (Sort) [PATTERN: 1d35fb97] - ROOT
  Node 18844 (Aggregate) [consumed]
    Node 18845 (Gather)
      Node 18846 (Aggregate)
        Node 18847 (Hash Join)
          Node 18848 (Seq Scan) - LEAF
          Node 18849 (Hash) [PATTERN: 444761fb]
            Node 18850 (Hash Join) [consumed]
              Node 18851 (Seq Scan) [consumed] - LEAF
              Node 18852 (Hash) [consumed]
                Node 18853 (Hash Join) [consumed]
                  Node 18854 (Hash Join)
                    Node 18855 (Nested Loop)
                      Node 18856 (Seq Scan) - LEAF
                      Node 18857 (Index Scan) - LEAF
                    Node 18858 (Hash)
                      Node 18859 (Seq Scan) - LEAF
                  Node 18860 (Hash)
                    Node 18861 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Hash -> Hash Join -> [Seq Scan | 444761fb | 18849 | 18843, 18844, 18850, 18851, 18852, 18853 |
| Sort -> Aggregate (Outer) | 1d35fb97 | 18843 | 18844, 18849, 18850, 18851, 18852, 18853 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 15.45%
- Improvement: -4.74%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 18843 | Sort | 1257.43 | 1063.12 | 15.5% | pattern |
| 18845 | Gather | 1256.40 | 962.19 | 23.4% | operator |
| 18846 | Aggregate | 1239.69 | 922.12 | 25.6% | operator |
| 18847 | Hash Join | 1211.03 | 571.38 | 52.8% | operator |
| 18848 | Seq Scan | 125.64 | 193.40 | 53.9% | operator |
| 18849 | Hash | 1023.54 | 35.69 | 96.5% | pattern |
| 18854 | Hash Join | 194.09 | 837.74 | 331.6% | operator |
| 18860 | Hash | 14.96 | 14.95 | 0.1% | operator |
| 18855 | Nested Loop | 187.35 | 1251.77 | 568.1% | operator |
| 18858 | Hash | 4.23 | 15.94 | 277.2% | operator |
| 18861 | Seq Scan | 14.95 | 2.94 | 80.4% | operator |
| 18856 | Seq Scan | 26.19 | 43.69 | 66.8% | operator |
| 18857 | Index Scan | 0.06 | -1.39 | 2453.4% | operator |
| 18859 | Seq Scan | 3.81 | 9.45 | 148.2% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 18856 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=5678
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0284
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=1.77, rt=43.69

### Step 2: Node 18857 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=17560
  - nt=4
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=14
  - reltuples=800000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.4200
  - total_cost=1.7400
- **Output:** st=0.01, rt=-1.39

### Step 3: Node 18859 (Seq Scan) - LEAF

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
- **Output:** st=0.04, rt=9.45

### Step 4: Node 18855 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=22712
  - nt1=5678
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=43.6945
  - rt2=-1.3885
  - sel=1.0000
  - st1=1.7676
  - st2=0.0113
  - startup_cost=0.4200
  - total_cost=15266.4800
- **Output:** st=153.58, rt=1251.77

### Step 5: Node 18858 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=10000
  - nt1=10000
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=0.0000
  - rt1=9.4454
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0398
  - st2=0.0000
  - startup_cost=323.0000
  - total_cost=323.0000
- **Output:** st=15.94, rt=15.94

### Step 6: Node 18861 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=1
  - nt=25
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=25.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=1.2500
- **Output:** st=0.05, rt=2.94

### Step 7: Node 18854 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=22712
  - nt1=22712
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1251.7685
  - rt2=15.9407
  - sel=0.0001
  - st1=153.5771
  - st2=15.9407
  - startup_cost=448.4300
  - total_cost=15774.1200
- **Output:** st=121.46, rt=837.74

### Step 8: Node 18860 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=25
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=2.9371
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0513
  - st2=0.0000
  - startup_cost=1.2500
  - total_cost=1.2500
- **Output:** st=14.95, rt=14.95

### Step 9: Node 18848 (Seq Scan) - LEAF

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
- **Output:** st=0.16, rt=193.40

### Step 10: Node 18849 (Hash) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 444761fb (Hash -> Hash Join -> [Seq Scan (Outer), Hash -> Hash Join (Outer) (Inner)] (Outer))
- **Consumes:** Nodes 18843, 18844, 18850, 18851, 18852, 18853
- **Input Features:**
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=22712
  - HashJoin_Outer_nt1=22712
  - HashJoin_Outer_nt2=25
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=126
  - HashJoin_Outer_reltuples=0.0000
  - HashJoin_Outer_sel=0.0400
  - HashJoin_Outer_startup_cost=449.9900
  - HashJoin_Outer_total_cost=15845.4100
  - Hash_Inner_np=0
  - Hash_Inner_nt=22712
  - Hash_Inner_nt1=22712
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=126
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=15845.4100
  - Hash_Inner_total_cost=15845.4100
  - Hash_np=0
  - Hash_nt=81779
  - Hash_nt1=81779
  - Hash_nt2=0
  - Hash_parallel_workers=0
  - Hash_plan_width=131
  - Hash_reltuples=0.0000
  - Hash_sel=1.0000
  - Hash_startup_cost=149790.4800
  - Hash_total_cost=149790.4800
  - SeqScan_Outer_np=112600
  - SeqScan_Outer_nt=1200243
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=29
  - SeqScan_Outer_reltuples=6001215.0000
  - SeqScan_Outer_sel=0.2000
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=124602.4300
- **Output:** st=35.69, rt=35.69

### Step 11: Node 18847 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=131901
  - nt1=483871
  - nt2=81779
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=193.4002
  - rt2=35.6935
  - sel=0.0000
  - st1=0.1618
  - st2=35.6925
  - startup_cost=150812.7200
  - total_cost=184195.5000
- **Output:** st=81.06, rt=571.38

### Step 12: Node 18846 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=131901
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=571.3800
  - rt2=0.0000
  - sel=0.4560
  - st1=81.0617
  - st2=0.0000
  - startup_cost=186503.7600
  - total_cost=187406.0100
- **Output:** st=934.68, rt=922.12

### Step 13: Node 18845 (Gather)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=180450
  - nt1=60150
  - nt2=0
  - parallel_workers=3
  - plan_width=168
  - reltuples=0.0000
  - rt1=922.1206
  - rt2=0.0000
  - sel=3.0000
  - st1=934.6849
  - st2=0.0000
  - startup_cost=187503.7600
  - total_cost=206451.0100
- **Output:** st=470.51, rt=962.19

### Step 14: Node 18843 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 1d35fb97 (Sort -> Aggregate (Outer))
- **Consumes:** Nodes 18844, 18849, 18850, 18851, 18852, 18853
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=60150
  - Aggregate_Outer_nt1=180450
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=168
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.3333
  - Aggregate_Outer_startup_cost=208255.5100
  - Aggregate_Outer_total_cost=209157.7600
  - Sort_np=0
  - Sort_nt=60150
  - Sort_nt1=60150
  - Sort_nt2=0
  - Sort_parallel_workers=0
  - Sort_plan_width=168
  - Sort_reltuples=0.0000
  - Sort_sel=1.0000
  - Sort_startup_cost=213932.5500
  - Sort_total_cost=214082.9300
- **Output:** st=1062.20, rt=1063.12
