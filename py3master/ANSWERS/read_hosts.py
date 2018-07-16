#!/usr/bin/env python

import re

rx_empty_or_whitespace = re.compile( r"^\s*$" )

addr_info_for = {}

with open( '../DATA/hosts' ) as HOSTS:
    for line in HOSTS:
        if rx_empty_or_whitespace.search( line ):
            continue
        if line.startswith( '#' ):
            continue

        flds = line[:-1].split()
        if len( flds ) == 2:
            others = ''
        else:
            others = ','.join(flds[2:] )

        addr_info_for[flds[1]] = [flds[0],others]

print("Host       IP               Aliases")
print("=" * 60)
for host,info in sorted(addr_info_for.items()):
    print(("{0:10s} {1[0]:15s} {1[1]}".format(host,info)))
