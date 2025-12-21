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

Use agent when:
- Searching multiple files (>3 files)
- Broad search scope (entire directory, pattern search)
- Comparing files (Train vs Test, Static vs Dynamic)
- Analyzing CSV values (ranges, distributions)

Do NOT use agent when:
- Single file read (known path)
- Targeted grep (pattern + scope known)
- Quick verification (does file X exist?)

## After Agent Returns

**Agent = Scout, not Authority**

Agent provides:
- WHERE: File + lines
- HOW: Its interpretation

You are responsible for:
1. ALWAYS verify critical logic yourself (Read FILE at LINES)
2. Confirm RELEVANT matches your need
3. Only report to user after verification
4. When in doubt: check yourself instead of trusting agent output
