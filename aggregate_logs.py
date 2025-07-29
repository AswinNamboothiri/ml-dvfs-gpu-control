# Script to aggregate power/runtime logs into ML dataset

import os
import pandas as pd

log_dir = "experiments/logs"
output_file = "datasets/processed/aggregated_dataset.csv"
os.makedirs("datasets/processed", exist_ok=True)

all_data = []
for filename in os.listdir(log_dir):
    if filename.endswith(".csv"):
        parts = filename.replace(".csv", "").split("_")
        kernel = parts[0]
        freq = int(parts[1].replace("MHz", ""))
        df = pd.read_csv(os.path.join(log_dir, filename), names=["Power(W)", "Runtime(ms)"])
        df["Kernel"] = kernel
        df["Frequency(MHz)"] = freq
        all_data.append(df)

final_df = pd.concat(all_data)
final_df.to_csv(output_file, index=False)
print(f"✅ Aggregated dataset saved to {output_file}")
