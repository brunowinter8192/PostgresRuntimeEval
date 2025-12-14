# Online Prediction Report

**Test Query:** Q8_127_seed_1033707906
**Timestamp:** 2025-12-13 04:14:54

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 3.86%

## Phase C: Patterns in Query

- Total Patterns: 82

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 75736.1626 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 113504.2307 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 172 | 6131.8766 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 19.6008 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 168 | 75544.5822 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 148 | 172.9284 |
| c0a8d3de | Hash -> Hash Join -> [Seq Scan (Outer), ... | 3 | 148 | 6113.5159 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 108.1438 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 140 | 6.2375 |
| 37515ad8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 124 | 168.3286 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 1 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 2 | 7df893ad | 6131.8766 | -0.0000% | REJECTED | 17.92% |
| 3 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 4 | f4cb205a | 75544.5822 | 0.0006% | REJECTED | 17.92% |
| 5 | bb930825 | 172.9284 | -0.0000% | REJECTED | 17.92% |
| 6 | c0a8d3de | 6113.5159 | -0.0000% | REJECTED | 17.92% |
| 7 | 2e0f44ef | 108.1438 | 0.0001% | REJECTED | 17.92% |
| 9 | 37515ad8 | 168.3286 | -0.0000% | REJECTED | 17.92% |
| 12 | 3e2d5a00 | 18.5586 | 0.0007% | REJECTED | 17.92% |
| 14 | a54055ce | 6089.1983 | -0.0000% | REJECTED | 17.92% |
| 17 | 2422d111 | 10.7757 | 0.0001% | REJECTED | 17.92% |
| 19 | 545b5e57 | 153.1732 | -0.0000% | REJECTED | 17.92% |
| 20 | 444761fb | 24.3176 | -0.0000% | REJECTED | 17.92% |
| 21 | ec92bdaa | 15.1555 | -0.0000% | REJECTED | 17.92% |
| 26 | 4db07220 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 28 | 440e6274 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 29 | 314469b0 | 20.7410 | 0.0000% | REJECTED | 17.92% |
| 30 | f4603221 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 32 | e1d7e5b4 | 13.2381 | -0.0000% | REJECTED | 17.92% |
| 33 | 54cb7f90 | 20.7410 | 0.0000% | REJECTED | 17.92% |
| 34 | 3d4c3db9 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 36 | c302739b | 13.2381 | -0.0000% | REJECTED | 17.92% |
| 37 | 9ce781b0 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 39 | a95bee4e | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 41 | c5dad784 | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 44 | 58ed95a8 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 45 | 6981af52 | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 49 | be705a2d | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 50 | b88a3db4 | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 54 | 5d01b240 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 55 | 800ffecc | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 59 | c7b8fb6d | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 60 | 9d50c2fc | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 64 | 1d069442 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 65 | cee0b988 | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 69 | d00b75d6 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 70 | 910f6702 | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 74 | 06857491 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 75 | fb7bcc0c | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 78 | 8febc667 | 2.4503 | 0.0007% | REJECTED | 17.92% |
## Query Tree

```
Node 13868 (Aggregate) - ROOT
  Node 13869 (Gather Merge)
    Node 13870 (Sort)
      Node 13871 (Hash Join)
        Node 13872 (Nested Loop)
          Node 13873 (Hash Join)
            Node 13874 (Nested Loop)
              Node 13875 (Hash Join)
                Node 13876 (Seq Scan) - LEAF
                Node 13877 (Hash)
                  Node 13878 (Hash Join)
                    Node 13879 (Seq Scan) - LEAF
                    Node 13880 (Hash)
                      Node 13881 (Hash Join)
                        Node 13882 (Seq Scan) - LEAF
                        Node 13883 (Hash)
                          Node 13884 (Seq Scan) - LEAF
              Node 13885 (Index Scan) - LEAF
            Node 13886 (Hash)
              Node 13887 (Seq Scan) - LEAF
          Node 13888 (Index Scan) - LEAF
        Node 13889 (Hash)
          Node 13890 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 3.14%
- Improvement: 0.71%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 13868 | Aggregate | 1219.25 | 1180.92 | 3.1% | operator |
| 13869 | Gather Merge | 1218.84 | 1123.87 | 7.8% | operator |
| 13870 | Sort | 1213.65 | 1087.88 | 10.4% | operator |
| 13871 | Hash Join | 1213.40 | 1055.49 | 13.0% | operator |
| 13872 | Nested Loop | 1213.08 | 1105.67 | 8.9% | operator |
| 13889 | Hash | 0.01 | 14.54 | 111744.0% | operator |
| 13873 | Hash Join | 1209.13 | 1027.32 | 15.0% | operator |
| 13888 | Index Scan | 0.01 | 0.05 | 753.5% | operator |
| 13890 | Seq Scan | 0.01 | 7.19 | 71844.7% | operator |
| 13874 | Nested Loop | 1161.85 | 1119.20 | 3.7% | operator |
| 13886 | Hash | 42.78 | 17.76 | 58.5% | operator |
| 13875 | Hash Join | 215.80 | 226.27 | 4.9% | operator |
| 13885 | Index Scan | 0.04 | 0.09 | 112.3% | operator |
| 13887 | Seq Scan | 42.72 | 44.47 | 4.1% | operator |
| 13876 | Seq Scan | 158.89 | 161.81 | 1.8% | operator |
| 13877 | Hash | 37.38 | 18.06 | 51.7% | operator |
| 13878 | Hash Join | 36.67 | 67.97 | 85.4% | operator |
| 13879 | Seq Scan | 35.11 | 24.87 | 29.1% | operator |
| 13880 | Hash | 0.24 | 17.93 | 7308.2% | operator |
| 13881 | Hash Join | 0.24 | 151.58 | 63590.5% | operator |
| 13882 | Seq Scan | 0.01 | 9.26 | 84087.6% | operator |
| 13883 | Hash | 0.22 | 16.01 | 7246.3% | operator |
| 13884 | Seq Scan | 0.21 | 21.39 | 9942.2% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 13884 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=1
  - nt=1
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=5.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.2000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=1.0600
- **Output:** st=0.12, rt=21.39

### Step 2: Node 13882 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=1
  - nt=25
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=25.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=1.2500
- **Output:** st=0.06, rt=9.26

### Step 3: Node 13883 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=1
  - nt1=1
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=21.3899
  - rt2=0.0000
  - sel=1.0000
  - st1=0.1185
  - st2=0.0000
  - startup_cost=1.0600
  - total_cost=1.0600
- **Output:** st=16.02, rt=16.01

### Step 4: Node 13881 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=25
  - nt2=1
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=9.2606
  - rt2=16.0149
  - sel=0.2000
  - st1=0.0596
  - st2=16.0154
  - startup_cost=1.0700
  - total_cost=2.4000
- **Output:** st=1.98, rt=151.58

### Step 5: Node 13879 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=3600
  - nt=62500
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=150000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.4167
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=4225.0000
- **Output:** st=0.28, rt=24.87

### Step 6: Node 13880 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=5
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=151.5834
  - rt2=0.0000
  - sel=1.0000
  - st1=1.9819
  - st2=0.0000
  - startup_cost=2.4000
  - total_cost=2.4000
- **Output:** st=17.93, rt=17.93

### Step 7: Node 13878 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=12500
  - nt1=62500
  - nt2=5
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=24.8735
  - rt2=17.9278
  - sel=0.0400
  - st1=0.2761
  - st2=17.9282
  - startup_cost=2.4600
  - total_cost=4586.8400
- **Output:** st=2.26, rt=67.97

### Step 8: Node 13876 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=147487
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=12
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0983
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=33394.0600
- **Output:** st=0.26, rt=161.81

### Step 9: Node 13877 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=12500
  - nt1=12500
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=67.9686
  - rt2=0.0000
  - sel=1.0000
  - st1=2.2615
  - st2=0.0000
  - startup_cost=4586.8400
  - total_cost=4586.8400
- **Output:** st=18.06, rt=18.06

### Step 10: Node 13875 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=29497
  - nt1=147487
  - nt2=12500
  - parallel_workers=0
  - plan_width=8
  - reltuples=0.0000
  - rt1=161.8115
  - rt2=18.0614
  - sel=0.0000
  - st1=0.2615
  - st2=18.0617
  - startup_cost=4743.0900
  - total_cost=38813.1400
- **Output:** st=27.70, rt=226.27

### Step 11: Node 13885 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=5
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.4300
  - total_cost=0.8300
- **Output:** st=0.04, rt=0.09

### Step 12: Node 13887 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=590
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0029
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=0.42, rt=44.47

### Step 13: Node 13874 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=118013
  - nt1=29497
  - nt2=5
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=226.2726
  - rt2=0.0870
  - sel=0.8002
  - st1=27.7005
  - st2=0.0386
  - startup_cost=4743.5200
  - total_cost=64785.2000
- **Output:** st=37.24, rt=1119.20

### Step 14: Node 13886 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=590
  - nt1=590
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=44.4702
  - rt2=0.0000
  - sel=1.0000
  - st1=0.4239
  - st2=0.0000
  - startup_cost=5169.6700
  - total_cost=5169.6700
- **Output:** st=17.76, rt=17.76

### Step 15: Node 13873 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=836
  - nt1=118013
  - nt2=590
  - parallel_workers=0
  - plan_width=20
  - reltuples=0.0000
  - rt1=1119.1991
  - rt2=17.7639
  - sel=0.0000
  - st1=37.2387
  - st2=17.7644
  - startup_cost=9920.5600
  - total_cost=70272.0400
- **Output:** st=77.17, rt=1027.32

### Step 16: Node 13888 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=223
  - nt=1
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=10000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0001
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.2900
  - total_cost=0.3000
- **Output:** st=0.01, rt=0.05

### Step 17: Node 13890 (Seq Scan) - LEAF

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
- **Output:** st=0.06, rt=7.19

### Step 18: Node 13872 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=836
  - nt1=836
  - nt2=1
  - parallel_workers=0
  - plan_width=20
  - reltuples=0.0000
  - rt1=1027.3194
  - rt2=0.0512
  - sel=1.0000
  - st1=77.1663
  - st2=0.0060
  - startup_cost=9920.8500
  - total_cost=70524.9700
- **Output:** st=27.00, rt=1105.67

### Step 19: Node 13889 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=25
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=7.1945
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0613
  - st2=0.0000
  - startup_cost=1.2500
  - total_cost=1.2500
- **Output:** st=14.54, rt=14.54

### Step 20: Node 13871 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=836
  - nt1=836
  - nt2=25
  - parallel_workers=0
  - plan_width=148
  - reltuples=0.0000
  - rt1=1105.6663
  - rt2=14.5397
  - sel=0.0400
  - st1=27.0049
  - st2=14.5393
  - startup_cost=9922.4100
  - total_cost=70531.1800
- **Output:** st=35.78, rt=1055.49

### Step 21: Node 13870 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=836
  - nt1=836
  - nt2=0
  - parallel_workers=0
  - plan_width=148
  - reltuples=0.0000
  - rt1=1055.4882
  - rt2=0.0000
  - sel=1.0000
  - st1=35.7848
  - st2=0.0000
  - startup_cost=70571.7600
  - total_cost=70573.8500
- **Output:** st=1086.93, rt=1087.88

### Step 22: Node 13869 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2592
  - nt1=836
  - nt2=0
  - parallel_workers=3
  - plan_width=148
  - reltuples=0.0000
  - rt1=1087.8841
  - rt2=0.0000
  - sel=3.1005
  - st1=1086.9261
  - st2=0.0000
  - startup_cost=71571.8000
  - total_cost=71878.4500
- **Output:** st=1120.79, rt=1123.87

### Step 23: Node 13868 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2406
  - nt1=2592
  - nt2=0
  - parallel_workers=0
  - plan_width=64
  - reltuples=0.0000
  - rt1=1123.8704
  - rt2=0.0000
  - sel=0.9282
  - st1=1120.7918
  - st2=0.0000
  - startup_cost=71571.8000
  - total_cost=71978.4100
- **Output:** st=1178.38, rt=1180.92
