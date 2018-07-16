#!/usr/bin/env python

airports = { 'IAD':"Dulles",'RDU':"Raleigh-Durham",
    "DCA":"Reagan", "BWI":"Baltimore/Washington",
    "EWR":"Newark","ABQ":"Albuquerque",
    "GDB":"Granite Falls" }

print("*** raw")
for abbr in airports:
    print("{0:3s} {1:<20s}".format(abbr,airports[abbr]))

print()
print("*** sorted (unpacked tuple)")
for abbr,airport in sorted(airports.items()):
    print("{0:3s} {1:<20s}".format(abbr,airport))

print()
print("*** sorted (tuple only)")
for kv in sorted(airports.items()):
    print("{0:3s} {1:<20s}".format(*kv))

