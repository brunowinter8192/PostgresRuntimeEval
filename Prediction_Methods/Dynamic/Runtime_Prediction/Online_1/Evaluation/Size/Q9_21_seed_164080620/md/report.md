# Online Prediction Report

**Test Query:** Q9_21_seed_164080620
**Timestamp:** 2025-12-21 17:14:50

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17280 | Operator + Pattern Training |
| Training_Test | 4320 | Pattern Selection Eval |
| Training | 21600 | Final Model Training |
| Test | 2719 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 6.62%

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
Node 17793 (Sort) - ROOT
  Node 17794 (Aggregate)
    Node 17795 (Gather)
      Node 17796 (Aggregate)
        Node 17797 (Nested Loop)
          Node 17798 (Hash Join)
            Node 17799 (Seq Scan) - LEAF
            Node 17800 (Hash)
              Node 17801 (Hash Join)
                Node 17802 (Hash Join)
                  Node 17803 (Nested Loop)
                    Node 17804 (Seq Scan) - LEAF
                    Node 17805 (Index Scan) - LEAF
                  Node 17806 (Hash)
                    Node 17807 (Seq Scan) - LEAF
                Node 17808 (Hash)
                  Node 17809 (Seq Scan) - LEAF
          Node 17810 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 6.84%
- Improvement: -0.23%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 17793 | Sort | 1202.41 | 1120.12 | 6.8% | operator |
| 17794 | Aggregate | 1202.29 | 898.05 | 25.3% | operator |
| 17795 | Gather | 1201.15 | 964.48 | 19.7% | operator |
| 17796 | Aggregate | 1180.89 | 1075.81 | 8.9% | operator |
| 17797 | Nested Loop | 1157.56 | 1252.17 | 8.2% | operator |
| 17798 | Hash Join | 982.12 | 633.69 | 35.5% | operator |
| 17810 | Index Scan | 0.00 | -5.54 | 184812.7% | operator |
| 17799 | Seq Scan | 707.49 | 509.93 | 27.9% | operator |
| 17800 | Hash | 180.78 | 48.14 | 73.4% | operator |
| 17801 | Hash Join | 178.75 | 924.53 | 417.2% | operator |
| 17802 | Hash Join | 164.29 | 837.66 | 409.9% | operator |
| 17808 | Hash | 13.85 | 14.95 | 8.0% | operator |
| 17803 | Nested Loop | 157.96 | 1251.77 | 692.4% | operator |
| 17806 | Hash | 4.07 | 15.94 | 292.0% | operator |
| 17809 | Seq Scan | 13.83 | 2.94 | 78.8% | operator |
| 17804 | Seq Scan | 19.37 | 43.89 | 126.6% | operator |
| 17805 | Index Scan | 0.08 | -1.39 | 1903.2% | operator |
| 17807 | Seq Scan | 3.50 | 9.45 | 170.2% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 17804 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=5177
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0259
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=1.79, rt=43.89

### Step 2: Node 17805 (Index Scan) - LEAF

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
  - total_cost=1.8300
- **Output:** st=0.01, rt=-1.39

### Step 3: Node 17807 (Seq Scan) - LEAF

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

### Step 4: Node 17803 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=20708
  - nt1=5177
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=43.8949
  - rt2=-1.3885
  - sel=1.0000
  - st1=1.7873
  - st2=0.0113
  - startup_cost=0.4200
  - total_cost=14833.2400
- **Output:** st=153.58, rt=1251.77

### Step 5: Node 17806 (Hash)

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

### Step 6: Node 17809 (Seq Scan) - LEAF

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

### Step 7: Node 17802 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=20708
  - nt1=20708
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1251.7668
  - rt2=15.9407
  - sel=0.0001
  - st1=153.5766
  - st2=15.9407
  - startup_cost=448.4300
  - total_cost=15335.6200
- **Output:** st=121.45, rt=837.66

### Step 8: Node 17808 (Hash)

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

### Step 9: Node 17801 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=20708
  - nt1=20708
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=837.6605
  - rt2=14.9479
  - sel=0.0400
  - st1=121.4499
  - st2=14.9467
  - startup_cost=449.9900
  - total_cost=15400.7600
- **Output:** st=105.87, rt=924.53

### Step 10: Node 17799 (Seq Scan) - LEAF

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

### Step 11: Node 17800 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=20708
  - nt1=20708
  - nt2=0
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=924.5324
  - rt2=0.0000
  - sel=1.0000
  - st1=105.8668
  - st2=0.0000
  - startup_cost=15400.7600
  - total_cost=15400.7600
- **Output:** st=48.14, rt=48.14

### Step 12: Node 17798 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=74565
  - nt1=1200243
  - nt2=20708
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=509.9269
  - rt2=48.1433
  - sel=0.0000
  - st1=7.9002
  - st2=48.1419
  - startup_cost=15711.3800
  - total_cost=149315.7500
- **Output:** st=73.75, rt=633.69

### Step 13: Node 17810 (Index Scan) - LEAF

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

### Step 14: Node 17797 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=74565
  - nt1=74565
  - nt2=1
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=633.6875
  - rt2=-5.5414
  - sel=1.0000
  - st1=73.7544
  - st2=0.0041
  - startup_cost=15711.8000
  - total_cost=183097.0600
- **Output:** st=154.10, rt=1252.17

### Step 15: Node 17796 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=74565
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=1252.1681
  - rt2=0.0000
  - sel=0.8067
  - st1=154.1042
  - st2=0.0000
  - startup_cost=184401.9400
  - total_cost=185304.1900
- **Output:** st=1074.38, rt=1075.81

### Step 16: Node 17795 (Gather)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=300750
  - nt1=60150
  - nt2=0
  - parallel_workers=5
  - plan_width=168
  - reltuples=0.0000
  - rt1=1075.8136
  - rt2=0.0000
  - sel=5.0000
  - st1=1074.3798
  - st2=0.0000
  - startup_cost=185401.9400
  - total_cost=216379.1900
- **Output:** st=471.69, rt=964.48

### Step 17: Node 17794 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=300750
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=964.4809
  - rt2=0.0000
  - sel=0.2000
  - st1=471.6851
  - st2=0.0000
  - startup_cost=219386.6900
  - total_cost=220288.9400
- **Output:** st=893.07, rt=898.05

### Step 18: Node 17793 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=60150
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=898.0507
  - rt2=0.0000
  - sel=1.0000
  - st1=893.0685
  - st2=0.0000
  - startup_cost=225063.7300
  - total_cost=225214.1100
- **Output:** st=1119.39, rt=1120.12
