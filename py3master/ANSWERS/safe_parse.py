#!/usr/bin/env python

TEST_VALUES = 0, 1, 101, 'abc', '123a', 'a123'

def parse_float(string, default=None):
    try:
        float_val = float(string)
    except ValueError as err:
        return default
    else:
        return float_val
    
for tv in TEST_VALUES:
    print("Test value: {0} Result {1}".format(tv, parse_float(tv, 0)))
