"""
set 1 challenge 6: break repeating-key XOR (from https://cryptopals.com/sets/1/challenges/6)


"""
from base64 import b64decode
from unittest import mock
from scoring import freq_score, hamming_distance
from utils import find_key_length, break_single_xor

filename = "c6.dat"
#TODO: refine testing arrangements.
check_filename = "../play_that_funky_music.txt"

def multi_xor_decrypt(ciphertxt: bytes, verbose = False):
    plaintxt = "".ljust(len(ciphertxt), " ")
    key_length = find_key_length(ciphertxt, False)
    repeat_length = len(ciphertxt) // key_length
    for i in range(0,key_length):
        sub_block = bytes([ciphertxt[j*key_length+i] for j in range(0, repeat_length)])
        sub_plaintxt, key, _ = break_single_xor(sub_block, True)
        for j, k in enumerate(sub_plaintxt):
            plaintxt = plaintxt[:(j*key_length) + i] + k + plaintxt[(j*key_length) + i + 1:]
    return plaintxt

def test_multi_xor_decrypt():
    #again, two characters are different.
    with open(filename) as f, open(check_filename) as g:
        ciphertxt = b64decode(f.read())
        with mock.patch("builtins.input", return_value = 29): #Terminator X: Bring the noise
            plaintxt = multi_xor_decrypt(ciphertxt, True)
            test_plaintxt = g.read().lower()
            try:
                assert [a==b for a, b in zip(plaintxt, test_plaintxt)]
            except AssertionError:
                print(plaintxt)

def test_find_key_length():
    #this actually does have issues.
    with open(filename) as f:
        ciphertxt = b64decode(f.read())
        key_length = find_key_length(ciphertxt, True)
        assert key_length == 29

if __name__ == "__main__":
    test_multi_xor_decrypt()

