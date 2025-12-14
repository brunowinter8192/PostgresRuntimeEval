# Online Prediction Report

**Test Query:** Q9_30_seed_237916899
**Timestamp:** 2025-12-13 02:08:50

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 12.72%

## Phase C: Patterns in Query

- Total Patterns: 64

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 113504.2307 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 75736.1626 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 172 | 6131.8766 |
| c0a8d3de | Hash -> Hash Join -> [Seq Scan (Outer), ... | 3 | 148 | 6113.5159 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 148 | 172.9284 |
| 37515ad8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 124 | 168.3286 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 141.6847 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 108.1438 |
| 2873b8c3 | Hash Join -> [Nested Loop -> [Seq Scan (... | 3 | 48 | 94.8003 |
| 7d4e78be | Hash Join -> [Hash Join (Outer), Hash (I... | 2 | 48 | 89.9904 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 1 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 2 | 7df893ad | 6131.8766 | -0.0000% | REJECTED | 17.92% |
| 3 | c0a8d3de | 6113.5159 | -0.0000% | REJECTED | 17.92% |
| 4 | bb930825 | 172.9284 | -0.0000% | REJECTED | 17.92% |
| 5 | 37515ad8 | 168.3286 | -0.0000% | REJECTED | 17.92% |
| 6 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.92% |
| 7 | 2e0f44ef | 108.1438 | 0.0001% | REJECTED | 17.92% |
| 8 | 2873b8c3 | 94.8003 | 0.0000% | REJECTED | 17.92% |
| 9 | 7d4e78be | 89.9904 | 0.0000% | REJECTED | 17.92% |
| 10 | 30d6e09b | 89.9904 | 0.0000% | REJECTED | 17.92% |
| 11 | 7a51ce50 | 89.9904 | 0.0000% | REJECTED | 17.92% |
| 12 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 13 | 444761fb | 24.3176 | -0.0000% | REJECTED | 17.92% |
| 14 | 1a17c7f7 | 18.3606 | 0.0000% | REJECTED | 17.92% |
| 15 | fee45978 | 18.3606 | 0.0000% | REJECTED | 17.92% |
| 16 | 702e1a46 | 18.3606 | 0.0000% | REJECTED | 17.92% |
| 17 | ec92bdaa | 15.1555 | -0.0000% | REJECTED | 17.92% |
| 19 | a5f39f08 | 12.4695 | 1.7095% | ACCEPTED | 16.21% |
| 20 | e941d0ad | 4.5998 | N/A | REJECTED | 16.21% |
| 21 | 49ae7e42 | 4.5998 | N/A | REJECTED | 16.21% |
| 22 | ed7f2e45 | 4.5998 | N/A | REJECTED | 16.21% |
| 23 | 06fbc794 | 3.5767 | N/A | REJECTED | 16.21% |
| 24 | 59d2ec49 | 3.5767 | N/A | REJECTED | 16.21% |
| 25 | d8ffcf0c | 3.5767 | N/A | REJECTED | 16.21% |
| 29 | 9adbbadc | 1.9173 | N/A | REJECTED | 16.21% |
| 30 | 9a16eb41 | 1.9173 | N/A | REJECTED | 16.21% |
| 31 | f01db5fe | 1.9173 | N/A | REJECTED | 16.21% |
| 35 | d0331b81 | 0.7918 | N/A | REJECTED | 16.21% |
| 36 | 2bac8e6e | 0.7918 | N/A | REJECTED | 16.21% |
| 37 | 8259bae3 | 0.7918 | N/A | REJECTED | 16.21% |
| 38 | 4021e47f | 0.7918 | N/A | REJECTED | 16.21% |
| 39 | 45a78037 | 0.7918 | N/A | REJECTED | 16.21% |
| 40 | c65a77da | 0.7918 | N/A | REJECTED | 16.21% |
| 41 | 8951754f | 0.4452 | N/A | REJECTED | 16.21% |
| 42 | e92539ee | 0.4452 | N/A | REJECTED | 16.21% |
| 43 | fa5db8b6 | 0.4452 | N/A | REJECTED | 16.21% |
| 44 | 57d290cd | 0.4452 | N/A | REJECTED | 16.21% |
| 45 | 6e9566a0 | 0.4452 | N/A | REJECTED | 16.21% |
| 46 | 5968661e | 0.4452 | N/A | REJECTED | 16.21% |
| 47 | a2a9b057 | 0.4452 | N/A | REJECTED | 16.21% |
| 48 | ceeb5cca | 0.4452 | N/A | REJECTED | 16.21% |
## Query Tree

```
Node 17973 (Sort) - ROOT
  Node 17974 (Aggregate) [PATTERN: a5f39f08]
    Node 17975 (Gather) [consumed]
      Node 17976 (Aggregate) [consumed]
        Node 17977 (Hash Join)
          Node 17978 (Seq Scan) - LEAF
          Node 17979 (Hash)
            Node 17980 (Hash Join)
              Node 17981 (Seq Scan) - LEAF
              Node 17982 (Hash)
                Node 17983 (Hash Join)
                  Node 17984 (Hash Join)
                    Node 17985 (Nested Loop)
                      Node 17986 (Seq Scan) - LEAF
                      Node 17987 (Index Scan) - LEAF
                    Node 17988 (Hash)
                      Node 17989 (Seq Scan) - LEAF
                  Node 17990 (Hash)
                    Node 17991 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | a5f39f08 | 17974 | 17975, 17976 |


## Phase E: Final Prediction

- Final MRE: 12.07%
- Improvement: 0.65%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 17973 | Sort | 1303.38 | 1146.02 | 12.1% | operator |
| 17974 | Aggregate | 1303.25 | 1076.86 | 17.4% | pattern |
| 17977 | Hash Join | 1256.64 | 654.70 | 47.9% | operator |
| 17978 | Seq Scan | 154.21 | 192.19 | 24.6% | operator |
| 17979 | Hash | 1039.74 | 134.66 | 87.0% | operator |
| 17980 | Hash Join | 1022.10 | 832.28 | 18.6% | operator |
| 17981 | Seq Scan | 703.27 | 565.06 | 19.7% | operator |
| 17982 | Hash | 204.91 | 53.36 | 74.0% | operator |
| 17983 | Hash Join | 202.70 | 914.47 | 351.1% | operator |
| 17984 | Hash Join | 186.83 | 852.90 | 356.5% | operator |
| 17990 | Hash | 14.97 | 14.54 | 2.9% | operator |
| 17985 | Nested Loop | 179.66 | 1067.26 | 494.0% | operator |
| 17988 | Hash | 4.54 | 14.79 | 225.4% | operator |
| 17991 | Seq Scan | 14.96 | 7.19 | 51.9% | operator |
| 17986 | Seq Scan | 27.27 | 42.49 | 55.8% | operator |
| 17987 | Index Scan | 0.06 | 0.12 | 112.8% | operator |
| 17989 | Seq Scan | 4.08 | 10.62 | 160.0% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 17986 (Seq Scan) - LEAF

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

### Step 2: Node 17987 (Index Scan) - LEAF

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

### Step 3: Node 17989 (Seq Scan) - LEAF

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

### Step 4: Node 17985 (Nested Loop)

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

### Step 5: Node 17988 (Hash)

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

### Step 6: Node 17991 (Seq Scan) - LEAF

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

### Step 7: Node 17984 (Hash Join)

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

### Step 8: Node 17990 (Hash)

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

### Step 9: Node 17983 (Hash Join)

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

### Step 10: Node 17981 (Seq Scan) - LEAF

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

### Step 11: Node 17982 (Hash)

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

### Step 12: Node 17980 (Hash Join)

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

### Step 13: Node 17978 (Seq Scan) - LEAF

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

### Step 14: Node 17979 (Hash)

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

### Step 15: Node 17977 (Hash Join)

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

### Step 16: Node 17974 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** a5f39f08 (Aggregate -> Gather -> Aggregate (Outer) (Outer))
- **Consumes:** Nodes 17975, 17976
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

### Step 17: Node 17973 (Sort) - ROOT

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
