# Online Prediction Report

**Test Query:** Q7_74_seed_598894263
**Timestamp:** 2025-12-21 16:18:55

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17291 | Operator + Pattern Training |
| Training_Test | 4328 | Pattern Selection Eval |
| Training | 21619 | Final Model Training |
| Test | 2700 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 2.39%

## Phase C: Patterns in Query

- Total Patterns: 44

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 368 | 27128.1% | 99831.3585 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 360 | 19515.5% | 70255.9551 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 180 | 12.9% | 23.1405 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 158 | 5421.3% | 8565.6070 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 150 | 84.4% | 126.6606 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 142 | 4.1% | 5.7940 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 90 | 9.2% | 8.2533 |
| 3e2d5a00 | Sort -> Hash Join (Outer) | 2 | 90 | 25.2% | 22.7018 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 158 | 165.4% | 261.3404 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 150 | 66363.9% | 99545.8479 |
| c0a8d3de | Hash -> Hash Join -> [Seq Scan (Outer), ... | 3 | 128 | 6674.5% | 8543.4003 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 112 | 2.4% | 2.7134 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 90 | 5.5% | 4.9483 |
| 91d6e559 | Sort -> Hash Join -> [Nested Loop (Outer... | 3 | 60 | 7.1% | 4.2435 |
| 98d4ff98 | Gather Merge -> Sort -> Hash Join (Outer... | 3 | 30 | 8.5% | 2.5384 |
| 37515ad8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 128 | 201.0% | 257.3049 |
| bd9dfa7b | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 82 | 2.5% | 2.0349 |
| a54055ce | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 60 | 14188.5% | 8513.0877 |
| b149ff28 | Aggregate -> Gather Merge -> Sort -> Has... | 4 | 30 | 3.1% | 0.9427 |
| 3c6d8006 | Gather Merge -> Sort -> Hash Join -> [Ne... | 4 | 30 | 8.5% | 2.5384 |
| 9d0e407c | Nested Loop -> [Hash Join -> [Seq Scan (... | 5 | 60 | 2.7% | 1.6049 |
| 545b5e57 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 60 | 383.7% | 230.2087 |
| 53f9aa07 | Aggregate -> Gather Merge -> Sort -> Has... | 5 | 30 | 3.1% | 0.9427 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 99831.3585 | 0.0010% | REJECTED | 18.09% |
| 1 | 3aab37be | 70255.9551 | -0.0000% | REJECTED | 18.09% |
| 2 | 2724c080 | 23.1405 | 0.0057% | REJECTED | 18.09% |
| 3 | 7df893ad | 8565.6070 | -0.0000% | REJECTED | 18.09% |
| 4 | 2e0f44ef | 126.6606 | 0.0001% | REJECTED | 18.09% |
| 5 | 3cfa90d7 | 5.7940 | N/A | SKIPPED_LOW_ERROR | 18.09% |
| 6 | 1691f6f0 | 8.2533 | N/A | SKIPPED_LOW_ERROR | 18.09% |
| 7 | 3e2d5a00 | 22.7018 | 0.0077% | REJECTED | 18.09% |
| 8 | bb930825 | 261.3404 | -0.0000% | REJECTED | 18.09% |
| 9 | f4cb205a | 99545.8479 | 0.0006% | REJECTED | 18.09% |
| 10 | c0a8d3de | 8543.4003 | -0.0000% | REJECTED | 18.09% |
| 11 | e0e3c3e1 | 2.7134 | N/A | SKIPPED_LOW_ERROR | 18.09% |
| 12 | 29ee00db | 4.9483 | N/A | SKIPPED_LOW_ERROR | 18.09% |
| 13 | 91d6e559 | 4.2435 | N/A | SKIPPED_LOW_ERROR | 18.09% |
| 14 | 98d4ff98 | 2.5384 | N/A | SKIPPED_LOW_ERROR | 18.09% |
| 15 | 37515ad8 | 257.3049 | -0.0000% | REJECTED | 18.09% |
| 16 | bd9dfa7b | 2.0349 | N/A | SKIPPED_LOW_ERROR | 18.09% |
| 17 | a54055ce | 8513.0877 | 0.0000% | REJECTED | 18.09% |
| 18 | b149ff28 | 0.9427 | N/A | SKIPPED_LOW_ERROR | 18.09% |
| 19 | 3c6d8006 | 2.5384 | N/A | SKIPPED_LOW_ERROR | 18.09% |
| 20 | 9d0e407c | 1.6049 | N/A | SKIPPED_LOW_ERROR | 18.09% |
| 21 | 545b5e57 | 230.2087 | 0.0000% | REJECTED | 18.09% |
| 22 | 53f9aa07 | 0.9427 | N/A | SKIPPED_LOW_ERROR | 18.09% |
## Query Tree

```
Node 12679 (Aggregate) - ROOT
  Node 12680 (Gather Merge)
    Node 12681 (Sort)
      Node 12682 (Hash Join)
        Node 12683 (Nested Loop)
          Node 12684 (Hash Join)
            Node 12685 (Seq Scan) - LEAF
            Node 12686 (Hash)
              Node 12687 (Hash Join)
                Node 12688 (Seq Scan) - LEAF
                Node 12689 (Hash)
                  Node 12690 (Seq Scan) - LEAF
          Node 12691 (Index Scan) - LEAF
        Node 12692 (Hash)
          Node 12693 (Hash Join)
            Node 12694 (Seq Scan) - LEAF
            Node 12695 (Hash)
              Node 12696 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 3.12%
- Improvement: -0.74%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 12679 | Aggregate | 1172.63 | 1209.26 | 3.1% | operator |
| 12680 | Gather Merge | 1171.49 | 1142.98 | 2.4% | operator |
| 12681 | Sort | 1164.76 | 1109.13 | 4.8% | operator |
| 12682 | Hash Join | 1164.17 | 842.59 | 27.6% | operator |
| 12683 | Nested Loop | 1156.38 | 1216.16 | 5.2% | operator |
| 12692 | Hash | 3.25 | 17.53 | 439.5% | operator |
| 12684 | Hash Join | 213.94 | 384.47 | 79.7% | operator |
| 12691 | Index Scan | 0.03 | 0.96 | 3006.0% | operator |
| 12693 | Hash Join | 3.20 | 85.17 | 2558.4% | operator |
| 12685 | Seq Scan | 149.51 | 201.16 | 34.5% | operator |
| 12686 | Hash | 38.43 | 19.59 | 49.0% | operator |
| 12694 | Seq Scan | 2.87 | 11.47 | 300.2% | operator |
| 12695 | Hash | 0.01 | 16.89 | 112527.2% | operator |
| 12687 | Hash Join | 37.97 | 92.20 | 142.8% | operator |
| 12696 | Seq Scan | 0.01 | 45.79 | 381502.6% | operator |
| 12688 | Seq Scan | 36.80 | 21.86 | 40.6% | operator |
| 12689 | Hash | 0.01 | 16.89 | 168840.8% | operator |
| 12690 | Seq Scan | 0.01 | 45.79 | 654075.9% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 12690 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=1
  - nt=2
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=25.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0800
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=1.3800
- **Output:** st=14.56, rt=45.79

### Step 2: Node 12688 (Seq Scan) - LEAF

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
- **Output:** st=0.40, rt=21.86

### Step 3: Node 12689 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2
  - nt1=2
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=45.7923
  - rt2=0.0000
  - sel=1.0000
  - st1=14.5595
  - st2=0.0000
  - startup_cost=1.3800
  - total_cost=1.3800
- **Output:** st=16.89, rt=16.89

### Step 4: Node 12687 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5000
  - nt1=62500
  - nt2=2
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=21.8565
  - rt2=16.8941
  - sel=0.0400
  - st1=0.3977
  - st2=16.8931
  - startup_cost=1.4000
  - total_cost=4418.2700
- **Output:** st=12.10, rt=92.20

### Step 5: Node 12696 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=1
  - nt=2
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=25.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0800
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=1.3800
- **Output:** st=14.56, rt=45.79

### Step 6: Node 12685 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=483871
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.3226
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=30974.7100
- **Output:** st=-1.48, rt=201.16

### Step 7: Node 12686 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5000
  - nt1=5000
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=92.1996
  - rt2=0.0000
  - sel=1.0000
  - st1=12.0995
  - st2=0.0000
  - startup_cost=4418.2700
  - total_cost=4418.2700
- **Output:** st=19.59, rt=19.59

### Step 8: Node 12694 (Seq Scan) - LEAF

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
- **Output:** st=-0.10, rt=11.47

### Step 9: Node 12695 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2
  - nt1=2
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=45.7923
  - rt2=0.0000
  - sel=1.0000
  - st1=14.5595
  - st2=0.0000
  - startup_cost=1.3800
  - total_cost=1.3800
- **Output:** st=16.89, rt=16.89

### Step 10: Node 12684 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=38710
  - nt1=483871
  - nt2=5000
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=201.1625
  - rt2=19.5923
  - sel=0.0000
  - st1=-1.4824
  - st2=19.5913
  - startup_cost=4480.7700
  - total_cost=37431.2900
- **Output:** st=70.78, rt=384.47

### Step 11: Node 12691 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=1
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
  - total_cost=0.6400
- **Output:** st=0.04, rt=0.96

### Step 12: Node 12693 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=800
  - nt1=10000
  - nt2=2
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=11.4709
  - rt2=16.8941
  - sel=0.0400
  - st1=-0.1013
  - st2=16.8931
  - startup_cost=1.4000
  - total_cost=355.1000
- **Output:** st=9.80, rt=85.17

### Step 13: Node 12683 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=47115
  - nt1=38710
  - nt2=1
  - parallel_workers=0
  - plan_width=124
  - reltuples=0.0000
  - rt1=384.4697
  - rt2=0.9629
  - sel=1.2171
  - st1=70.7814
  - st2=0.0394
  - startup_cost=4481.2100
  - total_cost=62578.9300
- **Output:** st=173.65, rt=1216.16

### Step 14: Node 12692 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=800
  - nt1=800
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=85.1745
  - rt2=0.0000
  - sel=1.0000
  - st1=9.8048
  - st2=0.0000
  - startup_cost=355.1000
  - total_cost=355.1000
- **Output:** st=17.53, rt=17.53

### Step 15: Node 12682 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=1961
  - nt1=47115
  - nt2=800
  - parallel_workers=0
  - plan_width=252
  - reltuples=0.0000
  - rt1=1216.1552
  - rt2=17.5299
  - sel=0.0001
  - st1=173.6470
  - st2=17.5290
  - startup_cost=4846.3100
  - total_cost=63200.9900
- **Output:** st=124.71, rt=842.59

### Step 16: Node 12681 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=1961
  - nt1=1961
  - nt2=0
  - parallel_workers=0
  - plan_width=252
  - reltuples=0.0000
  - rt1=842.5878
  - rt2=0.0000
  - sel=1.0000
  - st1=124.7091
  - st2=0.0000
  - startup_cost=63308.2300
  - total_cost=63313.1300
- **Output:** st=1107.64, rt=1109.13

### Step 17: Node 12680 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6078
  - nt1=1961
  - nt2=0
  - parallel_workers=3
  - plan_width=252
  - reltuples=0.0000
  - rt1=1109.1336
  - rt2=0.0000
  - sel=3.0994
  - st1=1107.6410
  - st2=0.0000
  - startup_cost=64308.2700
  - total_cost=65027.3400
- **Output:** st=1139.67, rt=1142.98

### Step 18: Node 12679 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6078
  - nt1=6078
  - nt2=0
  - parallel_workers=0
  - plan_width=272
  - reltuples=0.0000
  - rt1=1142.9827
  - rt2=0.0000
  - sel=1.0000
  - st1=1139.6711
  - st2=0.0000
  - startup_cost=64308.2700
  - total_cost=65209.6800
- **Output:** st=1156.36, rt=1209.26
