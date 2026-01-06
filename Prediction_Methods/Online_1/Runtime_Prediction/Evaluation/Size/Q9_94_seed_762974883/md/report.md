# Online Prediction Report

**Test Query:** Q9_94_seed_762974883
**Timestamp:** 2026-01-01 18:48:36

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

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 33781.0% | 113504.2307 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 172 | 3565.0% | 6131.8766 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 9.3% | 13.3894 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 75.1% | 108.1438 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 96 | 8.0% | 7.7175 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 147.6% | 141.6847 |
| 7524c54c | Aggregate -> Hash Join (Outer) | 2 | 76 | 6.9% | 5.2190 |
| 7d4e78be | Hash Join -> [Hash Join (Outer), Hash (I... | 2 | 48 | 187.5% | 89.9904 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 148 | 116.8% | 172.9284 |
| c0a8d3de | Hash -> Hash Join -> [Seq Scan (Outer), ... | 3 | 148 | 4130.8% | 6113.5159 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 96 | 13.0% | 12.4695 |
| 422ae017 | Aggregate -> Hash Join -> [Seq Scan (Out... | 3 | 76 | 6.9% | 5.2190 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 72 | 4.0% | 2.9042 |
| 2e8f3f67 | Gather -> Aggregate -> Hash Join (Outer)... | 3 | 52 | 6.8% | 3.5252 |
| 30d6e09b | Hash Join -> [Hash Join -> [Nested Loop ... | 3 | 48 | 187.5% | 89.9904 |
| 2873b8c3 | Hash Join -> [Nested Loop -> [Seq Scan (... | 3 | 48 | 197.5% | 94.8003 |
| 1a17c7f7 | Hash -> Hash Join -> [Hash Join (Outer),... | 3 | 24 | 76.5% | 18.3606 |
| 37515ad8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 124 | 135.7% | 168.3286 |
| efde8b38 | Aggregate -> Gather -> Aggregate -> Hash... | 4 | 52 | 10.3% | 5.3353 |
| af27a52b | Gather -> Aggregate -> Hash Join -> [Seq... | 4 | 52 | 6.8% | 3.5252 |
| 444761fb | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 52 | 46.8% | 24.3176 |
| 7a51ce50 | Hash Join -> [Hash Join -> [Nested Loop ... | 4 | 48 | 187.5% | 89.9904 |
| 6e659102 | Sort -> Aggregate -> Gather -> Aggregate... | 4 | 24 | 6.2% | 1.4968 |
| e941d0ad | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 24 | 19.2% | 4.5998 |
| fee45978 | Hash -> Hash Join -> [Hash Join -> [Nest... | 4 | 24 | 76.5% | 18.3606 |
| 7542faeb | Aggregate -> Hash Join -> [Seq Scan (Out... | 4 | 4 | 22.0% | 0.8805 |
| 310134da | Aggregate -> Gather -> Aggregate -> Hash... | 5 | 52 | 10.3% | 5.3353 |
| ec92bdaa | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 52 | 29.1% | 15.1555 |
| 49ae7e42 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 24 | 19.2% | 4.5998 |
| 702e1a46 | Hash -> Hash Join -> [Hash Join -> [Nest... | 5 | 24 | 76.5% | 18.3606 |
| 8951754f | Sort -> Aggregate -> Gather -> Aggregate... | 5 | 4 | 11.3% | 0.4519 |
| 10ed8951 | Gather -> Aggregate -> Hash Join -> [Seq... | 5 | 4 | 15.9% | 0.6347 |
| 5891ae15 | Aggregate -> Hash Join -> [Seq Scan (Out... | 5 | 4 | 22.0% | 0.8805 |
| 06fbc794 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 5 | 4 | 89.4% | 3.5767 |
| ed7f2e45 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 24 | 19.2% | 4.5998 |
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
| 0 | 895c6e8c | 75736.1626 | 0.0004% | ACCEPTED | 17.92% |
| 1 | 3aab37be | 94712.4752 | -0.0000% | REJECTED | 17.92% |
| 2 | 1d35fb97 | 26.4006 | 0.1163% | ACCEPTED | 17.81% |
| 3 | 7df893ad | 678.6757 | N/A | REJECTED | 17.81% |
| 4 | 4fc84c77 | 15.8328 | 0.6911% | ACCEPTED | 17.12% |
| 5 | 2e0f44ef | 108.1433 | 0.0001% | ACCEPTED | 17.12% |
| 6 | 634cdbe2 | 9.1880 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 7 | c53c4396 | 8.0758 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 8 | 7524c54c | 5.0128 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 9 | 7d4e78be | 83.6779 | N/A | REJECTED | 17.12% |
| 10 | bb930825 | 188.3060 | N/A | REJECTED | 17.12% |
| 11 | a5f39f08 | 7.4593 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 12 | 422ae017 | 5.0128 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 13 | b3a45093 | 2.3813 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 14 | 2e8f3f67 | 8.2572 | -0.7238% | REJECTED | 17.12% |
| 15 | 30d6e09b | 83.6779 | N/A | REJECTED | 17.12% |
| 16 | 2873b8c3 | 121.6368 | N/A | REJECTED | 17.12% |
| 17 | 37515ad8 | 180.6991 | N/A | REJECTED | 17.12% |
| 18 | efde8b38 | 3.2490 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 19 | af27a52b | 8.2572 | -0.7236% | REJECTED | 17.12% |
| 20 | 7a51ce50 | 83.6779 | N/A | REJECTED | 17.12% |
| 21 | 6e659102 | 1.9242 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 22 | e941d0ad | 7.6069 | N/A | REJECTED | 17.12% |
| 23 | 7542faeb | 0.8960 | N/A | REJECTED | 17.12% |
| 24 | 310134da | 3.2490 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 25 | ec92bdaa | 20.9203 | N/A | REJECTED | 17.12% |
| 26 | 49ae7e42 | 7.6069 | N/A | REJECTED | 17.12% |
| 27 | 8951754f | 0.4966 | 0.1398% | ACCEPTED | 16.98% |
| 28 | c0a8d3de | 132.5174 | -0.0000% | REJECTED | 16.98% |
| 29 | 444761fb | 46.5602 | N/A | REJECTED | 16.98% |
| 30 | 06fbc794 | 3.5816 | N/A | REJECTED | 16.98% |
| 31 | ed7f2e45 | 7.6069 | N/A | REJECTED | 16.98% |
| 32 | e92539ee | 0.0267 | N/A | SKIPPED_LOW_ERROR | 16.98% |
| 33 | 59d2ec49 | 3.5816 | N/A | REJECTED | 16.98% |
| 34 | fa5db8b6 | 0.0267 | N/A | SKIPPED_LOW_ERROR | 16.98% |
| 35 | d8ffcf0c | 3.5816 | N/A | REJECTED | 16.98% |
| 36 | 57d290cd | 0.0267 | N/A | SKIPPED_LOW_ERROR | 16.98% |
| 37 | 6e9566a0 | 0.0267 | N/A | SKIPPED_LOW_ERROR | 16.98% |
| 38 | 5968661e | 0.0267 | N/A | SKIPPED_LOW_ERROR | 16.98% |
| 39 | a2a9b057 | 0.0267 | N/A | SKIPPED_LOW_ERROR | 16.98% |
| 40 | ceeb5cca | 0.0267 | N/A | SKIPPED_LOW_ERROR | 16.98% |
## Query Tree

```
Node 19243 (Sort) [PATTERN: 8951754f] - ROOT
  Node 19244 (Aggregate) [consumed]
    Node 19245 (Gather) [consumed]
      Node 19246 (Aggregate) [consumed]
        Node 19247 (Hash Join) [consumed]
          Node 19248 (Seq Scan) - LEAF
          Node 19249 (Hash)
            Node 19250 (Hash Join) [PATTERN: 895c6e8c]
              Node 19251 (Seq Scan) [consumed] - LEAF
              Node 19252 (Hash) [consumed]
                Node 19253 (Hash Join)
                  Node 19254 (Hash Join) [PATTERN: 2e0f44ef]
                    Node 19255 (Nested Loop) [consumed]
                      Node 19256 (Seq Scan) - LEAF
                      Node 19257 (Index Scan) - LEAF
                    Node 19258 (Hash) [consumed]
                      Node 19259 (Seq Scan) - LEAF
                  Node 19260 (Hash)
                    Node 19261 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Sort -> Aggregate -> Gather -> | 8951754f | 19243 | 19244, 19245, 19246, 19247, 19250, 19251, 19252, 19254, 19255, 19258 |
| Hash Join -> [Seq Scan (Outer) | 895c6e8c | 19250 | 19243, 19244, 19245, 19246, 19247, 19251, 19252, 19254, 19255, 19258 |
| Hash Join -> [Nested Loop (Out | 2e0f44ef | 19254 | 19243, 19244, 19245, 19246, 19247, 19250, 19251, 19252, 19255, 19258 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 0.77%
- Improvement: 10.92%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 19243 | Sort | 1287.96 | 1278.10 | 0.8% | pattern |
| 19248 | Seq Scan | 129.96 | 192.19 | 47.9% | operator |
| 19249 | Hash | 1041.70 | 132.35 | 87.3% | operator |
| 19250 | Hash Join | 1023.10 | 734.70 | 28.2% | pattern |
| 19253 | Hash Join | 211.09 | 821.11 | 289.0% | operator |
| 19254 | Hash Join | 195.55 | 981.16 | 401.7% | pattern |
| 19260 | Hash | 14.64 | 14.54 | 0.7% | operator |
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

### Step 4: Node 19261 (Seq Scan) - LEAF

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

### Step 5: Node 19254 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 2e0f44ef (Hash Join -> [Nested Loop (Outer), Hash (Inner)])
- **Consumes:** Nodes 19243, 19244, 19245, 19246, 19247, 19250, 19251, 19252, 19255, 19258
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=21377
  - HashJoin_nt1=21377
  - HashJoin_nt2=10000
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=26
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0001
  - HashJoin_startup_cost=448.4300
  - HashJoin_total_cost=15482.5600
  - Hash_Inner_np=0
  - Hash_Inner_nt=10000
  - Hash_Inner_nt1=10000
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=8
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=323.0000
  - Hash_Inner_total_cost=323.0000
  - NestedLoop_Outer_np=0
  - NestedLoop_Outer_nt=21377
  - NestedLoop_Outer_nt1=5344
  - NestedLoop_Outer_nt2=4
  - NestedLoop_Outer_parallel_workers=0
  - NestedLoop_Outer_plan_width=18
  - NestedLoop_Outer_reltuples=0.0000
  - NestedLoop_Outer_sel=1.0000
  - NestedLoop_Outer_startup_cost=0.4200
  - NestedLoop_Outer_total_cost=14978.4200
- **Output:** st=5.37, rt=981.16

### Step 6: Node 19260 (Hash)

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

### Step 7: Node 19253 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=21377
  - nt1=21377
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=981.1551
  - rt2=14.5397
  - sel=0.0400
  - st1=5.3651
  - st2=14.5393
  - startup_cost=449.9900
  - total_cost=15549.7500
- **Output:** st=26.58, rt=821.11

### Step 8: Node 19250 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 895c6e8c (Hash Join -> [Seq Scan (Outer), Hash (Inner)])
- **Consumes:** Nodes 19243, 19244, 19245, 19246, 19247, 19251, 19252, 19254, 19255, 19258
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=76972
  - HashJoin_nt1=1200243
  - HashJoin_nt2=21377
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=131
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0000
  - HashJoin_startup_cost=15870.4100
  - HashJoin_total_cost=149474.7900
  - Hash_Inner_np=0
  - Hash_Inner_nt=21377
  - Hash_Inner_nt1=21377
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=126
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=15549.7500
  - Hash_Inner_total_cost=15549.7500
  - SeqScan_Outer_np=112600
  - SeqScan_Outer_nt=1200243
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=29
  - SeqScan_Outer_reltuples=6001215.0000
  - SeqScan_Outer_sel=0.2000
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=124602.4300
- **Output:** st=176.07, rt=734.70

### Step 9: Node 19248 (Seq Scan) - LEAF

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

### Step 10: Node 19249 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=76972
  - nt1=76972
  - nt2=0
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=734.6992
  - rt2=0.0000
  - sel=1.0000
  - st1=176.0738
  - st2=0.0000
  - startup_cost=149474.7900
  - total_cost=149474.7900
- **Output:** st=132.35, rt=132.35

### Step 11: Node 19243 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 8951754f (Sort -> Aggregate -> Gather -> Aggregate -> Hash Join (Outer) (Outer) (Outer) (Outer))
- **Consumes:** Nodes 19244, 19245, 19246, 19247, 19250, 19251, 19252, 19254, 19255, 19258
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
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=124148
  - HashJoin_Outer_nt1=483871
  - HashJoin_Outer_nt2=76972
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=159
  - HashJoin_Outer_reltuples=0.0000
  - HashJoin_Outer_sel=0.0000
  - HashJoin_Outer_startup_cost=150436.9400
  - HashJoin_Outer_total_cost=183784.8300
  - Sort_np=0
  - Sort_nt=60150
  - Sort_nt1=60150
  - Sort_nt2=0
  - Sort_parallel_workers=0
  - Sort_plan_width=168
  - Sort_reltuples=0.0000
  - Sort_sel=1.0000
  - Sort_startup_cost=213386.2100
  - Sort_total_cost=213536.5900
- **Output:** st=1272.14, rt=1278.10
