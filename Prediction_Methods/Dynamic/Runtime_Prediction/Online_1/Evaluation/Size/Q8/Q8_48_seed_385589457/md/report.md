# Online Prediction Report

**Test Query:** Q8_48_seed_385589457
**Timestamp:** 2025-12-21 16:48:52

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 16691 | Operator + Pattern Training |
| Training_Test | 4178 | Pattern Selection Eval |
| Training | 20869 | Final Model Training |
| Test | 3450 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 4.90%

## Phase C: Patterns in Query

- Total Patterns: 82

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 368 | 24023.0% | 88404.7276 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 330 | 31979.6% | 105532.5343 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 180 | 12.9% | 23.2084 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 158 | 3454.0% | 5457.3989 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 120 | 122.9% | 147.4435 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 112 | 3.0% | 3.3617 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 90 | 6.8% | 6.0954 |
| 3e2d5a00 | Sort -> Hash Join (Outer) | 2 | 90 | 23.4% | 21.0975 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 180 | 49034.6% | 88262.2269 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 128 | 92.4% | 118.3091 |
| c0a8d3de | Hash -> Hash Join -> [Seq Scan (Outer), ... | 3 | 128 | 4246.5% | 5435.4562 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 112 | 3.0% | 3.3617 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 90 | 5.1% | 4.6238 |
| 91d6e559 | Sort -> Hash Join -> [Nested Loop (Outer... | 3 | 60 | 4.3% | 2.5954 |
| 98d4ff98 | Gather Merge -> Sort -> Hash Join (Outer... | 3 | 30 | 5.9% | 1.7696 |
| 2422d111 | Hash Join -> [Nested Loop -> [Hash Join ... | 3 | 30 | 16.6% | 4.9895 |
| 37515ad8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 98 | 115.9% | 113.5563 |
| a54055ce | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 90 | 6018.4% | 5416.5582 |
| bd9dfa7b | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 82 | 3.2% | 2.6341 |
| 444761fb | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 38 | 49.7% | 18.8979 |
| b149ff28 | Aggregate -> Gather Merge -> Sort -> Has... | 4 | 30 | 1.3% | 0.3955 |
| 3c6d8006 | Gather Merge -> Sort -> Hash Join -> [Ne... | 4 | 30 | 5.9% | 1.7696 |
| 12e6457c | Sort -> Hash Join -> [Nested Loop -> [Ha... | 4 | 30 | 2.1% | 0.6430 |
| 4db07220 | Hash Join -> [Nested Loop -> [Hash Join ... | 4 | 30 | 16.6% | 4.9895 |
| 9d0e407c | Nested Loop -> [Hash Join -> [Seq Scan (... | 5 | 60 | 3.3% | 1.9789 |
| 545b5e57 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 60 | 173.7% | 104.2271 |
| ec92bdaa | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 38 | 24.6% | 9.3291 |
| 53f9aa07 | Aggregate -> Gather Merge -> Sort -> Has... | 5 | 30 | 1.3% | 0.3955 |
| 440e6274 | Hash Join -> [Nested Loop -> [Hash Join ... | 5 | 30 | 16.6% | 4.9895 |
| 314469b0 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 5 | 30 | 39.7% | 11.9093 |
| f4603221 | Hash Join -> [Nested Loop -> [Hash Join ... | 6 | 30 | 16.6% | 4.9895 |
| 5bfce159 | Nested Loop -> [Hash Join -> [Seq Scan (... | 6 | 30 | 5.2% | 1.5619 |
| e1d7e5b4 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 30 | 18.5% | 5.5387 |
| 54cb7f90 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 6 | 30 | 39.7% | 11.9093 |
| 3d4c3db9 | Hash Join -> [Nested Loop -> [Hash Join ... | 7 | 30 | 16.6% | 4.9895 |
| ef93d4fc | Nested Loop -> [Hash Join -> [Seq Scan (... | 7 | 30 | 5.2% | 1.5619 |
| c302739b | Hash Join -> [Seq Scan (Outer), Hash -> ... | 7 | 30 | 18.5% | 5.5387 |
| 9ce781b0 | Hash Join -> [Nested Loop -> [Hash Join ... | 8 | 30 | 16.6% | 4.9895 |
| 5ae97df8 | Nested Loop -> [Hash Join -> [Seq Scan (... | 8 | 30 | 5.2% | 1.5619 |
| a95bee4e | Hash Join -> [Nested Loop -> [Hash Join ... | 9 | 30 | 16.6% | 4.9895 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 88404.7276 | 0.0009% | REJECTED | 17.99% |
| 1 | 3aab37be | 105532.5343 | -0.0000% | REJECTED | 17.99% |
| 2 | 2724c080 | 23.2084 | 0.4114% | REJECTED | 17.99% |
| 3 | 7df893ad | 5457.3989 | -0.0000% | REJECTED | 17.99% |
| 4 | 2e0f44ef | 147.4435 | 0.0000% | REJECTED | 17.99% |
| 5 | 3cfa90d7 | 3.3617 | N/A | SKIPPED_LOW_ERROR | 17.99% |
| 6 | 1691f6f0 | 6.0954 | N/A | SKIPPED_LOW_ERROR | 17.99% |
| 7 | 3e2d5a00 | 21.0975 | 0.0009% | REJECTED | 17.99% |
| 8 | f4cb205a | 88262.2269 | 0.0006% | REJECTED | 17.99% |
| 9 | bb930825 | 118.3091 | -0.0000% | REJECTED | 17.99% |
| 10 | c0a8d3de | 5435.4562 | -0.0000% | REJECTED | 17.99% |
| 11 | e0e3c3e1 | 3.3617 | N/A | SKIPPED_LOW_ERROR | 17.99% |
| 12 | 29ee00db | 4.6238 | N/A | SKIPPED_LOW_ERROR | 17.99% |
| 13 | 91d6e559 | 2.5954 | N/A | SKIPPED_LOW_ERROR | 17.99% |
| 14 | 98d4ff98 | 1.7696 | N/A | SKIPPED_LOW_ERROR | 17.99% |
| 15 | 2422d111 | 4.9895 | -0.0000% | REJECTED | 17.99% |
| 16 | 37515ad8 | 113.5563 | -0.0000% | REJECTED | 17.99% |
| 17 | a54055ce | 5416.5582 | 0.0000% | REJECTED | 17.99% |
| 18 | bd9dfa7b | 2.6341 | N/A | SKIPPED_LOW_ERROR | 17.99% |
| 19 | 444761fb | 18.8979 | -0.0000% | REJECTED | 17.99% |
| 20 | b149ff28 | 0.3955 | N/A | SKIPPED_LOW_ERROR | 17.99% |
| 21 | 3c6d8006 | 1.7696 | N/A | SKIPPED_LOW_ERROR | 17.99% |
| 22 | 12e6457c | 0.6430 | N/A | SKIPPED_LOW_ERROR | 17.99% |
| 23 | 4db07220 | 4.9895 | -0.0000% | REJECTED | 17.99% |
| 24 | 9d0e407c | 1.9789 | N/A | SKIPPED_LOW_ERROR | 17.99% |
| 25 | 545b5e57 | 104.2271 | -0.0000% | REJECTED | 17.99% |
| 26 | ec92bdaa | 9.3291 | -0.0000% | REJECTED | 17.99% |
| 27 | 53f9aa07 | 0.3955 | N/A | SKIPPED_LOW_ERROR | 17.99% |
| 28 | 440e6274 | 4.9895 | -0.0000% | REJECTED | 17.99% |
| 29 | 314469b0 | 11.9093 | 0.0000% | REJECTED | 17.99% |
| 30 | f4603221 | 4.9895 | -0.0000% | REJECTED | 17.99% |
| 31 | 5bfce159 | 1.5619 | N/A | SKIPPED_LOW_ERROR | 17.99% |
| 32 | e1d7e5b4 | 5.5387 | -0.0000% | REJECTED | 17.99% |
| 33 | 54cb7f90 | 11.9093 | 0.0000% | REJECTED | 17.99% |
| 34 | 3d4c3db9 | 4.9895 | -0.0000% | REJECTED | 17.99% |
| 35 | ef93d4fc | 1.5619 | N/A | SKIPPED_LOW_ERROR | 17.99% |
| 36 | c302739b | 5.5387 | -0.0000% | REJECTED | 17.99% |
| 37 | 9ce781b0 | 4.9895 | -0.0000% | REJECTED | 17.99% |
| 38 | 5ae97df8 | 1.5619 | N/A | SKIPPED_LOW_ERROR | 17.99% |
| 39 | a95bee4e | 4.9895 | -0.0000% | REJECTED | 17.99% |
## Query Tree

```
Node 15317 (Aggregate) - ROOT
  Node 15318 (Gather Merge)
    Node 15319 (Sort)
      Node 15320 (Hash Join)
        Node 15321 (Nested Loop)
          Node 15322 (Hash Join)
            Node 15323 (Nested Loop)
              Node 15324 (Hash Join)
                Node 15325 (Seq Scan) - LEAF
                Node 15326 (Hash)
                  Node 15327 (Hash Join)
                    Node 15328 (Seq Scan) - LEAF
                    Node 15329 (Hash)
                      Node 15330 (Hash Join)
                        Node 15331 (Seq Scan) - LEAF
                        Node 15332 (Hash)
                          Node 15333 (Seq Scan) - LEAF
              Node 15334 (Index Scan) - LEAF
            Node 15335 (Hash)
              Node 15336 (Seq Scan) - LEAF
          Node 15337 (Index Scan) - LEAF
        Node 15338 (Hash)
          Node 15339 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 3.43%
- Improvement: 1.47%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 15317 | Aggregate | 1238.26 | 1195.83 | 3.4% | operator |
| 15318 | Gather Merge | 1237.88 | 1097.17 | 11.4% | operator |
| 15319 | Sort | 1233.26 | 1046.21 | 15.2% | operator |
| 15320 | Hash Join | 1232.99 | 785.61 | 36.3% | operator |
| 15321 | Nested Loop | 1232.65 | 1198.29 | 2.8% | operator |
| 15338 | Hash | 0.02 | 13.72 | 76144.9% | operator |
| 15322 | Hash Join | 1228.80 | 785.60 | 36.1% | operator |
| 15337 | Index Scan | 0.01 | 12.42 | 206958.1% | operator |
| 15339 | Seq Scan | 0.01 | 6.51 | 49992.0% | operator |
| 15323 | Nested Loop | 1184.68 | 1198.29 | 1.1% | operator |
| 15335 | Hash | 39.31 | 19.97 | 49.2% | operator |
| 15324 | Hash Join | 218.71 | 251.17 | 14.8% | operator |
| 15334 | Index Scan | 0.04 | 2.88 | 6926.5% | operator |
| 15336 | Seq Scan | 39.18 | 48.88 | 24.7% | operator |
| 15325 | Seq Scan | 160.82 | 159.67 | 0.7% | operator |
| 15326 | Hash | 38.60 | 20.62 | 46.6% | operator |
| 15327 | Hash Join | 38.02 | 132.26 | 247.9% | operator |
| 15328 | Seq Scan | 36.54 | 23.03 | 37.0% | operator |
| 15329 | Hash | 0.13 | 23.66 | 17686.6% | operator |
| 15330 | Hash Join | 0.13 | 306.84 | 237757.3% | operator |
| 15331 | Seq Scan | 0.01 | 12.22 | 122149.4% | operator |
| 15332 | Hash | 0.11 | 18.14 | 15956.8% | operator |
| 15333 | Seq Scan | 0.11 | 23.36 | 21138.4% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 15333 (Seq Scan) - LEAF

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
- **Output:** st=0.26, rt=23.36

### Step 2: Node 15331 (Seq Scan) - LEAF

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
- **Output:** st=0.05, rt=12.22

### Step 3: Node 15332 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=1
  - nt1=1
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=23.3622
  - rt2=0.0000
  - sel=1.0000
  - st1=0.2635
  - st2=0.0000
  - startup_cost=1.0600
  - total_cost=1.0600
- **Output:** st=18.14, rt=18.14

### Step 4: Node 15330 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=25
  - nt2=1
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=12.2249
  - rt2=18.1441
  - sel=0.2000
  - st1=0.0533
  - st2=18.1442
  - startup_cost=1.0700
  - total_cost=2.4000
- **Output:** st=13.03, rt=306.84

### Step 5: Node 15328 (Seq Scan) - LEAF

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
- **Output:** st=0.31, rt=23.03

### Step 6: Node 15329 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=5
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=306.8360
  - rt2=0.0000
  - sel=1.0000
  - st1=13.0350
  - st2=0.0000
  - startup_cost=2.4000
  - total_cost=2.4000
- **Output:** st=23.66, rt=23.66

### Step 7: Node 15327 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=12500
  - nt1=62500
  - nt2=5
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=23.0305
  - rt2=23.6561
  - sel=0.0400
  - st1=0.3131
  - st2=23.6563
  - startup_cost=2.4600
  - total_cost=4586.8400
- **Output:** st=6.81, rt=132.26

### Step 8: Node 15325 (Seq Scan) - LEAF

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
- **Output:** st=0.26, rt=159.67

### Step 9: Node 15326 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=12500
  - nt1=12500
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=132.2606
  - rt2=0.0000
  - sel=1.0000
  - st1=6.8054
  - st2=0.0000
  - startup_cost=4586.8400
  - total_cost=4586.8400
- **Output:** st=20.62, rt=20.62

### Step 10: Node 15324 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=29497
  - nt1=147487
  - nt2=12500
  - parallel_workers=0
  - plan_width=8
  - reltuples=0.0000
  - rt1=159.6655
  - rt2=20.6155
  - sel=0.0000
  - st1=0.2557
  - st2=20.6159
  - startup_cost=4743.0900
  - total_cost=38813.1400
- **Output:** st=26.05, rt=251.17

### Step 11: Node 15334 (Index Scan) - LEAF

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
- **Output:** st=0.03, rt=2.88

### Step 12: Node 15336 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=548
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0027
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=1.66, rt=48.88

### Step 13: Node 15323 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=118013
  - nt1=29497
  - nt2=5
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=251.1695
  - rt2=2.8809
  - sel=0.8002
  - st1=26.0452
  - st2=0.0327
  - startup_cost=4743.5200
  - total_cost=64785.2000
- **Output:** st=186.04, rt=1198.29

### Step 14: Node 15335 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=548
  - nt1=548
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=48.8764
  - rt2=0.0000
  - sel=1.0000
  - st1=1.6588
  - st2=0.0000
  - startup_cost=5169.6700
  - total_cost=5169.6700
- **Output:** st=19.97, rt=19.97

### Step 15: Node 15322 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=776
  - nt1=118013
  - nt2=548
  - parallel_workers=0
  - plan_width=20
  - reltuples=0.0000
  - rt1=1198.2891
  - rt2=19.9704
  - sel=0.0000
  - st1=186.0414
  - st2=19.9705
  - startup_cost=9920.0400
  - total_cost=70271.5200
- **Output:** st=113.62, rt=785.60

### Step 16: Node 15337 (Index Scan) - LEAF

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
- **Output:** st=0.16, rt=12.42

### Step 17: Node 15339 (Seq Scan) - LEAF

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
- **Output:** st=0.16, rt=6.51

### Step 18: Node 15321 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=776
  - nt1=776
  - nt2=1
  - parallel_workers=0
  - plan_width=20
  - reltuples=0.0000
  - rt1=785.6048
  - rt2=12.4235
  - sel=1.0000
  - st1=113.6216
  - st2=0.1628
  - startup_cost=9920.3200
  - total_cost=70506.2900
- **Output:** st=186.04, rt=1198.29

### Step 19: Node 15338 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=25
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=6.5120
  - rt2=0.0000
  - sel=1.0000
  - st1=0.1624
  - st2=0.0000
  - startup_cost=1.2500
  - total_cost=1.2500
- **Output:** st=13.72, rt=13.72

### Step 20: Node 15320 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=776
  - nt1=776
  - nt2=25
  - parallel_workers=0
  - plan_width=148
  - reltuples=0.0000
  - rt1=1198.2891
  - rt2=13.7241
  - sel=0.0400
  - st1=186.0414
  - st2=13.7224
  - startup_cost=9921.8900
  - total_cost=70512.1800
- **Output:** st=113.62, rt=785.61

### Step 21: Node 15319 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=776
  - nt1=776
  - nt2=0
  - parallel_workers=0
  - plan_width=148
  - reltuples=0.0000
  - rt1=785.6126
  - rt2=0.0000
  - sel=1.0000
  - st1=113.6207
  - st2=0.0000
  - startup_cost=70549.4200
  - total_cost=70551.3600
- **Output:** st=1044.94, rt=1046.21

### Step 22: Node 15318 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2405
  - nt1=776
  - nt2=0
  - parallel_workers=3
  - plan_width=148
  - reltuples=0.0000
  - rt1=1046.2121
  - rt2=0.0000
  - sel=3.0992
  - st1=1044.9422
  - st2=0.0000
  - startup_cost=71549.4600
  - total_cost=71833.9900
- **Output:** st=1093.46, rt=1097.17

### Step 23: Node 15317 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2405
  - nt1=2405
  - nt2=0
  - parallel_workers=0
  - plan_width=64
  - reltuples=0.0000
  - rt1=1097.1703
  - rt2=0.0000
  - sel=1.0000
  - st1=1093.4632
  - st2=0.0000
  - startup_cost=71549.4600
  - total_cost=71930.1900
- **Output:** st=1164.33, rt=1195.83
