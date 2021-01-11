"""
set 1 challenge 3: break a single-byte xor cipher (from https://cryptopals.com/sets/1/challenges/3)

The first real 'challenge', it's mostly outsourced to a utility package here, since it's 
commonly used.
"""
from utils import break_single_xor

ciphertxt = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
#assuming the intending encoding is ascii, based on the previous - mapping one byte to one char. 

def single_xor(ciphertxt = ciphertxt):
    plaintxt, __, score = break_single_xor(ciphertxt, True)
    return plaintxt, score

if __name__ == "__main__":
    print(single_xor())