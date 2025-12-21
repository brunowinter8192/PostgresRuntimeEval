# Online Prediction Report

**Test Query:** Q9_2_seed_8204031
**Timestamp:** 2025-12-21 17:14:50

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17280 | Operator + Pattern Training |
| Training_Test | 4320 | Pattern Selection Eval |
| Training | 21600 | Final Model Training |
| Test | 2719 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 5.51%

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
Node 17955 (Sort) - ROOT
  Node 17956 (Aggregate)
    Node 17957 (Gather)
      Node 17958 (Aggregate)
        Node 17959 (Nested Loop)
          Node 17960 (Hash Join)
            Node 17961 (Seq Scan) - LEAF
            Node 17962 (Hash)
              Node 17963 (Hash Join)
                Node 17964 (Hash Join)
                  Node 17965 (Nested Loop)
                    Node 17966 (Seq Scan) - LEAF
                    Node 17967 (Index Scan) - LEAF
                  Node 17968 (Hash)
                    Node 17969 (Seq Scan) - LEAF
                Node 17970 (Hash)
                  Node 17971 (Seq Scan) - LEAF
          Node 17972 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 5.76%
- Improvement: -0.24%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 17955 | Sort | 1187.57 | 1119.21 | 5.8% | operator |
| 17956 | Aggregate | 1187.44 | 897.16 | 24.4% | operator |
| 17957 | Gather | 1186.37 | 964.74 | 18.7% | operator |
| 17958 | Aggregate | 1165.74 | 1106.30 | 5.1% | operator |
| 17959 | Nested Loop | 1141.11 | 1252.17 | 9.7% | operator |
| 17960 | Hash Join | 973.14 | 633.14 | 34.9% | operator |
| 17972 | Index Scan | 0.00 | -5.54 | 184812.7% | operator |
| 17961 | Seq Scan | 693.84 | 509.93 | 26.5% | operator |
| 17962 | Hash | 185.29 | 47.79 | 74.2% | operator |
| 17963 | Hash Join | 183.37 | 924.37 | 404.1% | operator |
| 17964 | Hash Join | 169.24 | 837.58 | 394.9% | operator |
| 17970 | Hash | 13.47 | 14.95 | 11.0% | operator |
| 17965 | Nested Loop | 162.92 | 1251.77 | 668.3% | operator |
| 17968 | Hash | 4.11 | 15.94 | 287.9% | operator |
| 17971 | Seq Scan | 13.46 | 2.94 | 78.2% | operator |
| 17966 | Seq Scan | 19.20 | 44.10 | 129.7% | operator |
| 17967 | Index Scan | 0.08 | -1.39 | 1835.6% | operator |
| 17969 | Seq Scan | 3.55 | 9.45 | 166.2% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 17966 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=4676
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0234
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=1.81, rt=44.10

### Step 2: Node 17967 (Index Scan) - LEAF

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
  - total_cost=1.9300
- **Output:** st=0.01, rt=-1.39

### Step 3: Node 17969 (Seq Scan) - LEAF

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

### Step 4: Node 17965 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18703
  - nt1=4676
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=44.0977
  - rt2=-1.3885
  - sel=0.9999
  - st1=1.8070
  - st2=0.0113
  - startup_cost=0.4200
  - total_cost=14392.0600
- **Output:** st=153.58, rt=1251.77

### Step 5: Node 17968 (Hash)

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

### Step 6: Node 17971 (Seq Scan) - LEAF

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

### Step 7: Node 17964 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18703
  - nt1=18703
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1251.7651
  - rt2=15.9407
  - sel=0.0001
  - st1=153.5760
  - st2=15.9407
  - startup_cost=448.4300
  - total_cost=14889.1800
- **Output:** st=121.44, rt=837.58

### Step 8: Node 17970 (Hash)

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

### Step 9: Node 17963 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18703
  - nt1=18703
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=837.5792
  - rt2=14.9479
  - sel=0.0400
  - st1=121.4395
  - st2=14.9467
  - startup_cost=449.9900
  - total_cost=14948.1600
- **Output:** st=105.85, rt=924.37

### Step 10: Node 17961 (Seq Scan) - LEAF

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

### Step 11: Node 17962 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18703
  - nt1=18703
  - nt2=0
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=924.3736
  - rt2=0.0000
  - sel=1.0000
  - st1=105.8486
  - st2=0.0000
  - startup_cost=14948.1600
  - total_cost=14948.1600
- **Output:** st=47.79, rt=47.79

### Step 12: Node 17960 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=67346
  - nt1=1200243
  - nt2=18703
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=509.9269
  - rt2=47.7923
  - sel=0.0000
  - st1=7.9002
  - st2=47.7909
  - startup_cost=15228.7100
  - total_cost=148833.0700
- **Output:** st=74.07, rt=633.14

### Step 13: Node 17972 (Index Scan) - LEAF

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

### Step 14: Node 17959 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=67346
  - nt1=67346
  - nt2=1
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=633.1414
  - rt2=-5.5414
  - sel=1.0000
  - st1=74.0660
  - st2=0.0041
  - startup_cost=15229.1300
  - total_cost=179343.8400
- **Output:** st=154.10, rt=1252.17

### Step 15: Node 17958 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=67346
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=1252.1681
  - rt2=0.0000
  - sel=0.8931
  - st1=154.1042
  - st2=0.0000
  - startup_cost=180522.4000
  - total_cost=181424.6500
- **Output:** st=1100.55, rt=1106.30

### Step 16: Node 17957 (Gather)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=300750
  - nt1=60150
  - nt2=0
  - parallel_workers=5
  - plan_width=168
  - reltuples=0.0000
  - rt1=1106.2967
  - rt2=0.0000
  - sel=5.0000
  - st1=1100.5465
  - st2=0.0000
  - startup_cost=181522.4000
  - total_cost=212499.6500
- **Output:** st=471.27, rt=964.74

### Step 17: Node 17956 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=300750
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=964.7438
  - rt2=0.0000
  - sel=0.2000
  - st1=471.2716
  - st2=0.0000
  - startup_cost=215507.1500
  - total_cost=216409.4000
- **Output:** st=894.10, rt=897.16

### Step 18: Node 17955 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=60150
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=897.1635
  - rt2=0.0000
  - sel=1.0000
  - st1=894.1039
  - st2=0.0000
  - startup_cost=221184.1900
  - total_cost=221334.5600
- **Output:** st=1118.48, rt=1119.21
