# Thesis: ML-Based Runtime Prediction for SQL Queries

## Project Overview

**Research Domain:** Machine learning-based runtime prediction for SQL queries
**Benchmark:** TPC-H queries on PostgreSQL
**Dataset:** 2,850 query variants (19 TPC-H templates × 150 parameter seeds)
**Methodology:** Exploration and evaluation of multiple ML-based prediction approaches

This project investigates various machine learning techniques for predicting SQL query execution time using the TPC-H benchmark on PostgreSQL. The research explores operator-level, plan-level, and hybrid pattern-level prediction methods.

---

## Directory Structure

```
Thesis_Final/
├── TPC-H V3.0.1/          # Official TPC-H benchmark suite
├── Prediction_Methods/     # All prediction approaches explored
├── Misc/                   # Foundational work and documentation
└── CLAUDE.md               # Engineering reference and coding standards
```

---

## TPC-H V3.0.1/

**Purpose:** Official TPC-H benchmark specification and data generation toolkit

**Contents:**
- Data generation tools (dbgen/)
- Official specification (specification.pdf, specification.docx)
- Reference data for validation (ref_data/)
- End-user license agreement (EULA.txt)

**Status:** Official download from TPC-H website, modified for PostgreSQL compatibility

**Configuration Details:** See `Misc/Setup.md` for PostgreSQL-specific modifications and setup instructions

---

## Prediction_Methods/

**Purpose:** Contains all machine learning-based runtime prediction approaches explored in this research

**Naming Convention:** Suffixes `_1` and `_2` indicate fundamental changes in prediction methodology

### Prediction Approaches

Each approach follows a consistent 3-phase workflow:
1. **Data_Generation/** - Feature and target extraction from EXPLAIN plans
2. **Datasets/** - Dataset preparation, cleaning, and train/test splits
3. **Runtime_Prediction/** - Model training, evaluation, and prediction

---

#### Operator_Level/

**Approach:** Per-operator runtime prediction using SVM models

**Methodology:**
- Extract operator-level features from query execution plans
- Train separate SVM models for each operator type
- Predict query runtime by aggregating individual operator predictions (bottom-up)

**Models:** 26 SVM models (13 operator types × 2 targets: startup time, runtime)

**Documentation:** See `Prediction_Methods/Operator_Level/README.md`

---

#### Plan_Level_1/

**Approach:** Whole-query runtime prediction using plan-level features

**Methodology:**
- Extract aggregated plan-level features from entire query execution plans
- Train models on complete query characteristics (no operator decomposition)
- Multiple model types: SVM, Random Forest, XGBoost

**Datasets:**
- **Baseline/** - Full 50-feature set (2,850 samples)
- **State_1/** - Basic 34-feature set (didactic/comparison purposes)

**Feature Selection:** Forward feature selection (FFS) applied to identify optimal feature subsets

**Documentation:** See `Prediction_Methods/Plan_Level_1/README.md`

---

#### Hybrid_1/

**Approach:** Pattern-level prediction grouping parent + children operators

**Methodology:**
- Discover recurring parent-child operator patterns in training data
- Train SVM models for each pattern (aggregating parent + children features)
- Hybrid prediction: pattern models for recognized patterns, operator-level fallback for uncovered operators

**Characteristics:**
- Depth filter: parent_depth >= 1 (excludes root-level patterns)
- Operator filter: REQUIRED_OPERATORS only (Gather, Hash, Hash Join, Nested Loop, Seq Scan)
- Pattern count: Approximately 21 patterns

**External Dependencies:** `Operator_Level/Runtime_Prediction/Baseline_SVM/` (fallback models)

**Documentation:** See `Prediction_Methods/Hybrid_1/README.md`

---

#### Hybrid_2/

**Approach:** Extended pattern-level prediction (broader coverage than Hybrid_1)

**Methodology:** Same as Hybrid_1 with different filtering criteria

**Characteristics:**
- Depth filter: parent_depth >= 0 (includes root-level patterns)
- Operator filter: None (all operator types considered)
- Pattern count: Approximately 39 patterns

**External Dependencies:** `Operator_Level/Runtime_Prediction/Baseline_SVM/` (fallback models)

**Documentation:** See `Prediction_Methods/Hybrid_2/README.md`

---

## Misc/

**Purpose:** Foundational and preliminary work supporting the main prediction methods

**Contents:**

### Key Resources

- **Learning-based_Query_Performance_Modeling_and_Pred.md**
  Research paper serving as the foundation for this thesis

- **Setup.md**
  Infrastructure setup documentation covering:
  - TPC-H kit configuration
  - PostgreSQL Docker container setup
  - Database performance tuning
  - Data generation process
  - Feature extraction methodology

- **Generated_Queries/**
  TPC-H query templates with parameter variations (19 templates × 150 seeds = 2,850 queries)

- **Konzepte/**
  Conceptual designs and exploratory work

---

## Quick Start

### Prerequisites

- Python 3.x with virtual environment
- PostgreSQL database
- TPC-H benchmark data

### Setup

1. **Environment Setup:**
   Follow instructions in `Misc/Setup.md` for PostgreSQL configuration and data generation

2. **Explore Prediction Methods:**
   Start with any prediction approach's README.md:
   - `Prediction_Methods/Operator_Level/README.md`
   - `Prediction_Methods/Plan_Level_1/README.md`
   - `Prediction_Methods/Hybrid_1/README.md`
   - `Prediction_Methods/Hybrid_2/README.md`

3. **Engineering Standards:**
   Review `CLAUDE.md` for coding conventions, architecture patterns, and project-specific rules

---

## Documentation Navigation

**Hierarchical Documentation Model:**

```
README.md (THIS FILE)           # Project root - Overview of all approaches
    ↓
Prediction_Methods/*/README.md  # Workflow-level - Phase orchestration
    ↓
Prediction_Methods/*/*/DOCS.md # Module-level - Script implementation details
```

**Root Level (Project Overview):**
- `README.md` - This file: project overview and directory structure
- `CLAUDE.md` - Engineering reference and coding standards

**Workflow Level (Prediction Approaches):**
- `Operator_Level/README.md` - Per-operator prediction workflow
- `Plan_Level_1/README.md` - Plan-level prediction workflow
- `Hybrid_1/README.md` - Pattern-level prediction workflow (filtered)
- `Hybrid_2/README.md` - Pattern-level prediction workflow (extended)

**Module Level (Implementation Details):**
- Each workflow contains 3 DOCS.md files (one per phase: Data_Generation, Datasets, Runtime_Prediction)

**Supporting Documentation:**
- `Misc/Setup.md` - Infrastructure and environment setup
- `Misc/Learning-based_Query_Performance_Modeling_and_Pred.md` - Foundational research paper

---

## Dataset Overview

**Benchmark:** TPC-H Decision Support Benchmark
**Query Templates:** 19 templates (Q1-Q22, excluding Q15, Q17, Q20)
**Parameter Seeds:** 150 variations per template
**Total Queries:** 2,850 query variants
**Database:** PostgreSQL with TPC-H schema
**CSV Delimiter:** Semicolon (`;`) for macOS Excel compatibility

**Common Dataset Variations:**
- **Baseline:** Standard configuration excluding templates with InitPlan/SubPlan (Q2, Q11, Q16, Q22)
- **State_1:** Reduced feature set for didactic comparison (Plan_Level_1 only)
- **Pattern-filtered:** Different operator/depth filters (Hybrid_1 vs Hybrid_2)

---

## Architecture Principles

This project follows a **standalone pipeline architecture**:

- **NO workflow orchestration:** User manually executes scripts in sequence
- **Silent execution:** Scripts run without console output
- **Structured exports:** Results exported to CSV/MD files only
- **Argparse configuration:** All scripts use command-line arguments (no hardcoded paths)
- **Manual review:** User reviews outputs between pipeline steps

For detailed architecture standards, see `CLAUDE.md`.
