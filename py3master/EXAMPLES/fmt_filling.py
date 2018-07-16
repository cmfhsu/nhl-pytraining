#!/usr/bin/env python
"""

@author: jstrick
Created on Wed Mar 20 08:09:11 2013

"""
name = 'Guido'
pos_num = 123
neg_num = -456
big_num = 1234567890

print('{0:#<13s}'.format(name))
print('{0:#>13s}'.format(name))
print('{0:#^13s}'.format(name))
print('{0:*<13s}'.format(name))
print('{0:><13s}'.format(name))
print()
print('{0:d} {1:d}'.format(pos_num, neg_num))
print('{0:-d} {1:-d}'.format(pos_num, neg_num))
print('{0: d} {1: d}'.format(pos_num, neg_num))
print('{0:+d} {1:+d}'.format(pos_num, neg_num))
print()
print('{0:,d}'.format(big_num))
