#!/usr/bin/env python

import sys

if len(sys.argv) < 3:
    print("Syntax: count_words.py PATTERN FILE ...")
    sys.exit()

pattern = sys.argv[1]

for fname in sys.argv[2:]:
    count = 0
    with open(fname) as f:
        for line in f:
            if pattern in line:
                count += 1
                
    print('''"{0}" occurred on  {1} lines in {2}'''.format(pattern,count,fname))
