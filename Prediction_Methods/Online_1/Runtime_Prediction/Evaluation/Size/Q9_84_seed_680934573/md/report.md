# Online Prediction Report

**Test Query:** Q9_84_seed_680934573
**Timestamp:** 2025-12-21 23:19:10

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 8.20%

## Phase C: Patterns in Query

- Total Patterns: 64

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 72 | 4.0% | 2.9042 |
| 6e659102 | Sort -> Aggregate -> Gather -> Aggregate... | 4 | 24 | 6.2% | 1.4968 |
| 8951754f | Sort -> Aggregate -> Gather -> Aggregate... | 5 | 4 | 11.3% | 0.4519 |
| e92539ee | Sort -> Aggregate -> Gather -> Aggregate... | 6 | 4 | 11.3% | 0.4519 |
| fa5db8b6 | Sort -> Aggregate -> Gather -> Aggregate... | 7 | 4 | 11.3% | 0.4519 |
| 57d290cd | Sort -> Aggregate -> Gather -> Aggregate... | 8 | 4 | 11.3% | 0.4519 |
| 6e9566a0 | Sort -> Aggregate -> Gather -> Aggregate... | 9 | 4 | 11.3% | 0.4519 |
| 5968661e | Sort -> Aggregate -> Gather -> Aggregate... | 10 | 4 | 11.3% | 0.4519 |
| a2a9b057 | Sort -> Aggregate -> Gather -> Aggregate... | 11 | 4 | 11.3% | 0.4519 |
| ceeb5cca | Sort -> Aggregate -> Gather -> Aggregate... | 12 | 4 | 11.3% | 0.4519 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 9.3% | 13.3894 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 96 | 13.0% | 12.4695 |
| efde8b38 | Aggregate -> Gather -> Aggregate -> Hash... | 4 | 52 | 10.3% | 5.3353 |
| 310134da | Aggregate -> Gather -> Aggregate -> Hash... | 5 | 52 | 10.3% | 5.3353 |
| d0331b81 | Aggregate -> Gather -> Aggregate -> Hash... | 6 | 4 | 22.2% | 0.8883 |
| 2bac8e6e | Aggregate -> Gather -> Aggregate -> Hash... | 7 | 4 | 22.2% | 0.8883 |
| 8259bae3 | Aggregate -> Gather -> Aggregate -> Hash... | 8 | 4 | 22.2% | 0.8883 |
| 4021e47f | Aggregate -> Gather -> Aggregate -> Hash... | 9 | 4 | 22.2% | 0.8883 |
| 45a78037 | Aggregate -> Gather -> Aggregate -> Hash... | 10 | 4 | 22.2% | 0.8883 |
| c65a77da | Aggregate -> Gather -> Aggregate -> Hash... | 11 | 4 | 22.2% | 0.8883 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 96 | 8.0% | 7.7175 |
| 2e8f3f67 | Gather -> Aggregate -> Hash Join (Outer)... | 3 | 52 | 6.8% | 3.5252 |
| af27a52b | Gather -> Aggregate -> Hash Join -> [Seq... | 4 | 52 | 6.8% | 3.5252 |
| 10ed8951 | Gather -> Aggregate -> Hash Join -> [Seq... | 5 | 4 | 15.9% | 0.6347 |
| 4ecd02f7 | Gather -> Aggregate -> Hash Join -> [Seq... | 6 | 4 | 15.9% | 0.6347 |
| 2eaabdb6 | Gather -> Aggregate -> Hash Join -> [Seq... | 7 | 4 | 15.9% | 0.6347 |
| eb55f880 | Gather -> Aggregate -> Hash Join -> [Seq... | 8 | 4 | 15.9% | 0.6347 |
| 9627c015 | Gather -> Aggregate -> Hash Join -> [Seq... | 9 | 4 | 15.9% | 0.6347 |
| ec6765c4 | Gather -> Aggregate -> Hash Join -> [Seq... | 10 | 4 | 15.9% | 0.6347 |
| 7524c54c | Aggregate -> Hash Join (Outer) | 2 | 76 | 6.9% | 5.2190 |
| 422ae017 | Aggregate -> Hash Join -> [Seq Scan (Out... | 3 | 76 | 6.9% | 5.2190 |
| 7542faeb | Aggregate -> Hash Join -> [Seq Scan (Out... | 4 | 4 | 22.0% | 0.8805 |
| 5891ae15 | Aggregate -> Hash Join -> [Seq Scan (Out... | 5 | 4 | 22.0% | 0.8805 |
| c57cb4bb | Aggregate -> Hash Join -> [Seq Scan (Out... | 6 | 4 | 22.0% | 0.8805 |
| 6b3fb960 | Aggregate -> Hash Join -> [Seq Scan (Out... | 7 | 4 | 22.0% | 0.8805 |
| d3455a22 | Aggregate -> Hash Join -> [Seq Scan (Out... | 8 | 4 | 22.0% | 0.8805 |
| 800ae9e1 | Aggregate -> Hash Join -> [Seq Scan (Out... | 9 | 4 | 22.0% | 0.8805 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 148 | 116.8% | 172.9284 |
| 37515ad8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 124 | 135.7% | 168.3286 |
| ec92bdaa | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 52 | 29.1% | 15.1555 |
| 9adbbadc | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 4 | 47.9% | 1.9173 |
| 9a16eb41 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 7 | 4 | 47.9% | 1.9173 |
| f01db5fe | Hash Join -> [Seq Scan (Outer), Hash -> ... | 8 | 4 | 47.9% | 1.9173 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 172 | 3565.0% | 6131.8766 |
| c0a8d3de | Hash -> Hash Join -> [Seq Scan (Outer), ... | 3 | 148 | 4130.8% | 6113.5159 |
| 444761fb | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 52 | 46.8% | 24.3176 |
| 06fbc794 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 5 | 4 | 89.4% | 3.5767 |
| 59d2ec49 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 6 | 4 | 89.4% | 3.5767 |
| d8ffcf0c | Hash -> Hash Join -> [Seq Scan (Outer), ... | 7 | 4 | 89.4% | 3.5767 |
| e941d0ad | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 24 | 19.2% | 4.5998 |
| 49ae7e42 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 24 | 19.2% | 4.5998 |
| ed7f2e45 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 24 | 19.2% | 4.5998 |
| 1a17c7f7 | Hash -> Hash Join -> [Hash Join (Outer),... | 3 | 24 | 76.5% | 18.3606 |
| fee45978 | Hash -> Hash Join -> [Hash Join -> [Nest... | 4 | 24 | 76.5% | 18.3606 |
| 702e1a46 | Hash -> Hash Join -> [Hash Join -> [Nest... | 5 | 24 | 76.5% | 18.3606 |
| 7d4e78be | Hash Join -> [Hash Join (Outer), Hash (I... | 2 | 48 | 187.5% | 89.9904 |
| 30d6e09b | Hash Join -> [Hash Join -> [Nested Loop ... | 3 | 48 | 187.5% | 89.9904 |
| 7a51ce50 | Hash Join -> [Hash Join -> [Nested Loop ... | 4 | 48 | 187.5% | 89.9904 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 75.1% | 108.1438 |
| 2873b8c3 | Hash Join -> [Nested Loop -> [Seq Scan (... | 3 | 48 | 197.5% | 94.8003 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 147.6% | 141.6847 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 33781.0% | 113504.2307 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 1 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 2 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 3 | 7df893ad | 6131.8766 | -0.0000% | REJECTED | 17.92% |
| 4 | 4fc84c77 | 13.3894 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 5 | 2e0f44ef | 108.1438 | 0.0001% | REJECTED | 17.92% |
| 6 | 634cdbe2 | 7.7175 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 7 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.92% |
| 8 | 7524c54c | 5.2190 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 9 | 7d4e78be | 89.9904 | 0.0000% | REJECTED | 17.92% |
| 10 | bb930825 | 172.9284 | -0.0000% | REJECTED | 17.92% |
| 11 | c0a8d3de | 6113.5159 | -0.0000% | REJECTED | 17.92% |
| 12 | a5f39f08 | 12.4695 | 1.7095% | ACCEPTED | 16.21% |
| 13 | 422ae017 | 3.0007 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 14 | b3a45093 | 2.7998 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 15 | 30d6e09b | 89.9904 | 0.0000% | REJECTED | 16.21% |
| 16 | 2873b8c3 | 94.8003 | 0.0000% | REJECTED | 16.21% |
| 17 | 1a17c7f7 | 18.3606 | N/A | REJECTED | 16.21% |
| 18 | 37515ad8 | 168.3286 | -0.0000% | REJECTED | 16.21% |
| 19 | efde8b38 | 1.7942 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 20 | 444761fb | 24.3176 | 0.0000% | REJECTED | 16.21% |
| 21 | 7a51ce50 | 89.9904 | 0.0000% | REJECTED | 16.21% |
| 22 | 6e659102 | 1.3924 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 23 | e941d0ad | 4.5998 | N/A | REJECTED | 16.21% |
| 24 | fee45978 | 18.3606 | N/A | REJECTED | 16.21% |
| 25 | 310134da | 1.7942 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 26 | ec92bdaa | 15.1555 | -0.0000% | REJECTED | 16.21% |
| 27 | 49ae7e42 | 4.5998 | N/A | REJECTED | 16.21% |
| 28 | 702e1a46 | 18.3606 | N/A | REJECTED | 16.21% |
| 29 | 8951754f | 0.4452 | N/A | REJECTED | 16.21% |
| 30 | 06fbc794 | 3.5767 | N/A | REJECTED | 16.21% |
| 31 | ed7f2e45 | 4.5998 | N/A | REJECTED | 16.21% |
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
Node 19043 (Sort) - ROOT
  Node 19044 (Aggregate) [PATTERN: a5f39f08]
    Node 19045 (Gather) [consumed]
      Node 19046 (Aggregate) [consumed]
        Node 19047 (Hash Join)
          Node 19048 (Seq Scan) - LEAF
          Node 19049 (Hash)
            Node 19050 (Hash Join)
              Node 19051 (Seq Scan) - LEAF
              Node 19052 (Hash)
                Node 19053 (Hash Join)
                  Node 19054 (Hash Join)
                    Node 19055 (Nested Loop)
                      Node 19056 (Seq Scan) - LEAF
                      Node 19057 (Index Scan) - LEAF
                    Node 19058 (Hash)
                      Node 19059 (Seq Scan) - LEAF
                  Node 19060 (Hash)
                    Node 19061 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | a5f39f08 | 19044 | 19045, 19046 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 7.52%
- Improvement: 0.68%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 19043 | Sort | 1239.24 | 1146.02 | 7.5% | operator |
| 19044 | Aggregate | 1239.12 | 1076.86 | 13.1% | pattern |
| 19047 | Hash Join | 1192.52 | 654.70 | 45.1% | operator |
| 19048 | Seq Scan | 132.07 | 192.19 | 45.5% | operator |
| 19049 | Hash | 999.25 | 134.66 | 86.5% | operator |
| 19050 | Hash Join | 981.43 | 832.28 | 15.2% | operator |
| 19051 | Seq Scan | 652.85 | 565.06 | 13.4% | operator |
| 19052 | Hash | 212.56 | 53.36 | 74.9% | operator |
| 19053 | Hash Join | 209.91 | 914.47 | 335.7% | operator |
| 19054 | Hash Join | 194.16 | 852.90 | 339.3% | operator |
| 19060 | Hash | 14.84 | 14.54 | 2.0% | operator |
| 19055 | Nested Loop | 187.21 | 1067.26 | 470.1% | operator |
| 19058 | Hash | 4.56 | 14.79 | 224.1% | operator |
| 19061 | Seq Scan | 14.82 | 7.19 | 51.5% | operator |
| 19056 | Seq Scan | 27.38 | 42.49 | 55.2% | operator |
| 19057 | Index Scan | 0.06 | 0.12 | 105.4% | operator |
| 19059 | Seq Scan | 4.14 | 10.62 | 156.3% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 19056 (Seq Scan) - LEAF

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

### Step 2: Node 19057 (Index Scan) - LEAF

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

### Step 3: Node 19059 (Seq Scan) - LEAF

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

### Step 4: Node 19055 (Nested Loop)

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

### Step 5: Node 19058 (Hash)

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

### Step 6: Node 19061 (Seq Scan) - LEAF

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

### Step 7: Node 19054 (Hash Join)

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

### Step 8: Node 19060 (Hash)

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

### Step 9: Node 19053 (Hash Join)

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

### Step 10: Node 19051 (Seq Scan) - LEAF

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

### Step 11: Node 19052 (Hash)

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

### Step 12: Node 19050 (Hash Join)

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

### Step 13: Node 19048 (Seq Scan) - LEAF

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

### Step 14: Node 19049 (Hash)

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

### Step 15: Node 19047 (Hash Join)

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

### Step 16: Node 19044 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** a5f39f08 (Aggregate -> Gather -> Aggregate (Outer) (Outer))
- **Consumes:** Nodes 19045, 19046
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

### Step 17: Node 19043 (Sort) - ROOT

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
