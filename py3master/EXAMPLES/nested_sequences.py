#!/usr/bin/env python

months = [
    ("January", 31),
    ("February", 28),
    ("March", 31),
    ("April", 30),
    ("May", 31),
    ("June", 30),
    ("July", 31),
    ("August", 31),
    ("September", 30),
    ("October", 31),
    ("November", 30),
    ("December", 31)
]

fmt = "{0:9s} {1:2d}"
print(fmt.format(months[1][0], months[1][1]))
print(fmt.format(months[6][0], months[6][1]))
print()

for month, numdays in months:
    print(fmt.format(month, numdays))
print()

computer_guys = [
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Guido', 'Van Rossum', 'Python'),
    ('Larry', 'Wall', 'Perl'),
    ('Bill', 'Joy', 'Sun'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Steve', 'Case', 'AOL'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Steve', 'Jobs', 'Apple'),
    ('Dennis', 'Ritchie', 'Unix'),
]

for first_name, last_name, known_for in computer_guys:
    print(first_name, last_name)
