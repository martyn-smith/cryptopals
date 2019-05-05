"""
set 2 challenge 11: ECB/CBC detection oracle (from https://cryptopals.com/sets/2/challenges/11)
"""
import sys
sys.path.append('..')
from random import random, randint
from set_1.scoring import hamming_distance
from set_1.utils import find_key_length
from utils import pad, generate_IV, generate_key, cbc_mode, to_ascii
from Crypto.Cipher import AES
KEY_SIZE = 16

def cbc(plaintxt):
    #print(f"encrypting... {plaintxt}")
    return cbc_mode(plaintxt, generate_key(), generate_IV())

def ecb(plaintxt):
    #print(f"encrypting... {plaintxt}")
    a = AES.new(generate_key(), AES.MODE_ECB)
    return a.decrypt(pad(plaintxt))

def encryption_oracle(plaintxt: bytes):
    """
    Randomly chooses an encryption mode (cbc or ecb), and encrypts it.
    """
    left_pad, right_pad = (bytes([randint(0,0xff) for i in range(5,10)]),
                           bytes([randint(0,0xff) for i in range(5,10)]))
    plaintxt = pad(left_pad + plaintxt + right_pad)
    cipher = (cbc, ecb)
    ciphertxt = cipher[randint(0,1)](plaintxt)
    #ciphertxt = cbc(plaintxt)
    return ciphertxt

def test_oracle(num_samples = 20):
    known_plaintxt = bytes(KEY_SIZE)
    ciphertxt = encryption_oracle(known_plaintxt)
    _ = find_key_length(ciphertxt, True)
    print(f"ciphertext = {ciphertxt[0:20]}...")

if __name__ == "__main__":
    test_oracle()

