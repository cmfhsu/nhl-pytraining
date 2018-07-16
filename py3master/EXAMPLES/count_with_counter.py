#!/usr/bin/env python

from collections import Counter

counts = Counter()

with open("../DATA/breakfast.txt") as breakfast_in:
    for line in breakfast_in:
        item = line[:-1]
        counts[item] += 1

for item, count in counts.items():
    print(item, count)

