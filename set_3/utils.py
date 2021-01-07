
from Crypto.Cipher import AES
from os import urandom
BLOCK_SIZE = 16
KEY_SIZE = 16
MIN_KEY_LENGTH = 5
MAX_KEY_LENGTH = 40

class InvalidPaddingError(Exception):
    pass

class FailedDecryptionError(Exception):
    pass

def pad(plaintxt: bytes, block_size: int = BLOCK_SIZE) -> bytes:
    diff = block_size - (len(plaintxt) % block_size)
    padding = bytes([diff] * diff)
    return plaintxt + padding

def depad(plaintxt: bytes, block_size: int = BLOCK_SIZE - 1) -> bytes:
    pad = plaintxt[-1]
    #print(f"{pad=}")
    if pad > block_size or plaintxt[-pad:].count(pad) != pad:
        raise InvalidPaddingError
    #print(f"valid pad: {plaintxt[-pad:]}")
    return plaintxt[:-pad]

def generate_IV(size: int = BLOCK_SIZE) -> bytes:
    return urandom(size)

def generate_key(size: int = KEY_SIZE) -> bytes:
    return urandom(size)

def to_ascii(text: bytes) -> str:
    #pretty certain there's a more standard way of doing this.
    return "".join(chr(i) for i in text)