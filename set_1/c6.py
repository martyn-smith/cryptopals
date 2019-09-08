"""
set 1 challenge 6:  (from https://cryptopals.com/sets/1/challenges/6)


"""
from base64 import b64decode
from unittest import mock
from os.path import dirname, abspath
from scoring import freq_score, hamming_distance
from utils import find_key_length, break_single_xor

filename = dirname(abspath(__file__)) + "/" + "c6.dat"
#TODO: find a more pythonic way of accessing parent dir (i.e. "../"?)
check_filename = dirname(abspath(__file__))[:-5] + "/" + "play_that_funky_music.txt"

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
    #again, two characters are different.
    with open(filename) as f, open(check_filename) as g:
        ciphertxt = b64decode(f.read())
        with mock.patch("builtins.input", return_value = 29):
            plaintxt = multi_xor_decrypt(ciphertxt)
            test_plaintxt = g.read()
            assert plaintxt == test_plaintxt

def test_find_key_length():
    #this actually is broken.
    with open(filename) as f:      
        ciphertxt = b64decode(f.read())  
        key_length = find_key_length(ciphertxt, False)
        assert key_length == 29

if __name__ == "__main__":
    print(test_multi_xor_decrypt())

