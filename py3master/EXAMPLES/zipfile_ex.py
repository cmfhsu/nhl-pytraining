#!/usr/bin/env python
import zipfile

ztxt = zipfile.ZipFile("../DATA/textfiles.zip")

print(ztxt.namelist())

raw_data = ztxt.read("fruit.txt")
str_data = raw_data.decode()
print(str_data)

ztxt.close()

znew = zipfile.ZipFile("example.zip","w")

znew.write("../DATA/fruit.txt")
znew.write("../DATA/alice.txt")

znew.close()
