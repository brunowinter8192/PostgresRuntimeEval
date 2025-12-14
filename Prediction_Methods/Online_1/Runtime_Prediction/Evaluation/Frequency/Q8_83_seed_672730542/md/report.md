# Online Prediction Report

**Test Query:** Q8_83_seed_672730542
**Timestamp:** 2025-12-13 04:20:40

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 4.11%

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
Node 16214 (Aggregate) - ROOT
  Node 16215 (Gather Merge)
    Node 16216 (Sort)
      Node 16217 (Hash Join)
        Node 16218 (Nested Loop)
          Node 16219 (Hash Join)
            Node 16220 (Nested Loop)
              Node 16221 (Hash Join)
                Node 16222 (Seq Scan) - LEAF
                Node 16223 (Hash)
                  Node 16224 (Hash Join)
                    Node 16225 (Seq Scan) - LEAF
                    Node 16226 (Hash)
                      Node 16227 (Hash Join)
                        Node 16228 (Seq Scan) - LEAF
                        Node 16229 (Hash)
                          Node 16230 (Seq Scan) - LEAF
              Node 16231 (Index Scan) - LEAF
            Node 16232 (Hash)
              Node 16233 (Seq Scan) - LEAF
          Node 16234 (Index Scan) - LEAF
        Node 16235 (Hash)
          Node 16236 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 3.31%
- Improvement: 0.80%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 16214 | Aggregate | 1237.48 | 1196.51 | 3.3% | operator |
| 16215 | Gather Merge | 1237.12 | 1123.90 | 9.2% | operator |
| 16216 | Sort | 1229.83 | 1087.88 | 11.5% | operator |
| 16217 | Hash Join | 1229.58 | 1055.46 | 14.2% | operator |
| 16218 | Nested Loop | 1229.24 | 1105.64 | 10.1% | operator |
| 16235 | Hash | 0.02 | 14.54 | 69136.7% | operator |
| 16219 | Hash Join | 1225.29 | 1027.30 | 16.2% | operator |
| 16234 | Index Scan | 0.01 | 0.05 | 753.5% | operator |
| 16236 | Seq Scan | 0.02 | 7.19 | 44865.5% | operator |
| 16220 | Nested Loop | 1182.66 | 1119.20 | 5.4% | operator |
| 16232 | Hash | 38.06 | 17.76 | 53.3% | operator |
| 16221 | Hash Join | 218.70 | 226.27 | 3.5% | operator |
| 16231 | Index Scan | 0.04 | 0.09 | 112.3% | operator |
| 16233 | Seq Scan | 37.90 | 44.50 | 17.4% | operator |
| 16222 | Seq Scan | 161.51 | 161.81 | 0.2% | operator |
| 16223 | Hash | 39.01 | 18.06 | 53.7% | operator |
| 16224 | Hash Join | 38.35 | 67.97 | 77.2% | operator |
| 16225 | Seq Scan | 36.72 | 24.87 | 32.3% | operator |
| 16226 | Hash | 0.23 | 17.93 | 7797.7% | operator |
| 16227 | Hash Join | 0.22 | 151.58 | 67571.2% | operator |
| 16228 | Seq Scan | 0.01 | 9.26 | 92506.3% | operator |
| 16229 | Hash | 0.20 | 16.01 | 7712.2% | operator |
| 16230 | Seq Scan | 0.20 | 21.39 | 10489.1% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 16230 (Seq Scan) - LEAF

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

### Step 2: Node 16228 (Seq Scan) - LEAF

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

### Step 3: Node 16229 (Hash)

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

### Step 4: Node 16227 (Hash Join)

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

### Step 5: Node 16225 (Seq Scan) - LEAF

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

### Step 6: Node 16226 (Hash)

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

### Step 7: Node 16224 (Hash Join)

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

### Step 8: Node 16222 (Seq Scan) - LEAF

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

### Step 9: Node 16223 (Hash)

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

### Step 10: Node 16221 (Hash Join)

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

### Step 11: Node 16231 (Index Scan) - LEAF

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

### Step 12: Node 16233 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=517
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0026
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=0.42, rt=44.50

### Step 13: Node 16220 (Nested Loop)

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

### Step 14: Node 16232 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=517
  - nt1=517
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=44.5001
  - rt2=0.0000
  - sel=1.0000
  - st1=0.4241
  - st2=0.0000
  - startup_cost=5169.6700
  - total_cost=5169.6700
- **Output:** st=17.77, rt=17.76

### Step 15: Node 16219 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=732
  - nt1=118013
  - nt2=517
  - parallel_workers=0
  - plan_width=20
  - reltuples=0.0000
  - rt1=1119.1991
  - rt2=17.7648
  - sel=0.0000
  - st1=37.2387
  - st2=17.7652
  - startup_cost=9919.6500
  - total_cost=70271.1300
- **Output:** st=77.18, rt=1027.30

### Step 16: Node 16234 (Index Scan) - LEAF

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

### Step 17: Node 16236 (Seq Scan) - LEAF

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

### Step 18: Node 16218 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=732
  - nt1=732
  - nt2=1
  - parallel_workers=0
  - plan_width=20
  - reltuples=0.0000
  - rt1=1027.3037
  - rt2=0.0512
  - sel=1.0000
  - st1=77.1814
  - st2=0.0060
  - startup_cost=9919.9400
  - total_cost=70492.5900
- **Output:** st=27.01, rt=1105.64

### Step 19: Node 16235 (Hash)

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

### Step 20: Node 16217 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=732
  - nt1=732
  - nt2=25
  - parallel_workers=0
  - plan_width=148
  - reltuples=0.0000
  - rt1=1105.6429
  - rt2=14.5397
  - sel=0.0400
  - st1=27.0081
  - st2=14.5393
  - startup_cost=9921.5000
  - total_cost=70498.2300
- **Output:** st=35.78, rt=1055.46

### Step 21: Node 16216 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=732
  - nt1=732
  - nt2=0
  - parallel_workers=0
  - plan_width=148
  - reltuples=0.0000
  - rt1=1055.4563
  - rt2=0.0000
  - sel=1.0000
  - st1=35.7784
  - st2=0.0000
  - startup_cost=70533.0600
  - total_cost=70534.8900
- **Output:** st=1086.92, rt=1087.88

### Step 22: Node 16215 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2268
  - nt1=732
  - nt2=0
  - parallel_workers=3
  - plan_width=148
  - reltuples=0.0000
  - rt1=1087.8763
  - rt2=0.0000
  - sel=3.0984
  - st1=1086.9184
  - st2=0.0000
  - startup_cost=71533.1000
  - total_cost=71801.4200
- **Output:** st=1120.83, rt=1123.90

### Step 23: Node 16214 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2268
  - nt1=2268
  - nt2=0
  - parallel_workers=0
  - plan_width=64
  - reltuples=0.0000
  - rt1=1123.9045
  - rt2=0.0000
  - sel=1.0000
  - st1=1120.8266
  - st2=0.0000
  - startup_cost=71533.1000
  - total_cost=71892.1400
- **Output:** st=1187.93, rt=1196.51
