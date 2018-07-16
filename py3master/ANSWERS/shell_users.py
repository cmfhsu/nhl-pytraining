#!/usr/bin/env python

count_of = {}
with open("../DATA/passwd") as pw:
    for line in pw:
        (user,epw,uid,gid,comment,home,shell) = line[:-1].split(":")
        if shell == "":
            shell = "NONE"
        count_of[shell] = count_of.get(shell,0) + 1

for shell,count in count_of.items():
    print("{0:5d} {1}".format(count,shell))
