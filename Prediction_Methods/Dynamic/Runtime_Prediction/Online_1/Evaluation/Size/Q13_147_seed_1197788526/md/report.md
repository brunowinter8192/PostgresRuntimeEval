# Online Prediction Report

**Test Query:** Q13_147_seed_1197788526
**Timestamp:** 2026-01-18 19:56:38

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 18611 | Operator + Pattern Training |
| Training_Test | 4658 | Pattern Selection Eval |
| Training | 23269 | Final Model Training |
| Test | 1050 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 21.43%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 210 | 13.3% | 28.0303 |
| 7524c54c | Aggregate -> Hash Join (Outer) | 2 | 68 | 8.3% | 5.6254 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 428 | 18066.2% | 77323.2906 |
| 422ae017 | Aggregate -> Hash Join -> [Seq Scan (Out... | 3 | 68 | 8.3% | 5.6254 |
| 35ffb644 | Sort -> Aggregate -> Aggregate (Outer) (... | 3 | 0 | - | - |
| 46baed7f | Sort -> Aggregate -> Aggregate -> Hash J... | 4 | 0 | - | - |
| a396b865 | Sort -> Aggregate -> Aggregate -> Hash J... | 5 | 0 | - | - |
| f592ee11 | Sort -> Aggregate -> Aggregate -> Hash J... | 6 | 0 | - | - |
| 3d5edd2b | Aggregate -> Aggregate (Outer) | 2 | 0 | - | - |
| 57bf6442 | Aggregate -> Aggregate -> Hash Join (Out... | 3 | 0 | - | - |
| fc9b94fb | Aggregate -> Aggregate -> Hash Join -> [... | 4 | 0 | - | - |
| 32b96b54 | Aggregate -> Aggregate -> Hash Join -> [... | 5 | 0 | - | - |
| 5ad512ef | Aggregate -> Hash Join -> [Seq Scan (Out... | 4 | 0 | - | - |
| 24e458a8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 0 | - | - |
| deb558a9 | Hash -> Index Only Scan (Outer) | 2 | 0 | - | - |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 1d35fb97 | 28.0303 | 0.0561% | ACCEPTED | 17.01% |
| 1 | 7524c54c | 5.6254 | N/A | SKIPPED_LOW_ERROR | 17.01% |
| 2 | 895c6e8c | 77323.2906 | 0.0004% | ACCEPTED | 17.01% |
| 3 | 422ae017 | 5.6254 | N/A | SKIPPED_LOW_ERROR | 17.01% |
## Query Tree

```
Node 25727 (Sort) [PATTERN: 1d35fb97] - ROOT
  Node 25728 (Aggregate) [consumed]
    Node 25729 (Aggregate)
      Node 25730 (Hash Join) [PATTERN: 895c6e8c]
        Node 25731 (Seq Scan) [consumed] - LEAF
        Node 25732 (Hash) [consumed]
          Node 25733 (Index Only Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Sort -> Aggregate (Outer) | 1d35fb97 | 25727 | 25728, 25730, 25731, 25732 |
| Hash Join -> [Seq Scan (Outer) | 895c6e8c | 25730 | 25727, 25728, 25731, 25732 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 20.57%
- Improvement: 0.86%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 25727 | Sort | 895.70 | 1079.94 | 20.6% | pattern |
| 25729 | Aggregate | 889.59 | 999.76 | 12.4% | operator |
| 25730 | Hash Join | 681.43 | 470.31 | 31.0% | pattern |
| 25733 | Index Only Scan | 10.21 | 0.00 | 100.0% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 25733 (Index Only Scan) - LEAF

- **Source:** operator
- **Output:** st=0.00, rt=0.00

### Step 2: Node 25730 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 895c6e8c (Hash Join -> [Seq Scan (Outer), Hash (Inner)])
- **Consumes:** Nodes 25727, 25728, 25731, 25732
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=1487976
  - HashJoin_nt1=1487976
  - HashJoin_nt2=150000
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=8
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0000
  - HashJoin_startup_cost=4587.9200
  - HashJoin_total_cost=53379.9700
  - Hash_Inner_np=0
  - Hash_Inner_nt=150000
  - Hash_Inner_nt1=150000
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=4
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=2712.9200
  - Hash_Inner_total_cost=2712.9200
  - SeqScan_Outer_np=26136
  - SeqScan_Outer_nt=1487976
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=8
  - SeqScan_Outer_reltuples=1500000.0000
  - SeqScan_Outer_sel=0.9920
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=44886.0000
- **Output:** st=157.70, rt=470.31

### Step 3: Node 25729 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=150000
  - nt1=1487976
  - nt2=0
  - parallel_workers=0
  - plan_width=12
  - reltuples=0.0000
  - rt1=470.3112
  - rt2=0.0000
  - sel=0.1008
  - st1=157.7026
  - st2=0.0000
  - startup_cost=60819.8500
  - total_cost=62319.8500
- **Output:** st=908.26, rt=999.76

### Step 4: Node 25727 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 1d35fb97 (Sort -> Aggregate (Outer))
- **Consumes:** Nodes 25728, 25730, 25731, 25732
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=200
  - Aggregate_Outer_nt1=150000
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=16
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0013
  - Aggregate_Outer_startup_cost=64569.8500
  - Aggregate_Outer_total_cost=64571.8500
  - Sort_np=0
  - Sort_nt=200
  - Sort_nt1=200
  - Sort_nt2=0
  - Sort_parallel_workers=0
  - Sort_plan_width=16
  - Sort_reltuples=0.0000
  - Sort_sel=1.0000
  - Sort_startup_cost=64579.4900
  - Sort_total_cost=64579.9900
- **Output:** st=1078.70, rt=1079.94
