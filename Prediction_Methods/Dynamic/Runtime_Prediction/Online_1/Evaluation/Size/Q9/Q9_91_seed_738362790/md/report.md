# Online Prediction Report

**Test Query:** Q9_91_seed_738362790
**Timestamp:** 2025-12-21 17:24:34

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17280 | Operator + Pattern Training |
| Training_Test | 4320 | Pattern Selection Eval |
| Training | 21600 | Final Model Training |
| Test | 2719 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 6.97%

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
Node 19189 (Sort) - ROOT
  Node 19190 (Aggregate)
    Node 19191 (Gather)
      Node 19192 (Aggregate)
        Node 19193 (Nested Loop)
          Node 19194 (Hash Join)
            Node 19195 (Seq Scan) - LEAF
            Node 19196 (Hash)
              Node 19197 (Hash Join)
                Node 19198 (Hash Join)
                  Node 19199 (Nested Loop)
                    Node 19200 (Seq Scan) - LEAF
                    Node 19201 (Index Scan) - LEAF
                  Node 19202 (Hash)
                    Node 19203 (Seq Scan) - LEAF
                Node 19204 (Hash)
                  Node 19205 (Seq Scan) - LEAF
          Node 19206 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 7.27%
- Improvement: -0.30%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 19189 | Sort | 1202.90 | 1115.48 | 7.3% | operator |
| 19190 | Aggregate | 1202.77 | 908.94 | 24.4% | operator |
| 19191 | Gather | 1201.72 | 925.91 | 23.0% | operator |
| 19192 | Aggregate | 1181.56 | 1142.56 | 3.3% | operator |
| 19193 | Nested Loop | 1156.89 | 1252.17 | 8.2% | operator |
| 19194 | Hash Join | 983.45 | 630.95 | 35.8% | operator |
| 19206 | Index Scan | 0.00 | -5.54 | 184812.7% | operator |
| 19195 | Seq Scan | 707.06 | 509.93 | 27.9% | operator |
| 19196 | Hash | 181.36 | 46.46 | 74.4% | operator |
| 19197 | Hash Join | 175.39 | 923.53 | 426.6% | operator |
| 19198 | Hash Join | 159.65 | 837.16 | 424.4% | operator |
| 19204 | Hash | 15.10 | 14.95 | 1.0% | operator |
| 19199 | Nested Loop | 154.64 | 1251.76 | 709.5% | operator |
| 19202 | Hash | 2.96 | 15.94 | 437.6% | operator |
| 19205 | Seq Scan | 15.09 | 2.94 | 80.5% | operator |
| 19200 | Seq Scan | 20.42 | 44.86 | 119.7% | operator |
| 19201 | Index Scan | 0.07 | -1.39 | 1976.2% | operator |
| 19203 | Seq Scan | 2.49 | 9.45 | 279.2% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 19200 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=2839
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0142
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=1.88, rt=44.86

### Step 2: Node 19201 (Index Scan) - LEAF

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
  - total_cost=2.4500
- **Output:** st=0.01, rt=-1.39

### Step 3: Node 19203 (Seq Scan) - LEAF

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

### Step 4: Node 19199 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=11357
  - nt1=2839
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=44.8611
  - rt2=-1.3884
  - sel=1.0001
  - st1=1.8795
  - st2=0.0113
  - startup_cost=0.4200
  - total_cost=12243.6000
- **Output:** st=153.57, rt=1251.76

### Step 5: Node 19202 (Hash)

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

### Step 6: Node 19205 (Seq Scan) - LEAF

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

### Step 7: Node 19198 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=11357
  - nt1=11357
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1251.7595
  - rt2=15.9407
  - sel=0.0001
  - st1=153.5746
  - st2=15.9407
  - startup_cost=448.4300
  - total_cost=12721.4200
- **Output:** st=121.39, rt=837.16

### Step 8: Node 19204 (Hash)

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

### Step 9: Node 19197 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=11357
  - nt1=11357
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=837.1559
  - rt2=14.9479
  - sel=0.0400
  - st1=121.3859
  - st2=14.9467
  - startup_cost=449.9900
  - total_cost=12757.8500
- **Output:** st=105.75, rt=923.53

### Step 10: Node 19195 (Seq Scan) - LEAF

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

### Step 11: Node 19196 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=11357
  - nt1=11357
  - nt2=0
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=923.5325
  - rt2=0.0000
  - sel=1.0000
  - st1=105.7518
  - st2=0.0000
  - startup_cost=12757.8500
  - total_cost=12757.8500
- **Output:** st=46.46, rt=46.46

### Step 12: Node 19194 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=40892
  - nt1=1200243
  - nt2=11357
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=509.9269
  - rt2=46.4608
  - sel=0.0000
  - st1=7.9002
  - st2=46.4595
  - startup_cost=12928.2000
  - total_cost=146532.5300
- **Output:** st=75.14, rt=630.95

### Step 13: Node 19206 (Index Scan) - LEAF

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

### Step 14: Node 19193 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=40892
  - nt1=40892
  - nt2=1
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=630.9524
  - rt2=-5.5414
  - sel=1.0000
  - st1=75.1434
  - st2=0.0041
  - startup_cost=12928.6300
  - total_cost=165058.4500
- **Output:** st=154.10, rt=1252.17

### Step 15: Node 19192 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=40892
  - nt1=40892
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=1252.1681
  - rt2=0.0000
  - sel=1.0000
  - st1=154.1042
  - st2=0.0000
  - startup_cost=165774.0600
  - total_cost=166387.4400
- **Output:** st=1132.80, rt=1142.56

### Step 16: Node 19191 (Gather)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=204460
  - nt1=40892
  - nt2=0
  - parallel_workers=5
  - plan_width=168
  - reltuples=0.0000
  - rt1=1142.5648
  - rt2=0.0000
  - sel=5.0000
  - st1=1132.7991
  - st2=0.0000
  - startup_cost=166774.0600
  - total_cost=187833.4400
- **Output:** st=524.89, rt=925.91

### Step 17: Node 19190 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=204460
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=925.9146
  - rt2=0.0000
  - sel=0.2942
  - st1=524.8947
  - st2=0.0000
  - startup_cost=189878.0400
  - total_cost=190780.2900
- **Output:** st=920.26, rt=908.94

### Step 18: Node 19189 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=60150
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=908.9377
  - rt2=0.0000
  - sel=1.0000
  - st1=920.2643
  - st2=0.0000
  - startup_cost=195555.0800
  - total_cost=195705.4500
- **Output:** st=1114.72, rt=1115.48
