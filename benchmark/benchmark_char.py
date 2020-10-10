## https://stackoverflow.com/questions/16308989/fastest-method-to-generate-big-random-string-with-lower-latin-letters

from  random import random, getrandbits, choice
import time
import os, sys
from string import ascii_lowercase, ascii_uppercase

lowercase = True
_numrows = 10
if lowercase:
   min_lc = ord(b'a')
else:
    min_lc = ord(b'A')
len_lc = 26
ba = bytearray(os.urandom(_numrows))
for i, b in enumerate(ba):
    ba[i] = min_lc + b % len_lc  # convert 0..255 to 97..122
print(ba)
sys.stdout.buffer.write(ba)


if lowercase:
    bal = [c.encode('ascii') for c in ascii_lowercase]
else:
    bal = [c.encode('ascii') for c in ascii_uppercase]
a = [choice(bal) for _ in range(_numrows)]

print(a)