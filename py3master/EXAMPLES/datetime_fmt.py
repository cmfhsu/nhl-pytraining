#!/usr/bin/env python
"""

@author: jstrick
Created on Sun Mar 10 23:01:42 2t013

"""
from datetime import datetime as DateTime

# Bill Gates's birthday
gates_bd = DateTime(1955,10,28, 22, 0, 0)

print(gates_bd)
print()

print(gates_bd.strftime('Bill was born on %B %d, %Y at %I:%M %p'))
print()

print(gates_bd.strftime('BG: %m/%d/%y'))
print()

print(gates_bd.strftime('Mr. Gates was born %d-%b-%Y'))
print()

print(gates_bd.strftime('log entry: %Y-%m-%d'))
print()
