#!/usr/bin/env python

import sys
import re

wordsep = re.compile(r"[^\w']+")

for fname in sys.argv[1:]:
    with open(fname) as f:
        found = {}
        for line in f:
            words = wordsep.split(line)
            for x in words:
                if x == "": continue
                if x == "'": continue
                x = x.lower()
                if x in found:
                    found[x] += 1
                else:
                    found[x] = 1    
    
    words = list(found.keys())
    for w in sorted(words):
        print("{0:<16s} {1:4d}".format(w,found[w]))

        
