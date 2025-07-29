# ML model training script for DVFS prediction

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

df = pd.read_csv("datasets/processed/aggregated_dataset.csv")

X = df[["Frequency(MHz)", "Power(W)"]]
y = df["Runtime(ms)"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"✅ Model trained. MSE: {mse:.4f}")

import joblib
joblib.dump(model, "models/dvfs_model.pkl")
