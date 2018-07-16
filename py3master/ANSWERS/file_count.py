#!/usr/bin/env python
"""

@author: jstrick
Created on Thu Mar 21 00:26:40 2013

"""
import sys
import logging
import os

logging.basicConfig(
    filename='file_count.log',
    level=logging.INFO,
    filemode='w', # create new log each time program is run
)

start_dir = sys.argv[1]

for curr_dir, dir_list, file_list in os.walk(start_dir):
    message = '{0}: {1}'.format(curr_dir,len(file_list))
    logging.info(message)

