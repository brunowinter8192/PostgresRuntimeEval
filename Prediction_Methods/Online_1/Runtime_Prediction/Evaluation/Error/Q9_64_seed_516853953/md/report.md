# Online Prediction Report

**Test Query:** Q9_64_seed_516853953
**Timestamp:** 2025-12-13 02:14:19

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 3.75%

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
Node 18643 (Sort) - ROOT
  Node 18644 (Aggregate) [PATTERN: a5f39f08]
    Node 18645 (Gather) [consumed]
      Node 18646 (Aggregate) [consumed]
        Node 18647 (Nested Loop)
          Node 18648 (Hash Join)
            Node 18649 (Seq Scan) - LEAF
            Node 18650 (Hash)
              Node 18651 (Hash Join)
                Node 18652 (Hash Join)
                  Node 18653 (Nested Loop)
                    Node 18654 (Seq Scan) - LEAF
                    Node 18655 (Index Scan) - LEAF
                  Node 18656 (Hash)
                    Node 18657 (Seq Scan) - LEAF
                Node 18658 (Hash)
                  Node 18659 (Seq Scan) - LEAF
          Node 18660 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | a5f39f08 | 18644 | 18645, 18646 |


## Phase E: Final Prediction

- Final MRE: 2.57%
- Improvement: 1.18%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 18643 | Sort | 1180.81 | 1150.49 | 2.6% | operator |
| 18644 | Aggregate | 1180.68 | 1114.40 | 5.6% | pattern |
| 18647 | Nested Loop | 1133.99 | 1176.96 | 3.8% | operator |
| 18648 | Hash Join | 961.10 | 831.23 | 13.5% | operator |
| 18660 | Index Scan | 0.00 | -0.04 | 1512.7% | operator |
| 18649 | Seq Scan | 693.80 | 565.06 | 18.6% | operator |
| 18650 | Hash | 174.92 | 51.71 | 70.4% | operator |
| 18651 | Hash Join | 172.83 | 910.38 | 426.7% | operator |
| 18652 | Hash Join | 159.30 | 850.40 | 433.8% | operator |
| 18658 | Hash | 12.84 | 14.54 | 13.3% | operator |
| 18653 | Nested Loop | 153.90 | 1066.06 | 592.7% | operator |
| 18656 | Hash | 3.18 | 14.79 | 365.5% | operator |
| 18659 | Seq Scan | 12.82 | 7.19 | 43.9% | operator |
| 18654 | Seq Scan | 19.30 | 43.05 | 123.1% | operator |
| 18655 | Index Scan | 0.08 | 0.12 | 56.8% | operator |
| 18657 | Seq Scan | 2.65 | 10.62 | 300.3% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 18654 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=4175
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0209
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=0.41, rt=43.05

### Step 2: Node 18655 (Index Scan) - LEAF

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
  - total_cost=2.0600
- **Output:** st=0.07, rt=0.12

### Step 3: Node 18657 (Seq Scan) - LEAF

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

### Step 4: Node 18653 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=16700
  - nt1=4175
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=43.0540
  - rt2=0.1192
  - sel=1.0000
  - st1=0.4124
  - st2=0.0716
  - startup_cost=0.4200
  - total_cost=13941.0100
- **Output:** st=3.71, rt=1066.06

### Step 5: Node 18656 (Hash)

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

### Step 6: Node 18659 (Seq Scan) - LEAF

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

### Step 7: Node 18652 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=16700
  - nt1=16700
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1066.0585
  - rt2=14.7884
  - sel=0.0001
  - st1=3.7068
  - st2=14.7887
  - startup_cost=448.4300
  - total_cost=14432.8700
- **Output:** st=52.29, rt=850.40

### Step 8: Node 18658 (Hash)

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

### Step 9: Node 18651 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=16700
  - nt1=16700
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=850.3988
  - rt2=14.5397
  - sel=0.0400
  - st1=52.2897
  - st2=14.5393
  - startup_cost=449.9900
  - total_cost=14485.7000
- **Output:** st=40.23, rt=910.38

### Step 10: Node 18649 (Seq Scan) - LEAF

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

### Step 11: Node 18650 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=16700
  - nt1=16700
  - nt2=0
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=910.3832
  - rt2=0.0000
  - sel=1.0000
  - st1=40.2297
  - st2=0.0000
  - startup_cost=14485.7000
  - total_cost=14485.7000
- **Output:** st=51.71, rt=51.71

### Step 12: Node 18648 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60132
  - nt1=1200243
  - nt2=16700
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=565.0624
  - rt2=51.7124
  - sel=0.0000
  - st1=0.9985
  - st2=51.7117
  - startup_cost=14736.2000
  - total_cost=148340.5600
- **Output:** st=168.80, rt=831.23

### Step 13: Node 18660 (Index Scan) - LEAF

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

### Step 14: Node 18647 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60132
  - nt1=60132
  - nt2=1
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=831.2288
  - rt2=-0.0424
  - sel=1.0000
  - st1=168.8049
  - st2=0.0037
  - startup_cost=14736.6300
  - total_cost=175583.0600
- **Output:** st=122.05, rt=1176.96

### Step 15: Node 18644 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** a5f39f08 (Aggregate -> Gather -> Aggregate (Outer) (Outer))
- **Consumes:** Nodes 18645, 18646
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=60132
  - Aggregate_Outer_nt1=60132
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=168
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=176635.3700
  - Aggregate_Outer_total_cost=177537.3500
  - Aggregate_np=0
  - Aggregate_nt=60150
  - Aggregate_nt1=300660
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=168
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2001
  - Aggregate_startup_cost=211609.9500
  - Aggregate_total_cost=212512.2000
  - Gather_Outer_np=0
  - Gather_Outer_nt=300660
  - Gather_Outer_nt1=60132
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=5
  - Gather_Outer_plan_width=168
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=5.0000
  - Gather_Outer_startup_cost=177635.3700
  - Gather_Outer_total_cost=208603.3500
- **Output:** st=1108.93, rt=1114.40

### Step 16: Node 18643 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=60150
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=1114.4047
  - rt2=0.0000
  - sel=1.0000
  - st1=1108.9311
  - st2=0.0000
  - startup_cost=217286.9900
  - total_cost=217437.3700
- **Output:** st=1148.02, rt=1150.49
