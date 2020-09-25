from flask import Blueprint, Flask, redirect, render_template, request

from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.user_repository as user_repository
import repositories.merchant_repository as merchant_repository

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    merchants = merchant_repository.select_all()
    return render_template("transactions/index.html", transactions=transactions, merchants = merchants)