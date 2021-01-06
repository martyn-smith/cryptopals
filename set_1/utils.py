from scoring import freq_score, hamming_distance
MIN_KEY_LENGTH = 5
MAX_KEY_LENGTH = 40

def break_single_xor(ciphertxt: bytes, verbose = False):
    """
    Trials a SINGLE character key, using basic frequency analysis to rank options and returning
    the highest-scoring plaintxt.
    """
    score = 0
    key = ""
    plaintxt = ""
    for trial_key in range(0,256):
        #print(f"trying... {chr(trial_key)}")
        trial_txt = bytes(trial_key ^ a for a in ciphertxt)
        trial_txt = "".join(chr(i) for i in trial_txt).lower()
        trial_score = freq_score(trial_txt)
        #print(trial_txt)
        if trial_score > score:
            score = trial_score
            key = chr(trial_key)
            plaintxt = trial_txt
    return (plaintxt, key, score) if verbose else plaintxt

def find_key_length(ciphertxt: bytes, verbose = False):
    score = 0
    for trial_key_length in range(MIN_KEY_LENGTH, MAX_KEY_LENGTH+1):
        chunks = [ciphertxt[i*trial_key_length:(i+1)*trial_key_length] for i in range(len(ciphertxt) // trial_key_length - 1)]
        trial_score = (sum(hamming_distance(i, j) for i, j in zip(chunks[:-1], chunks[1:]))
                        / trial_key_length)
        if verbose:
            print(f"{trial_key_length}\t{trial_score:.3f}")
        if trial_score < score or not (score):
            key_length = trial_key_length
            score = trial_score
    if verbose:
        man_kl = input(f"auto-determined key length is: {key_length}\n" 
                        "Use different key length? Press ENTER to continue with " 
                        "auto-determined length\n")
        key_length = int(man_kl) if man_kl else key_length
    return key_length