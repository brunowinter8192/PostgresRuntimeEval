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

**GOOD:**
- "Find FEATURES constant definition in Runtime_Prediction/"
- "Find function that filters patterns by MRE threshold in 10_Pattern_Selection/"

**Pattern:**
1. Specific target (constant, function, class)
2. Scope (directory)
3. Context if needed (what you already know)

## After Agent Returns

ALWAYS verify agent output:
1. Read the FILE at LINES
2. Confirm RELEVANT matches your need
3. Then report to user
