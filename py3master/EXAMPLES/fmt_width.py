#!/usr/bin/env python

name = 'Ann Elk'
value = 10000
airspeed = 22.347
# note: [] are used to show field widths
print('[{0:s}]'.format(name))
print('[{0:10s}]'.format(name))
print('[{0:3s}]'.format(name))
print('[{0:3.3s}]'.format(name))
print()
print('[{0:8d}]'.format(value))
print('[{0:8f}]'.format(value))
print('[{0:8f}]'.format(airspeed))
print('[{0:8.3f}]'.format(airspeed))
print('[{0:8.2f}]'.format(airspeed))
print('[{0:.2f}]'.format(airspeed))
