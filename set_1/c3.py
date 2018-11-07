from utils import break_single_xor
ciphertxt = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
#assuming the intending encoding is ascii, based on the previous - mapping one byte to one char. 
#print(f"key is {key}, plaintext is: \n {plaintxt} \n score is {score}")

def single_xor():
    plaintxt, __, score = break_single_xor(ciphertxt, True)
    return plaintxt, score
