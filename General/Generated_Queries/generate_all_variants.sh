#!/bin/bash

set -euo pipefail

DBGEN_DIR="$1"
OUTPUT_DIR="$2"
REFERENCE_FILE="$DBGEN_DIR/reference/cmd_qgen_sf1"

TEMPLATES=(17 20)

for template in "${TEMPLATES[@]}"; do
    TEMPLATE_DIR="$OUTPUT_DIR/Q$template"
    mkdir -p "$TEMPLATE_DIR"
    
    counter=1
    while IFS= read -r line; do
        if [[ $line =~ -r[[:space:]]+([0-9]+) ]]; then
            seed="${BASH_REMATCH[1]}"
            output_file="$TEMPLATE_DIR/Q${template}_${counter}_seed_${seed}.sql"
            
            (cd "$DBGEN_DIR" && DSS_QUERY=./queries ./qgen -s 1 -r "$seed" "$template") > "$output_file"
            
            ((counter++))
        fi
    done < "$REFERENCE_FILE"
done
