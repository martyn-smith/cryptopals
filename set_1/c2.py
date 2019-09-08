"""
set 1 challenge 2: fixed XOR (from https://cryptopals.com/sets/1/challenges/2)

Similar to challenge 1, but checking you can use the ^ operator.
"""
message = bytes.fromhex("686974207468652062756c6c277320657965")
key = bytes.fromhex("1c0111001f010100061a024b53535009181c")

def fixed_XOR(message = message, key = key):
    out = bytes(a ^ b for a, b in zip(message, key))
    return bytes.hex(out)

def test_c2():
    assert fixed_XOR() == "746865206b696420646f6e277420706c6179"

if __name__ == "__main__":
    print(fixed_XOR())