# Online Prediction Report

**Test Query:** Q8_15_seed_114856434
**Timestamp:** 2025-12-13 01:57:15

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 3.77%

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
Node 14489 (Aggregate) - ROOT
  Node 14490 (Gather Merge)
    Node 14491 (Sort)
      Node 14492 (Hash Join)
        Node 14493 (Nested Loop)
          Node 14494 (Hash Join)
            Node 14495 (Nested Loop)
              Node 14496 (Hash Join)
                Node 14497 (Seq Scan) - LEAF
                Node 14498 (Hash)
                  Node 14499 (Hash Join)
                    Node 14500 (Seq Scan) - LEAF
                    Node 14501 (Hash)
                      Node 14502 (Hash Join)
                        Node 14503 (Seq Scan) - LEAF
                        Node 14504 (Hash)
                          Node 14505 (Seq Scan) - LEAF
              Node 14506 (Index Scan) - LEAF
            Node 14507 (Hash)
              Node 14508 (Seq Scan) - LEAF
          Node 14509 (Index Scan) - LEAF
        Node 14510 (Hash)
          Node 14511 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 3.01%
- Improvement: 0.76%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 14489 | Aggregate | 1227.16 | 1190.26 | 3.0% | operator |
| 14490 | Gather Merge | 1226.75 | 1123.88 | 8.4% | operator |
| 14491 | Sort | 1221.68 | 1087.88 | 11.0% | operator |
| 14492 | Hash Join | 1221.43 | 1055.48 | 13.6% | operator |
| 14493 | Nested Loop | 1221.10 | 1105.66 | 9.5% | operator |
| 14510 | Hash | 0.01 | 14.54 | 96831.4% | operator |
| 14494 | Hash Join | 1217.22 | 1027.31 | 15.6% | operator |
| 14509 | Index Scan | 0.01 | 0.05 | 753.5% | operator |
| 14511 | Seq Scan | 0.01 | 7.19 | 65304.3% | operator |
| 14495 | Nested Loop | 1171.35 | 1119.20 | 4.5% | operator |
| 14507 | Hash | 41.32 | 17.76 | 57.0% | operator |
| 14496 | Hash Join | 214.50 | 226.27 | 5.5% | operator |
| 14506 | Index Scan | 0.04 | 0.09 | 107.2% | operator |
| 14508 | Seq Scan | 41.16 | 44.48 | 8.1% | operator |
| 14497 | Seq Scan | 160.38 | 161.81 | 0.9% | operator |
| 14498 | Hash | 36.02 | 18.06 | 49.9% | operator |
| 14499 | Hash Join | 35.40 | 67.97 | 92.0% | operator |
| 14500 | Seq Scan | 33.83 | 24.87 | 26.5% | operator |
| 14501 | Hash | 0.21 | 17.93 | 8277.5% | operator |
| 14502 | Hash Join | 0.21 | 151.58 | 71740.5% | operator |
| 14503 | Seq Scan | 0.02 | 9.26 | 51348.0% | operator |
| 14504 | Hash | 0.18 | 16.01 | 8556.7% | operator |
| 14505 | Seq Scan | 0.18 | 21.39 | 11652.7% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 14505 (Seq Scan) - LEAF

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

### Step 2: Node 14503 (Seq Scan) - LEAF

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

### Step 3: Node 14504 (Hash)

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

### Step 4: Node 14502 (Hash Join)

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

### Step 5: Node 14500 (Seq Scan) - LEAF

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

### Step 6: Node 14501 (Hash)

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

### Step 7: Node 14499 (Hash Join)

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

### Step 8: Node 14497 (Seq Scan) - LEAF

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

### Step 9: Node 14498 (Hash)

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

### Step 10: Node 14496 (Hash Join)

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

### Step 11: Node 14506 (Index Scan) - LEAF

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

### Step 12: Node 14508 (Seq Scan) - LEAF

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

### Step 13: Node 14495 (Nested Loop)

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

### Step 14: Node 14507 (Hash)

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

### Step 15: Node 14494 (Hash Join)

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

### Step 16: Node 14509 (Index Scan) - LEAF

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

### Step 17: Node 14511 (Seq Scan) - LEAF

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

### Step 18: Node 14493 (Nested Loop)

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

### Step 19: Node 14510 (Hash)

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

### Step 20: Node 14492 (Hash Join)

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

### Step 21: Node 14491 (Sort)

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

### Step 22: Node 14490 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2480
  - nt1=800
  - nt2=0
  - parallel_workers=3
  - plan_width=148
  - reltuples=0.0000
  - rt1=1087.8814
  - rt2=0.0000
  - sel=3.1000
  - st1=1086.9234
  - st2=0.0000
  - startup_cost=71558.4000
  - total_cost=71851.8000
- **Output:** st=1120.80, rt=1123.88

### Step 23: Node 14489 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2406
  - nt1=2480
  - nt2=0
  - parallel_workers=0
  - plan_width=64
  - reltuples=0.0000
  - rt1=1123.8782
  - rt2=0.0000
  - sel=0.9702
  - st1=1120.7998
  - st2=0.0000
  - startup_cost=71558.4000
  - total_cost=71949.5200
- **Output:** st=1184.29, rt=1190.26
