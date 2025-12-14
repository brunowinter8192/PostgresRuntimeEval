# Online Prediction Report

**Test Query:** Q7_127_seed_1033707906
**Timestamp:** 2025-12-13 04:05:16

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 1.51%

## Phase C: Patterns in Query

- Total Patterns: 44

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
| 18 | 545b5e57 | 153.1732 | -0.0000% | REJECTED | 17.92% |
| 23 | 1e7829bf | 2.5679 | 0.0000% | REJECTED | 17.92% |
| 25 | 88cd04f5 | 2.5679 | 0.0000% | REJECTED | 17.92% |
| 28 | 2dab5c22 | 2.5679 | 0.0000% | REJECTED | 17.92% |
| 32 | 66a98304 | 2.5679 | 0.0000% | REJECTED | 17.92% |
| 37 | 759d57a4 | 2.5679 | 0.0000% | REJECTED | 17.92% |
## Query Tree

```
Node 11023 (Aggregate) - ROOT
  Node 11024 (Gather Merge)
    Node 11025 (Sort)
      Node 11026 (Hash Join)
        Node 11027 (Nested Loop)
          Node 11028 (Hash Join)
            Node 11029 (Seq Scan) - LEAF
            Node 11030 (Hash)
              Node 11031 (Hash Join)
                Node 11032 (Seq Scan) - LEAF
                Node 11033 (Hash)
                  Node 11034 (Seq Scan) - LEAF
          Node 11035 (Index Scan) - LEAF
        Node 11036 (Hash)
          Node 11037 (Hash Join)
            Node 11038 (Seq Scan) - LEAF
            Node 11039 (Hash)
              Node 11040 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 0.86%
- Improvement: 0.65%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 11023 | Aggregate | 1212.60 | 1202.22 | 0.9% | operator |
| 11024 | Gather Merge | 1211.49 | 1148.45 | 5.2% | operator |
| 11025 | Sort | 1205.76 | 1149.87 | 4.6% | operator |
| 11026 | Hash Join | 1205.13 | 1130.50 | 6.2% | operator |
| 11027 | Nested Loop | 1197.82 | 1145.81 | 4.3% | operator |
| 11036 | Hash | 3.66 | 15.44 | 321.9% | operator |
| 11028 | Hash Join | 215.88 | 319.53 | 48.0% | operator |
| 11035 | Index Scan | 0.03 | 0.09 | 163.5% | operator |
| 11037 | Hash Join | 3.61 | 49.64 | 1275.4% | operator |
| 11029 | Seq Scan | 155.88 | 192.19 | 23.3% | operator |
| 11030 | Hash | 35.02 | 17.27 | 50.7% | operator |
| 11038 | Seq Scan | 3.27 | 10.62 | 224.3% | operator |
| 11039 | Hash | 0.01 | 14.54 | 103736.9% | operator |
| 11031 | Hash Join | 34.76 | 54.15 | 55.8% | operator |
| 11040 | Seq Scan | 0.01 | 7.20 | 71859.5% | operator |
| 11032 | Seq Scan | 33.66 | 24.87 | 26.1% | operator |
| 11033 | Hash | 0.01 | 14.54 | 161424.0% | operator |
| 11034 | Seq Scan | 0.01 | 7.20 | 119832.4% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 11034 (Seq Scan) - LEAF

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

### Step 2: Node 11032 (Seq Scan) - LEAF

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

### Step 3: Node 11033 (Hash)

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

### Step 4: Node 11031 (Hash Join)

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

### Step 5: Node 11040 (Seq Scan) - LEAF

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

### Step 6: Node 11029 (Seq Scan) - LEAF

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

### Step 7: Node 11030 (Hash)

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

### Step 8: Node 11038 (Seq Scan) - LEAF

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

### Step 9: Node 11039 (Hash)

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

### Step 10: Node 11028 (Hash Join)

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

### Step 11: Node 11035 (Index Scan) - LEAF

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

### Step 12: Node 11037 (Hash Join)

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

### Step 13: Node 11027 (Nested Loop)

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

### Step 14: Node 11036 (Hash)

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

### Step 15: Node 11026 (Hash Join)

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

### Step 16: Node 11025 (Sort)

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

### Step 17: Node 11024 (Gather Merge)

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

### Step 18: Node 11023 (Aggregate) - ROOT

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
