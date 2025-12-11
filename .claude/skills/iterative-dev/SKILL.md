---
name: iterative-dev
description: Manages iterative workflow with plan-implement cycles. Use when user mentions "iterativer workflow".
---

# Iterative Development Workflow

**Note:** This skill extends native Claude Code Plan Mode, not replaces it.
Follow all native Plan Mode rules. This adds:
- Phase indicators (📋/🔨)
- Iterative cycle structure
- Explicit file vs chat separation

## Phase Tracking

Every response starts with phase indicator:
- `📋 PLAN` - Planning phase (Plan Mode active)
- `🔨 IMPLEMENT` - Implementation phase

## Planning Phase Rules (📋 PLAN)

**Communication:**
- Chat = Brainstorming, Asking Questions
- Plan file = Key Points and Implementation
  - Use system-provided plan file path from Plan Mode message
  - **ALWAYS use Write/Edit tool to update plan file**
  - **NEVER write plan content directly in chat**
- One question at a time, based on previous answer

**Critical:**
- Plan file consists of:
    - 1. Takeaways from the chat
    - 2. How to implement those takeaways
- Plan file has to be iteratively extended until execution
- A good Plan file is not written at once
- If any brainstorming/changes: UPDATE plan file immediately

**Bash Tool calls and Edits:**
- if the interactive planning session requires the execution of certain modules to further refine the Plan, call exitplanmode and execute only what needs to be executed in order to refine the Plan file
- ask the user to manually return to plan mode after execution

**Before ExitPlanMode:**
- Plan file MUST reflect current HOW
- NEVER call ExitPlanMode with stale plan

## Implementation Phase Rules (🔨 IMPLEMENT)

**After completing each implementation step:**
- Ask: "Continue implementing or back to 📋 Plan?"

**Cycle:**
📋 PLAN → ExitPlanMode → 🔨 IMPLEMENT → 📋 PLAN (new plan)

**Critical: After Implementation**
- call update plan and fully empty the plan file, override with just ' ' --> CLEAR THE PLAN AFTER EACH SUCCESSFUL IMPLEMENTATION
- make sure everything in the plan file was executed accordingly
- if there are non executed points in the plan file, make sure to not override them and inform the user about the open points


