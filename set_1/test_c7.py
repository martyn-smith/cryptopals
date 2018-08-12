from base64 import b64decode
#from cryptography.hazmat.primitives.ciphers.algorithms import AES
#from cryptography.hazmat.primitives.ciphers.modes import ECB
from Crypto.Cipher import AES
key = b"YELLOW SUBMARINE"

def test_AES_ECB_decrypt():
    with open("./c7.dat") as f, open("../play_that_funky_music.txt") as g:
        ciphertxt = b64decode(f.read())
        a = AES.new(key, AES.MODE_ECB)
        plaintxt = ''.join([chr(i) for i in a.decrypt(ciphertxt)])
        test_plaintxt = g.read()
        assert plaintxt == test_plaintxt