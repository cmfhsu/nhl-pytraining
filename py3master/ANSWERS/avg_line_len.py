#!/usr/bin/env python
"""

@author: jstrick
Created on Thu Mar 21 00:36:05 2013

"""
import fileinput

total_length = 0

for line in fileinput.input():
    total_length += len(line)

avg_line_len = total_length/fileinput.lineno()
print('{:.1f}'.format(avg_line_len))
