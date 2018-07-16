#!/usr/bin/env python
def hello():
    print("Hello, world")

hello()
print()


def hi(name):
    print("Hello,", name)

hi('world')
hi('Mom')
print()


def greet(greeting, name):
    print("{}, {}".format(greeting, name))

greet('hello', 'world')
greet('howdy', 'partner')
print()


def greet_many(greeting, *names):
    for name in names:
        print("{}, {}".format(greeting, name))

greet_many('hi', 'Mom')
print()
greet_many('hi', 'Mom', 'Dad', 'Sis', 'Uncle Wiggily')
print()


def heya(whom="world"):
    print("Heya,", whom)

heya()
heya('Mom')
