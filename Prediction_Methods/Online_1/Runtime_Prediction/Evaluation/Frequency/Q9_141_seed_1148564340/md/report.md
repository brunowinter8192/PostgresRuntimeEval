# Online Prediction Report

**Test Query:** Q9_141_seed_1148564340
**Timestamp:** 2025-12-22 08:06:31

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 10.26%

## Phase C: Patterns in Query

- Total Patterns: 64

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 33781.0% | 113504.2307 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 172 | 3565.0% | 6131.8766 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 148 | 116.8% | 172.9284 |
| c0a8d3de | Hash -> Hash Join -> [Seq Scan (Outer), ... | 3 | 148 | 4130.8% | 6113.5159 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 9.3% | 13.3894 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 75.1% | 108.1438 |
| 37515ad8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 124 | 135.7% | 168.3286 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 96 | 8.0% | 7.7175 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 147.6% | 141.6847 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 96 | 13.0% | 12.4695 |
| 7524c54c | Aggregate -> Hash Join (Outer) | 2 | 76 | 6.9% | 5.2190 |
| 422ae017 | Aggregate -> Hash Join -> [Seq Scan (Out... | 3 | 76 | 6.9% | 5.2190 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 72 | 4.0% | 2.9042 |
| 2e8f3f67 | Gather -> Aggregate -> Hash Join (Outer)... | 3 | 52 | 6.8% | 3.5252 |
| efde8b38 | Aggregate -> Gather -> Aggregate -> Hash... | 4 | 52 | 10.3% | 5.3353 |
| af27a52b | Gather -> Aggregate -> Hash Join -> [Seq... | 4 | 52 | 6.8% | 3.5252 |
| 444761fb | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 52 | 46.8% | 24.3176 |
| 310134da | Aggregate -> Gather -> Aggregate -> Hash... | 5 | 52 | 10.3% | 5.3353 |
| ec92bdaa | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 52 | 29.1% | 15.1555 |
| 7d4e78be | Hash Join -> [Hash Join (Outer), Hash (I... | 2 | 48 | 187.5% | 89.9904 |
| 30d6e09b | Hash Join -> [Hash Join -> [Nested Loop ... | 3 | 48 | 187.5% | 89.9904 |
| 2873b8c3 | Hash Join -> [Nested Loop -> [Seq Scan (... | 3 | 48 | 197.5% | 94.8003 |
| 7a51ce50 | Hash Join -> [Hash Join -> [Nested Loop ... | 4 | 48 | 187.5% | 89.9904 |
| 1a17c7f7 | Hash -> Hash Join -> [Hash Join (Outer),... | 3 | 24 | 76.5% | 18.3606 |
| 6e659102 | Sort -> Aggregate -> Gather -> Aggregate... | 4 | 24 | 6.2% | 1.4968 |
| e941d0ad | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 24 | 19.2% | 4.5998 |
| fee45978 | Hash -> Hash Join -> [Hash Join -> [Nest... | 4 | 24 | 76.5% | 18.3606 |
| 49ae7e42 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 24 | 19.2% | 4.5998 |
| 702e1a46 | Hash -> Hash Join -> [Hash Join -> [Nest... | 5 | 24 | 76.5% | 18.3606 |
| ed7f2e45 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 24 | 19.2% | 4.5998 |
| 7542faeb | Aggregate -> Hash Join -> [Seq Scan (Out... | 4 | 4 | 22.0% | 0.8805 |
| 8951754f | Sort -> Aggregate -> Gather -> Aggregate... | 5 | 4 | 11.3% | 0.4519 |
| 10ed8951 | Gather -> Aggregate -> Hash Join -> [Seq... | 5 | 4 | 15.9% | 0.6347 |
| 5891ae15 | Aggregate -> Hash Join -> [Seq Scan (Out... | 5 | 4 | 22.0% | 0.8805 |
| 06fbc794 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 5 | 4 | 89.4% | 3.5767 |
| e92539ee | Sort -> Aggregate -> Gather -> Aggregate... | 6 | 4 | 11.3% | 0.4519 |
| d0331b81 | Aggregate -> Gather -> Aggregate -> Hash... | 6 | 4 | 22.2% | 0.8883 |
| 4ecd02f7 | Gather -> Aggregate -> Hash Join -> [Seq... | 6 | 4 | 15.9% | 0.6347 |
| c57cb4bb | Aggregate -> Hash Join -> [Seq Scan (Out... | 6 | 4 | 22.0% | 0.8805 |
| 9adbbadc | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 4 | 47.9% | 1.9173 |
| 59d2ec49 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 6 | 4 | 89.4% | 3.5767 |
| fa5db8b6 | Sort -> Aggregate -> Gather -> Aggregate... | 7 | 4 | 11.3% | 0.4519 |
| 2bac8e6e | Aggregate -> Gather -> Aggregate -> Hash... | 7 | 4 | 22.2% | 0.8883 |
| 2eaabdb6 | Gather -> Aggregate -> Hash Join -> [Seq... | 7 | 4 | 15.9% | 0.6347 |
| 6b3fb960 | Aggregate -> Hash Join -> [Seq Scan (Out... | 7 | 4 | 22.0% | 0.8805 |
| 9a16eb41 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 7 | 4 | 47.9% | 1.9173 |
| d8ffcf0c | Hash -> Hash Join -> [Seq Scan (Outer), ... | 7 | 4 | 89.4% | 3.5767 |
| 57d290cd | Sort -> Aggregate -> Gather -> Aggregate... | 8 | 4 | 11.3% | 0.4519 |
| 8259bae3 | Aggregate -> Gather -> Aggregate -> Hash... | 8 | 4 | 22.2% | 0.8883 |
| eb55f880 | Gather -> Aggregate -> Hash Join -> [Seq... | 8 | 4 | 15.9% | 0.6347 |
| d3455a22 | Aggregate -> Hash Join -> [Seq Scan (Out... | 8 | 4 | 22.0% | 0.8805 |
| f01db5fe | Hash Join -> [Seq Scan (Outer), Hash -> ... | 8 | 4 | 47.9% | 1.9173 |
| 6e9566a0 | Sort -> Aggregate -> Gather -> Aggregate... | 9 | 4 | 11.3% | 0.4519 |
| 4021e47f | Aggregate -> Gather -> Aggregate -> Hash... | 9 | 4 | 22.2% | 0.8883 |
| 9627c015 | Gather -> Aggregate -> Hash Join -> [Seq... | 9 | 4 | 15.9% | 0.6347 |
| 800ae9e1 | Aggregate -> Hash Join -> [Seq Scan (Out... | 9 | 4 | 22.0% | 0.8805 |
| 5968661e | Sort -> Aggregate -> Gather -> Aggregate... | 10 | 4 | 11.3% | 0.4519 |
| 45a78037 | Aggregate -> Gather -> Aggregate -> Hash... | 10 | 4 | 22.2% | 0.8883 |
| ec6765c4 | Gather -> Aggregate -> Hash Join -> [Seq... | 10 | 4 | 15.9% | 0.6347 |
| a2a9b057 | Sort -> Aggregate -> Gather -> Aggregate... | 11 | 4 | 11.3% | 0.4519 |
| c65a77da | Aggregate -> Gather -> Aggregate -> Hash... | 11 | 4 | 22.2% | 0.8883 |
| ceeb5cca | Sort -> Aggregate -> Gather -> Aggregate... | 12 | 4 | 11.3% | 0.4519 |

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
| 4 | bb930825 | 172.9284 | -0.0000% | REJECTED | 17.92% |
| 5 | c0a8d3de | 6113.5159 | -0.0000% | REJECTED | 17.92% |
| 6 | 4fc84c77 | 13.3894 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 7 | 2e0f44ef | 108.1438 | 0.0001% | REJECTED | 17.92% |
| 8 | 37515ad8 | 168.3286 | -0.0000% | REJECTED | 17.92% |
| 9 | 634cdbe2 | 7.7175 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 10 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.92% |
| 11 | a5f39f08 | 12.4695 | 1.7095% | ACCEPTED | 16.21% |
| 12 | 7524c54c | 3.0007 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 13 | 422ae017 | 3.0007 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 14 | b3a45093 | 2.7998 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 15 | efde8b38 | 1.7942 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 16 | 444761fb | 24.3176 | 0.0000% | REJECTED | 16.21% |
| 17 | 310134da | 1.7942 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 18 | ec92bdaa | 15.1555 | -0.0000% | REJECTED | 16.21% |
| 19 | 7d4e78be | 89.9904 | 0.0000% | REJECTED | 16.21% |
| 20 | 30d6e09b | 89.9904 | 0.0000% | REJECTED | 16.21% |
| 21 | 2873b8c3 | 94.8003 | 0.0000% | REJECTED | 16.21% |
| 22 | 7a51ce50 | 89.9904 | 0.0000% | REJECTED | 16.21% |
| 23 | 1a17c7f7 | 18.3606 | N/A | REJECTED | 16.21% |
| 24 | 6e659102 | 1.3924 | N/A | SKIPPED_LOW_ERROR | 16.21% |
| 25 | e941d0ad | 4.5998 | N/A | REJECTED | 16.21% |
| 26 | fee45978 | 18.3606 | N/A | REJECTED | 16.21% |
| 27 | 49ae7e42 | 4.5998 | N/A | REJECTED | 16.21% |
| 28 | 702e1a46 | 18.3606 | N/A | REJECTED | 16.21% |
| 29 | ed7f2e45 | 4.5998 | N/A | REJECTED | 16.21% |
| 30 | 8951754f | 0.4452 | 0.1245% | REJECTED | 16.21% |
| 31 | 06fbc794 | 3.5767 | N/A | REJECTED | 16.21% |
| 32 | e92539ee | 0.4452 | 0.1245% | REJECTED | 16.21% |
| 33 | d0331b81 | 0.7918 | 0.0191% | REJECTED | 16.21% |
| 34 | 9adbbadc | 1.9173 | N/A | REJECTED | 16.21% |
| 35 | 59d2ec49 | 3.5767 | N/A | REJECTED | 16.21% |
| 36 | fa5db8b6 | 0.4452 | 0.1245% | REJECTED | 16.21% |
| 37 | 2bac8e6e | 0.7918 | 0.0191% | REJECTED | 16.21% |
| 38 | 9a16eb41 | 1.9173 | N/A | REJECTED | 16.21% |
| 39 | d8ffcf0c | 3.5767 | N/A | REJECTED | 16.21% |
| 40 | 57d290cd | 0.4452 | 0.1245% | REJECTED | 16.21% |
| 41 | 8259bae3 | 0.7918 | 0.0191% | REJECTED | 16.21% |
| 42 | f01db5fe | 1.9173 | N/A | REJECTED | 16.21% |
| 43 | 6e9566a0 | 0.4452 | 0.1245% | REJECTED | 16.21% |
| 44 | 4021e47f | 0.7918 | 0.0191% | REJECTED | 16.21% |
| 45 | 5968661e | 0.4452 | 0.1245% | REJECTED | 16.21% |
| 46 | 45a78037 | 0.7918 | 0.0191% | REJECTED | 16.21% |
| 47 | a2a9b057 | 0.4452 | 0.1245% | REJECTED | 16.21% |
| 48 | c65a77da | 0.7918 | 0.0191% | REJECTED | 16.21% |
| 49 | ceeb5cca | 0.4452 | 0.1245% | REJECTED | 16.21% |
## Query Tree

```
Node 17465 (Sort) - ROOT
  Node 17466 (Aggregate) [PATTERN: a5f39f08]
    Node 17467 (Gather) [consumed]
      Node 17468 (Aggregate) [consumed]
        Node 17469 (Hash Join)
          Node 17470 (Seq Scan) - LEAF
          Node 17471 (Hash)
            Node 17472 (Hash Join)
              Node 17473 (Seq Scan) - LEAF
              Node 17474 (Hash)
                Node 17475 (Hash Join)
                  Node 17476 (Hash Join)
                    Node 17477 (Nested Loop)
                      Node 17478 (Seq Scan) - LEAF
                      Node 17479 (Index Scan) - LEAF
                    Node 17480 (Hash)
                      Node 17481 (Seq Scan) - LEAF
                  Node 17482 (Hash)
                    Node 17483 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather -> Aggrega | a5f39f08 | 17466 | 17467, 17468 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 9.59%
- Improvement: 0.67%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 17465 | Sort | 1267.52 | 1146.02 | 9.6% | operator |
| 17466 | Aggregate | 1267.41 | 1077.54 | 15.0% | pattern |
| 17469 | Hash Join | 1217.82 | 653.52 | 46.3% | operator |
| 17470 | Seq Scan | 128.24 | 192.19 | 49.9% | operator |
| 17471 | Hash | 1027.13 | 134.12 | 86.9% | operator |
| 17472 | Hash Join | 1009.45 | 832.17 | 17.6% | operator |
| 17473 | Seq Scan | 686.94 | 565.06 | 17.7% | operator |
| 17474 | Hash | 206.55 | 53.17 | 74.3% | operator |
| 17475 | Hash Join | 203.95 | 914.01 | 348.2% | operator |
| 17476 | Hash Join | 188.01 | 852.61 | 353.5% | operator |
| 17482 | Hash | 15.04 | 14.54 | 3.3% | operator |
| 17477 | Nested Loop | 183.00 | 1067.12 | 483.1% | operator |
| 17480 | Hash | 2.51 | 14.79 | 489.6% | operator |
| 17483 | Seq Scan | 15.03 | 7.19 | 52.1% | operator |
| 17478 | Seq Scan | 26.21 | 42.55 | 62.3% | operator |
| 17479 | Index Scan | 0.06 | 0.12 | 109.0% | operator |
| 17481 | Seq Scan | 2.06 | 10.62 | 416.1% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 17478 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=5511
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0276
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=0.41, rt=42.55

### Step 2: Node 17479 (Index Scan) - LEAF

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
  - total_cost=1.7700
- **Output:** st=0.07, rt=0.12

### Step 3: Node 17481 (Seq Scan) - LEAF

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

### Step 4: Node 17477 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=22043
  - nt1=5511
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=42.5529
  - rt2=0.1192
  - sel=1.0000
  - st1=0.4075
  - st2=0.0716
  - startup_cost=0.4200
  - total_cost=15123.1100
- **Output:** st=3.78, rt=1067.12

### Step 5: Node 17480 (Hash)

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

### Step 6: Node 17483 (Seq Scan) - LEAF

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

### Step 7: Node 17476 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=22043
  - nt1=22043
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1067.1177
  - rt2=14.7884
  - sel=0.0001
  - st1=3.7816
  - st2=14.7887
  - startup_cost=448.4300
  - total_cost=15628.9900
- **Output:** st=52.58, rt=852.61

### Step 8: Node 17482 (Hash)

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

### Step 9: Node 17475 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=22043
  - nt1=22043
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=852.6072
  - rt2=14.5397
  - sel=0.0400
  - st1=52.5788
  - st2=14.5393
  - startup_cost=449.9900
  - total_cost=15698.2300
- **Output:** st=40.68, rt=914.01

### Step 10: Node 17473 (Seq Scan) - LEAF

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

### Step 11: Node 17474 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=22043
  - nt1=22043
  - nt2=0
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=914.0091
  - rt2=0.0000
  - sel=1.0000
  - st1=40.6798
  - st2=0.0000
  - startup_cost=15698.2300
  - total_cost=15698.2300
- **Output:** st=53.17, rt=53.17

### Step 12: Node 17472 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=79372
  - nt1=1200243
  - nt2=22043
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=565.0624
  - rt2=53.1730
  - sel=0.0000
  - st1=0.9985
  - st2=53.1722
  - startup_cost=16028.8800
  - total_cost=149633.2600
- **Output:** st=168.13, rt=832.17

### Step 13: Node 17470 (Seq Scan) - LEAF

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

### Step 14: Node 17471 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=79372
  - nt1=79372
  - nt2=0
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=832.1743
  - rt2=0.0000
  - sel=1.0000
  - st1=168.1255
  - st2=0.0000
  - startup_cost=149633.2600
  - total_cost=149633.2600
- **Output:** st=134.12, rt=134.12

### Step 15: Node 17469 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=128019
  - nt1=483871
  - nt2=79372
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=192.1919
  - rt2=134.1174
  - sel=0.0000
  - st1=0.1717
  - st2=134.1163
  - startup_cost=150625.4100
  - total_cost=183990.7200
- **Output:** st=107.74, rt=653.52

### Step 16: Node 17466 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** a5f39f08 (Aggregate -> Gather -> Aggregate (Outer) (Outer))
- **Consumes:** Nodes 17467, 17468
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=60150
  - Aggregate_Outer_nt1=128019
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=168
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.4699
  - Aggregate_Outer_startup_cost=186231.0600
  - Aggregate_Outer_total_cost=187133.3100
  - Aggregate_np=0
  - Aggregate_nt=60150
  - Aggregate_nt1=180450
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=168
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.3333
  - Aggregate_startup_cost=207982.8100
  - Aggregate_total_cost=208885.0600
  - Gather_Outer_np=0
  - Gather_Outer_nt=180450
  - Gather_Outer_nt1=60150
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=168
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.0000
  - Gather_Outer_startup_cost=187231.0600
  - Gather_Outer_total_cost=206178.3100
- **Output:** st=1072.04, rt=1077.54

### Step 17: Node 17465 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=60150
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=1077.5418
  - rt2=0.0000
  - sel=1.0000
  - st1=1072.0361
  - st2=0.0000
  - startup_cost=213659.8500
  - total_cost=213810.2200
- **Output:** st=1143.59, rt=1146.02
