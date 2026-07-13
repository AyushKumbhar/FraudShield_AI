import joblib

# Load trained model
model = joblib.load("models/fraud_model.pkl")

def predict_transaction(amount, time, location_risk, card_present, transaction_type):
    prediction = model.predict([[amount, time, location_risk, card_present, transaction_type]])

    if prediction[0] == 1:
        return "Fraud Detected"
    else:
        return "Legitimate Transaction"