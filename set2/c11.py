"""
set 2 challenge 11: ECB/CBC detection oracle (from https://cryptopals.com/sets/2/challenges/11)

The tricky part here is choosing a plaintext - it needs to be long enough so that the 
role of the left and right padding - essentially another IV - is minimised.  At the 
same time, too long a plaintext and you will have repititions even in CBC mode.

48 seems to work (cribbed from the internet - 3 * 16).
"""
from targets import encryption_oracle
from utils import BLOCK_SIZE, KEY_SIZE

def detect_ECB_mode(ciphertxt):
    blocks = [ciphertxt[(i*BLOCK_SIZE):(i+1)*BLOCK_SIZE] for i in range(0, len(ciphertxt)//BLOCK_SIZE)]
    #print(blocks)
    return any(blocks.count(block) > 1 for block in blocks)

def count_ECB_mode(num_samples = 1000, plaintxt_size = 48):
    ECB_count = 0
    for _ in range(0, num_samples):
        known_plaintxt = bytes([0x42] * plaintxt_size)
        ciphertxt = encryption_oracle(known_plaintxt)
        if detect_ECB_mode(ciphertxt):
            ECB_count += 1
    return ECB_count

if __name__ == "__main__":
    num_samples = 1000
    ECB_count = count_ECB_mode(num_samples)
    print(f"detected ECB in {ECB_count} of {num_samples} samples")

