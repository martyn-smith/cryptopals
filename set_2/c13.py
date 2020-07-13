"""
set 2 challenge 13: ECB cut-and-paste (from https://cryptopals.com/sets/2/challenges/13)

Given an AES-ECB encrypted profile, and the key, generate a valid ciphertext that would decrypt to
the same profile, with 'role' changed from 'user' to 'admin'.
"""
from Crypto.Cipher import AES
from utils import depad, generate_key, pad, to_ascii

def parse_profile(x : str) -> dict:
    k_v_pairs = x.split("&")
    key_values = [k_v.split("=") for k_v in k_v_pairs]
    profile = dict(key_values)
    return profile

def unparse_profile(profile : dict) -> str:
    return ''.join([f"{item}={profile[item]}&" for item in profile])[:-1]

def test_parse():
    profile = parse_profile("foo=bar&baz=qux&zap=zazzle")
    assert profile == {"foo" : "bar", "baz" : "qux", "zap" : "zazzle"}
    assert unparse_profile(profile) == "foo=bar&baz=qux&zap=zazzle"

def profile_for(email_addr : str):
    assert type(email_addr) == str
    email_addr = email_addr.strip("&").strip("=")
    uid=10
    role="user"
    key = generate_key()
    profile = parse_profile(f"email={email_addr}&uid={uid}&role={role}")
    a = AES.new(key, AES.MODE_ECB)
    return key, a.encrypt(pad(bytes(unparse_profile(profile), "utf-8")))

def change_role():
    key, ciphertext = profile_for("foo@bar.com")
    a = AES.new(key, AES.MODE_ECB)
    plaintext = to_ascii(depad(a.decrypt(ciphertext)))
    plaintext = plaintext.replace("user", "admin")
    print(ciphertext)
    print(a.encrypt(pad(bytes(plaintext, "utf-8"))))

if __name__ == "__main__":
    change_role()