# Online Prediction Report

**Test Query:** Q9_7_seed_49224186
**Timestamp:** 2025-12-13 04:31:54

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 11.45%

## Phase C: Patterns in Query

- Total Patterns: 64

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 75736.1626 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 113504.2307 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 26.4017 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 172 | 6131.8766 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 148 | 172.9284 |
| c0a8d3de | Hash -> Hash Join -> [Seq Scan (Outer), ... | 3 | 148 | 6113.5159 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 13.3894 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 108.1438 |
| 37515ad8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 124 | 168.3286 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 96 | 7.7175 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 1 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 2 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 3 | 7df893ad | 6131.8766 | -0.0000% | REJECTED | 17.92% |
| 4 | bb930825 | 172.9284 | -0.0000% | REJECTED | 17.92% |
| 5 | c0a8d3de | 6113.5159 | -0.0000% | REJECTED | 17.92% |
| 7 | 2e0f44ef | 108.1438 | 0.0001% | REJECTED | 17.92% |
| 8 | 37515ad8 | 168.3286 | -0.0000% | REJECTED | 17.92% |
| 10 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.92% |
| 11 | a5f39f08 | 12.4695 | 1.7095% | ACCEPTED | 16.21% |
| 16 | 444761fb | 24.3176 | 0.0000% | REJECTED | 16.21% |
| 18 | ec92bdaa | 15.1555 | -0.0000% | REJECTED | 16.21% |
| 19 | 7d4e78be | 89.9904 | 0.0000% | REJECTED | 16.21% |
| 20 | 30d6e09b | 89.9904 | 0.0000% | REJECTED | 16.21% |
| 21 | 2873b8c3 | 94.8003 | 0.0000% | REJECTED | 16.21% |
| 22 | 7a51ce50 | 89.9904 | 0.0000% | REJECTED | 16.21% |
| 23 | 1a17c7f7 | 18.3606 | N/A | REJECTED | 16.21% |
| 25 | e941d0ad | 4.5998 | N/A | REJECTED | 16.21% |
| 26 | fee45978 | 18.3606 | N/A | REJECTED | 16.21% |
| 27 | 49ae7e42 | 4.5998 | N/A | REJECTED | 16.21% |
| 28 | 702e1a46 | 18.3606 | N/A | REJECTED | 16.21% |
| 29 | ed7f2e45 | 4.5998 | N/A | REJECTED | 16.21% |
| 30 | 8951754f | 0.4452 | N/A | REJECTED | 16.21% |
| 31 | 06fbc794 | 3.5767 | N/A | REJECTED | 16.21% |
| 32 | e92539ee | 0.4452 | N/A | REJECTED | 16.21% |
| 33 | d0331b81 | 0.7918 | N/A | REJECTED | 16.21% |
| 34 | 9adbbadc | 1.9173 | N/A | REJECTED | 16.21% |
| 35 | 59d2ec49 | 3.5767 | N/A | REJECTED | 16.21% |
| 36 | fa5db8b6 | 0.4452 | N/A | REJECTED | 16.21% |
| 37 | 2bac8e6e | 0.7918 | N/A | REJECTED | 16.21% |
| 38 | 9a16eb41 | 1.9173 | N/A | REJECTED | 16.21% |
| 39 | d8ffcf0c | 3.5767 | N/A | REJECTED | 16.21% |
| 40 | 57d290cd | 0.4452 | N/A | REJECTED | 16.21% |
| 41 | 8259bae3 | 0.7918 | N/A | REJECTED | 16.21% |
| 42 | f01db5fe | 1.9173 | N/A | REJECTED | 16.21% |
| 43 | 6e9566a0 | 0.4452 | N/A | REJECTED | 16.21% |
| 44 | 4021e47f | 0.7918 | N/A | REJECTED | 16.21% |
| 45 | 5968661e | 0.4452 | N/A | REJECTED | 16.21% |
| 46 | 45a78037 | 0.7918 | N/A | REJECTED | 16.21% |
| 47 | a2a9b057 | 0.4452 | N/A | REJECTED | 16.21% |
| 48 | c65a77da | 0.7918 | N/A | REJECTED | 16.21% |
| 49 | ceeb5cca | 0.4452 | N/A | REJECTED | 16.21% |
## Query Tree

```
Node 18952 (Sort) - ROOT
  Node 18953 (Aggregate) [PATTERN: a5f39f08]
    Node 18954 (Gather) [consumed]
      Node 18955 (Aggregate) [consumed]
        Node 18956 (Hash Join)
          Node 18957 (Seq Scan) - LEAF
          Node 18958 (Hash)
            Node 18959 (Hash Join)
              Node 18960 (Seq Scan) - LEAF
              Node 18961 (Hash)
                Node 18962 (Hash Join)
                  Node 18963 (Hash Join)
                    Node 18964 (Nested Loop)
                      Node 18965 (Seq Scan) - LEAF
                      Node 18966 (Index Scan) - LEAF
                    Node 18967 (Hash)
                      Node 18968 (Seq Scan) - LEAF
                  Node 18969 (Hash)
                    Node 18970 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | a5f39f08 | 18953 | 18954, 18955 |


## Phase E: Final Prediction

- Final MRE: 10.79%
- Improvement: 0.66%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 18952 | Sort | 1284.67 | 1146.02 | 10.8% | operator |
| 18953 | Aggregate | 1284.52 | 1076.86 | 16.2% | pattern |
| 18956 | Hash Join | 1237.34 | 654.70 | 47.1% | operator |
| 18957 | Seq Scan | 130.84 | 192.19 | 46.9% | operator |
| 18958 | Hash | 1044.43 | 134.66 | 87.1% | operator |
| 18959 | Hash Join | 1026.44 | 832.28 | 18.9% | operator |
| 18960 | Seq Scan | 695.97 | 565.06 | 18.8% | operator |
| 18961 | Hash | 213.29 | 53.36 | 75.0% | operator |
| 18962 | Hash Join | 210.91 | 914.47 | 333.6% | operator |
| 18963 | Hash Join | 195.40 | 852.90 | 336.5% | operator |
| 18969 | Hash | 14.63 | 14.54 | 0.6% | operator |
| 18964 | Nested Loop | 188.27 | 1067.26 | 466.9% | operator |
| 18967 | Hash | 4.45 | 14.79 | 232.5% | operator |
| 18970 | Seq Scan | 14.62 | 7.19 | 50.8% | operator |
| 18965 | Seq Scan | 26.32 | 42.49 | 61.4% | operator |
| 18966 | Index Scan | 0.06 | 0.12 | 102.0% | operator |
| 18968 | Seq Scan | 3.95 | 10.62 | 168.9% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 18965 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=5678
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0284
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=0.41, rt=42.49

### Step 2: Node 18966 (Index Scan) - LEAF

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
  - total_cost=1.7400
- **Output:** st=0.07, rt=0.12

### Step 3: Node 18968 (Seq Scan) - LEAF

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

### Step 4: Node 18964 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=22712
  - nt1=5678
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=42.4913
  - rt2=0.1192
  - sel=1.0000
  - st1=0.4069
  - st2=0.0716
  - startup_cost=0.4200
  - total_cost=15266.4800
- **Output:** st=3.80, rt=1067.26

### Step 5: Node 18967 (Hash)

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

### Step 6: Node 18970 (Seq Scan) - LEAF

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

### Step 7: Node 18963 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=22712
  - nt1=22712
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1067.2563
  - rt2=14.7884
  - sel=0.0001
  - st1=3.7975
  - st2=14.7887
  - startup_cost=448.4300
  - total_cost=15774.1200
- **Output:** st=52.62, rt=852.90

### Step 8: Node 18969 (Hash)

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

### Step 9: Node 18962 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=22712
  - nt1=22712
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=852.9039
  - rt2=14.5397
  - sel=0.0400
  - st1=52.6150
  - st2=14.5393
  - startup_cost=449.9900
  - total_cost=15845.4100
- **Output:** st=40.74, rt=914.47

### Step 10: Node 18960 (Seq Scan) - LEAF

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

### Step 11: Node 18961 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=22712
  - nt1=22712
  - nt2=0
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=914.4693
  - rt2=0.0000
  - sel=1.0000
  - st1=40.7372
  - st2=0.0000
  - startup_cost=15845.4100
  - total_cost=15845.4100
- **Output:** st=53.36, rt=53.36

### Step 12: Node 18959 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=81779
  - nt1=1200243
  - nt2=22712
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=565.0624
  - rt2=53.3587
  - sel=0.0000
  - st1=0.9985
  - st2=53.3579
  - startup_cost=16186.0900
  - total_cost=149790.4800
- **Output:** st=168.03, rt=832.28

### Step 13: Node 18957 (Seq Scan) - LEAF

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

### Step 14: Node 18958 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=81779
  - nt1=81779
  - nt2=0
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=832.2810
  - rt2=0.0000
  - sel=1.0000
  - st1=168.0318
  - st2=0.0000
  - startup_cost=149790.4800
  - total_cost=149790.4800
- **Output:** st=134.66, rt=134.66

### Step 15: Node 18956 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=131901
  - nt1=483871
  - nt2=81779
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=192.1919
  - rt2=134.6618
  - sel=0.0000
  - st1=0.1717
  - st2=134.6607
  - startup_cost=150812.7200
  - total_cost=184195.5000
- **Output:** st=107.72, rt=654.70

### Step 16: Node 18953 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** a5f39f08 (Aggregate -> Gather -> Aggregate (Outer) (Outer))
- **Consumes:** Nodes 18954, 18955
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=60150
  - Aggregate_Outer_nt1=131901
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=168
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.4560
  - Aggregate_Outer_startup_cost=186503.7600
  - Aggregate_Outer_total_cost=187406.0100
  - Aggregate_np=0
  - Aggregate_nt=60150
  - Aggregate_nt1=180450
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=168
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.3333
  - Aggregate_startup_cost=208255.5100
  - Aggregate_total_cost=209157.7600
  - Gather_Outer_np=0
  - Gather_Outer_nt=180450
  - Gather_Outer_nt1=60150
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=168
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.0000
  - Gather_Outer_startup_cost=187503.7600
  - Gather_Outer_total_cost=206451.0100
- **Output:** st=1071.35, rt=1076.86

### Step 17: Node 18952 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=60150
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=1076.8577
  - rt2=0.0000
  - sel=1.0000
  - st1=1071.3516
  - st2=0.0000
  - startup_cost=213932.5500
  - total_cost=214082.9300
- **Output:** st=1143.58, rt=1146.02
