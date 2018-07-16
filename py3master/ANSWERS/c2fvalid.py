#!/usr/bin/env python

import sys

user_input = sys.argv[1]

if user_input.strip().replace('.','').isdigit():
    c = float(user_input)
    f = ((9 * c) / 5 ) + 32
    print("{0:.1f} C is {1:.1f} F".format(c,f))
else:
    print("Sorry, invalid number")
