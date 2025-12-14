# Online Prediction Report

**Test Query:** Q5_127_seed_1033707906
**Timestamp:** 2025-12-13 01:36:58

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 3.97%

## Phase C: Patterns in Query

- Total Patterns: 85

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
| 10 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 11 | 444761fb | 24.3176 | -0.0000% | REJECTED | 17.92% |
| 12 | 314469b0 | 20.7410 | 0.0000% | REJECTED | 17.92% |
| 13 | 54cb7f90 | 20.7410 | 0.0000% | REJECTED | 17.92% |
| 14 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 15 | 3e2d5a00 | 18.5586 | 0.0007% | REJECTED | 17.92% |
| 16 | ec92bdaa | 15.1555 | -0.0000% | REJECTED | 17.92% |
| 17 | ddb1e0ca | 13.6847 | -5.3651% | REJECTED | 17.92% |
| 18 | e1d7e5b4 | 13.2381 | -0.0000% | REJECTED | 17.92% |
| 19 | c302739b | 13.2381 | -0.0000% | REJECTED | 17.92% |
| 20 | 2422d111 | 10.7757 | 0.0001% | REJECTED | 17.92% |
| 22 | 4db07220 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 23 | 440e6274 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 24 | f4603221 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 25 | 3d4c3db9 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 26 | 9ce781b0 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 27 | a95bee4e | 5.9049 | 0.0000% | REJECTED | 17.92% |
## Query Tree

```
Node 7481 (Sort) - ROOT
  Node 7482 (Aggregate)
    Node 7483 (Gather Merge)
      Node 7484 (Aggregate)
        Node 7485 (Sort)
          Node 7486 (Hash Join)
            Node 7487 (Nested Loop)
              Node 7488 (Hash Join)
                Node 7489 (Seq Scan) - LEAF
                Node 7490 (Hash)
                  Node 7491 (Hash Join)
                    Node 7492 (Seq Scan) - LEAF
                    Node 7493 (Hash)
                      Node 7494 (Hash Join)
                        Node 7495 (Seq Scan) - LEAF
                        Node 7496 (Hash)
                          Node 7497 (Seq Scan) - LEAF
              Node 7498 (Index Scan) - LEAF
            Node 7499 (Hash)
              Node 7500 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 3.58%
- Improvement: 0.39%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 7481 | Sort | 1066.07 | 1104.24 | 3.6% | operator |
| 7482 | Aggregate | 1066.06 | 1057.87 | 0.8% | operator |
| 7483 | Gather Merge | 1066.05 | 1124.35 | 5.5% | operator |
| 7484 | Aggregate | 1060.91 | 1019.89 | 3.9% | operator |
| 7485 | Sort | 1060.66 | 1074.66 | 1.3% | operator |
| 7486 | Hash Join | 1060.14 | 1107.14 | 4.4% | operator |
| 7487 | Nested Loop | 1048.04 | 1102.69 | 5.2% | operator |
| 7499 | Hash | 3.59 | 14.79 | 312.0% | operator |
| 7488 | Hash Join | 220.12 | 234.18 | 6.4% | operator |
| 7498 | Index Scan | 0.07 | -0.03 | 134.4% | operator |
| 7500 | Seq Scan | 3.05 | 10.62 | 248.0% | operator |
| 7489 | Seq Scan | 170.26 | 161.95 | 4.9% | operator |
| 7490 | Hash | 36.63 | 21.31 | 41.8% | operator |
| 7491 | Hash Join | 35.61 | 62.87 | 76.6% | operator |
| 7492 | Seq Scan | 34.19 | 24.87 | 27.3% | operator |
| 7493 | Hash | 0.06 | 16.80 | 26991.2% | operator |
| 7494 | Hash Join | 0.06 | 142.84 | 242008.3% | operator |
| 7495 | Seq Scan | 0.01 | 10.49 | 131084.1% | operator |
| 7496 | Hash | 0.04 | 16.01 | 37144.0% | operator |
| 7497 | Seq Scan | 0.04 | 21.39 | 52070.6% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 7497 (Seq Scan) - LEAF

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

### Step 2: Node 7495 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=1
  - nt=25
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=112
  - reltuples=25.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=1.2500
- **Output:** st=-0.02, rt=10.49

### Step 3: Node 7496 (Hash)

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

### Step 4: Node 7494 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=25
  - nt2=1
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=10.4947
  - rt2=16.0149
  - sel=0.2000
  - st1=-0.0152
  - st2=16.0154
  - startup_cost=1.0700
  - total_cost=2.4000
- **Output:** st=1.92, rt=142.84

### Step 5: Node 7492 (Seq Scan) - LEAF

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

### Step 6: Node 7493 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=5
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=142.8439
  - rt2=0.0000
  - sel=1.0000
  - st1=1.9164
  - st2=0.0000
  - startup_cost=2.4000
  - total_cost=2.4000
- **Output:** st=16.80, rt=16.80

### Step 7: Node 7491 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=12500
  - nt1=62500
  - nt2=5
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=24.8735
  - rt2=16.7965
  - sel=0.0400
  - st1=0.2761
  - st2=16.7962
  - startup_cost=2.4600
  - total_cost=4586.8400
- **Output:** st=3.04, rt=62.87

### Step 8: Node 7489 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=74418
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0496
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=33394.0600
- **Output:** st=0.18, rt=161.95

### Step 9: Node 7490 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=12500
  - nt1=12500
  - nt2=0
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=62.8708
  - rt2=0.0000
  - sel=1.0000
  - st1=3.0413
  - st2=0.0000
  - startup_cost=4586.8400
  - total_cost=4586.8400
- **Output:** st=21.31, rt=21.31

### Step 10: Node 7488 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14884
  - nt1=74418
  - nt2=12500
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=161.9546
  - rt2=21.3137
  - sel=0.0000
  - st1=0.1790
  - st2=21.3132
  - startup_cost=4743.0900
  - total_cost=38478.2400
- **Output:** st=24.76, rt=234.18

### Step 11: Node 7498 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=5
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=20
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.4300
  - total_cost=1.1400
- **Output:** st=0.07, rt=-0.03

### Step 12: Node 7500 (Seq Scan) - LEAF

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
- **Output:** st=0.04, rt=10.62

### Step 13: Node 7487 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=59546
  - nt1=14884
  - nt2=5
  - parallel_workers=0
  - plan_width=128
  - reltuples=0.0000
  - rt1=234.1837
  - rt2=-0.0251
  - sel=0.8001
  - st1=24.7647
  - st2=0.0674
  - startup_cost=4743.5200
  - total_cost=56121.2800
- **Output:** st=42.63, rt=1102.69

### Step 14: Node 7499 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=10000
  - nt1=10000
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=0.0000
  - rt1=10.6168
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0355
  - st2=0.0000
  - startup_cost=323.0000
  - total_cost=323.0000
- **Output:** st=14.79, rt=14.79

### Step 15: Node 7486 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2382
  - nt1=59546
  - nt2=10000
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=1102.6872
  - rt2=14.7884
  - sel=0.0000
  - st1=42.6265
  - st2=14.7887
  - startup_cost=5216.5200
  - total_cost=56906.9000
- **Output:** st=49.51, rt=1107.14

### Step 16: Node 7485 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2382
  - nt1=2382
  - nt2=0
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=1107.1381
  - rt2=0.0000
  - sel=1.0000
  - st1=49.5074
  - st2=0.0000
  - startup_cost=57040.5100
  - total_cost=57046.4600
- **Output:** st=1073.74, rt=1074.66

### Step 17: Node 7484 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=2382
  - nt2=0
  - parallel_workers=0
  - plan_width=136
  - reltuples=0.0000
  - rt1=1074.6625
  - rt2=0.0000
  - sel=0.0105
  - st1=1073.7395
  - st2=0.0000
  - startup_cost=57040.5100
  - total_cost=57070.5900
- **Output:** st=1017.87, rt=1019.89

### Step 18: Node 7483 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=75
  - nt1=25
  - nt2=0
  - parallel_workers=3
  - plan_width=136
  - reltuples=0.0000
  - rt1=1019.8930
  - rt2=0.0000
  - sel=3.0000
  - st1=1017.8677
  - st2=0.0000
  - startup_cost=58040.5500
  - total_cost=58079.4500
- **Output:** st=1121.33, rt=1124.35

### Step 19: Node 7482 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=75
  - nt2=0
  - parallel_workers=0
  - plan_width=136
  - reltuples=0.0000
  - rt1=1124.3522
  - rt2=0.0000
  - sel=0.3333
  - st1=1121.3337
  - st2=0.0000
  - startup_cost=58040.5500
  - total_cost=58080.3200
- **Output:** st=1074.31, rt=1057.87

### Step 20: Node 7481 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=25
  - nt2=0
  - parallel_workers=0
  - plan_width=136
  - reltuples=0.0000
  - rt1=1057.8672
  - rt2=0.0000
  - sel=1.0000
  - st1=1074.3091
  - st2=0.0000
  - startup_cost=58080.9000
  - total_cost=58080.9600
- **Output:** st=1102.40, rt=1104.24
