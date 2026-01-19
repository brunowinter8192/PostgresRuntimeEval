# Query Prediction Report

**Query:** Q14_109_seed_886035348
**Timestamp:** 2026-01-09 16:34:39

## Input Summary

- **Test File:** Prediction_Methods/Operator_Level/Datasets/Baseline/04b_test_cleaned.csv
- **Overview File:** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/SVM/two_step_evaluation_overview.csv
- **Models Directory:** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model

## Query Tree

```
Node 26483 (Aggregate) - ROOT
  Node 26484 (Gather)
    Node 26485 (Aggregate)
      Node 26486 (Hash Join)
        Node 26487 (Seq Scan) - LEAF
        Node 26488 (Hash)
          Node 26489 (Seq Scan) - LEAF
```

## Prediction Chain (Bottom-Up)

### Step 1: Node 26487 (Seq Scan) - LEAF

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Seq_Scan/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Seq_Scan/model.pkl

**Input Features (execution_time):** np=112600.0000, plan_width=16.0000, sel=0.0026
**Input Features (start_time):** nt1=0.0000, nt2=0.0000, parallel_workers=0.0000, plan_width=16.0000, rt1=0.0000, rt2=0.0000, sel=0.0026, st1=0.0000, st2=0.0000, startup_cost=0.0000, total_cost=130603.6400

**Output:** predicted_startup_time=3.65, predicted_total_time=739.92

### Step 2: Node 26489 (Seq Scan) - LEAF

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Seq_Scan/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Seq_Scan/model.pkl

**Input Features (execution_time):** np=4128.0000, plan_width=25.0000, sel=0.4167
**Input Features (start_time):** nt1=0.0000, nt2=0.0000, parallel_workers=0.0000, plan_width=25.0000, rt1=0.0000, rt2=0.0000, sel=0.4167, st1=0.0000, st2=0.0000, startup_cost=0.0000, total_cost=4961.3300

**Output:** predicted_startup_time=2.62, predicted_total_time=36.69

### Step 3: Node 26488 (Hash)

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Hash/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Hash/model.pkl

**Input Features (execution_time):** nt1=83333.0000, nt2=0.0000, rt1=36.6883, rt2=0.0000, st1=2.6224, st2=0.0000, startup_cost=4961.3300, total_cost=4961.3300
**Input Features (start_time):** nt1=83333.0000, nt2=0.0000, rt1=36.6883, rt2=0.0000, st1=2.6224, st2=0.0000, startup_cost=4961.3300, total_cost=4961.3300

**Output:** predicted_startup_time=32.86, predicted_total_time=32.86

### Step 4: Node 26486 (Hash Join)

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Hash_Join/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Hash_Join/model.pkl

**Input Features (execution_time):** nt1=15778.0000, nt2=83333.0000, rt1=739.9241, rt2=32.8612, st1=3.6511, st2=32.8602, total_cost=136648.0600
**Input Features (start_time):** nt1=15778.0000, nt2=83333.0000, rt1=739.9241, rt2=32.8612, st1=3.6511, st2=32.8602, total_cost=136648.0600

**Output:** predicted_startup_time=50.02, predicted_total_time=834.81

### Step 5: Node 26485 (Aggregate)

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Aggregate/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Aggregate/model.pkl

**Input Features (execution_time):** nt1=15778.0000, nt2=0.0000, rt1=834.8139, rt2=0.0000, st1=50.0168, st2=0.0000
**Input Features (start_time):** nt1=15778.0000, nt2=0.0000, rt1=834.8139, rt2=0.0000, st1=50.0168, st2=0.0000

**Output:** predicted_startup_time=919.88, predicted_total_time=930.10

### Step 6: Node 26484 (Gather)

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Gather/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Gather/model.pkl

**Input Features (execution_time):** nt1=1.0000, nt2=0.0000, rt1=930.1000, rt2=0.0000, st1=919.8841, st2=0.0000
**Input Features (start_time):** nt1=1.0000, nt2=0.0000, parallel_workers=5.0000, rt1=930.1000, rt2=0.0000, st1=919.8841, st2=0.0000

**Output:** predicted_startup_time=603.62, predicted_total_time=886.45

### Step 7: Node 26483 (Aggregate) - ROOT

**Model (execution_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/execution_time/Aggregate/model.pkl
**Model (start_time):** Prediction_Methods/Operator_Level/Runtime_Prediction/Baseline_SVM/Model/start_time/Aggregate/model.pkl

**Input Features (execution_time):** nt1=5.0000, nt2=0.0000, rt1=886.4533, rt2=0.0000, st1=603.6243, st2=0.0000
**Input Features (start_time):** nt1=5.0000, nt2=0.0000, rt1=886.4533, rt2=0.0000, st1=603.6243, st2=0.0000

**Output:** predicted_startup_time=937.96, predicted_total_time=926.23

## Prediction Results

| Node | Type | Actual ST | Actual RT | Pred ST | Pred RT | MRE ST (%) | MRE RT (%) |
|------|------|-----------|-----------|---------|---------|------------|------------|
| 26487 | Seq Scan | 1.07 | 738.89 | 3.65 | 739.92 | 240.0 | 0.1 |
| 26489 | Seq Scan | 7.78 | 36.39 | 2.62 | 36.69 | 66.3 | 0.8 |
| 26488 | Hash | 41.85 | 41.85 | 32.86 | 32.86 | 21.5 | 21.5 |
| 26486 | Hash Join | 43.72 | 788.86 | 50.02 | 834.81 | 14.4 | 5.8 |
| 26485 | Aggregate | 791.17 | 791.17 | 919.88 | 930.10 | 16.3 | 17.6 |
| 26484 | Gather | 803.75 | 810.15 | 603.62 | 886.45 | 24.9 | 9.4 |
| 26483 | Aggregate | 804.13 | 810.16 | 937.96 | 926.23 | 16.6 | 14.3 |
