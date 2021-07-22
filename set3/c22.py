"""
Set 3 challenge 22: crack an MT19937 seed (https://cryptopals.com/sets/3/challenges/22)
"""
from c21 import MT19937
from random import randint
import time

def generate():
    #    time.sleep(randint(40,1000))
    r = MT19937(int(time.time()) - 2000 + randint(80,2000))
    #    time.sleep(randint(40,1000))
    return next(r)

def crack():
    r = generate()
    start = int(time.time() - 2000)
    for i in range(2000):
        test = MT19937(start+i)
        if next(test) == r:
            return start+i

if __name__ == "__main__":
    print(crack())
    

