#!/usr/bin/env python

airports = {'IAD': "Dulles", 'RDU': "Raleigh-Durham",
            "DCA": "Reagan", "BWI": "Baltimore/Washington",
            "EWR": "Newark", "ABQ": "Albuquerque",
            "GDB": "Granite Falls"}

print("*** raw")
for abbr, airport in airports.items():
    print("{0:3s} {1:<20s}".format(abbr, airport))

print()
print("*** sorted")
for abbr, airport in sorted(airports.items()):
    print("{0:3s} {1:<20s}".format(abbr, airport))
