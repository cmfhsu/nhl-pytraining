#!/usr/bin/env python

# list to hold all presidents (will be list of lists)
all_pres = []

with open("../DATA/presidents.txt", "r") as PRES:
    for line in PRES:
        fields = line[:-1].split(":")
        all_pres.append(fields) # add list of fields

# sort by lname, fname
for fields in sorted(all_pres, key=lambda e: (e[1],e[2])):
    full_name = '{} {}'.format(fields[2], fields[1])
    print('{:35s} {}'.format(full_name, fields[6]))

