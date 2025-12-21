# Online Prediction Report

**Test Query:** Q9_84_seed_680934573
**Timestamp:** 2025-12-21 17:22:54

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17280 | Operator + Pattern Training |
| Training_Test | 4320 | Pattern Selection Eval |
| Training | 21600 | Final Model Training |
| Test | 2719 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 9.41%

## Phase C: Patterns in Query

- Total Patterns: 64

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 420 | 12818.3% | 53836.8732 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 360 | 40658.7% | 146371.3776 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 210 | 14.4% | 30.2509 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 180 | 4284.6% | 7712.2590 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 150 | 5.7% | 8.5422 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 150 | 9.7% | 14.5467 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 90 | 3.4% | 3.0966 |
| 7524c54c | Aggregate -> Hash Join (Outer) | 2 | 90 | 4.5% | 4.0342 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 90 | 11.3% | 10.1670 |
| 7d4e78be | Hash Join -> [Hash Join (Outer), Hash (I... | 2 | 30 | 5.5% | 1.6532 |
| c0a8d3de | Hash -> Hash Join -> [Seq Scan (Outer), ... | 3 | 180 | 4284.6% | 7712.2590 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 150 | 79.2% | 118.8648 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 90 | 8.1% | 7.2489 |
| 422ae017 | Aggregate -> Hash Join -> [Seq Scan (Out... | 3 | 90 | 4.5% | 4.0342 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 60 | 3.5% | 2.1270 |
| 2e8f3f67 | Gather -> Aggregate -> Hash Join (Outer)... | 3 | 60 | 2.1% | 1.2456 |
| 30d6e09b | Hash Join -> [Hash Join -> [Nested Loop ... | 3 | 30 | 5.5% | 1.6532 |
| 2873b8c3 | Hash Join -> [Nested Loop -> [Seq Scan (... | 3 | 30 | 3.4% | 1.0295 |
| 37515ad8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 150 | 79.2% | 118.8648 |
| efde8b38 | Aggregate -> Gather -> Aggregate -> Hash... | 4 | 60 | 6.0% | 3.6123 |
| af27a52b | Gather -> Aggregate -> Hash Join -> [Seq... | 4 | 60 | 2.1% | 1.2456 |
| 444761fb | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 60 | 46.6% | 27.9372 |
| 7a51ce50 | Hash Join -> [Hash Join -> [Nested Loop ... | 4 | 30 | 5.5% | 1.6532 |
| 310134da | Aggregate -> Gather -> Aggregate -> Hash... | 5 | 60 | 6.0% | 3.6123 |
| ec92bdaa | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 60 | 17.5% | 10.5165 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 53836.8732 | 0.0007% | REJECTED | 17.17% |
| 1 | 3aab37be | 146371.3776 | -0.0000% | REJECTED | 17.17% |
| 2 | 1d35fb97 | 30.2509 | 0.2650% | REJECTED | 17.17% |
| 3 | 7df893ad | 7712.2590 | -0.0000% | REJECTED | 17.17% |
| 4 | 4fc84c77 | 8.5422 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 5 | 2e0f44ef | 14.5467 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 6 | 634cdbe2 | 3.0966 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 7 | 7524c54c | 4.0342 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 8 | c53c4396 | 10.1670 | -0.0000% | REJECTED | 17.17% |
| 9 | 7d4e78be | 1.6532 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 10 | c0a8d3de | 7712.2590 | -0.0000% | REJECTED | 17.17% |
| 11 | bb930825 | 118.8648 | -0.0000% | REJECTED | 17.17% |
| 12 | a5f39f08 | 7.2489 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 13 | 422ae017 | 4.0342 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 14 | b3a45093 | 2.1270 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 15 | 2e8f3f67 | 1.2456 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 16 | 30d6e09b | 1.6532 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 17 | 2873b8c3 | 1.0295 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 18 | 37515ad8 | 118.8648 | -0.0000% | REJECTED | 17.17% |
| 19 | efde8b38 | 3.6123 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 20 | af27a52b | 1.2456 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 21 | 444761fb | 27.9372 | 0.0000% | REJECTED | 17.17% |
| 22 | 7a51ce50 | 1.6532 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 23 | 310134da | 3.6123 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 24 | ec92bdaa | 10.5165 | -0.0000% | REJECTED | 17.17% |
## Query Tree

```
Node 19043 (Sort) - ROOT
  Node 19044 (Aggregate)
    Node 19045 (Gather)
      Node 19046 (Aggregate)
        Node 19047 (Hash Join)
          Node 19048 (Seq Scan) - LEAF
          Node 19049 (Hash)
            Node 19050 (Hash Join)
              Node 19051 (Seq Scan) - LEAF
              Node 19052 (Hash)
                Node 19053 (Hash Join)
                  Node 19054 (Hash Join)
                    Node 19055 (Nested Loop)
                      Node 19056 (Seq Scan) - LEAF
                      Node 19057 (Index Scan) - LEAF
                    Node 19058 (Hash)
                      Node 19059 (Seq Scan) - LEAF
                  Node 19060 (Hash)
                    Node 19061 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 9.64%
- Improvement: -0.23%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 19043 | Sort | 1239.24 | 1119.81 | 9.6% | operator |
| 19044 | Aggregate | 1239.12 | 916.13 | 26.1% | operator |
| 19045 | Gather | 1238.21 | 962.19 | 22.3% | operator |
| 19046 | Aggregate | 1221.05 | 922.15 | 24.5% | operator |
| 19047 | Hash Join | 1192.52 | 572.47 | 52.0% | operator |
| 19048 | Seq Scan | 132.07 | 193.40 | 46.4% | operator |
| 19049 | Hash | 999.25 | 111.27 | 88.9% | operator |
| 19050 | Hash Join | 981.43 | 634.24 | 35.4% | operator |
| 19051 | Seq Scan | 652.85 | 509.93 | 21.9% | operator |
| 19052 | Hash | 212.56 | 48.50 | 77.2% | operator |
| 19053 | Hash Join | 209.91 | 924.68 | 340.5% | operator |
| 19054 | Hash Join | 194.16 | 837.74 | 331.5% | operator |
| 19060 | Hash | 14.84 | 14.95 | 0.7% | operator |
| 19055 | Nested Loop | 187.21 | 1251.77 | 568.7% | operator |
| 19058 | Hash | 4.56 | 15.94 | 249.3% | operator |
| 19061 | Seq Scan | 14.82 | 2.94 | 80.2% | operator |
| 19056 | Seq Scan | 27.38 | 43.69 | 59.6% | operator |
| 19057 | Index Scan | 0.06 | -1.39 | 2494.0% | operator |
| 19059 | Seq Scan | 4.14 | 9.45 | 128.0% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 19056 (Seq Scan) - LEAF

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

### Step 2: Node 19057 (Index Scan) - LEAF

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

### Step 3: Node 19059 (Seq Scan) - LEAF

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

### Step 4: Node 19055 (Nested Loop)

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

### Step 5: Node 19058 (Hash)

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

### Step 6: Node 19061 (Seq Scan) - LEAF

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

### Step 7: Node 19054 (Hash Join)

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

### Step 8: Node 19060 (Hash)

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

### Step 9: Node 19053 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=22712
  - nt1=22712
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=837.7383
  - rt2=14.9479
  - sel=0.0400
  - st1=121.4600
  - st2=14.9467
  - startup_cost=449.9900
  - total_cost=15845.4100
- **Output:** st=105.88, rt=924.68

### Step 10: Node 19051 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=1200243
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=29
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.2000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=124602.4300
- **Output:** st=7.90, rt=509.93

### Step 11: Node 19052 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=22712
  - nt1=22712
  - nt2=0
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=924.6845
  - rt2=0.0000
  - sel=1.0000
  - st1=105.8844
  - st2=0.0000
  - startup_cost=15845.4100
  - total_cost=15845.4100
- **Output:** st=48.50, rt=48.50

### Step 12: Node 19050 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=81779
  - nt1=1200243
  - nt2=22712
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=509.9269
  - rt2=48.5025
  - sel=0.0000
  - st1=7.9002
  - st2=48.5011
  - startup_cost=16186.0900
  - total_cost=149790.4800
- **Output:** st=73.44, rt=634.24

### Step 13: Node 19048 (Seq Scan) - LEAF

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

### Step 14: Node 19049 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=81779
  - nt1=81779
  - nt2=0
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=634.2404
  - rt2=0.0000
  - sel=1.0000
  - st1=73.4436
  - st2=0.0000
  - startup_cost=149790.4800
  - total_cost=149790.4800
- **Output:** st=111.27, rt=111.27

### Step 15: Node 19047 (Hash Join)

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
  - rt2=111.2732
  - sel=0.0000
  - st1=0.1618
  - st2=111.2717
  - startup_cost=150812.7200
  - total_cost=184195.5000
- **Output:** st=81.95, rt=572.47

### Step 16: Node 19046 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=131901
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=572.4660
  - rt2=0.0000
  - sel=0.4560
  - st1=81.9506
  - st2=0.0000
  - startup_cost=186503.7600
  - total_cost=187406.0100
- **Output:** st=934.73, rt=922.15

### Step 17: Node 19045 (Gather)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=180450
  - nt1=60150
  - nt2=0
  - parallel_workers=3
  - plan_width=168
  - reltuples=0.0000
  - rt1=922.1476
  - rt2=0.0000
  - sel=3.0000
  - st1=934.7344
  - st2=0.0000
  - startup_cost=187503.7600
  - total_cost=206451.0100
- **Output:** st=470.51, rt=962.19

### Step 18: Node 19044 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=180450
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=962.1881
  - rt2=0.0000
  - sel=0.3333
  - st1=470.5109
  - st2=0.0000
  - startup_cost=208255.5100
  - total_cost=209157.7600
- **Output:** st=919.85, rt=916.13

### Step 19: Node 19043 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=60150
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=916.1329
  - rt2=0.0000
  - sel=1.0000
  - st1=919.8516
  - st2=0.0000
  - startup_cost=213932.5500
  - total_cost=214082.9300
- **Output:** st=1119.07, rt=1119.81
