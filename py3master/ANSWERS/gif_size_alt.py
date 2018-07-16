#!/usr/bin/env python
"""

@author: jstrick
Created on Tue Mar 19 17:26:07 2013

"""
import sys

gif_file_name = sys.argv[1]
with open(gif_file_name, 'rb') as gif_file:
    data = gif_file.read()

if data[:3] == b'GIF':
    # data is an array of BYTES, not CHARACTERS
    height = data[6] + data[7] * 256
    width = data[8] + data[9] * 256
else:
    print("Not a GIF file")

print("{0}x{1}".format(height,width))
