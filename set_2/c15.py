from utils import pad

def validate_pad(text: bytes) -> bytes:
    pad_length = int(text[-1])
    pre_pad = text[:-pad_length]
    try:
        assert text[-pad_length:] == bytes([pad_length] * pad_length) 
    except AssertionError:
        print(f"Text {text} has been improperly padded.\nprepad: {pre_pad}") 
    try:
        assert len(pre_pad) + pad_length == len(text)
    except AssertionError:
        print(f"Text {text} has been improperly padded.\nlength:{pad_length}") 
    return pre_pad

def test_validate_pad():
    #correct
    validate_pad(b"ICE ICE BABY\x04\x04\x04\x04")
    #incorrect
    validate_pad(b"ICE ICE BABY\x05\x05\x05\x05")
    validate_pad(b"ICE ICE BABY\x01\x02\x03\x04")

if __name__ == "__main__":
    test_validate_pad()