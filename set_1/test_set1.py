from c1 import b64_decoder
from c2 import fixed_XOR
from c3 import single_xor
from c4 import find_single_xor
from c5 import repeating_xor, test_ciphertxt

def test_c1():
    assert b64_decoder() == b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

def test_c2():
    assert fixed_XOR() == "746865206b696420646f6e277420706c6179"

def test_single_xor():
    plaintxt, score = single_xor()
    assert plaintxt == "cooking mc's like a pound of bacon"
    assert score == 153

def test_find_single_xor():
    plaintxt, __, __, __ = find_single_xor("./set_1/")
    assert plaintxt == "now that the party is jumping\n"

def test_repeating_xor():
    assert repeating_xor() == test_ciphertxt

