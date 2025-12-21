# Online Prediction Report

**Test Query:** Q9_10_seed_73836279
**Timestamp:** 2025-12-21 17:08:05

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17280 | Operator + Pattern Training |
| Training_Test | 4320 | Pattern Selection Eval |
| Training | 21600 | Final Model Training |
| Test | 2719 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 6.18%

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
Node 16832 (Sort) - ROOT
  Node 16833 (Aggregate)
    Node 16834 (Gather)
      Node 16835 (Aggregate)
        Node 16836 (Nested Loop)
          Node 16837 (Hash Join)
            Node 16838 (Seq Scan) - LEAF
            Node 16839 (Hash)
              Node 16840 (Hash Join)
                Node 16841 (Hash Join)
                  Node 16842 (Nested Loop)
                    Node 16843 (Seq Scan) - LEAF
                    Node 16844 (Index Scan) - LEAF
                  Node 16845 (Hash)
                    Node 16846 (Seq Scan) - LEAF
                Node 16847 (Hash)
                  Node 16848 (Seq Scan) - LEAF
          Node 16849 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 6.48%
- Improvement: -0.30%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 16832 | Sort | 1192.77 | 1115.48 | 6.5% | operator |
| 16833 | Aggregate | 1192.64 | 908.94 | 23.8% | operator |
| 16834 | Gather | 1191.92 | 925.91 | 22.3% | operator |
| 16835 | Aggregate | 1170.64 | 1142.56 | 2.4% | operator |
| 16836 | Nested Loop | 1146.98 | 1252.17 | 9.2% | operator |
| 16837 | Hash Join | 976.94 | 630.95 | 35.4% | operator |
| 16849 | Index Scan | 0.00 | -5.54 | 184812.7% | operator |
| 16838 | Seq Scan | 692.68 | 509.93 | 26.4% | operator |
| 16839 | Hash | 191.04 | 46.46 | 75.7% | operator |
| 16840 | Hash Join | 184.03 | 923.53 | 401.8% | operator |
| 16841 | Hash Join | 169.87 | 837.16 | 392.8% | operator |
| 16847 | Hash | 13.54 | 14.95 | 10.4% | operator |
| 16842 | Nested Loop | 163.02 | 1251.76 | 667.9% | operator |
| 16845 | Hash | 4.52 | 15.94 | 252.4% | operator |
| 16848 | Seq Scan | 13.52 | 2.94 | 78.3% | operator |
| 16843 | Seq Scan | 21.22 | 44.86 | 111.4% | operator |
| 16844 | Index Scan | 0.08 | -1.39 | 1880.0% | operator |
| 16846 | Seq Scan | 3.96 | 9.45 | 138.6% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 16843 (Seq Scan) - LEAF

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

### Step 2: Node 16844 (Index Scan) - LEAF

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

### Step 3: Node 16846 (Seq Scan) - LEAF

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

### Step 4: Node 16842 (Nested Loop)

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

### Step 5: Node 16845 (Hash)

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

### Step 6: Node 16848 (Seq Scan) - LEAF

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

### Step 7: Node 16841 (Hash Join)

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

### Step 8: Node 16847 (Hash)

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

### Step 9: Node 16840 (Hash Join)

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

### Step 10: Node 16838 (Seq Scan) - LEAF

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

### Step 11: Node 16839 (Hash)

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

### Step 12: Node 16837 (Hash Join)

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

### Step 13: Node 16849 (Index Scan) - LEAF

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

### Step 14: Node 16836 (Nested Loop)

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

### Step 15: Node 16835 (Aggregate)

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

### Step 16: Node 16834 (Gather)

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

### Step 17: Node 16833 (Aggregate)

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

### Step 18: Node 16832 (Sort) - ROOT

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
