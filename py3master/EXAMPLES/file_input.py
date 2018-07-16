#!/usr/bin/env python
"""

@author: jstrick
Created on Wed Mar 13 10:00:26 2013

"""
import fileinput

for line in fileinput.input():
    if 'bird' in line:
        print('{0}: {1}'.format(fileinput.filename(), line), end=' ')

