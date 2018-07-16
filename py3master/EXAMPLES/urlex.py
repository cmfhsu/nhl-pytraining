#!/usr/bin/env pythonimport urllib.request, urllib.error, urllib.parse

u = urllib.request.urlopen("http://www.google.com")
print(u.info())
print()
for line in u:
    print(line)
