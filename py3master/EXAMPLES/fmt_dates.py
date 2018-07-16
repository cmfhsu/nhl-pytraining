#!/usr/bin/env python
"""

@author: jstrick
Created on Wed Mar 20 07:55:25 2013

"""
from datetime import datetime as DateTime

event = DateTime(2012,7,4,11,15)

print(event)
print()

print('{0:%A, %B %d, %Y}'.format(event))
print('{0:%m/%d/%y %I:%M %p}'.format(event))
