#!/usr/bin/env python
"""

@author: jstrick
Created on Tue Mar 19 17:26:07 2013

"""
import sys
from struct import unpack

gif_file_name = sys.argv[1]
with open(gif_file_name, 'rb') as gif_file:
    data = gif_file.read()

if data[:3] == b'GIF':
    height_bytes = data[6:8]
    width_bytes = data[8:10]
    height = unpack('h',height_bytes)
    width = unpack('h', width_bytes)
    print('{0}x{1}'.format(height[0], width[0]))
else:
    print("Not a GIF file")

# print "{0}x{1}".format(height,width)
