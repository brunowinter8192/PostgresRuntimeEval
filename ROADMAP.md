# Thesis Implementation Roadmap

## Project Status Overview

**Current Date:** November 2025
**Research Question:** ML-based runtime prediction for SQL queries on TPC-H benchmark
**Dataset:** 2,850 queries (19 templates × 150 parameter seeds)

### What's Implemented

1. **Operator_Level/** - Per-operator SVM prediction (MRE: 63.58%)
2. **Plan_Level_1/** - Whole-query prediction with SVM/RF/XGBoost (MRE: varies by model)
3. **Hybrid_1/** - Pattern-level (depth ≥1, filtered operators) with ~21 patterns
4. **Hybrid_2/** - Pattern-level (depth ≥0, all operators) with 31 patterns (MRE: 16.44%)

### What's Missing (vs Paper)

1. **Dynamic Workload Evaluation** - Leave-one-template-out cross-validation
2. **Optimizer Cost Model Baseline** - Proves ML necessity (~120% MRE expected)
3. **Iterative Hybrid Algorithm** - Error-based sub-plan selection (Paper's Algorithm 1)
4. **On-the-Fly Model Building** - Query-specific custom models at runtime
5. **Actual vs Estimate Feature Analysis** - Robustness to optimizer estimation errors

---

## Paper Summary: Akdere et al. (2012)

**Title:** Learning-based Query Performance Modeling and Prediction

### Core Approaches

**1. Operator-Level**
- Models: Linear Regression per operator type
- Features: np, nt, nt1, nt2, sel, st1, rt1, st2, rt2
- Bottom-up composition
- Static MRE: ~7-54% (template-dependent)
- Dynamic MRE: ~40-60%

**2. Plan-Level**
- Model: SVM (nu-SVR kernel)
- Features: Plan metrics + operator counts/rows
- Forward Feature Selection
- Static MRE: 6.75%
- Dynamic MRE: >50% (fails on unseen templates!)

**3. Hybrid (Offline)**
- Algorithm 1: Iterative sub-plan selection
- Start with operator models, add plan models for high-error sub-plans
- Three ordering strategies: Size-based, Frequency-based, Error-based
- Static MRE: ~5-10%
- Dynamic MRE: ~15-30%

**4. Hybrid (Online)**
- Build custom models at query execution time
- Use existing feature data (no new executions)
- Query-specific sub-plan matching and training
- Static MRE: ~5-8%
- Dynamic MRE: ~10-20% (best overall!)

### Key Insights from Paper

1. **Analytical cost models inadequate** - Optimizer-based prediction: 120% MRE
2. **Plan-level excels for static, fails for dynamic** - Overfits to training templates
3. **Operator-level generalizes but less accurate** - High variance across templates
4. **Hybrid combines strengths** - Pattern models + operator fallback
5. **Online building most powerful** - Adapts to specific queries
6. **Estimation errors tolerable** - EST/EST nearly as good as ACT/ACT

### Paper's Dataset

- 12 TPC-H templates
- ~55 queries per template
- ~1,000 total queries
- 1GB and 10GB databases

---

## Our Implementation vs Paper

### Advantages

**More Data:**
- 15-19 templates (vs 12)
- 150 queries per template (vs 55)
- 2,850 total queries (vs 1,000)
- **3x more data for training!**

**Multiple Models:**
- Plan-Level: SVM, Random Forest, XGBoost (vs SVM only)
- Multi-seed FFS for stability (5 seeds vs 1)

**Novel Contributions:**
- Pattern-level hybrid approach (Hybrid_1/2)
- Systematic pattern size exploration
- Comprehensive evaluation suite

### Gaps

**Evaluation:**
- No dynamic workload testing (leave-one-template-out)
- No optimizer baseline comparison
- No ACT/EST feature analysis

**Algorithms:**
- No iterative hybrid with error-based selection
- No on-the-fly model building
- No online learning capability

**Infrastructure:**
- No hash-based sub-plan indexing
- No query-specific similarity matching
- No model caching strategy

---

## Hybrid_2 Deep Dive Analysis

### Current Performance

**Overall:** 16.44% MRE (74% better than pure operator-level)

**Pattern vs Operator Split:**
- Pattern predictions: 76.3% (1,950 / 2,556 operators)
- Operator fallback: 23.7% (606 / 2,556 operators)

**Best Templates (MRE < 5%):**
- Q12: 1.62%
- Q4: 1.22%
- Q5: 1.35%
- Q7: 1.52%
- Q8: 1.71%

**Worst Templates (MRE > 50%):**
- Q10: 68.21%
- Q3: 61.25%

### Critical Issues

**1. Seq Scan Operator Model Failure (HIGHEST PRIORITY)**

```
Seq Scan Fallback Predictions:
Q5:  13,997.85% MRE
Q7:  17,572.91% MRE
Q13: 80.04% MRE
```

**Impact:** Contaminates 23.7% of predictions (606 operators)

**Root Cause:** Operator-Level Seq Scan model fundamentally broken
- 4-5 orders of magnitude errors
- Likely feature selection or data quality issue
- External dependency: Operator_Level/Runtime_Prediction/Baseline_SVM

**Fix Required:** Retrain Operator_Level Seq Scan model immediately

---

**2. Pattern Overfitting on Rare Patterns**

**Current:** 31 patterns trained, many with < 500 samples

**Distribution:**
- 12 patterns: Exactly 120 samples (single template only!)
- Low-frequency patterns likely overfit
- No minimum occurrence threshold applied

**Solution:** Filter patterns with < 240 samples

---

**3. Overly Aggressive Feature Selection**

**Examples:**
- Hash_Join_Seq_Scan: Only 5 features selected
- Many patterns: Only 1-4 features
- Over-reliance on child timing (st1, rt1, st2, rt2)
- Missing structural features (nt, nt1, nt2, sel)

**Current Settings:**
```python
FFS_MIN_FEATURES = 1  # Too aggressive!
MIN_IMPROVEMENT = 0   # Accepts any improvement
```

**Solution:**
- MIN_FEATURES = 5
- MIN_IMPROVEMENT = 0.01
- Force structural features to always be included

---

**4. Child Timing Cascade Errors**

**Problem:**
- Non-leaf patterns require grandchild predictions for st1/rt1/st2/rt2
- Bad grandchild predictions poison parent pattern features
- Error cascades up the tree

**Example:**
```
Hash Join (uses Pattern Model)
├── Hash (st1/rt1 predicted by operator)
│   └── Seq Scan (predicted wrong!)
└── Hash (st2/rt2 predicted by operator)
    └── Seq Scan (predicted wrong!)

→ Hash predictions are bad
→ Hash Join pattern gets bad st1/rt1/st2/rt2 features
→ Hash Join prediction also bad!
```

**Solution:**
- Evaluate grandchild prediction quality
- Remove st/rt features if grandchildren poorly predicted
- Use confidence weighting for child features

---

**5. Root-Level Pattern Inclusion**

**Current:** Depth ≥0 includes root operators (e.g., Sort, Aggregate)
- Root operators vary significantly across queries
- Limited training samples per root pattern
- Poor generalization

**Solution:** Revert to depth ≥1 (exclude root), like Hybrid_1

---

### Adjustable Levers for Improvement

#### LEVER 1: Fix Operator-Level Fallback (Critical)
**Priority:** HIGHEST
**Impact:** 5-10% MRE reduction

**Actions:**
- Analyze Operator_Level/Runtime_Prediction/Baseline_SVM/Seq Scan model
- Check feature selection quality
- Verify training data quality
- Retrain with proper features

---

#### LEVER 2: Pattern Filtering
**Priority:** HIGH
**Impact:** 10-20% MRE reduction

**Current:** No filtering
**Proposed:**
```python
MIN_PATTERN_OCCURRENCES = 240  # Eliminate rare patterns
parent_depth >= 1              # Exclude root operators
```

**Expected:** 31 patterns → ~15-20 high-quality patterns

---

#### LEVER 3: Feature Selection Configuration
**Priority:** HIGH
**Impact:** 5-15% MRE reduction

**Current:**
```python
FFS_MIN_FEATURES = 1
MIN_IMPROVEMENT = 0
```

**Proposed:**
```python
FFS_MIN_FEATURES = 5
MIN_IMPROVEMENT = 0.01
REQUIRED_STRUCTURAL = ['nt', 'nt1', 'nt2', 'total_cost', 'startup_cost']
```

---

#### LEVER 4: Child Timing Feature Handling
**Priority:** MEDIUM
**Impact:** 5-10% MRE reduction

**Proposed:**
- Evaluate grandchild prediction quality per pattern
- Remove st/rt features for patterns with poor grandchild predictions
- Use confidence-weighted child features

---

#### LEVER 5: SVM Hyperparameters
**Priority:** MEDIUM
**Impact:** 3-8% MRE reduction

**Current:** RBF kernel, nu=0.65, C=1.5

**Proposed Pattern-Specific:**
- Large patterns (1000+ samples): RBF kernel, nu=0.65
- Medium patterns (500-1000): RBF kernel, nu=0.5
- Small patterns (< 500): Linear kernel, C=2.0

---

#### LEVER 6: Prediction Strategy
**Priority:** MEDIUM
**Impact:** 5-10% MRE reduction

**Current:** Pattern first, operator fallback

**Alternatives:**
- Confidence-based selection (use pattern only if confidence high)
- Ensemble prediction (blend pattern + operator)
- Pattern whitelist (only use high-quality patterns)

---

## Implementation Roadmap

### Phase 1: Hybrid_2 Fix → Hybrid_3 (1-2 Weeks)

**Goal:** Improve current pattern-level hybrid to 7-10% MRE

**Week 1: Critical Fixes**

1. **Fix Seq Scan Operator Model**
   - Location: Operator_Level/Runtime_Prediction/Baseline_SVM
   - Analyze current model and feature selection
   - Retrain with proper features
   - Verify < 20% MRE for Seq Scan fallback
   - **Deliverable:** Fixed Operator_Level fallback models

2. **Pattern Filtering**
   - Location: Hybrid_2/Data_Generation/01_Find_Patterns.py
   - Add MIN_PATTERN_OCCURRENCES = 240
   - Add parent_depth >= 1 filter
   - **Deliverable:** Reduced pattern count to ~15-20

3. **Feature Selection Improvements**
   - Location: Hybrid_2/Runtime_Prediction/ffs_config.py
   - Set MIN_FEATURES = 5
   - Set MIN_IMPROVEMENT = 0.01
   - Add REQUIRED_STRUCTURAL_FEATURES
   - **Deliverable:** More robust feature sets per pattern

**Week 2: Advanced Fixes & Evaluation**

4. **Child Timing Feature Handling**
   - Evaluate grandchild prediction quality
   - Implement conditional removal of st/rt features
   - Add confidence weighting
   - **Deliverable:** Reduced cascade errors

5. **Pattern-Specific Hyperparameters**
   - Implement kernel selection based on sample count
   - Tune nu/C parameters per pattern size
   - **Deliverable:** Better model quality for small patterns

6. **Comprehensive Evaluation**
   - Re-run complete pipeline with all fixes
   - Measure MRE by template, node type, prediction source
   - Compare vs Hybrid_2 baseline
   - **Deliverable:** Hybrid_3 with 7-10% target MRE

**Success Criteria:**
- Overall MRE: 7-10% (from 16.44%)
- Seq Scan fallback: < 20% MRE (from 13,000%)
- Template outliers: < 30% MRE (Q3, Q10 improved)
- No single pattern with > 100% MRE

---

### Phase 2: Dynamic Workload Evaluation (1 Week)

**Goal:** Implement leave-one-template-out testing (Paper's Section 5.4)

**Tasks:**

1. **Modify Dataset Scripts**
   - Location: */Datasets/
   - Implement template-based train/test splitting
   - Create 15 iterations (one per template)
   - Each iteration: Train on 14 templates, test on 1

2. **Run All Methods**
   - Operator_Level on dynamic splits
   - Plan_Level_1 on dynamic splits (expect >50% MRE!)
   - Hybrid_3 on dynamic splits (expect ~15-30% MRE)

3. **Analysis**
   ```
   Expected Results:
   - Plan-Level:    6-8% (static) → >50% (dynamic) [FAILS]
   - Operator-Level: 40-60% (static) → 40-60% (dynamic) [STABLE]
   - Hybrid_3:      7-10% (static) → 15-30% (dynamic) [GOOD]
   ```

4. **Template Analysis**
   - Which templates generalize well/poorly?
   - Which patterns help with unseen templates?
   - Error analysis: Why does plan-level fail?

**Deliverable:**
- Dynamic workload results for all methods
- Proof that hybrid generalizes better than plan-level
- Validates paper's key finding

**Success Criteria:**
- Plan-Level dynamic MRE > 50% (demonstrates overfitting)
- Hybrid_3 dynamic MRE < 30% (demonstrates generalization)
- Clear evidence hybrid is necessary for dynamic workloads

---

### Phase 3: On-the-Fly Model Building (2-3 Weeks)

**Goal:** Implement Paper's online hybrid approach (Section 4)

**Week 1: Infrastructure**

1. **Hash-based Sub-Plan Indexing**
   - Create plan tree hash function
   - Build inverted index: Sub-plan → Query IDs
   - Build forward index: Query ID → Sub-plans
   - **Deliverable:** Fast sub-plan lookup (< 1ms)

2. **Feature Database**
   - Store all training features + runtimes
   - Indexed by query ID and sub-plan hash
   - Support range queries on features (similarity search)
   - **Deliverable:** Queryable feature database

**Week 2: Similarity Matching & Training**

3. **Similarity Matching Algorithm**
   - Define similarity criteria:
     - Exact: operator type, structure
     - Similar: kardinalitäten (±20%), relations
   - Implement fast matching (< 10ms for 2,850 queries)
   - Tune minimum sample threshold (10-20 samples)
   - **Deliverable:** Similarity matcher

4. **On-the-Fly Training**
   - When query Q arrives:
     - Extract all sub-plans
     - Find similar sub-plans in database
     - Train custom model if ≥ MIN_SAMPLES matches
     - Otherwise fallback to offline hybrid
   - **Deliverable:** Online model builder

**Week 3: Optimization & Evaluation**

5. **Model Caching**
   - Cache recently trained models
   - LRU eviction policy
   - Cache key: Sub-plan hash + feature ranges
   - **Deliverable:** Reduced training overhead

6. **Evaluation**
   - Static workload: Compare vs Offline Hybrid
   - Dynamic workload: Compare vs Offline Hybrid
   - Measure training time overhead
   - **Deliverable:** Online_Hybrid/ approach

**Success Criteria:**
- Static MRE: 5-8% (better than Hybrid_3)
- Dynamic MRE: 10-20% (best overall)
- Training time: < 5 seconds per query
- Cache hit rate: > 50% for repetitive workloads

---

### Phase 4: Comparison & Documentation (2 Weeks)

**Goal:** Comprehensive evaluation and thesis documentation

**Week 1: Missing Baselines**

1. **Optimizer Cost Model Baseline**
   - Create Prediction_Methods/Baseline_Optimizer/
   - Extract optimizer cost estimates (p_tot_cost)
   - Train linear regression: cost → runtime
   - Evaluate on all datasets
   - **Expected:** ~120% MRE (proves ML is necessary)

2. **Actual vs Estimate Feature Analysis**
   - Extract actual cardinalities from EXPLAIN ANALYZE
   - Train with ACT/ACT, ACT/EST, EST/EST combinations
   - Compare robustness to estimation errors
   - **Expected:** EST/EST nearly as good as ACT/ACT

**Week 2: Final Comparison & Documentation**

3. **Comprehensive Results Table**

```
| Method              | Static MRE | Dynamic MRE | Models | Samples/Model | Training Time |
|---------------------|------------|-------------|--------|---------------|---------------|
| Optimizer Baseline  | 120%       | 120%        | 1      | 2,850         | Instant       |
| Plan-Level (SVM)    | 6-8%       | >50%        | 1      | 2,850         | Fast          |
| Plan-Level (RF)     | 7-9%       | >50%        | 1      | 2,850         | Fast          |
| Plan-Level (XGBoost)| 6-8%       | >50%        | 1      | 2,850         | Medium        |
| Operator-Level      | 40-60%     | 40-60%      | 26     | ~200/model    | Fast          |
| Hybrid_1 (Offline)  | 10-15%     | 20-35%      | ~40    | ~100/pattern  | Medium        |
| Hybrid_2 (Offline)  | 16%        | 25-40%      | 62     | ~50/pattern   | Medium        |
| Hybrid_3 (Fixed)    | 7-10%      | 15-30%      | ~40    | ~150/pattern  | Medium        |
| Hybrid (Online)     | 5-8%       | 10-20%      | Dynamic| Variable      | Slow          |
```

4. **Thesis Documentation**
   - Implementation details for all approaches
   - Results analysis and comparison
   - Novel contributions:
     - Pattern-level hybrid (systematic size-based)
     - Multi-model comparison (SVM/RF/XGBoost)
     - Multi-seed FFS for stability
   - Future work and limitations

**Deliverable:**
- Complete results for all methods
- Thesis-ready analysis and figures
- Comparison vs Paper (side-by-side)

---

## Timeline Summary

```
Week 1-2:   Phase 1 - Hybrid_3 (critical fixes + evaluation)
Week 3:     Phase 2 - Dynamic Workload Evaluation
Week 4-6:   Phase 3 - On-the-Fly Model Building
Week 7-8:   Phase 4 - Comparison & Documentation

Total: 8 weeks
```

---

## Key Decisions & Tradeoffs

### Why Fix Hybrid Before Dynamic Workload?

**Option A:** Fix Hybrid_2 first, then test dynamic
- Pro: Better baseline for comparison
- Pro: Learn from fixing before tackling harder problem
- Con: Don't know if fixes actually help generalization

**Option B:** Test dynamic first, then fix
- Pro: Understand generalization issues immediately
- Pro: Motivates fixes with concrete evidence
- Con: Testing broken implementation wastes time

**DECISION:** Option A (fix first)
- Seq Scan fix is critical regardless
- Pattern filtering improves both static and dynamic
- Better to have solid baseline before dynamic eval

---

### Why Online Building Last?

**Reasoning:**
- Most complex implementation
- Requires solid offline hybrid baseline
- Only worthwhile if offline hybrid works
- Papers shows 2x improvement (15-30% → 10-20%)

**Alternative:** Could skip if offline hybrid already good enough (< 10% MRE)

---

### Sample Size Thresholds

**Pattern Filtering:** 240 samples minimum
- Rationale: ~1.5 templates worth of data
- Conservative enough to prevent overfitting
- Generous enough to keep important patterns

**On-the-Fly Training:** 10-20 samples minimum
- Rationale: SVM needs ≥ 10 samples for meaningful fit
- Too few → use offline model instead

---

## Success Metrics

### Phase 1 Success:
- Hybrid_3 MRE < 10%
- No template > 30% MRE
- Seq Scan fallback < 20% MRE

### Phase 2 Success:
- Plan-Level dynamic MRE > 50% (validates paper)
- Hybrid_3 dynamic MRE < 30% (generalizes better)

### Phase 3 Success:
- Online Hybrid dynamic MRE < 20% (best overall)
- Training overhead < 5s per query

### Overall Success:
- Match or exceed paper's results
- Novel contributions documented
- Thesis-ready implementation

---

## Open Questions

1. **Is 16.44% MRE actually bad?**
   - Operator-Level is 63% → we're 74% better
   - Plan-Level is 6-8% → we're 2x worse
   - Paper's Hybrid is 5-10% → we're competitive

2. **Should we implement iterative hybrid (Algorithm 1)?**
   - Paper's core innovation
   - Different from our systematic size-based approach
   - Could be Phase 3b alternative to On-the-Fly

3. **How much does pattern size matter?**
   - Current: Size 2 (parent + children)
   - Future: Size 3, 4, 5?
   - Tradeoff: More context vs data sparsity

4. **Is our data advantage enough?**
   - 3x more queries than paper
   - Does this enable larger patterns?
   - Or do we still hit sparsity at size 3-4?

---

## Notes

- This roadmap is a living document
- Adjust based on results from each phase
- If Hybrid_3 achieves < 7% MRE, consider stopping
- If dynamic eval shows < 20% MRE, online building optional
- Focus is on thesis contribution, not perfect replication
