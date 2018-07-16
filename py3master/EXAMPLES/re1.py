#!/usr/bin/env python
import re
r = re.compile(r"\d{2,}")
with open("../DATA/spam.txt") as sp:
    for line in sp:
        if r.search(line):
            print(line, end=' ')
