"""
set 1 challenge 5: implement repeating-key XOR (from https://cryptopals.com/sets/1/challenges/5)

Another test of implementation of basic XOR encryption.
"""
from itertools import cycle

test_ciphertxt = bytes.fromhex("0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324"
                               "272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165"
                               "286326302e27282f")
plaintxt = b"Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key = b"ICE"

def repeating_xor(plaintxt = plaintxt, key = key):
    ciphertxt = bytes([p ^ k for p, k in zip(plaintxt, cycle(key))])
    return ciphertxt 

def test_repeating_xor():
    #a single character difference.
    assert repeating_xor() == test_ciphertxt

if __name__ == "__main__":
    print(repeating_xor())