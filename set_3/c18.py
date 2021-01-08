from base64 import b64decode
from Crypto.Cipher import AES
from utils import BLOCK_SIZE, make_chunks, to_ascii

ciphertxt = b64decode("L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==")
key = b"YELLOW SUBMARINE"
nonce = b"\x00" * BLOCK_SIZE

def ctr_mode(key, nonce):
    a = AES.new(key)
    while True:
        nonce = nonce[:8] + bytes([nonce[8] + 1]) + nonce[8:] 
        yield a.encrypt(nonce)

ctr = ctr_mode(key, nonce)
for chunk in make_chunks(ciphertxt):
    print(to_ascii(ciphertxt ^ next(ctr)))