#!/usr/bin/env python

ctemps = [ -40.0, 0.0, 37.0, 75.0, 100.0, -1 ]

fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]

computer_people = [
    ('Bill', 'Gates', 'Windows'),
    ('Bill', 'Joy', 'Sun Microsystems'),
    ('Brian', 'Kernighan', 'Unix'),
    ('Dennis', 'Ritchie', 'Unix'),
    ('Ken', 'Thompson', 'Unix'),
    ('Guido', 'van Rossum', 'Python'),
    ('Larry', 'Wall', 'Perl'),
    ('Matz','Matsumoto', 'Ruby'),
    ('John', 'Osterhout', 'TCL'),
    ('Linus', 'Torvalds', 'Linux'),
]


# ex 5-2
for c in ctemps:
    f = ((9 * c) / 5 ) + 32
    print("{0:.1f} C is {1:.1f} F".format(c, f))
print()

# ex 5-3
for i, fruit in enumerate(fruits, 1):
    print(i, fruit)
print()

# ex 5-4
clean_fruits = [ f.strip().lower() for f in fruits ]

print(','.join(clean_fruits))
print()

# ex 5-5
fruit_gen = (f.upper() for f in clean_fruits)
for cfruit in fruit_gen:
    print(cfruit, end=' ')
print()
print()

# ex 5-6
for firstname, lastname, thing in computer_people:
    print(lastname.upper())
print()

