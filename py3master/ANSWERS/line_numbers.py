#!/usr/bin/env python

import sys

for fname in sys.argv[1:]:
    with open(fname) as f:
        for num,line in enumerate(f,1):
            print("{0:4d}: {1}".format(num,line), end=' ')


