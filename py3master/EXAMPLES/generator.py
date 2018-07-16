#!/usr/bin/env python

fh_fruit = open('../DATA/fruit.txt')

ufruits = ( fruit[:-1].upper() for fruit in fh_fruit )

print(ufruits)
for f in (ufruits):
    print(f)
