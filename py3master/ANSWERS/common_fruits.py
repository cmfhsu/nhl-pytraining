#!/usr/bin/env python

fruit1 = set()
fruit2 = set()

with open("../DATA/fruit1.txt","r") as F1:
    for f in F1:
        fruit1.add(f.strip().lower())

with open("../DATA/fruit2.txt","r") as F2:
    for f in F2:
        fruit2.add(f.strip().lower())

common = fruit1 & fruit2

print("\n".join(common))
