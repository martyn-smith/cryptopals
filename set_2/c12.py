"""
set 2 challenge 12: Byte-at-a-time ECB decryption (from https://cryptopals.com/sets/2/challenges/12)

We're going to cheat a bit, initially at least: we already know it's AES with 16-byte blocks.
"""
from base64 import b64decode
from Crypto.Cipher import AES
from utils import BLOCK_SIZE, generate_key, pad, to_ascii

filename = "c12.dat"
key = generate_key()
a = AES.new(key, AES.MODE_ECB)

def prepended_ECB(prefix):
    with open(filename) as f:
        msg = b64decode(f.read())
    return a.encrypt(pad(prefix + msg, BLOCK_SIZE))

def ECB_bytewise_decrypt():
    block_size, block_count = BLOCK_SIZE, 0 #cheating a bit by assuming block size.
    plaintxt = ""
    try:
        while True:
            start_byte, end_byte = block_count * block_size, ((block_count + 1) * block_size) - 1
            for offset in range(block_size-1, -1, -1): #create a decreasing sliding mask
                msg = prepended_ECB(bytes(offset))[start_byte : end_byte]
                #create a mask with each possible plaintext value.
                #The bytes() function is a bit weird, and does three different things 
                #(zeros, str encode, char encode) here.
                test_msgs = [prepended_ECB(bytes(offset)
                                            + bytes(plaintxt, encoding="utf-8") 
                                            + bytes([test_char]))
                                    [start_byte : end_byte] 
                                    for test_char in range(0xff)]
                try:
                    plaintxt += chr(test_msgs.index(msg))
                except ValueError:
                    raise ValueError
            block_count += 1
    except ValueError:
        print(f"no matches for block {block_count}, quitting. \n")
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