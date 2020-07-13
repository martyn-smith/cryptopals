
from Crypto.Cipher import AES
from os import urandom
BLOCK_SIZE = 16
KEY_SIZE = 16
MIN_KEY_LENGTH = 5
MAX_KEY_LENGTH = 40

def pad(plaintxt: bytes, block_length: int = BLOCK_SIZE) -> bytes:
    #print(f"incoming length = {len(plaintxt)}")
    diff = block_length - (len(plaintxt) % block_length)
    padding = diff.to_bytes(1, byteorder = "big") * diff
    plaintxt = plaintxt + padding
    return plaintxt

def depad(plaintxt: bytes, block_length: int = BLOCK_SIZE) -> bytes:
    pad = plaintxt[-1]
    if plaintxt[:pad:-1].count(pad) == pad:
        return plaintxt[:-pad]
    #invalid padding?
    #raise InvalidPaddingError:

def generate_IV(size: int = BLOCK_SIZE) -> bytes:
    return urandom(size)

def generate_key(size: int = KEY_SIZE) -> bytes:
    return urandom(size)

def to_ascii(text: bytes) -> str:
    #pretty certain there's a more standard way of doing this.
    return "".join(chr(i) for i in text)
    #return ''.join([bytes([char]).decode("ascii", "backslashreplace") for char in text])

def cbc_mode(ciphertxt: bytes, key: bytes, IV: bytes, block_size: int = BLOCK_SIZE) -> bytes:
    ciphertxt = pad(IV + ciphertxt, block_size)
    a = AES.new(key, AES.MODE_ECB)
    blocks = [ciphertxt[(i*BLOCK_SIZE):(i+1)*block_size] for i in range(0, len(ciphertxt)//block_size)]
    plaintxt_blocks = []
    for i in range(0, len(ciphertxt)//block_size -1):
        cbc_block = (blocks[i], a.decrypt(blocks[i+1]))
        plaintxt_blocks.append(bytes([a ^ b for a, b in zip(cbc_block[0], cbc_block[1])]))
    plaintxt = b''.join([block for block in plaintxt_blocks])
    return plaintxt

def find_key_length(ciphertxt: bytes, verbose = False):
    score = 0
    for trial_key_length in range(MIN_KEY_LENGTH, MAX_KEY_LENGTH+1):
        trial_score = (hamming_distance(ciphertxt[0:trial_key_length], 
                                        ciphertxt[trial_key_length:(2*trial_key_length)]) 
                        / trial_key_length)
        if verbose:
            print(f"{trial_key_length}\t{trial_score:.3f}")
        if trial_score < score or not (score):
            key_length = trial_key_length
            score = trial_score
    if verbose:
        man_kl = input(f"auto-determined key length is: {key_length}\n" 
                        "Use different key length? Type RET to continue with " 
                        "auto-determined length\n")
        key_length = int(man_kl) if man_kl else key_length
    return key_length

def hamming_distance(bytestr_1: bytes, bytestr_2: bytes):
    #print([i for i in zip(bytestr_1, bytestr_2)])
    score = sum(hamming_byte(a,b) for a, b in zip(bytestr_1, bytestr_2))
    return score

def hamming_byte(a,b):
    x = a^b
    score = sum(1 for i in range(0,8) if (x >> i) % 2)
    #print(f"{bin(a)} ({a})\t{bin(b)} ({b})\t{bin(x)}\t{score}")
    return score