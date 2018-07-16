#!/usr/bin/env python

import sys

if len(sys.argv) == 2:
	limit = int(sys.argv[1])
else:
	limit = 50

flags = set()

print(2, end=' ')
for num in range(3,limit,2):
	if num not in flags:
		print(num, end=' ')
		for x in range(num,limit,num):
			flags.add(x)
