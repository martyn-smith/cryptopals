from itertools import cycle
plaintxt = b"Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key = b"ICE"
test_ciphertxt = bytes.fromhex("0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324"
                               "272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165"
                               "286326302e27282f")

def test_repeating_xor():
    ciphertxt = bytes([p ^ k for p, k in zip(plaintxt, cycle(key))])
    assert ciphertxt == test_ciphertxt
