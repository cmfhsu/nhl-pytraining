#!/usr/bin/env python

states = (
    'Virginia',
    'North Carolina',
    'Washington',
    'New York',
    'Florida',
    'Ohio',
)

with open("states.txt","w") as states_out:
    for state in states:
        states_out.write(state + "\n")

fruits = [ 'apple', 'cherry', 'peach', 'lemon', 'banana']

with open("fruit_names.txt", "w") as fruits_out:
    fruits_out.writelines(fr + '\n' for fr in fruits)
