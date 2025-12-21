# Online Prediction Report

**Test Query:** Q10_24_seed_188692713
**Timestamp:** 2025-12-21 17:37:11

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17891 | Operator + Pattern Training |
| Training_Test | 4478 | Pattern Selection Eval |
| Training | 22369 | Final Model Training |
| Test | 1950 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 82.72%

## Phase C: Patterns in Query

- Total Patterns: 29

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 360 | 34236.0% | 123249.7776 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 210 | 15.2% | 31.9214 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 150 | 10.6% | 15.8901 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 150 | 87.4% | 131.1122 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 90 | 195.4% | 175.8467 |
| e296a71f | Limit -> Sort (Outer) | 2 | 60 | 48.4% | 29.0440 |
| 7d4e78be | Hash Join -> [Hash Join (Outer), Hash (I... | 2 | 30 | 375.5% | 112.6472 |
| 7bcfec22 | Limit -> Sort -> Aggregate (Outer) (Oute... | 3 | 60 | 48.4% | 29.0440 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 60 | 5.3% | 3.1940 |
| 30d6e09b | Hash Join -> [Hash Join -> [Nested Loop ... | 3 | 30 | 375.5% | 112.6472 |
| 2873b8c3 | Hash Join -> [Nested Loop -> [Seq Scan (... | 3 | 30 | 391.6% | 117.4853 |
| 25df29b5 | Limit -> Sort -> Aggregate -> Gather (Ou... | 4 | 30 | 68.7% | 20.6018 |
| 7a51ce50 | Hash Join -> [Hash Join -> [Nested Loop ... | 4 | 30 | 375.5% | 112.6472 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 3aab37be | 123249.7776 | -0.0000% | REJECTED | 13.80% |
| 1 | 1d35fb97 | 31.9214 | 0.0688% | REJECTED | 13.80% |
| 2 | 4fc84c77 | 15.8901 | 1.8685% | ACCEPTED | 11.93% |
| 3 | 2e0f44ef | 131.1122 | 0.0001% | REJECTED | 11.93% |
| 4 | c53c4396 | 175.8467 | -0.0001% | REJECTED | 11.93% |
| 5 | e296a71f | 29.0436 | 0.0547% | REJECTED | 11.93% |
| 6 | 7d4e78be | 112.6472 | N/A | REJECTED | 11.93% |
| 7 | 7bcfec22 | 29.0436 | 0.0348% | REJECTED | 11.93% |
| 8 | b3a45093 | 2.9766 | N/A | SKIPPED_LOW_ERROR | 11.93% |
| 9 | 30d6e09b | 112.6472 | N/A | REJECTED | 11.93% |
| 10 | 2873b8c3 | 117.4853 | N/A | REJECTED | 11.93% |
| 11 | 25df29b5 | 20.6014 | 5.1752% | ACCEPTED | 6.76% |
| 12 | 7a51ce50 | 112.6472 | N/A | REJECTED | 6.76% |
## Query Tree

```
Node 20228 (Limit) [PATTERN: 25df29b5] - ROOT
  Node 20229 (Sort) [consumed]
    Node 20230 (Aggregate) [consumed]
      Node 20231 (Gather) [consumed]
        Node 20232 (Hash Join)
          Node 20233 (Hash Join)
            Node 20234 (Nested Loop)
              Node 20235 (Seq Scan) - LEAF
              Node 20236 (Index Scan) - LEAF
            Node 20237 (Hash)
              Node 20238 (Seq Scan) - LEAF
          Node 20239 (Hash)
            Node 20240 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Limit -> Sort -> Aggregate ->  | 25df29b5 | 20228 | 20229, 20230, 20231 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 3.20%
- Improvement: 79.52%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 20228 | Limit | 1162.32 | 1199.47 | 3.2% | pattern |
| 20232 | Hash Join | 1115.31 | 1007.32 | 9.7% | operator |
| 20233 | Hash Join | 1112.34 | 1004.29 | 9.7% | operator |
| 20239 | Hash | 0.02 | 15.71 | 82588.3% | operator |
| 20234 | Nested Loop | 1064.15 | 1204.75 | 13.2% | operator |
| 20237 | Hash | 36.93 | 55.57 | 50.5% | operator |
| 20240 | Seq Scan | 0.01 | 6.98 | 46424.7% | operator |
| 20235 | Seq Scan | 163.69 | 159.75 | 2.4% | operator |
| 20236 | Index Scan | 0.06 | -0.52 | 909.7% | operator |
| 20238 | Seq Scan | 24.88 | 26.64 | 7.1% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 20235 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=17945
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0120
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=33394.0600
- **Output:** st=-0.55, rt=159.75

### Step 2: Node 20236 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=1
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=16
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.4300
  - total_cost=2.3300
- **Output:** st=0.03, rt=-0.52

### Step 3: Node 20238 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=3600
  - nt=62500
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=148
  - reltuples=150000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.4167
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=4225.0000
- **Output:** st=-10.03, rt=26.64

### Step 4: Node 20234 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=17761
  - nt1=17945
  - nt2=1
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=159.7452
  - rt2=-0.5182
  - sel=0.9897
  - st1=-0.5500
  - st2=0.0265
  - startup_cost=0.4300
  - total_cost=75353.3500
- **Output:** st=124.80, rt=1204.75

### Step 5: Node 20237 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=62500
  - nt1=62500
  - nt2=0
  - parallel_workers=0
  - plan_width=148
  - reltuples=0.0000
  - rt1=26.6397
  - rt2=0.0000
  - sel=1.0000
  - st1=-10.0295
  - st2=0.0000
  - startup_cost=4225.0000
  - total_cost=4225.0000
- **Output:** st=55.57, rt=55.57

### Step 6: Node 20240 (Seq Scan) - LEAF

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
- **Output:** st=0.44, rt=6.98

### Step 7: Node 20233 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=17761
  - nt1=17761
  - nt2=62500
  - parallel_workers=0
  - plan_width=160
  - reltuples=0.0000
  - rt1=1204.7496
  - rt2=55.5689
  - sel=0.0000
  - st1=124.7980
  - st2=55.5682
  - startup_cost=5006.6800
  - total_cost=80406.2200
- **Output:** st=109.67, rt=1004.29

### Step 8: Node 20239 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=25
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=6.9787
  - rt2=0.0000
  - sel=1.0000
  - st1=0.4364
  - st2=0.0000
  - startup_cost=1.2500
  - total_cost=1.2500
- **Output:** st=15.71, rt=15.71

### Step 9: Node 20232 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=17761
  - nt1=17761
  - nt2=25
  - parallel_workers=0
  - plan_width=260
  - reltuples=0.0000
  - rt1=1004.2851
  - rt2=15.7108
  - sel=0.0400
  - st1=109.6744
  - st2=15.7100
  - startup_cost=5008.2400
  - total_cost=80462.3100
- **Output:** st=98.87, rt=1007.32

### Step 10: Node 20228 (Limit) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 25df29b5 (Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer))
- **Consumes:** Nodes 20229, 20230, 20231
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=55059
  - Aggregate_Outer_nt1=55059
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=280
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=1.0000
  - Aggregate_Outer_startup_cost=87656.4500
  - Aggregate_Outer_total_cost=88344.6800
  - Gather_Outer_np=0
  - Gather_Outer_nt=55059
  - Gather_Outer_nt1=17761
  - Gather_Outer_nt2=0
  - Gather_Outer_parallel_workers=3
  - Gather_Outer_plan_width=260
  - Gather_Outer_reltuples=0.0000
  - Gather_Outer_sel=3.1000
  - Gather_Outer_startup_cost=6008.2400
  - Gather_Outer_total_cost=86968.2100
  - Limit_np=0
  - Limit_nt=20
  - Limit_nt1=55059
  - Limit_nt2=0
  - Limit_parallel_workers=0
  - Limit_plan_width=280
  - Limit_reltuples=0.0000
  - Limit_sel=0.0004
  - Limit_startup_cost=89809.7800
  - Limit_total_cost=89809.8300
  - Sort_Outer_np=0
  - Sort_Outer_nt=55059
  - Sort_Outer_nt1=55059
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=280
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=89809.7800
  - Sort_Outer_total_cost=89947.4300
- **Output:** st=1197.42, rt=1199.47
