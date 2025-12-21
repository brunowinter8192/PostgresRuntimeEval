# Online Prediction Report

**Test Query:** Q7_92_seed_746566821
**Timestamp:** 2025-12-21 22:56:36

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 0.86%

## Phase C: Patterns in Query

- Total Patterns: 44

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 96 | 4.7% | 4.4662 |
| b149ff28 | Aggregate -> Gather Merge -> Sort -> Has... | 4 | 48 | 2.2% | 1.0579 |
| 53f9aa07 | Aggregate -> Gather Merge -> Sort -> Has... | 5 | 48 | 2.2% | 1.0579 |
| 27c3eea9 | Aggregate -> Gather Merge -> Sort -> Has... | 6 | 24 | 1.2% | 0.2928 |
| e8907654 | Aggregate -> Gather Merge -> Sort -> Has... | 7 | 24 | 1.2% | 0.2928 |
| c83209ef | Aggregate -> Gather Merge -> Sort -> Has... | 8 | 24 | 1.2% | 0.2928 |
| 9d0b7ec3 | Aggregate -> Gather Merge -> Sort -> Has... | 9 | 24 | 1.2% | 0.2928 |
| e7dc2e6a | Aggregate -> Gather Merge -> Sort -> Has... | 10 | 24 | 1.2% | 0.2928 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 96 | 7.6% | 7.3257 |
| 98d4ff98 | Gather Merge -> Sort -> Hash Join (Outer... | 3 | 48 | 6.2% | 2.9727 |
| 3c6d8006 | Gather Merge -> Sort -> Hash Join -> [Ne... | 4 | 48 | 6.2% | 2.9727 |
| 814388b1 | Gather Merge -> Sort -> Hash Join -> [Ne... | 5 | 24 | 4.5% | 1.0842 |
| 34811571 | Gather Merge -> Sort -> Hash Join -> [Ne... | 6 | 24 | 4.5% | 1.0842 |
| 3d2df434 | Gather Merge -> Sort -> Hash Join -> [Ne... | 7 | 24 | 4.5% | 1.0842 |
| 991242c7 | Gather Merge -> Sort -> Hash Join -> [Ne... | 8 | 24 | 4.5% | 1.0842 |
| 1ec32e3e | Gather Merge -> Sort -> Hash Join -> [Ne... | 9 | 24 | 4.5% | 1.0842 |
| 3e2d5a00 | Sort -> Hash Join (Outer) | 2 | 96 | 19.3% | 18.5586 |
| 91d6e559 | Sort -> Hash Join -> [Nested Loop (Outer... | 3 | 72 | 5.4% | 3.8546 |
| 94a6aee0 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 4 | 24 | 4.0% | 0.9537 |
| 6b43f5a7 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 5 | 24 | 4.0% | 0.9537 |
| cfb66570 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 6 | 24 | 4.0% | 0.9537 |
| f5c4d937 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 7 | 24 | 4.0% | 0.9537 |
| bdf0194d | Sort -> Hash Join -> [Nested Loop -> [Ha... | 8 | 24 | 4.0% | 0.9537 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 75.1% | 108.1438 |
| 1e7829bf | Hash Join -> [Nested Loop -> [Hash Join ... | 3 | 24 | 10.7% | 2.5679 |
| 88cd04f5 | Hash Join -> [Nested Loop -> [Hash Join ... | 4 | 24 | 10.7% | 2.5679 |
| 2dab5c22 | Hash Join -> [Nested Loop -> [Hash Join ... | 5 | 24 | 10.7% | 2.5679 |
| 66a98304 | Hash Join -> [Nested Loop -> [Hash Join ... | 6 | 24 | 10.7% | 2.5679 |
| 759d57a4 | Hash Join -> [Nested Loop -> [Hash Join ... | 7 | 24 | 10.7% | 2.5679 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 140 | 4.5% | 6.2375 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 116 | 3.5% | 4.0772 |
| bd9dfa7b | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 92 | 3.7% | 3.3601 |
| 9d0e407c | Nested Loop -> [Hash Join -> [Seq Scan (... | 5 | 72 | 4.1% | 2.9587 |
| 68382c9c | Nested Loop -> [Hash Join -> [Seq Scan (... | 6 | 24 | 3.4% | 0.8246 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 148 | 116.8% | 172.9284 |
| 37515ad8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 124 | 135.7% | 168.3286 |
| 545b5e57 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 72 | 212.7% | 153.1732 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 172 | 3565.0% | 6131.8766 |
| c0a8d3de | Hash -> Hash Join -> [Seq Scan (Outer), ... | 3 | 148 | 4130.8% | 6113.5159 |
| a54055ce | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 96 | 6342.9% | 6089.1983 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 168 | 44967.0% | 75544.5822 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 33781.0% | 113504.2307 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 1 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 2 | 7df893ad | 6131.8766 | -0.0000% | REJECTED | 17.92% |
| 3 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 4 | 2e0f44ef | 108.1438 | 0.0001% | REJECTED | 17.92% |
| 5 | 3cfa90d7 | 6.2375 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 6 | 1691f6f0 | 7.3257 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 7 | 3e2d5a00 | 18.5586 | 0.0007% | REJECTED | 17.92% |
| 8 | f4cb205a | 75544.5822 | 0.0006% | REJECTED | 17.92% |
| 9 | bb930825 | 172.9284 | -0.0000% | REJECTED | 17.92% |
| 10 | c0a8d3de | 6113.5159 | -0.0000% | REJECTED | 17.92% |
| 11 | e0e3c3e1 | 4.0772 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 12 | 29ee00db | 4.4662 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 13 | 91d6e559 | 3.8546 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 14 | 98d4ff98 | 2.9727 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 15 | 1e7829bf | 2.5679 | 0.0000% | REJECTED | 17.92% |
| 16 | 37515ad8 | 168.3286 | -0.0000% | REJECTED | 17.92% |
| 17 | a54055ce | 6089.1983 | -0.0000% | REJECTED | 17.92% |
| 18 | bd9dfa7b | 3.3601 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 19 | b149ff28 | 1.0579 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 20 | 3c6d8006 | 2.9727 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 21 | 94a6aee0 | 0.9537 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 22 | 88cd04f5 | 2.5679 | 0.0000% | REJECTED | 17.92% |
| 23 | 9d0e407c | 2.9587 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 24 | 545b5e57 | 153.1732 | -0.0000% | REJECTED | 17.92% |
| 25 | 53f9aa07 | 1.0579 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 26 | 814388b1 | 1.0842 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 27 | 6b43f5a7 | 0.9537 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 28 | 2dab5c22 | 2.5679 | 0.0000% | REJECTED | 17.92% |
| 29 | 27c3eea9 | 0.2928 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 30 | 34811571 | 1.0842 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 31 | cfb66570 | 0.9537 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 32 | 66a98304 | 2.5679 | 0.0000% | REJECTED | 17.92% |
| 33 | 68382c9c | 0.8246 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 34 | e8907654 | 0.2928 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 35 | 3d2df434 | 1.0842 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 36 | f5c4d937 | 0.9537 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 37 | 759d57a4 | 2.5679 | 0.0000% | REJECTED | 17.92% |
| 38 | c83209ef | 0.2928 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 39 | 991242c7 | 1.0842 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 40 | bdf0194d | 0.9537 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 41 | 9d0b7ec3 | 0.2928 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 42 | 1ec32e3e | 1.0842 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 43 | e7dc2e6a | 0.2928 | N/A | SKIPPED_LOW_ERROR | 17.92% |
## Query Tree

```
Node 13039 (Aggregate) - ROOT
  Node 13040 (Gather Merge)
    Node 13041 (Sort)
      Node 13042 (Hash Join)
        Node 13043 (Nested Loop)
          Node 13044 (Hash Join)
            Node 13045 (Seq Scan) - LEAF
            Node 13046 (Hash)
              Node 13047 (Hash Join)
                Node 13048 (Seq Scan) - LEAF
                Node 13049 (Hash)
                  Node 13050 (Seq Scan) - LEAF
          Node 13051 (Index Scan) - LEAF
        Node 13052 (Hash)
          Node 13053 (Hash Join)
            Node 13054 (Seq Scan) - LEAF
            Node 13055 (Hash)
              Node 13056 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 0.21%
- Improvement: 0.66%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 13039 | Aggregate | 1204.69 | 1202.22 | 0.2% | operator |
| 13040 | Gather Merge | 1203.73 | 1148.45 | 4.6% | operator |
| 13041 | Sort | 1198.42 | 1149.87 | 4.1% | operator |
| 13042 | Hash Join | 1197.85 | 1130.50 | 5.6% | operator |
| 13043 | Nested Loop | 1190.02 | 1145.81 | 3.7% | operator |
| 13052 | Hash | 4.13 | 15.44 | 273.7% | operator |
| 13044 | Hash Join | 216.20 | 319.53 | 47.8% | operator |
| 13051 | Index Scan | 0.03 | 0.09 | 163.5% | operator |
| 13053 | Hash Join | 4.08 | 49.64 | 1115.7% | operator |
| 13045 | Seq Scan | 152.35 | 192.19 | 26.2% | operator |
| 13046 | Hash | 38.70 | 17.27 | 55.4% | operator |
| 13054 | Seq Scan | 3.77 | 10.62 | 181.3% | operator |
| 13055 | Hash | 0.02 | 14.54 | 76411.4% | operator |
| 13047 | Hash Join | 38.41 | 54.15 | 41.0% | operator |
| 13056 | Seq Scan | 0.01 | 7.20 | 51299.6% | operator |
| 13048 | Seq Scan | 37.31 | 24.87 | 33.3% | operator |
| 13049 | Hash | 0.01 | 14.54 | 132056.0% | operator |
| 13050 | Seq Scan | 0.01 | 7.20 | 89849.3% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 13050 (Seq Scan) - LEAF

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
- **Output:** st=0.06, rt=7.20

### Step 2: Node 13048 (Seq Scan) - LEAF

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

### Step 3: Node 13049 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2
  - nt1=2
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=7.1959
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0575
  - st2=0.0000
  - startup_cost=1.3800
  - total_cost=1.3800
- **Output:** st=14.54, rt=14.54

### Step 4: Node 13047 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5000
  - nt1=62500
  - nt2=2
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=24.8735
  - rt2=14.5372
  - sel=0.0400
  - st1=0.2761
  - st2=14.5368
  - startup_cost=1.4000
  - total_cost=4418.2700
- **Output:** st=1.57, rt=54.15

### Step 5: Node 13056 (Seq Scan) - LEAF

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
- **Output:** st=0.06, rt=7.20

### Step 6: Node 13045 (Seq Scan) - LEAF

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
- **Output:** st=0.17, rt=192.19

### Step 7: Node 13046 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5000
  - nt1=5000
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=54.1481
  - rt2=0.0000
  - sel=1.0000
  - st1=1.5683
  - st2=0.0000
  - startup_cost=4418.2700
  - total_cost=4418.2700
- **Output:** st=17.27, rt=17.27

### Step 8: Node 13054 (Seq Scan) - LEAF

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

### Step 9: Node 13055 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2
  - nt1=2
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=7.1959
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0575
  - st2=0.0000
  - startup_cost=1.3800
  - total_cost=1.3800
- **Output:** st=14.54, rt=14.54

### Step 10: Node 13044 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=38710
  - nt1=483871
  - nt2=5000
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=192.1919
  - rt2=17.2659
  - sel=0.0000
  - st1=0.1717
  - st2=17.2655
  - startup_cost=4480.7700
  - total_cost=37431.2900
- **Output:** st=41.57, rt=319.53

### Step 11: Node 13051 (Index Scan) - LEAF

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
- **Output:** st=0.04, rt=0.09

### Step 12: Node 13053 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=800
  - nt1=10000
  - nt2=2
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=10.6168
  - rt2=14.5372
  - sel=0.0400
  - st1=0.0355
  - st2=14.5368
  - startup_cost=1.4000
  - total_cost=355.1000
- **Output:** st=1.99, rt=49.64

### Step 13: Node 13043 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=47115
  - nt1=38710
  - nt2=1
  - parallel_workers=0
  - plan_width=124
  - reltuples=0.0000
  - rt1=319.5259
  - rt2=0.0870
  - sel=1.2171
  - st1=41.5708
  - st2=0.0386
  - startup_cost=4481.2100
  - total_cost=62578.9300
- **Output:** st=43.62, rt=1145.81

### Step 14: Node 13052 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=800
  - nt1=800
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=49.6383
  - rt2=0.0000
  - sel=1.0000
  - st1=1.9885
  - st2=0.0000
  - startup_cost=355.1000
  - total_cost=355.1000
- **Output:** st=15.44, rt=15.44

### Step 15: Node 13042 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=1961
  - nt1=47115
  - nt2=800
  - parallel_workers=0
  - plan_width=252
  - reltuples=0.0000
  - rt1=1145.8080
  - rt2=15.4365
  - sel=0.0001
  - st1=43.6201
  - st2=15.4361
  - startup_cost=4846.3100
  - total_cost=63200.9900
- **Output:** st=43.99, rt=1130.50

### Step 16: Node 13041 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=1961
  - nt1=1961
  - nt2=0
  - parallel_workers=0
  - plan_width=252
  - reltuples=0.0000
  - rt1=1130.4961
  - rt2=0.0000
  - sel=1.0000
  - st1=43.9923
  - st2=0.0000
  - startup_cost=63308.2300
  - total_cost=63313.1300
- **Output:** st=1149.28, rt=1149.87

### Step 17: Node 13040 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6078
  - nt1=1961
  - nt2=0
  - parallel_workers=3
  - plan_width=252
  - reltuples=0.0000
  - rt1=1149.8739
  - rt2=0.0000
  - sel=3.0994
  - st1=1149.2783
  - st2=0.0000
  - startup_cost=64308.2700
  - total_cost=65027.3400
- **Output:** st=1145.38, rt=1148.45

### Step 18: Node 13039 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6078
  - nt1=6078
  - nt2=0
  - parallel_workers=0
  - plan_width=272
  - reltuples=0.0000
  - rt1=1148.4451
  - rt2=0.0000
  - sel=1.0000
  - st1=1145.3760
  - st2=0.0000
  - startup_cost=64308.2700
  - total_cost=65209.6800
- **Output:** st=1174.30, rt=1202.22
