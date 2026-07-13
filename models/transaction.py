from datetime import datetime
from extensions import db


class Transaction(db.Model):

    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    amount = db.Column(db.Float, nullable=False)

    time = db.Column(db.Integer, nullable=False)

    location_risk = db.Column(db.Integer, nullable=False)

    card_present = db.Column(db.Integer, nullable=False)

    transaction_type = db.Column(db.Integer, nullable=False)

    prediction = db.Column(db.String(50), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)