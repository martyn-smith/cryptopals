from Crypto.Cipher import AES
from os import urandom
BLOCK_SIZE = 16
KEY_SIZE = 16

def pad(plaintxt: bytes, block_length: int = BLOCK_SIZE):
    #print(f"incoming length = {len(plaintxt)}")
    diff = block_length - (len(plaintxt) % block_length)
    padding = diff.to_bytes(1, byteorder = "big") * diff
    plaintxt = plaintxt + padding
    return plaintxt

def generate_IV(size: int = BLOCK_SIZE):
    return urandom(size)

def generate_key(size: int = KEY_SIZE):
    return urandom(size)

def to_ascii(text: bytes) -> str:
    #pretty certain there's a more standard way of doing this.
    return "".join(chr(i) for i in text)
    #return ''.join([bytes([char]).decode("ascii", "backslashreplace") for char in text])

def cbc_mode(ciphertxt: bytes, key: bytes, IV: bytes, block_size: int = BLOCK_SIZE) -> bytes:
    ciphertxt = pad(IV + ciphertxt, block_size)
    a = AES.new(key, AES.MODE_ECB)
    blocks = [ciphertxt[(i*BLOCK_SIZE):(i+1)*block_size] \
              for i in range(0, len(ciphertxt)//block_size)]
    plaintxt_blocks = []
    for i in range(0, len(ciphertxt)//block_size -1):
        cbc_block = (blocks[i], a.decrypt(blocks[i+1]))
        plaintxt_blocks.append(bytes([a ^ b for a, b in zip(cbc_block[0], cbc_block[1])]))
    plaintxt = b''.join([block for block in plaintxt_blocks])
    return plaintxt