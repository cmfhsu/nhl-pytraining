#!/usr/bin/env python

d1 = dict()
d2 = {}
d3 = dict(red=5, blue=10, yellow=1, brown=5, black=12)

airports = { 'IAD': 'Dulles', 'SEA': 'Seattle-Tacoma',
       'RDU': 'Raleigh-Durham', 'LAX': 'Los Angeles' }

pairs = [('Washington', 'Olympia'),('Virginia','Richmond'),
    ('Oregon','Salem'), ('California', 'Sacramento')]

state_caps = dict(pairs)
print(state_caps['Virginia'])

print(d3['red'])
print(airports['LAX'])

airports['SLC'] = 'Salt Lake City'
airports['LAX'] = 'Lost Angels'
print(airports['SLC'])

key = 'PSP'
if key in airports:
    print(airports[key])

print(airports.get(key))
print(airports.get(key, 'NO SUCH AIRPORT'))

print(airports.setdefault(key, 'Palm Springs'))
print(key in airports)

