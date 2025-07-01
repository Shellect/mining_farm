class CryptoException(Exception):
    """Базовое исключение для всех ошибок системы"""
    pass


class InsufficientFundsError(CryptoException):
    """
    Исключение 'Недостаточно средств на счете'
    """

    def __init__(self, address: str, balance: float, amount: float):
        super().__init__(f"Insufficient funds in {address}: balance {balance}" \
                         + f", tried to send {amount}")

class InvalidTransactionError(CryptoException):
    """Некорректная транзакция"""
    def __init__(self, tx_hash: str, reason: str):
        self.tx_hash = tx_hash
        self.reason = reason
        super().__init__(f"Invalid transaction {tx_hash}: {reason}")


class InvalidSignatureError(CryptoException):
    """Неверная подпись транзакции"""

    def __init__(self, tx_hash: str):
        self.tx_hash = tx_hash
        super().__init__(f"Invalid signature for transaction {tx_hash}")