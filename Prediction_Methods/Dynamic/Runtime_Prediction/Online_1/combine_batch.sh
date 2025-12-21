#!/bin/bash
# Runs both Online_1 batches sequentially

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=== Starting Online_1 (Static) ==="
cd ./Prediction_Methods/Online_1/Runtime_Prediction
./batch_predict.sh

echo "=== Starting Dynamic/Online_1 ==="
cd "$SCRIPT_DIR"
./batch_predict.sh

echo "=== All done ==="
