def freq_score(trial_txt):
    letters = "etaoin shrdlu"
    freqs = (13, 9, 8, 8, 7, 7, 6, 6, 6, 4, 4, 3)
    score = sum(trial_txt.count(letter) * freq for letter, freq in zip(letters, freqs))
    return score

def hamming_distance(bytestr_1: bytes, bytestr_2: bytes):
    #print([i for i in zip(bytestr_1, bytestr_2)])
    score = sum(hamming_byte(a,b) for a, b in zip(bytestr_1, bytestr_2))
    return score

def hamming_byte(a,b):
    x = a^b
    score = sum(1 for i in range(0,8) if (x >> i) % 2)
    #print(f"{bin(a)} ({a})\t{bin(b)} ({b})\t{bin(x)}\t{score}")
    return score

