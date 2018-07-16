#!/usr/bin/env python
"""

@author: jstrick
Created on Wed Mar 13 09:27:45 2013

"""
import os

FILENAMES = (
    '../DATA/mystery',
    '../DATA/alt.txt',
    '/bin/ls',
    'c:/windows/system32/netstat.exe',
)

for filename in FILENAMES:
    print(filename, end=' ')
    if os.access(filename, os.F_OK):
        if os.access(filename, os.R_OK):
            print("is readable", end=' ')
        if os.access(filename, os.W_OK):
            print("is writable", end=' ')
        if os.access(filename, os.X_OK):
            print("is executable", end=' ')
    else:
        print("does not exist", end=' ')
    print()


