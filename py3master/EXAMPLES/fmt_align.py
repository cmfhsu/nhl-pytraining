#!/usr/bin/env python

name = 'Ann'
value = 12345
nvalue = -12345

print('[{0:10s}]'.format(name))
print('[{0:<10s}]'.format(name))
print('[{0:>10s}]'.format(name))
print('[{0:^10s}]'.format(name))
print()
print('[{0:10d}] [{1:10d}]'.format(value,nvalue))
print('[{0:>10d}] [{1:>10d}]'.format(value,nvalue))
print('[{0:<10d}] [{1:<10d}]'.format(value,nvalue))
print('[{0:^10d}] [{1:^10d}]'.format(value,nvalue))
print('[{0:=10d}] [{1:=10d}]'.format(value,nvalue))
