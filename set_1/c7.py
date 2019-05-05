"""
set 1 challenge 7:  implement AES (from https://cryptopals.com/sets/1/challenges/7)

Gaining familiarity with basic usage of AES decryption modules.
"""

#from cryptography.hazmat.primitives.ciphers.algorithms import AES
#from cryptography.hazmat.primitives.ciphers.modes import ECB
from base64 import b64decode
from Crypto.Cipher import AES
from os.path import dirname, abspath

filename = dirname(abspath(__file__)) + "/" + "c7.dat"
key = b"YELLOW SUBMARINE"

def AES_ECB_decrypt(filename = filename, key = key):
    with open("./c7.dat") as f, open("../play_that_funky_music.txt") as g:
        ciphertxt = b64decode(f.read())
        a = AES.new(key, AES.MODE_ECB)
        plaintxt = ''.join([chr(i) for i in a.decrypt(ciphertxt)])
        test_plaintxt = g.read()
        assert plaintxt == test_plaintxt

if __name__ == "__main__":
    print(AES_ECB_decrypt())