#!/bin/bash
# Runs Dynamic/Online_1 batch only (Online_1 Static already done)

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Online_1 (Static) - DONE 08:24:55
# echo "=== Starting Online_1 (Static) ==="
# cd /Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Online_1/Runtime_Prediction
# ./batch_predict.sh

echo "=== Starting Dynamic/Online_1 ==="
cd "$SCRIPT_DIR"
./batch_predict.sh

echo "=== All done ==="
