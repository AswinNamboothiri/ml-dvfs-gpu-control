# Plot predictions vs actual for trained ML model

import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv("datasets/processed/aggregated_dataset.csv")
X = df[["Frequency(MHz)", "Power(W)"]]
y = df["Runtime(ms)"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = joblib.load("models/dvfs_model.pkl")
y_pred = model.predict(X_test)

plt.figure(figsize=(10, 6))
plt.plot(y_test.values, label="Actual", marker='o')
plt.plot(y_pred, label="Predicted", marker='x')
plt.title("Predicted vs Actual Runtime")
plt.xlabel("Sample")
plt.ylabel("Runtime (ms)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("experiments/figures/runtime_prediction.png")
print("✅ Plot saved to experiments/figures/runtime_prediction.png")
