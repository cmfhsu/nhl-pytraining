#!/usr/bin/env python

import sys

if len(sys.argv) < 3:
    print("Syntax: count_words.py PATTERN FILE ...")
    sys.exit()

pattern = sys.argv[1].lower()

for fname in sys.argv[2:]:
    count = 0
    with open(fname) as f:
        for line in f:
            if pattern in line.lower():
                count += 1
    print('''"{0}" occured {1} times in {2}'''.format(pattern,count,fname))
