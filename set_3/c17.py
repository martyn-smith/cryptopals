""" ... generate a random AES key (which it should save for all future encryptions), 
pad the string out to the 16-byte AES block size and CBC-encrypt it under that key, providing the caller the ciphertext and IV.
"""

from base64 import b64decode
from Crypto.Cipher import AES
from random import choice
from utils import BLOCK_SIZE, generate_key, generate_IV, pad, depad, InvalidPaddingError

key, IV = generate_key(), generate_IV()
a = AES.new(key, AES.MODE_CBC, IV)

def cbc_oracle(ciphertxt):
    depad(a.decrypt(ciphertxt))

with open("c17.dat") as f:
    line = choice([b64decode(line) for line in f.readlines()])
    ciphertxt = a.encrypt(pad(line))
    plaintxt = ""
    def get_pad():
        for i in range(BLOCK_SIZE):
            target = len(ciphertxt) - (BLOCK_SIZE * 2) + i
            test_ctxt = ciphertxt[:target] + bytes([0xff]) + ciphertxt[target+1:]
            try:
                cbc_oracle(test_ctxt)
            except InvalidPaddingError:
                return BLOCK_SIZE - i
    pad = get_pad()
    # for test_char in range(0xff):
    #         target = len(ciphertxt) - BLOCK_SIZE
    #         try:
    #             #print(ciphertxt)
    #             #print(ciphertxt[:target] + bytes([test_char]) + ciphertxt[target+1:])
    #             cbc_oracle(ciphertxt[:target] + bytes([test_char]) + ciphertxt[target+1:])
    #             #test_char is valid
    #             pad = ciphertxt[target] ^ (test_char ^ 1)
    #             print(pad)
    #             break
    #         except InvalidPaddingError:
    #             continue
    # for i in range(len(ciphertxt)):
    #     #print(f"testing... {i}")
    #     for test_char in range(0xff):
    #         target = len(ciphertxt) - BLOCK_SIZE - i
    #         try:
    #             cbc_oracle(ciphertxt[:target] + bytes([test_char]) + ciphertxt[target+1:])
    #             #test_char is valid
    #             plaintxt += chr((test_char ^ i+1) ^ ciphertxt[target + BLOCK_SIZE - 1])
    #             break
    #         except InvalidPaddingError:
    #             continue
    # print(plaintxt[::-1])