# Online Prediction Report

**Test Query:** Q9_22_seed_172284651
**Timestamp:** 2025-12-13 03:17:47

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 4.85%

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
Node 17811 (Sort) - ROOT
  Node 17812 (Aggregate) [PATTERN: a5f39f08]
    Node 17813 (Gather) [consumed]
      Node 17814 (Aggregate) [consumed]
        Node 17815 (Nested Loop)
          Node 17816 (Hash Join)
            Node 17817 (Seq Scan) - LEAF
            Node 17818 (Hash)
              Node 17819 (Hash Join)
                Node 17820 (Hash Join)
                  Node 17821 (Nested Loop)
                    Node 17822 (Seq Scan) - LEAF
                    Node 17823 (Index Scan) - LEAF
                  Node 17824 (Hash)
                    Node 17825 (Seq Scan) - LEAF
                Node 17826 (Hash)
                  Node 17827 (Seq Scan) - LEAF
          Node 17828 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | a5f39f08 | 17812 | 17813, 17814 |


## Phase E: Final Prediction

- Final MRE: 3.75%
- Improvement: 1.10%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 17811 | Sort | 1193.64 | 1148.84 | 3.8% | operator |
| 17812 | Aggregate | 1193.50 | 1109.59 | 7.0% | pattern |
| 17815 | Nested Loop | 1149.80 | 1173.71 | 2.1% | operator |
| 17816 | Hash Join | 979.98 | 830.97 | 15.2% | operator |
| 17828 | Index Scan | 0.00 | -0.04 | 1512.7% | operator |
| 17817 | Seq Scan | 702.61 | 565.06 | 19.6% | operator |
| 17818 | Hash | 182.72 | 51.35 | 71.9% | operator |
| 17819 | Hash Join | 180.60 | 909.48 | 403.6% | operator |
| 17820 | Hash Join | 166.74 | 849.88 | 409.7% | operator |
| 17826 | Hash | 13.24 | 14.54 | 9.8% | operator |
| 17821 | Nested Loop | 160.09 | 1065.81 | 565.7% | operator |
| 17824 | Hash | 4.32 | 14.79 | 242.2% | operator |
| 17827 | Seq Scan | 13.23 | 7.19 | 45.6% | operator |
| 17822 | Seq Scan | 20.48 | 43.18 | 110.9% | operator |
| 17823 | Index Scan | 0.08 | 0.12 | 52.8% | operator |
| 17825 | Seq Scan | 3.70 | 10.62 | 187.2% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 17822 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=3841
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0192
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=0.41, rt=43.18

### Step 2: Node 17823 (Index Scan) - LEAF

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
  - total_cost=2.1600
- **Output:** st=0.07, rt=0.12

### Step 3: Node 17825 (Seq Scan) - LEAF

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

### Step 4: Node 17821 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15363
  - nt1=3841
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=43.1815
  - rt2=0.1192
  - sel=0.9999
  - st1=0.4136
  - st2=0.0716
  - startup_cost=0.4200
  - total_cost=13635.2500
- **Output:** st=3.70, rt=1065.81

### Step 5: Node 17824 (Hash)

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

### Step 6: Node 17827 (Seq Scan) - LEAF

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

### Step 7: Node 17820 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15363
  - nt1=15363
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1065.8057
  - rt2=14.7884
  - sel=0.0001
  - st1=3.6989
  - st2=14.7887
  - startup_cost=448.4300
  - total_cost=14123.6000
- **Output:** st=52.22, rt=849.88

### Step 8: Node 17826 (Hash)

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

### Step 9: Node 17819 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15363
  - nt1=15363
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=849.8782
  - rt2=14.5397
  - sel=0.0400
  - st1=52.2175
  - st2=14.5393
  - startup_cost=449.9900
  - total_cost=14172.3300
- **Output:** st=40.12, rt=909.48

### Step 10: Node 17817 (Seq Scan) - LEAF

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

### Step 11: Node 17818 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15363
  - nt1=15363
  - nt2=0
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=909.4826
  - rt2=0.0000
  - sel=1.0000
  - st1=40.1192
  - st2=0.0000
  - startup_cost=14172.3300
  - total_cost=14172.3300
- **Output:** st=51.35, rt=51.35

### Step 12: Node 17816 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=55319
  - nt1=1200243
  - nt2=15363
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=565.0624
  - rt2=51.3535
  - sel=0.0000
  - st1=0.9985
  - st2=51.3528
  - startup_cost=14402.7800
  - total_cost=148007.1200
- **Output:** st=168.96, rt=830.97

### Step 13: Node 17828 (Index Scan) - LEAF

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

### Step 14: Node 17815 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=55319
  - nt1=55319
  - nt2=1
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=830.9666
  - rt2=-0.0424
  - sel=1.0000
  - st1=168.9557
  - st2=0.0037
  - startup_cost=14403.2000
  - total_cost=173069.1200
- **Output:** st=116.36, rt=1173.71

### Step 15: Node 17812 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** a5f39f08 (Aggregate -> Gather -> Aggregate (Outer) (Outer))
- **Consumes:** Nodes 17813, 17814
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=55319
  - Aggregate_Outer_nt1=55319
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=168
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=174037.2000
  - Aggregate_Outer_total_cost=174866.9900
  - Aggregate_np=0
  - Aggregate_nt=60150
  - Aggregate_nt1=276595
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=168
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2175
  - Aggregate_startup_cost=206292.4400
  - Aggregate_total_cost=207194.6900
  - Gather_Outer_np=0
  - Gather_Outer_nt=276595
  - Gather_Outer_nt1=55319
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=5
  - Gather_Outer_plan_width=168
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=5.0000
  - Gather_Outer_startup_cost=175037.2000
  - Gather_Outer_total_cost=203526.4900
- **Output:** st=1104.10, rt=1109.59

### Step 16: Node 17811 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=60150
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=1109.5854
  - rt2=0.0000
  - sel=1.0000
  - st1=1104.1017
  - st2=0.0000
  - startup_cost=211969.4800
  - total_cost=212119.8500
- **Output:** st=1146.39, rt=1148.84
