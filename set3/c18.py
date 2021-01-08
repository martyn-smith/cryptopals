from base64 import b64decode
from Crypto.Cipher import AES
from utils import BLOCK_SIZE, make_chunks, to_ascii

ciphertxt = b64decode("L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==")
key = b"YELLOW SUBMARINE"
nonce = b"\x00" * BLOCK_SIZE

def ctr_mode(key, nonce):
    a = AES.new(key)
    while True:
        yield a.encrypt(nonce)
        nonce = nonce[:BLOCK_SIZE//2] + bytes([nonce[BLOCK_SIZE//2] + 1]) + nonce[(BLOCK_SIZE//2)+1:]

print("".join(
        ["".join([chr(c ^ i) for c, i in zip(chunk, ctr)]) 
            for chunk, ctr in zip(make_chunks(ciphertxt), ctr_mode(key, nonce))]))