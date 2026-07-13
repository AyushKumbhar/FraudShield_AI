import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("datasets/transactions.csv")

# Features and target
X = data.drop("is_fraud", axis=1)
y = data["is_fraud"]

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, "models/fraud_model.pkl")

print("Fraud detection model trained successfully!")