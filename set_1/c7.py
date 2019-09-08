"""
set 1 challenge 7:  implement AES (from https://cryptopals.com/sets/1/challenges/7)

Gaining familiarity with basic usage of AES decryption modules.
"""

#from cryptography.hazmat.primitives.ciphers.algorithms import AES
#from cryptography.hazmat.primitives.ciphers.modes import ECB
from base64 import b64decode
from os.path import dirname, abspath
from Crypto.Cipher import AES

filename = dirname(abspath(__file__)) + "/" + "c7.dat"
#TODO: find a more pythonic way of accessing parent dir (i.e. "../"?)
check_filename = dirname(abspath(__file__))[:-5] + "/" + "play_that_funky_music.txt"

key = b"YELLOW SUBMARINE"

def test_AES_ECB_decrypt(filename = filename, key = key):
    with open(filename) as f, open(check_filename) as g:
        ciphertxt = b64decode(f.read())
        a = AES.new(key, AES.MODE_ECB)
        plaintxt = ''.join([chr(i) for i in a.decrypt(ciphertxt)])
        test_plaintxt = g.read()
        #test plaintext is not padded, AES-decrypted is
        assert plaintxt[:-6] == test_plaintxt
