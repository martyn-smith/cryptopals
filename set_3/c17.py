""" 
Vaudenay's attack.
Generate a random AES key (which it should save for all future encryptions), 
pad the string out to the 16-byte AES block size and CBC-encrypt it under that key, providing the caller the ciphertext and IV.
"""

from base64 import b64decode
from Crypto.Cipher import AES
from random import choice
from utils import BLOCK_SIZE, generate_key, generate_IV, pad, depad, InvalidPaddingError

key, IV = generate_key(), generate_IV()
a = AES.new(key, AES.MODE_CBC, IV)

def cbc_oracle(ciphertxt):
    try:
        depad(a.decrypt(ciphertxt))
        return True
    except InvalidPaddingError:
        return False


def make_pad(intermediate: bytes) -> bytes:
    pad = bytes()
    l = len(intermediate)
    for i in intermediate:
        pad = bytes([l ^ int(i)]) + pad
    # print(f"I = {len(intermediate)}, pad = {len(pad)}")
    # print(pad)
    return pad

with open("c17.dat") as f:
    line = choice([b64decode(line) for line in f.readlines()])
    ciphertxt = a.encrypt(pad(line))

print(len(ciphertxt))
intermediate = bytes()
for i in range(1, BLOCK_SIZE+1):
    pos = BLOCK_SIZE+i
    for test_char in range(0xff): 
        trial_ciphertxt = ciphertxt[:-pos] + bytes([test_char]) + make_pad(intermediate) + ciphertxt[-BLOCK_SIZE:]
        if cbc_oracle(trial_ciphertxt):
            intermediate = bytes([test_char ^ i ^ ciphertxt[pos]]) + intermediate
            print(intermediate)
            break
