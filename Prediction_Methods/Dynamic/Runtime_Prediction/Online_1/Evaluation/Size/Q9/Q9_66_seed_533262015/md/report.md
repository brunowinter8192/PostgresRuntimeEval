# Online Prediction Report

**Test Query:** Q9_66_seed_533262015
**Timestamp:** 2025-12-21 17:21:13

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17280 | Operator + Pattern Training |
| Training_Test | 4320 | Pattern Selection Eval |
| Training | 21600 | Final Model Training |
| Test | 2719 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 6.05%

## Phase C: Patterns in Query

- Total Patterns: 56

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 420 | 12818.3% | 53836.8732 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 360 | 40658.7% | 146371.3776 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 210 | 14.4% | 30.2509 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 180 | 4284.6% | 7712.2590 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 150 | 5.7% | 8.5422 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 150 | 4.6% | 6.8991 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 150 | 9.7% | 14.5467 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 90 | 3.4% | 3.0966 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 90 | 11.3% | 10.1670 |
| 3b447875 | Aggregate -> Nested Loop (Outer) | 2 | 30 | 10.6% | 3.1651 |
| 7d4e78be | Hash Join -> [Hash Join (Outer), Hash (I... | 2 | 30 | 5.5% | 1.6532 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 150 | 79.2% | 118.8648 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 120 | 3.5% | 4.1629 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 90 | 8.1% | 7.2489 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 60 | 3.5% | 2.1270 |
| 30d6e09b | Hash Join -> [Hash Join -> [Nested Loop ... | 3 | 30 | 5.5% | 1.6532 |
| 2873b8c3 | Hash Join -> [Nested Loop -> [Seq Scan (... | 3 | 30 | 3.4% | 1.0295 |
| bd9dfa7b | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 90 | 3.8% | 3.3937 |
| 7a51ce50 | Hash Join -> [Hash Join -> [Nested Loop ... | 4 | 30 | 5.5% | 1.6532 |

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
| 5 | 3cfa90d7 | 6.8991 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 6 | 2e0f44ef | 14.5467 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 7 | 634cdbe2 | 3.0966 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 8 | c53c4396 | 10.1670 | -0.0000% | REJECTED | 17.17% |
| 9 | 3b447875 | 3.1651 | 0.0002% | REJECTED | 17.17% |
| 10 | 7d4e78be | 1.6532 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 11 | bb930825 | 118.8648 | -0.0000% | REJECTED | 17.17% |
| 12 | e0e3c3e1 | 4.1629 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 13 | a5f39f08 | 7.2489 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 14 | b3a45093 | 2.1270 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 15 | 30d6e09b | 1.6532 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 16 | 2873b8c3 | 1.0295 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 17 | bd9dfa7b | 3.3937 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 18 | 7a51ce50 | 1.6532 | N/A | SKIPPED_LOW_ERROR | 17.17% |
## Query Tree

```
Node 18679 (Sort) - ROOT
  Node 18680 (Aggregate)
    Node 18681 (Gather)
      Node 18682 (Aggregate)
        Node 18683 (Nested Loop)
          Node 18684 (Hash Join)
            Node 18685 (Seq Scan) - LEAF
            Node 18686 (Hash)
              Node 18687 (Hash Join)
                Node 18688 (Hash Join)
                  Node 18689 (Nested Loop)
                    Node 18690 (Seq Scan) - LEAF
                    Node 18691 (Index Scan) - LEAF
                  Node 18692 (Hash)
                    Node 18693 (Seq Scan) - LEAF
                Node 18694 (Hash)
                  Node 18695 (Seq Scan) - LEAF
          Node 18696 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 6.36%
- Improvement: -0.30%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 18679 | Sort | 1191.38 | 1115.66 | 6.4% | operator |
| 18680 | Aggregate | 1191.24 | 905.86 | 24.0% | operator |
| 18681 | Gather | 1190.28 | 930.93 | 21.8% | operator |
| 18682 | Aggregate | 1172.24 | 1142.35 | 2.5% | operator |
| 18683 | Nested Loop | 1148.47 | 1252.17 | 9.0% | operator |
| 18684 | Hash Join | 973.91 | 631.18 | 35.2% | operator |
| 18696 | Index Scan | 0.00 | -5.54 | 184812.7% | operator |
| 18685 | Seq Scan | 698.28 | 509.93 | 27.0% | operator |
| 18686 | Hash | 180.36 | 46.59 | 74.2% | operator |
| 18687 | Hash Join | 173.17 | 923.64 | 433.4% | operator |
| 18688 | Hash Join | 158.82 | 837.21 | 427.1% | operator |
| 18694 | Hash | 13.72 | 14.95 | 9.0% | operator |
| 18689 | Nested Loop | 150.08 | 1251.76 | 734.1% | operator |
| 18692 | Hash | 6.72 | 15.94 | 137.4% | operator |
| 18695 | Seq Scan | 13.70 | 2.94 | 78.6% | operator |
| 18690 | Seq Scan | 19.20 | 44.79 | 133.3% | operator |
| 18691 | Index Scan | 0.07 | -1.39 | 2028.4% | operator |
| 18693 | Seq Scan | 6.15 | 9.45 | 53.6% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 18690 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=3006
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0150
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=1.87, rt=44.79

### Step 2: Node 18691 (Index Scan) - LEAF

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
  - total_cost=2.4000
- **Output:** st=0.01, rt=-1.39

### Step 3: Node 18693 (Seq Scan) - LEAF

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

### Step 4: Node 18689 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=12023
  - nt1=3006
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=44.7904
  - rt2=-1.3884
  - sel=0.9999
  - st1=1.8729
  - st2=0.0113
  - startup_cost=0.4200
  - total_cost=12504.3200
- **Output:** st=153.57, rt=1251.76

### Step 5: Node 18692 (Hash)

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

### Step 6: Node 18695 (Seq Scan) - LEAF

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

### Step 7: Node 18688 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=12023
  - nt1=12023
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1251.7600
  - rt2=15.9407
  - sel=0.0001
  - st1=153.5747
  - st2=15.9407
  - startup_cost=448.4300
  - total_cost=12983.8900
- **Output:** st=121.39, rt=837.21

### Step 8: Node 18694 (Hash)

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

### Step 9: Node 18687 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=12023
  - nt1=12023
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=837.2090
  - rt2=14.9479
  - sel=0.0400
  - st1=121.3925
  - st2=14.9467
  - startup_cost=449.9900
  - total_cost=13022.3700
- **Output:** st=105.76, rt=923.64

### Step 10: Node 18685 (Seq Scan) - LEAF

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

### Step 11: Node 18686 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=12023
  - nt1=12023
  - nt2=0
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=923.6396
  - rt2=0.0000
  - sel=1.0000
  - st1=105.7643
  - st2=0.0000
  - startup_cost=13022.3700
  - total_cost=13022.3700
- **Output:** st=46.59, rt=46.59

### Step 12: Node 18684 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=43293
  - nt1=1200243
  - nt2=12023
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=509.9269
  - rt2=46.5921
  - sel=0.0000
  - st1=7.9002
  - st2=46.5908
  - startup_cost=13202.7100
  - total_cost=146807.0400
- **Output:** st=75.05, rt=631.18

### Step 13: Node 18696 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=1
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.4300
  - total_cost=0.4500
- **Output:** st=0.00, rt=-5.54

### Step 14: Node 18683 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=43293
  - nt1=43293
  - nt2=1
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=631.1799
  - rt2=-5.5414
  - sel=1.0000
  - st1=75.0542
  - st2=0.0041
  - startup_cost=13203.1400
  - total_cost=166420.7200
- **Output:** st=154.10, rt=1252.17

### Step 15: Node 18682 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=43293
  - nt1=43293
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=1252.1681
  - rt2=0.0000
  - sel=1.0000
  - st1=154.1042
  - st2=0.0000
  - startup_cost=167178.3400
  - total_cost=167827.7400
- **Output:** st=1132.15, rt=1142.35

### Step 16: Node 18681 (Gather)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=216465
  - nt1=43293
  - nt2=0
  - parallel_workers=5
  - plan_width=168
  - reltuples=0.0000
  - rt1=1142.3544
  - rt2=0.0000
  - sel=5.0000
  - st1=1132.1506
  - st2=0.0000
  - startup_cost=168178.3400
  - total_cost=190474.2400
- **Output:** st=518.12, rt=930.93

### Step 17: Node 18680 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=216465
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=930.9340
  - rt2=0.0000
  - sel=0.2779
  - st1=518.1211
  - st2=0.0000
  - startup_cost=192638.8900
  - total_cost=193541.1400
- **Output:** st=915.65, rt=905.86

### Step 18: Node 18679 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=60150
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=905.8601
  - rt2=0.0000
  - sel=1.0000
  - st1=915.6484
  - st2=0.0000
  - startup_cost=198315.9300
  - total_cost=198466.3000
- **Output:** st=1114.91, rt=1115.66
