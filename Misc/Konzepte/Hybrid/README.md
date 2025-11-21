# Hybrid Prediction Concepts

Exploration and evaluation of hybrid pattern/operator prediction approaches for SQL query runtime estimation.

## Overview

This directory contains experimental modules exploring different hybrid strategies that combine pattern-level and operator-level prediction for more accurate SQL query runtime estimation. The focus is on understanding when pattern-based predictions outperform operator-level predictions and vice versa.

## Modules

### OperatorEngineering [See DOCS.md]

**Purpose:** Comprehensive analysis of operator characteristics, pattern performance evaluation, and execution plan generation with intelligent pass-through operator handling.

**Key Features:**
- **Pass-Through Operator Identification:** Automatic detection of operators with minimal processing overhead (startup_total_ratio >= 0.99)
- **Complete Pattern Name Reconstruction:** Full pattern names including parent and all children (e.g., `Hash_Join_Seq_Scan_Outer_Hash_Inner`)
- **Pattern-Level MRE Evaluation:** Performance analysis per complete pattern across query templates
- **Pass-Through Logic Implementation:** Bottom-up execution plan with prediction inheritance for pass-through operators
- **Template Variant Detection:** Identification of query execution plan variants within templates

**Pass-Through Operators Identified:**
1. Incremental Sort (1.000)
2. Merge Join (0.999)
3. Limit (0.999)
4. Sort (0.997)
5. Hash (0.996)

**Core Concept - Pass-Through "Fressen":**
Pass-through operators inherit predictions from their children without modification:
- `predicted_startup_time = child.predicted_startup_time`
- `predicted_total_time = child.predicted_total_time`

Example: `Limit → Sort → Aggregate` chain where Limit and Sort pass through Aggregate's predictions.

**Workflow Overview:**

```
01_Analyze_Operators
   → Identify pass-through vs computational operators
   → Output: operator_runtime_analysis.csv

02_Analyze_Template_Patterns
   → Detect query execution plan variants per template
   → Output: template_pattern_analysis.csv

03_Pattern_Complete_Evaluation
   → Reconstruct complete pattern names from predictions
   → Calculate MRE per pattern per template
   → Output: pattern MRE pivot tables (execution_time + start_time)

04_Filter_Passthrough_Patterns
   → Filter patterns with pass-through children (non-PT parent)
   → Evaluate performance of patterns containing pass-through operators
   → Output: filtered pattern MRE tables

05_create_execution_plan
   → Generate detailed bottom-up execution plan for single query
   → Apply pass-through logic and pattern matching
   → Output: markdown execution plan with step-by-step breakdown
```

**Pattern Exclusion Strategy:**
- Patterns with pass-through parents are NOT matched as patterns
- Example: `Sort_Aggregate_Outer` is rejected because Sort is pass-through
- Individual pass-through operators handled via prediction inheritance instead

**Key Insights:**
- Pass-through operators have minimal prediction overhead
- Patterns with pass-through children show different performance characteristics
- Bottom-up execution planning with pass-through logic reduces prediction complexity
- Template variants reveal query optimization strategies

**Documentation:** See `OperatorEngineering/DOCS.md` for complete script documentation, workflow details, and usage examples.

## Research Context

This work is part of a thesis exploring ML-based runtime prediction for SQL queries using the TPC-H benchmark on PostgreSQL. The OperatorEngineering module specifically investigates:

1. **Operator Categorization:** Distinguishing pass-through operators from computational operators based on runtime characteristics
2. **Pattern Performance:** Evaluating when pattern-level predictions outperform operator-level predictions
3. **Hybrid Strategies:** Developing intelligent prediction routing (pattern vs operator vs pass-through)
4. **Execution Plan Generation:** Creating detailed prediction workflows for query execution

## Future Directions

Potential extensions of this work:
- Dynamic threshold tuning for pass-through detection
- Multi-level pattern hierarchies (patterns containing patterns)
- Adaptive routing based on query characteristics
- Integration with query optimizer hints
