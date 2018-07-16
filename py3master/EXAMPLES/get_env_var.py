#!/usr/bin/env python
import sys
import os

if sys.platform == 'win32':
    print("Path extensions are:",os.environ.get('PATHEXT'))
else:
    print("Login name is", os.environ.get('LOGNAME'))
