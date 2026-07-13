import random
import pandas as pd

random.seed(42)

data = []

for _ in range(250):

    amount = random.randint(100, 100000)

    time = random.randint(0, 23)

    location_risk = random.randint(0, 1)

    card_present = random.randint(0, 1)

    transaction_type = random.randint(0, 5)

    fraud = 0

    if (
        amount > 50000
        and location_risk == 1
        and card_present == 0
    ):
        fraud = 1

    if (
        transaction_type in [2, 3, 4, 5]
        and amount > 70000
        and location_risk == 1
    ):
        fraud = 1

    data.append([
        amount,
        time,
        location_risk,
        card_present,
        transaction_type,
        fraud
    ])

df = pd.DataFrame(
    data,
    columns=[
        "amount",
        "time",
        "location_risk",
        "card_present",
        "transaction_type",
        "is_fraud"
    ]
)

df.to_csv(
    "datasets/transactions.csv",
    index=False
)

print("Dataset created successfully!")