"""
set 2 challenge 11: ECB/CBC detection oracle (from https://cryptopals.com/sets/2/challenges/11)

The tricky part here is choosing a plaintext - it needs to be long enough so that the 
role of the left and right padding - essentially another IV - is minimised.  At the 
same time, too long a plaintext and you will have repititions even in CBC mode.

48 seems to work (cribbed from the internet - 3 * 16).
"""
from random import random, randint
from Crypto.Cipher import AES
from utils import pad, generate_IV, generate_key, cbc_mode, to_ascii, find_key_length
from scoring import hamming_distance

#TODO: refine test arrangements.
KEY_SIZE = 16
BLOCK_SIZE = 16

def cbc(plaintxt):
    #print(f"encrypting... {plaintxt}")
    return cbc_mode(plaintxt, generate_key(), generate_IV())

def ecb(plaintxt):
    #print(f"encrypting... {plaintxt}")
    a = AES.new(generate_key(), AES.MODE_ECB)
    return a.encrypt(pad(plaintxt))

def encryption_oracle(plaintxt: bytes):
    """
    Randomly chooses an encryption mode (cbc or ecb), and encrypts it.
    """
    left_pad, right_pad = (bytes([randint(0,0xff) for _ in range(0,randint(5, 10))]),
                           bytes([randint(0,0xff) for _ in range(0,randint(5, 10))]))
    plaintxt = pad(left_pad + plaintxt + right_pad)
    cipher = (cbc, ecb)
    ciphertxt = cipher[randint(0,1)](plaintxt)
    return ciphertxt

def detect_ECB_mode(ciphertxt):
    blocks = [ciphertxt[(i*BLOCK_SIZE):(i+1)*BLOCK_SIZE] for i in range(0, len(ciphertxt)//BLOCK_SIZE)]
    #print(blocks)
    return any(blocks.count(block) > 1 for block in blocks)

def test_detect_ECB_mode(num_samples = 1000, plaintxt_size = 48):
    ECB_count = 0
    for _ in range(0, num_samples):
        known_plaintxt = bytes([0x42] * plaintxt_size)
        ciphertxt = encryption_oracle(known_plaintxt)
        if detect_ECB_mode(ciphertxt):
            #print("ECB mode found")
            ECB_count += 1
    print(f"detected ECB in {ECB_count} of {num_samples} samples")
    assert 0.45 < (ECB_count / num_samples) < 0.55

if __name__ == "__main__":
    test_detect_ECB_mode()

