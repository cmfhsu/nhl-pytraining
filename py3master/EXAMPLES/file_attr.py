#!/usr/bin/env python
"""

@author: jstrick
Created on Wed Mar 13 07:19:23 2013

"""
import os
from datetime import datetime as DateTime

def format_time(ts):
    """convert time stamp to YYYY-MM-DD HH:MM string"""
    dt = DateTime.fromtimestamp(ts)
    s = dt.strftime('%Y-%m-%d %H:%M')

    return s

filenames = (
    '../DATA/alice.txt',
    '../ANSWERS/sieve.py',
    'file_attr.py',
    '../sequences.py',
)

for filename in filenames:
    size = os.path.getsize(filename)
    mtime_ts = os.path.getmtime(filename)
    mtime = format_time(mtime_ts)

    atime_ts = os.path.getatime(filename)
    atime = format_time(atime_ts)


    print('{0:20s} {1:8d}  {2}  {3}'.format(filename, size, mtime, atime))
