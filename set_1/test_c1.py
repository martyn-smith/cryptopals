from base64 import b64encode
hexstring = ("49276d206b696c6c696e6720796f757220627261696e206c"
             "696b65206120706f69736f6e6f7573206d757368726f6f6d")

def test_b64_decoding():
    plaintxt = bytes.fromhex(hexstring)
    b64txt = b64encode(plaintxt)
    assert b64txt == b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"