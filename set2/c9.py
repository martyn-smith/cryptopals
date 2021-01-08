"""
set 2 challenge 9: implement PCKS#7 padding (from https://cryptopals.com/sets/2/challenges/9)

Similar to challenge 1, essentially checking familiarity with the padding algorithm.
"""
from utils import pad
plaintxt = b"YELLOW SUBMARINE"

def padding(plaintxt = plaintxt):
    return pad(plaintxt, 20)

def test_padding():
    assert padding() == b"YELLOW SUBMARINE\x04\x04\x04\x04"

if __name__ == "__main__":
    print(padding())