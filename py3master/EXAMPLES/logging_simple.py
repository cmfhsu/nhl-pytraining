#!/usr/bin/env python
import logging

logging.basicConfig(
    filename='../TEMP/simple.log',
    level=logging.WARNING,
)

logging.warning('This message will be logged')
