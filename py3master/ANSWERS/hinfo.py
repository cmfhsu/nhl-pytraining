#!/usr/bin/env python
# one data record:
# aquila:Solaris:10:Sparc:elx0/11.1.3.10;elx0/11.1.14.37:200000:4096:Porky Pig

FIELD_NAMES = [
    'OS',
    'OS_VERSION',
    'ARCHITECTURE',
    'NET_IFACE',
    'HARD_DRIVES',
    'MEMORY',
    'USER',
]

host_info = {}

with open('../DATA/systems.dat') as systems_in:
    for rec in systems_in:
        fields = rec[:-1].split(':')
        host_name = fields[0]
        fields[4] = fields[4].split(';')
        fields[5] = fields[5].split(',')
        host_info[host_name] = dict(zip(FIELD_NAMES, fields[1:]))

output_format = '\t{0:25s} {1}'
while True:
    hostname = input("Enter host name or q to quit: ")
    if hostname.lower() == 'q':
        break
    if hostname == '':
        continue

    if hostname in host_info:
        print((hostname + ':'))
        h = host_info[hostname]
        print(output_format.format('Operating System',h['OS']))
        print(output_format.format('OS Version',h['OS_VERSION']))
        print(output_format.format('Architecture',h['ARCHITECTURE']))
        print(output_format.format('Network Interfaces',' '.join(h['NET_IFACE'])))
        print(output_format.format('Hard Drives',', '.join(h['HARD_DRIVES'])))
        print(output_format.format('Memory (GB)',h['MEMORY']))
        print(output_format.format('User',h['USER']))
        print()
    else:
        print("Sorry, that host does not exist\n")
