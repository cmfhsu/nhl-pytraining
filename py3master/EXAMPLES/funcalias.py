#!/usr/bin/env python


def cavort():
    print("wheeeee")

gambol = cavort

cavort()
gambol()
print("gambol() is really",gambol.__name__)
