#!/usr/bin/env python
"""
@author: jstrick
"""

import argparse

parser = argparse.ArgumentParser("A Celsius-to-Fahrenheit converter")

parser.add_argument('ctemp',type=float, metavar='CELSIUS-TEMPERATURE')

args = parser.parse_args()

ftemp = ((9 * args.ctemp) / 5 ) + 32

print("{0:.1f} C is {1:.1f} F".format(args.ctemp,ftemp))