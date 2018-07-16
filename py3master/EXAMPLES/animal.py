#!/usr/bin/env python

class Animal(object):
    def __init__(self,species,name,sound):
        self._species = species
        self._name = name
        self._sound = sound

    @property
    def species(self):
        return self._species
    
    @property
    def name(self):
        return self._name
    
    def make_sound(self):
        print(self._sound)
    
if __name__ == "__main__":
    leo = Animal("African lion","Leo","Roarrrrrrr")
    garfield = Animal("cat","Garfield","Meowwwww")
    felix = Animal("cat","Felix","Meowwwww")

    print(leo.name,"is a",leo.species,"--", end=' ')
    leo.make_sound()
    
    print(garfield.name,"is a",garfield.species,"--", end=' ')
    garfield.make_sound()
    
    print(felix.name,"is a",felix.species,"--", end=' ')
    felix.make_sound()
