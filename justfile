# Thesis Prediction Methods - Justfile
# Usage: just <recipe> [args]

set shell := ["bash", "-cu"]

# Default: show available commands
default:
    @just --list --unsorted

# ═══════════════════════════════════════════════════════════════════════════════
# GIT SHORTCUTS
# ═══════════════════════════════════════════════════════════════════════════════

# Quick commit with message
commit msg:
    git add -A
    git commit -m "{{msg}}"

# Commit with scope prefix
commit-scope scope msg:
    git add -A
    git commit -m "{{scope}}: {{msg}}"

# Show recent commits
log n="5":
    git log --oneline -{{n}}

# ═══════════════════════════════════════════════════════════════════════════════
# HYBRID_1 - APPROACH PIPELINES
# ═══════════════════════════════════════════════════════════════════════════════

# Predict for an approach (e.g., just h1-predict approach_1)
h1-predict approach *flags:
    cd Prediction_Methods/Hybrid_1/Runtime_Prediction && \
    python3 03_Predict_Queries/03_Predict_Queries.py \
      ../Datasets/Baseline_SVM/test.csv \
      ../Datasets/Baseline_SVM/{{approach}}/patterns.csv \
      Baseline_SVM/SVM/Patterns/two_step_evaluation_overview.csv \
      Baseline_SVM/SVM/Operators/operator_overview.csv \
      Baseline_SVM/Model \
      --output-dir Baseline_SVM/Predictions/{{approach}} {{flags}}

# Evaluate predictions for an approach
h1-evaluate approach:
    cd Prediction_Methods/Hybrid_1/Runtime_Prediction && \
    python3 A_01a_Evaluate_Predictions.py \
      Baseline_SVM/Predictions/{{approach}}/predictions.csv \
      --output-dir Baseline_SVM/Evaluation/{{approach}}

# Generate propagation plots for an approach
h1-propagation approach:
    cd Prediction_Methods/Hybrid_1/Runtime_Prediction && \
    python3 A_01d_Depth_Propagation.py \
      ../Datasets/Baseline_SVM/test.csv \
      Baseline_SVM/Predictions/{{approach}}/predictions.csv \
      --output-dir Baseline_SVM/Evaluation/{{approach}}

# Full prediction pipeline for an approach
h1-run approach *flags: (h1-predict approach flags) (h1-evaluate approach) (h1-propagation approach)

# Generate dataset for an approach (extract, aggregate, clean, filter)
h1-generate approach *flags:
    cd Prediction_Methods/Hybrid_1/Datasets && \
    python3 03_Extract_Patterns.py Baseline_SVM/training.csv --output-dir Baseline_SVM/{{approach}} {{flags}}
    cd Prediction_Methods/Hybrid_1/Datasets && \
    python3 04_Aggregate_Patterns.py Baseline_SVM/{{approach}}/patterns.csv Baseline_SVM/{{approach}}
    cd Prediction_Methods/Hybrid_1/Datasets && \
    python3 05_Clean_Patterns.py Baseline_SVM/{{approach}}
    cd Prediction_Methods/Hybrid_1/Datasets && \
    python3 06_Filter_Patterns.py ../Data_Generation/csv/01_patterns_*.csv Baseline_SVM/{{approach}}/patterns.csv --output-dir Baseline_SVM/{{approach}} --threshold 0

# ═══════════════════════════════════════════════════════════════════════════════
# OPERATOR_LEVEL
# ═══════════════════════════════════════════════════════════════════════════════

# Data generation for Operator_Level
op-data:
    cd Prediction_Methods/Operator_Level/Data_Generation && python3 01a_Extract_Features.py
    cd Prediction_Methods/Operator_Level/Data_Generation && python3 01b_Extract_Targets.py
    cd Prediction_Methods/Operator_Level/Data_Generation && python3 02_Merge_Data.py

# Dataset preparation for Operator_Level
op-prepare:
    cd Prediction_Methods/Operator_Level/Datasets && python3 01_Filter_Templates.py
    cd Prediction_Methods/Operator_Level/Datasets && python3 02_Child_Features.py
    cd Prediction_Methods/Operator_Level/Datasets && python3 03_Split_Data.py
    cd Prediction_Methods/Operator_Level/Datasets && python3 04a_Split_Types.py

# Training for Operator_Level
op-train:
    cd Prediction_Methods/Operator_Level/Runtime_Prediction && python3 01_Forward_Selection.py
    cd Prediction_Methods/Operator_Level/Runtime_Prediction && python3 02_Train_Models.py

# Prediction for Operator_Level
op-predict:
    cd Prediction_Methods/Operator_Level/Runtime_Prediction && python3 03_Query_Prediction.py

# Full pipeline for Operator_Level
op-full: op-data op-prepare op-train op-predict

# ═══════════════════════════════════════════════════════════════════════════════
# PLAN_LEVEL_1
# ═══════════════════════════════════════════════════════════════════════════════

# Data generation for Plan_Level_1
plan-data:
    cd Prediction_Methods/Plan_Level_1/Data_Generation && python3 01a_Runtime_Data.py
    cd Prediction_Methods/Plan_Level_1/Data_Generation && python3 01b_Plan_Features.py
    cd Prediction_Methods/Plan_Level_1/Data_Generation && python3 01c_Row_Features.py
    cd Prediction_Methods/Plan_Level_1/Data_Generation && python3 02_Merge_Data.py

# Dataset preparation for Plan_Level_1
plan-prepare:
    cd Prediction_Methods/Plan_Level_1/Datasets && python3 01_Split_Train_Test.py
    cd Prediction_Methods/Plan_Level_1/Datasets && python3 02_Create_State_1.py

# Training for Plan_Level_1
plan-train:
    cd Prediction_Methods/Plan_Level_1/Runtime_Prediction && python3 01_Forward_Selection.py
    cd Prediction_Methods/Plan_Level_1/Runtime_Prediction && python3 02_Train_Model.py

# Prediction for Plan_Level_1
plan-predict:
    cd Prediction_Methods/Plan_Level_1/Runtime_Prediction && python3 03_Summarize_Results.py

# Full pipeline for Plan_Level_1
plan-full: plan-data plan-prepare plan-train plan-predict

# ═══════════════════════════════════════════════════════════════════════════════
# HYBRID_1 (Legacy full pipeline)
# ═══════════════════════════════════════════════════════════════════════════════

# Data generation for Hybrid_1
h1-data:
    cd Prediction_Methods/Hybrid_1/Data_Generation && python3 01_Find_Patterns.py

# Dataset preparation for Hybrid_1
h1-prepare:
    cd Prediction_Methods/Hybrid_1/Datasets && python3 01_Split_Train_Test.py
    cd Prediction_Methods/Hybrid_1/Datasets && python3 02_Extract_Operators.py
    cd Prediction_Methods/Hybrid_1/Datasets && python3 03_Extract_Patterns.py
    cd Prediction_Methods/Hybrid_1/Datasets && python3 04_Aggregate_Patterns.py
    cd Prediction_Methods/Hybrid_1/Datasets && python3 05_Clean_Patterns.py
    cd Prediction_Methods/Hybrid_1/Datasets && python3 06_Filter_Patterns.py

# Training for Hybrid_1 (patterns + operators)
h1-train:
    cd Prediction_Methods/Hybrid_1/Runtime_Prediction && python3 01_Feature_Selection.py
    cd Prediction_Methods/Hybrid_1/Runtime_Prediction && python3 01b_Feature_Selection_Operators.py
    cd Prediction_Methods/Hybrid_1/Runtime_Prediction && python3 02_Train_Models.py
    cd Prediction_Methods/Hybrid_1/Runtime_Prediction && python3 02b_Train_Models_Operators.py

# Full pipeline for Hybrid_1
h1-full: h1-data h1-prepare h1-train

# ═══════════════════════════════════════════════════════════════════════════════
# HYBRID_2
# ═══════════════════════════════════════════════════════════════════════════════

# Data generation for Hybrid_2
h2-data:
    cd Prediction_Methods/Hybrid_2/Data_Generation && python3 01_Find_Patterns.py

# Training pipeline for Hybrid_2 (greedy pattern selection)
h2-train:
    cd Prediction_Methods/Hybrid_2/Runtime_Prediction && python3 02_Operator_Train.py
    cd Prediction_Methods/Hybrid_2/Runtime_Prediction && python3 06_Extract_Test_Patterns.py
    cd Prediction_Methods/Hybrid_2/Runtime_Prediction && python3 07_Order_Patterns.py
    cd Prediction_Methods/Hybrid_2/Runtime_Prediction && python3 08_Error_Baseline.py
    cd Prediction_Methods/Hybrid_2/Runtime_Prediction && python3 09_Pretrain_Patterns.py

# Prediction for Hybrid_2
h2-predict:
    cd Prediction_Methods/Hybrid_2/Runtime_Prediction && python3 04_Query_Prediction.py

# Full pipeline for Hybrid_2
h2-full: h2-data h2-train h2-predict

# ═══════════════════════════════════════════════════════════════════════════════
# ONLINE_1
# ═══════════════════════════════════════════════════════════════════════════════

# Run Online_1 workflow for a single query
online query seed="42":
    cd Prediction_Methods/Online_1/Runtime_Prediction && python3 workflow.py --query {{query}} --seed {{seed}}

# Batch prediction with parallel execution
online-batch strategy="error" jobs="14":
    cd Prediction_Methods/Online_1/Runtime_Prediction && ./batch_predict.sh {{strategy}} {{jobs}}

# ═══════════════════════════════════════════════════════════════════════════════
# RESULTS & ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════

# Show results for a method
results method:
    @find Prediction_Methods/{{method}} -name "*results*.csv" -o -name "*summary*.csv" 2>/dev/null | head -10
    @echo "---"
    @ls -la Prediction_Methods/{{method}}/Runtime_Prediction/csv/ 2>/dev/null || echo "No csv directory"

# Show model files for a method
models method:
    @find Prediction_Methods/{{method}} -name "*.pkl" 2>/dev/null | head -20

# Quick summary of all methods
summary:
    @echo "=== Operator_Level ===" && ls Prediction_Methods/Operator_Level/Runtime_Prediction/csv/ 2>/dev/null | head -5 || echo "No results"
    @echo "=== Plan_Level_1 ===" && ls Prediction_Methods/Plan_Level_1/Runtime_Prediction/csv/ 2>/dev/null | head -5 || echo "No results"
    @echo "=== Hybrid_1 ===" && ls Prediction_Methods/Hybrid_1/Runtime_Prediction/csv/ 2>/dev/null | head -5 || echo "No results"
    @echo "=== Hybrid_2 ===" && ls Prediction_Methods/Hybrid_2/Runtime_Prediction/csv/ 2>/dev/null | head -5 || echo "No results"
    @echo "=== Online_1 ===" && ls Prediction_Methods/Online_1/Runtime_Prediction/Evaluation/ 2>/dev/null | head -5 || echo "No results"

# List all methods
methods:
    @echo "Operator_Level Plan_Level_1 Hybrid_1 Hybrid_2 Online_1 Dynamic"
