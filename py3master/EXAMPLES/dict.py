#!/usr/bin/env python
d = {}
d['apple'] = 10
d['blueberry'] = 25
d['grape'] = 2

print("d",d)
print("d['apple']",d['apple'])
print("len(d)",len(d))
print()

d['apple'] = 33
d['Apple'] = 91
d['APPLE'] = "munchkin"
print("d",d)
print("d['apple']",d['apple'])
