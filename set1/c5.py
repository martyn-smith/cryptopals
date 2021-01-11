"""
set 1 challenge 5: implement repeating-key XOR (from https://cryptopals.com/sets/1/challenges/5)

Another test of implementation of basic XOR encryption.
"""
from itertools import cycle

plaintxt = b"Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key = b"ICE"

def repeating_xor(plaintxt = plaintxt, key = key):
    ciphertxt = bytes([p ^ k for p, k in zip(plaintxt, cycle(key))])
    return ciphertxt

if __name__ == "__main__":
    print(repeating_xor())