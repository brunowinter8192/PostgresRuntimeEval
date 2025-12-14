# Online Prediction Report

**Test Query:** Q5_92_seed_746566821
**Timestamp:** 2025-12-13 01:44:05

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 5.01%

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
Node 9721 (Sort) - ROOT
  Node 9722 (Aggregate)
    Node 9723 (Gather Merge)
      Node 9724 (Aggregate)
        Node 9725 (Sort)
          Node 9726 (Hash Join)
            Node 9727 (Nested Loop)
              Node 9728 (Hash Join)
                Node 9729 (Seq Scan) - LEAF
                Node 9730 (Hash)
                  Node 9731 (Hash Join)
                    Node 9732 (Seq Scan) - LEAF
                    Node 9733 (Hash)
                      Node 9734 (Hash Join)
                        Node 9735 (Seq Scan) - LEAF
                        Node 9736 (Hash)
                          Node 9737 (Seq Scan) - LEAF
              Node 9738 (Index Scan) - LEAF
            Node 9739 (Hash)
              Node 9740 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 4.62%
- Improvement: 0.39%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 9721 | Sort | 1055.46 | 1104.23 | 4.6% | operator |
| 9722 | Aggregate | 1055.44 | 1057.98 | 0.2% | operator |
| 9723 | Gather Merge | 1055.43 | 1124.38 | 6.5% | operator |
| 9724 | Aggregate | 1050.71 | 1020.01 | 2.9% | operator |
| 9725 | Sort | 1050.45 | 1074.62 | 2.3% | operator |
| 9726 | Hash Join | 1049.93 | 1106.62 | 5.4% | operator |
| 9727 | Nested Loop | 1038.23 | 1102.43 | 6.2% | operator |
| 9739 | Hash | 2.74 | 14.79 | 439.3% | operator |
| 9728 | Hash Join | 217.04 | 234.19 | 7.9% | operator |
| 9738 | Index Scan | 0.07 | -0.03 | 135.4% | operator |
| 9740 | Seq Scan | 2.22 | 10.62 | 378.0% | operator |
| 9729 | Seq Scan | 168.39 | 161.94 | 3.8% | operator |
| 9730 | Hash | 33.42 | 21.31 | 36.2% | operator |
| 9731 | Hash Join | 32.64 | 62.87 | 92.6% | operator |
| 9732 | Seq Scan | 30.88 | 24.87 | 19.5% | operator |
| 9733 | Hash | 0.36 | 16.80 | 4501.8% | operator |
| 9734 | Hash Join | 0.36 | 142.84 | 39359.6% | operator |
| 9735 | Seq Scan | 0.01 | 10.49 | 74862.3% | operator |
| 9736 | Hash | 0.34 | 16.01 | 4638.1% | operator |
| 9737 | Seq Scan | 0.33 | 21.39 | 6304.2% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 9737 (Seq Scan) - LEAF

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

### Step 2: Node 9735 (Seq Scan) - LEAF

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

### Step 3: Node 9736 (Hash)

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

### Step 4: Node 9734 (Hash Join)

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

### Step 5: Node 9732 (Seq Scan) - LEAF

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

### Step 6: Node 9733 (Hash)

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

### Step 7: Node 9731 (Hash Join)

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

### Step 8: Node 9729 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=73059
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0487
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=33394.0600
- **Output:** st=0.18, rt=161.94

### Step 9: Node 9730 (Hash)

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

### Step 10: Node 9728 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14612
  - nt1=73059
  - nt2=12500
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=161.9437
  - rt2=21.3137
  - sel=0.0000
  - st1=0.1785
  - st2=21.3132
  - startup_cost=4743.0900
  - total_cost=38472.0100
- **Output:** st=24.77, rt=234.19

### Step 11: Node 9738 (Index Scan) - LEAF

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
  - total_cost=1.1500
- **Output:** st=0.07, rt=-0.03

### Step 12: Node 9740 (Seq Scan) - LEAF

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

### Step 13: Node 9727 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=58459
  - nt1=14612
  - nt2=5
  - parallel_workers=0
  - plan_width=128
  - reltuples=0.0000
  - rt1=234.1855
  - rt2=-0.0251
  - sel=0.8002
  - st1=24.7651
  - st2=0.0674
  - startup_cost=4743.5200
  - total_cost=55959.8900
- **Output:** st=42.49, rt=1102.43

### Step 14: Node 9739 (Hash)

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

### Step 15: Node 9726 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2338
  - nt1=58459
  - nt2=10000
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=1102.4340
  - rt2=14.7884
  - sel=0.0000
  - st1=42.4883
  - st2=14.7887
  - startup_cost=5216.5200
  - total_cost=56739.8000
- **Output:** st=49.37, rt=1106.62

### Step 16: Node 9725 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2338
  - nt1=2338
  - nt2=0
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=1106.6216
  - rt2=0.0000
  - sel=1.0000
  - st1=49.3672
  - st2=0.0000
  - startup_cost=56870.6200
  - total_cost=56876.4700
- **Output:** st=1073.70, rt=1074.62

### Step 17: Node 9724 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=2338
  - nt2=0
  - parallel_workers=0
  - plan_width=136
  - reltuples=0.0000
  - rt1=1074.6211
  - rt2=0.0000
  - sel=0.0107
  - st1=1073.6989
  - st2=0.0000
  - startup_cost=56870.6200
  - total_cost=56900.1600
- **Output:** st=1017.98, rt=1020.01

### Step 18: Node 9723 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=75
  - nt1=25
  - nt2=0
  - parallel_workers=3
  - plan_width=136
  - reltuples=0.0000
  - rt1=1020.0115
  - rt2=0.0000
  - sel=3.0000
  - st1=1017.9762
  - st2=0.0000
  - startup_cost=57870.6600
  - total_cost=57909.0100
- **Output:** st=1121.37, rt=1124.38

### Step 19: Node 9722 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=75
  - nt2=0
  - parallel_workers=0
  - plan_width=136
  - reltuples=0.0000
  - rt1=1124.3842
  - rt2=0.0000
  - sel=0.3333
  - st1=1121.3663
  - st2=0.0000
  - startup_cost=57870.6600
  - total_cost=57909.8900
- **Output:** st=1074.39, rt=1057.98

### Step 20: Node 9721 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=25
  - nt2=0
  - parallel_workers=0
  - plan_width=136
  - reltuples=0.0000
  - rt1=1057.9756
  - rt2=0.0000
  - sel=1.0000
  - st1=1074.3861
  - st2=0.0000
  - startup_cost=57910.4700
  - total_cost=57910.5300
- **Output:** st=1102.40, rt=1104.23
