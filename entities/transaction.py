from dataclasses import dataclass
from typing import Optional


@dataclass
class Transaction:
    sender: str
    recipient: str
    amount: float
    signature: Optional[str] = None
    tx_hash: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount,
            "signature": self.signature,
            "hash": self.tx_hash
        }
