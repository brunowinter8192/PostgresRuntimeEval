#!/bin/bash
ONLINE1_DIR="../../Dataset/Dataset_Online_1"
OPERATOR_DIR="../../Dataset/Dataset_Operator"
OUTPUT_DIR="./Evaluation"
LOG_FILE="$OUTPUT_DIR/progress.log"
MAX_JOBS=14
STRATEGIES="size"
TEMPLATES="Q1 Q3 Q4 Q5 Q6 Q7 Q8 Q9 Q10 Q12 Q13 Q14 Q18 Q19"

mkdir -p "$OUTPUT_DIR"
echo "Started: $(date)" > "$LOG_FILE"

for strategy in $STRATEGIES; do
    echo "Starting strategy: $strategy - $(date)" >> "$LOG_FILE"

    for template in $TEMPLATES; do
        echo "Starting template: $template - $(date)" >> "$LOG_FILE"

        TT_CSV="$ONLINE1_DIR/$template/Training_Training.csv"
        TV_CSV="$ONLINE1_DIR/$template/Training_Test.csv"
        TRAIN_CSV="$OPERATOR_DIR/$template/training.csv"
        TEST_CSV="$OPERATOR_DIR/$template/test.csv"

        queries=$(cut -d';' -f1 "$TEST_CSV" | tail -n +2 | sort -u)
        total=$(echo "$queries" | wc -l | tr -d ' ')
        echo "Template $template: $total queries" >> "$LOG_FILE"

        job_count=0
        index=0
        for query in $queries; do
            ((index++))
            (
                python3 workflow.py "$query" \
                    "$TT_CSV" \
                    "$TV_CSV" \
                    "$TRAIN_CSV" \
                    "$TEST_CSV" \
                    --output-dir "$OUTPUT_DIR" \
                    --strategy "$strategy"
                echo "$(date +%H:%M:%S) - $strategy - $template - $index/$total - $query - DONE" >> "$LOG_FILE"
            ) &

            ((job_count++))
            if ((job_count >= MAX_JOBS)); then
                wait
                job_count=0
            fi
        done
        wait
        echo "Finished template: $template - $(date)" >> "$LOG_FILE"
    done

    echo "Finished strategy: $strategy - $(date)" >> "$LOG_FILE"
done
echo "Finished all: $(date)" >> "$LOG_FILE"
