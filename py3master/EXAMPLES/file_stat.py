#!/usr/bin/env python
"""

@author: jstrick
Created on Wed Mar 13 09:01:14 2013

"""
import os

info = os.stat('../DATA/parrot.txt')
print(info)

print('size is', info[6])
print('size is', info.st_size)

