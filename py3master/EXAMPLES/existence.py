#!/usr/bin/env python

import os

for path in ('c:/windows','/etc', '/wombat', '/tmp', 'C:/temp'):
    print(path, end=' ')
    if os.path.exists(path):
        print('exists')
    else:
        print('does not exist')
