# Thesis Prediction Methods - Justfile
# Usage: just <recipe> [args]

set shell := ["bash", "-cu"]

# Default: show available commands
default:
    @just --list --unsorted

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
