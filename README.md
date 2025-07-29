# Machine Learning-Based Voltage and Frequency Control for Energy-Efficient GPU Computing

This repository contains the full implementation of a predictive DVFS control system for GPU computing using machine learning.

## 📁 Repository Structure
- `external/` – Git submodules from HPC-ULisboa:
  - `gpuPTXModel`: CUDA benchmark kernels
  - `gpowerSAMPLER`: Power sampling tool
- `experiments/` – Logs, power traces, and output plots
- `datasets/` – Raw and processed CSVs for training
- `models/` – Trained ML models (.pkl)
- `deployment/` – Runtime controller code
- `scripts/` – All automation scripts and notebooks

## 🔧 How to Use

```bash
# Clone with submodules
git clone --recurse-submodules https://github.com/your-username/ml-dvfs-gpu-control.git
cd ml-dvfs-gpu-control

# Step 1: Run all kernels and collect logs
bash run_all_benchmarks.sh

# Step 2: Aggregate logs into training dataset
python3 aggregate_logs.py

# Step 3: Train ML model
python3 train_model.py

# Step 4: Visualize prediction accuracy
python3 predict_and_plot.py

# Step 5: Simulate live inference (adjustable for real deployment)
python3 dvfs_runtime_controller.py
