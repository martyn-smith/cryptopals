test_filename = "../play_that_funky_music.txt"

def test_challenge_1():
    from c1 import b64_encoder
    assert b64_encoder() == b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

def test_challenge_2():
    from c2 import fixed_xor
    assert fixed_xor() == "746865206b696420646f6e277420706c6179"

def test_challenge_3():
    from c3 import single_xor
    plaintxt, score = single_xor()
    assert plaintxt == "cooking mc's like a pound of bacon"
    assert score == 153

def test_challenge_4():
    from c4 import find_single_xor
    plaintxt, __, __, __ = find_single_xor()
    assert plaintxt == "now that the party is jumping\n"

def test_challenge_5():
    from c5 import repeating_xor
    test_ciphertxt = bytes.fromhex("0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324"
                               "272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165"
                               "286326302e27282f")
    assert repeating_xor()[:40] == test_ciphertxt[:40]

def test_challenge_6():
    pass

def test_challenge_7():
    from c7 import AES_ECB_decrypt
    with open(test_filename) as f:
        test_plaintxt = f.read()
    plaintxt = AES_ECB_decrypt()
    #test plaintext is not padded, AES-decrypted is
    assert plaintxt[:-6] == test_plaintxt

def test_challenge_8():
    from c8 import find_ECB_line
    assert find_ECB_line() == 132