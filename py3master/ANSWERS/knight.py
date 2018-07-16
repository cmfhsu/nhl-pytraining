#!/usr/bin/env python
class UnknownKnightError(Exception):
    pass

class Knight(object):

    def __init__(self,name):
        self._name = name
        try:
            with open('../DATA/knights.txt') as K:
                for line in K:
                    (name,title,color,quest,cmt) = line[:-1].split(":")
                    if name == self._name:
                        self._title = title
                        self._color = color
                        self._quest = quest
                        self._comment = cmt
                        found = True
                        break
                else:
                    raise UnknownKnightError('''No such knight as "{0}"'''.format(self._name))
        except IOError as err:
            print(err)

    @property
    def name(self):
        return self._name
            
    @property
    def title(self):
        return self._title
            
    @property
    def favorite_color(self):
        return self._color
            
    @property
    def quest(self):
        return self._quest
            
    @property
    def comment(self):
        return self._comment
            

if __name__== "__main__":
    k1 = Knight("Arthur")
    print(k1. name, k1.favorite_color, k1.comment, k1.title)

    k2 = Knight("Bedevere")
    print(k2.name, k2.favorite_color, k2.comment, k2.title)

    try:
        k3 = Knight("Hillary")
    except UnknownKnightError as err:
        print(err)
