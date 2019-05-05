"""
set 2 challenge 10: Implement CBC mode (from https://cryptopals.com/sets/2/challenges/10) 

In CBC mode, each ciphertext block is added to the next plaintext block before the next
call to the cipher core.  (The 1st block has an IV).

In this case most of the heavy lifting is offloaded to s2utils.
"""
#from cryptography.hazmat.primitives.ciphers.algorithms import AES
#from cryptography.hazmat.primitives.ciphers.modes import ECB
from base64 import b64decode
from s2utils import cbc_mode, to_ascii, BLOCK_SIZE
from os.path import dirname, abspath

filename = dirname(abspath(__file__)) + "/" + "c10.dat"
KEY = b"YELLOW SUBMARINE"
IV = b'\x00' * BLOCK_SIZE

def store_plaintxt():
    with open("./c10.dat") as f, open("../play_that_funky_music.txt", "w+") as g:
        ciphertxt = b64decode(f.read())
        plaintxt = to_ascii(cbc_mode(ciphertxt, KEY, IV))   
        print(f"writing... {plaintxt}")
        g.write(plaintxt)

def implement_cbc_mode():
    with open("./c10.dat") as f:
        ciphertxt = b64decode(f.read())
        plaintxt = to_ascii(cbc_mode(ciphertxt, KEY, IV))
        return plaintxt

if __name__ == "__main__":
    print(implement_cbc_mode())