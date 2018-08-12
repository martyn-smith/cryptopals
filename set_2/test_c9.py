from s2utils import pad
plaintxt = b"YELLOW SUBMARINE"

def test_padding():
    assert pad(b"YELLOW SUBMARINE", 20) == b'YELLOW SUBMARINE\x04\x04\x04\x04'
