#!/usr/bin/env python

knight_info = {}

with open("../DATA/knights.txt") as knights_in:
    for line in knights_in:
        (name, title, color, quest, comment) = line[:-1].split(":")
        knight_info[name] = {
            'title': title,
            'color': color,
            'quest': quest,
            'comment': comment,
        }

for name, info in knight_info.items():
    print("{0} {1}".format(info['title'], name))
