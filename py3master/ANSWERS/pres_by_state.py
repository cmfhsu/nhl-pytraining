#!/usr/bin/env python
"""

@author: jstrick
Created on Mon Apr  1 06:26:12 2013

"""
# BONUS

pres_by_state = {}

with open('../DATA/presidents.txt') as PRES:
    for rec in PRES:
        flds = rec[:-1].split(':')
        state = flds[6]  # not necessary, but easier to read
        if state in pres_by_state:
            pres_by_state[state] += 1
        else:
            pres_by_state[state] = 1

for state, count in sorted(pres_by_state.items()):
    print("{0:20s} {1:2d}".format(state,count))
