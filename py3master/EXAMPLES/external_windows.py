#!/usr/bin/env python
import sys
import os

if sys.platform != 'win32':
    print("This script is only for Windows")
    exit(1)

os.system(r"dir ..\DATA") 
print()

with os.popen("netstat -an") as NS: 
    for entry in NS:
        if 'ESTABLISHED' in entry:
            print(entry[:-1])
    print()

# backticks equivalent 
host_name = os.popen("hostname").read()

print(host_name)
