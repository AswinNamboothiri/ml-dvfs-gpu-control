# Runtime DVFS controller using trained ML model

import joblib
import pandas as pd
import time
import random

model = joblib.load("models/dvfs_model.pkl")

def get_live_metrics():
    # Simulate metric collection (replace with real-time GPU reads)
    power = random.uniform(25.0, 80.0)
    freq = random.choice([300, 600, 900, 1200, 1500])
    return pd.DataFrame([[freq, power]], columns=["Frequency(MHz)", "Power(W)"]), freq

while True:
    X_live, curr_freq = get_live_metrics()
    predicted_runtime = model.predict(X_live)[0]
    print(f"Current Freq: {curr_freq} MHz | Power: {X_live['Power(W)'][0]:.2f} W | Predicted Runtime: {predicted_runtime:.2f} ms")

    # Optional: Adjust frequency based on some runtime heuristic
    time.sleep(5)
