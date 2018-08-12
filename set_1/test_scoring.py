from scoring import hamming_distance

def test_hamming_distance():
    str_1 = "this is a test"
    str_2 = "wokka wokka!!!"
    assert hamming_distance(bytes(str_1, "utf-8"), bytes(str_2, "utf-8")) == 37