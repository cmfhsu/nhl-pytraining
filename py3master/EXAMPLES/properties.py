#!/usr/bin/env python

class Person(object):

    def __init__(self,lastname=None,firstname=None):
        self.LastName = lastname
        self.FirstName = firstname

    @property
    def LastName(self):
        return self._lname

    @LastName.setter
    def LastName(self,value):
       if value != None and not value.isalpha():
            raise ValueError("Last name may only contain letters")
       self._lname = value

    @property
    def FirstName(self):
        return self._fname

    @FirstName.setter
    def FirstName(self,value):
       if value != None and not value.isalpha():
            raise ValueError("First name may only contain letters")
       self._fname = value

if __name__ == '__main__':
    p1 = Person('Ferneater', 'Eulalia')

    p2 = Person()
    p2.LastName = 'Pepperpot'
    p2.FirstName = 'Hortense'
print("{0} {1}".format(p1.FirstName,p1.LastName))
print("{0} {1}".format(p2.FirstName,p2.LastName))

    p3 = Person("R2D2")
print("{0} {1}".format(p3.FirstName,p3.LastName))
