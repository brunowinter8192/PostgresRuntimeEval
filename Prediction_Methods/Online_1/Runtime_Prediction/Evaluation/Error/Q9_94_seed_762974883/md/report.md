# Online Prediction Report

**Test Query:** Q9_94_seed_762974883
**Timestamp:** 2025-12-13 02:14:19

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 11.68%

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
Node 19243 (Sort) - ROOT
  Node 19244 (Aggregate) [PATTERN: a5f39f08]
    Node 19245 (Gather) [consumed]
      Node 19246 (Aggregate) [consumed]
        Node 19247 (Hash Join)
          Node 19248 (Seq Scan) - LEAF
          Node 19249 (Hash)
            Node 19250 (Hash Join)
              Node 19251 (Seq Scan) - LEAF
              Node 19252 (Hash)
                Node 19253 (Hash Join)
                  Node 19254 (Hash Join)
                    Node 19255 (Nested Loop)
                      Node 19256 (Seq Scan) - LEAF
                      Node 19257 (Index Scan) - LEAF
                    Node 19258 (Hash)
                      Node 19259 (Seq Scan) - LEAF
                  Node 19260 (Hash)
                    Node 19261 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | a5f39f08 | 19244 | 19245, 19246 |


## Phase E: Final Prediction

- Final MRE: 11.02%
- Improvement: 0.66%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 19243 | Sort | 1287.96 | 1146.03 | 11.0% | operator |
| 19244 | Aggregate | 1287.83 | 1078.22 | 16.3% | pattern |
| 19247 | Hash Join | 1238.03 | 652.36 | 47.3% | operator |
| 19248 | Seq Scan | 129.96 | 192.19 | 47.9% | operator |
| 19249 | Hash | 1041.70 | 133.58 | 87.2% | operator |
| 19250 | Hash Join | 1023.10 | 832.06 | 18.7% | operator |
| 19251 | Seq Scan | 693.83 | 565.06 | 18.6% | operator |
| 19252 | Hash | 213.44 | 52.99 | 75.2% | operator |
| 19253 | Hash Join | 211.09 | 913.56 | 332.8% | operator |
| 19254 | Hash Join | 195.55 | 852.32 | 335.9% | operator |
| 19260 | Hash | 14.64 | 14.54 | 0.7% | operator |
| 19255 | Nested Loop | 188.65 | 1066.98 | 465.6% | operator |
| 19258 | Hash | 4.23 | 14.79 | 249.6% | operator |
| 19261 | Seq Scan | 14.62 | 7.19 | 50.8% | operator |
| 19256 | Seq Scan | 28.92 | 42.61 | 47.3% | operator |
| 19257 | Index Scan | 0.06 | 0.12 | 109.1% | operator |
| 19259 | Seq Scan | 3.75 | 10.62 | 182.7% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 19256 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=5344
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0267
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=0.41, rt=42.61

### Step 2: Node 19257 (Index Scan) - LEAF

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
  - total_cost=1.8000
- **Output:** st=0.07, rt=0.12

### Step 3: Node 19259 (Seq Scan) - LEAF

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

### Step 4: Node 19255 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=21377
  - nt1=5344
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=42.6148
  - rt2=0.1192
  - sel=1.0000
  - st1=0.4081
  - st2=0.0716
  - startup_cost=0.4200
  - total_cost=14978.4200
- **Output:** st=3.77, rt=1066.98

### Step 5: Node 19258 (Hash)

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

### Step 6: Node 19261 (Seq Scan) - LEAF

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

### Step 7: Node 19254 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=21377
  - nt1=21377
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1066.9817
  - rt2=14.7884
  - sel=0.0001
  - st1=3.7697
  - st2=14.7887
  - startup_cost=448.4300
  - total_cost=15482.5600
- **Output:** st=52.54, rt=852.32

### Step 8: Node 19260 (Hash)

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

### Step 9: Node 19253 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=21377
  - nt1=21377
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=852.3241
  - rt2=14.5397
  - sel=0.0400
  - st1=52.5426
  - st2=14.5393
  - startup_cost=449.9900
  - total_cost=15549.7500
- **Output:** st=40.62, rt=913.56

### Step 10: Node 19251 (Seq Scan) - LEAF

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

### Step 11: Node 19252 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=21377
  - nt1=21377
  - nt2=0
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=913.5557
  - rt2=0.0000
  - sel=1.0000
  - st1=40.6229
  - st2=0.0000
  - startup_cost=15549.7500
  - total_cost=15549.7500
- **Output:** st=52.99, rt=52.99

### Step 12: Node 19250 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=76972
  - nt1=1200243
  - nt2=21377
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=565.0624
  - rt2=52.9884
  - sel=0.0000
  - st1=0.9985
  - st2=52.9877
  - startup_cost=15870.4100
  - total_cost=149474.7900
- **Output:** st=168.22, rt=832.06

### Step 13: Node 19248 (Seq Scan) - LEAF

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

### Step 14: Node 19249 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=76972
  - nt1=76972
  - nt2=0
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=832.0650
  - rt2=0.0000
  - sel=1.0000
  - st1=168.2167
  - st2=0.0000
  - startup_cost=149474.7900
  - total_cost=149474.7900
- **Output:** st=133.57, rt=133.58

### Step 15: Node 19247 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=124148
  - nt1=483871
  - nt2=76972
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=192.1919
  - rt2=133.5750
  - sel=0.0000
  - st1=0.1717
  - st2=133.5740
  - startup_cost=150436.9400
  - total_cost=183784.8300
- **Output:** st=107.77, rt=652.36

### Step 16: Node 19244 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** a5f39f08 (Aggregate -> Gather -> Aggregate (Outer) (Outer))
- **Consumes:** Nodes 19245, 19246
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=60150
  - Aggregate_Outer_nt1=124148
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=168
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.4845
  - Aggregate_Outer_startup_cost=185957.4200
  - Aggregate_Outer_total_cost=186859.6700
  - Aggregate_np=0
  - Aggregate_nt=60150
  - Aggregate_nt1=180450
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=168
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.3333
  - Aggregate_startup_cost=207709.1700
  - Aggregate_total_cost=208611.4200
  - Gather_Outer_np=0
  - Gather_Outer_nt=180450
  - Gather_Outer_nt1=60150
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=168
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.0000
  - Gather_Outer_startup_cost=186957.4200
  - Gather_Outer_total_cost=205904.6700
- **Output:** st=1072.72, rt=1078.22

### Step 17: Node 19243 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=60150
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=1078.2214
  - rt2=0.0000
  - sel=1.0000
  - st1=1072.7161
  - st2=0.0000
  - startup_cost=213386.2100
  - total_cost=213536.5900
- **Output:** st=1143.60, rt=1146.03
