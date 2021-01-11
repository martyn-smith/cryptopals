"""
set 1 challenge 2: fixed XOR (from https://cryptopals.com/sets/1/challenges/2)

Similar to challenge 1, but checking you can use the ^ operator.
"""
message = bytes.fromhex("686974207468652062756c6c277320657965")
key = bytes.fromhex("1c0111001f010100061a024b53535009181c")

def fixed_xor(message = message, key = key):
    out = bytes(a ^ b for a, b in zip(message, key))
    return bytes.hex(out)

if __name__ == "__main__":
    print(fixed_XOR())