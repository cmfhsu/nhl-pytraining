#!/usr/bin/env python

colors = "red blue green yellow brown black".split()

months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()

for c in enumerate(colors):
    print("{0} {1}".format(*c))

print()
    
for num,month in enumerate( months, 1 ):
    print("{0} {1}".format( num, month ))
