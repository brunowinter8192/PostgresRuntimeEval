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

## Activation Gate (CRITICAL)

On skill activation ALWAYS:

1. **Declare phase:** "📋 PLAN - Skill activated"
2. **Check context:**
   - What is the goal?
   - Which files are affected?
   - What is the current state?
3. **Establish or confirm context:**
   - New: Ask at least 3 questions
   - Continuation: "We were at [X], continue?"

**NEVER** go directly to IMPLEMENT without established context.

---

## Planning Phase (PLAN)

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

**CRITICAL: NO EDITS IN EVALUATE.** Only collect and report. All edits happen in IMPROVE.

**NO:**
- Summarizing what was implemented
- Making edits or fixes (that's IMPROVE)

**YES:**
- Content quality: Does the code/docs work correctly?
- Process quality: Was the planning efficient?

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

**Purpose:** Implement improvements identified in EVALUATE.

**CRITICAL:** This is where edits happen, NOT in EVALUATE.

1. Review improvement list from EVALUATE (including user feedback)
2. Implement each improvement
3. Ask: "Proceed to CLOSING?"

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
