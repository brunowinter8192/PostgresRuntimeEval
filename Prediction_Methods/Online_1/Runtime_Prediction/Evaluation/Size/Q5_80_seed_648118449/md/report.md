# Online Prediction Report

**Test Query:** Q5_80_seed_648118449
**Timestamp:** 2025-12-13 02:53:05

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 2.42%

## Phase C: Patterns in Query

- Total Patterns: 85

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 75736.1626 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 113504.2307 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 26.4017 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 172 | 6131.8766 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 19.6008 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 108.1438 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 140 | 6.2375 |
| 3e2d5a00 | Sort -> Hash Join (Outer) | 2 | 96 | 18.5586 |
| 46f37744 | Gather Merge -> Aggregate (Outer) | 2 | 48 | 2.8144 |
| 3754655c | Aggregate -> Sort (Outer) | 2 | 48 | 2.1302 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 1 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 2 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 3 | 7df893ad | 6131.8766 | -0.0000% | REJECTED | 17.92% |
| 4 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 5 | 2e0f44ef | 108.1438 | 0.0001% | REJECTED | 17.92% |
| 7 | 3e2d5a00 | 18.5586 | 0.0007% | REJECTED | 17.92% |
| 10 | f4cb205a | 75544.5822 | 0.0006% | REJECTED | 17.92% |
| 11 | bb930825 | 172.9284 | -0.0000% | REJECTED | 17.92% |
| 12 | c0a8d3de | 6113.5159 | -0.0000% | REJECTED | 17.92% |
| 15 | 2422d111 | 10.7757 | 0.0001% | REJECTED | 17.92% |
| 16 | ddb1e0ca | 13.6847 | -5.3651% | REJECTED | 17.92% |
| 20 | 37515ad8 | 168.3286 | -0.0000% | REJECTED | 17.92% |
| 21 | a54055ce | 6089.1983 | -0.0000% | REJECTED | 17.92% |
| 23 | 444761fb | 24.3176 | -0.0000% | REJECTED | 17.92% |
| 26 | 4db07220 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 31 | 545b5e57 | 153.1732 | -0.0000% | REJECTED | 17.92% |
| 32 | ec92bdaa | 15.1555 | -0.0000% | REJECTED | 17.92% |
| 33 | 440e6274 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 34 | 314469b0 | 20.7410 | 0.0000% | REJECTED | 17.92% |
| 40 | f4603221 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 42 | e1d7e5b4 | 13.2381 | -0.0000% | REJECTED | 17.92% |
| 43 | 54cb7f90 | 20.7410 | 0.0000% | REJECTED | 17.92% |
| 49 | 3d4c3db9 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 51 | c302739b | 13.2381 | -0.0000% | REJECTED | 17.92% |
| 57 | 9ce781b0 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 64 | a95bee4e | 5.9049 | 0.0000% | REJECTED | 17.92% |
## Query Tree

```
Node 9461 (Sort) - ROOT
  Node 9462 (Aggregate)
    Node 9463 (Gather Merge)
      Node 9464 (Aggregate)
        Node 9465 (Sort)
          Node 9466 (Hash Join)
            Node 9467 (Nested Loop)
              Node 9468 (Hash Join)
                Node 9469 (Seq Scan) - LEAF
                Node 9470 (Hash)
                  Node 9471 (Hash Join)
                    Node 9472 (Seq Scan) - LEAF
                    Node 9473 (Hash)
                      Node 9474 (Hash Join)
                        Node 9475 (Seq Scan) - LEAF
                        Node 9476 (Hash)
                          Node 9477 (Seq Scan) - LEAF
              Node 9478 (Index Scan) - LEAF
            Node 9479 (Hash)
              Node 9480 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 2.04%
- Improvement: 0.38%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 9461 | Sort | 1082.16 | 1104.24 | 2.0% | operator |
| 9462 | Aggregate | 1082.15 | 1057.87 | 2.2% | operator |
| 9463 | Gather Merge | 1082.14 | 1124.35 | 3.9% | operator |
| 9464 | Aggregate | 1076.77 | 1019.89 | 5.3% | operator |
| 9465 | Sort | 1076.52 | 1074.66 | 0.2% | operator |
| 9466 | Hash Join | 1076.01 | 1107.14 | 2.9% | operator |
| 9467 | Nested Loop | 1065.44 | 1102.69 | 3.5% | operator |
| 9479 | Hash | 2.62 | 14.79 | 464.0% | operator |
| 9468 | Hash Join | 207.93 | 234.18 | 12.6% | operator |
| 9478 | Index Scan | 0.07 | -0.03 | 133.5% | operator |
| 9480 | Seq Scan | 2.10 | 10.62 | 404.8% | operator |
| 9469 | Seq Scan | 162.60 | 161.95 | 0.4% | operator |
| 9470 | Hash | 32.24 | 21.31 | 33.9% | operator |
| 9471 | Hash Join | 31.53 | 62.87 | 99.4% | operator |
| 9472 | Seq Scan | 30.01 | 24.87 | 17.1% | operator |
| 9473 | Hash | 0.13 | 16.80 | 12721.8% | operator |
| 9474 | Hash Join | 0.13 | 142.84 | 111496.8% | operator |
| 9475 | Seq Scan | 0.01 | 10.49 | 131084.1% | operator |
| 9476 | Hash | 0.11 | 16.01 | 14072.5% | operator |
| 9477 | Seq Scan | 0.11 | 21.39 | 19345.4% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 9477 (Seq Scan) - LEAF

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

### Step 2: Node 9475 (Seq Scan) - LEAF

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

### Step 3: Node 9476 (Hash)

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

### Step 4: Node 9474 (Hash Join)

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

### Step 5: Node 9472 (Seq Scan) - LEAF

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

### Step 6: Node 9473 (Hash)

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

### Step 7: Node 9471 (Hash Join)

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

### Step 8: Node 9469 (Seq Scan) - LEAF

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

### Step 9: Node 9470 (Hash)

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

### Step 10: Node 9468 (Hash Join)

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

### Step 11: Node 9478 (Index Scan) - LEAF

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

### Step 12: Node 9480 (Seq Scan) - LEAF

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

### Step 13: Node 9467 (Nested Loop)

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

### Step 14: Node 9479 (Hash)

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

### Step 15: Node 9466 (Hash Join)

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

### Step 16: Node 9465 (Sort)

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

### Step 17: Node 9464 (Aggregate)

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

### Step 18: Node 9463 (Gather Merge)

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

### Step 19: Node 9462 (Aggregate)

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

### Step 20: Node 9461 (Sort) - ROOT

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
