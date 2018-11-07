from utils import break_single_xor
from os.path import dirname, abspath
print(__file__)
filename = dirname(abspath(__file__)) + "c4.dat"

def find_single_xor():
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





        
