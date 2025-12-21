#!/bin/bash
DATASET_DIR="../../Hybrid_2/Dataset/Baseline"
OUTPUT_DIR="./Evaluation"
LOG_FILE="$OUTPUT_DIR/progress.log"
MAX_JOBS=6
STRATEGIES="error size frequency"

mkdir -p "$OUTPUT_DIR"
echo "Started: $(date)" > "$LOG_FILE"

queries=$(cut -d';' -f1 "$DATASET_DIR/Test.csv" | tail -n +2 | sort -u)
total=$(echo "$queries" | wc -l | tr -d ' ')
echo "Total queries: $total" >> "$LOG_FILE"
echo "Strategies: $STRATEGIES" >> "$LOG_FILE"

for strategy in $STRATEGIES; do
    echo "Starting strategy: $strategy - $(date)" >> "$LOG_FILE"
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
                --output-dir "$OUTPUT_DIR" \
                --strategy "$strategy"
            echo "$(date +%H:%M:%S) - $strategy - $index/$total - $query - DONE" >> "$LOG_FILE"
        ) &

        ((job_count++))
        if ((job_count >= MAX_JOBS)); then
            wait
            job_count=0
        fi
    done
    wait
    echo "Finished strategy: $strategy - $(date)" >> "$LOG_FILE"
done
echo "Finished all: $(date)" >> "$LOG_FILE"
