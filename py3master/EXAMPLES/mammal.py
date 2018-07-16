#!/usr/bin/env python

from  animal import Animal

class Mammal(Animal):
    def __init__(self, species, name, sound, gestation):
        super(Mammal, self).__init__(species, name, sound)
        self._gestation = gestation

    @property
    def gestation(self):
        """Length of gestation period in days"""
        return self._gestation

if __name__ == "__main__":
    m1 = Mammal("African lion", "Bob", "Roarrrr", 120)
    print(m1.name, "is a", m1.species, "--", end=' ')
    m1.make_sound()

    m2 = Mammal("Fruit bat", "Freddie", "Squeak!!", 180)
    print(m2.name, "is a", m2.species, "--", end=' ')
    m2.make_sound()

    print("Gestation period of the",m1.species,"is", m1.gestation, "days")
    print("Gestation period of the",m2.species,"is", m2.gestation, "days")
