# CLAUDE.MD - Thesis1 Project Engineering Reference

## 1. PROJECT IDENTITY

**Research Domain:** ML-based runtime prediction for SQL queries
**Benchmark:** TPC-H queries on PostgreSQL
**Methodology:** Exploration and evaluation of various ML approaches
**Pipeline:** Dataset → Feature Selection → Model Training → Prediction → Evaluation

**Critical Constraint:** Large, mature codebase requiring focused, session-based navigation with strict context management.

**Hierarchy:**
- User + Claude Desktop → Meta-level, review, decisions
- Claude Code → Code implementation
- Subagents → Specialized tasks

---

## 2. SCIENTIFIC FOUNDATION

**Base Paper:** "Learning-based Query Performance Modeling and Prediction" (Akdere, Cetintemel, Upfal - Brown University, 2012)

**Paper Source:** `Misc/Learning-based_Query_Performance_Modeling_and_Pred.md`

**Workflow-Hook:** Bei jedem neuen Workflow (## Marker) frage: "Basiert dieser Ansatz auf dem Paper?" Falls ja: Paper lesen fuer Kontext.

---

## 3. PRIORITY LEVELS

**CRITICAL:** Must follow - violations break the system
**IMPORTANT:** Should follow - violations reduce quality
**RECOMMENDED:** Good practice - improves maintainability

---

## 4. CRITICAL STANDARDS

- NO comments inside function bodies (only function header comments + section markers)
- NO test files in root (ONLY in debug/ folder when requested)
- NO emojis in code AND documentation
- NO logging statements - scripts run completely silent
- NO console output (print, console.log, echo)
- NO hardcoded paths (always use argparse)
- NO verbose output of any kind

**Type hints:** RECOMMENDED but optional

**Fail-Fast:** Let exceptions fly. No try-catch that silently swallows errors affecting business logic. Script must fail if it cannot fulfill its purpose.

**Sofortiger Stopp bei Problemen:**
- Bei JEDEM unerwarteten Problem waehrend der Ausfuehrung: SOFORT STOPPEN
- User informieren mit klarer Problembeschreibung
- NIEMALS eigenmaechtig "fixen" oder Workarounds implementieren
- Warten auf explizite User-Entscheidung bevor fortgefahren wird

**Beispiele:** NaN-Werte, fehlende Dateien, unerwartete Formate, Algorithmus-Fehler, Abhaengigkeitsprobleme, etc.

**Warum:** Ein eigenmaechtiger "Fix" kann das gesamte Projekt invalidieren. Lieber einmal zu oft fragen als einmal zu wenig.

---

## 5. PROJECT ARCHITECTURE: Standalone Pipeline

**This project uses standalone module architecture, NOT orchestrated workflow.**

### Key Characteristics:
- NO workflow.py (manual orchestration by user)
- Each module: Independent script with argparse
- Scripts run completely silent
- Output ONLY via structured exports (.csv or .md files)
- User manually executes scripts in sequence, reviewing outputs between steps

### Rationale:
Research pipeline where each step requires manual analysis before proceeding. Structured exports serve as execution trace. No need for logging when outputs are already structured.

### Execution Pattern:
```
User runs: python 01_Script.py <args>
         → Script runs silently
         → Exports to csv/ or md/ folder
         → User reviews output
         → User runs: python 02_Script.py <args>
         → ...
```

---

## 6. THESIS-SPECIFIC RULES

### CSV Files

**CRITICAL:** ALL CSV files MUST use semicolon `;` as delimiter, never comma

**Rationale:** Excel on macOS requires semicolon to parse correctly

**Implementation:**
- When reading: `pd.read_csv(file, delimiter=';')` or `csv.reader(f, delimiter=';')`
- When writing: `pd.to_csv(file, sep=';')` or `csv.writer(f, delimiter=';')`

**Fix tool:** `/Users/brunowinter2000/Documents/Thesis/2025_2026/convert_csv_delimiter.py`
**Usage:** `python3 convert_csv_delimiter.py <csv_file>` (in-place conversion)

---

### Script Output Rules

**Output ONLY:** .md or .csv exports
**Export location:** Dedicated folder in same directory as script
**Folder naming:** Descriptive (e.g., `md/`, `csv/`, `analysis/`, `execution_time/`, `start_time/`, `predictions/`)
**Script behavior:** Completely silent - no prints, no logging, no verbose output

---

### Module Architecture

**Standalone modules:**
- Each module: Fixed Input (argparse) → Processing → Fixed Output (export folder)
- NO automatic cross-module orchestration
- User orchestrates execution manually

---

## 7. CODE ORGANIZATION

**CRITICAL:** Every script follows this structure:

**INFRASTRUCTURE → ORCHESTRATOR → FUNCTIONS**

### INFRASTRUCTURE
- Imports and constants
- Argparse setup (positional + optional flags)
- NO functions, NO logic

### ORCHESTRATOR
- ONE function calling other functions in sequence
- ZERO functional logic (no calculations, transformations, business rules)
- Meta-logic allowed: conditional workflow execution, parameter routing

### FUNCTIONS
- Ordered by call sequence
- One responsibility each
- Can call other functions internally

**Example:**
```python
# INFRASTRUCTURE
import pandas as pd
from pathlib import Path

# ORCHESTRATOR
def process_workflow(input_file: str, output_dir: str) -> None:
    raw = load_data(input_file)
    cleaned = clean_data(raw)
    export_results(analyze_data(cleaned), output_dir)

# FUNCTIONS

# Load raw data from CSV with semicolon delimiter
def load_data(input_file: str) -> pd.DataFrame:
    return pd.read_csv(input_file, delimiter=';')

# Remove invalid rows
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()

# Calculate statistics
def analyze_data(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby('category').mean()

# Save results to CSV
def export_results(results: pd.DataFrame, output_dir: str) -> None:
    Path(output_dir).mkdir(exist_ok=True)
    results.to_csv(f'{output_dir}/results.csv', sep=';', index=False)
```

---

## 8. COMMENT RULES

**CRITICAL:** Three types of allowed comments only

### 1. Section Markers
`# INFRASTRUCTURE`, `# ORCHESTRATOR`, `# FUNCTIONS`

### 2. Function Header Comments
One line describing WHAT the function does, placed directly above function definition.
```python
# Load validated customer data from CSV
def load_customer_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path, delimiter=';')
```

### 3. Cross-Module Import Comments
Format: `# From <module>.py: <what it does>`
```python
# From data_loader.py: Load and validate CSV
from data_loader import load_validated_data
```

**CRITICAL:** ALL cross-module imports MUST have comments. NO inline comments inside function bodies.

---

## 9. ERROR HANDLING

**IMPORTANT:** Fail-fast philosophy. If the script cannot fulfill its purpose, it must fail visibly.

**ALLOWED:**
- Retry logic with exponential backoff
- Resource cleanup (files, connections)
- Converting exceptions to domain errors

**PROHIBITED:**
- Silently swallowing errors
- Generic `except Exception: pass`
- Hiding failures affecting business logic

**Example:**
```python
def fetch_data(params):
    for attempt in range(3):
        try:
            return connect_and_fetch(params)
        except ConnectionError:
            if attempt == 2: raise
            time.sleep(2 ** attempt)
```

---

## 10. ARGPARSE TEMPLATE

```python
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Positional arguments
    parser.add_argument("input", help="Input path")

    # Required flags
    parser.add_argument("--output-dir", required=True, help="Output directory")

    # Optional with defaults
    parser.add_argument("--param", type=int, default=5, help="Parameter")

    args = parser.parse_args()

    main_workflow(Path(args.input), args.output_dir, args.param)
```

---

## 11. ARCHITECTURE STANDARDS

### Naming Conventions

**Scripts:** `NN_Two_Words.py`
- `NN`: Workflow position (01-99)
- `Two_Words`: Max 2 words, capitals
- Examples: `01_Process_Data.py`, `05_Extract_Features.py`, `07_Merge_Data.py`

**Parallel Scripts:** `NNx_Two_Words.py`
- Scripts on same level that can run in parallel: `01a`, `01b`, `01c`
- Successor script uses next number: `02` (requires all `01x` outputs)
- Examples: `01a_Runtime_Data.py`, `01b_Plan_Features.py` -> `02_Merge_Data.py`

**Analysis Scripts:** `A_NNx_Two_Words.py`
- Standalone analysis tools, NOT part of main workflow
- `A_` prefix distinguishes from workflow scripts
- Parallel numbering (`A_01a`, `A_01b`) since no dependencies between them
- Examples: `A_01a_Correlation_Analysis.py`, `A_01b_Scatter_Plots.py`

**Directories:** `Capital_Words/`
- Capital first letters, underscores between words
- Examples: `Data_Generation/`, `Raw_Data/`, `Runtime_Prediction/`

**Output Files:** `NN_descriptive_name.ext`
- Use same `NN` prefix as the script that generates them
- Timestamp for multiple runs: `NN_name_{timestamp}.ext`
- Examples: `05_features_20251102_135531.csv`, `07_operator_dataset_20251102_140747.csv`

**Rationale:** Immediate visual connection between script and its outputs

---

### Mapping Configuration Pattern

**Purpose:** Central mapping files (e.g., `mapping_config.py`) define dataset schema, folder naming, and feature sets for consistency.

**Use mapping for block operations** where multiple related values must stay synchronized:
- Folder naming (ensures consistent structure across scripts)
- Feature sets (column names that change together)
- Type definitions (operator types, node categories)

**Example:**
```python
from mapping_config import CHILD_FEATURES_TIMING
df = df.drop(columns=CHILD_FEATURES_TIMING)  # NOT ['st1', 'rt1', 'st2', 'rt2']
```

**Skip mapping for individual column access** where script uses subset of columns:
```python
df_filtered = df[['query_file', 'node_type']]  # Hardcoded is fine
```

**Split maps for semantic differences:**
```python
CHILD_FEATURES_TIMING = ['st1', 'rt1', 'st2', 'rt2']      # Unknown at prediction
CHILD_FEATURES_STRUCTURAL = ['nt1', 'nt2']                # Known at prediction
```

**Principle:** Mapping for coherent blocks, not arbitrary individual accesses.

---

## 12. DOCUMENTATION STRUCTURE

### Hierarchical Documentation Model

**Two-level hierarchy:** README (Workflow) stands ABOVE DOCS (Module)

**Key principles:**
- **README = Workflow-Level** - Can occur multiple times (one per workflow)
- **DOCS = Module-Level** - Lives under README
- **Relationship:** 1 README : n DOCS (NOT reverse)
- **README hierarchically ABOVE DOCS** - Workflow orchestration documented before module details

**Structure visualization:**

```
Project/
├── Workflow_A/
│   ├── README.md          # Workflow-Level
│   ├── Module_1/
│   │   └── DOCS.md        # Module-Level
│   ├── Module_2/
│   │   └── DOCS.md        # Module-Level
│   └── Module_3/
│       └── DOCS.md        # Module-Level
│
└── Workflow_B/
    ├── README.md          # Workflow-Level
    └── Module_4/
        └── DOCS.md        # Module-Level
```

**Concrete example (Operator_Level):**

```
Operator_Level/
├── README.md                    # Workflow-Level (1 README)
├── Data_Generation/
│   └── DOCS.md                  # Module-Level
├── Datasets/
│   └── DOCS.md                  # Module-Level
└── Runtime_Prediction/
    └── DOCS.md                  # Module-Level
                                 # → 3 DOCS under 1 README
```

---

### README.md (Workflow-Level Documentation)

**Purpose:** High-level overview of multi-phase workflow orchestration

**Placement Rules:**
- **Location:** Workflow root (e.g., `Plan_Level_1/`)
- **Relationship:** One README per workflow
- **Scope:** Orchestrates multiple modules (references multiple DOCS)

**Required Sections:**

#### 1. Directory Structure

Tree with 2-3 levels, inline comments, `[See DOCS.md]` references:

```
Plan_Level_1/
├── mapping_config.py                    # Shared configuration
├── README.md                            # Workflow documentation (THIS FILE)
├── Data_Generation/                     [See DOCS.md]
│   ├── 01a_Runtime_Data.py
│   ├── 01b_Plan_Features.py
│   └── csv/
├── Datasets/                            [See DOCS.md]
│   ├── 01_Split_Train_Test.py
│   ├── Baseline/
│   └── State_1/
└── Runtime_Prediction/                  [See DOCS.md]
    ├── ffs_config.py
    ├── 01_Forward_Selection.py
    └── Baseline_SVM/
```

#### 2. Shared Infrastructure

Config files with bullet list of exports:

```markdown
**mapping_config.py:**
- `DB_CONFIG`: PostgreSQL connection parameters
- `OPERATOR_TYPES`: 13 plan operator types for feature extraction
- `PLAN_METADATA`: ['query_file', 'template']
- `PLAN_TARGET`: 'runtime'
```

#### 3. Datasets

Table with dataset variants:

```markdown
| State | Features | Samples | Train/Test | Purpose |
|-------|----------|---------|------------|---------|
| Baseline | 50 | 2,850 | 2,280/570 | Full feature set reference |
| State_1 | 33 | 2,850 | 2,280/570 | Feature reduction impact |
```

#### 4. Workflow Overview

ASCII flow diagram showing phase dependencies:

```
Phase 1: Data_Generation
├── 01a_Runtime_Data.py ──┐
├── 01b_Plan_Features.py ─┼──→ 02_Merge_Data.py → complete_dataset.csv
└── 01c_Row_Features.py ──┘

Phase 2: Datasets
01_Split_Train_Test.py → 02_Create_State_1.py

Phase 3: Runtime_Prediction
01_Forward_Selection.py → 02_Train_Model.py → 03_Summarize_Results.py
```

#### 5. Phase Documentation

Per phase: Purpose, Input, Output, Details link:

```markdown
### Phase 1: Data_Generation

**Purpose:** Extract features and measure runtime for TPC-H queries

**Input:** Query directory with Q1/-Q22/ template folders containing SQL files

**Output:** `complete_dataset.csv` (2850 samples x 53 columns)
- 2 Metadata columns (query_file, template)
- 50 Feature columns (plan-level + operator metrics)
- 1 Target column (runtime in ms, cold cache)

**Details:** See [Data_Generation/DOCS.md](Data_Generation/DOCS.md)
```

**Keep it focused:** README explains WHAT happens at workflow level, DOCS explain HOW it happens at module level

---

### DOCS.md (Module-Level Documentation)

**Purpose:** Detailed documentation of scripts within one module/phase

**Placement Rules:**
- **Location:** Module directories (e.g., `Runtime_Prediction/`)
- **Relationship:** Multiple DOCS can exist under one README
- **Scope:** Documents scripts within ONE module only

**Required Sections:**
1. **Shared Infrastructure** - Module-specific config (e.g., `ffs_config.py`), constants, functions
2. **Workflow Execution Order** - Script sequence (00 → 01 → 02), dependencies, ASCII flow diagram
3. **Script Documentation** - Per script (### NN - Script_Name.py):
   - **Purpose:** One sentence
   - **Workflow:** Step-by-step process
   - **Inputs:** Positional argparse arguments
   - **Outputs:** Files with format, columns, location
   - **Usage:** Command template with example
   - **Variables:** Optional argparse flags

**Single-Script Modules:** Can use README.md instead of DOCS.md with simplified structure

---

**Key principle:**
- **README** = "How to RUN this workflow" (orchestration level)
- **DOCS** = "How modules WORK" (implementation level)
- **Hierarchy** = README references DOCS, never reverse

**User Reading Flow:**
1. README.md -> Understand tree structure + high-level workflow
2. DOCS.md -> Understand granular workflow + script details

---

## 13. PROJECT STRUCTURE

**Dynamic, organized by workflow needs**

**Common patterns:**
- `debug/` - Test files (when requested)
- `config.py` - Shared infrastructure
- `mapping_config.py` - Central mappings
- `README.md` - Project documentation
- `NN_Script_Name.py` - Workflow scripts
- Output folders: `csv/`, `md/`, `analysis/`, etc.

**NOT included:**
- NO `logs/` folder (scripts are silent, exports are the trace)
- NO `workflow.py` (manual orchestration)

