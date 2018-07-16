#!/usr/bin/env python
# (c) 2015 John Strickler
#


def spam(p1, p2, *p3, p4=None, **p5):
    print("p1:", p1)
    print("p2:", p2)
    print("p3:", p3)
    print("p4:", p4)
    print("p5:", p5)
    print()

spam('a', 'b')
spam('a', 'b', 'c', 'd', 'e')
spam('a', 'b', 'c', 'd', 'e', p4='f')
spam('a', 'b', 'c', 'd', 'e', ham='f', eggs='g')
spam('a', 'b', 'c', 'd', 'e', p4='f', ham='g', eggs='h')
spam('a', 'b', ham='g', eggs='h')
spam('a', 'b', 'c', ham='g', eggs='h')
spam('a', 'b', 'c', 'd', p4='e')
