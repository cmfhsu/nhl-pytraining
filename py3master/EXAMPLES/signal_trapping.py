#!/usr/bin/env python
"""

@author: jstrick
Created on Sun Mar 17 22:14:46 2013

"""
import sys
import signal
import time

def SIGINT_handler(signal_to_handle, stack_frame):
    print('Ouch!')

def SIGQUIT_handler(signal_to_handle, stack_frame):
    print('OK, I give up')
    sys.exit(0)

signal.signal(signal.SIGINT, SIGINT_handler)
signal.signal(signal.SIGQUIT, SIGQUIT_handler)

for i in range(100):
    print(".")
    time.sleep(1)

