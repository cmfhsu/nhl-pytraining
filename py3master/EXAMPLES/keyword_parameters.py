#!/usr/bin/env python

def set_position(*, latitude=None, longitude=None):
    print("Latitude is {}, Longitude is {}".format(latitude, longitude))

# both latitude and longitude must be specified
set_position(latitude=36.011852, longitude=-78.928335)
set_position(longitude=-78.928335, latitude=36.011852)
print()

def logger_config(**config):
    for name, value in config.items():
        print(name, value)

logger_config(filename='mystuff.log', log_folder='/var/log', max_entries=5)
print()
logger_config(filename='mystuff.log', max_entries=5)
