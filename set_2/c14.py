"""
set 2 challenge 14: Byte-at-a-time ECB decryption (Harder) (from https://cryptopals.com/sets/2/challenges/14)

Using the function from #12, with a random count of random bytes prepended to every plaintext, i.e.:

AES-128-ECB(random-prefix || attacker-controlled || target-bytes, random-key)
"""