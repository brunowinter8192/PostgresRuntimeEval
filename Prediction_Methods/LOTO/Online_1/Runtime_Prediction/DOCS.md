# Runtime_Prediction Module - Dynamic On-The-Fly Modeling

This module implements the complete on-the-fly modeling pipeline, combining pattern extraction, feature aggregation, model training, and prediction into a single end-to-end script.

## Directory Structure

```
Runtime_Prediction/
├── 01_Predict_OnTheFly.py          # Complete on-the-fly prediction pipeline
├── Predictions/                    # Output directory for predictions
│   ├── Q1/
│   │   └── predictions.csv         # [output] Q1 test query predictions
│   ├── Q3/
│   │   └── predictions.csv         # [output] Q3 test query predictions
│   ├── Q4/
│   ├── Q5/
│   ├── Q6/
│   ├── Q7/
│   ├── Q8/
│   ├── Q9/
│   ├── Q10/
│   ├── Q12/
│   ├── Q13/
│   ├── Q14/
│   ├── Q18/
│   └── Q19/
│       └── predictions.csv         # [output] Q19 test query predictions
└── DOCS.md
```

## Shared Infrastructure

### mapping_config.py

Located at: `../mapping_config.py`

**PATTERNS**
- List of 72 pattern hashes discovered from Data_Generation phase
- Used for pattern matching in test queries
- Example: `['895c6e8c1a30a094329d71cef3111fbd', '3aab37bea1a884da206eb32f2c1ae5ba', ...]`

**PATTERN_OPERATOR_COUNT**
- Dictionary mapping pattern hash to operator count
- Used for chunking extracted operators during aggregation
- Example: `{'895c6e8c1a30a094329d71cef3111fbd': 3, '3aab37bea1a884da206eb32f2c1ae5ba': 2, ...}`

**CHILD_FEATURES_TIMING**
- List of child timing features: `['st1', 'rt1', 'st2', 'rt2']`
- Not directly used in Runtime_Prediction (handled in Datasets/02_Clean_Test.py)

## Workflow Execution

```
01_Predict_OnTheFly.py
    |
    v
For each template folder (Q1, Q3, ..., Q19):
    |
    ├─ Load training_cleaned.csv (13 templates)
    ├─ Load 02_test_cleaned.csv (1 template)
    |
    ├─ For each test query:
    │   |
    │   ├─ [Phase 1] Extract patterns from query operators
    │   │   └─ Build tree → Hash-based matching → Extract pattern nodes
    │   |
    │   ├─ [Phase 2] Aggregate pattern features
    │   │   └─ Chunk by operator_count → Build tree → Hierarchical aggregation
    │   |
    │   ├─ [Phase 3] Train models on-the-fly
    │   │   ├─ Train pattern-specific SVM models (execution_time + start_time)
    │   │   └─ Train operator-specific SVM models (execution_time + start_time)
    │   |
    │   ├─ [Phase 4] Build execution plan
    │   │   └─ Greedy pattern matching (depth-first, longest first)
    │   |
    │   └─ [Phase 5] Execute predictions
    │       └─ Bottom-up propagation with cached child predictions
    |
    └─ Export predictions.csv to Predictions/{template_name}/
```

## Script Documentation

### 01 - Predict_OnTheFly.py

**Purpose:** Complete on-the-fly modeling pipeline combining pattern extraction, feature aggregation, model training, and prediction for 13-out-of-14 LOTO cross-validation

**Workflow:**

**Phase 0: Setup**
1. Load PATTERNS, PATTERN_OPERATOR_COUNT from mapping_config.py
2. Initialize SVM configuration (NuSVR with kernel='rbf', nu=0.65, C=1.5)

**Phase 1: Pattern Extraction**
1. Build tree structure from test query operators
2. For each node in tree:
   - Compute structural hash at each pattern length
   - Match against known pattern hashes
   - Extract operator rows for matched patterns
3. Result: Dict[pattern_hash → List[operator_rows]]

**Phase 2: Feature Aggregation**
1. For each matched pattern:
   - Extract pattern training data from 13 training templates
   - Chunk operators by PATTERN_OPERATOR_COUNT[pattern_hash]
   - For each chunk:
     - Build tree from operators
     - Aggregate hierarchical features with prefixes (e.g., HashJoin_node_type, SeqScan_Outer_row_estimate)
     - Create pattern-level feature vector
2. Result: DataFrame with pattern-level features

**Phase 3: Model Training (On-The-Fly)**
1. For each matched pattern:
   - Train SVM model for execution_time (actual_total_time)
   - Train SVM model for start_time (actual_startup_time)
   - Store models in memory with feature lists
2. For each operator type in test query:
   - Load operator-level training data (13 templates)
   - Train SVM model for execution_time
   - Train SVM model for start_time
   - Store models in memory with feature lists
3. Result: In-memory model dictionary

**Phase 4: Execution Plan Building**
1. Build tree from test query operators
2. Sort patterns by operator_count descending (longest first)
3. For each node (depth-first, shallowest first):
   - Try to match largest available pattern
   - If match: Add pattern_step to plan, mark nodes as consumed
   - Else: Add operator_step to plan
4. Result: Execution plan (list of steps)

**Phase 5: Prediction Execution**
1. Process execution plan in reverse order (bottom-up)
2. For each pattern_step:
   - Aggregate pattern features
   - Add child predictions from cache
   - Predict with pattern models
   - Cache predictions for all nodes in pattern
3. For each operator_step:
   - Aggregate operator features
   - Add child predictions from cache (st1, rt1, st2, rt2)
   - Predict with operator models
   - Cache prediction
4. Result: All node predictions (actual vs. predicted times)

**Inputs:**
- `baseline_dir`: Path to Datasets/Baseline/ directory containing 14 template folders
  - Example: `/path/to/Dynamic/Datasets/Baseline`
  - Each folder contains: training_cleaned.csv, test_cleaned.csv, 02_test_cleaned.csv

- `operator_training_file`: Path to operator-level dataset for operator model training
  - Example: `/path/to/Operator_Level/Datasets/Baseline/02_operator_dataset_cleaned.csv`
  - Format: Semicolon-delimited CSV with all operator-level features
  - Required columns: node_type, all operator features, actual_startup_time, actual_total_time

**Outputs:**
- `predictions.csv` (14 files, one per template directory)
  - Format: Semicolon-delimited CSV
  - Columns:
    - query_file: Query identifier
    - node_id: Node identifier in execution plan
    - node_type: Operator type (e.g., Hash Join, Seq Scan)
    - depth: Depth in execution plan tree
    - parent_relationship: Relationship to parent (Outer, Inner, SubPlan, InitPlan)
    - subplan_name: Subplan identifier (if applicable)
    - actual_startup_time: Ground truth startup time (ms)
    - actual_total_time: Ground truth execution time (ms)
    - predicted_startup_time: Predicted startup time (ms)
    - predicted_total_time: Predicted execution time (ms)
    - prediction_type: "pattern" or "operator"
  - Location: `Predictions/{template_name}/predictions.csv`
  - Rows: All operators from all test queries in template

**Usage:**
```bash
python3 01_Predict_OnTheFly.py \
    /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Dynamic/Datasets/Baseline \
    /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Operator_Level/Datasets/Baseline/02_operator_dataset_cleaned.csv \
    --output-dir /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Dynamic/Runtime_Prediction/Predictions
```

**Variables:**
- `--output-dir` (required): Output directory for predictions

**Technical Details:**

**Tree Structure:**
- QueryNode class with attributes: node_type, parent_relationship, depth, node_id, df_index, row_data, children
- Tree built from flat operator rows using depth-based parent-child relationships
- Used for pattern matching, feature aggregation, and execution plan building

**Pattern Matching:**
- Hash computation: MD5(node_type + sorted(child_hashes:parent_relationship))
- Order-independent: Children are sorted before hashing
- Recursive: Hash computed from leaves up to specified depth
- Conflict resolution: Depth-first processing with consumed node tracking

**Feature Aggregation:**
- Hierarchical prefixes: {NodeType}_{ParentRel}_{feature}
- Example: `SeqScan_Outer_row_estimate`, `Hash_Inner_plan_width`
- Root features: {NodeType}_{feature}
- Targets: Only root node's actual_startup_time and actual_total_time

**Model Training:**
- Algorithm: NuSVR (Nu Support Vector Regression)
- Kernel: RBF (Radial Basis Function)
- Hyperparameters: nu=0.65, C=1.5, gamma='scale'
- Scaling: MaxAbsScaler (scales features to [-1, 1])
- No feature selection: All available features used

**Execution Plan:**
- Greedy strategy: Longest patterns first (maximizes context)
- Depth-first: Process shallow nodes before deep nodes
- Consumed tracking: Prevents pattern overlaps
- Fallback: Operator-level models for unmatched operators

**Bottom-Up Propagation:**
- Child predictions cached by node_id
- Parent aggregation includes child predictions in features
- Child timing features: st1 (Outer child startup), rt1 (Outer child total), st2 (Inner child startup), rt2 (Inner child total)
- Enables recursive prediction from leaves to root

**Performance:**
- Processes 14 folds (one per template)
- Each fold: ~150 test queries
- Time per fold: ~10-15 minutes (extraction + aggregation + training + prediction)
- Total time: ~2-3 hours for complete evaluation
- Memory: ~500 MB peak per fold

**Limitations:**
- Requires PATTERNS from Hybrid_5 pattern mining (cannot discover patterns on-the-fly)
- No feature selection (uses all features, may include irrelevant ones)
- Slow compared to pre-trained approaches (trade-off for true unseen evaluation)
- Pattern extraction duplicates work across queries with same structure

## Implementation Notes

### Why Single Monolithic Script?

The script combines 5 Hybrid_5 phases (extraction, aggregation, cleaning, training, prediction) into one because:
1. **Simplicity:** No intermediate file I/O between phases
2. **Performance:** In-memory data structures (no CSV exports)
3. **Flexibility:** On-the-fly decisions (e.g., which patterns to train)
4. **Atomicity:** Complete prediction pipeline for each query

### Why No Feature Selection?

Dynamic uses all available features (no FFS) because:
1. **Time Constraint:** FFS would double execution time
2. **Pattern-Specific:** Each pattern has different optimal features
3. **Limited Data:** Only 13 templates for training (FFS needs more data)
4. **Baseline Comparison:** Using all features provides fair comparison

### Why Hash-Based Matching?

MD5 structural hashing provides:
1. **Order Independence:** Sorted children ensure consistent hashing
2. **Uniqueness:** Each pattern structure has unique hash
3. **Efficiency:** O(1) hash comparison vs. O(n) tree comparison
4. **Reusability:** Same hashes across Hybrid_5 and Dynamic

## Comparison with Hybrid_5

| Aspect | Hybrid_5 | Dynamic (01_Predict_OnTheFly.py) |
|--------|----------|----------------------------------|
| **Pattern Extraction** | 01_Extract_Patterns.py (offline) | Embedded in script (on-the-fly) |
| **Feature Aggregation** | 03_Aggregate_Patterns.py (offline) | Embedded in script (on-the-fly) |
| **Feature Cleaning** | 05_Clean_Aggregated.py (offline) | Implicit (all features used) |
| **Model Training** | 02_Train_Models.py (offline) | Embedded in script (on-the-fly) |
| **Prediction** | 03_Predict_Queries.py | Embedded in script (on-the-fly) |
| **Total Scripts** | 5 separate scripts | 1 monolithic script |
| **Execution** | Sequential (manual) | Automatic (per query) |
| **Models** | Pre-trained (disk) | Trained on-the-fly (memory) |
| **Test Data** | All templates | Excluded from training |

## Future Improvements

1. **Caching:** Cache extracted patterns across queries with same structure
2. **Parallelization:** Process multiple test queries in parallel
3. **Incremental FFS:** Perform fast feature selection on-the-fly
4. **Pattern Discovery:** Mine patterns from training folds only (no reliance on Hybrid_5)
5. **Adaptive Aggregation:** Skip aggregation for previously seen patterns

## Related Scripts

- `Datasets/01_Split_Templates.py` - Creates 13-of-14 train/test splits
- `Datasets/02_Clean_Test.py` - Removes child timing features from test sets
- `Hybrid_5/Datasets/01_Extract_Patterns.py` - Original pattern extraction logic
- `Hybrid_5/Datasets/03_Aggregate_Patterns.py` - Original feature aggregation logic
- `Hybrid_5/Runtime_Prediction/02_Train_Models.py` - Original model training logic
- `Hybrid_5/Runtime_Prediction/03_Predict_Queries.py` - Original prediction logic
