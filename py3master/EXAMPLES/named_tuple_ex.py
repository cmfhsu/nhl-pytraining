#!/usr/bin/env python
"""

@author: jstrick
Created on Thu Mar 14 09:07:57 2013

"""
from collections import namedtuple

Knight = namedtuple('Knight', 'name title color quest comment')

k = Knight('Bob', 'Sir', 'green', 'whirled peas', 'Who am i?')
print(k.title, k.name)
print(k[1], k[0])
print()

knights = {}
with open('../DATA/knights.txt') as KN:
    for line in KN:
        flds = line[:-1].split(':')
        knights[flds[0]] = Knight(*flds)

for knight, info in knights.items():
    print('{0} {1}: {2}'.format(info.title, knight, info.color))
