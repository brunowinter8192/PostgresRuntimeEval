#!/bin/bash
DATASET_DIR="../../Hybrid_7/Dataset/Baseline"
OUTPUT_DIR="./output"
LOG_FILE="$OUTPUT_DIR/progress.log"
MAX_JOBS=14

mkdir -p "$OUTPUT_DIR"
echo "Started: $(date)" > "$LOG_FILE"

queries=$(cut -d';' -f1 "$DATASET_DIR/Test.csv" | tail -n +2 | sort -u)
total=$(echo "$queries" | wc -l | tr -d ' ')
echo "Total queries: $total" >> "$LOG_FILE"

job_count=0
index=0
for query in $queries; do
    ((index++))
    (
        python3 workflow.py "$query" \
            "$DATASET_DIR/Training_Training.csv" \
            "$DATASET_DIR/Training_Test.csv" \
            "$DATASET_DIR/Training.csv" \
            "$DATASET_DIR/Test.csv" \
            --output-dir "$OUTPUT_DIR"
        echo "$(date +%H:%M:%S) - $index/$total - $query - DONE" >> "$LOG_FILE"
    ) &

    ((job_count++))
    if ((job_count >= MAX_JOBS)); then
        wait
        job_count=0
    fi
done
wait
echo "Finished: $(date)" >> "$LOG_FILE"
