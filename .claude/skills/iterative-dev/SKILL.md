---
name: iterative-dev
description: Manages iterative workflow with plan-implement cycles. Use when user mentions "iterativer workflow".
---

# Iterative Development Skill

## Overview

This skill extends native Claude Code Plan Mode with:
- Phase indicators
- Iterative cycle structure
- Explicit file vs chat separation

Follow all native Plan Mode rules.

## Cycle

```
PLAN -> ExitPlanMode -> IMPLEMENT -> PLAN (new cycle)
```

Every response starts with phase indicator:
- `📋 PLAN` - Planning phase (Plan Mode active)
- `🔨 IMPLEMENT` - Implementation phase

---

## Planning Phase (PLAN)

### Communication

| Channel | Purpose |
|---------|---------|
| Chat | Brainstorming, asking questions |
| Plan file | Key points and implementation steps |

- One question at a time, based on previous answer, prefer multiple choice, 'aksuserquestion' tool
	- Questions building up on each other, one leads to another
- Use system-provided plan file path from Plan Mode message
- ALWAYS use Write/Edit tool to update plan file
- NEVER write plan content directly in chat

### Plan File Management

**Core Principle:** Build the plan iteratively.

```
update -> update -> update -> implement -> clear
```

- After each chat exchange: UPDATE the plan file
- Never write the complete plan at once
- Plan grows organically through conversation
- Only call ExitPlanMode when plan reflects current understanding

### Execution During Planning

If the planning session requires module execution to refine the plan:
1. Call ExitPlanMode
2. Execute only what is needed to refine the plan
3. Ask user to manually return to plan mode

### Before ExitPlanMode

- Plan file MUST reflect current implementation approach
- NEVER call ExitPlanMode with stale plan

---

## Question Tracking

Second file alongside plan file: `questions/questions.md` in project root.

**Purpose:** Knowledge base for future sessions - "did we discuss this before?"

**Workflow:**
1. User asks a question during planning
2. Claude explains/answers
3. Claude asks: "Add to questions.md?"
4. If yes: append Q + A to `questions/questions.md`

**Format:** Question + Answer

**Exception:** This file CAN be written during Plan Mode (unlike other files).

---

## Implementation Phase (IMPLEMENT)

### After Each Step

Ask: "Continue implementing or back to PLAN?"

### After IMPLEMENTATION
**CRITICAL**
1. Verify all plan items were executed
2. If open points remain: inform user, do NOT override them
3. If complete: clear plan file (override with single space), CLEAR OFF ALL WELL EXECUTED TASKS IN THE PLAN FILE AFTER EXECUTION
