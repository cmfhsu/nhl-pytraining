#!/usr/bin/env python

def hello():
    print("Hello, world")

def sqrt(n):
    return n ** .5

hello()

m = sqrt(1234)
n = sqrt(2)
print("m is {0:.3f} n is {1:.3f}".format(m, n))
