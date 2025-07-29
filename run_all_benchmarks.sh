#!/bin/bash
# Script to compile and run GPU benchmarks and collect power logs

KERNEL_ROOT=external/gpuPTXModel/microbenchmarks
GPOWER=external/gpowerSAMPLER/bin/gpowerSAMPLER
OUTPUT_DIR=experiments/logs
FREQ_LIST=(300 600 900 1200 1500)

mkdir -p $OUTPUT_DIR
BENCHMARKS=("FP32/FP32_ADD" "INT/INT_ADD" "SHARED_MEM" "DRAM")

for BENCH in "${BENCHMARKS[@]}"; do
    BENCH_PATH="$KERNEL_ROOT/$BENCH"
    BENCH_NAME=$(basename $BENCH)

    echo "🔧 Compiling $BENCH_NAME..."
    nvcc -o "$BENCH_PATH/$BENCH_NAME" "$BENCH_PATH/$BENCH_NAME.cu"

    for FREQ in "${FREQ_LIST[@]}"; do
        echo "⚙️ Running $BENCH_NAME at ${FREQ}MHz"
        sudo nvidia-smi -ac 5001,$FREQ
        TIMESTAMP=$(date +%Y%m%d_%H%M%S)
        LOG_FILE="$OUTPUT_DIR/${BENCH_NAME}_${FREQ}MHz_${TIMESTAMP}.csv"
        $GPOWER "$BENCH_PATH/$BENCH_NAME" > "$LOG_FILE"
        sleep 5
    done
done
