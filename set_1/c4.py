"""
set 1 challenge 4: find and break a single-char xor (from https://cryptopals.com/sets/1/challenges/4)

Slightly harder than challenge 3, as you have to find the ciphered line first.
"""
from os.path import dirname, abspath
from utils import break_single_xor

filename = dirname(abspath(__file__)) + "/" + "c4.dat"

def find_single_xor(filename = filename):
    with open(filename) as f:
        score = 0
        key = ""
        plaintxt = ""
        best_line = 0
        for line_num, line in enumerate(f):
            trial_ciphertxt = bytes.fromhex(line.strip())
            trial_plaintxt, line_key, line_score = break_single_xor(trial_ciphertxt, True)
            if line_score > score:
                score = line_score
                key = line_key
                plaintxt = trial_plaintxt
                best_line = line_num
    print(f"best key is {key}, on line {best_line}.  plaintext is: \n {plaintxt} \n score is {score}")
    return (plaintxt, best_line, key, score)

def test_find_single_xor():
    plaintxt, __, __, __ = find_single_xor()
    assert plaintxt == "now that the party is jumping\n"

if __name__ == "__main__":
    print(find_single_xor())



        
