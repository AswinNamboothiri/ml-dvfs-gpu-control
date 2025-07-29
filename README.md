# Machine Learning-Based Voltage and Frequency Control for Energy-Efficient GPU Computing

This repository contains all code, scripts, models, benchmarks, and results used in our project, based on predictive DVFS modeling for GPU power optimization using machine learning.

## 📂 Project Structure
- `kernels/`: CUDA compute and memory benchmarks
- `gpowerSAMPLER/`: Power sampling tool for NVIDIA GPUs
- `data_collection/`: Scripts to collect power, performance, and frequency data
- `datasets/`: Raw and processed data for ML model training
- `models/`: ML training code and saved models
- `deployment/`: Real-time ML-based DVFS controller
- `experiments/`: Plots, logs, and result summaries
- `paper/`: IEEE-format LaTeX paper and references
- `docs/`: PhD thesis and supporting documentation

## 🚀 How to Run
```bash
# Clone repo
git clone https://github.com/your-username/ml-dvfs-gpu-control.git
cd ml-dvfs-gpu-control

# Install dependencies
pip install -r requirements.txt

# Compile and run benchmark
cd kernels/
nvcc -o fp32_add fp32_add.cu
./fp32_add

# Power sample
cd ../gpowerSAMPLER
make
./bin/gpowerSAMPLER ../kernels/fp32_add

# Collect metrics and train ML model
cd ../models
python3 train_model.py

# Deploy DVFS controller
cd ../deployment
python3 dvfs_runtime_controller.py

