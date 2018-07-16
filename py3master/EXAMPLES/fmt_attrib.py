#!/usr/bin/env python
from datetime import date

fruits = ( 'apple', 'banana', 'mango' )
values = [5,18,27,6]
dday = date(1944,6,6)
pythons = { 'Idle':'Eric', 'Cleese':'John', 'Gilliam':'Terry',
    'Chapman':'Graham', 'Palin':'Michael', 'Jones':'Terry'}

print('{0[0]} {0[2]}'.format(fruits))
print('{f[0]} {f[2]}'.format(f=fruits))
print()
print('{0[0]} {0[2]}'.format(values))
print()
print('{0[Palin]} {0[Cleese]}'.format(pythons))
print('{names[Palin]} {names[Cleese]}'.format(names=pythons))
print()
print('{0.month}-{0.day}-{0.year}'.format(dday))
