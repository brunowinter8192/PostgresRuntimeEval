# Online Prediction Report

**Test Query:** Q9_137_seed_1115748216
**Timestamp:** 2025-12-21 17:13:09

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17280 | Operator + Pattern Training |
| Training_Test | 4320 | Pattern Selection Eval |
| Training | 21600 | Final Model Training |
| Test | 2719 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 4.25%

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
Node 17375 (Sort) - ROOT
  Node 17376 (Aggregate)
    Node 17377 (Gather)
      Node 17378 (Aggregate)
        Node 17379 (Nested Loop)
          Node 17380 (Hash Join)
            Node 17381 (Seq Scan) - LEAF
            Node 17382 (Hash)
              Node 17383 (Hash Join)
                Node 17384 (Hash Join)
                  Node 17385 (Nested Loop)
                    Node 17386 (Seq Scan) - LEAF
                    Node 17387 (Index Scan) - LEAF
                  Node 17388 (Hash)
                    Node 17389 (Seq Scan) - LEAF
                Node 17390 (Hash)
                  Node 17391 (Seq Scan) - LEAF
          Node 17392 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 4.54%
- Improvement: -0.29%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 17375 | Sort | 1170.05 | 1116.97 | 4.5% | operator |
| 17376 | Aggregate | 1169.91 | 898.50 | 23.2% | operator |
| 17377 | Gather | 1168.93 | 950.92 | 18.7% | operator |
| 17378 | Aggregate | 1148.05 | 1141.61 | 0.6% | operator |
| 17379 | Nested Loop | 1123.86 | 1252.17 | 11.4% | operator |
| 17380 | Hash Join | 956.13 | 632.07 | 33.9% | operator |
| 17392 | Index Scan | 0.00 | -5.54 | 184812.7% | operator |
| 17381 | Seq Scan | 685.75 | 509.93 | 25.6% | operator |
| 17382 | Hash | 174.05 | 47.12 | 72.9% | operator |
| 17383 | Hash Join | 171.99 | 924.03 | 437.3% | operator |
| 17384 | Hash Join | 158.07 | 837.40 | 429.8% | operator |
| 17390 | Hash | 13.28 | 14.95 | 12.6% | operator |
| 17385 | Nested Loop | 152.59 | 1251.76 | 720.3% | operator |
| 17388 | Hash | 3.41 | 15.94 | 367.7% | operator |
| 17391 | Seq Scan | 13.27 | 2.94 | 77.9% | operator |
| 17386 | Seq Scan | 18.95 | 44.51 | 134.9% | operator |
| 17387 | Index Scan | 0.07 | -1.39 | 2002.0% | operator |
| 17389 | Seq Scan | 2.95 | 9.45 | 220.0% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 17386 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=3674
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0184
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=1.85, rt=44.51

### Step 2: Node 17387 (Index Scan) - LEAF

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
  - total_cost=2.2200
- **Output:** st=0.01, rt=-1.39

### Step 3: Node 17389 (Seq Scan) - LEAF

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

### Step 4: Node 17385 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14697
  - nt1=3674
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=44.5102
  - rt2=-1.3884
  - sel=1.0001
  - st1=1.8465
  - st2=0.0113
  - startup_cost=0.4200
  - total_cost=13480.1200
- **Output:** st=153.58, rt=1251.76

### Step 5: Node 17388 (Hash)

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

### Step 6: Node 17391 (Seq Scan) - LEAF

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

### Step 7: Node 17384 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14697
  - nt1=14697
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1251.7619
  - rt2=15.9407
  - sel=0.0001
  - st1=153.5750
  - st2=15.9407
  - startup_cost=448.4300
  - total_cost=13966.7100
- **Output:** st=121.42, rt=837.40

### Step 8: Node 17390 (Hash)

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

### Step 9: Node 17383 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14697
  - nt1=14697
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=837.4044
  - rt2=14.9479
  - sel=0.0400
  - st1=121.4172
  - st2=14.9467
  - startup_cost=449.9900
  - total_cost=14013.3900
- **Output:** st=105.81, rt=924.03

### Step 10: Node 17381 (Seq Scan) - LEAF

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

### Step 11: Node 17382 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14697
  - nt1=14697
  - nt2=0
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=924.0330
  - rt2=0.0000
  - sel=1.0000
  - st1=105.8104
  - st2=0.0000
  - startup_cost=14013.3900
  - total_cost=14013.3900
- **Output:** st=47.11, rt=47.12

### Step 12: Node 17380 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=52919
  - nt1=1200243
  - nt2=14697
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=509.9269
  - rt2=47.1151
  - sel=0.0000
  - st1=7.9002
  - st2=47.1138
  - startup_cost=14233.8500
  - total_cost=147838.1900
- **Output:** st=74.69, rt=632.07

### Step 13: Node 17392 (Index Scan) - LEAF

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

### Step 14: Node 17379 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=52919
  - nt1=52919
  - nt2=1
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=632.0688
  - rt2=-5.5414
  - sel=1.0000
  - st1=74.6885
  - st2=0.0041
  - startup_cost=14234.2700
  - total_cost=171812.8800
- **Output:** st=154.10, rt=1252.17

### Step 15: Node 17378 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=52919
  - nt1=52919
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=1252.1681
  - rt2=0.0000
  - sel=1.0000
  - st1=154.1042
  - st2=0.0000
  - startup_cost=172738.9600
  - total_cost=173532.7500
- **Output:** st=1129.59, rt=1141.61

### Step 16: Node 17377 (Gather)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=264595
  - nt1=52919
  - nt2=0
  - parallel_workers=5
  - plan_width=168
  - reltuples=0.0000
  - rt1=1141.6129
  - rt2=0.0000
  - sel=5.0000
  - st1=1129.5927
  - st2=0.0000
  - startup_cost=173738.9600
  - total_cost=200992.2500
- **Output:** st=490.67, rt=950.92

### Step 17: Node 17376 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=264595
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=950.9201
  - rt2=0.0000
  - sel=0.2273
  - st1=490.6741
  - st2=0.0000
  - startup_cost=203638.2000
  - total_cost=204540.4500
- **Output:** st=902.00, rt=898.50

### Step 18: Node 17375 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=60150
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=898.4998
  - rt2=0.0000
  - sel=1.0000
  - st1=902.0028
  - st2=0.0000
  - startup_cost=209315.2400
  - total_cost=209465.6100
- **Output:** st=1116.23, rt=1116.97
