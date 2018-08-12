from random import random, randint
from s2utils import pad, generate_IV, generate_key, cbc_decrypt
from Crypto.Cipher import AES
KEY_SIZE = 16

def cbc(plaintxt):
    print(f"encrypting... {plaintxt}")
    return cbc_decrypt(plaintxt, generate_key(), generate_IV())

def ecb(plaintxt):
    print(f"encrypting... {plaintxt}")
    a = AES.new(generate_key(), AES.MODE_ECB)
    return a.decrypt(pad(plaintxt))

def encryption_oracle(plaintxt: bytes):
    left_pad, right_pad = (bytes([randint(0,0xff) for i in range(5,10)]),
                           bytes([randint(0,0xff) for i in range(5,10)]))
    plaintxt = pad(left_pad + plaintxt + right_pad)
    cipher = [cbc, ecb]
    #ciphertxt = cipher[randint(0,1)](plaintxt)
    ciphertxt = ecb(plaintxt)
    return ciphertxt

if __name__ == "__main__":
    plaintxt = bytes(input("enter string to encrypt: "), "utf-8")
    print(f"ciphertxt is: {encryption_oracle(plaintxt)}")