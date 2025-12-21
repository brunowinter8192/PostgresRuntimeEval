# Online Prediction Report

**Test Query:** Q9_116_seed_943463565
**Timestamp:** 2025-12-21 17:09:47

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17280 | Operator + Pattern Training |
| Training_Test | 4320 | Pattern Selection Eval |
| Training | 21600 | Final Model Training |
| Test | 2719 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 6.06%

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
Node 16960 (Sort) - ROOT
  Node 16961 (Aggregate)
    Node 16962 (Gather)
      Node 16963 (Aggregate)
        Node 16964 (Nested Loop)
          Node 16965 (Hash Join)
            Node 16966 (Seq Scan) - LEAF
            Node 16967 (Hash)
              Node 16968 (Hash Join)
                Node 16969 (Hash Join)
                  Node 16970 (Nested Loop)
                    Node 16971 (Seq Scan) - LEAF
                    Node 16972 (Index Scan) - LEAF
                  Node 16973 (Hash)
                    Node 16974 (Seq Scan) - LEAF
                Node 16975 (Hash)
                  Node 16976 (Seq Scan) - LEAF
          Node 16977 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 6.33%
- Improvement: -0.27%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 16960 | Sort | 1193.40 | 1117.85 | 6.3% | operator |
| 16961 | Aggregate | 1193.27 | 896.88 | 24.8% | operator |
| 16962 | Gather | 1192.45 | 960.51 | 19.5% | operator |
| 16963 | Aggregate | 1170.92 | 1141.32 | 2.5% | operator |
| 16964 | Nested Loop | 1146.71 | 1252.17 | 9.2% | operator |
| 16965 | Hash Join | 974.93 | 632.42 | 35.1% | operator |
| 16977 | Index Scan | 0.00 | -5.54 | 184812.7% | operator |
| 16966 | Seq Scan | 696.71 | 509.93 | 26.8% | operator |
| 16967 | Hash | 184.24 | 47.34 | 74.3% | operator |
| 16968 | Hash Join | 182.15 | 924.15 | 407.4% | operator |
| 16969 | Hash Join | 168.57 | 837.46 | 396.8% | operator |
| 16975 | Hash | 12.97 | 14.95 | 15.2% | operator |
| 16970 | Nested Loop | 161.03 | 1251.76 | 677.3% | operator |
| 16973 | Hash | 5.22 | 15.94 | 205.6% | operator |
| 16976 | Seq Scan | 12.97 | 2.94 | 77.3% | operator |
| 16971 | Seq Scan | 19.08 | 44.37 | 132.5% | operator |
| 16972 | Index Scan | 0.08 | -1.39 | 1857.5% | operator |
| 16974 | Seq Scan | 4.56 | 9.45 | 107.0% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 16971 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=4008
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0200
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=1.83, rt=44.37

### Step 2: Node 16972 (Index Scan) - LEAF

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
  - total_cost=2.1100
- **Output:** st=0.01, rt=-1.39

### Step 3: Node 16974 (Seq Scan) - LEAF

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

### Step 4: Node 16970 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=16032
  - nt1=4008
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=44.3717
  - rt2=-1.3885
  - sel=1.0000
  - st1=1.8334
  - st2=0.0113
  - startup_cost=0.4200
  - total_cost=13788.6400
- **Output:** st=153.58, rt=1251.76

### Step 5: Node 16973 (Hash)

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

### Step 6: Node 16976 (Seq Scan) - LEAF

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

### Step 7: Node 16969 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=16032
  - nt1=16032
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1251.7629
  - rt2=15.9407
  - sel=0.0001
  - st1=153.5753
  - st2=15.9407
  - startup_cost=448.4300
  - total_cost=14278.7500
- **Output:** st=121.42, rt=837.46

### Step 8: Node 16975 (Hash)

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

### Step 9: Node 16968 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=16032
  - nt1=16032
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=837.4645
  - rt2=14.9479
  - sel=0.0400
  - st1=121.4248
  - st2=14.9467
  - startup_cost=449.9900
  - total_cost=14329.5300
- **Output:** st=105.82, rt=924.15

### Step 10: Node 16966 (Seq Scan) - LEAF

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

### Step 11: Node 16967 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=16032
  - nt1=16032
  - nt2=0
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=924.1500
  - rt2=0.0000
  - sel=1.0000
  - st1=105.8234
  - st2=0.0000
  - startup_cost=14329.5300
  - total_cost=14329.5300
- **Output:** st=47.34, rt=47.34

### Step 12: Node 16965 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=57726
  - nt1=1200243
  - nt2=16032
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=509.9269
  - rt2=47.3372
  - sel=0.0000
  - st1=7.9002
  - st2=47.3359
  - startup_cost=14570.0100
  - total_cost=148174.3600
- **Output:** st=74.48, rt=632.42

### Step 13: Node 16977 (Index Scan) - LEAF

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

### Step 14: Node 16964 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=57726
  - nt1=57726
  - nt2=1
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=632.4235
  - rt2=-5.5414
  - sel=1.0000
  - st1=74.4811
  - st2=0.0041
  - startup_cost=14570.4300
  - total_cost=174326.8400
- **Output:** st=154.10, rt=1252.17

### Step 15: Node 16963 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=57726
  - nt1=57726
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=1252.1681
  - rt2=0.0000
  - sel=1.0000
  - st1=154.1042
  - st2=0.0000
  - startup_cost=175337.0400
  - total_cost=176202.9300
- **Output:** st=1128.41, rt=1141.32

### Step 16: Node 16962 (Gather)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=288630
  - nt1=57726
  - nt2=0
  - parallel_workers=5
  - plan_width=168
  - reltuples=0.0000
  - rt1=1141.3208
  - rt2=0.0000
  - sel=5.0000
  - st1=1128.4097
  - st2=0.0000
  - startup_cost=176337.0400
  - total_cost=206065.9300
- **Output:** st=477.22, rt=960.51

### Step 17: Node 16961 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=288630
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=960.5114
  - rt2=0.0000
  - sel=0.2084
  - st1=477.2168
  - st2=0.0000
  - startup_cost=208952.2300
  - total_cost=209854.4800
- **Output:** st=897.27, rt=896.88

### Step 18: Node 16960 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=60150
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=896.8792
  - rt2=0.0000
  - sel=1.0000
  - st1=897.2718
  - st2=0.0000
  - startup_cost=214629.2700
  - total_cost=214779.6500
- **Output:** st=1117.11, rt=1117.85
