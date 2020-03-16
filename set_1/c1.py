"""
set 1 challenge 1: convert hex to base 64 (https://cryptopals.com/sets/1/challenges/1).

Essentially just checking you can use bytes.fromhex() and b64encode.
And begins the cryptopals tradition of questionable song lyrics as example text.
"""
from base64 import b64encode

hexstring = ("49276d206b696c6c696e6720796f757220627261696e206c"
             "696b65206120706f69736f6e6f7573206d757368726f6f6d")

def b64_encoder(hexstring = hexstring):
    plaintxt = bytes.fromhex(hexstring)
    return b64encode(plaintxt)

def test_b64_encoder():
    assert b64_encoder() == b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

if __name__ == "__main__":
    print(b64_encoder())