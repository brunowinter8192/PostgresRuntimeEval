---
name: iterative-dev
description: Manages iterative workflow with plan-implement cycles. Use when user mentions "iterative workflow".
---

# Iterative Development Skill

## Overview

This skill extends native Claude Code Plan Mode with:
- Phase indicators
- Iterative cycle structure
- Explicit file vs chat separation

Follow all native Plan Mode rules.

## Task Management Hierarchy

- **Beads** (`.beads/`) - Cross-session (weeks/months)
- **Plan-File** (`.claude/plans/`) - Within a session (hours)
- **TodoWrite** - Within an iteration (minutes)

## CRITICAL CYCLE

```
PLAN (Plan Mode) -> IMPLEMENT -> EVALUATE -> IMPROVE -> CLOSING -> PLAN (new cycle)
```

EVERY RESPONSE STARTS WITH A PHASE INDICATOR:
- `📋 PLAN` - Planning phase (Plan Mode active)
- `🔨 IMPLEMENT` - Implementation phase
- `🔍 EVALUATE` - Report phase (not Plan Mode)
- `🛠️ IMPROVE` - Improvements phase (not Plan Mode)
- `✅ CLOSING` - Cycle completion (not Plan Mode)

**Note:** Only PLAN uses Claude Code's native Plan Mode system prompt. EVALUATE, IMPROVE and CLOSING are skill-internal phases that happen after IMPLEMENT, regardless of system mode. 

**Phase Detection:** System message contains "Plan mode is active" → PLAN phase is active. This is the trigger to return to PLAN from any other phase.

---

## Planning Phase (PLAN)

### Exploration

**Documentation First (MANDATORY):**

BEFORE any action in a directory (running scripts, editing files, exploring code):
1. STOP
2. READ the DOCS.md in that directory
3. ONLY THEN proceed

This is NON-NEGOTIABLE. Skipping DOCS.md leads to: wrong paths, wrong arguments, wrong understanding.

**Agent Usage:**
- Decide autonomously whether an agent is necessary
- Agents are useful for getting an overview of unfamiliar areas
- Critical information (paths, parameters, dependencies) MUST be verified firsthand
- When in doubt: Read the file yourself

**Prompting the Search Agent:**
When delegating to search agent, be SPECIFIC:

WRONG: "Find where features are defined"
RIGHT: "Find where FEATURES constant is defined in Runtime_Prediction/"

WRONG: "How does pattern selection work?"
RIGHT: "Find the function that filters patterns by MRE threshold"

The agent returns FILE/LINES/RELEVANT - you then read those specific lines to verify and understand.

### Communication

| Channel | Purpose |
|---------|---------|
| Chat | Brainstorming, asking questions |
| Plan file | Key points and implementation steps |

**Proactivity (CRITICAL):**
- On skill start: Ask context questions IMMEDIATELY, don't wait
- Form hypotheses and verify them
- Don't wait for user hints - explore yourself

**Questions:**
- One question at a time, based on previous answer, prefer multiple choice, 'askuserquestion' tool
- Questions building up on each other, one leads to another

**Plan-File:**
- Use system-provided plan file path from Plan Mode message
- ALWAYS use Write/Edit tool to update plan file
- NEVER write plan content directly in chat

### Plan File Management

**Core Principle:** Build the plan ITERATIVELY.

- **CRITICAL:**
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

## Implementation Phase (IMPLEMENT)

- execute whats stated in the PLAN file

### After IMPLEMENTATION

**Principle:** One phase per response. Never combine IMPLEMENT and EVALUATE in same response.

1. Verify all plan items were executed
2. **If open points remain:** Inform user: "Open items: [list]"
3. Ask: "Continue implementing or proceed to EVALUATE?"

User confirms → next response starts with 🔍 EVALUATE

### Ad-hoc Window

After completing plan edits, BEFORE transition to EVALUATE:

1. Claude: "Plan edits completed. Proceed to EVALUATE?"
2. User can request ad-hoc edits
3. Claude executes ad-hoc edits
4. Back to step 1 until user says "eval"

**CRITICAL:** This window is the ONLY place for ad-hoc edits.

---

## Evaluation Phase (EVALUATE)

**Purpose:** Evaluate the PLAN→IMPLEMENT iteration - both CONTENT and PROCESS.

**ABSOLUTE RULE: ZERO EDITS IN EVALUATE.**

EVALUATE = COLLECT improvements
IMPROVE = EXECUTE improvements

**FORBIDDEN in EVALUATE:**
- ANY file edits (code, docs, config)
- ANY tool calls that modify files (Edit, Write, Bash with side effects)
- Executing user remarks immediately

**ALLOWED in EVALUATE:**
- Read tools (Read, Glob, Grep)
- Git commit (for IMPLEMENT changes only)
- Collecting improvements into a list
- Adding user remarks to the improvement list

**When user gives a remark in EVALUATE:**
1. ADD it to the improvement list
2. DO NOT execute it
3. Ask: "Added to improvements. Any more remarks?"
4. Only execute in IMPROVE phase

Claude writes a report covering:

### 1. Execution
- What matched the plan, what deviated

### 2. Process Reflection (CRITICAL)
Explicitly analyze the planning phase:
- **Efficiency:** Did we iterate too much? Could we have reached the plan faster?
- **Questions:** Were my questions focused or scattered?
- **Assumptions:** Did I make wrong assumptions that needed correction?
- **User Clarity:** Was the user's intent clear from the start?

**Anti-Pattern:** Long back-and-forth in PLAN before reaching a stable plan. If this happened, identify WHY and how to prevent it next time.

### 3. Documentation
- Does DOCS.md need updating? (new scripts, changed behavior, new parameters)

### 4. Improvements
Two categories - BOTH are important:

**Content Improvements (Code/Docs):**
- Critical: Must fix (breaks functionality, wrong behavior)
- Important: Should fix (code quality, maintainability)
- Optional: Nice to have (style, minor optimizations)

**Process Improvements (Workflow):**
- What would make the next PLAN phase more efficient?
- Which questions should I ask earlier?
- Which assumptions should I verify before proposing?

**COMMIT (CRITICAL):** After the report, check: Were edits made during IMPLEMENT? → Commit immediately.

After report + commit:
1. Ask: "Any remarks?"
2. Collect additional user feedback into improvement list
3. Ask: "Proceed to IMPROVE?"

**CRITICAL:** Wait for EXPLICIT confirmation (e.g., "improve", "proceed", "yes"). User adding remarks is NOT confirmation. Only enter IMPROVE when user explicitly confirms the phase transition.

User confirms → next response starts with 🛠️ IMPROVE

---

## Improve Phase (IMPROVE)

**Purpose:** Execute ALL improvements collected in EVALUATE.

**THIS is where edits happen. NOT in EVALUATE.**

Improvement sources:
- Report findings (DOCS.md updates, code fixes)
- User remarks collected during EVALUATE
- Process improvements (CLAUDE.md, skill files)

**Workflow:**
1. List all collected improvements
2. Execute each one (Edit, Write, Bash)
3. Commit changes
4. Ask: "Proceed to CLOSING?"

User confirms → next response starts with ✅ CLOSING

---

## Closing Phase (CLOSING)

Only enter when user confirms (e.g., "proceed", "close", "done").

1. Update DOCS.md (if needed)
2. Handle open items:
   - For each open item, ASK: "Should [Item X] go to Beads? (cross-session)"
   - User confirms → `bd create --title "..." --body "..."`
   - User declines → Keep in plan file for next iteration
   - If no open items remain: clear plan file (overwrite with single space)
3. Ask: "New cycle or done for now?"
