#!/usr/bin/env python
"""

@author: jstrick
Created on Sat Mar 16 00:47:05 2013

"""
import pickle
import pprint

airports = {
    'RDU': 'Raleigh-Durham', 'IAD': 'Dulles', 'MGW': 'Morgantown',
    'EWR': 'Newark', 'LAX': 'Los Angeles', 'ORD': 'Chicago'
}

colors = [
    'red', 'blue', 'green', 'yellow', 'black',
    'white', 'orange', 'brown', 'purple'
]

data = (
    colors,
    airports,
)

with open ('../TEMP/pickled_data.pic', 'wb') as PIC_OUT:
    pickle.dump(data, PIC_OUT)

with open ('../TEMP/pickled_data.pic', 'rb') as PIC_IN:
    pickled_data = pickle.load(PIC_IN)

pprint.pprint(pickled_data)
