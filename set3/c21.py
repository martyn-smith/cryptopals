"""
Set 3 Challenge 21: Implement the Mersenne Twister (https://cryptopals.com/sets/3/challenges/21)
"""

def MT19937(seed):
    """
    The series x is defined as a series of w-bit quantities with the recurrence relation:

    x_{k+n} = x_{k+m} ⊕ ( ( (x_k-upper , x_{k + 1}-lower )  * A ) k = 0 , 1,

    ⊕ = the bitwise exclusive or (XOR), -u means the upper w − r bits of xk, and -l means the lower r bits of xk+1. 
    The twist transformation A is defined in rational normal form as: 
  
    x * A = match x_0
        0 => x >> 1
        1 => x >> 1 ⊕ a 

    where x_0 is the lowest order bit of x. 
    """

    w = 32
    max_int = 1 << w
    r = 31
    n = 624
    m = 397
    a = 0x9908b0df

    #TODO: upper should be upper (w-r = 1) bits, lower should be lower (r=31) bits
    upper = lambda x : x >> r
    lower = lambda x : x & (1 << (r+1)) - 1
    lowest = lambda x: x % 2
    A = lambda x : (x >> 1 if lowest(x) == 0 else (x >> 1) ^ a) % max_int

    def init(seed):
        f = 1812433253
        x = [seed]
        for i in range(1, n):
            x.append((f * (x[-1] ^ (x[-1] >> (w - 2))) + i) % max_int)
        return x

    def twist(x):
        for k in range(n):
            x.append((x[k+m] ^ A(upper(x[k]) | lower(x[k+1]))) % max_int)
        return x[-n:]

    def temper(x):
        (u, d) = (11, 0xffffffff)
        (s, b) = (7, 0x9d2c5680)
        (t, c) = (15, 0xefc60000)
        l = 18
        y = (x ^ ((x >> u) & d)) % max_int
        y = (y ^ ((y << s) & b)) % max_int
        y = (y ^ ((y << t) & c)) % max_int
        return (y ^ (y << l)) % max_int

    assert(0 < seed < max_int)

    x = init(seed)
    #x = twist(x)
    
    i = 0
    while True:
        if i == n:
            x = twist(x)
            i = 0
        #temper(42) = 1521226794
        yield temper(x[i]) #temper(x[i])
        i += 1

if __name__ == "__main__":
    t = MT19937(42)
    for _ in range(1):
        print(next(t))