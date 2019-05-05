"""
set 1 challenge 8: find AES encryption (from https://cryptopals.com/sets/1/challenges/8)

Shades of challenge 4 here, objective is to detect AES-encrypted lines.
"""
from base64 import b64decode
from Crypto.Cipher import AES
from os.path import dirname, abspath

filename =  dirname(abspath(__file__)) + "/" + "c8.dat"
key = b'0000000000000000'
BLOCK_SIZE = 16

def find_AES_encryption(filename = filename, key = key):
    with open(filename) as f:
        for line_num, line in enumerate(f):
            line = b64decode(line)
            blocks = [line[(i*BLOCK_SIZE):(i+1)*BLOCK_SIZE] for i in range(0, len(line)//BLOCK_SIZE)]
            if any(blocks.count(block) > 1 for block in blocks):
                print(f"line number {line_num} may be encrypted.  line is:\n {line}")
                return line_num

if __name__ == "__main__":
    print(find_AES_encryption())

