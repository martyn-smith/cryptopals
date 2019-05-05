"""
set 2 challenge 9: implement PCKS#7 padding (from https://cryptopals.com/sets/2/challenges/9)

Similar to challenge 1, essentially checking familiarity with the padding algorithm.
"""
from s2utils import pad
plaintxt = b"YELLOW SUBMARINE"

def padding(plaintxt = plaintxt):
    return pad(plaintxt, 20)

if __name__ == "__main__":
    print(padding())