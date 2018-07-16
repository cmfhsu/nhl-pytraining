#!/usr/bin/env python
"""
Created on Sat Mar  9 08:09:02 2013

@author: jstrick

"""
import string
from random import choice

print("ascii_letters:", repr(string.ascii_letters))
print("ascii_lowercase:", repr(string.ascii_lowercase))
print("ascii_uppercase:", repr(string.ascii_uppercase))
print("digits:", repr(string.digits))
print("hexdigits:", repr(string.hexdigits))
print("octdigits:", repr(string.octdigits))
print("printable:", repr(string.printable))
print("punctuation:", repr(string.punctuation))
print("whitespace:", repr(string.whitespace))
print()

colors = 'red GREEN BLUE black white YELLOW'.split()
print(sorted(colors))
print(sorted(colors, key=str.lower))
print()

random_letters = []
for i in range(50):
    random_letters.append(choice(string.ascii_lowercase))

random_string = ''.join(random_letters)
print(random_string)
print()
