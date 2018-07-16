#!/usr/bin/env python
"""

@author: jstrick
Created on Wed Mar 20 23:52:46 2013

"""
import pickle
from collections import namedtuple

President = namedtuple(
    'President',
    'firstname lastname birthplace birthstate party',
)

with open('potus.pic','rb') as POTUS:
    ptemp = pickle.load(POTUS)

# convert from tuple to namedtuple
presidents = [
    President(*p) for p in ptemp
]

for president in presidents:
    print("{0.firstname} {0.lastname} ({0.party})".format(president))
