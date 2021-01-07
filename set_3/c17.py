""" 
Vaudenay's attack.
Generate a random AES key (which it should save for all future encryptions), 
pad the string out to the 16-byte AES block size and CBC-encrypt it under that key, providing the caller the ciphertext and IV.
"""

from base64 import b64decode
from Crypto.Cipher import AES
from random import choice
from secrets import token_bytes
from utils import BLOCK_SIZE, generate_key, generate_IV, pad, depad, InvalidPaddingError, FailedDecryptionError
# from targets import cbc_oracle

key, IV = generate_key(), generate_IV()
a = AES.new(key, AES.MODE_CBC, IV)

def cbc_oracle(ciphertxt):
    try:
        depad(a.decrypt(ciphertxt))
        return True
    except InvalidPaddingError:
        return False

def make_pad(intermediate: bytes) -> bytes:
    pad = bytes()
    l = len(intermediate) + 1
    for i in intermediate[::-1]:
        pad = bytes([l ^ int(i)]) + pad
    #print(f"padded {intermediate} to {pad}")
    return pad

def make_chunks(ciphertext: str, chunk_size = BLOCK_SIZE) -> list:
    return [ciphertxt[i*BLOCK_SIZE:(i+1)*BLOCK_SIZE] for i in range(len(ciphertxt) // BLOCK_SIZE)]

with open("c17.dat") as f:
    line = choice([b64decode(line) for line in f.readlines()])
    ciphertxt = a.encrypt(pad(line))
    chunks = make_chunks(ciphertxt)
    assert chunks[-1] == ciphertxt[-BLOCK_SIZE:]
    # for c in chunks:
    #     print(c)
    #     print(len(c))

def decrypt_chunk(test_chunk, target_chunk):
    assert len(test_chunk) == len(target_chunk)
    block_size = len(target_chunk)
    intermediate = bytes()
    for i in range(1, block_size + 1):
        pos = block_size + i
        success = False
        for test_char in range(0xff): 
            trial_ciphertxt = token_bytes(block_size - i) + bytes([test_char]) + make_pad(intermediate) + target_chunk
            if cbc_oracle(trial_ciphertxt):
                success = True
                intermediate = bytes([test_char ^ i]) + intermediate
                print(f"{len(intermediate)} of {len(test_chunk)} bytes decrypted")
                break
        if not success:
            print(f"failed decryption at pos {i}")
    #print(len(intermediate))
    #print(len(test_chunk))
    return "".join([chr(i ^ c) for i, c in zip(intermediate, test_chunk[1:])])

# intermediate = bytes()
# for i in range(1, BLOCK_SIZE+1):
#     pos = BLOCK_SIZE+i
#     for test_char in range(0xff): 
#         trial_ciphertxt = ciphertxt[:-pos] + bytes([test_char]) + make_pad(intermediate) + ciphertxt[-BLOCK_SIZE:]
#         if cbc_oracle(trial_ciphertxt):
#             intermediate = bytes([test_char ^ i]) + intermediate
#             print(intermediate)
#             break

# print("".join([chr(i ^ c) for i, c in zip(intermediate, ciphertxt[-(2*BLOCK_SIZE)+1:-BLOCK_SIZE]) ]))
for (c1, c2) in zip(chunks[:-1], chunks[1:]):
    print(decrypt_chunk(c1, c2))
print(decrypt_chunk(chunks[-2], chunks[-1]))
