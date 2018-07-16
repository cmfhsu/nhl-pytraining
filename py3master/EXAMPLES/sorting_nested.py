#!/usr/bin/env python
# (c)2015 John Strickler

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

# sort by first name (default)
print("By first name:")
for first_name, last_name, product in sorted(computer_guys):
    print(first_name, last_name, product)
print('-' * 60)

# sort by last name
print("By last name:")
for first_name, last_name, product in sorted(computer_guys,
                                             key=lambda e: e[1]):
    print(first_name, last_name, product)
print('-' * 60)

# sort by company
print("By company/product:")
for first_name, last_name, product in sorted(computer_guys,
                                             key=lambda e: e[2]):
    print(first_name, last_name, product)
