#!/usr/bin/env python

counts = {}
with open("../DATA/breakfast.txt") as breakfast_in:
    for line in breakfast_in:
        breakfast_item = line[:-1]
        if breakfast_item in counts:
            counts[breakfast_item] = counts[breakfast_item] + 1
        else:
            counts[breakfast_item] = 1

for item, count in counts.items():
    print(item,count)
