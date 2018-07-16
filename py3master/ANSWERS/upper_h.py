#!/usr/bin/env python
"""

@author: jstrick
Created on Tue Mar 19 22:32:23 2013

"""
import re

rx_kwords = re.compile(r'\bh[a-z]+')


with open('../DATA/alice.txt') as ALICE_IN:
    all_contents = ALICE_IN.read()
    new_contents = rx_kwords.sub(lambda m: m.group(0).upper(),all_contents)
    with open('../TEMP/alice_h.txt','w') as ALICE_OUT:
        ALICE_OUT.write(new_contents)


