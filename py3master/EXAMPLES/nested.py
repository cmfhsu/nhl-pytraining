#!/usr/bin/env python

northam = [ "US","El Salvador","Mexico","Canada" ]
europe = [ "Germany","France","Bulgaria","Estonia","Wales"]
africa = [ "Benin","Kenya","Egypt","Morocco"]

earth = [ northam,europe,africa ]
venus = []
mars = []
print("earth[1]",earth[1])
print("earth[1][2]",earth[1][2])

solarsys = [ earth,mars,venus ]
print("solarsys[0][2][1]",solarsys[0][2][1])

months = [
   (None,0),
   ("January",31),
   ("February",28),
   ("March",31),
   ("April",30),
   ("May",31),
   ("June",30),
   ("July",31),
   ("August",31),
   ("September",30),
   ("October",31),
   ("November",30),
   ("December",31)
]
print("{0:9s} {1:2d}".format(months[1][0],months[1][1]))
print("{0:9s} {1:2d}".format(months[6][0],months[6][1]))