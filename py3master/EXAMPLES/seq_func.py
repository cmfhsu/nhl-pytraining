#!/usr/bin/env python

colors = ["red","blue","green","yellow","brown","black"]
months = (
    "Jan","Feb","Mar","Apr","May","Jun",
    "Jul","Aug","Sep","Oct","Nov","Dec",
)

print("colors: len is {0}; min is {1}; max is {2}".format(len(colors),min(colors),max(colors)))
print("months: len is {0}; min is {1}; max is {2}".format(len(months),min(months),max(months)))

print("sorted:", end=' ')
for m in sorted(colors):
    print(m, end=' ')
print()

phrase = ('dog','bites','man')
print(" ".join(reversed(phrase)))

values1 = (0,1,0,0,0,0,1)
values2 = (True,True,True)

print("any(colors):",any(colors))
print("any(values1):",any(values1))
print("all(values1):",all(values1))
print("all(values2):",all(values2))

first = "Jennifer Stevie Thomas Rickie".split()
middle = "Love Ray Alva Lee".split()
last = "Hewitt Vaughn Edison Jones".split()

for name in zip(first,middle,last):
    print("{0} {1} {2}".format(*name))




