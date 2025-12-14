# Online Prediction Report

**Test Query:** Q9_26_seed_205100775
**Timestamp:** 2025-12-13 03:17:47

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 9.68%

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
Node 17883 (Sort) - ROOT
  Node 17884 (Aggregate) [PATTERN: a5f39f08]
    Node 17885 (Gather) [consumed]
      Node 17886 (Aggregate) [consumed]
        Node 17887 (Nested Loop)
          Node 17888 (Hash Join)
            Node 17889 (Seq Scan) - LEAF
            Node 17890 (Hash)
              Node 17891 (Hash Join)
                Node 17892 (Hash Join)
                  Node 17893 (Nested Loop)
                    Node 17894 (Seq Scan) - LEAF
                    Node 17895 (Index Scan) - LEAF
                  Node 17896 (Hash)
                    Node 17897 (Seq Scan) - LEAF
                Node 17898 (Hash)
                  Node 17899 (Seq Scan) - LEAF
          Node 17900 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | a5f39f08 | 17884 | 17885, 17886 |


## Phase E: Final Prediction

- Final MRE: 8.56%
- Improvement: 1.12%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 17883 | Sort | 1259.70 | 1151.86 | 8.6% | operator |
| 17884 | Aggregate | 1259.57 | 1113.60 | 11.6% | pattern |
| 17887 | Nested Loop | 1214.62 | 1185.17 | 2.4% | operator |
| 17888 | Hash Join | 1043.47 | 831.84 | 20.3% | operator |
| 17900 | Index Scan | 0.00 | -0.04 | 1512.7% | operator |
| 17889 | Seq Scan | 755.05 | 565.06 | 25.2% | operator |
| 17890 | Hash | 190.30 | 52.62 | 72.3% | operator |
| 17891 | Hash Join | 188.01 | 912.64 | 385.4% | operator |
| 17892 | Hash Join | 174.33 | 851.75 | 388.6% | operator |
| 17898 | Hash | 13.05 | 14.54 | 11.4% | operator |
| 17893 | Nested Loop | 166.78 | 1066.71 | 539.6% | operator |
| 17896 | Hash | 5.42 | 14.79 | 172.7% | operator |
| 17899 | Seq Scan | 13.04 | 7.19 | 44.8% | operator |
| 17894 | Seq Scan | 19.85 | 42.74 | 115.3% | operator |
| 17895 | Index Scan | 0.08 | 0.12 | 47.1% | operator |
| 17897 | Seq Scan | 4.91 | 10.62 | 116.1% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 17894 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=5010
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0250
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=0.41, rt=42.74

### Step 2: Node 17895 (Index Scan) - LEAF

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
  - total_cost=1.8600
- **Output:** st=0.07, rt=0.12

### Step 3: Node 17897 (Seq Scan) - LEAF

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

### Step 4: Node 17893 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=20040
  - nt1=5010
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=42.7391
  - rt2=0.1192
  - sel=1.0000
  - st1=0.4094
  - st2=0.0716
  - startup_cost=0.4200
  - total_cost=14687.3000
- **Output:** st=3.74, rt=1066.71

### Step 5: Node 17896 (Hash)

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

### Step 6: Node 17899 (Seq Scan) - LEAF

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

### Step 7: Node 17892 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=20040
  - nt1=20040
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1066.7112
  - rt2=14.7884
  - sel=0.0001
  - st1=3.7448
  - st2=14.7887
  - startup_cost=448.4300
  - total_cost=15187.9200
- **Output:** st=52.47, rt=851.75

### Step 8: Node 17898 (Hash)

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

### Step 9: Node 17891 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=20040
  - nt1=20040
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=851.7531
  - rt2=14.5397
  - sel=0.0400
  - st1=52.4703
  - st2=14.5393
  - startup_cost=449.9900
  - total_cost=15251.0100
- **Output:** st=40.51, rt=912.64

### Step 10: Node 17889 (Seq Scan) - LEAF

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

### Step 11: Node 17890 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=20040
  - nt1=20040
  - nt2=0
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=912.6433
  - rt2=0.0000
  - sel=1.0000
  - st1=40.5095
  - st2=0.0000
  - startup_cost=15251.0100
  - total_cost=15251.0100
- **Output:** st=52.62, rt=52.62

### Step 12: Node 17888 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=72159
  - nt1=1200243
  - nt2=20040
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=565.0624
  - rt2=52.6206
  - sel=0.0000
  - st1=0.9985
  - st2=52.6199
  - startup_cost=15551.6100
  - total_cost=149155.9800
- **Output:** st=168.39, rt=831.84

### Step 13: Node 17900 (Index Scan) - LEAF

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

### Step 14: Node 17887 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=72159
  - nt1=72159
  - nt2=1
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=831.8390
  - rt2=-0.0424
  - sel=1.0000
  - st1=168.3945
  - st2=0.0037
  - startup_cost=15552.0400
  - total_cost=181847.2600
- **Output:** st=136.32, rt=1185.17

### Step 15: Node 17884 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** a5f39f08 (Aggregate -> Gather -> Aggregate (Outer) (Outer))
- **Consumes:** Nodes 17885, 17886
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=60150
  - Aggregate_Outer_nt1=72159
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=168
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.8336
  - Aggregate_Outer_startup_cost=183110.0500
  - Aggregate_Outer_total_cost=184012.3000
  - Aggregate_np=0
  - Aggregate_nt=60150
  - Aggregate_nt1=300750
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=168
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=218094.8000
  - Aggregate_total_cost=218997.0500
  - Gather_Outer_np=0
  - Gather_Outer_nt=300750
  - Gather_Outer_nt1=60150
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=5
  - Gather_Outer_plan_width=168
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=5.0000
  - Gather_Outer_startup_cost=184110.0500
  - Gather_Outer_total_cost=215087.3000
- **Output:** st=1108.12, rt=1113.60

### Step 16: Node 17883 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=60150
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=1113.5975
  - rt2=0.0000
  - sel=1.0000
  - st1=1108.1241
  - st2=0.0000
  - startup_cost=223771.8400
  - total_cost=223922.2100
- **Output:** st=1149.36, rt=1151.86
