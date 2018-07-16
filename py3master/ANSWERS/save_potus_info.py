#!/usr/bin/env python
"""

@author: jstrick
Created on Wed Mar 20 23:34:17 2013

"""
import csv
import pickle
from collections import namedtuple

President = namedtuple(
    'President',
    'firstname lastname birthplace birthstate party',
)

presidents = []
with open('../DATA/presidents.csv') as PRES:
    rdr = csv.reader(PRES)
    for row in rdr:
        pres = President(
            firstname = row[1],
            lastname = row[2],
            birthplace = row[3],
            birthstate = row[4],
            party = row[5],
        )
        presidents.append(pres)

print(presidents[15].firstname, end=' ')
print(presidents[15].lastname)
print(presidents[42].party)

# convert from namedtuple to tuple
pcopy = [ tuple(p) for p in presidents ]

with open('potus.pic','wb') as POTUS:
    pickle.dump(pcopy,POTUS)
