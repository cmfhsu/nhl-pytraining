#!/usr/bin/env python
from animal import Animal


class Insect(Animal):
    def __init__(self, species, name, sound, can_fly=False):
        Animal.__init__(self, species, name, sound)
        self._can_fly = can_fly

    def can_fly():
       return self._can_fly

if __name__ == '__main__':
    i1 = Insect('Bumblebee', 'Boris', 'Bzzzzzzzz', True)
    i1.make_sound()

