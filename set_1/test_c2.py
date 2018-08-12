message = bytes.fromhex("686974207468652062756c6c277320657965")
key = bytes.fromhex("1c0111001f010100061a024b53535009181c")

def test_fixed_XOR():
    out = bytes(a ^ b for a, b in zip(message, key))
    out = bytes.hex(out)
    assert out == "746865206b696420646f6e277420706c6179"