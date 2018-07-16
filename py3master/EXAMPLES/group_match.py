#!/usr/bin/env python

import re

r = re.compile(r"([a-z])[,;:/](\d+)")

s = "a,123 b;456 c:989 f/134"
matches = r.findall(s)
print(matches)
print()

for m in r.finditer(s):
    for num in range(3):
        print("({0}) {1}".format(num,m.group(num)), end=' ')
    print()

