#!/usr/bin/env pythonspam = [
    "Spam",
    "eggs  ",
    "   spam    ",
    "     spam spam     ",
    "SPAM	",
    "       SPAM and eggs    ",
    "Spam",
    "   Spam,    spam, spam,    spam, spam, eggs, and spam      ",
]

def cleanup(dirty):
    clean = dirty.strip().lower()
    return clean

for s in spam:
    print("Before: [{0}]".format(s))
    clean_s = cleanup(s)
    print("After: [{0}]".format(clean_s))
    print()
