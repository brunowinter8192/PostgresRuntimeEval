---
name: agent-dispatch
description: (project)
---

# Agent Dispatch

## Agent Registry

| Agent | Model | Purpose | Output |
|-------|-------|---------|--------|
| search-specialist-thesis | Haiku | Codebase exploration, file search | FILE/LINES/RELEVANT |

## How to Prompt

**BAD:**
- "Find where features are defined"
- "How does pattern selection work?"
- "List all subdirectories and their contents" (too broad, causes context pollution)

**GOOD:**
- "Find FEATURES constant definition in Runtime_Prediction/"
- "Find function that filters patterns by MRE threshold in 10_Pattern_Selection/"
- "List subdirectories and Python files in Misc/. Exclude csv/, data files."

**Pattern:**
1. Specific target (constant, function, class)
2. Scope (directory)
3. Constraints: "Exclude *.csv, *.png" or "Limit depth to 2"
4. Context if needed (what you already know)
5. **Follow imports:** "If code imports from external modules, locate and READ those files"

**Exploration Constraints:**
- Always specify: "Exclude data files (*.csv, *.png, *.jpg)"
- For unknown directories: "Limit initial depth to 2 levels"
- For doc audits: "Focus on *.py files and DOCS.md"

**Tool Recommendations:**
- "Use `find` to locate files. Do NOT use `ls -R`"
- For CSV value search: "Use awk for numeric comparison, not grep"
- For large result sets: "Count matches first before printing"

## When to Use Agent

**Rule of thumb: >20k token exploration → Agent**

**Besser einen Agent zu viel als einen zu wenig.**

Use agent when:
- Searching multiple files (>3 files)
- Broad search scope (entire directory, pattern search)
- Comparing files (Train vs Test, Static vs Dynamic)
- Analyzing CSV values (ranges, distributions)
- **Comparing implementations** (e.g., Hybrid_2 vs Online_1) - use parallel agents

Do NOT use agent when:
- Single file read (known path)
- Targeted grep (pattern + scope known)
- Quick verification (does file X exist?)

## Parallel Agent Rules

Parallel agents are only efficient with **disjoint datasets**.

**Partition by:**
- **Layer:** Agent A = Docs only, Agent B = Code only
- **Scope:** Agent A = Training/, Agent B = Evaluation/
- **Aspect:** Agent A = Input/Output flow, Agent B = Algorithm logic

**NEVER:** Have multiple agents read the same files.

**BAD:**
- Agent A: "Investigate Runtime_Prediction/"
- Agent B: "Investigate Online_1/"
→ Both read workflow.py, DOCS.md, selection.py = wasted tokens

**GOOD:**
- Agent A (Architect): "Read ONLY DOCS.md and src/DOCS.md - create module map"
- Agent B (Inspector): "Read ONLY src/*.py - analyze selection logic"
→ Disjoint datasets, merge results in main agent

## After Agent Returns

**CRITICAL: Agent = Scout, not Authority**

Agent provides:
- WHERE: File + lines
- HOW: Its interpretation

**You MUST:**
1. **ALWAYS** verify critical logic yourself (Read FILE at LINES)
2. Confirm RELEVANT matches your need
3. Only report to user after verification
4. When in doubt: check yourself instead of trusting agent output

**NEVER** trust agent output blindly. The agent may:
- Miss files
- Misinterpret code
- Return outdated information

**Verify before reporting to user.**
