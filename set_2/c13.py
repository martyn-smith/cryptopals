def parse_profile(x : str) -> dict:
    k_v_pairs = x.split("&")
    key_values = [k_v.split("=") for k_v in k_v_pairs]
    profile = dict(key_values)
