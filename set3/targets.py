def cbc_oracle(ciphertxt):
    try:
        depad(a.decrypt(ciphertxt))
        return True
    except InvalidPaddingError:
        return False