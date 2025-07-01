from entities.transaction import Transaction
from exceptions import InsufficientFundsError
from infrastructure.crypto import generate_keys, sign_transaction


class Wallet:
    def __init__(self):
        self.private_key, self.public_key = generate_keys()
        self.balance = 0.0

    def create_transaction(self, amount: float, recipient: str):
        if self.balance < amount:
            raise InsufficientFundsError(self.public_key, self.balance, amount)

        transaction = Transaction(self.public_key, recipient, amount)
        signature = sign_transaction(self.private_key, transaction)
        transaction.signature = signature
        return transaction
