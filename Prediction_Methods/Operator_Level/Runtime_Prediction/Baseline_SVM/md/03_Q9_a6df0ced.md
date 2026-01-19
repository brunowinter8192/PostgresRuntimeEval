# Query Prediction Report

**Query:** Q9_111_seed_902443410
**Timestamp:** 2026-01-09 16:34:36

## Input Summary

- **Test File:** Prediction_Methods/Operator_Level/Datasets/Baseline/04b_test_cleaned.csv
- **Overview File:** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/SVM/two_step_evaluation_overview.csv
- **Models Directory:** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model

## Query Tree

```
Node 16868 (Sort) - ROOT
  Node 16869 (Aggregate)
    Node 16870 (Gather)
      Node 16871 (Aggregate)
        Node 16872 (Hash Join)
          Node 16873 (Seq Scan) - LEAF
          Node 16874 (Hash)
            Node 16875 (Hash Join)
              Node 16876 (Seq Scan) - LEAF
              Node 16877 (Hash)
                Node 16878 (Hash Join)
                  Node 16879 (Hash Join)
                    Node 16880 (Nested Loop)
                      Node 16881 (Seq Scan) - LEAF
                      Node 16882 (Index Scan) - LEAF
                    Node 16883 (Hash)
                      Node 16884 (Seq Scan) - LEAF
                  Node 16885 (Hash)
                    Node 16886 (Seq Scan) - LEAF
```

## Prediction Chain (Bottom-Up)

### Step 1: Node 16873 (Seq Scan) - LEAF

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Seq_Scan/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Seq_Scan/model.pkl

**Input Features (execution_time):** np=26136.0000, plan_width=8.0000, sel=0.3226
**Input Features (start_time):** nt1=0.0000, nt2=0.0000, parallel_workers=0.0000, plan_width=8.0000, rt1=0.0000, rt2=0.0000, sel=0.3226, st1=0.0000, st2=0.0000, startup_cost=0.0000, total_cost=30974.7100

**Output:** predicted_startup_time=0.10, predicted_total_time=153.23

### Step 2: Node 16876 (Seq Scan) - LEAF

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Seq_Scan/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Seq_Scan/model.pkl

**Input Features (execution_time):** np=112600.0000, plan_width=29.0000, sel=0.2000
**Input Features (start_time):** nt1=0.0000, nt2=0.0000, parallel_workers=0.0000, plan_width=29.0000, rt1=0.0000, rt2=0.0000, sel=0.2000, st1=0.0000, st2=0.0000, startup_cost=0.0000, total_cost=124602.4300

**Output:** predicted_startup_time=0.66, predicted_total_time=681.18

### Step 3: Node 16881 (Seq Scan) - LEAF

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Seq_Scan/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Seq_Scan/model.pkl

**Input Features (execution_time):** np=4128.0000, plan_width=4.0000, sel=0.0284
**Input Features (start_time):** nt1=0.0000, nt2=0.0000, parallel_workers=0.0000, plan_width=4.0000, rt1=0.0000, rt2=0.0000, sel=0.0284, st1=0.0000, st2=0.0000, startup_cost=0.0000, total_cost=5169.6700

**Output:** predicted_startup_time=0.38, predicted_total_time=35.34

### Step 4: Node 16882 (Index Scan) - LEAF

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Index_Scan/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Index_Scan/model.pkl

**Input Features (execution_time):** plan_width=14.0000, startup_cost=0.4200
**Input Features (start_time):** nt=4.0000, plan_width=14.0000, reltuples=800000.0000, startup_cost=0.4200, total_cost=1.7400

**Output:** predicted_startup_time=0.07, predicted_total_time=0.07

### Step 5: Node 16884 (Seq Scan) - LEAF

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Seq_Scan/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Seq_Scan/model.pkl

**Input Features (execution_time):** np=223.0000, plan_width=8.0000, sel=1.0000
**Input Features (start_time):** nt1=0.0000, nt2=0.0000, parallel_workers=0.0000, plan_width=8.0000, rt1=0.0000, rt2=0.0000, sel=1.0000, st1=0.0000, st2=0.0000, startup_cost=0.0000, total_cost=323.0000

**Output:** predicted_startup_time=0.05, predicted_total_time=6.23

### Step 6: Node 16886 (Seq Scan) - LEAF

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Seq_Scan/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Seq_Scan/model.pkl

**Input Features (execution_time):** np=1.0000, plan_width=108.0000, sel=1.0000
**Input Features (start_time):** nt1=0.0000, nt2=0.0000, parallel_workers=0.0000, plan_width=108.0000, rt1=0.0000, rt2=0.0000, sel=1.0000, st1=0.0000, st2=0.0000, startup_cost=0.0000, total_cost=1.2500

**Output:** predicted_startup_time=0.06, predicted_total_time=2.88

### Step 7: Node 16880 (Nested Loop)

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Nested_Loop/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Nested_Loop/model.pkl

**Input Features (execution_time):** nt1=5678.0000, nt2=4.0000, rt1=35.3415, rt2=0.0733, st1=0.3759, st2=0.0717
**Input Features (start_time):** nt1=5678.0000, nt2=4.0000, plan_width=18.0000, rt1=35.3415, rt2=0.0733, sel=1.0000, st1=0.3759, st2=0.0717

**Output:** predicted_startup_time=4.85, predicted_total_time=1057.02

### Step 8: Node 16883 (Hash)

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Hash/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Hash/model.pkl

**Input Features (execution_time):** nt1=10000.0000, nt2=0.0000, rt1=6.2348, rt2=0.0000, st1=0.0495, st2=0.0000, startup_cost=323.0000, total_cost=323.0000
**Input Features (start_time):** nt1=10000.0000, nt2=0.0000, rt1=6.2348, rt2=0.0000, st1=0.0495, st2=0.0000, startup_cost=323.0000, total_cost=323.0000

**Output:** predicted_startup_time=11.60, predicted_total_time=11.61

### Step 9: Node 16885 (Hash)

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Hash/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Hash/model.pkl

**Input Features (execution_time):** nt1=25.0000, nt2=0.0000, rt1=2.8822, rt2=0.0000, st1=0.0560, st2=0.0000, startup_cost=1.2500, total_cost=1.2500
**Input Features (start_time):** nt1=25.0000, nt2=0.0000, rt1=2.8822, rt2=0.0000, st1=0.0560, st2=0.0000, startup_cost=1.2500, total_cost=1.2500

**Output:** predicted_startup_time=9.97, predicted_total_time=9.97

### Step 10: Node 16879 (Hash Join)

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Hash_Join/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Hash_Join/model.pkl

**Input Features (execution_time):** nt1=22712.0000, nt2=10000.0000, rt1=1057.0167, rt2=11.6057, st1=4.8516, st2=11.6047, total_cost=15774.1200
**Input Features (start_time):** nt1=22712.0000, nt2=10000.0000, rt1=1057.0167, rt2=11.6057, st1=4.8516, st2=11.6047, total_cost=15774.1200

**Output:** predicted_startup_time=42.23, predicted_total_time=953.16

### Step 11: Node 16878 (Hash Join)

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Hash_Join/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Hash_Join/model.pkl

**Input Features (execution_time):** nt1=22712.0000, nt2=25.0000, rt1=953.1588, rt2=9.9702, st1=42.2261, st2=9.9692, total_cost=15845.4100
**Input Features (start_time):** nt1=22712.0000, nt2=25.0000, rt1=953.1588, rt2=9.9702, st1=42.2261, st2=9.9692, total_cost=15845.4100

**Output:** predicted_startup_time=44.34, predicted_total_time=1022.38

### Step 12: Node 16877 (Hash)

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Hash/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Hash/model.pkl

**Input Features (execution_time):** nt1=22712.0000, nt2=0.0000, rt1=1022.3783, rt2=0.0000, st1=44.3446, st2=0.0000, startup_cost=15845.4100, total_cost=15845.4100
**Input Features (start_time):** nt1=22712.0000, nt2=0.0000, rt1=1022.3783, rt2=0.0000, st1=44.3446, st2=0.0000, startup_cost=15845.4100, total_cost=15845.4100

**Output:** predicted_startup_time=153.20, predicted_total_time=153.20

### Step 13: Node 16875 (Hash Join)

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Hash_Join/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Hash_Join/model.pkl

**Input Features (execution_time):** nt1=1200243.0000, nt2=22712.0000, rt1=681.1795, rt2=153.2042, st1=0.6643, st2=153.2032, total_cost=149790.4800
**Input Features (start_time):** nt1=1200243.0000, nt2=22712.0000, rt1=681.1795, rt2=153.2042, st1=0.6643, st2=153.2032, total_cost=149790.4800

**Output:** predicted_startup_time=166.37, predicted_total_time=877.82

### Step 14: Node 16874 (Hash)

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Hash/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Hash/model.pkl

**Input Features (execution_time):** nt1=81779.0000, nt2=0.0000, rt1=877.8191, rt2=0.0000, st1=166.3661, st2=0.0000, startup_cost=149790.4800, total_cost=149790.4800
**Input Features (start_time):** nt1=81779.0000, nt2=0.0000, rt1=877.8191, rt2=0.0000, st1=166.3661, st2=0.0000, startup_cost=149790.4800, total_cost=149790.4800

**Output:** predicted_startup_time=178.60, predicted_total_time=178.60

### Step 15: Node 16872 (Hash Join)

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Hash_Join/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Hash_Join/model.pkl

**Input Features (execution_time):** nt1=483871.0000, nt2=81779.0000, rt1=153.2265, rt2=178.6034, st1=0.1028, st2=178.6024, total_cost=184195.5000
**Input Features (start_time):** nt1=483871.0000, nt2=81779.0000, rt1=153.2265, rt2=178.6034, st1=0.1028, st2=178.6024, total_cost=184195.5000

**Output:** predicted_startup_time=117.40, predicted_total_time=609.96

### Step 16: Node 16871 (Aggregate)

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Aggregate/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Aggregate/model.pkl

**Input Features (execution_time):** nt1=131901.0000, nt2=0.0000, rt1=609.9556, rt2=0.0000, st1=117.4004, st2=0.0000
**Input Features (start_time):** nt1=131901.0000, nt2=0.0000, rt1=609.9556, rt2=0.0000, st1=117.4004, st2=0.0000

**Output:** predicted_startup_time=862.02, predicted_total_time=871.91

### Step 17: Node 16870 (Gather)

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Gather/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Gather/model.pkl

**Input Features (execution_time):** nt1=60150.0000, nt2=0.0000, rt1=871.9083, rt2=0.0000, st1=862.0218, st2=0.0000
**Input Features (start_time):** nt1=60150.0000, nt2=0.0000, parallel_workers=3.0000, rt1=871.9083, rt2=0.0000, st1=862.0218, st2=0.0000

**Output:** predicted_startup_time=494.76, predicted_total_time=1060.61

### Step 18: Node 16869 (Aggregate)

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Aggregate/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Aggregate/model.pkl

**Input Features (execution_time):** nt1=180450.0000, nt2=0.0000, rt1=1060.6062, rt2=0.0000, st1=494.7613, st2=0.0000
**Input Features (start_time):** nt1=180450.0000, nt2=0.0000, rt1=1060.6062, rt2=0.0000, st1=494.7613, st2=0.0000

**Output:** predicted_startup_time=993.48, predicted_total_time=979.21

### Step 19: Node 16868 (Sort) - ROOT

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Sort/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Sort/model.pkl

**Input Features (execution_time):** nt1=60150.0000, nt2=0.0000, plan_width=168.0000, rt1=979.2053, rt2=0.0000, sel=1.0000, st1=993.4818, st2=0.0000
**Input Features (start_time):** nt1=60150.0000, nt2=0.0000, plan_width=168.0000, rt1=979.2053, rt2=0.0000, sel=1.0000, st1=993.4818, st2=0.0000

**Output:** predicted_startup_time=1118.47, predicted_total_time=1121.23

## Prediction Results

| Node | Type | Actual ST | Actual RT | Pred ST | Pred RT | MRE ST (%) | MRE RT (%) |
|------|------|-----------|-----------|---------|---------|------------|------------|
| 16873 | Seq Scan | 0.26 | 132.24 | 0.10 | 153.23 | 60.2 | 15.9 |
| 16876 | Seq Scan | 0.33 | 689.96 | 0.66 | 681.18 | 100.7 | 1.3 |
| 16881 | Seq Scan | 0.22 | 25.76 | 0.38 | 35.34 | 67.8 | 37.2 |
| 16882 | Index Scan | 0.06 | 0.06 | 0.07 | 0.07 | 25.9 | 20.2 |
| 16884 | Seq Scan | 0.16 | 4.46 | 0.05 | 6.23 | 68.9 | 39.7 |
| 16886 | Seq Scan | 14.68 | 14.69 | 0.06 | 2.88 | 99.6 | 80.4 |
| 16880 | Nested Loop | 0.42 | 192.16 | 4.85 | 1057.02 | 1047.0 | 450.1 |
| 16883 | Hash | 4.92 | 4.92 | 11.60 | 11.61 | 136.1 | 136.1 |
| 16885 | Hash | 14.70 | 14.70 | 9.97 | 9.97 | 32.2 | 32.2 |
| 16879 | Hash Join | 5.36 | 199.50 | 42.23 | 953.16 | 687.4 | 377.8 |
| 16878 | Hash Join | 20.08 | 215.08 | 44.34 | 1022.38 | 120.9 | 375.4 |
| 16877 | Hash | 217.33 | 217.33 | 153.20 | 153.20 | 29.5 | 29.5 |
| 16875 | Hash Join | 217.75 | 1021.61 | 166.37 | 877.82 | 23.6 | 14.1 |
| 16874 | Hash | 1039.24 | 1039.26 | 178.60 | 178.60 | 82.8 | 82.8 |
| 16872 | Hash Join | 1039.83 | 1233.78 | 117.40 | 609.96 | 88.7 | 50.6 |
| 16871 | Aggregate | 1262.39 | 1263.05 | 862.02 | 871.91 | 31.7 | 31.0 |
| 16870 | Gather | 1272.57 | 1278.94 | 494.76 | 1060.61 | 61.1 | 17.1 |
| 16869 | Aggregate | 1274.33 | 1280.22 | 993.48 | 979.21 | 22.0 | 23.5 |
| 16868 | Sort | 1274.87 | 1280.36 | 1118.47 | 1121.23 | 12.3 | 12.4 |
