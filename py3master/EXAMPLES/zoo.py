#!/usr/bin/env python
# (c)2015 John Strickler
from mammal import Mammal
from insect import Insect

m1 = Mammal("African lion","Bob","Roarrrr",120)
m2 = Mammal("Fruit bat","Freddie","Squeak!!",180)
i1 = Insect('Bumblebee', 'Boris', 'Bzzzzzzzz', True)

for animal in m1, m2, i1:
    print("My name is {} and my species is {}".format(animal.name, animal.species))
    print("I like to say", end=' ')
    animal.make_sound()  # inherited method
    print()
