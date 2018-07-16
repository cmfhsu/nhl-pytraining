#!/usr/bin/env python
import re

fs = "apple banana artichoke cherry date enchilada appetizer"
fruits = fs.split()

r1 = re.compile(r"c.")
for f in fruits:
    if r1.search(f):
        print(f, end=' ')
print()

for f in fruits:
    m = r1.search(f)
    if m:
        print(f, end=' ')
        print(m.group(), end=' ')
        print(m.start(), end=' ')
        print(m.end())
print()

r2 = re.compile(r"a([a-z]{3})(.)")
print(r2.findall(fs))
print()

for m in r2.finditer(fs):
    print(m,m.group(),m.start(),m.end(),m.group(1))

print(re.findall(r'\ba.{3}',fs,re.IGNORECASE))

r3 = re.compile(r"\b(a[a-z]+)(\s*)")
print(r3.sub('',fs))
print(r3.subn('',fs))

def doit(m):
    return "'" + m.group(1) + "'" + m.group(2)

print(r3.sub(doit,fs))
print(r3.subn(doit,fs))

s2 = "hogwash nonsense, blarney;fol-de-rol    junk"

rx_nonword_sep = re.compile(r"[^a-z-]+")

print(rx_nonword_sep.split(s2))
