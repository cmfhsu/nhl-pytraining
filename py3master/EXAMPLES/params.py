#!/usr/bin/env python

def spam(a,m,*b,**c):
    print("a is",a)
    print("m is",m)
    for x in b:
        print(x)
    for x in c:
        print(x,c[x])

spam('apple',2,3,name="Bob",count=12)
