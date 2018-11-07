from scoring import freq_score, hamming_distance
from base64 import b64decode
from utils import find_key_length, break_single_xor
from unittest import mock

def multi_xor_decrypt(ciphertxt: bytes, verbose = False):
    plaintxt = "".ljust(len(ciphertxt), " ")
    key_length = find_key_length(ciphertxt, True)
    key = "".ljust(key_length, " ")
    repeat_length = len(ciphertxt) // key_length
    for i in range(0,key_length):
        sub_block = bytes([ciphertxt[j*key_length+i] for j in range(0, repeat_length)])
        sub_plaintxt = break_single_xor(sub_block)
        #sub_plaintxt = ''.join([chr(i) for i in sub_block])
        for j, k in enumerate(sub_plaintxt):
            #print("0123456789012345678901234567890123456789012345678901234567890123456789")
            plaintxt = plaintxt[:(j*key_length) + i] + k + plaintxt[(j*key_length) + i + 1:]
    return (plaintxt, key) if verbose else plaintxt      

def test_multi_xor_decrypt():
    with open("./c6.dat") as f, open("../play_that_funky_music.txt") as g:
        ciphertxt = b64decode(f.read())
        with mock.patch("builtins.input", return_value = 29):
            plaintxt = multi_xor_decrypt(ciphertxt)
            test_plaintxt = g.read()
            assert plaintxt == test_plaintxt

def test_find_key_length():
    with open("./c6.dat") as f:      
        ciphertxt = b64decode(f.read())  
        key_length = find_key_length(ciphertxt, False)
        assert key_length == 29



