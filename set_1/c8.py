from base64 import b64decode
from Crypto.Cipher import AES
key = b'0000000000000000'
BLOCK_SIZE = 16

with open("./c8.dat") as f:
    for line_num, line in enumerate(f):
        line = b64decode(line)
        blocks = [line[(i*BLOCK_SIZE):(i+1)*BLOCK_SIZE] for i in range(0, len(line)//BLOCK_SIZE)]
        if any(blocks.count(block) > 1 for block in blocks):
            print(f"line number {line_num} may be encrypted.  line is {line}")
        #print(possible_ciphertxt)
    #a = AES.new(key, AES.MODE_ECB)
    #plaintxt = ''.join([chr(i) for i in a.decrypt(ciphertxt)])
    #print(plaintxt)