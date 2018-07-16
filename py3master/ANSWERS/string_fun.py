#!/usr/bin/env python

name = input("Enter a full name: ")

print("name: ",name)
print("upper: ",name.upper())
print("title: ",name.title())

# other string methods
print("'j' count:",name.lower().count('j'))
print("pos of 'jacob':", name.lower().index('jacob'))
