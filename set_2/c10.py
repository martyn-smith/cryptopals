"""
set 2 challenge 10: Implement CBC mode (from https://cryptopals.com/sets/2/challenges/10) 

In CBC mode, each ciphertext block is added to the next plaintext block before the next
call to the cipher core.  (The 1st block has an IV).

In this case most of the heavy lifting is offloaded to s2utils.
"""
#from cryptography.hazmat.primitives.ciphers.algorithms import AES
#from cryptography.hazmat.primitives.ciphers.modes import ECB
from base64 import b64decode
from utils import cbc_mode, to_ascii, BLOCK_SIZE

filename = "c10.dat" 
check_filename = "../play_that_funky_music.txt"
KEY = b"YELLOW SUBMARINE"
IV = b'\x00' * BLOCK_SIZE

def store_plaintxt():
    with open(filename) as f, open(check_filename, "w+") as g:
        ciphertxt = b64decode(f.read())
        plaintxt = to_ascii(cbc_mode(ciphertxt, KEY, IV))   
        print(f"writing... {plaintxt}")
        g.write(plaintxt)

def implement_cbc_mode():
    with open(filename) as f:
        ciphertxt = b64decode(f.read())
        plaintxt = to_ascii(cbc_mode(ciphertxt, KEY, IV))
        return plaintxt

def test_implement_cbc_mode():
    with open(check_filename) as g:
        plaintxt = implement_cbc_mode()
        test_plaintxt = g.read()
        assert plaintxt[:16] == test_plaintxt[:16]

if __name__ == "__main__":
    print(implement_cbc_mode())