#!/usr/bin/env python

mylist = [ "Idle","Cleese","Chapman","Gilliam","Palin","Jones"]
mytup = ("Roger","Old Woman","Prince Herbert","Brother Maynard")
mystr = "She turned me into a newt"
print("mylist:",mylist)
print("mytup:",mytup)
print("mystr:",mystr)
print()
print("mylist[0]",mylist[0])
print("mylist[5]",mylist[5])
print("mylist[0:3]",mylist[0:3])
print("mylist[2:]",mylist[2:])
print("mylist[:2]",mylist[:2])
print("mylist[1:-1]",mylist[1:-1])
print("mylist[0::2]",mylist[0::2])
print("mylist[1::2]",mylist[1::2])
mylist[3] = "Innes"
print("mylist:",mylist)
print()
print("mytup",mytup)
print("mytup[2]",mytup[2])
print("mytup[1:]",mytup[1:])
# mytup[2] = "Patsy"  # ERROR -- can't assign to tuple
print()
print("mystr",mystr)
print("mystr[0]",mystr[0])
print("mystr[-1]",mystr[-1])
print("mystr[21:25]",mystr[21:25])
print("mystr[21:]",mystr[21:])
print("mystr[:10]",mystr[:10])
print("mystr[::2]",mystr[::2])
