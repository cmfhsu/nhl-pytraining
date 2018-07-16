#!/usr/bin/env python

f = open("../DATA/tyger.txt","r")
for line in f:
print(line[:-1])
f.close()

print()

f = open("../DATA/tyger.txt","r")
lines = f.readlines()
f.close()

print("** 1st stanza **")
for line in lines[2:6]:
print(line[:-1])
