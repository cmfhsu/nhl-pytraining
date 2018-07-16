#!/usr/bin/env python

from tempconv import c2f

while True:
    cel_str = input('Enter Celsius temp: ')
    if cel_str.lower() == 'q':
        break

    try:
        cel = float(cel_str)
    except ValueError as e:
        print("Invalid number.\n")
        continue

    fahr = c2f(cel)
    print('{0:.1f} C is {1:.1f} F\n'.format(cel,fahr))

