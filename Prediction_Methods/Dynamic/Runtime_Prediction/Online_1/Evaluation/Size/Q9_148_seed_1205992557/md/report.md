# Online Prediction Report

**Test Query:** Q9_148_seed_1205992557
**Timestamp:** 2025-12-21 17:13:09

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17280 | Operator + Pattern Training |
| Training_Test | 4320 | Pattern Selection Eval |
| Training | 21600 | Final Model Training |
| Test | 2719 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 12.62%

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
Node 17592 (Sort) - ROOT
  Node 17593 (Aggregate)
    Node 17594 (Gather)
      Node 17595 (Aggregate)
        Node 17596 (Hash Join)
          Node 17597 (Seq Scan) - LEAF
          Node 17598 (Hash)
            Node 17599 (Hash Join)
              Node 17600 (Seq Scan) - LEAF
              Node 17601 (Hash)
                Node 17602 (Hash Join)
                  Node 17603 (Hash Join)
                    Node 17604 (Nested Loop)
                      Node 17605 (Seq Scan) - LEAF
                      Node 17606 (Index Scan) - LEAF
                    Node 17607 (Hash)
                      Node 17608 (Seq Scan) - LEAF
                  Node 17609 (Hash)
                    Node 17610 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 12.85%
- Improvement: -0.22%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 17592 | Sort | 1284.76 | 1119.70 | 12.8% | operator |
| 17593 | Aggregate | 1284.63 | 916.08 | 28.7% | operator |
| 17594 | Gather | 1284.00 | 962.11 | 25.1% | operator |
| 17595 | Aggregate | 1266.84 | 931.09 | 26.5% | operator |
| 17596 | Hash Join | 1239.42 | 569.62 | 54.0% | operator |
| 17597 | Seq Scan | 127.97 | 193.40 | 51.1% | operator |
| 17598 | Hash | 1048.57 | 110.13 | 89.5% | operator |
| 17599 | Hash Join | 1030.42 | 633.87 | 38.5% | operator |
| 17600 | Seq Scan | 699.85 | 509.93 | 27.1% | operator |
| 17601 | Hash | 215.62 | 48.26 | 77.6% | operator |
| 17602 | Hash Join | 213.15 | 924.58 | 333.8% | operator |
| 17603 | Hash Join | 198.00 | 837.69 | 323.1% | operator |
| 17609 | Hash | 14.24 | 14.95 | 4.9% | operator |
| 17604 | Nested Loop | 191.46 | 1251.77 | 553.8% | operator |
| 17607 | Hash | 3.98 | 15.94 | 301.0% | operator |
| 17610 | Seq Scan | 14.23 | 2.94 | 79.4% | operator |
| 17605 | Seq Scan | 25.66 | 43.83 | 70.8% | operator |
| 17606 | Index Scan | 0.06 | -1.39 | 2414.2% | operator |
| 17608 | Seq Scan | 3.56 | 9.45 | 165.0% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 17605 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=5344
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0267
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=1.78, rt=43.83

### Step 2: Node 17606 (Index Scan) - LEAF

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
  - total_cost=1.8000
- **Output:** st=0.01, rt=-1.39

### Step 3: Node 17608 (Seq Scan) - LEAF

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

### Step 4: Node 17604 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=21377
  - nt1=5344
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=43.8279
  - rt2=-1.3885
  - sel=1.0000
  - st1=1.7807
  - st2=0.0113
  - startup_cost=0.4200
  - total_cost=14978.4200
- **Output:** st=153.58, rt=1251.77

### Step 5: Node 17607 (Hash)

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

### Step 6: Node 17610 (Seq Scan) - LEAF

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

### Step 7: Node 17603 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=21377
  - nt1=21377
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1251.7674
  - rt2=15.9407
  - sel=0.0001
  - st1=153.5768
  - st2=15.9407
  - startup_cost=448.4300
  - total_cost=15482.5600
- **Output:** st=121.45, rt=837.69

### Step 8: Node 17609 (Hash)

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

### Step 9: Node 17602 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=21377
  - nt1=21377
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=837.6868
  - rt2=14.9479
  - sel=0.0400
  - st1=121.4533
  - st2=14.9467
  - startup_cost=449.9900
  - total_cost=15549.7500
- **Output:** st=105.87, rt=924.58

### Step 10: Node 17600 (Seq Scan) - LEAF

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

### Step 11: Node 17601 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=21377
  - nt1=21377
  - nt2=0
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=924.5838
  - rt2=0.0000
  - sel=1.0000
  - st1=105.8727
  - st2=0.0000
  - startup_cost=15549.7500
  - total_cost=15549.7500
- **Output:** st=48.26, rt=48.26

### Step 12: Node 17599 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=76972
  - nt1=1200243
  - nt2=21377
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=509.9269
  - rt2=48.2622
  - sel=0.0000
  - st1=7.9002
  - st2=48.2608
  - startup_cost=15870.4100
  - total_cost=149474.7900
- **Output:** st=73.65, rt=633.87

### Step 13: Node 17597 (Seq Scan) - LEAF

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

### Step 14: Node 17598 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=76972
  - nt1=76972
  - nt2=0
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=633.8711
  - rt2=0.0000
  - sel=1.0000
  - st1=73.6506
  - st2=0.0000
  - startup_cost=149474.7900
  - total_cost=149474.7900
- **Output:** st=110.13, rt=110.13

### Step 15: Node 17596 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=124148
  - nt1=483871
  - nt2=76972
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=193.4002
  - rt2=110.1306
  - sel=0.0000
  - st1=0.1618
  - st2=110.1292
  - startup_cost=150436.9400
  - total_cost=183784.8300
- **Output:** st=81.93, rt=569.62

### Step 16: Node 17595 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=124148
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=569.6177
  - rt2=0.0000
  - sel=0.4845
  - st1=81.9264
  - st2=0.0000
  - startup_cost=185957.4200
  - total_cost=186859.6700
- **Output:** st=943.29, rt=931.09

### Step 17: Node 17594 (Gather)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=180450
  - nt1=60150
  - nt2=0
  - parallel_workers=3
  - plan_width=168
  - reltuples=0.0000
  - rt1=931.0933
  - rt2=0.0000
  - sel=3.0000
  - st1=943.2937
  - st2=0.0000
  - startup_cost=186957.4200
  - total_cost=205904.6700
- **Output:** st=470.71, rt=962.11

### Step 18: Node 17593 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=180450
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=962.1128
  - rt2=0.0000
  - sel=0.3333
  - st1=470.7058
  - st2=0.0000
  - startup_cost=207709.1700
  - total_cost=208611.4200
- **Output:** st=920.07, rt=916.08

### Step 19: Node 17592 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=60150
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=916.0804
  - rt2=0.0000
  - sel=1.0000
  - st1=920.0654
  - st2=0.0000
  - startup_cost=213386.2100
  - total_cost=213536.5900
- **Output:** st=1118.95, rt=1119.70
