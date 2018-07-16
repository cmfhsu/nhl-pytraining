#!/usr/bin/env python

colors = ["red","blue","green","yellow","brown","black"]

months = (
    "Jan","Feb","Mar","Apr","May","Jun",
    "Jul","Aug","Sep","Oct","Nov","Dec",
)

print("colors: len is {0}; min is {1}; max is {2}".format(len(colors),min(colors),max(colors)))
print("months: len is {0}; min is {1}; max is {2}".format(len(months),min(months),max(months)))
print()

print("sorted:", end=' ')
for m in sorted(colors):
    print(m, end=' ')
print()

phrase = ('dog','bites','man')
print(" ".join(reversed(phrase)))
print()

first_names = "Bill Bill Dennis Steve Larry".split()
last_names = "Gates Joy Richie Jobs Ellison".split()

full_names = zip(first_names, last_names)
print("full_names:", full_names)
print()

for first_name, last_name in full_names:
    print("{0} {1}".format(first_name, last_name))
