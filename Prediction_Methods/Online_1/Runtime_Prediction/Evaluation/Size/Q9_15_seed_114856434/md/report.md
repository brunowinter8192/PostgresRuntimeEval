# Online Prediction Report

**Test Query:** Q9_15_seed_114856434
**Timestamp:** 2025-12-13 03:17:47

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 4.13%

## Phase C: Patterns in Query

- Total Patterns: 56

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 75736.1626 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 113504.2307 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 26.4017 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 172 | 6131.8766 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 13.3894 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 108.1438 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 140 | 6.2375 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 96 | 7.7175 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 141.6847 |
| 7d4e78be | Hash Join -> [Hash Join (Outer), Hash (I... | 2 | 48 | 89.9904 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 1 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 2 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 3 | 7df893ad | 6131.8766 | -0.0000% | REJECTED | 17.92% |
| 5 | 2e0f44ef | 108.1438 | 0.0001% | REJECTED | 17.92% |
| 8 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.92% |
| 9 | 7d4e78be | 89.9904 | 0.0000% | REJECTED | 17.92% |
| 11 | bb930825 | 172.9284 | -0.0000% | REJECTED | 17.92% |
| 13 | a5f39f08 | 12.4695 | 1.7095% | ACCEPTED | 16.21% |
| 15 | 30d6e09b | 89.9904 | 0.0000% | REJECTED | 16.21% |
| 16 | 2873b8c3 | 94.8003 | 0.0000% | REJECTED | 16.21% |
| 17 | 1a17c7f7 | 18.3606 | N/A | REJECTED | 16.21% |
| 19 | 7a51ce50 | 89.9904 | 0.0000% | REJECTED | 16.21% |
| 21 | e941d0ad | 4.5998 | N/A | REJECTED | 16.21% |
| 22 | fee45978 | 18.3606 | N/A | REJECTED | 16.21% |
| 23 | 0405d50f | 2.3736 | N/A | REJECTED | 16.21% |
| 24 | 49ae7e42 | 4.5998 | N/A | REJECTED | 16.21% |
| 25 | 702e1a46 | 18.3606 | N/A | REJECTED | 16.21% |
| 27 | 6e1ec341 | 2.3736 | N/A | REJECTED | 16.21% |
| 29 | ed7f2e45 | 4.5998 | N/A | REJECTED | 16.21% |
| 31 | 51640d13 | 2.3736 | N/A | REJECTED | 16.21% |
| 34 | 366e9db5 | 2.3736 | N/A | REJECTED | 16.21% |
| 37 | 88dc07c3 | 2.3736 | N/A | REJECTED | 16.21% |
| 39 | c94fcfda | 2.3736 | N/A | REJECTED | 16.21% |
| 41 | 1c7aa67e | 2.3736 | N/A | REJECTED | 16.21% |
## Query Tree

```
Node 17665 (Sort) - ROOT
  Node 17666 (Aggregate) [PATTERN: a5f39f08]
    Node 17667 (Gather) [consumed]
      Node 17668 (Aggregate) [consumed]
        Node 17669 (Nested Loop)
          Node 17670 (Hash Join)
            Node 17671 (Seq Scan) - LEAF
            Node 17672 (Hash)
              Node 17673 (Hash Join)
                Node 17674 (Hash Join)
                  Node 17675 (Nested Loop)
                    Node 17676 (Seq Scan) - LEAF
                    Node 17677 (Index Scan) - LEAF
                  Node 17678 (Hash)
                    Node 17679 (Seq Scan) - LEAF
                Node 17680 (Hash)
                  Node 17681 (Seq Scan) - LEAF
          Node 17682 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | a5f39f08 | 17666 | 17667, 17668 |


## Phase E: Final Prediction

- Final MRE: 2.94%
- Improvement: 1.19%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 17665 | Sort | 1186.48 | 1151.60 | 2.9% | operator |
| 17666 | Aggregate | 1186.35 | 1113.88 | 6.1% | pattern |
| 17669 | Nested Loop | 1138.62 | 1183.53 | 3.9% | operator |
| 17670 | Hash Join | 966.95 | 831.72 | 14.0% | operator |
| 17682 | Index Scan | 0.00 | -0.04 | 1512.7% | operator |
| 17671 | Seq Scan | 695.60 | 565.06 | 18.8% | operator |
| 17672 | Hash | 177.38 | 52.44 | 70.4% | operator |
| 17673 | Hash Join | 175.44 | 912.19 | 419.9% | operator |
| 17674 | Hash Join | 161.53 | 851.47 | 427.1% | operator |
| 17680 | Hash | 13.29 | 14.54 | 9.4% | operator |
| 17675 | Nested Loop | 155.34 | 1066.58 | 586.6% | operator |
| 17678 | Hash | 3.84 | 14.79 | 285.4% | operator |
| 17681 | Seq Scan | 13.28 | 7.19 | 45.8% | operator |
| 17676 | Seq Scan | 20.92 | 42.80 | 104.6% | operator |
| 17677 | Index Scan | 0.07 | 0.12 | 58.9% | operator |
| 17679 | Seq Scan | 3.26 | 10.62 | 226.0% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 17676 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=4843
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0242
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=0.41, rt=42.80

### Step 2: Node 17677 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=17560
  - nt=4
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=14
  - reltuples=800000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.4200
  - total_cost=1.8900
- **Output:** st=0.07, rt=0.12

### Step 3: Node 17679 (Seq Scan) - LEAF

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

### Step 4: Node 17675 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=19372
  - nt1=4843
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=42.8017
  - rt2=0.1192
  - sel=1.0000
  - st1=0.4100
  - st2=0.0716
  - startup_cost=0.4200
  - total_cost=14540.0600
- **Output:** st=3.73, rt=1066.58

### Step 5: Node 17678 (Hash)

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

### Step 6: Node 17681 (Seq Scan) - LEAF

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

### Step 7: Node 17674 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=19372
  - nt1=19372
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1066.5781
  - rt2=14.7884
  - sel=0.0001
  - st1=3.7347
  - st2=14.7887
  - startup_cost=448.4300
  - total_cost=15038.9400
- **Output:** st=52.43, rt=851.47

### Step 8: Node 17680 (Hash)

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

### Step 9: Node 17673 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=19372
  - nt1=19372
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=851.4747
  - rt2=14.5397
  - sel=0.0400
  - st1=52.4342
  - st2=14.5393
  - startup_cost=449.9900
  - total_cost=15099.9700
- **Output:** st=40.45, rt=912.19

### Step 10: Node 17671 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=1200243
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=29
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.2000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=124602.4300
- **Output:** st=1.00, rt=565.06

### Step 11: Node 17672 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=19372
  - nt1=19372
  - nt2=0
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=912.1894
  - rt2=0.0000
  - sel=1.0000
  - st1=40.4531
  - st2=0.0000
  - startup_cost=15099.9700
  - total_cost=15099.9700
- **Output:** st=52.44, rt=52.44

### Step 12: Node 17670 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=69752
  - nt1=1200243
  - nt2=19372
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=565.0624
  - rt2=52.4377
  - sel=0.0000
  - st1=0.9985
  - st2=52.4370
  - startup_cost=15390.5500
  - total_cost=148994.9300
- **Output:** st=168.48, rt=831.72

### Step 13: Node 17682 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=1
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.4300
  - total_cost=0.4500
- **Output:** st=0.00, rt=-0.04

### Step 14: Node 17669 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=69752
  - nt1=69752
  - nt2=1
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=831.7221
  - rt2=-0.0424
  - sel=1.0000
  - st1=168.4805
  - st2=0.0037
  - startup_cost=15390.9800
  - total_cost=180595.7300
- **Output:** st=133.49, rt=1183.53

### Step 15: Node 17666 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** a5f39f08 (Aggregate -> Gather -> Aggregate (Outer) (Outer))
- **Consumes:** Nodes 17667, 17668
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=60150
  - Aggregate_Outer_nt1=69752
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=168
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.8623
  - Aggregate_Outer_startup_cost=181816.3900
  - Aggregate_Outer_total_cost=182718.6400
  - Aggregate_np=0
  - Aggregate_nt=60150
  - Aggregate_nt1=300750
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=168
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=216801.1400
  - Aggregate_total_cost=217703.3900
  - Gather_Outer_np=0
  - Gather_Outer_nt=300750
  - Gather_Outer_nt1=60150
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=5
  - Gather_Outer_plan_width=168
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=5.0000
  - Gather_Outer_startup_cost=182816.3900
  - Gather_Outer_total_cost=213793.6400
- **Output:** st=1108.41, rt=1113.88

### Step 16: Node 17665 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=60150
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=1113.8798
  - rt2=0.0000
  - sel=1.0000
  - st1=1108.4061
  - st2=0.0000
  - startup_cost=222478.1800
  - total_cost=222628.5500
- **Output:** st=1149.11, rt=1151.60
