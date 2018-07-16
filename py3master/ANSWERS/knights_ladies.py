#!/usr/bin/env python
import csv

with open('../DATA/knights.csv') as K:
    rdr = csv.reader(K)
    for name, title, color, quest, comment, number, lady_str in rdr:
        lady_list = lady_str.split(',')
        if len(lady_list) == 1:
            ending = 'y'
        else:
            ending = 'ies'
        print("{0} {1} has {2} lad{3}".format(
            title, name, len(lady_list), ending
        ))


