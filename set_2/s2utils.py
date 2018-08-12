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

def cbc_decrypt(ciphertxt: bytes, key: bytes, IV: bytes, block_size: int = BLOCK_SIZE):
    ciphertxt = pad(IV + ciphertxt, block_size)
    a = AES.new(key, AES.MODE_ECB)
    blocks = [ciphertxt[(i*BLOCK_SIZE):(i+1)*block_size] \
              for i in range(0, len(ciphertxt)//block_size)]
    plaintxt_blocks = []
    for i in range(0, len(ciphertxt)//block_size -1):
        cbc_block = (blocks[i], a.decrypt(blocks[i+1]))
        plaintxt_blocks.append(bytes([a ^ b for a, b in zip(cbc_block[0], cbc_block[1])]))
    plaintxt = ''.join([block.decode("ascii") for block in plaintxt_blocks])
    return plaintxt

