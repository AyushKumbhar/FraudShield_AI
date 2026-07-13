from flask import Blueprint, render_template, request, session, redirect, url_for
from utils.predict import predict_transaction
from models.transaction import Transaction
from extensions import db

detect = Blueprint("detect", __name__)


@detect.route("/detect", methods=["GET", "POST"])
def fraud_detection():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    prediction = None

    if request.method == "POST":

        amount = float(request.form["amount"])
        hour = int(request.form["hour"])
        location = int(request.form["location"])
        card_present = int(request.form["card_present"])
        merchant = int(request.form["merchant"])

        prediction = predict_transaction(
            amount,
            hour,
            location,
            card_present,
            merchant
        )

        transaction = Transaction(
            user_id=session["user_id"],
            amount=amount,
            time=hour,
            location_risk=location,
            card_present=card_present,
            transaction_type=merchant,
            prediction=prediction
        )

        db.session.add(transaction)
        db.session.commit()

    return render_template(
        "detect.html",
        prediction=prediction
    )