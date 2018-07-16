#!/usr/bin/env python

while True:
    name = input("Enter a name (or q to quit): ")
    if name.lower() == 'q':
        print("goodbye!")
        break
    if name == '':
        continue
    print("welcome,", name)
