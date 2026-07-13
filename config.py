import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "FraudShield_AI_Secret_Key"

    SQLALCHEMY_DATABASE_URI = \
        "sqlite:///" + os.path.join(BASE_DIR, "database", "fraudshield.db")

    SQLALCHEMY_TRACK_MODIFICATIONS = False