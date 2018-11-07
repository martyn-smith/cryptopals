from base64 import b64encode
hexstring = ("49276d206b696c6c696e6720796f757220627261696e206c"
             "696b65206120706f69736f6e6f7573206d757368726f6f6d")

def b64_decoder():
    plaintxt = bytes.fromhex(hexstring)
    return b64encode(plaintxt)