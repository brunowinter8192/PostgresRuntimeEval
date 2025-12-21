# Online Prediction Report

**Test Query:** Q9_62_seed_500445891
**Timestamp:** 2025-12-21 17:19:33

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17280 | Operator + Pattern Training |
| Training_Test | 4320 | Pattern Selection Eval |
| Training | 21600 | Final Model Training |
| Test | 2719 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 12.34%

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
Node 18606 (Sort) - ROOT
  Node 18607 (Aggregate)
    Node 18608 (Gather)
      Node 18609 (Aggregate)
        Node 18610 (Hash Join)
          Node 18611 (Seq Scan) - LEAF
          Node 18612 (Hash)
            Node 18613 (Hash Join)
              Node 18614 (Seq Scan) - LEAF
              Node 18615 (Hash)
                Node 18616 (Hash Join)
                  Node 18617 (Hash Join)
                    Node 18618 (Nested Loop)
                      Node 18619 (Seq Scan) - LEAF
                      Node 18620 (Index Scan) - LEAF
                    Node 18621 (Hash)
                      Node 18622 (Seq Scan) - LEAF
                  Node 18623 (Hash)
                    Node 18624 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 12.56%
- Improvement: -0.22%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 18606 | Sort | 1280.63 | 1119.76 | 12.6% | operator |
| 18607 | Aggregate | 1280.49 | 916.11 | 28.5% | operator |
| 18608 | Gather | 1279.49 | 962.15 | 24.8% | operator |
| 18609 | Aggregate | 1263.15 | 926.43 | 26.7% | operator |
| 18610 | Hash Join | 1234.14 | 571.03 | 53.7% | operator |
| 18611 | Seq Scan | 126.82 | 193.40 | 52.5% | operator |
| 18612 | Hash | 1044.83 | 110.70 | 89.4% | operator |
| 18613 | Hash Join | 1026.88 | 634.06 | 38.3% | operator |
| 18614 | Seq Scan | 686.99 | 509.93 | 25.8% | operator |
| 18615 | Hash | 220.82 | 48.38 | 78.1% | operator |
| 18616 | Hash Join | 218.66 | 924.63 | 322.9% | operator |
| 18617 | Hash Join | 202.98 | 837.71 | 312.7% | operator |
| 18623 | Hash | 14.79 | 14.95 | 1.1% | operator |
| 18618 | Nested Loop | 194.77 | 1251.77 | 542.7% | operator |
| 18621 | Hash | 5.72 | 15.94 | 178.7% | operator |
| 18624 | Seq Scan | 14.78 | 2.94 | 80.1% | operator |
| 18619 | Seq Scan | 26.35 | 43.76 | 66.1% | operator |
| 18620 | Index Scan | 0.06 | -1.39 | 2376.2% | operator |
| 18622 | Seq Scan | 5.24 | 9.45 | 80.3% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 18619 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=5511
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0276
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=1.77, rt=43.76

### Step 2: Node 18620 (Index Scan) - LEAF

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
  - total_cost=1.7700
- **Output:** st=0.01, rt=-1.39

### Step 3: Node 18622 (Seq Scan) - LEAF

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

### Step 4: Node 18618 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=22043
  - nt1=5511
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=43.7610
  - rt2=-1.3885
  - sel=1.0000
  - st1=1.7742
  - st2=0.0113
  - startup_cost=0.4200
  - total_cost=15123.1100
- **Output:** st=153.58, rt=1251.77

### Step 5: Node 18621 (Hash)

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

### Step 6: Node 18624 (Seq Scan) - LEAF

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

### Step 7: Node 18617 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=22043
  - nt1=22043
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1251.7679
  - rt2=15.9407
  - sel=0.0001
  - st1=153.5769
  - st2=15.9407
  - startup_cost=448.4300
  - total_cost=15628.9900
- **Output:** st=121.46, rt=837.71

### Step 8: Node 18623 (Hash)

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

### Step 9: Node 18616 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=22043
  - nt1=22043
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=837.7128
  - rt2=14.9479
  - sel=0.0400
  - st1=121.4567
  - st2=14.9467
  - startup_cost=449.9900
  - total_cost=15698.2300
- **Output:** st=105.88, rt=924.63

### Step 10: Node 18614 (Seq Scan) - LEAF

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

### Step 11: Node 18615 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=22043
  - nt1=22043
  - nt2=0
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=924.6346
  - rt2=0.0000
  - sel=1.0000
  - st1=105.8786
  - st2=0.0000
  - startup_cost=15698.2300
  - total_cost=15698.2300
- **Output:** st=48.38, rt=48.38

### Step 12: Node 18613 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=79372
  - nt1=1200243
  - nt2=22043
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=509.9269
  - rt2=48.3817
  - sel=0.0000
  - st1=7.9002
  - st2=48.3803
  - startup_cost=16028.8800
  - total_cost=149633.2600
- **Output:** st=73.55, rt=634.06

### Step 13: Node 18611 (Seq Scan) - LEAF

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

### Step 14: Node 18612 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=79372
  - nt1=79372
  - nt2=0
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=634.0553
  - rt2=0.0000
  - sel=1.0000
  - st1=73.5473
  - st2=0.0000
  - startup_cost=149633.2600
  - total_cost=149633.2600
- **Output:** st=110.70, rt=110.70

### Step 15: Node 18610 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=128019
  - nt1=483871
  - nt2=79372
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=193.4002
  - rt2=110.6982
  - sel=0.0000
  - st1=0.1618
  - st2=110.6967
  - startup_cost=150625.4100
  - total_cost=183990.7200
- **Output:** st=81.94, rt=571.03

### Step 16: Node 18609 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=128019
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=571.0339
  - rt2=0.0000
  - sel=0.4699
  - st1=81.9355
  - st2=0.0000
  - startup_cost=186231.0600
  - total_cost=187133.3100
- **Output:** st=938.85, rt=926.43

### Step 17: Node 18608 (Gather)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=180450
  - nt1=60150
  - nt2=0
  - parallel_workers=3
  - plan_width=168
  - reltuples=0.0000
  - rt1=926.4331
  - rt2=0.0000
  - sel=3.0000
  - st1=938.8523
  - st2=0.0000
  - startup_cost=187231.0600
  - total_cost=206178.3100
- **Output:** st=470.60, rt=962.15

### Step 18: Node 18607 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=180450
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=962.1519
  - rt2=0.0000
  - sel=0.3333
  - st1=470.6034
  - st2=0.0000
  - startup_cost=207982.8100
  - total_cost=208885.0600
- **Output:** st=919.96, rt=916.11

### Step 19: Node 18606 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=60150
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=916.1062
  - rt2=0.0000
  - sel=1.0000
  - st1=919.9579
  - st2=0.0000
  - startup_cost=213659.8500
  - total_cost=213810.2200
- **Output:** st=1119.01, rt=1119.76
