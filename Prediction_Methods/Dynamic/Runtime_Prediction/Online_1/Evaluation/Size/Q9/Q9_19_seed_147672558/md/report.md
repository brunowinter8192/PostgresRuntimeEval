# Online Prediction Report

**Test Query:** Q9_19_seed_147672558
**Timestamp:** 2025-12-21 17:14:50

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17280 | Operator + Pattern Training |
| Training_Test | 4320 | Pattern Selection Eval |
| Training | 21600 | Final Model Training |
| Test | 2719 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 9.35%

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
Node 17738 (Sort) - ROOT
  Node 17739 (Aggregate)
    Node 17740 (Gather)
      Node 17741 (Aggregate)
        Node 17742 (Hash Join)
          Node 17743 (Seq Scan) - LEAF
          Node 17744 (Hash)
            Node 17745 (Hash Join)
              Node 17746 (Seq Scan) - LEAF
              Node 17747 (Hash)
                Node 17748 (Hash Join)
                  Node 17749 (Hash Join)
                    Node 17750 (Nested Loop)
                      Node 17751 (Seq Scan) - LEAF
                      Node 17752 (Index Scan) - LEAF
                    Node 17753 (Hash)
                      Node 17754 (Seq Scan) - LEAF
                  Node 17755 (Hash)
                    Node 17756 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 9.57%
- Improvement: -0.23%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 17738 | Sort | 1238.74 | 1120.16 | 9.6% | operator |
| 17739 | Aggregate | 1238.59 | 916.31 | 26.0% | operator |
| 17740 | Gather | 1237.76 | 962.35 | 22.3% | operator |
| 17741 | Aggregate | 1220.02 | 902.75 | 26.0% | operator |
| 17742 | Hash Join | 1191.48 | 581.30 | 51.2% | operator |
| 17743 | Seq Scan | 129.36 | 193.40 | 49.5% | operator |
| 17744 | Hash | 1000.54 | 114.84 | 88.5% | operator |
| 17745 | Hash Join | 982.84 | 635.37 | 35.4% | operator |
| 17746 | Seq Scan | 655.64 | 509.93 | 22.2% | operator |
| 17747 | Hash | 210.07 | 49.25 | 76.6% | operator |
| 17748 | Hash Join | 207.38 | 924.97 | 346.0% | operator |
| 17749 | Hash Join | 191.91 | 837.88 | 336.6% | operator |
| 17755 | Hash | 14.57 | 14.95 | 2.6% | operator |
| 17750 | Nested Loop | 184.97 | 1251.77 | 576.8% | operator |
| 17753 | Hash | 4.40 | 15.94 | 262.0% | operator |
| 17756 | Seq Scan | 14.56 | 2.94 | 79.8% | operator |
| 17751 | Seq Scan | 27.75 | 43.30 | 56.0% | operator |
| 17752 | Index Scan | 0.06 | -1.39 | 2536.0% | operator |
| 17754 | Seq Scan | 3.98 | 9.45 | 137.3% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 17751 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=6680
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0334
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=1.73, rt=43.30

### Step 2: Node 17752 (Index Scan) - LEAF

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
  - total_cost=1.6000
- **Output:** st=0.01, rt=-1.39

### Step 3: Node 17754 (Seq Scan) - LEAF

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

### Step 4: Node 17750 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=26720
  - nt1=6680
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=43.3005
  - rt2=-1.3885
  - sel=1.0000
  - st1=1.7284
  - st2=0.0113
  - startup_cost=0.4200
  - total_cost=16109.2300
- **Output:** st=153.58, rt=1251.77

### Step 5: Node 17753 (Hash)

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

### Step 6: Node 17756 (Seq Scan) - LEAF

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

### Step 7: Node 17749 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=26720
  - nt1=26720
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1251.7721
  - rt2=15.9407
  - sel=0.0001
  - st1=153.5785
  - st2=15.9407
  - startup_cost=448.4300
  - total_cost=16627.4000
- **Output:** st=121.48, rt=837.88

### Step 8: Node 17755 (Hash)

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

### Step 9: Node 17748 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=26720
  - nt1=26720
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=837.8830
  - rt2=14.9479
  - sel=0.0400
  - st1=121.4791
  - st2=14.9467
  - startup_cost=449.9900
  - total_cost=16710.9900
- **Output:** st=105.92, rt=924.97

### Step 10: Node 17746 (Seq Scan) - LEAF

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

### Step 11: Node 17747 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=26720
  - nt1=26720
  - nt2=0
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=924.9686
  - rt2=0.0000
  - sel=1.0000
  - st1=105.9180
  - st2=0.0000
  - startup_cost=16710.9900
  - total_cost=16710.9900
- **Output:** st=49.24, rt=49.25

### Step 12: Node 17745 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=96211
  - nt1=1200243
  - nt2=26720
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=509.9269
  - rt2=49.2455
  - sel=0.0000
  - st1=7.9002
  - st2=49.2441
  - startup_cost=17111.7900
  - total_cost=150716.2100
- **Output:** st=72.82, rt=635.37

### Step 13: Node 17743 (Seq Scan) - LEAF

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

### Step 14: Node 17744 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=96211
  - nt1=96211
  - nt2=0
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=635.3665
  - rt2=0.0000
  - sel=1.0000
  - st1=72.8233
  - st2=0.0000
  - startup_cost=150716.2100
  - total_cost=150716.2100
- **Output:** st=114.84, rt=114.84

### Step 15: Node 17742 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=155180
  - nt1=483871
  - nt2=96211
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=193.4002
  - rt2=114.8439
  - sel=0.0000
  - st1=0.1618
  - st2=114.8424
  - startup_cost=151918.8400
  - total_cost=185406.3800
- **Output:** st=82.17, rt=581.30

### Step 16: Node 17741 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=155180
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=581.3003
  - rt2=0.0000
  - sel=0.3876
  - st1=82.1749
  - st2=0.0000
  - startup_cost=188122.0300
  - total_cost=189024.2800
- **Output:** st=915.58, rt=902.75

### Step 17: Node 17740 (Gather)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=180450
  - nt1=60150
  - nt2=0
  - parallel_workers=3
  - plan_width=168
  - reltuples=0.0000
  - rt1=902.7526
  - rt2=0.0000
  - sel=3.0000
  - st1=915.5801
  - st2=0.0000
  - startup_cost=189122.0300
  - total_cost=208069.2800
- **Output:** st=470.14, rt=962.35

### Step 18: Node 17739 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=180450
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=962.3460
  - rt2=0.0000
  - sel=0.3333
  - st1=470.1429
  - st2=0.0000
  - startup_cost=209873.7800
  - total_cost=210776.0300
- **Output:** st=919.24, rt=916.31

### Step 19: Node 17738 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=60150
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=916.3129
  - rt2=0.0000
  - sel=1.0000
  - st1=919.2359
  - st2=0.0000
  - startup_cost=215550.8200
  - total_cost=215701.2000
- **Output:** st=1119.41, rt=1120.16
