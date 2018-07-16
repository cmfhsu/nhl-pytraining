#!/usr/bin/env python

colors = ["red","blue","green","yellow","brown","black"]

months = (
    "Jan","Feb","Mar","Apr","May","Jun",
    "Jul","Aug","Sep","Oct","Nov","Dec",
)
print("yellow in colors: ",("yellow" in colors))
print("pink in colors: ",("pink" in colors))
print("colors: ", ",".join(colors))

del colors[4]  # remove brown
print("removed 'brown':",",".join(colors))

colors.remove('green')
print("removed 'green':",",".join(colors))

sum_of_lists = [True] + [True] + [False]
print("sum of lists:",sum_of_lists)

product = [True] * 5
print("product of lists:",product)

