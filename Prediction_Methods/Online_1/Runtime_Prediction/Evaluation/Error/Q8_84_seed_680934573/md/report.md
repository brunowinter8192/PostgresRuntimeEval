# Online Prediction Report

**Test Query:** Q8_84_seed_680934573
**Timestamp:** 2025-12-13 02:03:02

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 1.88%

## Phase C: Patterns in Query

- Total Patterns: 82

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 113504.2307 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 75736.1626 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 168 | 75544.5822 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 172 | 6131.8766 |
| c0a8d3de | Hash -> Hash Join -> [Seq Scan (Outer), ... | 3 | 148 | 6113.5159 |
| a54055ce | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 96 | 6089.1983 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 148 | 172.9284 |
| 37515ad8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 124 | 168.3286 |
| 545b5e57 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 72 | 153.1732 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 108.1438 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 1 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 2 | f4cb205a | 75544.5822 | 0.0006% | REJECTED | 17.92% |
| 3 | 7df893ad | 6131.8766 | -0.0000% | REJECTED | 17.92% |
| 4 | c0a8d3de | 6113.5159 | -0.0000% | REJECTED | 17.92% |
| 5 | a54055ce | 6089.1983 | -0.0000% | REJECTED | 17.92% |
| 6 | bb930825 | 172.9284 | -0.0000% | REJECTED | 17.92% |
| 7 | 37515ad8 | 168.3286 | -0.0000% | REJECTED | 17.92% |
| 8 | 545b5e57 | 153.1732 | -0.0000% | REJECTED | 17.92% |
| 9 | 2e0f44ef | 108.1438 | 0.0001% | REJECTED | 17.92% |
| 10 | 444761fb | 24.3176 | -0.0000% | REJECTED | 17.92% |
| 11 | 314469b0 | 20.7410 | 0.0000% | REJECTED | 17.92% |
| 12 | 54cb7f90 | 20.7410 | 0.0000% | REJECTED | 17.92% |
| 13 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 14 | 3e2d5a00 | 18.5586 | 0.0007% | REJECTED | 17.92% |
| 15 | ec92bdaa | 15.1555 | -0.0000% | REJECTED | 17.92% |
| 16 | e1d7e5b4 | 13.2381 | -0.0000% | REJECTED | 17.92% |
| 17 | c302739b | 13.2381 | -0.0000% | REJECTED | 17.92% |
| 18 | 2422d111 | 10.7757 | 0.0001% | REJECTED | 17.92% |
| 21 | 4db07220 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 22 | 440e6274 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 23 | f4603221 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 24 | 3d4c3db9 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 25 | 9ce781b0 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 26 | a95bee4e | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 27 | c5dad784 | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 28 | 6981af52 | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 29 | b88a3db4 | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 30 | 800ffecc | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 31 | 9d50c2fc | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 32 | cee0b988 | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 33 | 910f6702 | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 34 | fb7bcc0c | 4.8707 | 0.0001% | REJECTED | 17.92% |
| 43 | 58ed95a8 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 44 | be705a2d | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 45 | 5d01b240 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 46 | c7b8fb6d | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 47 | 1d069442 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 48 | d00b75d6 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 49 | 06857491 | 2.4503 | 0.0007% | REJECTED | 17.92% |
| 50 | 8febc667 | 2.4503 | 0.0007% | REJECTED | 17.92% |
## Query Tree

```
Node 16237 (Aggregate) - ROOT
  Node 16238 (Gather Merge)
    Node 16239 (Sort)
      Node 16240 (Hash Join)
        Node 16241 (Nested Loop)
          Node 16242 (Hash Join)
            Node 16243 (Nested Loop)
              Node 16244 (Hash Join)
                Node 16245 (Seq Scan) - LEAF
                Node 16246 (Hash)
                  Node 16247 (Hash Join)
                    Node 16248 (Seq Scan) - LEAF
                    Node 16249 (Hash)
                      Node 16250 (Hash Join)
                        Node 16251 (Seq Scan) - LEAF
                        Node 16252 (Hash)
                          Node 16253 (Seq Scan) - LEAF
              Node 16254 (Index Scan) - LEAF
            Node 16255 (Hash)
              Node 16256 (Seq Scan) - LEAF
          Node 16257 (Index Scan) - LEAF
        Node 16258 (Hash)
          Node 16259 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 1.14%
- Improvement: 0.74%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 16237 | Aggregate | 1197.68 | 1184.07 | 1.1% | operator |
| 16238 | Gather Merge | 1197.20 | 1123.89 | 6.1% | operator |
| 16239 | Sort | 1191.23 | 1087.88 | 8.7% | operator |
| 16240 | Hash Join | 1190.96 | 1055.48 | 11.4% | operator |
| 16241 | Nested Loop | 1190.62 | 1105.66 | 7.1% | operator |
| 16258 | Hash | 0.02 | 14.54 | 63116.2% | operator |
| 16242 | Hash Join | 1187.04 | 1027.32 | 13.5% | operator |
| 16257 | Index Scan | 0.01 | 0.05 | 924.2% | operator |
| 16259 | Seq Scan | 0.01 | 7.19 | 51289.1% | operator |
| 16243 | Nested Loop | 1146.95 | 1119.20 | 2.4% | operator |
| 16255 | Hash | 35.47 | 17.76 | 49.9% | operator |
| 16244 | Hash Join | 207.51 | 226.27 | 9.0% | operator |
| 16254 | Index Scan | 0.04 | 0.09 | 112.3% | operator |
| 16256 | Seq Scan | 35.39 | 44.47 | 25.7% | operator |
| 16245 | Seq Scan | 157.99 | 161.81 | 2.4% | operator |
| 16246 | Hash | 32.07 | 18.06 | 43.7% | operator |
| 16247 | Hash Join | 31.48 | 67.97 | 115.9% | operator |
| 16248 | Seq Scan | 29.99 | 24.87 | 17.1% | operator |
| 16249 | Hash | 0.19 | 17.93 | 9538.6% | operator |
| 16250 | Hash Join | 0.18 | 151.58 | 83187.6% | operator |
| 16251 | Seq Scan | 0.02 | 9.26 | 51348.0% | operator |
| 16252 | Hash | 0.15 | 16.01 | 10232.2% | operator |
| 16253 | Seq Scan | 0.15 | 21.39 | 14160.0% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 16253 (Seq Scan) - LEAF

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

### Step 2: Node 16251 (Seq Scan) - LEAF

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

### Step 3: Node 16252 (Hash)

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

### Step 4: Node 16250 (Hash Join)

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

### Step 5: Node 16248 (Seq Scan) - LEAF

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

### Step 6: Node 16249 (Hash)

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

### Step 7: Node 16247 (Hash Join)

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

### Step 8: Node 16245 (Seq Scan) - LEAF

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

### Step 9: Node 16246 (Hash)

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

### Step 10: Node 16244 (Hash Join)

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

### Step 11: Node 16254 (Index Scan) - LEAF

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

### Step 12: Node 16256 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=582
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

### Step 13: Node 16243 (Nested Loop)

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

### Step 14: Node 16255 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=582
  - nt1=582
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=44.4735
  - rt2=0.0000
  - sel=1.0000
  - st1=0.4239
  - st2=0.0000
  - startup_cost=5169.6700
  - total_cost=5169.6700
- **Output:** st=17.76, rt=17.76

### Step 15: Node 16242 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=824
  - nt1=118013
  - nt2=582
  - parallel_workers=0
  - plan_width=20
  - reltuples=0.0000
  - rt1=1119.1991
  - rt2=17.7640
  - sel=0.0000
  - st1=37.2387
  - st2=17.7645
  - startup_cost=9920.4600
  - total_cost=70271.9400
- **Output:** st=77.17, rt=1027.32

### Step 16: Node 16257 (Index Scan) - LEAF

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

### Step 17: Node 16259 (Seq Scan) - LEAF

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

### Step 18: Node 16241 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=824
  - nt1=824
  - nt2=1
  - parallel_workers=0
  - plan_width=20
  - reltuples=0.0000
  - rt1=1027.3177
  - rt2=0.0512
  - sel=1.0000
  - st1=77.1680
  - st2=0.0060
  - startup_cost=9920.7500
  - total_cost=70521.2400
- **Output:** st=27.01, rt=1105.66

### Step 19: Node 16258 (Hash)

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

### Step 20: Node 16240 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=824
  - nt1=824
  - nt2=25
  - parallel_workers=0
  - plan_width=148
  - reltuples=0.0000
  - rt1=1105.6635
  - rt2=14.5397
  - sel=0.0400
  - st1=27.0053
  - st2=14.5393
  - startup_cost=9922.3100
  - total_cost=70527.3900
- **Output:** st=35.78, rt=1055.48

### Step 21: Node 16239 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=824
  - nt1=824
  - nt2=0
  - parallel_workers=0
  - plan_width=148
  - reltuples=0.0000
  - rt1=1055.4845
  - rt2=0.0000
  - sel=1.0000
  - st1=35.7841
  - st2=0.0000
  - startup_cost=70567.3000
  - total_cost=70569.3600
- **Output:** st=1086.93, rt=1087.88

### Step 22: Node 16238 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2554
  - nt1=824
  - nt2=0
  - parallel_workers=3
  - plan_width=148
  - reltuples=0.0000
  - rt1=1087.8832
  - rt2=0.0000
  - sel=3.0995
  - st1=1086.9252
  - st2=0.0000
  - startup_cost=71567.3400
  - total_cost=71869.4900
- **Output:** st=1120.81, rt=1123.89

### Step 23: Node 16237 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2406
  - nt1=2554
  - nt2=0
  - parallel_workers=0
  - plan_width=64
  - reltuples=0.0000
  - rt1=1123.8857
  - rt2=0.0000
  - sel=0.9421
  - st1=1120.8074
  - st2=0.0000
  - startup_cost=71567.3400
  - total_cost=71968.6900
- **Output:** st=1180.43, rt=1184.07
