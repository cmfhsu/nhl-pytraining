#!/usr/bin/env python


temp_str = input("Enter the temperature: ")
temp = int(temp_str)
if temp < 76:
    print("Don't go swimming")

num_str = input("Enter a number: ")
num = int(num_str)
if num > 1000000:
    print(num, "is a big number")
else:
    print("your number is", num)

hour_str = input("Enter the hour: ")
hour = int(hour_str)
if hour < 12:
    print("Good morning")
elif hour < 18:
    print("Good afternoon")
elif hour < 23:
    print("Good evening")
else:
    print("You're up late")
