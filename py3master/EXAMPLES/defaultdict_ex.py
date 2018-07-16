#!/usr/bin/env python
"""

@author: jstrick
Created on Wed Mar 13 20:45:42 2013

"""
from collections import defaultdict

dd = defaultdict(lambda: 0)


dd['spam'] = 10
dd['eggs'] = 22

print(dd['spam'])
print(dd['eggs'])
print(dd['foo'])




