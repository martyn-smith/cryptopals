"""
CBC bitflipping attacks (from https://cryptopals.com/sets/2/challenges/16)

"""

from Crypto.Cipher import AES
from utils import BLOCK_SIZE, generate_key, generate_IV, pad

a = AES.new(generate_key(), AES.MODE_CBC, generate_IV())

def surrounded_CBC(msg):
    prefix = "comment1=cooking%20MCs;userdata="
    postfix = ";comment2=%20like%20a%20pound%20of%20bacon"
    msg = prefix.replace(";","").replace("=","") + msg.replace(";","").replace("=","") + postfix.replace(";","").replace("=","")
    return a.encrypt(pad(bytes(msg, encoding="utf-8")))

def find_admin_string(msg):
    return "admin=true" in msg

def bitflip_cbc():
    ciphertext = surrounded_CBC("   " + "admin" + chr(0) + "true")
    target = a.decrypt(ciphertext).index(b"admin") + 5 - BLOCK_SIZE
    ciphertext = ciphertext[0:target] + bytes([ciphertext[target] ^ ord("=")]) + ciphertext[target+1:]
    new_plaintxt = "".join([chr(i) for i in a.decrypt(ciphertext)])
    return find_admin_string(new_plaintxt)

if __name__ == "__main__":
    print(bitflip_cbc())
