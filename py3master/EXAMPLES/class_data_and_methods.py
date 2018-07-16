#!/usr/bin/env python
# (c)2015 John Strickler

import random

class Fruit(object):

    FRUITS = 'apple', 'mango', 'banana', 'fig'

    @classmethod
    def fruits_as_list(cls):
        return list(Fruit.FRUITS)

    @classmethod
    def fruits_as_tuple(cls):
        return Fruit.FRUITS

    @classmethod
    def fruits_as_string(cls):
        return ' '.join(Fruit.FRUITS)

    def random_pie(self):
        return "{0} pie".format(random.choice(Fruit.FRUITS))

if __name__ == '__main__':
    print(Fruit.fruits_as_list())
    print(Fruit.fruits_as_tuple())
    print(Fruit.fruits_as_string())

    f = Fruit()
    print(f.random_pie())
