# Online Prediction Report

**Test Query:** Q8_35_seed_278937054
**Timestamp:** 2025-12-13 03:06:18

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 5.51%

## Phase C: Patterns in Query

- Total Patterns: 82

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 75736.1626 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 113504.2307 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 172 | 6131.8766 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 19.6008 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 108.1438 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 140 | 6.2375 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 96 | 7.3257 |
| 3e2d5a00 | Sort -> Hash Join (Outer) | 2 | 96 | 18.5586 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 168 | 75544.5822 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 148 | 172.9284 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 1 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 2 | 7df893ad | 6131.8766 | -0.0000% | REJECTED | 17.92% |
| 3 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 4 | 2e0f44ef | 108.1438 | 0.0001% | REJECTED | 17.92% |
| 7 | 3e2d5a00 | 18.5586 | 0.0007% | REJECTED | 17.92% |
| 8 | f4cb205a | 75544.5822 | 0.0006% | REJECTED | 17.92% |
| 9 | bb930825 | 172.9284 | -0.0000% | REJECTED | 17.92% |
| 10 | c0a8d3de | 6113.5159 | -0.0000% | REJECTED | 17.92% |
| 14 | 2422d111 | 10.7757 | 0.0001% | REJECTED | 17.92% |
| 17 | 37515ad8 | 168.3286 | -0.0000% | REJECTED | 17.92% |
| 18 | a54055ce | 6089.1983 | -0.0000% | REJECTED | 17.92% |
| 20 | 444761fb | 24.3176 | -0.0000% | REJECTED | 17.92% |
| 24 | 4db07220 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 25 | c5dad784 | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 28 | 545b5e57 | 153.1732 | -0.0000% | REJECTED | 17.92% |
| 29 | ec92bdaa | 15.1555 | -0.0000% | REJECTED | 17.92% |
| 31 | 440e6274 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 32 | 314469b0 | 20.7410 | 0.0000% | REJECTED | 17.92% |
| 34 | 58ed95a8 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 35 | 6981af52 | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 37 | f4603221 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 39 | e1d7e5b4 | 13.2381 | -0.0000% | REJECTED | 17.92% |
| 40 | 54cb7f90 | 20.7410 | 0.0000% | REJECTED | 17.92% |
| 43 | be705a2d | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 44 | b88a3db4 | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 46 | 3d4c3db9 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 48 | c302739b | 13.2381 | -0.0000% | REJECTED | 17.92% |
| 51 | 5d01b240 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 52 | 800ffecc | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 54 | 9ce781b0 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 58 | c7b8fb6d | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 59 | 9d50c2fc | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 61 | a95bee4e | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 64 | 1d069442 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 65 | cee0b988 | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 69 | d00b75d6 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 70 | 910f6702 | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 74 | 06857491 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 75 | fb7bcc0c | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 78 | 8febc667 | 2.4503 | 0.0007% | REJECTED | 17.92% |
## Query Tree

```
Node 14995 (Aggregate) - ROOT
  Node 14996 (Gather Merge)
    Node 14997 (Sort)
      Node 14998 (Hash Join)
        Node 14999 (Nested Loop)
          Node 15000 (Hash Join)
            Node 15001 (Nested Loop)
              Node 15002 (Hash Join)
                Node 15003 (Seq Scan) - LEAF
                Node 15004 (Hash)
                  Node 15005 (Hash Join)
                    Node 15006 (Seq Scan) - LEAF
                    Node 15007 (Hash)
                      Node 15008 (Hash Join)
                        Node 15009 (Seq Scan) - LEAF
                        Node 15010 (Hash)
                          Node 15011 (Seq Scan) - LEAF
              Node 15012 (Index Scan) - LEAF
            Node 15013 (Hash)
              Node 15014 (Seq Scan) - LEAF
          Node 15015 (Index Scan) - LEAF
        Node 15016 (Hash)
          Node 15017 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 4.76%
- Improvement: 0.75%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 14995 | Aggregate | 1249.83 | 1190.34 | 4.8% | operator |
| 14996 | Gather Merge | 1249.44 | 1123.90 | 10.0% | operator |
| 14997 | Sort | 1244.33 | 1087.88 | 12.6% | operator |
| 14998 | Hash Join | 1244.08 | 1055.48 | 15.2% | operator |
| 14999 | Nested Loop | 1243.77 | 1105.66 | 11.1% | operator |
| 15016 | Hash | 0.01 | 14.54 | 96831.4% | operator |
| 15000 | Hash Join | 1239.91 | 1027.31 | 17.1% | operator |
| 15015 | Index Scan | 0.01 | 0.05 | 753.5% | operator |
| 15017 | Seq Scan | 0.01 | 7.19 | 71844.7% | operator |
| 15001 | Nested Loop | 1193.43 | 1119.20 | 6.2% | operator |
| 15013 | Hash | 42.07 | 17.76 | 57.8% | operator |
| 15002 | Hash Join | 216.03 | 226.27 | 4.7% | operator |
| 15012 | Index Scan | 0.04 | 0.09 | 102.4% | operator |
| 15014 | Seq Scan | 41.97 | 44.48 | 6.0% | operator |
| 15003 | Seq Scan | 162.22 | 161.81 | 0.3% | operator |
| 15004 | Hash | 35.58 | 18.06 | 49.2% | operator |
| 15005 | Hash Join | 34.73 | 67.97 | 95.7% | operator |
| 15006 | Seq Scan | 33.07 | 24.87 | 24.8% | operator |
| 15007 | Hash | 0.32 | 17.93 | 5591.3% | operator |
| 15008 | Hash Join | 0.31 | 151.58 | 48484.4% | operator |
| 15009 | Seq Scan | 0.01 | 9.26 | 92506.3% | operator |
| 15010 | Hash | 0.30 | 16.01 | 5310.4% | operator |
| 15011 | Seq Scan | 0.29 | 21.39 | 7225.3% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 15011 (Seq Scan) - LEAF

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

### Step 2: Node 15009 (Seq Scan) - LEAF

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

### Step 3: Node 15010 (Hash)

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

### Step 4: Node 15008 (Hash Join)

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

### Step 5: Node 15006 (Seq Scan) - LEAF

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

### Step 6: Node 15007 (Hash)

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

### Step 7: Node 15005 (Hash Join)

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

### Step 8: Node 15003 (Seq Scan) - LEAF

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

### Step 9: Node 15004 (Hash)

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

### Step 10: Node 15002 (Hash Join)

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

### Step 11: Node 15012 (Index Scan) - LEAF

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

### Step 12: Node 15014 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=565
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0028
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=0.42, rt=44.48

### Step 13: Node 15001 (Nested Loop)

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

### Step 14: Node 15013 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=565
  - nt1=565
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=44.4804
  - rt2=0.0000
  - sel=1.0000
  - st1=0.4240
  - st2=0.0000
  - startup_cost=5169.6700
  - total_cost=5169.6700
- **Output:** st=17.76, rt=17.76

### Step 15: Node 15000 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=800
  - nt1=118013
  - nt2=565
  - parallel_workers=0
  - plan_width=20
  - reltuples=0.0000
  - rt1=1119.1991
  - rt2=17.7642
  - sel=0.0000
  - st1=37.2387
  - st2=17.7647
  - startup_cost=9920.2500
  - total_cost=70271.7300
- **Output:** st=77.17, rt=1027.31

### Step 16: Node 15015 (Index Scan) - LEAF

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

### Step 17: Node 15017 (Seq Scan) - LEAF

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

### Step 18: Node 14999 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=800
  - nt1=800
  - nt2=1
  - parallel_workers=0
  - plan_width=20
  - reltuples=0.0000
  - rt1=1027.3140
  - rt2=0.0512
  - sel=1.0000
  - st1=77.1715
  - st2=0.0060
  - startup_cost=9920.5400
  - total_cost=70513.7700
- **Output:** st=27.01, rt=1105.66

### Step 19: Node 15016 (Hash)

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

### Step 20: Node 14998 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=800
  - nt1=800
  - nt2=25
  - parallel_workers=0
  - plan_width=148
  - reltuples=0.0000
  - rt1=1105.6581
  - rt2=14.5397
  - sel=0.0400
  - st1=27.0060
  - st2=14.5393
  - startup_cost=9922.1000
  - total_cost=70519.7800
- **Output:** st=35.78, rt=1055.48

### Step 21: Node 14997 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=800
  - nt1=800
  - nt2=0
  - parallel_workers=0
  - plan_width=148
  - reltuples=0.0000
  - rt1=1055.4771
  - rt2=0.0000
  - sel=1.0000
  - st1=35.7826
  - st2=0.0000
  - startup_cost=70558.3600
  - total_cost=70560.3600
- **Output:** st=1086.92, rt=1087.88

### Step 22: Node 14996 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2479
  - nt1=800
  - nt2=0
  - parallel_workers=3
  - plan_width=148
  - reltuples=0.0000
  - rt1=1087.8814
  - rt2=0.0000
  - sel=3.0987
  - st1=1086.9234
  - st2=0.0000
  - startup_cost=71558.4000
  - total_cost=71851.6800
- **Output:** st=1120.82, rt=1123.90

### Step 23: Node 14995 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2406
  - nt1=2479
  - nt2=0
  - parallel_workers=0
  - plan_width=64
  - reltuples=0.0000
  - rt1=1123.8979
  - rt2=0.0000
  - sel=0.9706
  - st1=1120.8198
  - st2=0.0000
  - startup_cost=71558.4000
  - total_cost=71949.3800
- **Output:** st=1184.34, rt=1190.34
