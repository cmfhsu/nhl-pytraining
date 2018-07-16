#!/usr/bin/env python
import re

fs = "apple banana artichoke cherry date enchilada appetizer"
r = re.compile(r"\b(a[a-z]+)(\s*)")
print(r.sub('',fs))
print(r.subn('XXX',fs))

def replace_it(m):
    return "'" + m.group(1) + "'" + m.group(2)
print(r.sub(replace_it,fs))
