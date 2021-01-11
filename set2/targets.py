from Crypto.Cipher import AES
from random import randint
from utils import cbc_mode, generate_IV, generate_key, pad

def cbc(plaintxt):
    #print(f"encrypting... {plaintxt}")
    return cbc_mode(plaintxt, generate_key(), generate_IV())

def ecb(plaintxt):
    #print(f"encrypting... {plaintxt}")
    a = AES.new(generate_key(), AES.MODE_ECB)
    return a.encrypt(pad(plaintxt))

def encryption_oracle(plaintxt: bytes):
    """
    Randomly chooses an encryption mode (cbc or ecb), and encrypts it.
    """
    left_pad, right_pad = (bytes([randint(0,0xff) for _ in range(0,randint(5, 10))]),
                           bytes([randint(0,0xff) for _ in range(0,randint(5, 10))]))
    plaintxt = pad(left_pad + plaintxt + right_pad)
    cipher = (cbc, ecb)
    ciphertxt = cipher[randint(0,1)](plaintxt)
    return ciphertxt