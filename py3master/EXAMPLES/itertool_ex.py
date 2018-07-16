#!/usr/bin/env python

from itertools import groupby

m = '''
    Brave Sir Robin ran away
    Boldly ran away away
    When danger reared its ugly head
    He bravely turned his tail and fled
    Brave brave brave brave Sir Robin
'''

for x in groupby(sorted(m.split(), key=len), len):
    print(x[0], list(x[1]))
