"""
set 2 challenge 12: Byte-at-a-time ECB decryption (from https://cryptopals.com/sets/2/challenges/12)

We're going to cheat a bit, initially at least: we already know it's AES with 16-byte blocks.
"""
from base64 import b64decode
from itertools import combinations
from Crypto.Cipher import AES
from utils import BLOCK_SIZE, generate_key, pad, to_ascii

filename = "c12.dat"
key = generate_key()
a = AES.new(key, AES.MODE_ECB)

def prepended_ECB(plaintxt):
    with open(filename) as f:
        msg = b64decode(f.read()) #bytes
    return a.encrypt(pad(plaintxt + msg, BLOCK_SIZE))

def ECB_bytewise_decrypt():
    block_size = BLOCK_SIZE #cheating because I'm lazy
    block_count = 0
    plaintxt = ""  
    while True:
        start_byte, end_byte = block_count * block_size, ((block_count + 1) * block_size) - 1
        prev_block = (None if block_count == 0 else plaintxt_block)
        plaintxt_block = []
        try:
            for i in range(block_size - 1, -1, -1):
                substitutions = [prepended_ECB(bytes([0x00] * i)
                                                + bytes(plaintxt, encoding="utf-8") 
                                                + bytes(plaintxt_block) 
                                                + bytes([j]))[start_byte : end_byte] 
                                    for j in range(0, 0xff)]
                #block with zeros until the byte being tested.
                msg = prepended_ECB(bytes([0x00] * i))
                attack_block = msg[start_byte : end_byte]
                #print(f"block = {attack_block}")
                plaintxt_block.append(substitutions.index(attack_block))
        except ValueError:
            print(f"cannot match at block {block_count}, quitting. \n")
            plaintxt += "".join([chr(p) for p in plaintxt_block])
            break
        plaintxt += "".join([chr(p) for p in plaintxt_block])
        block_count += 1
    return plaintxt

def test_ECB_bytewise_decrypt():
    assert ECB_bytewise_decrypt() == \
"""
Rollin' in my 5.0
With my rag-top down so my hair can blow
The girlies on standby waving just to say hi
Did you stop? No, I just drove by
"""

if __name__ == "__main__":
    print(ECB_bytewise_decrypt())