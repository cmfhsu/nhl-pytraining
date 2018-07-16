#!/usr/bin/env python

with open("../DATA/mystery","rb") as m:
    chars = m.read()

print(chars[::2].decode())
