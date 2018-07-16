#!/usr/bin/env python

x = 5
if x > 0:
    modern_man = 'Matt Damon'  # global

cave_man = 'Barney Rubble'  # global

def spam():
    global cave_woman
    cave_baby = 'Bamm-bamm'  # local
    cave_woman = 'Betty Rubble'  # global, not local
print("Cave man is", cave_man)

spam()
print("Cave woman is", cave_woman)
print(modern_man)
