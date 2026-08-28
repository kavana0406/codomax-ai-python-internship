# Codomax Internship - Task 5
# AI-Based Battery Health Prediction System

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Create simulated battery data
np.random.seed(42)

data = {
    "Voltage": np.round(np.random.uniform(3.2, 4.2, 100), 2),
    "Current": np.round(np.random.uniform(0.5, 5.0, 100), 2),
    "Temperature": np.round(np.random.uniform(20, 60, 100), 1),
    "Charging_Cycles": np.random.randint(50, 1000, 100)
}

df = pd.DataFrame(data)

# Generate a simulated battery health score
df["Health_Score"] = (
    40 * (df["Voltage"] - 3.2)
    + 25 * (1 - (df["Current"] - 0.5) / 4.5)
    + 20 * (1 - (df["Temperature"] - 20) / 40)
    + 15 * (1 - (df["Charging_Cycles"] - 50) / 950)
)

# Create health categories
df["Health_Status"] = pd.cut(
    df["Health_Score"],
    bins=[-np.inf, 35, 65, np.inf],
    labels=["Critical", "Warning", "Healthy"]
)

# Prepare ML data
X = df[["Voltage", "Current", "Temperature", "Charging_Cycles"]]
y = df["Health_Status"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Test model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("======================================")
print("   AI BATTERY HEALTH PREDICTION")
print("======================================")

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# User input
print("\nEnter battery details:")

voltage = float(input("Voltage (V): "))
current = float(input("Current (A): "))
temperature = float(input("Temperature (°C): "))
cycles = int(input("Charging Cycles: "))

new_battery = pd.DataFrame({
    "Voltage": [voltage],
    "Current": [current],
    "Temperature": [temperature],
    "Charging_Cycles": [cycles]
})

prediction = model.predict(new_battery)[0]

print("\n--------------------------------------")
print("Battery Health Prediction:", prediction)
print("--------------------------------------")
