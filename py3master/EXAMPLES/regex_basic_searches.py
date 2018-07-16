#!/usr/bin/env python
# (c)2015 John Strickler
import re

# text from www.pigeon.org
pigeon_racing = '''
You can seek out your own comfort level with the birds. If you desire a lower-key approach,
with only a handful of homing pigeons for the family to enjoy, that's certainly an
attractive approach for many. The spectrum also includes those who are deeply committed to
racing. Races range in distance from 100 miles to 600 miles, with 300 miles being among the
most popular distances.
'''

rx_number = re.compile(r'\d+')

# Does it match?

if rx_number.search(pigeon_racing):
    print('It matches\n')

# get the first match

m = rx_number.search(pigeon_racing)
if m:
    print('First match:', m.group(0), '\n')  # 0 is default, and can be omitted
else:
    print('No match', '\n')

# iterate over all matches
for m in rx_number.finditer(pigeon_racing):
    print(m.group())   # 0 not needed
print()

# just get all matches
all_matches = rx_number.findall(pigeon_racing)
print(all_matches, '\n')

