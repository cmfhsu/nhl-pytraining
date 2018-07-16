#!/usr/bin/env python

class Person(object):
    def __init__(self,lastname=None, firstname=None):
        self.last_name = lastname      # note: assigning to property
        self.first_name = firstname

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self,value):
       if value != None and not value.isalpha():
            raise ValueError("Last name may only contain letters")
       self._last_name = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self,value):
       if value != None and not value.isalpha():
            raise ValueError("First name may only contain letters")
       self._first_name = value

if __name__ == '__main__':
    for last_name, first_name in (('Ferneater', 'Eulalia'), ('Pepperpot', 'Hortense'), ('R2-D2', None)):
        try:
            p = Person(last_name, first_name)
        except ValueError as err:
print("ERROR:", err)
        else:
print("{0} {1}".format(p.first_name, p.last_name))
