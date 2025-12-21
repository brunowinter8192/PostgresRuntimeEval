# Online Prediction Report

**Test Query:** Q9_16_seed_123060465
**Timestamp:** 2025-12-21 17:14:50

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17280 | Operator + Pattern Training |
| Training_Test | 4320 | Pattern Selection Eval |
| Training | 21600 | Final Model Training |
| Test | 2719 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 5.37%

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
Node 17683 (Sort) - ROOT
  Node 17684 (Aggregate)
    Node 17685 (Gather)
      Node 17686 (Aggregate)
        Node 17687 (Nested Loop)
          Node 17688 (Hash Join)
            Node 17689 (Seq Scan) - LEAF
            Node 17690 (Hash)
              Node 17691 (Hash Join)
                Node 17692 (Hash Join)
                  Node 17693 (Nested Loop)
                    Node 17694 (Seq Scan) - LEAF
                    Node 17695 (Index Scan) - LEAF
                  Node 17696 (Hash)
                    Node 17697 (Seq Scan) - LEAF
                Node 17698 (Hash)
                  Node 17699 (Seq Scan) - LEAF
          Node 17700 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 5.66%
- Improvement: -0.29%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 17683 | Sort | 1183.56 | 1116.58 | 5.7% | operator |
| 17684 | Aggregate | 1183.44 | 899.75 | 24.0% | operator |
| 17685 | Gather | 1182.52 | 945.99 | 20.0% | operator |
| 17686 | Aggregate | 1164.51 | 1141.78 | 2.0% | operator |
| 17687 | Nested Loop | 1140.78 | 1252.17 | 9.8% | operator |
| 17688 | Hash Join | 973.17 | 631.85 | 35.1% | operator |
| 17700 | Index Scan | 0.00 | -5.54 | 184812.7% | operator |
| 17689 | Seq Scan | 697.21 | 509.93 | 26.9% | operator |
| 17690 | Hash | 179.06 | 46.99 | 73.8% | operator |
| 17691 | Hash Join | 176.26 | 923.94 | 424.2% | operator |
| 17692 | Hash Join | 162.71 | 837.36 | 414.6% | operator |
| 17698 | Hash | 12.94 | 14.95 | 15.6% | operator |
| 17693 | Nested Loop | 155.32 | 1251.76 | 705.9% | operator |
| 17696 | Hash | 4.95 | 15.94 | 222.1% | operator |
| 17699 | Seq Scan | 12.92 | 2.94 | 77.3% | operator |
| 17694 | Seq Scan | 21.64 | 44.58 | 106.0% | operator |
| 17695 | Index Scan | 0.07 | -1.39 | 1951.2% | operator |
| 17697 | Seq Scan | 4.38 | 9.45 | 115.9% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 17694 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=3507
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0175
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=1.85, rt=44.58

### Step 2: Node 17695 (Index Scan) - LEAF

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
  - total_cost=2.2600
- **Output:** st=0.01, rt=-1.39

### Step 3: Node 17697 (Seq Scan) - LEAF

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

### Step 4: Node 17693 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14028
  - nt1=3507
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=44.5799
  - rt2=-1.3884
  - sel=1.0000
  - st1=1.8531
  - st2=0.0113
  - startup_cost=0.4200
  - total_cost=13249.9400
- **Output:** st=153.57, rt=1251.76

### Step 5: Node 17696 (Hash)

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

### Step 6: Node 17699 (Seq Scan) - LEAF

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

### Step 7: Node 17692 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14028
  - nt1=14028
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1251.7614
  - rt2=15.9407
  - sel=0.0001
  - st1=153.5749
  - st2=15.9407
  - startup_cost=448.4300
  - total_cost=13734.7800
- **Output:** st=121.41, rt=837.36

### Step 8: Node 17698 (Hash)

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

### Step 9: Node 17691 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14028
  - nt1=14028
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=837.3588
  - rt2=14.9479
  - sel=0.0400
  - st1=121.4114
  - st2=14.9467
  - startup_cost=449.9900
  - total_cost=13779.4100
- **Output:** st=105.80, rt=923.94

### Step 10: Node 17689 (Seq Scan) - LEAF

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

### Step 11: Node 17690 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14028
  - nt1=14028
  - nt2=0
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=923.9414
  - rt2=0.0000
  - sel=1.0000
  - st1=105.7997
  - st2=0.0000
  - startup_cost=13779.4100
  - total_cost=13779.4100
- **Output:** st=46.98, rt=46.99

### Step 12: Node 17688 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=50512
  - nt1=1200243
  - nt2=14028
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=509.9269
  - rt2=46.9858
  - sel=0.0000
  - st1=7.9002
  - st2=46.9845
  - startup_cost=13989.8300
  - total_cost=147594.1600
- **Output:** st=74.78, rt=631.85

### Step 13: Node 17700 (Index Scan) - LEAF

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

### Step 14: Node 17687 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=50512
  - nt1=50512
  - nt2=1
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=631.8519
  - rt2=-5.5414
  - sel=1.0000
  - st1=74.7816
  - st2=0.0041
  - startup_cost=13990.2500
  - total_cost=170478.3700
- **Output:** st=154.10, rt=1252.17

### Step 15: Node 17686 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=50512
  - nt1=50512
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=1252.1681
  - rt2=0.0000
  - sel=1.0000
  - st1=154.1042
  - st2=0.0000
  - startup_cost=171362.3300
  - total_cost=172120.0100
- **Output:** st=1130.22, rt=1141.78

### Step 16: Node 17685 (Gather)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=252560
  - nt1=50512
  - nt2=0
  - parallel_workers=5
  - plan_width=168
  - reltuples=0.0000
  - rt1=1141.7826
  - rt2=0.0000
  - sel=5.0000
  - st1=1130.2242
  - st2=0.0000
  - startup_cost=172362.3300
  - total_cost=198376.0100
- **Output:** st=497.52, rt=945.99

### Step 17: Node 17684 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=252560
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=945.9899
  - rt2=0.0000
  - sel=0.2382
  - st1=497.5155
  - st2=0.0000
  - startup_cost=200901.6100
  - total_cost=201803.8600
- **Output:** st=904.83, rt=899.75

### Step 18: Node 17683 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=60150
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=899.7456
  - rt2=0.0000
  - sel=1.0000
  - st1=904.8300
  - st2=0.0000
  - startup_cost=206578.6500
  - total_cost=206729.0300
- **Output:** st=1115.83, rt=1116.58
