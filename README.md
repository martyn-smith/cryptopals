# CRYPTOPALS

A simple attempt at the problems posed on the [cryptopals](https://cryptopals.com) website.

Each problem has a python file associated with it in the directory associated with the 
set that problem is in, e.g. set_1/c1.py for the very first problem. Each set is self-contained.

Common utilities, e.g. single-character frequency analysis, are located in the directory
associated with the problem set they are first encountered in, e.g. set_1/scoring.py for 
the above and hamming scoring.

Since the good folks at cryptopals have an odd fascination with "play that funky music",
the plaintext is located at root level for easier use by all problems.

## BUILT WITH

* python 3.8.6
* pytest