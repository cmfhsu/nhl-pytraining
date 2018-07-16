#!/usr/bin/env python
"""

@author: jstrick
Created on Sat Mar 16 06:29:43 2013

"""
import shelve

shelf_in = shelve.open('../TEMP/airports')

shelf_in['IAD'] = ('Dulles', 'VA')
shelf_in['EWR'] = ('Newark', 'NJ')
shelf_in['LAX'] = ('Los Angeles', 'CA')

shelf_in.close()

shelf_out = shelve.open('../TEMP/airports')
for abbr, city in shelf_out.items():
    print(abbr, city)

