#!/usr/bin/env python

fruit = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon",
    "Kiwi", "ORANGE", "lime", "Watermelon", "guava", "papaya", "FIG",
    "pear", "banana", "Tamarind", "persimmon", "elderberry", "peach",
    "BLUEberry", "lychee", "grape" ]

def ignore_case(e):
    return e.lower()

fs1 = sorted(fruit, key=ignore_case)
print("Ignoring case:")
print(" ".join(fs1), end="\n\n")

def by_length_then_name(e):
    return (len(e), e.lower())

fs2 = sorted(fruit,key=by_length_then_name)
print("By length, then name:")
print(" ".join(fs2))
print()

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = sorted(nums)
print("Numbers sorted numerically:")
for n in n1:
    print(n, end=' ')
print("\n")

n2 = sorted(nums, key=str)
print("Numbers sorted as strings:")
for n in n2:
    print(n, end=' ')
print()
