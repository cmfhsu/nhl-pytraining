#!/usr/bin/env python

a = "My hovercraft is full of EELS"

print("original:",a)
print("upper:",a.upper())
print("lower:",a.lower())
print("swapcase:",a.swapcase())
print("title:",a.title())
print("e count (normal):",a.count('e'))
print("e count (lower-case):",a.lower().count('e'))
print("found EELS at:",a.find('EELS'))
print("found WOLVERINES at:",a.find('WOLVERINES'))

b = "graham"
print("Capitalized:",b.capitalize())

