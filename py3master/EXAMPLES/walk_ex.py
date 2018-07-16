#!/usr/bin/env python
"""
    count all files and folders
"""
import sys
import os

if len(sys.argv) < 2:
    print('Syntax: walk_ex.py START-DIR')
    sys.exit(1)

total_dirs = 0
total_files = 0

for currdir, subdirs,files in os.walk(sys.argv[1]):
    total_dirs += 1
    total_files += len(files)

print("{0} contains {1} files and {2} directories".format(
    sys.argv[1], total_files, total_dirs))
