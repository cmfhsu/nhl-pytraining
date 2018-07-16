#!/usr/bin/env python
"""

@author: jstrick
Created on Wed Mar 13 21:13:22 2013

"""
import pprint

struct = {
    'part1':[
        ['a','b','c'], ['d','e','f']
    ],
    'part2':{
        'red':55,
        'blue':[8, 98, -3],
        'purple':['Chicago','New York','L.A.'],
    },
    'part3': ['g','h','i'],
}

print('Without prprint:')
print(struct)
print()

print('With prprint:')
pprint.pprint(struct)
print()

print('With prprint (depth=2):')
pprint.pprint(struct, depth=2)
print()
