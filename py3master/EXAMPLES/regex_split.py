#!/usr/bin/env python

import re

re_wordsep = re.compile(r"[\W']+")
re_capwords = re.compile(r"[A-Z][a-z]+")
re_float = re.compile(r"\d+(\.|\.\d+)?")
re_int = re.compile(r"\d+")

s1 = "There are 10 kinds of people in a Binary world"
s2 = "Noone expects the Spanish Inquisition"
s3 = "3 calling birds 2 french hens"
s4 = "a thing or 2"

m = re_int.match(s3)
if m:
    print(m.group())
m = re_int.match(s4)
if m:
    print(m.group())
m = re_int.search(s3)
if m:
    print(m.group())
m = re_int.search(s4)
if m:
    print(m.group())

if re_int.match(s1):
    print("s1 contains integers")

words = re_wordsep.split(s2)
print(words)

print(re_capwords.findall(s1))

for x in re_capwords.finditer(s1):
    print(x.group())

