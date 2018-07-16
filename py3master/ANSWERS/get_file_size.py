#!/usr/bin/env python

import sys
import os.path

for f in sys.argv[1:]:
    if os.path.isdir(f):
        print("{0} is a directory".format(f))
        continue
    else:
        print(f,os.path.getsize(f))
