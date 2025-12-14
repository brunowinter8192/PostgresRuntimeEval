# Online Prediction Report

**Test Query:** Q9_71_seed_574282170
**Timestamp:** 2025-12-13 02:14:19

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 6.41%

## Phase C: Patterns in Query

- Total Patterns: 56

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 113504.2307 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 75736.1626 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 172 | 6131.8766 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 148 | 172.9284 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 141.6847 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 108.1438 |
| 2873b8c3 | Hash Join -> [Nested Loop -> [Seq Scan (... | 3 | 48 | 94.8003 |
| 7d4e78be | Hash Join -> [Hash Join (Outer), Hash (I... | 2 | 48 | 89.9904 |
| 30d6e09b | Hash Join -> [Hash Join -> [Nested Loop ... | 3 | 48 | 89.9904 |
| 7a51ce50 | Hash Join -> [Hash Join -> [Nested Loop ... | 4 | 48 | 89.9904 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 1 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 2 | 7df893ad | 6131.8766 | -0.0000% | REJECTED | 17.92% |
| 3 | bb930825 | 172.9284 | -0.0000% | REJECTED | 17.92% |
| 4 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.92% |
| 5 | 2e0f44ef | 108.1438 | 0.0001% | REJECTED | 17.92% |
| 6 | 2873b8c3 | 94.8003 | 0.0000% | REJECTED | 17.92% |
| 7 | 7d4e78be | 89.9904 | 0.0000% | REJECTED | 17.92% |
| 8 | 30d6e09b | 89.9904 | 0.0000% | REJECTED | 17.92% |
| 9 | 7a51ce50 | 89.9904 | 0.0000% | REJECTED | 17.92% |
| 10 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 11 | 1a17c7f7 | 18.3606 | 0.0000% | REJECTED | 17.92% |
| 12 | fee45978 | 18.3606 | 0.0000% | REJECTED | 17.92% |
| 13 | 702e1a46 | 18.3606 | 0.0000% | REJECTED | 17.92% |
| 15 | a5f39f08 | 12.4695 | 1.7095% | ACCEPTED | 16.21% |
| 17 | 3b447875 | 5.5697 | 0.0002% | REJECTED | 16.21% |
| 18 | e941d0ad | 4.5998 | N/A | REJECTED | 16.21% |
| 19 | 49ae7e42 | 4.5998 | N/A | REJECTED | 16.21% |
| 20 | ed7f2e45 | 4.5998 | N/A | REJECTED | 16.21% |
| 24 | 0405d50f | 2.3736 | N/A | REJECTED | 16.21% |
| 25 | 6e1ec341 | 2.3736 | N/A | REJECTED | 16.21% |
| 26 | 51640d13 | 2.3736 | N/A | REJECTED | 16.21% |
| 27 | 366e9db5 | 2.3736 | N/A | REJECTED | 16.21% |
| 28 | 88dc07c3 | 2.3736 | N/A | REJECTED | 16.21% |
| 29 | c94fcfda | 2.3736 | N/A | REJECTED | 16.21% |
| 30 | 1c7aa67e | 2.3736 | N/A | REJECTED | 16.21% |
## Query Tree

```
Node 18788 (Sort) - ROOT
  Node 18789 (Aggregate) [PATTERN: a5f39f08]
    Node 18790 (Gather) [consumed]
      Node 18791 (Aggregate) [consumed]
        Node 18792 (Nested Loop)
          Node 18793 (Hash Join)
            Node 18794 (Seq Scan) - LEAF
            Node 18795 (Hash)
              Node 18796 (Hash Join)
                Node 18797 (Hash Join)
                  Node 18798 (Nested Loop)
                    Node 18799 (Seq Scan) - LEAF
                    Node 18800 (Index Scan) - LEAF
                  Node 18801 (Hash)
                    Node 18802 (Seq Scan) - LEAF
                Node 18803 (Hash)
                  Node 18804 (Seq Scan) - LEAF
          Node 18805 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | a5f39f08 | 18789 | 18790, 18791 |


## Phase E: Final Prediction

- Final MRE: 5.37%
- Improvement: 1.04%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 18788 | Sort | 1213.12 | 1147.94 | 5.4% | operator |
| 18789 | Aggregate | 1212.99 | 1106.28 | 8.8% | pattern |
| 18792 | Nested Loop | 1169.72 | 1172.12 | 0.2% | operator |
| 18793 | Hash Join | 994.48 | 830.83 | 16.5% | operator |
| 18805 | Index Scan | 0.00 | -0.04 | 1512.7% | operator |
| 18794 | Seq Scan | 709.78 | 565.06 | 20.4% | operator |
| 18795 | Hash | 188.90 | 51.18 | 72.9% | operator |
| 18796 | Hash Join | 186.92 | 909.04 | 386.3% | operator |
| 18797 | Hash Join | 172.87 | 849.64 | 391.5% | operator |
| 18803 | Hash | 13.41 | 14.54 | 8.4% | operator |
| 18798 | Nested Loop | 165.47 | 1065.68 | 544.0% | operator |
| 18801 | Hash | 5.00 | 14.79 | 196.1% | operator |
| 18804 | Seq Scan | 13.40 | 7.19 | 46.3% | operator |
| 18799 | Seq Scan | 20.19 | 43.25 | 114.2% | operator |
| 18800 | Index Scan | 0.08 | 0.12 | 50.9% | operator |
| 18802 | Seq Scan | 4.39 | 10.62 | 141.6% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 18799 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=3674
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0184
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=0.41, rt=43.25

### Step 2: Node 18800 (Index Scan) - LEAF

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
  - total_cost=2.2200
- **Output:** st=0.07, rt=0.12

### Step 3: Node 18802 (Seq Scan) - LEAF

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

### Step 4: Node 18798 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14697
  - nt1=3674
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=43.2456
  - rt2=0.1192
  - sel=1.0001
  - st1=0.4141
  - st2=0.0716
  - startup_cost=0.4200
  - total_cost=13480.1200
- **Output:** st=3.70, rt=1065.68

### Step 5: Node 18801 (Hash)

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

### Step 6: Node 18804 (Seq Scan) - LEAF

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

### Step 7: Node 18797 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14697
  - nt1=14697
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1065.6828
  - rt2=14.7884
  - sel=0.0001
  - st1=3.7002
  - st2=14.7887
  - startup_cost=448.4300
  - total_cost=13966.7100
- **Output:** st=52.18, rt=849.64

### Step 8: Node 18803 (Hash)

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

### Step 9: Node 18796 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14697
  - nt1=14697
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=849.6351
  - rt2=14.5397
  - sel=0.0400
  - st1=52.1813
  - st2=14.5393
  - startup_cost=449.9900
  - total_cost=14013.3900
- **Output:** st=40.06, rt=909.04

### Step 10: Node 18794 (Seq Scan) - LEAF

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

### Step 11: Node 18795 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14697
  - nt1=14697
  - nt2=0
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=909.0401
  - rt2=0.0000
  - sel=1.0000
  - st1=40.0644
  - st2=0.0000
  - startup_cost=14013.3900
  - total_cost=14013.3900
- **Output:** st=51.17, rt=51.18

### Step 12: Node 18793 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=52919
  - nt1=1200243
  - nt2=14697
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=565.0624
  - rt2=51.1754
  - sel=0.0000
  - st1=0.9985
  - st2=51.1747
  - startup_cost=14233.8500
  - total_cost=147838.1900
- **Output:** st=169.03, rt=830.83

### Step 13: Node 18805 (Index Scan) - LEAF

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

### Step 14: Node 18792 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=52919
  - nt1=52919
  - nt2=1
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=830.8315
  - rt2=-0.0424
  - sel=1.0000
  - st1=169.0276
  - st2=0.0037
  - startup_cost=14234.2700
  - total_cost=171812.8800
- **Output:** st=113.55, rt=1172.12

### Step 15: Node 18789 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** a5f39f08 (Aggregate -> Gather -> Aggregate (Outer) (Outer))
- **Consumes:** Nodes 18790, 18791
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=52919
  - Aggregate_Outer_nt1=52919
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=168
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=172738.9600
  - Aggregate_Outer_total_cost=173532.7500
  - Aggregate_np=0
  - Aggregate_nt=60150
  - Aggregate_nt1=264595
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=168
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2273
  - Aggregate_startup_cost=203638.2000
  - Aggregate_total_cost=204540.4500
  - Gather_Outer_np=0
  - Gather_Outer_nt=264595
  - Gather_Outer_nt1=52919
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=5
  - Gather_Outer_plan_width=168
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=5.0000
  - Gather_Outer_startup_cost=173738.9600
  - Gather_Outer_total_cost=200992.2500
- **Output:** st=1100.80, rt=1106.28

### Step 16: Node 18788 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=60150
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=1106.2845
  - rt2=0.0000
  - sel=1.0000
  - st1=1100.7954
  - st2=0.0000
  - startup_cost=209315.2400
  - total_cost=209465.6100
- **Output:** st=1145.50, rt=1147.94
