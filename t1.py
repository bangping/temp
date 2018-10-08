import os
import sys
from collections import defaultdict

def abbr(a, b, al, bl, mem):
    if (al, bl) in mem:
        return mem((al. bl))
    else:
        r = calc(a, b, al, bl, mem)
        mem[(al, bl)] = r
        return r

def calc(a, b, al, bl, mem):
    if al == 0:
        return bl == 0
    elif bl == 0:
        return a[:al].islower()

    c = a[al - 1]
    if c.isupper():
        if c != b[bl - 1]:
            return False
        else:
            return abbr(a, b, al - 1, bl - 1, mem)
    else:
        uc = c.upper()
        if uc != b[bl - 1]:
            return abbr(a, b, al - 1, bl, mem)
        else:
            return abbr(a, b, al - 1, bl, mem) or abbr(a, b, al - 1, bl - 1, mem)

def abbreviation(a, b):
    r = abbr(a, b, len(a), len(b), {})
    return 'YES' if r else 'NO'
