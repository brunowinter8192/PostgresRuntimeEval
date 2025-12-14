# Online Prediction Report

**Test Query:** Q5_111_seed_902443410
**Timestamp:** 2025-12-13 03:54:40

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 0.55%

## Phase C: Patterns in Query

- Total Patterns: 85

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 75736.1626 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 113504.2307 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 26.4017 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 172 | 6131.8766 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 19.6008 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 168 | 75544.5822 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 148 | 172.9284 |
| c0a8d3de | Hash -> Hash Join -> [Seq Scan (Outer), ... | 3 | 148 | 6113.5159 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 108.1438 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 140 | 6.2375 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 1 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 2 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 3 | 7df893ad | 6131.8766 | -0.0000% | REJECTED | 17.92% |
| 4 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 5 | f4cb205a | 75544.5822 | 0.0006% | REJECTED | 17.92% |
| 6 | bb930825 | 172.9284 | -0.0000% | REJECTED | 17.92% |
| 7 | c0a8d3de | 6113.5159 | -0.0000% | REJECTED | 17.92% |
| 8 | 2e0f44ef | 108.1438 | 0.0001% | REJECTED | 17.92% |
| 10 | 37515ad8 | 168.3286 | -0.0000% | REJECTED | 17.92% |
| 12 | 3e2d5a00 | 18.5586 | 0.0007% | REJECTED | 17.92% |
| 13 | a54055ce | 6089.1983 | -0.0000% | REJECTED | 17.92% |
| 16 | 2422d111 | 10.7757 | 0.0001% | REJECTED | 17.92% |
| 18 | 545b5e57 | 153.1732 | -0.0000% | REJECTED | 17.92% |
| 19 | 444761fb | 24.3176 | -0.0000% | REJECTED | 17.92% |
| 20 | ec92bdaa | 15.1555 | -0.0000% | REJECTED | 17.92% |
| 23 | ddb1e0ca | 13.6847 | -5.3651% | REJECTED | 17.92% |
| 28 | 4db07220 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 29 | 440e6274 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 30 | 314469b0 | 20.7410 | 0.0000% | REJECTED | 17.92% |
| 31 | f4603221 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 33 | e1d7e5b4 | 13.2381 | -0.0000% | REJECTED | 17.92% |
| 34 | 54cb7f90 | 20.7410 | 0.0000% | REJECTED | 17.92% |
| 35 | 3d4c3db9 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 37 | c302739b | 13.2381 | -0.0000% | REJECTED | 17.92% |
| 38 | 9ce781b0 | 5.9049 | 0.0000% | REJECTED | 17.92% |
| 40 | a95bee4e | 5.9049 | 0.0000% | REJECTED | 17.92% |
## Query Tree

```
Node 7141 (Sort) - ROOT
  Node 7142 (Aggregate)
    Node 7143 (Gather Merge)
      Node 7144 (Aggregate)
        Node 7145 (Sort)
          Node 7146 (Hash Join)
            Node 7147 (Nested Loop)
              Node 7148 (Hash Join)
                Node 7149 (Seq Scan) - LEAF
                Node 7150 (Hash)
                  Node 7151 (Hash Join)
                    Node 7152 (Seq Scan) - LEAF
                    Node 7153 (Hash)
                      Node 7154 (Hash Join)
                        Node 7155 (Seq Scan) - LEAF
                        Node 7156 (Hash)
                          Node 7157 (Seq Scan) - LEAF
              Node 7158 (Index Scan) - LEAF
            Node 7159 (Hash)
              Node 7160 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 0.92%
- Improvement: -0.37%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 7141 | Sort | 1114.51 | 1104.24 | 0.9% | operator |
| 7142 | Aggregate | 1114.49 | 1057.92 | 5.1% | operator |
| 7143 | Gather Merge | 1114.49 | 1124.37 | 0.9% | operator |
| 7144 | Aggregate | 1109.87 | 1019.95 | 8.1% | operator |
| 7145 | Sort | 1109.62 | 1074.64 | 3.2% | operator |
| 7146 | Hash Join | 1109.13 | 1106.89 | 0.2% | operator |
| 7147 | Nested Loop | 1097.79 | 1102.57 | 0.4% | operator |
| 7159 | Hash | 3.26 | 14.79 | 354.2% | operator |
| 7148 | Hash Join | 219.83 | 234.18 | 6.5% | operator |
| 7158 | Index Scan | 0.08 | -0.03 | 132.6% | operator |
| 7160 | Seq Scan | 2.45 | 10.62 | 332.8% | operator |
| 7149 | Seq Scan | 175.18 | 161.95 | 7.6% | operator |
| 7150 | Hash | 31.59 | 21.31 | 32.5% | operator |
| 7151 | Hash Join | 30.70 | 62.87 | 104.8% | operator |
| 7152 | Seq Scan | 29.07 | 24.87 | 14.4% | operator |
| 7153 | Hash | 0.27 | 16.80 | 6052.6% | operator |
| 7154 | Hash Join | 0.27 | 142.84 | 53803.4% | operator |
| 7155 | Seq Scan | 0.01 | 10.49 | 80628.7% | operator |
| 7156 | Hash | 0.24 | 16.01 | 6463.5% | operator |
| 7157 | Seq Scan | 0.24 | 21.39 | 8812.5% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 7157 (Seq Scan) - LEAF

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

### Step 2: Node 7155 (Seq Scan) - LEAF

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

### Step 3: Node 7156 (Hash)

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

### Step 4: Node 7154 (Hash Join)

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

### Step 5: Node 7152 (Seq Scan) - LEAF

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

### Step 6: Node 7153 (Hash)

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

### Step 7: Node 7151 (Hash Join)

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

### Step 8: Node 7149 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=73782
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0492
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=33394.0600
- **Output:** st=0.18, rt=161.95

### Step 9: Node 7150 (Hash)

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

### Step 10: Node 7148 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14756
  - nt1=73782
  - nt2=12500
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=161.9494
  - rt2=21.3137
  - sel=0.0000
  - st1=0.1788
  - st2=21.3132
  - startup_cost=4743.0900
  - total_cost=38475.3200
- **Output:** st=24.76, rt=234.18

### Step 11: Node 7158 (Index Scan) - LEAF

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

### Step 12: Node 7160 (Seq Scan) - LEAF

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

### Step 13: Node 7147 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=59037
  - nt1=14756
  - nt2=5
  - parallel_workers=0
  - plan_width=128
  - reltuples=0.0000
  - rt1=234.1843
  - rt2=-0.0251
  - sel=0.8002
  - st1=24.7649
  - st2=0.0674
  - startup_cost=4743.5200
  - total_cost=56044.8800
- **Output:** st=42.56, rt=1102.57

### Step 14: Node 7159 (Hash)

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

### Step 15: Node 7146 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2362
  - nt1=59037
  - nt2=10000
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=1102.5677
  - rt2=14.7884
  - sel=0.0000
  - st1=42.5610
  - st2=14.7887
  - startup_cost=5216.5200
  - total_cost=56827.8200
- **Output:** st=49.44, rt=1106.89

### Step 16: Node 7145 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=2362
  - nt1=2362
  - nt2=0
  - parallel_workers=0
  - plan_width=116
  - reltuples=0.0000
  - rt1=1106.8941
  - rt2=0.0000
  - sel=1.0000
  - st1=49.4411
  - st2=0.0000
  - startup_cost=56960.1600
  - total_cost=56966.0700
- **Output:** st=1073.72, rt=1074.64

### Step 17: Node 7144 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=2362
  - nt2=0
  - parallel_workers=0
  - plan_width=136
  - reltuples=0.0000
  - rt1=1074.6429
  - rt2=0.0000
  - sel=0.0106
  - st1=1073.7204
  - st2=0.0000
  - startup_cost=56960.1600
  - total_cost=56990.0000
- **Output:** st=1017.92, rt=1019.95

### Step 18: Node 7143 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=75
  - nt1=25
  - nt2=0
  - parallel_workers=3
  - plan_width=136
  - reltuples=0.0000
  - rt1=1019.9490
  - rt2=0.0000
  - sel=3.0000
  - st1=1017.9186
  - st2=0.0000
  - startup_cost=57960.2000
  - total_cost=57998.8500
- **Output:** st=1121.35, rt=1124.37

### Step 19: Node 7142 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=75
  - nt2=0
  - parallel_workers=0
  - plan_width=136
  - reltuples=0.0000
  - rt1=1124.3673
  - rt2=0.0000
  - sel=0.3333
  - st1=1121.3491
  - st2=0.0000
  - startup_cost=57960.2000
  - total_cost=57999.7300
- **Output:** st=1074.35, rt=1057.92

### Step 20: Node 7141 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=25
  - nt2=0
  - parallel_workers=0
  - plan_width=136
  - reltuples=0.0000
  - rt1=1057.9185
  - rt2=0.0000
  - sel=1.0000
  - st1=1074.3455
  - st2=0.0000
  - startup_cost=58000.3100
  - total_cost=58000.3700
- **Output:** st=1102.40, rt=1104.24
