#!/usr/bin/env python
"""

@author: jstrick
Created on Wed Mar 20 21:39:34 2013

"""
import glob
import shutil

files_to_copy = glob.iglob('../DATA/*.csv')

for file_to_copy in files_to_copy:
    shutil.copy(file_to_copy, '../TEMP')