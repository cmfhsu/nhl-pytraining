#!/usr/bin/env python
import sys
import re
import os

rx_print = re.compile(r'^\s*print\(\((?P<PAYLOAD>.*?)\)\)$', re.MULTILINE | re.DOTALL)

def do_replacement(m):
    payload = m.group('PAYLOAD')
    replacement = 'print({})'.format(payload)
    return replacement

for i, file_name in enumerate(sys.argv[1:], 1):
    with open(file_name) as file_in:
        contents = file_in.read()

    new_contents = rx_print.sub(do_replacement, contents)

    os.rename(file_name, file_name + '.BAK')

    with open(file_name, 'w') as file_out:
        file_out.write(new_contents)
