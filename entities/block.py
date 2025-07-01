from dataclasses import dataclass
import time


@dataclass
class Block:
    index: int
    data: list[str]
    previous_hash: str
    self_hash: str
    timestamp: float  = time.time()
