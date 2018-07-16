#!/usr/bin/env python
import re

# text from www.pigeon.org
pigeon_racing = '''
You can seek out your own comfort level with the birds. If you desire a lower-key approach,
with only a handful of homing pigeons for the family to enjoy, that's certainly an
attractive approach for many. The spectrum also includes those who are deeply committed to
racing. Races range in distance from 100 miles to 600 miles, with 300 miles being among the
most popular distances.
'''


# Does it match?

if re.search(r'\d+', pigeon_racing):
    print('It matches\n')

# get the first match

m = re.search(r'\d+', pigeon_racing)
if m:
    print('First match:', m.group(0), '\n')  # 0 is default, and can be omitted
else:
    print('No match', '\n')

# iterate over all matches
for m in re.finditer(r'\d+', pigeon_racing):
    print(m.group())   # 0 not needed
print()

# just get all matches
all_matches = re.findall(r'\d+', pigeon_racing)
print(all_matches, '\n')
