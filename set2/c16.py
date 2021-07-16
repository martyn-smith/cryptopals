"""
set 2 challenge 16: CBC bitflipping attacks (from https://cryptopals.com/sets/2/challenges/16)

"""

from Crypto.Cipher import AES
from utils import BLOCK_SIZE, generate_key, generate_IV, pad

key = generate_key()
IV = generate_IV()
a, b = AES.new(key, AES.MODE_CBC, IV), AES.new(key, AES.MODE_CBC, IV)

def surrounded_CBC(msg):
    prefix = "comment1=cooking%20MCs;userdata="
    postfix = ";comment2=%20like%20a%20pound%20of%20bacon"
    msg = prefix.replace(";","").replace("=","") + msg.replace(";","").replace("=","") + postfix.replace(";","").replace("=","")
    return a.encrypt(pad(bytes(msg, encoding="utf-8")))

def bitflip_cbc():
    ciphertext = surrounded_CBC("   " + "admin" + chr(0) + "true")
    target = b.decrypt(ciphertext).index(b"admin") + 5 - BLOCK_SIZE
    ciphertext = ciphertext[0:target] + bytes([ciphertext[target] ^ ord("=")]) + ciphertext[target+1:]
    new_plaintxt = "".join([chr(i) for i in b.decrypt(ciphertext)])
    return "admin=true" in new_plaintxt

if __name__ == "__main__":
    print(bitflip_cbc())
