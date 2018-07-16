#!/usr/bin/env python
import sys
import os

if sys.platform == 'win32':
    print("This script is only for non-Windows systems")
    exit(1)

os.system("who")
print()

with os.popen("ls -l ../DATA","r") as ls:
    for entry in ls:
        print(entry[:-1])
    print()

# backticks equivalent
host_name = os.popen("uname -n").read()

print(host_name)
