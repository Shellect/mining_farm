import json

from ecdsa import SigningKey, NIST256p, VerifyingKey, BadSignatureError


def generate_keys():
    private_key = SigningKey.generate(curve=NIST256p)
    public_key = private_key.get_verifying_key()
    return (private_key.to_string().hex(),
            public_key.to_string().hex())


def sign_transaction(private_key: str, transaction) -> str:
    private_key = SigningKey.from_string(bytes.fromhex(private_key), curve=NIST256p)
    tx_data = json.dumps(transaction.to_dict(), sort_keys=True).encode()
    signature = private_key.sign(tx_data)
    return signature.hex()


def verify_signature(public_key: str, transaction, signature) -> bool:
    public_key = VerifyingKey.from_string(bytes.fromhex(public_key), curve=NIST256p)
    tx_data = json.dumps(transaction.to_dict(), sort_keys=True).encode()
    signature = bytes.fromhex(signature)
    try:
        return public_key.verify(signature, tx_data)
    except BadSignatureError:
        return False