# Online Prediction Report

**Test Query:** Q9_62_seed_500445891
**Timestamp:** 2026-01-01 20:52:31

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 11.17%

## Phase C: Patterns in Query

- Total Patterns: 64

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 33781.0% | 113504.2307 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 172 | 3565.0% | 6131.8766 |
| c0a8d3de | Hash -> Hash Join -> [Seq Scan (Outer), ... | 3 | 148 | 4130.8% | 6113.5159 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 148 | 116.8% | 172.9284 |
| 37515ad8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 124 | 135.7% | 168.3286 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 147.6% | 141.6847 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 75.1% | 108.1438 |
| 2873b8c3 | Hash Join -> [Nested Loop -> [Seq Scan (... | 3 | 48 | 197.5% | 94.8003 |
| 30d6e09b | Hash Join -> [Hash Join -> [Nested Loop ... | 3 | 48 | 187.5% | 89.9904 |
| 7a51ce50 | Hash Join -> [Hash Join -> [Nested Loop ... | 4 | 48 | 187.5% | 89.9904 |
| 7d4e78be | Hash Join -> [Hash Join (Outer), Hash (I... | 2 | 48 | 187.5% | 89.9904 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 444761fb | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 52 | 46.8% | 24.3176 |
| 1a17c7f7 | Hash -> Hash Join -> [Hash Join (Outer),... | 3 | 24 | 76.5% | 18.3606 |
| 702e1a46 | Hash -> Hash Join -> [Hash Join -> [Nest... | 5 | 24 | 76.5% | 18.3606 |
| fee45978 | Hash -> Hash Join -> [Hash Join -> [Nest... | 4 | 24 | 76.5% | 18.3606 |
| ec92bdaa | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 52 | 29.1% | 15.1555 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 9.3% | 13.3894 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 96 | 13.0% | 12.4695 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 96 | 8.0% | 7.7175 |
| 310134da | Aggregate -> Gather -> Aggregate -> Hash... | 5 | 52 | 10.3% | 5.3353 |
| efde8b38 | Aggregate -> Gather -> Aggregate -> Hash... | 4 | 52 | 10.3% | 5.3353 |
| 422ae017 | Aggregate -> Hash Join -> [Seq Scan (Out... | 3 | 76 | 6.9% | 5.2190 |
| 7524c54c | Aggregate -> Hash Join (Outer) | 2 | 76 | 6.9% | 5.2190 |
| 49ae7e42 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 24 | 19.2% | 4.5998 |
| e941d0ad | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 24 | 19.2% | 4.5998 |
| ed7f2e45 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 24 | 19.2% | 4.5998 |
| 06fbc794 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 5 | 4 | 89.4% | 3.5767 |
| 59d2ec49 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 6 | 4 | 89.4% | 3.5767 |
| d8ffcf0c | Hash -> Hash Join -> [Seq Scan (Outer), ... | 7 | 4 | 89.4% | 3.5767 |
| 2e8f3f67 | Gather -> Aggregate -> Hash Join (Outer)... | 3 | 52 | 6.8% | 3.5252 |
| af27a52b | Gather -> Aggregate -> Hash Join -> [Seq... | 4 | 52 | 6.8% | 3.5252 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 72 | 4.0% | 2.9042 |
| 9a16eb41 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 7 | 4 | 47.9% | 1.9173 |
| 9adbbadc | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 4 | 47.9% | 1.9173 |
| f01db5fe | Hash Join -> [Seq Scan (Outer), Hash -> ... | 8 | 4 | 47.9% | 1.9173 |
| 6e659102 | Sort -> Aggregate -> Gather -> Aggregate... | 4 | 24 | 6.2% | 1.4968 |
| 2bac8e6e | Aggregate -> Gather -> Aggregate -> Hash... | 7 | 4 | 22.2% | 0.8883 |
| 4021e47f | Aggregate -> Gather -> Aggregate -> Hash... | 9 | 4 | 22.2% | 0.8883 |
| 45a78037 | Aggregate -> Gather -> Aggregate -> Hash... | 10 | 4 | 22.2% | 0.8883 |
| 8259bae3 | Aggregate -> Gather -> Aggregate -> Hash... | 8 | 4 | 22.2% | 0.8883 |
| c65a77da | Aggregate -> Gather -> Aggregate -> Hash... | 11 | 4 | 22.2% | 0.8883 |
| d0331b81 | Aggregate -> Gather -> Aggregate -> Hash... | 6 | 4 | 22.2% | 0.8883 |
| 5891ae15 | Aggregate -> Hash Join -> [Seq Scan (Out... | 5 | 4 | 22.0% | 0.8805 |
| 6b3fb960 | Aggregate -> Hash Join -> [Seq Scan (Out... | 7 | 4 | 22.0% | 0.8805 |
| 7542faeb | Aggregate -> Hash Join -> [Seq Scan (Out... | 4 | 4 | 22.0% | 0.8805 |
| 800ae9e1 | Aggregate -> Hash Join -> [Seq Scan (Out... | 9 | 4 | 22.0% | 0.8805 |
| c57cb4bb | Aggregate -> Hash Join -> [Seq Scan (Out... | 6 | 4 | 22.0% | 0.8805 |
| d3455a22 | Aggregate -> Hash Join -> [Seq Scan (Out... | 8 | 4 | 22.0% | 0.8805 |
| 10ed8951 | Gather -> Aggregate -> Hash Join -> [Seq... | 5 | 4 | 15.9% | 0.6347 |
| 2eaabdb6 | Gather -> Aggregate -> Hash Join -> [Seq... | 7 | 4 | 15.9% | 0.6347 |
| 4ecd02f7 | Gather -> Aggregate -> Hash Join -> [Seq... | 6 | 4 | 15.9% | 0.6347 |
| 9627c015 | Gather -> Aggregate -> Hash Join -> [Seq... | 9 | 4 | 15.9% | 0.6347 |
| eb55f880 | Gather -> Aggregate -> Hash Join -> [Seq... | 8 | 4 | 15.9% | 0.6347 |
| ec6765c4 | Gather -> Aggregate -> Hash Join -> [Seq... | 10 | 4 | 15.9% | 0.6347 |
| 57d290cd | Sort -> Aggregate -> Gather -> Aggregate... | 8 | 4 | 11.3% | 0.4519 |
| 5968661e | Sort -> Aggregate -> Gather -> Aggregate... | 10 | 4 | 11.3% | 0.4519 |
| 6e9566a0 | Sort -> Aggregate -> Gather -> Aggregate... | 9 | 4 | 11.3% | 0.4519 |
| 8951754f | Sort -> Aggregate -> Gather -> Aggregate... | 5 | 4 | 11.3% | 0.4519 |
| a2a9b057 | Sort -> Aggregate -> Gather -> Aggregate... | 11 | 4 | 11.3% | 0.4519 |
| ceeb5cca | Sort -> Aggregate -> Gather -> Aggregate... | 12 | 4 | 11.3% | 0.4519 |
| e92539ee | Sort -> Aggregate -> Gather -> Aggregate... | 6 | 4 | 11.3% | 0.4519 |
| fa5db8b6 | Sort -> Aggregate -> Gather -> Aggregate... | 7 | 4 | 11.3% | 0.4519 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 1 | 895c6e8c | 75736.1626 | 0.0004% | ACCEPTED | 17.92% |
| 2 | 7df893ad | 678.6757 | N/A | REJECTED | 17.92% |
| 3 | c0a8d3de | 583.9768 | 0.0000% | ACCEPTED | 17.92% |
| 4 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.92% |
| 5 | 2e0f44ef | 108.1444 | 0.0001% | ACCEPTED | 17.92% |
| 6 | 2873b8c3 | 121.6368 | 0.0000% | ACCEPTED | 17.92% |
| 7 | bb930825 | 57.0004 | -0.0000% | REJECTED | 17.92% |
| 8 | 37515ad8 | 50.1314 | -0.0000% | REJECTED | 17.92% |
| 9 | 30d6e09b | 42.9691 | N/A | REJECTED | 17.92% |
| 10 | 7a51ce50 | 42.9691 | 0.0000% | ACCEPTED | 17.92% |
| 11 | 7d4e78be | 59.2266 | N/A | REJECTED | 17.92% |
| 12 | 1d35fb97 | 26.4006 | 0.1163% | ACCEPTED | 17.81% |
| 13 | 4fc84c77 | 15.8328 | 0.6911% | ACCEPTED | 17.12% |
| 14 | ec92bdaa | 15.2103 | N/A | REJECTED | 17.12% |
| 15 | 634cdbe2 | 9.1862 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 16 | 2e8f3f67 | 8.2514 | -0.7238% | REJECTED | 17.12% |
| 17 | af27a52b | 8.2514 | -0.7236% | REJECTED | 17.12% |
| 18 | 49ae7e42 | 7.4970 | N/A | REJECTED | 17.12% |
| 19 | e941d0ad | 7.4970 | N/A | REJECTED | 17.12% |
| 20 | ed7f2e45 | 7.4970 | N/A | REJECTED | 17.12% |
| 21 | a5f39f08 | 7.4593 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 22 | 444761fb | 6.7516 | N/A | REJECTED | 17.12% |
| 23 | 422ae017 | 4.9975 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 24 | 7524c54c | 4.9975 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 25 | 06fbc794 | 3.8679 | N/A | REJECTED | 17.12% |
| 26 | 59d2ec49 | 3.8679 | N/A | REJECTED | 17.12% |
| 27 | d8ffcf0c | 3.8679 | N/A | REJECTED | 17.12% |
| 28 | 310134da | 3.2490 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 29 | efde8b38 | 3.2490 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 30 | b3a45093 | 2.3813 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 31 | 6e659102 | 1.9242 | N/A | SKIPPED_LOW_ERROR | 17.12% |
| 32 | 9a16eb41 | 1.9221 | N/A | REJECTED | 17.12% |
| 33 | 9adbbadc | 1.9221 | N/A | REJECTED | 17.12% |
| 34 | f01db5fe | 1.9221 | N/A | REJECTED | 17.12% |
| 35 | 5891ae15 | 0.8807 | N/A | REJECTED | 17.12% |
| 36 | 6b3fb960 | 0.8807 | N/A | REJECTED | 17.12% |
| 37 | 7542faeb | 0.8807 | N/A | REJECTED | 17.12% |
| 38 | 800ae9e1 | 0.8807 | N/A | REJECTED | 17.12% |
| 39 | c57cb4bb | 0.8807 | N/A | REJECTED | 17.12% |
| 40 | d3455a22 | 0.8807 | N/A | REJECTED | 17.12% |
| 41 | 10ed8951 | 0.6347 | N/A | REJECTED | 17.12% |
| 42 | 2eaabdb6 | 0.6347 | N/A | REJECTED | 17.12% |
| 43 | 4ecd02f7 | 0.6347 | N/A | REJECTED | 17.12% |
| 44 | 9627c015 | 0.6347 | N/A | REJECTED | 17.12% |
| 45 | eb55f880 | 0.6347 | N/A | REJECTED | 17.12% |
| 46 | ec6765c4 | 0.6347 | N/A | REJECTED | 17.12% |
| 47 | 57d290cd | 0.4966 | 0.1398% | ACCEPTED | 16.98% |
| 48 | 5968661e | 0.0267 | N/A | SKIPPED_LOW_ERROR | 16.98% |
| 49 | 6e9566a0 | 0.0267 | N/A | SKIPPED_LOW_ERROR | 16.98% |
| 50 | 8951754f | 0.0267 | N/A | SKIPPED_LOW_ERROR | 16.98% |
| 51 | a2a9b057 | 0.0267 | N/A | SKIPPED_LOW_ERROR | 16.98% |
| 52 | ceeb5cca | 0.0267 | N/A | SKIPPED_LOW_ERROR | 16.98% |
| 53 | e92539ee | 0.0267 | N/A | SKIPPED_LOW_ERROR | 16.98% |
| 54 | fa5db8b6 | 0.0267 | N/A | SKIPPED_LOW_ERROR | 16.98% |
## Query Tree

```
Node 18606 (Sort) [PATTERN: 57d290cd] - ROOT
  Node 18607 (Aggregate) [consumed]
    Node 18608 (Gather) [consumed]
      Node 18609 (Aggregate) [consumed]
        Node 18610 (Hash Join) [consumed]
          Node 18611 (Seq Scan) [consumed] - LEAF
          Node 18612 (Hash) [consumed]
            Node 18613 (Hash Join) [consumed]
              Node 18614 (Seq Scan) [consumed] - LEAF
              Node 18615 (Hash) [consumed]
                Node 18616 (Hash Join) [PATTERN: 7a51ce50]
                  Node 18617 (Hash Join) [consumed]
                    Node 18618 (Nested Loop) [consumed]
                      Node 18619 (Seq Scan) [consumed] - LEAF
                      Node 18620 (Index Scan) [consumed] - LEAF
                    Node 18621 (Hash) [consumed]
                      Node 18622 (Seq Scan) [consumed] - LEAF
                  Node 18623 (Hash) [consumed]
                    Node 18624 (Seq Scan) [consumed] - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Sort -> Aggregate -> Gather -> | 57d290cd | 18606 | 18607, 18608, 18609, 18610, 18611, 18612, 18613, 18614, 18615, 18616, 18617, 18618, 18619, 18620, 18621, 18622, 18623, 18624 |
| Hash Join -> [Hash Join -> [Ne | 7a51ce50 | 18616 | 18606, 18607, 18608, 18609, 18610, 18611, 18612, 18613, 18614, 18615, 18617, 18618, 18619, 18620, 18621, 18622, 18623, 18624 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 0.20%
- Improvement: 10.98%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 18606 | Sort | 1280.63 | 1278.10 | 0.2% | pattern |
| 18616 | Hash Join | 218.66 | 547.61 | 150.4% | pattern |

## Prediction Chain (Bottom-Up)

### Step 1: Node 18616 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 7a51ce50 (Hash Join -> [Hash Join -> [Nested Loop -> [Seq Scan (Outer), Index Scan (Inner)] (Outer), Hash -> Seq Scan (Outer) (Inner)] (Outer), Hash -> Seq Scan (Outer) (Inner)])
- **Consumes:** Nodes 18606, 18607, 18608, 18609, 18610, 18611, 18612, 18613, 18614, 18615, 18617, 18618, 18619, 18620, 18621, 18622, 18623, 18624
- **Input Features:**
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=22043
  - HashJoin_Outer_nt1=22043
  - HashJoin_Outer_nt2=10000
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=26
  - HashJoin_Outer_reltuples=0.0000
  - HashJoin_Outer_sel=0.0001
  - HashJoin_Outer_startup_cost=448.4300
  - HashJoin_Outer_total_cost=15628.9900
  - HashJoin_np=0
  - HashJoin_nt=22043
  - HashJoin_nt1=22043
  - HashJoin_nt2=25
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=126
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0400
  - HashJoin_startup_cost=449.9900
  - HashJoin_total_cost=15698.2300
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
  - IndexScan_Inner_np=17560
  - IndexScan_Inner_nt=4
  - IndexScan_Inner_nt1=0
  - IndexScan_Inner_nt2=0
  - IndexScan_Inner_parallel_workers=0
  - IndexScan_Inner_plan_width=14
  - IndexScan_Inner_reltuples=800000.0000
  - IndexScan_Inner_sel=0.0000
  - IndexScan_Inner_startup_cost=0.4200
  - IndexScan_Inner_total_cost=1.7700
  - NestedLoop_Outer_np=0
  - NestedLoop_Outer_nt=22043
  - NestedLoop_Outer_nt1=5511
  - NestedLoop_Outer_nt2=4
  - NestedLoop_Outer_parallel_workers=0
  - NestedLoop_Outer_plan_width=18
  - NestedLoop_Outer_reltuples=0.0000
  - NestedLoop_Outer_sel=1.0000
  - NestedLoop_Outer_startup_cost=0.4200
  - NestedLoop_Outer_total_cost=15123.1100
  - SeqScan_Outer_np=223
  - SeqScan_Outer_nt=10000
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=8
  - SeqScan_Outer_reltuples=10000.0000
  - SeqScan_Outer_sel=1.0000
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=323.0000
- **Output:** st=18.67, rt=547.61

### Step 2: Node 18606 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 57d290cd (Sort -> Aggregate -> Gather -> Aggregate -> Hash Join -> [Seq Scan (Outer), Hash -> Hash Join -> [Seq Scan (Outer), Hash (Inner)] (Outer) (Inner)] (Outer) (Outer) (Outer) (Outer))
- **Consumes:** Nodes 18607, 18608, 18609, 18610, 18611, 18612, 18613, 18614, 18615, 18616, 18617, 18618, 18619, 18620, 18621, 18622, 18623, 18624
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
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=79372
  - HashJoin_Outer_nt1=1200243
  - HashJoin_Outer_nt2=22043
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=131
  - HashJoin_Outer_reltuples=0.0000
  - HashJoin_Outer_sel=0.0000
  - HashJoin_Outer_startup_cost=16028.8800
  - HashJoin_Outer_total_cost=149633.2600
  - Hash_Inner_np=0
  - Hash_Inner_nt=22043
  - Hash_Inner_nt1=22043
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=126
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=15698.2300
  - Hash_Inner_total_cost=15698.2300
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
  - Sort_np=0
  - Sort_nt=60150
  - Sort_nt1=60150
  - Sort_nt2=0
  - Sort_parallel_workers=0
  - Sort_plan_width=168
  - Sort_reltuples=0.0000
  - Sort_sel=1.0000
  - Sort_startup_cost=213659.8500
  - Sort_total_cost=213810.2200
- **Output:** st=1272.14, rt=1278.10
