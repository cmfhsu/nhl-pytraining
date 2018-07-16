#!/usr/bin/env python

import sys

try:
    c = float(sys.argv[1])
except ValueError as e:
    print("Invalid number.")
    sys.exit()

f = ((9 * c) / 5 ) + 32

print("{0:.1f} C is {1:.1f} F".format(c,f))

