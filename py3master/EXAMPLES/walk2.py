#!/usr/bin/env python
"""
    find files whose size is greater than 1000 bytes
"""
import sys
import os

if sys.platform == 'win32':
    target = 'C:/Windows'
else:
    target = '/etc'

for currdir, subdirs,files in os.walk(target):
    for file in files:
        fullpath = os.path.join(currdir, file)
        if os.path.isfile(fullpath):
            fsize = os.path.getsize(fullpath)
            if fsize > 1000000:
                print("{0:40s} {1:8d}".format(fullpath, fsize))
