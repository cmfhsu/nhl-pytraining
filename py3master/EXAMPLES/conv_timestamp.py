#!/usr/bin/env python
"""

@author: jstrick
Created on Mon Mar 11 16:02:38 2013

"""
from datetime import datetime as DateTime
import time

adate = DateTime(1975, 4, 2, 12, 9, 55)
timestamp = time.mktime(adate.timetuple())
today = time.time()

timestamps = (0, timestamp, today)

for ts in timestamps:
    tm = time.localtime(ts)
    print(tm.tm_year, tm.tm_mon, tm.tm_mday)
    print()

    dt = DateTime.fromtimestamp(ts)
    print(dt.year, dt.month, dt.day)
    print('-' * 20)
