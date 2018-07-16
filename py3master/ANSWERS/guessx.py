#!/usr/bin/env python

import sys

max_val = 26
if len(sys.argv) > 1:
    max_val = int(sys.argv[1]) + 1
min_val = 0
tries = 0

while True:
    guess = (max_val + min_val)/2
    ans = input("Is {0} your number? ".format(guess))

    if ans == "q":
        break

    tries = tries + 1

    if ans == "h":
        max_val = guess
    elif ans == "l":
        min_val = guess
    elif ans == "y":
        print("I got it in {0} try(ies)!".format(tries))
        break
    else:
        print("Please enter h, l, or y")


