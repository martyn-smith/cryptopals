"""
set 2 challenge 13: ECB cut-and-paste (from https://cryptopals.com/sets/2/challenges/13)
"""

def parse_profile(x : str) -> dict:
    k_v_pairs = x.split("&")
    key_values = [k_v.split("=") for k_v in k_v_pairs]
    profile = dict(key_values)
    return profile

def test_parse():
    profile = parse_profile("foo=bar&baz=qux&zap=zazzle")
    assert profile == {"foo" : "bar", "baz" : "qux", "zap" : "zazzle"}

def profile_for(email_addr: str):
    assert type(email_addr) == str
    email_addr = email_addr.strip(["&", "="])
    #remove metachars
    uid=10
    role="user"
    profile = parse_profile(f"email={email_addr}&uid={uid}&role={role}")
