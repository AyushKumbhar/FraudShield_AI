from flask import Blueprint, render_template, session, redirect, url_for
from models.transaction import Transaction

history = Blueprint("history", __name__)


@history.route("/history")
def view_history():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    transactions = Transaction.query.filter_by(
        user_id=session["user_id"]
    ).order_by(
        Transaction.created_at.desc()
    ).all()

    return render_template(
        "history.html",
        transactions=transactions
    )