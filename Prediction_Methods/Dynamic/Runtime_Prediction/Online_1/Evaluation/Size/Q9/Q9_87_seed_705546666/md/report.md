# Online Prediction Report

**Test Query:** Q9_87_seed_705546666
**Timestamp:** 2025-12-21 17:22:54

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17280 | Operator + Pattern Training |
| Training_Test | 4320 | Pattern Selection Eval |
| Training | 21600 | Final Model Training |
| Test | 2719 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 4.77%

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
Node 19098 (Sort) - ROOT
  Node 19099 (Aggregate)
    Node 19100 (Gather)
      Node 19101 (Aggregate)
        Node 19102 (Nested Loop)
          Node 19103 (Hash Join)
            Node 19104 (Seq Scan) - LEAF
            Node 19105 (Hash)
              Node 19106 (Hash Join)
                Node 19107 (Hash Join)
                  Node 19108 (Nested Loop)
                    Node 19109 (Seq Scan) - LEAF
                    Node 19110 (Index Scan) - LEAF
                  Node 19111 (Hash)
                    Node 19112 (Seq Scan) - LEAF
                Node 19113 (Hash)
                  Node 19114 (Seq Scan) - LEAF
          Node 19115 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 5.06%
- Improvement: -0.28%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 19098 | Sort | 1176.48 | 1116.97 | 5.1% | operator |
| 19099 | Aggregate | 1176.35 | 898.50 | 23.6% | operator |
| 19100 | Gather | 1175.32 | 950.92 | 19.1% | operator |
| 19101 | Aggregate | 1150.88 | 1141.61 | 0.8% | operator |
| 19102 | Nested Loop | 1126.70 | 1252.17 | 11.1% | operator |
| 19103 | Hash Join | 950.66 | 632.07 | 33.5% | operator |
| 19115 | Index Scan | 0.00 | -5.54 | 184812.7% | operator |
| 19104 | Seq Scan | 680.76 | 509.93 | 25.1% | operator |
| 19105 | Hash | 176.35 | 47.12 | 73.3% | operator |
| 19106 | Hash Join | 174.60 | 924.03 | 429.2% | operator |
| 19107 | Hash Join | 160.38 | 837.40 | 422.1% | operator |
| 19113 | Hash | 13.58 | 14.95 | 10.0% | operator |
| 19108 | Nested Loop | 154.36 | 1251.76 | 710.9% | operator |
| 19111 | Hash | 4.06 | 15.94 | 292.9% | operator |
| 19114 | Seq Scan | 13.57 | 2.94 | 78.4% | operator |
| 19109 | Seq Scan | 21.48 | 44.51 | 107.2% | operator |
| 19110 | Index Scan | 0.07 | -1.39 | 1976.3% | operator |
| 19112 | Seq Scan | 3.55 | 9.45 | 166.3% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 19109 (Seq Scan) - LEAF

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

### Step 2: Node 19110 (Index Scan) - LEAF

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

### Step 3: Node 19112 (Seq Scan) - LEAF

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

### Step 4: Node 19108 (Nested Loop)

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

### Step 5: Node 19111 (Hash)

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

### Step 6: Node 19114 (Seq Scan) - LEAF

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

### Step 7: Node 19107 (Hash Join)

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

### Step 8: Node 19113 (Hash)

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

### Step 9: Node 19106 (Hash Join)

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

### Step 10: Node 19104 (Seq Scan) - LEAF

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

### Step 11: Node 19105 (Hash)

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

### Step 12: Node 19103 (Hash Join)

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

### Step 13: Node 19115 (Index Scan) - LEAF

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

### Step 14: Node 19102 (Nested Loop)

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

### Step 15: Node 19101 (Aggregate)

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

### Step 16: Node 19100 (Gather)

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

### Step 17: Node 19099 (Aggregate)

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

### Step 18: Node 19098 (Sort) - ROOT

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
