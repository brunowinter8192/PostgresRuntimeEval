# Hybrid_4 Workflow Roadmap

## Current Status

**✅ Completed:**
- Phase 0: Setup and Configuration
  - Created Hybrid_4 from Hybrid_3 structure
  - Updated `mapping_config.py` with 7 PT operators (≥95% threshold)
  - Updated README.md with Hybrid_4 differences
  - Phase 1 Pattern Discovery completed → **9 patterns found** (vs 20 in Hybrid_3)

**📊 Pattern Reduction:**
- Hybrid_3: 20 patterns → 40 models
- Hybrid_4: 9 patterns → 18 models (55% reduction)

**🎯 Hypothesis:** Q18 MRE improvement by treating Aggregate and Gather Merge as passthrough

---

## Remaining Workflow

### Phase 2: Datasets - Pattern Extraction and Preparation

**Input:** `/Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Operator_Level/Datasets/Baseline/04_training.csv`

**Working Directory:** `Hybrid_4/Datasets/`

#### Step 1: Extract Patterns
```bash
cd /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Hybrid_4/Datasets
python3 01_Extract_Patterns.py \
  /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Operator_Level/Datasets/Baseline/04_training.csv \
  Baseline_SVM \
  --output-dir Baseline_SVM
```
**Output:** `Baseline_SVM/{Pattern}/training.csv` (9 folders)

#### Step 2: Verify Extraction
```bash
python3 02_Verify_Extraction.py Baseline_SVM --output-dir Baseline_SVM
```
**Output:** `Baseline_SVM/csv/extraction_verification_{timestamp}.csv`

#### Step 3: Aggregate Patterns
```bash
python3 03_Aggregate_Patterns.py Baseline_SVM --output-dir Baseline_SVM
```
**Output:** `Baseline_SVM/{Pattern}/training_aggregated.csv`

#### Step 4: Verify Aggregation
```bash
python3 04_Verify_Aggregation.py Baseline_SVM --output-dir Baseline_SVM
```
**Output:** `Baseline_SVM/csv/aggregation_verification_{timestamp}.csv`

#### Step 5: Clean Patterns
```bash
python3 05_Clean_Patterns.py Baseline_SVM --output-dir Baseline_SVM
```
**Output:** `Baseline_SVM/{Pattern}/training_cleaned.csv`

---

### Phase 3: Runtime_Prediction - Model Training and Evaluation

**Working Directory:** `Hybrid_4/Runtime_Prediction/`

#### Step 6: Feature Selection
```bash
cd /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Hybrid_4/Runtime_Prediction
python3 01_Feature_Selection.py ../Datasets/Baseline_SVM --output-dir Baseline_SVM
```
**Output:**
- `Baseline_SVM/SVM/{target}/{Pattern}_csv/` (FFS results per pattern)
- `Baseline_SVM/SVM/two_step_evaluation_overview.csv`

**Note:** Memory intensive! May take 10-15 minutes.

#### Step 7: Train Models
```bash
python3 02_Train_Models.py \
  ../Datasets/Baseline_SVM \
  Baseline_SVM/SVM/two_step_evaluation_overview.csv \
  --output-dir Baseline_SVM
```
**Output:** `Baseline_SVM/Model/{target}/{Pattern}/model.pkl` (18 models total)

#### Step 8: Predict Queries
```bash
python3 03_Predict_Queries.py \
  /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Operator_Level/Datasets/Baseline/04_test.csv \
  Baseline_SVM/SVM/two_step_evaluation_overview.csv \
  ../../Operator_Level/Runtime_Prediction/Baseline_SVM/SVM/two_step_evaluation_overview.csv \
  Baseline_SVM/Model \
  ../../Operator_Level/Runtime_Prediction/Baseline_SVM/Model \
  --output-dir Baseline_SVM/Evaluation
```
**Output:** `Baseline_SVM/Evaluation/predictions.csv` with prediction_type (pattern/operator/passthrough)

#### Step 9: Evaluate Predictions
```bash
python3 04_Evaluate_Predictions.py \
  Baseline_SVM/Evaluation/predictions.csv \
  --output-dir Baseline_SVM/Evaluation
```
**Output:**
- `Baseline_SVM/Evaluation/overall_mre.csv`
- `Baseline_SVM/Evaluation/template_mre.csv`
- `Baseline_SVM/Evaluation/template_mre_plot.png`

**🎯 Key Metric:** Check Q18 MRE (Hybrid_3: 50.22%)

#### Step 10: Node Evaluation (Optional)
```bash
python3 05_Node_Evaluation.py \
  Baseline_SVM/Evaluation/predictions.csv \
  --output-dir Baseline_SVM/Evaluation
```
**Output:** Node-type MRE breakdown by prediction source

---

## Expected Results

**Pattern Statistics:**
- Total patterns: 9 (down from 20)
- Model count: 18 (down from 40)
- PT operators: 7 (up from 5)

**Prediction Type Distribution (Expected):**
- Pattern predictions: Lower count (fewer patterns)
- Operator predictions: Higher count (more fallback)
- Passthrough predictions: **Higher count** (Aggregate + Gather Merge now PT)

**Performance Hypothesis:**
- Q18 MRE: < 50.22% (improvement expected)
- Overall MRE: May increase or decrease (tradeoff)
- Passthrough inheritance: Zero approximation error for Aggregate/Gather Merge

---

## Comparison Command

After completion, compare Hybrid_3 vs Hybrid_4:

```bash
# Hybrid_3 Results
cat /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Hybrid_3/Runtime_Prediction/Baseline_SVM/Evaluation/overall_mre.csv
cat /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Hybrid_3/Runtime_Prediction/Baseline_SVM/Evaluation/template_mre.csv | grep Q18

# Hybrid_4 Results
cat /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Hybrid_4/Runtime_Prediction/Baseline_SVM/Evaluation/overall_mre.csv
cat /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Hybrid_4/Runtime_Prediction/Baseline_SVM/Evaluation/template_mre.csv | grep Q18
```

---

## Timeline Estimate

- Phase 2 (Datasets): ~5 minutes
- Phase 3 (FFS): ~10-15 minutes (memory intensive)
- Phase 3 (Training): ~2 minutes
- Phase 3 (Prediction): ~1 minute
- Phase 3 (Evaluation): <1 minute

**Total:** ~20-25 minutes
