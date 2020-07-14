"""
set 2 challenge 14: Byte-at-a-time ECB decryption (Harder) (from https://cryptopals.com/sets/2/challenges/14)

Using the function from #12, with a random count of random bytes prepended to every plaintext, i.e.:

AES-128-ECB(random-prefix || attacker-controlled || target-bytes, random-key)

...assume random no more than 16? 128?
"""

from base64 import b64decode
from Crypto.Cipher import AES
from itertools import combinations
from random import randint
from utils import BLOCK_SIZE, generate_IV, generate_key, pad, to_ascii

filename = "c12.dat" #apparently?
key = generate_key()
a = AES.new(key, AES.MODE_ECB)
MAXIMUM_ATTEMPTS = 256

def random_prepended_ECB(prefix : bytes) -> bytes:
    with open(filename) as f:
        plaintxt = b64decode(f.read())
    return a.encrypt(pad(generate_IV(randint(0,32)) + prefix + plaintxt, BLOCK_SIZE))

def find_null_cipher() -> bytes:
    ciphertxt = random_prepended_ECB(bytes(BLOCK_SIZE * 3))
    blocks = [ciphertxt[i:i+BLOCK_SIZE] for i in range(0, len(ciphertxt), BLOCK_SIZE)]
    for i in range(len(blocks)-1):
        if blocks[i] == blocks[i+1]:
            return blocks[i]

class MaximumAttemptsError(Exception):
    pass

def ECB_bytewise_decrypt():
    block_count = 0
    plaintxt = ""
    null_block = find_null_cipher()
    while True:
        try:
            attempts = 0
            matches = 0
            while True:
                msg = random_prepended_ECB(bytes(BLOCK_SIZE * 2)) #guarantees a null block
                #create a mask with each possible plaintext value.
                #since we don't know msg length (thanks to padding), offset is no longer controlled,
                #on each run we'll have a 1/16 chance of the correct char having the correct offset.
                test_msgs = [random_prepended_ECB(bytes(BLOCK_SIZE * 2)
                                            + bytes(plaintxt, encoding="utf-8") 
                                            + bytes([test_char]))
                                    for test_char in range(1, 0xff)] #need to remove 0 
                #remove the random preamble.
                msg = msg[msg.index(null_block)+1:]
                test_msgs = [t[t.index(null_block)+1:] for t in test_msgs]
                #print(f"{[len(t) for t in test_msgs]}\n\n")
                #search for matches.
                try:
                    plaintxt += chr(test_msgs.index(msg) - 1) #0! First match should be 82.
                    matches += 1
                    print(test_msgs.index(msg))
                except ValueError:
                    attempts += 1
                    if attempts > MAXIMUM_ATTEMPTS:
                        raise MaximumAttemptsError
                    continue
        except MaximumAttemptsError:
            print(f"maximum attempts at block {block_count} exceeded. Quitting")
            break
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