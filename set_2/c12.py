from base64 import b64decode
hexstring = ("")

with open("./c12.dat") as f:
    mystery_txt = b64decode(f.read())

a = AES.new(generate_key(), AES.MODE_ECB)
b = a.decrypt(pad(plaintxt + mystery_txt))