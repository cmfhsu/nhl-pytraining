#!/usr/bin/env python

fruit = ["pomegranate","cherry","apricot","date","Apple","lemon","Kiwi",
"ORANGE","lime","Watermelon","guava","papaya","FIG","pear","banana",
"Tamarind","persimmon","elderberry","peach","BLUEberry","lychee",
 "grape" ]

nums = [800,80,1000,32,255,400,5,5000]

def by_length(e):
    return (len(e),e.lower())

fs1 = sorted(fruit,key=str.lower)
print("Ignoring case:")
print(" ".join(fs1))
print()

fs2 = sorted(fruit,key=by_length)
print("By length, then name:")
print(" ".join(fs2))
print()

fs3 = sorted(nums)
print("Numbers sorted numerically:")
for n in fs3:
    print(n, end=' ')
print()
print()

fs4 = sorted(nums,key=str)
print("Numbers sorted as strings:")
for n in fs4:
    print(n, end=' ')
print()
