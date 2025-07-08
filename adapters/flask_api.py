from flask import Flask, jsonify, request, render_template

from controller import load_json
from entities.transaction import Transaction
from exceptions import CryptoException, InvalidTransactionError, InvalidSignatureError
from infrastructure.crypto import verify_signature
from use_cases.wallet_operations import Wallet
from math import ceil

import json

app = Flask(__name__)


@app.errorhandler(CryptoException)
def handle_exception(e):
    return jsonify({
        "error": type(e).__name__,
        "message": str(e),
        "details": vars(e) if hasattr(e, '__dict__') else {}
    }), 400


@app.get("/")
def index():
    return render_template("base.html")


@app.get('/transaction_list')
def transaction_list():
    page = request.args.get('page', 1, type=int)
    transactions = load_json('transactions.json')
    transactions_len = len(transactions)
    total_pages = ceil(transactions_len / 4)
    start = (page - 1) * 4
    end = page * 4
    page_transactions = transactions[start:end]
    return render_template("transaction_list.html",
                           transactions=page_transactions,
                           current_page=page,
                           total_pages=total_pages,
                           has_next_page=page < total_pages,
                           has_previous_page=page > 1)


@app.get("/wallet/new")
def new_wallet():
    wallet = Wallet()
    return jsonify({
        "public_key": wallet.public_key,
        "balance": wallet.balance
    }), 201


@app.post("/transaction/new")
def new_transaction():
    values = request.get_json()
    if not all(k in values for k in [
        'sender', 'recipient', 'amount', 'signature'
    ]):
        raise InvalidTransactionError("unknown", "Missing required fields")

    transaction = Transaction(
        values["sender"], values["recipient"], values["amount"], values["signature"]
    )

    if not verify_signature(values["sender"], transaction, values["signature"]):
        raise InvalidSignatureError("unknown")


@app.get("/wallet")
def wallet_dashboard():
    return render_template("wallet_dashboard.html")


if __name__ == '__main__':
    app.run(debug=True)
