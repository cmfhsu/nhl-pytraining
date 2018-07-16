#!/usr/bin/env python

def c2f(cel):
    f = ((9 * cel) / 5 ) + 32

    return f

while True:
	c = input('Enter Celsius temp: ')
	if c.lower() == 'q':
		break
	c = float(c)
	f = c2f(c)
	print('{0:.1f} C is {1:.1f} F\n'.format(c,f))

