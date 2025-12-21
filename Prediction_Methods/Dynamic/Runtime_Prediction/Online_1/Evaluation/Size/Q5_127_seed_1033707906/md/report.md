# Online Prediction Report

**Test Query:** Q5_127_seed_1033707906
**Timestamp:** 2025-12-21 15:15:38

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17051 | Operator + Pattern Training |
| Training_Test | 4268 | Pattern Selection Eval |
| Training | 21319 | Final Model Training |
| Test | 3000 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 3.36%

## Phase C: Patterns in Query

- Total Patterns: 85

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 368 | 15859.1% | 58361.5143 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 360 | 40138.8% | 144499.6064 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 210 | 15.1% | 31.8055 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 180 | 12.6% | 22.6523 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 158 | 2790.8% | 4409.3994 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 150 | 87.2% | 130.7419 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 142 | 4.2% | 5.9004 |
| 3e2d5a00 | Sort -> Hash Join (Outer) | 2 | 90 | 25.8% | 23.2555 |
| 46f37744 | Gather Merge -> Aggregate (Outer) | 2 | 30 | 7.7% | 2.3145 |
| 3754655c | Aggregate -> Sort (Outer) | 2 | 30 | 4.1% | 1.2175 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 180 | 32329.9% | 58193.8858 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 128 | 112.3% | 143.7620 |
| c0a8d3de | Hash -> Hash Join -> [Seq Scan (Outer), ... | 3 | 128 | 3427.7% | 4387.4701 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 112 | 2.8% | 3.0826 |
| 91d6e559 | Sort -> Hash Join -> [Nested Loop (Outer... | 3 | 60 | 8.0% | 4.7942 |
| 2422d111 | Hash Join -> [Nested Loop -> [Hash Join ... | 3 | 60 | 16.0% | 9.5977 |
| ddb1e0ca | Sort -> Aggregate -> Gather Merge (Outer... | 3 | 30 | 51.7% | 15.5228 |
| 8a8c43c6 | Aggregate -> Gather Merge -> Aggregate (... | 3 | 30 | 4.2% | 1.2555 |
| e6c1e0d8 | Gather Merge -> Aggregate -> Sort (Outer... | 3 | 30 | 7.7% | 2.3145 |
| 37515ad8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 98 | 142.5% | 139.6620 |
| a54055ce | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 90 | 4855.4% | 4369.8323 |
| bd9dfa7b | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 82 | 3.0% | 2.4909 |
| 444761fb | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 38 | 46.4% | 17.6378 |
| 460af52c | Aggregate -> Gather Merge -> Aggregate -... | 4 | 30 | 4.2% | 1.2555 |
| 12e6457c | Sort -> Hash Join -> [Nested Loop -> [Ha... | 4 | 30 | 11.3% | 3.3821 |
| 4db07220 | Hash Join -> [Nested Loop -> [Hash Join ... | 4 | 30 | 17.3% | 5.2041 |
| 9d0e407c | Nested Loop -> [Hash Join -> [Seq Scan (... | 5 | 60 | 3.0% | 1.7738 |
| 545b5e57 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 60 | 213.5% | 128.0948 |
| ec92bdaa | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 38 | 30.4% | 11.5672 |
| 440e6274 | Hash Join -> [Nested Loop -> [Hash Join ... | 5 | 30 | 17.3% | 5.2041 |
| 314469b0 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 5 | 30 | 35.5% | 10.6486 |
| f4603221 | Hash Join -> [Nested Loop -> [Hash Join ... | 6 | 30 | 17.3% | 5.2041 |
| 5bfce159 | Nested Loop -> [Hash Join -> [Seq Scan (... | 6 | 30 | 2.8% | 0.8258 |
| e1d7e5b4 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 30 | 26.7% | 8.0206 |
| 54cb7f90 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 6 | 30 | 35.5% | 10.6486 |
| 3d4c3db9 | Hash Join -> [Nested Loop -> [Hash Join ... | 7 | 30 | 17.3% | 5.2041 |
| ef93d4fc | Nested Loop -> [Hash Join -> [Seq Scan (... | 7 | 30 | 2.8% | 0.8258 |
| c302739b | Hash Join -> [Seq Scan (Outer), Hash -> ... | 7 | 30 | 26.7% | 8.0206 |
| 9ce781b0 | Hash Join -> [Nested Loop -> [Hash Join ... | 8 | 30 | 17.3% | 5.2041 |
| 5ae97df8 | Nested Loop -> [Hash Join -> [Seq Scan (... | 8 | 30 | 2.8% | 0.8258 |
| a95bee4e | Hash Join -> [Nested Loop -> [Hash Join ... | 9 | 30 | 17.3% | 5.2041 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 58361.5143 | 0.0007% | REJECTED | 18.02% |
| 1 | 3aab37be | 144499.6064 | -0.0000% | REJECTED | 18.02% |
| 2 | 1d35fb97 | 31.8055 | -0.0106% | REJECTED | 18.02% |
| 3 | 2724c080 | 22.6523 | -0.3132% | REJECTED | 18.02% |
| 4 | 7df893ad | 4409.3994 | -0.0000% | REJECTED | 18.02% |
| 5 | 2e0f44ef | 130.7419 | 0.0001% | REJECTED | 18.02% |
| 6 | 3cfa90d7 | 5.9004 | N/A | SKIPPED_LOW_ERROR | 18.02% |
| 7 | 3e2d5a00 | 23.2555 | 0.0090% | REJECTED | 18.02% |
| 8 | 46f37744 | 2.3145 | N/A | SKIPPED_LOW_ERROR | 18.02% |
| 9 | 3754655c | 1.2175 | N/A | SKIPPED_LOW_ERROR | 18.02% |
| 10 | f4cb205a | 58193.8858 | 0.0006% | REJECTED | 18.02% |
| 11 | bb930825 | 143.7620 | -0.0000% | REJECTED | 18.02% |
| 12 | c0a8d3de | 4387.4701 | -0.0000% | REJECTED | 18.02% |
| 13 | e0e3c3e1 | 3.0826 | N/A | SKIPPED_LOW_ERROR | 18.02% |
| 14 | 91d6e559 | 4.7942 | N/A | SKIPPED_LOW_ERROR | 18.02% |
| 15 | 2422d111 | 9.5977 | 0.0001% | REJECTED | 18.02% |
| 16 | ddb1e0ca | 15.5228 | 0.1072% | REJECTED | 18.02% |
| 17 | 8a8c43c6 | 1.2555 | N/A | SKIPPED_LOW_ERROR | 18.02% |
| 18 | e6c1e0d8 | 2.3145 | N/A | SKIPPED_LOW_ERROR | 18.02% |
| 19 | 37515ad8 | 139.6620 | -0.0000% | REJECTED | 18.02% |
| 20 | a54055ce | 4369.8323 | -0.0000% | REJECTED | 18.02% |
| 21 | bd9dfa7b | 2.4909 | N/A | SKIPPED_LOW_ERROR | 18.02% |
| 22 | 444761fb | 17.6378 | -0.0000% | REJECTED | 18.02% |
| 23 | 460af52c | 1.2555 | N/A | SKIPPED_LOW_ERROR | 18.02% |
| 24 | 12e6457c | 3.3821 | 0.0011% | REJECTED | 18.02% |
| 25 | 4db07220 | 5.2041 | 0.0000% | REJECTED | 18.02% |
| 26 | 9d0e407c | 1.7738 | N/A | SKIPPED_LOW_ERROR | 18.02% |
| 27 | 545b5e57 | 128.0948 | -0.0000% | REJECTED | 18.02% |
| 28 | ec92bdaa | 11.5672 | -0.0000% | REJECTED | 18.02% |
| 29 | 440e6274 | 5.2041 | 0.0000% | REJECTED | 18.02% |
| 30 | 314469b0 | 10.6486 | 0.0000% | REJECTED | 18.02% |
| 31 | f4603221 | 5.2041 | 0.0000% | REJECTED | 18.02% |
| 32 | 5bfce159 | 0.8258 | N/A | SKIPPED_LOW_ERROR | 18.02% |
| 33 | e1d7e5b4 | 8.0206 | -0.0000% | REJECTED | 18.02% |
| 34 | 54cb7f90 | 10.6486 | 0.0000% | REJECTED | 18.02% |
| 35 | 3d4c3db9 | 5.2041 | 0.0000% | REJECTED | 18.02% |
| 36 | ef93d4fc | 0.8258 | N/A | SKIPPED_LOW_ERROR | 18.02% |
| 37 | c302739b | 8.0206 | -0.0000% | REJECTED | 18.02% |
| 38 | 9ce781b0 | 5.2041 | 0.0000% | REJECTED | 18.02% |
| 39 | 5ae97df8 | 0.8258 | N/A | SKIPPED_LOW_ERROR | 18.02% |
| 40 | a95bee4e | 5.2041 | 0.0000% | REJECTED | 18.02% |
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


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 3.08%
- Improvement: 0.28%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 7481 | Sort | 1066.07 | 1098.96 | 3.1% | operator |
| 7482 | Aggregate | 1066.06 | 1032.53 | 3.1% | operator |
| 7483 | Gather Merge | 1066.05 | 1133.57 | 6.3% | operator |
| 7484 | Aggregate | 1060.91 | 985.86 | 7.1% | operator |
| 7485 | Sort | 1060.66 | 1068.17 | 0.7% | operator |
| 7486 | Hash Join | 1060.14 | 1131.80 | 6.8% | operator |
| 7487 | Nested Loop | 1048.04 | 1188.56 | 13.4% | operator |
| 7499 | Hash | 3.59 | 18.67 | 420.2% | operator |
| 7488 | Hash Join | 220.12 | 252.47 | 14.7% | operator |
| 7498 | Index Scan | 0.07 | -0.22 | 401.4% | operator |
| 7500 | Seq Scan | 3.05 | 12.36 | 305.1% | operator |
| 7489 | Seq Scan | 170.26 | 159.81 | 6.1% | operator |
| 7490 | Hash | 36.63 | 22.67 | 38.1% | operator |
| 7491 | Hash Join | 35.61 | 102.01 | 186.5% | operator |
| 7492 | Seq Scan | 34.19 | 24.28 | 29.0% | operator |
| 7493 | Hash | 0.06 | 21.93 | 35272.0% | operator |
| 7494 | Hash Join | 0.06 | 284.32 | 481803.9% | operator |
| 7495 | Seq Scan | 0.01 | 11.81 | 147503.4% | operator |
| 7496 | Hash | 0.04 | 21.05 | 48861.0% | operator |
| 7497 | Seq Scan | 0.04 | 22.93 | 55835.0% | operator |

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
- **Output:** st=0.17, rt=22.93

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
- **Output:** st=-0.03, rt=11.81

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
  - rt1=22.9333
  - rt2=0.0000
  - sel=1.0000
  - st1=0.1690
  - st2=0.0000
  - startup_cost=1.0600
  - total_cost=1.0600
- **Output:** st=21.05, rt=21.05

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
  - rt1=11.8083
  - rt2=21.0532
  - sel=0.2000
  - st1=-0.0333
  - st2=21.0522
  - startup_cost=1.0700
  - total_cost=2.4000
- **Output:** st=16.34, rt=284.32

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
- **Output:** st=0.35, rt=24.28

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
  - rt1=284.3233
  - rt2=0.0000
  - sel=1.0000
  - st1=16.3403
  - st2=0.0000
  - startup_cost=2.4000
  - total_cost=2.4000
- **Output:** st=21.93, rt=21.93

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
  - rt1=24.2787
  - rt2=21.9306
  - sel=0.0400
  - st1=0.3531
  - st2=21.9306
  - startup_cost=2.4600
  - total_cost=4586.8400
- **Output:** st=3.41, rt=102.01

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
- **Output:** st=0.14, rt=159.81

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
  - rt1=102.0102
  - rt2=0.0000
  - sel=1.0000
  - st1=3.4058
  - st2=0.0000
  - startup_cost=4586.8400
  - total_cost=4586.8400
- **Output:** st=22.67, rt=22.67

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
  - rt1=159.8129
  - rt2=22.6725
  - sel=0.0000
  - st1=0.1444
  - st2=22.6725
  - startup_cost=4743.0900
  - total_cost=38478.2400
- **Output:** st=16.82, rt=252.47

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
- **Output:** st=0.04, rt=-0.22

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
- **Output:** st=0.03, rt=12.36

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
  - rt1=252.4696
  - rt2=-0.2200
  - sel=0.8001
  - st1=16.8155
  - st2=0.0370
  - startup_cost=4743.5200
  - total_cost=56121.2800
- **Output:** st=100.31, rt=1188.56

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
  - rt1=12.3595
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0320
  - st2=0.0000
  - startup_cost=323.0000
  - total_cost=323.0000
- **Output:** st=18.67, rt=18.67

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
  - rt1=1188.5636
  - rt2=18.6713
  - sel=0.0000
  - st1=100.3074
  - st2=18.6703
  - startup_cost=5216.5200
  - total_cost=56906.9000
- **Output:** st=100.42, rt=1131.80

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
  - rt1=1131.8048
  - rt2=0.0000
  - sel=1.0000
  - st1=100.4230
  - st2=0.0000
  - startup_cost=57040.5100
  - total_cost=57046.4600
- **Output:** st=1067.49, rt=1068.17

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
  - rt1=1068.1654
  - rt2=0.0000
  - sel=0.0105
  - st1=1067.4909
  - st2=0.0000
  - startup_cost=57040.5100
  - total_cost=57070.5900
- **Output:** st=976.23, rt=985.86

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
  - rt1=985.8579
  - rt2=0.0000
  - sel=3.0000
  - st1=976.2341
  - st2=0.0000
  - startup_cost=58040.5500
  - total_cost=58079.4500
- **Output:** st=1130.52, rt=1133.57

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
  - rt1=1133.5658
  - rt2=0.0000
  - sel=0.3333
  - st1=1130.5186
  - st2=0.0000
  - startup_cost=58040.5500
  - total_cost=58080.3200
- **Output:** st=1048.66, rt=1032.53

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
  - rt1=1032.5317
  - rt2=0.0000
  - sel=1.0000
  - st1=1048.6634
  - st2=0.0000
  - startup_cost=58080.9000
  - total_cost=58080.9600
- **Output:** st=1097.56, rt=1098.96
