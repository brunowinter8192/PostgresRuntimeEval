# Online Prediction Report

**Test Query:** Q9_129_seed_1050115968
**Timestamp:** 2026-01-11 17:36:20

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 10.71%

## Phase C: Patterns in Query

- Total Patterns: 64

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 33781.0% | 113504.2307 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 172 | 3565.0% | 6131.8766 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 144 | 9.3% | 13.3894 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 96 | 8.0% | 7.7175 |
| 7524c54c | Aggregate -> Hash Join (Outer) | 2 | 76 | 6.9% | 5.2190 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 75.1% | 108.1438 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 96 | 13.0% | 12.4695 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 147.6% | 141.6847 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 72 | 4.0% | 2.9042 |
| 2e8f3f67 | Gather -> Aggregate -> Hash Join (Outer)... | 3 | 52 | 6.8% | 3.5252 |
| 7d4e78be | Hash Join -> [Hash Join (Outer), Hash (I... | 2 | 48 | 187.5% | 89.9904 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 148 | 116.8% | 172.9284 |
| c0a8d3de | Hash -> Hash Join -> [Seq Scan (Outer), ... | 3 | 148 | 4130.8% | 6113.5159 |
| 422ae017 | Aggregate -> Hash Join -> [Seq Scan (Out... | 3 | 76 | 6.9% | 5.2190 |
| efde8b38 | Aggregate -> Gather -> Aggregate -> Hash... | 4 | 52 | 10.3% | 5.3353 |
| 1a17c7f7 | Hash -> Hash Join -> [Hash Join (Outer),... | 3 | 24 | 76.5% | 18.3606 |
| 6e659102 | Sort -> Aggregate -> Gather -> Aggregate... | 4 | 24 | 6.2% | 1.4968 |
| 444761fb | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 52 | 46.8% | 24.3176 |
| af27a52b | Gather -> Aggregate -> Hash Join -> [Seq... | 4 | 52 | 6.8% | 3.5252 |
| 7542faeb | Aggregate -> Hash Join -> [Seq Scan (Out... | 4 | 4 | 22.0% | 0.8805 |
| 8951754f | Sort -> Aggregate -> Gather -> Aggregate... | 5 | 4 | 11.3% | 0.4519 |
| 37515ad8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 124 | 135.7% | 168.3286 |
| 310134da | Aggregate -> Gather -> Aggregate -> Hash... | 5 | 52 | 10.3% | 5.3353 |
| 2873b8c3 | Hash Join -> [Nested Loop -> [Seq Scan (... | 3 | 48 | 197.5% | 94.8003 |
| 30d6e09b | Hash Join -> [Hash Join -> [Nested Loop ... | 3 | 48 | 187.5% | 89.9904 |
| e941d0ad | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 24 | 19.2% | 4.5998 |
| 10ed8951 | Gather -> Aggregate -> Hash Join -> [Seq... | 5 | 4 | 15.9% | 0.6347 |
| ec92bdaa | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 52 | 29.1% | 15.1555 |
| fee45978 | Hash -> Hash Join -> [Hash Join -> [Nest... | 4 | 24 | 76.5% | 18.3606 |
| 06fbc794 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 5 | 4 | 89.4% | 3.5767 |
| 5891ae15 | Aggregate -> Hash Join -> [Seq Scan (Out... | 5 | 4 | 22.0% | 0.8805 |
| d0331b81 | Aggregate -> Gather -> Aggregate -> Hash... | 6 | 4 | 22.2% | 0.8883 |
| e92539ee | Sort -> Aggregate -> Gather -> Aggregate... | 6 | 4 | 11.3% | 0.4519 |
| 4ecd02f7 | Gather -> Aggregate -> Hash Join -> [Seq... | 6 | 4 | 15.9% | 0.6347 |
| c57cb4bb | Aggregate -> Hash Join -> [Seq Scan (Out... | 6 | 4 | 22.0% | 0.8805 |
| fa5db8b6 | Sort -> Aggregate -> Gather -> Aggregate... | 7 | 4 | 11.3% | 0.4519 |
| 7a51ce50 | Hash Join -> [Hash Join -> [Nested Loop ... | 4 | 48 | 187.5% | 89.9904 |
| 49ae7e42 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 24 | 19.2% | 4.5998 |
| 2bac8e6e | Aggregate -> Gather -> Aggregate -> Hash... | 7 | 4 | 22.2% | 0.8883 |
| 2eaabdb6 | Gather -> Aggregate -> Hash Join -> [Seq... | 7 | 4 | 15.9% | 0.6347 |
| 9adbbadc | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 4 | 47.9% | 1.9173 |
| 702e1a46 | Hash -> Hash Join -> [Hash Join -> [Nest... | 5 | 24 | 76.5% | 18.3606 |
| 57d290cd | Sort -> Aggregate -> Gather -> Aggregate... | 8 | 4 | 11.3% | 0.4519 |
| 59d2ec49 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 6 | 4 | 89.4% | 3.5767 |
| 6b3fb960 | Aggregate -> Hash Join -> [Seq Scan (Out... | 7 | 4 | 22.0% | 0.8805 |
| 8259bae3 | Aggregate -> Gather -> Aggregate -> Hash... | 8 | 4 | 22.2% | 0.8883 |
| 6e9566a0 | Sort -> Aggregate -> Gather -> Aggregate... | 9 | 4 | 11.3% | 0.4519 |
| eb55f880 | Gather -> Aggregate -> Hash Join -> [Seq... | 8 | 4 | 15.9% | 0.6347 |
| ed7f2e45 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 24 | 19.2% | 4.5998 |
| 4021e47f | Aggregate -> Gather -> Aggregate -> Hash... | 9 | 4 | 22.2% | 0.8883 |
| 9a16eb41 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 7 | 4 | 47.9% | 1.9173 |
| 5968661e | Sort -> Aggregate -> Gather -> Aggregate... | 10 | 4 | 11.3% | 0.4519 |
| d3455a22 | Aggregate -> Hash Join -> [Seq Scan (Out... | 8 | 4 | 22.0% | 0.8805 |
| d8ffcf0c | Hash -> Hash Join -> [Seq Scan (Outer), ... | 7 | 4 | 89.4% | 3.5767 |
| 9627c015 | Gather -> Aggregate -> Hash Join -> [Seq... | 9 | 4 | 15.9% | 0.6347 |
| 45a78037 | Aggregate -> Gather -> Aggregate -> Hash... | 10 | 4 | 22.2% | 0.8883 |
| f01db5fe | Hash Join -> [Seq Scan (Outer), Hash -> ... | 8 | 4 | 47.9% | 1.9173 |
| 800ae9e1 | Aggregate -> Hash Join -> [Seq Scan (Out... | 9 | 4 | 22.0% | 0.8805 |
| a2a9b057 | Sort -> Aggregate -> Gather -> Aggregate... | 11 | 4 | 11.3% | 0.4519 |
| ec6765c4 | Gather -> Aggregate -> Hash Join -> [Seq... | 10 | 4 | 15.9% | 0.6347 |
| c65a77da | Aggregate -> Gather -> Aggregate -> Hash... | 11 | 4 | 22.2% | 0.8883 |
| ceeb5cca | Sort -> Aggregate -> Gather -> Aggregate... | 12 | 4 | 11.3% | 0.4519 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 1 | 1d35fb97 | 26.4017 | 0.1167% | ACCEPTED | 17.81% |
| 2 | 7df893ad | 6131.8766 | 0.0000% | ACCEPTED | 17.81% |
| 3 | 4fc84c77 | 13.3894 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 4 | 634cdbe2 | 7.7175 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 5 | 7524c54c | 5.2190 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 6 | 895c6e8c | 75736.1626 | 0.0001% | ACCEPTED | 17.81% |
| 7 | 2e0f44ef | 108.1438 | 0.0001% | ACCEPTED | 17.81% |
| 8 | a5f39f08 | 12.4695 | 1.8366% | ACCEPTED | 15.97% |
| 9 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 15.97% |
| 10 | b3a45093 | 2.9042 | N/A | SKIPPED_LOW_ERROR | 15.97% |
| 11 | 2e8f3f67 | 3.5252 | N/A | SKIPPED_LOW_ERROR | 15.97% |
| 12 | 7d4e78be | 89.9904 | N/A | REJECTED | 15.97% |
| 13 | bb930825 | 172.9284 | -0.0000% | REJECTED | 15.97% |
| 14 | c0a8d3de | 6113.5159 | -0.0000% | REJECTED | 15.97% |
| 15 | 422ae017 | 5.2190 | N/A | SKIPPED_LOW_ERROR | 15.97% |
| 16 | efde8b38 | 5.3353 | 0.0189% | ACCEPTED | 15.95% |
| 17 | 1a17c7f7 | 18.3606 | N/A | REJECTED | 15.95% |
| 18 | 6e659102 | 1.4968 | N/A | SKIPPED_LOW_ERROR | 15.95% |
| 19 | 444761fb | 24.3176 | N/A | REJECTED | 15.95% |
| 20 | af27a52b | 3.5252 | N/A | SKIPPED_LOW_ERROR | 15.95% |
| 21 | 7542faeb | 0.8805 | N/A | REJECTED | 15.95% |
| 22 | 8951754f | 0.4519 | 0.1366% | ACCEPTED | 15.82% |
| 23 | 37515ad8 | 168.3286 | -0.0000% | REJECTED | 15.82% |
| 24 | 310134da | 5.3353 | 0.0003% | ACCEPTED | 15.81% |
| 25 | 2873b8c3 | 94.8003 | N/A | REJECTED | 15.81% |
| 26 | 30d6e09b | 89.9904 | N/A | REJECTED | 15.81% |
| 27 | e941d0ad | 4.5998 | N/A | REJECTED | 15.81% |
| 28 | 10ed8951 | 0.6347 | N/A | REJECTED | 15.81% |
| 29 | ec92bdaa | 15.1555 | N/A | REJECTED | 15.81% |
| 30 | fee45978 | 18.3606 | N/A | REJECTED | 15.81% |
| 31 | 06fbc794 | 3.5767 | N/A | REJECTED | 15.81% |
| 32 | 5891ae15 | 0.8805 | N/A | REJECTED | 15.81% |
| 33 | d0331b81 | 0.8883 | -0.1054% | REJECTED | 15.81% |
| 34 | e92539ee | 0.4519 | 0.0000% | ACCEPTED | 15.81% |
| 35 | 4ecd02f7 | 0.6347 | N/A | REJECTED | 15.81% |
| 36 | c57cb4bb | 0.8805 | N/A | REJECTED | 15.81% |
| 37 | fa5db8b6 | 0.4519 | -0.0000% | REJECTED | 15.81% |
| 38 | 7a51ce50 | 89.9904 | N/A | REJECTED | 15.81% |
| 39 | 49ae7e42 | 4.5998 | N/A | REJECTED | 15.81% |
| 40 | 2bac8e6e | 0.8883 | -0.1054% | REJECTED | 15.81% |
| 41 | 2eaabdb6 | 0.6347 | -0.1398% | REJECTED | 15.81% |
| 42 | 9adbbadc | 1.9173 | N/A | REJECTED | 15.81% |
| 43 | 702e1a46 | 18.3606 | N/A | REJECTED | 15.81% |
| 44 | 57d290cd | 0.4519 | -0.0000% | REJECTED | 15.81% |
| 45 | 59d2ec49 | 3.5767 | N/A | REJECTED | 15.81% |
| 46 | 6b3fb960 | 0.8805 | -0.1398% | REJECTED | 15.81% |
| 47 | 8259bae3 | 0.8883 | -0.1054% | REJECTED | 15.81% |
| 48 | 6e9566a0 | 0.4519 | -0.0000% | REJECTED | 15.81% |
| 49 | eb55f880 | 0.6347 | -0.1398% | REJECTED | 15.81% |
| 50 | ed7f2e45 | 4.5998 | N/A | REJECTED | 15.81% |
| 51 | 4021e47f | 0.8883 | -0.1054% | REJECTED | 15.81% |
| 52 | 9a16eb41 | 1.9173 | -0.1245% | REJECTED | 15.81% |
| 53 | 5968661e | 0.4519 | 0.0000% | ACCEPTED | 15.81% |
| 54 | d3455a22 | 0.8805 | N/A | REJECTED | 15.81% |
| 55 | d8ffcf0c | 3.5767 | N/A | REJECTED | 15.81% |
| 56 | 9627c015 | 0.6347 | N/A | REJECTED | 15.81% |
| 57 | 45a78037 | 0.8883 | N/A | REJECTED | 15.81% |
| 58 | f01db5fe | 1.9173 | N/A | REJECTED | 15.81% |
| 59 | 800ae9e1 | 0.8805 | N/A | REJECTED | 15.81% |
| 60 | a2a9b057 | 0.4519 | -0.0000% | REJECTED | 15.81% |
| 61 | ec6765c4 | 0.6347 | N/A | REJECTED | 15.81% |
| 62 | c65a77da | 0.8883 | -0.1055% | REJECTED | 15.81% |
| 63 | ceeb5cca | 0.4519 | -0.0000% | REJECTED | 15.81% |
## Query Tree

```
Node 17212 (Sort) [PATTERN: 5968661e] - ROOT
  Node 17213 (Aggregate) [consumed]
    Node 17214 (Gather) [consumed]
      Node 17215 (Aggregate) [consumed]
        Node 17216 (Hash Join) [consumed]
          Node 17217 (Seq Scan) [consumed] - LEAF
          Node 17218 (Hash) [consumed]
            Node 17219 (Hash Join) [consumed]
              Node 17220 (Seq Scan) [consumed] - LEAF
              Node 17221 (Hash) [consumed]
                Node 17222 (Hash Join) [consumed]
                  Node 17223 (Hash Join) [consumed]
                    Node 17224 (Nested Loop)
                      Node 17225 (Seq Scan) - LEAF
                      Node 17226 (Index Scan) - LEAF
                    Node 17227 (Hash)
                      Node 17228 (Seq Scan) - LEAF
                  Node 17229 (Hash) [consumed]
                    Node 17230 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Sort -> Aggregate -> Gather -> | 5968661e | 17212 | 17213, 17214, 17215, 17216, 17217, 17218, 17219, 17220, 17221, 17222, 17223, 17229 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 0.32%
- Improvement: 10.38%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 17212 | Sort | 1273.98 | 1278.10 | 0.3% | pattern |
| 17224 | Nested Loop | 192.94 | 1067.26 | 453.2% | operator |
| 17227 | Hash | 4.18 | 14.79 | 253.6% | operator |
| 17230 | Seq Scan | 14.19 | 7.19 | 49.3% | operator |
| 17225 | Seq Scan | 27.88 | 42.49 | 52.4% | operator |
| 17226 | Index Scan | 0.06 | 0.12 | 95.3% | operator |
| 17228 | Seq Scan | 3.77 | 10.62 | 181.5% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 17225 (Seq Scan) - LEAF

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

### Step 2: Node 17226 (Index Scan) - LEAF

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

### Step 3: Node 17228 (Seq Scan) - LEAF

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

### Step 4: Node 17224 (Nested Loop)

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

### Step 5: Node 17227 (Hash)

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

### Step 6: Node 17230 (Seq Scan) - LEAF

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

### Step 7: Node 17212 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 5968661e (Sort -> Aggregate -> Gather -> Aggregate -> Hash Join -> [Seq Scan (Outer), Hash -> Hash Join -> [Seq Scan (Outer), Hash -> Hash Join -> [Hash Join (Outer), Hash (Inner)] (Outer) (Inner)] (Outer) (Inner)] (Outer) (Outer) (Outer) (Outer))
- **Consumes:** Nodes 17213, 17214, 17215, 17216, 17217, 17218, 17219, 17220, 17221, 17222, 17223, 17229
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
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=22712
  - HashJoin_Outer_nt1=22712
  - HashJoin_Outer_nt2=10000
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=26
  - HashJoin_Outer_reltuples=0.0000
  - HashJoin_Outer_sel=0.0001
  - HashJoin_Outer_startup_cost=448.4300
  - HashJoin_Outer_total_cost=15774.1200
  - Hash_Inner_np=0
  - Hash_Inner_nt=25
  - Hash_Inner_nt1=25
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=108
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=1.2500
  - Hash_Inner_total_cost=1.2500
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
  - Sort_startup_cost=213932.5500
  - Sort_total_cost=214082.9300
- **Output:** st=1272.14, rt=1278.10
