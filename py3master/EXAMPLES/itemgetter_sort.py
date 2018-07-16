#!/usr/bin/env python

import operator

pres = [("George", "", "Washingon"), ("John", "", "Adams"),
        ("John", "Quincy", "Adams"), ("Franklin", "Delano", "Roosevelt"),
        ("Richard", "Milhous", "Nixon"),
        ("James", "", "Monroe"), ("James", "", "Madison")]

print("sort by first name")
psort = sorted(pres)
for p in psort:
    print(" ".join(list(p)))
print()

print("sort by last name")
psort = sorted(pres, key=operator.itemgetter(2, 1))
for p in psort:
    print(" ".join(list(p)))
print()
