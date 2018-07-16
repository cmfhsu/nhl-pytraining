#!/usr/bin/env python
# (c)2015 John Strickler
import re

alice_text = '''
  There was nothing so VERY remarkable in that; nor did Alice
think it so VERY much out of the way to hear the Rabbit say to
itself, `Oh dear!  Oh dear!  I shall be late!'  (when she thought
it over afterwards, it occurred to her that she ought to have
wondered at this, but at the time it all seemed quite natural);
but when the Rabbit actually TOOK A WATCH OUT OF ITS WAISTCOAT-
POCKET, and looked at it, and then hurried on, Alice started to
her feet, for it flashed across her mind that she had never
before seen a rabbit with either a waistcoat-pocket, or a watch to
take out of it, and burning with curiosity, she ran across the
field after it, and fortunately was just in time to see it pop
down a large rabbit-hole under the hedge.
'''

# case-sensitive
print("rabbit:")
rx_rabbit = re.compile(r'\brabbit\b')
print(rx_rabbit.findall(alice_text), '\n')

# case-insensitive
print("rabbit (ignore case):")
rx_rabbit_ic = re.compile(r'\brabbit\b', re.IGNORECASE)   # shortcut is re.I
print(rx_rabbit_ic.findall(alice_text), '\n')

# match "t" at beginning of string
print("t at beginning")
rx_begin_with_t = re.compile(r'^t', re.I)
for match_text in rx_begin_with_t.findall(alice_text):
    print(match_text)
print()

# match "t" at beginning of embedded_lines
print("t at beginning")
rx_lines_begin_with_t = re.compile(r'^t.*\n', re.M | re.I)
for match_text in rx_lines_begin_with_t.findall(alice_text):
    print(match_text, end=' ')
print()

