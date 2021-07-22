"""
Set 3 challenge 19: Break fixed-nonce CTR mode using substitutions (https://cryptopals.com/sets/3/challenges/19)
"""
from base64 import b64decode
from Crypto.Cipher import AES
from random import choice
from secrets import token_bytes

with open("c19.dat") as f:
    lines = [b64decode(line) for line in f.readlines()]

key = token_bytes(16)

def ctr_mode(line):
    a = AES.new(key, AES.MODE_CTR)
    return a.encrypt(line)

a, b = AES.new(key, AES.MODE_CTR, nonce = b'\x00'), AES.new(key, AES.MODE_CTR, nonce = b'\x00')

ciphertxt = [a.encrypt(line) for line in lines]
plaintxt = [b.decrypt(c) for c in ciphertxt]
print(plaintxt)
