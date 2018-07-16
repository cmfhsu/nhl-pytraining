#!/usr/bin/env python

import re
rx_sep = re.compile(r"[^a-zA-Z]")  # match anything but a letter

with open('../DATA/poe_sonnet.txt') as POE:
    for index,line in enumerate(POE):
        line = rx_sep.sub('',line)  # delete non-letters
        print(line[index], end=' ')  # print Nth character

print()
