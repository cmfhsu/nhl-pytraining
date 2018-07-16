#!/usr/bin/env python

name = "Tim"
count = 5
avg = 3.456
info = 2093
print("Name is [{0:<10s}]".format(name))
print("Name is [{0:>10s}]".format(name))
print("count is {0:03d} avg is {1:6.2f}".format(count,avg))
print("info is {0} {0:d} {0:o} {0:x}".format(info))
print("info is {0} {0:d} {0:#o} {0:#x}".format(info))
print("${0:,d}".format(38293892))
print("It is {temp} in {city}".format(city='Orlando',temp=85))
