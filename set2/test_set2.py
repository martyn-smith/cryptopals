test_filename = "../play_that_funky_music.txt"

def test_challenge_9():
    from c9 import padding
    assert padding() == b"YELLOW SUBMARINE\x04\x04\x04\x04"

def test_challenge_10():
    from c10 import implement_cbc_mode
    with open(test_filename) as f:
        test_plaintxt = f.read()
    plaintxt = implement_cbc_mode()
    assert plaintxt[:16] == test_plaintxt[:16]

def test_challenge_11():
    from c11 import count_ECB_mode
    num_samples = 1000
    ECB_count = count_ECB_mode(num_samples)
    assert 0.45 < (ECB_count / num_samples) < 0.55

def test_challenge_12():
    from c12 import ECB_bytewise_decrypt
    assert ECB_bytewise_decrypt()[:-1] == \
"""\
Rollin' in my 5.0
With my rag-top down so my hair can blow
The girlies on standby waving just to say hi
Did you stop? No, I just drove by
"""

def test_challenge_13():
    from c13 import change_role
    from utils import to_ascii, depad
    assert "role=admin" in to_ascii(depad(change_role()))

def test_challenge_14():
    from c14 import ECB_bytewise_decrypt
    assert ECB_bytewise_decrypt() == \
"""\
Rollin' in my 5.0
With my rag-top down so my hair can blow
The girlies on standby waving just to say hi
Did you stop? No, I just drove by
"""

def test_challenge_15():
    from c15 import validate_pad
    #correct
    validate_pad(b"ICE ICE BABY\x04\x04\x04\x04")
    #incorrect
    try:
        validate_pad(b"ICE ICE BABY\x05\x05\x05\x05")
        validate_pad(b"ICE ICE BABY\x01\x02\x03\x04")
    except AssertionError:
        pass

def test_challenge_16():
    from c16 import bitflip_cbc
    assert(bitflip_cbc())