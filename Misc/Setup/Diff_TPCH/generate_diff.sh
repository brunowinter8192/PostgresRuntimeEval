#!/bin/bash

OLD_DIR="$1"
NEW_DIR="$2"
OUTPUT_FILE="$3"

if [ -z "$OLD_DIR" ] || [ -z "$NEW_DIR" ] || [ -z "$OUTPUT_FILE" ]; then
    echo "Usage: ./generate_diff.sh <old_dir> <new_dir> <output_file>"
    exit 1
fi

diff -Nur \
  --exclude='*.o' \
  --exclude='*.tbl' \
  --exclude='dbgen' \
  --exclude='qgen' \
  --exclude='.DS_Store' \
  "$OLD_DIR" \
  "$NEW_DIR" \
  > "$OUTPUT_FILE"

echo "Diff generated: $OUTPUT_FILE"
