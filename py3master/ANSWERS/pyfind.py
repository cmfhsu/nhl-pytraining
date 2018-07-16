#!/usr/bin/env python

import sys
import re

if len(sys.argv) < 3:
    print("Usage: pfind PATTERN file ...")

try:
    pat = re.compile(sys.argv[1])
except Exception as e:
    print("Error compiling RE: {0}".format(e))
    sys.exit()

for fname in sys.argv[2:]:
    try:
        f = open(fname)
    except IOError as e:
        print("Unable to open {0}: {1}".format(fname,e))
        continue
    else:
        for line in f:
            if pat.search(line):
                print("{0}: {1}".format(fname,line), end=' ')
        f.close()
    
