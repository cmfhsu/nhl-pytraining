#!/usr/bin/env python
import sys

copyright_text = '''
The preceding joke (c) 1937 by LaffsaMinute,Inc.
'''

with open('../DATA/parrot.txt', 'a') as PARROT:
    PARROT.write(copyright_text)


