#from cryptography.hazmat.primitives.ciphers.algorithms import AES
#from cryptography.hazmat.primitives.ciphers.modes import ECB
from base64 import b64decode
from s2utils import cbc_mode, to_ascii, BLOCK_SIZE
KEY = b"YELLOW SUBMARINE"
IV = b'\x00' * BLOCK_SIZE

def store_plaintxt():
    with open("./c10.dat") as f, open("../play_that_funky_music.txt", "w+") as g:
        ciphertxt = b64decode(f.read())
        plaintxt = to_ascii(cbc_mode(ciphertxt, KEY, IV))   
        print(f"writing... {plaintxt}")
        g.write(plaintxt)

def test_implement_cbc_mode():
    with open("./c10.dat") as f, open("../play_that_funky_music.txt") as g:
        ciphertxt = b64decode(f.read())
        plaintxt = to_ascii(cbc_mode(ciphertxt, KEY, IV))
        assert plaintxt == g.read()