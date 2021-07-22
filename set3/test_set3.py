test_filename = "../data/ice_ice_baby.txt"

def test_challenge_17():
    from c17 import vaudenay
    with open(test_filename) as f:
        test_plaintxt = f.read()
    assert vaudenay() in test_plaintxt

def test_challenge_18():
    from c18 import ctr_mode
    assert ctr_mode() == "Yo, VIP Let's kick it Ice, Ice, baby Ice, Ice, b"

def test_challenge_21():
    from c21 import MT19937
    r = MT19937(42)
    assert next(r) == 1608637542

#True values:
# 1608637542
# 3421126067
# 4083286876
# 0787846414
# 3143890026
# 3348747335
# 2571218620
# 2563451924
# 0670094950
# 1914837113

def test_challenge_22():
    from c22 import crack
    assert crack() is not None
