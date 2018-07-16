#!/usr/bin/env python
"""

@author: jstrick
Created on Wed Mar 13 20:34:36 2013

"""
from shutil import copy, copyfile, move

# copy from DATA to parent direcotry
copy('../DATA/parrot.txt','..')

# move parrot.txt from parent to DATA
move('../parrot.txt','../DATA/budgie.txt')

# copy file from DATA to EXAMPLES
copyfile('../DATA/budgie.txt', '../EXAMPLES/parrot.txt')

