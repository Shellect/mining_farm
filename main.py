import hashlib

from entities.block import Block


def hash_block(block: Block):
    sha = hashlib.sha256()
    sha.update(str(Block).encode('utf-8'))
    return sha.hexdigest()