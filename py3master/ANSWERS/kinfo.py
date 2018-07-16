#!/usr/bin/env python

import sys
from knight import Knight, UnknownKnightError

for name in sys.argv[1:]:
    try:
        k = Knight(name)
    except UnknownKnightError as e:
        print(e)
        continue

    print("Name: {0} {1}".format(k.title,name))
    print("Favorite Color:",k.favorite_color)
    print("Quest:",k.quest)
    print("Comment:",k.comment)
    print()
