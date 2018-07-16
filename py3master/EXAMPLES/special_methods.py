#!/usr/bin/env python
# (c)2015 John Strickler

class Special(object):

    def __init__(self,value):
        self._value = value

    # define ... Special object ... added to another Special object
    def __add__(self,other):
        return self._value + other._value

    # define what happens when Special object is multiplied by a value
    def __mul__(self,num):
        return ''.join((self._value for i in range(num)))

    # define what happens when str() called on a Special object
    def __str__(self):
        return self._value.upper()

    def __eq__(self,other):
        return self._value == other._value

if __name__ == '__main__':
    s = Special('spam')
    t = Special('eggs')
    u = Special('spam')
print("s + s", s + s)
print("s + t", s + t)
print("t + t", t + t)
print("s * 10", s * 10)
print("t * 3", t * 3)
print("str(s)=%s  str(t)=%s" % ( str(s), str(t) ))
print("id(s)=%d id(t)=%d id(u)=%d" % ( id(s), id(t), id(u) ))
print("s == s", s == s)
print("s == t", s == t)
print("u == s", s == u)
