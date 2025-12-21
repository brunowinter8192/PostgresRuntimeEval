# Thesis Prediction Methods - Justfile
# Usage: just <recipe> [args]

set shell := ["bash", "-cu"]

# Default: show available commands
default:
    @just --list --unsorted

# ═══════════════════════════════════════════════════════════════════════════════
# GIT SHORTCUTS
# ═══════════════════════════════════════════════════════════════════════════════

# Quick commit with message
commit msg:
    git add -A
    git commit -m "{{msg}}"

# Commit with scope prefix
commit-scope scope msg:
    git add -A
    git commit -m "{{scope}}: {{msg}}"

# Show recent commits
log n="5":
    git log --oneline -{{n}}

# ═══════════════════════════════════════════════════════════════════════════════
# BEADS
# ═══════════════════════════════════════════════════════════════════════════════

# List open beads
beads:
    bd list -s open

# Create new bead
bead-new title:
    bd create "{{title}}" --label task --priority P2

# Add comment to bead
bead-comment id msg:
    bd comment {{id}} "{{msg}}"
