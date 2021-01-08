"""
set 1 challenge 8: find AES encryption (from https://cryptopals.com/sets/1/challenges/8)

Shades of challenge 4 here, objective is to detect AES-encrypted lines in ECB mode.

The weakness with ECB mode is that it is stateless and deterministic: 
the same block will always produce the same ciphertext.
"""
from base64 import b64decode
from Crypto.Cipher import AES

filename =  "c8.dat"
key = b'0000000000000000'
BLOCK_SIZE = 16

def detect_ECB_mode(ciphertxt):
    blocks = [ciphertxt[(i*BLOCK_SIZE):(i+1)*BLOCK_SIZE] for i in range(0, len(ciphertxt)//BLOCK_SIZE)]
    return any(blocks.count(block) > 1 for block in blocks)

def find_ECB_line(filename = filename, key = key):
    with open(filename) as f:
        for line_num, line in enumerate(f):
            if detect_ECB_mode(b64decode(line)):           
                print(f"line number {line_num} may be encrypted in ECB mode.  line is:\n {line}")
                return line_num

def test_find_ECB_line():
    line_num = find_ECB_line() 
    assert line_num == 132 

if __name__ == "__main__":
    print(find_ECB_line())

