#!/usr/bin/env python

pythons = { 'Idle', 'Chapman', 'Cleese', 'Palin' }
fawlty = { 'Cleese', 'Booth', 'Scales' }

pythons.add('Jones')
pythons.add('Gilliam')
print("pythons", pythons)
print("fawlty", fawlty)
print("pythons & fawlty", pythons & fawlty)
print("pythons | fawlty", pythons | fawlty)
print("pythons ^ fawlty", pythons ^ fawlty)
print("pythons - fawlty", pythons - fawlty)

