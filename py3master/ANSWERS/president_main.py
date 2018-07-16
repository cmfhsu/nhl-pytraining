#!/usr/bin/env python

from president import President

p = President(1)   # George Washington
bd = p.birth_date
print("George was born on {0}-{1}-{2}".format(bd.month, bd.day, bd.year))

p = President(26)
print("Teddy belonged to the {0} party".format(p.party))

p = President(37)
print("Milhous was born in {0}, {1}".format(p.birthplace, p.birth_state))

p = President(44)
print("Obama was born in the city of {0}, and his date of death is {1}".format(p.birthplace, p.death_date))
