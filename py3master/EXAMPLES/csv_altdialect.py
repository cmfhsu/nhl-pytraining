#!/usr/bin/env python
"""

@author: jstrick
Created on Sun Mar 10 16:36:31 2013

"""
import os
import csv

rows = (
    'spam;eggs;spam;spam;eggs',
    'for;bar;blah;bax;xunc',
    'apple;mango;peach;lime;kiwi',
)

class CSVWithSemicolons(object):
    def __init__(self):
        self.delimiter = ';'
        self.doublequote = True
        self.quoting = csv.QUOTE_MINIMAL
        self.quotechar = '"'
        self.escapechar = '\\'
        self.lineterminator = os.linesep
        self.skipinitialspace = True

dia = CSVWithSemicolons()
csv.register_dialect('semi',dia)

rdr = csv.reader(rows,dia)

for row in rdr:
    print(row[0],row[-1])
print()

rdr = csv.reader(rows,dia)
for row in rdr:
    print(row[:2])
